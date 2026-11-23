"""Closure (one-time): does any remaining screen-icon artwork already exist in the icon library (src/icons/svg)?

Each staged Figma SVG (exported for the closure; %TEMP%/annachy-closure-staging/assets) and every library SVG is rasterised
by Chrome, cropped to its ink, normalised to 48 x 48 (aspect kept, centred) and thresholded to a mask. For each staged
artwork the best library candidates by IoU are reported. A library icon is treated as an EXACT match only at IoU >= 0.97
(and is then confirmed visually); anything below is not reused. Output: docs/replication/closure-icon-match.json
    python -I tests/tools/closure_icon_match.py
"""
import glob, json, os, sys
sys.dont_write_bytecode = True; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
from cdp_lib import Harness

ST = os.path.join(os.environ["TEMP"], "annachy-closure-staging", "assets")
staged = {os.path.basename(f): open(f, encoding="utf-8").read() for f in sorted(glob.glob(os.path.join(ST, "*.svg")))}
lib = sorted(f.replace(os.sep, "/") for f in glob.glob("src/icons/svg/*/*.svg"))
H = Harness(800, 600)
H.navigate("tests/fixtures/r7-icon-fidelity-stage.html")
H.ev("""window.SIG = async (src) => { const img = new Image(); img.src = src; await img.decode();
  const N = 192, c = document.createElement('canvas'); c.width = c.height = N; const g = c.getContext('2d', { willReadFrequently: true });
  const s = N / Math.max(img.naturalWidth || 24, img.naturalHeight || 24); g.drawImage(img, 0, 0, (img.naturalWidth || 24) * s, (img.naturalHeight || 24) * s);
  const d = g.getImageData(0, 0, N, N).data; let x0 = N, y0 = N, x1 = -1, y1 = -1;
  for (let y = 0; y < N; y++) for (let x = 0; x < N; x++) if (d[(y * N + x) * 4 + 3] > 64) { if (x < x0) x0 = x; if (x > x1) x1 = x; if (y < y0) y0 = y; if (y > y1) y1 = y; }
  if (x1 < 0) return null; const w = x1 - x0 + 1, h = y1 - y0 + 1, M = 48, k = M / Math.max(w, h), ox = (M - w * k) / 2, oy = (M - h * k) / 2;
  const c2 = document.createElement('canvas'); c2.width = c2.height = M; const g2 = c2.getContext('2d', { willReadFrequently: true });
  g2.drawImage(c, x0, y0, w, h, ox, oy, w * k, h * k); const e = g2.getImageData(0, 0, M, M).data; const bits = new Uint8Array(M * M);
  for (let i = 0; i < M * M; i++) bits[i] = e[i * 4 + 3] > 96 ? 1 : 0; return { bits, aspect: w / h }; };
  window.LIB = []; true""")
B = 200
for i in range(0, len(lib), B):
    H.ev(f"""(async () => {{ for (const f of {json.dumps(lib[i:i + B])}) {{ try {{ const s = await SIG('/' + f); if (s) LIB.push([f, s]); }} catch (e) {{}} }} return LIB.length; }})()""")
print("library signatures:", H.ev("LIB.length"))
out = {}
for name, text in staged.items():
    res = H.ev(f"""(async () => {{ const s = await SIG('data:image/svg+xml;charset=utf-8,' + encodeURIComponent({json.dumps(text)})); if (!s) return null;
      const r = []; for (const [f, t] of LIB) {{ if (Math.abs(Math.log(t.aspect / s.aspect)) > 0.08) continue; let a = 0, u = 0;
        for (let i = 0; i < s.bits.length; i++) {{ const p = s.bits[i], q = t.bits[i]; a += p & q; u += p | q; }} r.push([f, u ? a / u : 0]); }}
      r.sort((x, y) => y[1] - x[1]); return r.slice(0, 3); }})()""")
    out[name] = res
    best = res[0] if res else None
    print(f"{name}: {('%.3f %s' % (best[1], best[0])) if best else 'no ink'}")
H.close()
json.dump(out, open("docs/replication/closure-icon-match.json", "w", encoding="utf-8"), indent=1)

"""Rend des artboards Design Hanamisé (.dc.html) en images Instagram 1080x1350.

Usage :
    python3 tools/render.py DOSSIER_SORTIE fichier1.dc.html [fichier2.dc.html ...]

- Chaque /_blob/<id> du fichier doit être listé dans assets/blobs.json
  (id -> nom de fichier dans assets/). Ajoutez-y tout nouvel asset.
- Les polices Anton, Montserrat et Cormorant Garamond viennent du dépôt
  github.com/google/fonts (clone partiel dans /tmp/gfonts au premier lancement).
  Noto Sans JP est remplacée par Noto Sans CJK JP, installée sur la machine.
- Produit <nom>.png et <nom>.jpg (qualité 85) pour chaque fichier.
"""
import glob
import json
import re
import subprocess
import sys
from pathlib import Path

from PIL import Image
from playwright.sync_api import sync_playwright

REPO = Path(__file__).resolve().parent.parent
ASSETS = REPO / "assets"
GF = Path("/tmp/gfonts")
F = GF / "ofl"


def ensure_fonts():
    if (F / "anton" / "Anton-Regular.ttf").exists():
        return
    subprocess.run(["rm", "-rf", str(GF)], check=True)
    subprocess.run(["git", "clone", "--depth", "1", "--filter=blob:none", "--sparse",
                    "https://github.com/google/fonts", str(GF)], check=True)
    subprocess.run(["git", "-C", str(GF), "sparse-checkout", "set",
                    "ofl/anton", "ofl/montserrat", "ofl/cormorantgaramond"], check=True)


def font_css():
    return f"""
@font-face{{font-family:'Anton';src:url('file://{F}/anton/Anton-Regular.ttf');font-weight:400}}
@font-face{{font-family:'Montserrat';src:url('file://{F}/montserrat/Montserrat[wght].ttf');font-weight:100 900}}
@font-face{{font-family:'Montserrat';src:url('file://{F}/montserrat/Montserrat-Italic[wght].ttf');font-style:italic;font-weight:100 900}}
@font-face{{font-family:'Cormorant Garamond';src:url('file://{F}/cormorantgaramond/CormorantGaramond[wght].ttf');font-weight:300 700}}
@font-face{{font-family:'Cormorant Garamond';src:url('file://{F}/cormorantgaramond/CormorantGaramond-Italic[wght].ttf');font-style:italic;font-weight:300 700}}
@font-face{{font-family:'Noto Sans JP';src:local('Noto Sans CJK JP Black'),local('NotoSansCJKjp-Black');font-weight:800 900}}
@font-face{{font-family:'Noto Sans JP';src:local('Noto Sans CJK JP Bold'),local('NotoSansCJKjp-Bold'),local('Noto Sans CJK JP Black');font-weight:600 700}}
@font-face{{font-family:'Noto Sans JP';src:local('Noto Sans CJK JP'),local('NotoSansCJKjp-Regular');font-weight:100 500}}
"""


def standalone(src: str, blobs: dict) -> str:
    helmet = re.search(r"<helmet>(.*?)</helmet>", src, re.S).group(1)
    styles = "".join(re.findall(r"<style>(.*?)</style>", helmet, re.S))
    body = re.search(r"</helmet>(.*?)</x-dc>", src, re.S).group(1)
    html = ("<!doctype html><html lang='fr'><head><meta charset='utf-8'><style>"
            + font_css() + styles + "</style></head><body>" + body + "</body></html>")
    for blob, name in blobs.items():
        html = html.replace(f"/_blob/{blob}", f"file://{ASSETS / name}")
    left = sorted(set(re.findall(r"/_blob/[0-9a-f]+", html)))
    if left:
        raise SystemExit(f"Assets absents de assets/blobs.json : {left}")
    return html


def main():
    out = Path(sys.argv[1]).resolve()
    files = [Path(p).resolve() for p in sys.argv[2:]]
    out.mkdir(parents=True, exist_ok=True)
    ensure_fonts()
    blobs = json.loads((ASSETS / "blobs.json").read_text())
    chrome = sorted(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome"))
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=chrome[-1] if chrome else None)
        page = browser.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
        for f in files:
            name = f.name.replace(".dc.html", "")
            tmp = out / f"{name}.render.html"
            tmp.write_text(standalone(f.read_text(), blobs))
            page.goto(f"file://{tmp}")
            page.evaluate("document.fonts.ready")
            page.wait_for_timeout(400)
            png = out / f"{name}.png"
            page.screenshot(path=str(png), clip={"x": 0, "y": 0, "width": 1080, "height": 1350})
            Image.open(png).convert("RGB").save(out / f"{name}.jpg", quality=85, optimize=True, progressive=True)
            tmp.unlink()
            print("ok", out / f"{name}.jpg")
        browser.close()


if __name__ == "__main__":
    main()

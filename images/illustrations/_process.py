"""
Process the 5 Higgsfield mountain illustrations:
- For ones with white backgrounds (helping-hand, team-overlook, route-marker): remove white -> transparent
- For ones with seafoam background as design (roped-team, summit-flag): keep as-is, just downscale + optimise
- Write rounded web-ready PNGs at 2x and 1x sizes
"""
from PIL import Image
from pathlib import Path

D = Path(r"C:\Users\robid\Desktop\Aventario Claude\website\images\illustrations")
WHITE_THRESHOLD = 240  # pixels with all RGB above this become transparent
FUZZ = 18              # tolerance band for partial transparency on near-white pixels

def make_white_transparent(src: Path, out: Path):
    im = Image.open(src).convert("RGBA")
    px = im.load()
    w, h = im.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            mn = min(r, g, b)
            if mn >= WHITE_THRESHOLD:
                # Full transparent if very white, partial if near-white (smoother edges)
                if mn >= 252:
                    px[x, y] = (r, g, b, 0)
                else:
                    # gradient transparency
                    a2 = int((WHITE_THRESHOLD + FUZZ - mn) / FUZZ * 255)
                    px[x, y] = (r, g, b, max(0, min(a2, 255)))
    im.save(out, "PNG", optimize=True)
    print(f"  -> {out.name}  ({im.size[0]}x{im.size[1]})")

def downscale(src: Path, out: Path, max_w: int):
    im = Image.open(src).convert("RGBA")
    if im.size[0] > max_w:
        im.thumbnail((max_w, max_w * 4), Image.LANCZOS)
    im.save(out, "PNG", optimize=True)
    print(f"  -> {out.name}  ({im.size[0]}x{im.size[1]})")

# Cutout (white bg -> transparent)
for name in ["helping-hand", "team-overlook", "route-marker"]:
    src = D / f"{name}-raw.png"
    if not src.exists():
        print(f"skip {name}: no raw")
        continue
    print(f"\n{name}: white bg -> transparent")
    tmp = D / f"{name}-cutout.png"
    make_white_transparent(src, tmp)
    # Two web sizes
    downscale(tmp, D / f"{name}.png", 1200)
    downscale(tmp, D / f"{name}-sm.png", 600)
    tmp.unlink()

# Keep-bg illustrations (the colored bg is part of the design)
for name in ["roped-team", "summit-flag"]:
    src = D / f"{name}-raw.png"
    if not src.exists():
        print(f"skip {name}: no raw")
        continue
    print(f"\n{name}: keep bg (design integral)")
    downscale(src, D / f"{name}.png", 1200)
    downscale(src, D / f"{name}-sm.png", 600)

print("\nDone.")

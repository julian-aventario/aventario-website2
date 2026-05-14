"""
One-shot site-wide footer fix.

Issue: the SUBSCRIBE NOW button in the Monthly Newsletter card wraps onto two
lines because the right-side promo column is too narrow.

Fix:
  1. Re-balance the 12-col footer grid so the right promo cards get more room:
     Brand:        col-span-3  ->  col-span-2  (it has space)
     Right cards:  col-span-3  ->  col-span-4
     Link columns stay at col-span-2 each.
  2. Add `whitespace-nowrap` to the SUBSCRIBE NOW button so the text never wraps.

Applies to every .html file that has the Monthly Newsletter footer block.
Idempotent: running it twice is a no-op.
"""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).parent
MARKER = "Monthly Newsletter"

# Three precise replacements. We require the exact match so we never change
# anything outside the intended footer block.

REPLACEMENTS = [
    # 1. Brand column: col-span-3 -> col-span-2
    #    Only catches the brand-block container right above the footer.
    (
        '<!-- Brand + contact (left block) -->\n                    <div class="lg:col-span-3">',
        '<!-- Brand + contact (left block) -->\n                    <div class="lg:col-span-2">',
    ),
    # 2. Right promo cards column: col-span-3 -> col-span-4
    (
        '<!-- Right-side promo cards: managedsuppliers + newsletter -->\n                    <div class="lg:col-span-3 space-y-4">',
        '<!-- Right-side promo cards: managedsuppliers + newsletter -->\n                    <div class="lg:col-span-4 space-y-4">',
    ),
    # 3. SUBSCRIBE NOW button: never wrap
    (
        '<button type="submit" class="text-xs font-bold uppercase tracking-widest px-4 py-2 rounded-full"',
        '<button type="submit" class="text-xs font-bold uppercase tracking-widest whitespace-nowrap px-4 py-2 rounded-full"',
    ),
]


def fix_file(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if MARKER not in text:
        return {"path": path, "skipped": True, "reason": "no footer marker"}

    applied = []
    new = text
    for old, repl in REPLACEMENTS:
        if old in new:
            new = new.replace(old, repl)
            applied.append(old[:60] + "...")
        elif repl in new:
            applied.append("(already fixed)")
        else:
            applied.append("(pattern not found)")

    if new == text:
        return {"path": path, "skipped": True, "reason": "already fixed or pattern not found", "applied": applied}

    path.write_text(new, encoding="utf-8")
    return {"path": path, "changed": True, "applied": applied}


def main():
    files = sorted(ROOT.rglob("*.html"))
    files = [f for f in files if "node_modules" not in str(f) and ".vercel" not in str(f)]

    changed = 0
    skipped = 0
    not_applicable = 0

    for f in files:
        result = fix_file(f)
        rel = f.relative_to(ROOT)
        if result.get("changed"):
            changed += 1
            print(f"  FIXED  {rel}")
        elif result.get("skipped") and "no footer marker" in result.get("reason", ""):
            not_applicable += 1
        else:
            skipped += 1
            print(f"  SKIP   {rel} ({result.get('reason')})")

    print()
    print(f"Total HTML files scanned: {len(files)}")
    print(f"Footer fix applied:       {changed}")
    print(f"Already fixed / skipped:  {skipped}")
    print(f"No newsletter footer:     {not_applicable}")


if __name__ == "__main__":
    main()

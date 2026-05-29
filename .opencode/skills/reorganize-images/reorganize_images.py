"""
Reorganize images in markdown files from flat layout to Obsidian nested layout.

Flat layout (current):      assets/笔记名-1.png
Obsidian layout (target):   assets/笔记名/笔记名-1.png

Usage:
    python reorganize_images.py --dry-run              # Preview only
    python reorganize_images.py                        # Apply changes
    python reorganize_images.py --path <project_root>  # Specify root
"""

import os
import re
import shutil
import argparse
from pathlib import Path
from collections import defaultdict


EXCLUDE_DIRS = {'.git', '.opencode', '__pycache__', 'node_modules', '.obsidian'}
EXCLUDE_PATH_PREFIXES = {'.git', '.opencode', '示例'}


def find_md_files(root_dir):
    md_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
        rel = os.path.relpath(dirpath, root_dir).replace('\\', '/')
        if any(rel == p or rel.startswith(p + '/') for p in EXCLUDE_PATH_PREFIXES):
            continue
        for f in filenames:
            if f.endswith('.md'):
                md_files.append(os.path.join(dirpath, f))
    return sorted(md_files)


def extract_image_refs(content):
    pattern = r'!\[.*?\]\((assets/[^)]+)\)'
    return [(m.group(0), m.group(1)) for m in re.finditer(pattern, content)]


def is_already_nested(img_path):
    parts = img_path.replace('\\', '/').split('/')
    return len(parts) > 2


def main():
    parser = argparse.ArgumentParser(description='Reorganize images to Obsidian nested layout')
    parser.add_argument('--dry-run', action='store_true', help='Preview only')
    parser.add_argument('-y', '--yes', action='store_true', help='Skip confirmation')
    parser.add_argument('--path', default='.', help='Project root (default: current dir)')
    args = parser.parse_args()

    root = os.path.abspath(args.path)
    md_files = find_md_files(root)
    print(f"Found {len(md_files)} markdown file(s)")

    all_changes = []
    for md_path in md_files:
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()
        refs = extract_image_refs(content)
        if not refs:
            continue
        md_dir = os.path.dirname(md_path)
        md_name = Path(md_path).stem
        for full_match, img_path in refs:
            if is_already_nested(img_path):
                continue
            img_file = os.path.basename(img_path)
            new_img_rel = f'assets/{md_name}/{img_file}'
            old_abs = os.path.normpath(os.path.join(md_dir, img_path))
            new_abs = os.path.normpath(os.path.join(md_dir, new_img_rel))
            all_changes.append({
                'md': md_path,
                'old_ref': img_path,
                'new_ref': new_img_rel,
                'old_abs': old_abs,
                'new_abs': new_abs,
                'full_match': full_match,
            })

    if not all_changes:
        print("No images need reorganization.")
        return

    by_md = defaultdict(list)
    for c in all_changes:
        by_md[c['md']].append(c)

    print(f"Found {len(all_changes)} image(s) to reorganize:\n")
    for md_file, clist in sorted(by_md.items()):
        print(f"  {os.path.relpath(md_file, root)}")
        for c in clist:
            print(f"    {c['old_ref']}  ->  {c['new_ref']}")

    if args.dry_run:
        print(f"\n[DRY RUN] No changes made. Run without --dry-run to apply.")
        return

    if not args.yes:
        try:
            resp = input(f"\nApply {len(all_changes)} change(s)? [y/N] ").strip().lower()
            if resp != 'y':
                print("Cancelled.")
                return
        except (EOFError, KeyboardInterrupt):
            print("\nCancelled.")
            return

    for md_path, clist in by_md.items():
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()
        for c in clist:
            content = content.replace(
                c['full_match'],
                c['full_match'].replace(c['old_ref'], c['new_ref'])
            )
            os.makedirs(os.path.dirname(c['new_abs']), exist_ok=True)
            if os.path.exists(c['old_abs']):
                shutil.move(c['old_abs'], c['new_abs'])
                print(f"  Moved: {os.path.relpath(c['old_abs'], root)} -> {os.path.relpath(c['new_abs'], root)}")
            else:
                print(f"  Warning: not found {os.path.relpath(c['old_abs'], root)} (reference still updated)")
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(content)

    print(f"\nDone! {len(all_changes)} image(s) reorganized.")


if __name__ == '__main__':
    main()

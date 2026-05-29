---
name: reorganize-images
description: >-
  Use when the user says "按照Obsidian格式整理图片路径".
  Converts flat assets/ layout (assets/foo-1.png) to Obsidian nested layout
  (assets/foo/foo-1.png) and updates all markdown references.
  Run --dry-run first to preview, then again without it to apply.
---

# 按照Obsidian格式整理图片路径

将 Markdown 笔记中的图片从扁平布局转换为 Obsidian 风格的嵌套布局。

## 转换规则

| 项目 | 说明 |
|------|------|
| **旧格式** | `assets/笔记名-1.png` — 所有图片平铺在 `assets/` 下 |
| **新格式** | `assets/笔记名/笔记名-1.png` — 每个笔记的图片放入独立子目录 |
| **文件名** | 保持不变，只改变目录结构 |
| **支持格式** | `.png`, `.jpeg`, `.jpg`, `.webp` |

## 使用方法

```powershell
# 第一步：预览变更（不实际修改）
python .opencode\skills\reorganize-images\reorganize_images.py --dry-run

# 第二步：确认后执行
python .opencode\skills\reorganize-images\reorganize_images.py
```

## 安全措施

- 自动跳过 `.git/`、`.opencode/`、`示例/` 目录
- 已符合 Obsidian 格式的图片不会重复处理
- `--dry-run` 预览模式，零风险检查

## 项目根目录指定

如果不在项目根目录执行，使用 `--path` 参数：

```powershell
python .opencode\skills\reorganize-images\reorganize_images.py --path D:\zp-note-book\zp-python-note --dry-run
python .opencode\skills\reorganize-images\reorganize_images.py --path D:\zp-note-book\zp-python-note
```

# zp-it-lecture-writer

## Purpose
用于编写 IT 讲义（Markdown）并在正文最终稿阶段生成封面图。

## Trigger
- 显式触发：`$zp-it-lecture-writer`
- 自然触发：`编写IT讲义`、`写讲义`、`生成讲义`

## Hard Rules
1. 仅输出 Markdown。
2. 先输出大纲，再等用户确认后输出正文。
3. 大纲必须到 `###`，每个 `###` 下 2-4 条要点。
4. 每个 `##` 节必须包含：
   - 1 条风险提醒
   - 1 条考试/面试易错点
   - 本节小结
5. 正文阶段必须包含可验证结果（输出、现象或检查点）。
6. 默认示例语言为 Python。
   - 调用时先做可选确认。
   - 若用户不回复，则按 Python 继续。

## Lecture Writing Style Baseline
1. 结构：`#` 章 -> `##` 节 -> `###` 小节，不跳级。
2. 叙述顺序：概念定义 -> 场景动机 -> 步骤操作 -> 示例代码 -> 结果验证 -> 常见问题。
3. 表达风格：课堂讲解式，直接、分步、可执行。
4. 操作描述：使用编号步骤（`1). 2). 3).`）。
5. 参数/对比内容：优先表格。
6. 每个关键知识点至少 1 个代码块，必须带语言标识。
7. 每节练习：基础题、进阶题、排错题各至少 1 题。

## Cover Generation Rules
1. 仅在正文最终稿阶段生成封面，不在大纲阶段生成。
2. 使用 APIMart 的 GPT-Image-2 接口异步生成（严格轮询任务状态）。
3. 默认参数：
   - `n=1`
   - `size=16:9`
   - `resolution=2k`
4. 如果 `2k` 失败，自动降级到可用分辨率（脚本当前降到 `1k`）。
5. 失败自动重试 2 次。
6. 封面允许中文文字；不使用 Logo/水印。
7. 同一课程系列保持统一风格：
   - 首篇自动生成并固化 `style_profile`
   - 复用保存于 `data/style_profiles.json`

## Output Path Rules
以目标讲义文件 `X:\...\lesson.md` 为例：
- 输出目录：`X:\...\assets\lesson\`
- 封面文件：`X:\...\assets\lesson\cover.png`
- 若已存在 `cover.png`，先备份为 `cover.bak.png` 再覆盖。

## API Key Rules
1. 不修改 `C:\Users\Administrator\.gateway.env`。
2. 仅从该文件读取 `APIMART_API_KEY`。

## Script
封面生成脚本：
- `scripts/generate_cover.py`

常用调用示例：
```bash
python .codex/skills/zp-it-lecture-writer/scripts/generate_cover.py \
  --markdown "E:/develop/my_obsidian_note/zp-python-note/Python语法2025/python_code/demo.md" \
  --series "Python基础班"
```

可选参数：
- `--cover-text`：封面文字（可空）
- `--style-hint`：额外风格提示词
- `--poll-interval`：轮询间隔秒数（默认 4）
- `--timeout`：轮询超时秒数（默认 240）

## Project Preset (zp-python-note)
以下约束用于本仓库的“仿写/重写讲义”任务，除非用户明确覆盖，否则默认启用：

1. 代码素材范围：
   - 当用户提供代码目录时，仅提取与当前章节主题直接相关的代码文件。
   - 不要求覆盖目录内全部代码文件。

2. 目标受众：
   - 默认面向零基础初学者。
   - 讲解粒度以“能跟做、能看懂、能验证”为准。

3. 结构策略：
   - 基本沿用原讲义章节顺序增强。
   - 允许局部微调表述，但不做大幅重排。

4. 扩展内容：
   - 允许增加：课堂练习、面试题、排错题、常见坑清单、课后作业。
   - 扩展内容应服务于理解与实操，不做无关延展。

5. 验证要求：
   - 每个知识点都必须配“可验证结果”。
   - 可验证结果包含：运行输出、现象描述或可执行检查点。

6. 封面要求：
   - 在正文最终阶段必须生成封面图（遵循 Cover Generation Rules）。

7. 文件命名要求：
   - 若用户指定标题/文件名“严格使用”，则不得追加日期、版本号或其他后缀。

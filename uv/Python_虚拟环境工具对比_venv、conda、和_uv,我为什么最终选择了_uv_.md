如果你写 Python 写得足够久，一定遇到过这种情况：

-   同一个项目跑得好好的，突然另一个项目用的依赖把它“搞坏了”；
-   安装一个库，另一个库就炸了，版本互相冲突；
-   各种「Requirement already satisfied」，但程序还是跑不起来；
-   要上一个新项目，结果各种包冲突、环境配置花了半天...

这就是著名的 **“依赖地狱”**。而虚拟环境，就是解决它的终极武器。

-   还有就是，当从github上clone 一个项目安装，发现其依赖包巨大。`pip install` 的过程中，一个个下载，巨慢。

我从一开始用 `venv` 隔离简单项目，到后来用上 `mini[conda](https://zhida.zhihu.com/search?content_id=256519672&content_type=Article&match_order=1&q=conda&zhida_source=entity)` 来应对一些AI相关的任务，再到现在彻底迁移到 **uv**。这篇文章就带你一起看看我踩过的坑、用过的工具，以及为什么我强烈推荐你尝试一下 uv。

## 一、我用虚拟环境的经历

### venv ：最朴素的环境隔离方式

Python 自带的 `venv`，其实已经能满足不少轻量项目的需求，特别是我最开始写脚本、做简单工具的时候，它就足够用了。

比如在嵌入式开发中，[ESP32](https://zhida.zhihu.com/search?content_id=256519672&content_type=Article&match_order=1&q=ESP32&zhida_source=entity) 的 [IDF SDK](https://zhida.zhihu.com/search?content_id=256519672&content_type=Article&match_order=1&q=IDF+SDK&zhida_source=entity) 就是基于 `venv` 来做环境隔离的。你可以同时装多个不同版本的开发框架，互不影响。 用法非常简单：

```bash
# 创建虚拟环境
python -m venv venv
# 激活环境（Linux / macOS）
source venv/bin/activate
# Windows：
venv\Scripts\activate
# 退出环境
deactivate
```

它的优点是：

-   python自带，非常轻量

同时这也是它的缺点：

-   依赖于某个python版本。

当你的工程不支持这个版本时，就又要一番折腾。

### miniconda：AI领域更方便

后来，我开始涉及机器学习、LLM 等方向（是的，我不仅仅只做嵌入式），python版本经常要换，`venv` 就有点跟不上了。于是我转向了 `miniconda`。

```bash
conda create -n myenv python=3.10
conda activate myenv
```

[Miniconda](https://zhida.zhihu.com/search?content_id=256519672&content_type=Article&match_order=1&q=Miniconda&zhida_source=entity) 是 Anaconda 的轻量版，没有默认装一堆科学包。我更喜欢它干净、可控，再按需装库。

它的优点是：

-   解决了venv中python版本的问题。
-   管理的不只是 Python 包，还能管理 Python 本身和系统级依赖（如 C 库、R 语言）。
-   适用于科学计算、数据分析领域。圈子里的README都推荐用它。

但它也有缺点：

-   创建和激活环境速度较慢。
-   当做了一堆项目，创建了一堆环境后，记忆会很痛苦。
-   会改写 `.bashrc` 自动加载 base 环境，有时会导致莫名其妙的问题。（比如不小心就pip install了啥，强迫症也见不得命令行前面加一个符号）

### ⚡️uv：现代感爆棚的 Python 包管理工具

从 2024 年底我开始尝试使用 `[uv](https://link.zhihu.com/?target=https%3A//github.com/astral-sh/uv)`，现在我所有的新项目都迁移到了它上面。它像是 nodejs的 `npm`，或者 [Rust](https://zhida.zhihu.com/search?content_id=256519672&content_type=Article&match_order=1&q=Rust&zhida_source=entity) 的 `cargo`，在很多方面都碾压传统方案。

### *两种使用方式：*

1.  **传统方式**（兼容 venv）：

```bash
uv venv myenv --python=3.10
source myenv/bin/activate
uv pip install numpy
```

这就像是 venv + pip 的加速版，适合脚本或已有项目。

1.  **推荐方式：project 模式（类似nodejs 的 npm）**

```bash
uv init             # 初始化项目（生成 pyproject.toml）
uv add numpy        # 安装依赖并自动写入配置文件
uv run main.py      # 自动激活环境 + 运行代码
```

执行 `uv run` 时，uv 会自动创建 `.venv` 文件夹，读取 `pyproject.toml` 和 `[uv.lock](https://zhida.zhihu.com/search?content_id=256519672&content_type=Article&match_order=1&q=uv.lock&zhida_source=entity)`，同步依赖并运行程序。 你甚至可以：

```bash
uv add -r requirements.txt  # 从传统依赖列表迁移
```

这种模式，完美的和现有的工程进行融合。从创建到最后的build都包含了。

除了project外，也提供了`tool` 的方式，让我们在安装和运行命令行程序时，做到较好的隔离。比如 `uv tool install --python 3.12 pdf2zh` 就可以一键安装pdf的翻译工具。独立的依赖，不会因为我电脑上的环境导致问题。

### *为什么我喜欢它？*

-   **快！** 使用rust编写，安装依赖是并行的，比 pip 和 conda 都快；
-   **现代！** 项目结构清晰，依赖写在 `pyproject.toml` ，最后锁定在lock文件中；
-   **轻！** 删除 `.venv` 文件夹就等于删掉环境；
-   **干净！** 不污染系统，不自动写配置，不乱改 `.bashrc`；

## 二、三者对比分析

| **特性** | **venv** | **Conda (Miniconda)** | **uv (推荐 project 模式)** |
| --- | --- | --- | --- |
| 是否内置 | ✅ 是 | ❌（需安装） | ❌（需安装） |
| 安装方式 | Python 自带 | 官网下载安装（推荐 Miniconda） | pip install uv |
| 环境创建速度 | ✅ 快 | ❌ 慢 | 超快（并行） |
| 占用空间 | ✅ 小 | ❌ 大 | ✅ 小 |
| 依赖管理 | 手动 requirements.txt | conda + pip | ✅ pyproject.toml + uv.lock |
| 项目初始化 | ❌ 无 | ❌ 无 | ✅ uv init 一键结构化 |
| 源支持 | 使用 pip 镜像 | 使用 Conda 自有源 | 使用 pip 镜像 |
| 非 Python 包支持 | ❌ | ✅（如 cudatoolkit） | ❌ |
| 适合场景 | 脚本 / 嵌入式工具链 | 数据科学 / 科研项目 | 所有项目，特别是现代开发 |

## 三、为什么我现在只用 uv？

直到我用了 uv，我才发现：  
**“原来 Python 项目也可以像前端一样，有现代开发体验。”**

以下是我彻底迁移到 uv 的原因：

### 1. **速度不是快一点，是快几倍**

uv 本身是用 Rust 写的，所有 pip 安装的操作都会**并行处理**，特别是当依赖比较多时，体验是断崖式领先。

pip 是串行安装，uv 是并发安装，差距非常明显。 比如我有一个项目依赖 30 多个库，用 pip 安装需要 1-2 分钟，用 uv **10 秒内就搞定**。

### 2. **项目就是环境，结构天然清晰**

uv 的推荐模式是以项目为中心的，类似 `npm` 的体验：

```bash
uv init
uv add flask
uv run app.py
```

一切都写在 `pyproject.toml`，你不再需要手动维护 `requirements.txt`，也不需要关心激活哪个环境、有没有冲突 —— **因为环境就是项目自己管理的** `**.venv**` **文件夹。** 更棒的是，你只要把项目文件夹打包发给别人，对方：

```bash
git clone ...
uv sync
```

就能 100% 还原运行环境。**这比 pip + venv 要靠谱太多了。**

### 3. **从“工具链散装”到“一条龙集成”**

传统 Python 开发中，你可能要用这些工具配合：

-   venv 创建环境
-   pip 装包
-   requirements.txt 管依赖
-   手动处理依赖冲突
-   virtualenvwrapper 管多项目
-   [pip-tools](https://zhida.zhihu.com/search?content_id=256519672&content_type=Article&match_order=1&q=pip-tools&zhida_source=entity) 锁依赖

uv 把这些功能都整合成一体，统一通过 `pyproject.toml + uv.lock` 管理。 这种**集中式管理方式**极大提升了我开发的专注度：我不再分神在环境配置上，只专注写业务逻辑。

### 4. **删除项目=删除环境，干净利落**

用 Conda 时，我经常忘了删不用的环境，堆了一堆 `base`, `env-1`, `env-2`… 用 venv 时，不小心激活了错的环境，程序就会报奇怪的错。 而 uv 把虚拟环境放在 `.venv`，你只要：

```bash
rm -rf .venv
```

就彻底清掉这个环境，**没有任何污染，不动系统，不乱写配置文件。**

### 5. **工具链现代化，更适合团队和持续集成**

uv 对 `pyproject.toml` 的支持非常好，意味着你可以和：

-   `ruff`, `black`, `pytest`, `mypy`
-   `pre-commit`, `poetry`, `setuptools`

这些现代工具配合使用，**统一配置、统一管理**，为团队协作和 CI/CD 提供天然支持。

## 四、总结一句话：

conda 很稳，venv 很轻，但 uv —— 又轻、又快、还酷。 如果你追求轻量、极速、现代化的 Python 开发体验，不妨现在就试试 `uv`，你一定会爱上它。
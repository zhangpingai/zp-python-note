### 使用uv管理环境

```bash
# 创建项目（已初始化）
uv init --python 3.12

# 安装依赖
uv sync

# 安装新包
uv add <package>

# 安装开发依赖
uv add --dev <package>

# 激活虚拟环境（Windows）
.venv\Scripts\activate

# 激活虚拟环境（Linux/Mac）
source .venv/bin/activate

# 查看已安装的包
uv pip list

# 运行Python脚本
uv run python script.py

# 运行Flask应用
uv run python run.py
```

### 依赖管理

-   使用`pyproject.toml`管理所有依赖
-   生产依赖自动添加到主依赖列表
-   开发依赖使用`--dev`标记
-   uv自动管理虚拟环境，无需手动创建

### 常用uv命令

```bash
# 检查uv版本
uv --version

# 查看Python版本
uv python list

# 添加Flask相关依赖
uv add flask flask-sqlalchemy flask-migrate

# 添加开发工具
uv add --dev black isort flake8 pytest

# 更新依赖
uv sync

# 运行应用
uv run python app.py
```

## 常用Flask命令

```bash
# 启动开发服务器
uv run flask run

# 启动Flask shell
uv run flask shell

# 数据库迁移
uv run flask db init          # 初始化迁移
uv run flask db migrate -m "message"  # 创建迁移
uv run flask db upgrade       # 应用迁移

# 查看路由
uv run flask routes

# 运行测试
uv run pytest
```

### 代码格式化

```bash
# 格式化代码
uv run black .

# 检查格式
uv run black --check .

# 排序导入
uv run isort .

# 检查导入排序
uv run isort --check-only .
```

### 代码检查

```bash
# 使用flake8检查代码风格
uv run flake8

# 使用pylint进行代码分析
uv run pylint app/

# 类型检查
uv run mypy app/
```

### 日常开发命令

```bash
# 安装新依赖
uv add flask-extension

# 运行开发服务器
uv run python run.py

# 运行测试
uv run pytest

# 代码格式化
uv run black . && uv run isort .

# 数据库迁移
uv run flask db migrate -m "添加新功能"
uv run flask db upgrade
```

### 提交之前

1.  运行完整测试套件：`uv run pytest`
2.  检查代码格式化：`uv run black --check .`
3.  排序导入：`uv run isort --check-only .`
4.  运行代码检查：`uv run flake8`
5.  运行类型检查：`uv run mypy app/`

### 部署准备

1.  更新依赖：`uv sync`
2.  运行数据库迁移：`uv run flask db upgrade`
3.  收集静态文件（如果需要）
4.  配置生产环境变量
5.  使用gunicorn启动：`gunicorn -w 4 -b 0.0.0.0:5000 app:app`
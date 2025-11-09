---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 為 Pip 套件加入可執行腳本
translated: true
type: note
---

### 在 Python Pip 套件中建立可執行指令碼

要在可透過 `pip` 安裝的 Python 套件中包含可執行指令碼（即命令列工具），您需要在套件的配置檔案中定義 **進入點**。這讓使用者在安裝後能直接執行您的指令碼（例如在終端機中輸入 `my-script`）。

我們將使用一個簡單範例：名為 `mytools` 的套件，其中包含一個能列印問候語的 `greet` 指令碼。

#### 步驟 1：設定套件結構
建立如下目錄結構：

```
mytools/
├── pyproject.toml          # 現代化配置檔案（建議優先於 setup.py）
├── README.md
└── src/
    └── mytools/
        ├── __init__.py     # 使其成為套件
        └── greet.py        # 您的指令碼邏輯
```

在 `src/mytools/__init__.py` 中（可為空或包含版本資訊）：
```python
__version__ = "0.1.0"
```

在 `src/mytools/greet.py` 中（指令碼將呼叫的函數）：
```python
import sys

def main():
    name = sys.argv[1] if len(sys.argv) > 1 else "World"
    print(f"Hello, {name}!")

if __name__ == "__main__":
    main()
```

#### 步驟 2：在 `pyproject.toml` 中配置進入點
使用 `[project.scripts]` 區段來定義控制台指令碼。這會指示 pip 建立可執行封裝器。

```toml
[build-system]
requires = ["hatchling"]  # 或 "setuptools"、"flit" 等
build-backend = "hatchling.build"

[project]
name = "mytools"
version = "0.1.0"
description = "A simple tool package"
readme = "README.md"
requires-python = ">=3.8"
dependencies = []  # 在此新增依賴項，例如 "requests"

[project.scripts]
greet = "mytools.greet:main"  # 格式：script_name = package.module:function
```

- `greet` 是使用者將執行的命令（例如 `greet Alice`）。
- `mytools.greet:main` 指向 `greet.py` 中的 `main()` 函數。

如果您偏好舊版的 `setup.py`（仍可使用但不建議）：
```python
from setuptools import setup, find_packages

setup(
    name="mytools",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "greet = mytools.greet:main"
        ]
    },
    # ... 其他欄位如 description、install_requires
)
```

#### 步驟 3：建置並安裝套件
1. 安裝建置工具：`pip install build twine`（若使用 hatchling 後端則安裝 `hatchling`）。

2. 建置套件：
   ```
   python -m build
   ```
   這會在 `dist/` 目錄中建立 `.tar.gz` 和 `.whl` 檔案。

3. 本地安裝測試：
   ```
   pip install -e .  # 可編輯模式（變更立即生效）
   ```
   或進行乾淨安裝：`pip install dist/mytools-0.1.0-py3-none-any.whl`。

4. 測試：在終端機中執行 `greet Alice`，應輸出 "Hello, Alice!"。

#### 步驟 4：發佈（可選）
- 上傳至 PyPI：`twine upload dist/*`（需要 PyPI 帳號）。
- 使用者即可透過 `pip install mytools` 安裝並執行 `greet`。

#### 實用提示
- **多個指令碼**：在 `[project.scripts]` 中新增更多行，例如 `another-script = mytools.other:main`。
- **參數處理**：在 `main()` 中使用 `argparse` 以獲得更好的命令列處理能力。
- **依賴項**：在 `[project.dependencies]` 中列出（例如 CLI 框架可使用 `click`）。
- **虛擬環境**：務必使用虛擬環境（`python -m venv env; source env/bin/activate`）以避免衝突。
- **遇到錯誤？** 執行 `pip install --verbose` 查看詳細資訊。確保您的函數不帶參數（或能處理 `sys.argv`）。

如需進階設定（例如使用 Poetry 或 Flit），請查閱官方文件。

#### 參考資料
- [Python Packaging User Guide: Entry Points](https://packaging.python.org/en/latest/guides/writing-entry-points/)
- [PyPI: Building and Publishing](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
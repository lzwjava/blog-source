---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Requests Setup.py 檔案解析
translated: true
type: note
---

### 概覽
這是一個 `setup.py` 檔案，它是與 `setuptools` 搭配使用的標準 Python 指令碼，用於定義和建置 Python 套件。具體來說，這個檔案是為 **Requests** 函式庫所編寫——一個流行的 Python HTTP 客戶端。它負責處理元數據，例如套件名稱、版本、相依性以及分類器（用於 PyPI 發佈）。當你執行 `pip install requests` 時，背後執行的就是這個指令碼（或其建置產物）來安裝套件。

該指令碼結構上是一個單一的 `setup()` 函式呼叫，但它包含了一些防護機制、輔助功能以及從其他檔案動態讀取內容的程式碼。我將逐節進行解析。

### 1. 匯入與 Python 版本檢查
```python
#!/usr/bin/env python
import os
import sys
from codecs import open

from setuptools import setup

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 9)

if CURRENT_PYTHON < REQUIRED_PYTHON:
    # 錯誤訊息並退出
    sys.exit(1)
```
- **Shebang (`#!/usr/bin/env python`)**：讓檔案在類 Unix 系統上可執行，使用系統的 Python 直譯器來執行。
- **匯入**：引入 `os` 和 `sys` 用於系統互動，`codecs.open` 用於 UTF-8 檔案讀取（以安全處理非 ASCII 字元），以及從 `setuptools` 引入 `setup` 用於建置套件。
- **版本檢查**：確保使用者執行的是 Python 3.9 或更高版本。如果不是，則會顯示一個有用的錯誤訊息，建議升級或固定使用舊版 Requests (<2.32.0)，然後以代碼 1（失敗）退出。這強制執行了相容性要求，因為 Requests 已放棄對舊版 Python 的支援。

### 2. 發佈捷徑
```python
if sys.argv[-1] == "publish":
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    sys.exit()
```
- 為維護者提供的便利功能：如果你執行 `python setup.py publish`，它會：
  - 在 `dist/` 資料夾中建置原始碼發佈版 (`sdist`) 和 wheel 套件 (`bdist_wheel`)。
  - 使用 `twine`（一個安全的上傳工具）將它們上傳到 PyPI。
- 這是發布新版本的快速方法，無需手動輸入指令。執行完畢後會退出。

### 3. 相依性
```python
requires = [
    "charset_normalizer>=2,<4",
    "idna>=2.5,<4",
    "urllib3>=1.21.1,<3",
    "certifi>=2017.4.17",
]
test_requirements = [
    "pytest-httpbin==2.1.0",
    "pytest-cov",
    "pytest-mock",
    "pytest-xdist",
    "PySocks>=1.5.6, !=1.5.7",
    "pytest>=3",
]
```
- **`requires`**：當你執行 `pip install requests` 時會安裝的核心相依套件。這些套件負責處理編碼 (`charset_normalizer`)、國際化網域名稱 (`idna`)、HTTP 傳輸 (`urllib3`) 和 SSL 憑證 (`certifi`)。
- **`test_requirements`**：僅在執行測試時安裝（例如，透過 `pip install -e '.[tests]'`）。包含測試工具，例如用於 HTTP 模擬、覆蓋率測試和並行測試的 `pytest` 變體。`PySocks` 用於測試中的 SOCKS 代理支援。

### 4. 動態載入元數據
```python
about = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "src", "requests", "__version__.py"), "r", "utf-8") as f:
    exec(f.read(), about)

with open("README.md", "r", "utf-8") as f:
    readme = f.read()
```
- **`about` 字典**：從 `src/requests/__version__.py` 讀取元數據（例如 `__title__`、`__version__`、`__description__` 等），使用 `exec()` 執行。這使得版本資訊可以集中管理——只需更新一次，`setup.py` 就會自動讀取。
- **`readme`**：將整個 `README.md` 檔案載入為字串，作為套件在 PyPI 上的長描述。

### 5. 主要的 `setup()` 呼叫
這是檔案的核心部分。它配置套件以進行建置/安裝：
```python
setup(
    name=about["__title__"],  # 例如："requests"
    version=about["__version__"],  # 例如："2.32.3"
    description=about["__description__"],  # 簡短摘要
    long_description=readme,  # 完整的 README
    long_description_content_type="text/markdown",  # 在 PyPI 上以 Markdown 格式渲染
    author=about["__author__"],  # 例如："Kenneth Reitz"
    author_email=about["__author_email__"],
    url=about["__url__"],  # 例如：GitHub 儲存庫
    packages=["requests"],  # 安裝 'requests' 套件
    package_data={"": ["LICENSE", "NOTICE"]},  # 包含非 Python 檔案
    package_dir={"": "src"},  # 原始碼位於 'src/' 目錄下
    include_package_data=True,  # 引入所有資料檔案
    python_requires=">=3.9",  # 與版本檢查保持一致
    install_requires=requires,  # 來自前面定義的 requires
    license=about["__license__"],  # 例如："Apache 2.0"
    zip_safe=False,  # 允許編輯已安裝的檔案（函式庫常見做法）
    classifiers=[  # PyPI 分類，提高可發現性
        "Development Status :: 5 - Production/Stable",
        # ... (完整列表包括 Python 版本、作業系統、主題等)
    ],
    tests_require=test_requirements,  # 用於 `pip install -e '.[tests]'`
    extras_require={  # 可選相依性
        "security": [],  # 空白——可能供未來使用
        "socks": ["PySocks>=1.5.6, !=1.5.7"],  # SOCKS 代理支援
        "use_chardet_on_py3": ["chardet>=3.0.2,<6"],  # 舊版字元編碼後備方案
    },
    project_urls={  # PyPI 頁面上的連結
        "Documentation": "https://requests.readthedocs.io",
        "Source": "https://github.com/psf/requests",
    },
)
```
- **關鍵參數**：
  - **名稱/版本/描述**：從 `__version__.py` 讀取，便於維護。
  - **套件/套件目錄**：告訴 setuptools 套件位於 `src/requests/` 目錄下，並將其安裝為 `import requests`。
  - **分類器**：一個字串列表，用於對套件進行分類（例如，穩定版、Python 3.9+、Apache 許可證、網路/HTTP 主題）。這有助於使用者在 PyPI 上找到它。
  - **可選相依性**：讓使用者可以安裝可選功能，例如 `pip install requests[socks]` 以獲得代理支援。
  - **專案網址**：在 PyPI 頁面上添加可點擊的連結，指向文件和原始碼。

### 實際運作方式
- **安裝**：`pip install .`（從儲存庫）或 `pip install requests`（從 PyPI）會執行此指令碼來複製檔案、安裝相依套件並設定套件。
- **建置**：`python setup.py sdist` 建立可發佈的歸檔檔案。
- **為何採用此結構？** 這是一種「src 佈局」（程式碼放在 `src/` 目錄下），這是現代的最佳實踐，旨在避免開發期間意外匯入。該檔案是自包含的，但將細節委派給其他檔案，例如 `__version__.py`。

這個 setup.py 來自官方的 Requests 儲存庫，並且多年來變化不大——它經過了實戰測試，非常可靠。

### 參考資料
- [Requests 文件](https://requests.readthedocs.io/en/latest/)
- [Requests GitHub 儲存庫](https://github.com/psf/requests)
- [Python 套件使用者指南](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
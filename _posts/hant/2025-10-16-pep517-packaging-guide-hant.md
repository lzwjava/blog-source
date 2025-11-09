---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: PEP 517 Python 打包指南
translated: true
type: note
---

PEP 517 於 2016 年獲接納，它定義了一個標準化介面，用於構建 Python 套件，將建置後端（建立發行版的邏輯）與前端（如 pip 等協調流程的工具）解耦。這讓開發者能夠使用現代建置工具，而無需受限於像 setuptools 的 `setup.py` 這類舊系統。結合 PEP 518（指定建置依賴項），它實現了從原始碼樹或原始碼發行版（sdists）進行可靠、隔離的建置。截至 2025 年，PEP 517 已成為現代 Python 套件管理的基礎，並獲得 pip（自版本 10 起支援 PEP 518，版本 19 起完整支援 PEP 517）以及 Poetry、Flit 和 PDM 等工具的支持。

本指南涵蓋了動機、關鍵概念、規範、工作流程、實作及最佳實踐。

## 動機與背景

Python 套件管理從 `distutils`（於 Python 1.6，2000 年引入）演進到 `setuptools`（2004 年），後者增加了依賴管理，但也帶來了問題：
- **指令式且脆弱**：建置依賴執行 `python setup.py`，這是一個任意腳本，可能因環境假設（例如缺少用於擴展的 Cython）而失敗。
- **無建置依賴項**：建置所需的工具（例如編譯器、Cython）未被宣告，導致手動安裝和版本衝突。
- **緊密耦合**：Pip 硬編碼了 `setup.py` 的調用，阻礙了像 Flit 或 Bento 這類替代建置系統。
- **主機環境污染**：建置使用使用者的全域 Python 環境，存在副作用風險。

這些問題阻礙了創新，並在原始碼安裝（例如從 Git）期間導致錯誤。PEP 517 通過標準化一個最小介面來解決此問題：前端在隔離環境中調用後端掛鉤。Wheels（預編譯的二進位檔，2014 年引入）簡化了發行流程——後端只需產生符合規範的 wheels/sdists。PEP 518 通過在 `pyproject.toml` 中宣告建置需求來補充，實現了隔離。

結果是：一個宣告式、可擴展的生態系統，其中 `setup.py` 是可選的，且像 pip 這樣的工具無需依賴舊版後備方案即可建置任何符合規範的專案。

## 關鍵概念

### 原始碼樹與發行版
- **原始碼樹**：包含套件程式碼和 `pyproject.toml` 的目錄（例如 VCS 檢出）。像 `pip install .` 這樣的工具從中建置。
- **原始碼發行版 (Sdist)**：一個 gzip 壓縮的 tarball（`.tar.gz`），例如 `package-1.0.tar.gz`，解壓縮到一個帶有 `pyproject.toml` 和元資料（PKG-INFO）的 `{name}-{version}` 目錄。用於發行版和下遊套件管理（例如 Debian）。
- **Wheel**：一個 `.whl` 二進位發行版——預先建置、平台特定，且無需編譯即可安裝。PEP 517 要求使用 wheels 以確保可重現性。

舊版 sdists（PEP 517 之前）解壓縮到可執行樹，但現在必須包含 `pyproject.toml` 以符合規範。

### pyproject.toml
此 TOML 檔案集中管理配置。`[build-system]` 部分（來自 PEP 518/517）指定：
- `requires`：建置所需的 PEP 508 依賴項列表（例如 `["setuptools>=40.8.0", "wheel"]`）。
- `build-backend`：後端的入口點（例如 `"setuptools.build_meta"` 或 `"poetry.masonry.api"`）。
- `backend-path`（可選）：用於自託管後端的樹內路徑，添加到 `sys.path`（例如 `["src/backend"]`）。

最小配置範例：
```
[build-system]
requires = ["setuptools>=40.8.0", "wheel"]
build-backend = "setuptools.build_meta"
```

需求形成一個 DAG（無循環；前端檢測並失敗）。其他部分如 `[project]`（PEP 621）或 `[tool.poetry]` 保存元資料/依賴項。

### 建置後端與前端
- **後端**：通過掛鉤（可呼叫函數）實作建置邏輯。在子進程中運行以實現隔離。
- **前端**：協調（例如 pip）。設置隔離環境，安裝需求，調用掛鉤。
- **解耦**：前端調用標準化掛鉤，而非 `setup.py`。這支援多樣化的後端而無需更改 pip。

掛鉤使用 `config_settings`（用於標誌的字典，例如 `{"--debug": true}`）並可能輸出到 stdout/stderr（UTF-8）。

## 規範詳情

### [build-system] 詳情
- `requires`：PEP 508 字串（例如 `">=1.0; sys_platform == 'win32'"`）。
- `build-backend`：`module:object`（例如 `flit_core.buildapi` 導入 `flit_core; backend = flit_core.buildapi`）。
- 無 sys.path 污染——後端通過隔離導入。

### 掛鉤
後端將這些作為屬性公開：

**強制性：**
- `build_wheel(wheel_directory, config_settings=None, metadata_directory=None) -> str`：在 `wheel_directory` 中建置 wheel，返回基本名稱（例如 `"myproj-1.0-py3-none-any.whl"`）。如果提供了先前的元資料，則使用之。通過臨時檔案處理唯讀來源。
- `build_sdist(sdist_directory, config_settings=None) -> str`：在 `sdist_directory` 中建置 sdist（pax 格式，UTF-8）。如果不可能（例如無 VCS），則引發 `UnsupportedOperation`。

**可選（預設為 `[]` 或後備方案）：**
- `get_requires_for_build_wheel(config_settings=None) -> list[str]`：額外的 wheel 依賴項（例如 `["cython"]`）。
- `prepare_metadata_for_build_wheel(metadata_directory, config_settings=None) -> str`：寫入 `{pkg}-{ver}.dist-info` 元資料（符合 wheel 規範，無 RECORD）。返回基本名稱；如果缺失，前端從 wheel 提取。
- `get_requires_for_build_sdist(config_settings=None) -> list[str]`：額外的 sdist 依賴項。

掛鉤對錯誤引發異常。前端在隔離環境中調用（例如僅有 stdlib + 需求的 venv）。

### 建置環境
- 隔離的 venv：用於 `get_requires_*` 的引導，完整環境用於建置。
- CLI 工具（例如 `flit`）在 PATH 中。
- 無 stdin；每個掛鉤使用子進程。

## 建置流程詳解

### 逐步工作流程
對於 `pip install .`（原始碼樹）或 sdist 安裝：

1. **發現**：前端讀取 `pyproject.toml`。
2. **隔離設置**：建立 venv；安裝 `requires`。
3. **需求查詢**：調用 `get_requires_for_build_wheel`（安裝額外依賴項）。
4. **元資料準備**：調用 `prepare_metadata_for_build_wheel`（或建置 wheel 並提取）。
5. **Wheel 建置**：在隔離環境中調用 `build_wheel`；安裝產生的 wheel。
6. **後備方案**：如果 sdist 不受支援，則建置 wheel；如果無掛鉤，則使用舊版 `setup.py`。

對於 sdists：解壓縮，視為原始碼樹。開發者工作流程（例如 `pip wheel .`）：
1. 隔離環境。
2. 為 wheel/sdist 調用後端掛鉤。

### 建置隔離 (PEP 518)
為建置建立臨時 venv，避免主機污染。Pip 的 `--no-build-isolation` 停用之（謹慎使用）。像 tox 這樣的工具預設使用隔離。

舊版 vs. 新版：
- **舊版**：在主機環境中執行 `python setup.py install`——存在衝突風險。
- **新版**：隔離掛鉤——可重現、安全。

## 實作建置後端

建立一個後端：
1. 定義一個帶有掛鉤的模組（例如 `mybackend.py`）。
2. 將 `build-backend` 指向它。

最小範例（純 Python 套件）：
```python
# mybackend.py
from zipfile import ZipFile
import os
from pathlib import Path

def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    # 複製原始碼到 wheel 目錄，壓縮為 .whl
    dist = Path(wheel_directory) / "myproj-1.0-py3-none-any.whl"
    with ZipFile(dist, 'w') as z:
        for src in Path('.').rglob('*'):
            z.write(src, src.relative_to('.'))
    return str(dist.relative_to(wheel_directory))

# 可選掛鉤
def get_requires_for_build_wheel(config_settings=None):
    return []

def prepare_metadata_for_build_wheel(metadata_directory, config_settings=None):
    # 寫入 METADATA 等
    return "myproj-1.0.dist-info"
```

在 `pyproject.toml` 中：
```
[build-system]
requires = []
build-backend = "mybackend:build_wheel"  # 實際指向模組物件
```

使用像 `pyproject-hooks` 這樣的函式庫來處理樣板程式碼。對於擴展，通過 `config_settings` 整合 C 編譯器。

## 與工具一起使用 PEP 517

- **pip**：自動檢測 `pyproject.toml`；使用 `--use-pep517`（自 19.1 起預設）。對於可編輯安裝：`pip install -e .` 調用掛鉤。
- **Poetry**：宣告式工具。產生：
  ```
  [build-system]
  requires = ["poetry-core>=1.0.0"]
  build-backend = "poetry.core.masonry.api"
  ```
  通過 `poetry build` 安裝；與 pip 相容。
- **Flit**：適用於純 Python 的簡單工具。使用：
  ```
  [build-system]
  requires = ["flit_core >=3.2,<4"]
  build-backend = "flit_core.buildapi"
  ```
  `flit publish` 建置/上傳。
- **Setuptools**：舊版橋接：
  ```
  [build-system]
  requires = ["setuptools>=40.8.0", "wheel"]
  build-backend = "setuptools.build_meta"
  ```
  支援 `setup.cfg` 用於宣告式元資料。

遷移舊版：添加 `[build-system]`；移除 `setup.py` 調用。

## 錯誤處理與最佳實踐

- **錯誤**：掛鉤引發異常（例如 `ValueError` 用於無效配置）。循環：前端失敗並顯示訊息。不支援的 sdist：後備到 wheel。
- **最佳實踐**：
  - 優先使用宣告式（`setup.cfg` 或 `[project]`）。
  - 宣告確切的建置依賴項（例如 `cython==0.29`）。
  - 測試隔離：`pip wheel . --no-build-isolation` 用於除錯。
  - 對於樹內後端：使用 `backend-path`；避免循環。
  - 安全性：掛鉤在子進程中；無任意程式碼。
  - 相容性：包含 `setup.py` 以支援舊工具。

截至 2025 年，setuptools 佔主導地位（根據調查），但 Poetry/Flit 的採用因簡便性而增長。

## 參考資料
- [PEP 517 – A build-system independent format for source trees](https://peps.python.org/pep-0517/)
- [PEP 517 and 518 in Plain English](https://chadsmith-software.medium.com/pep-517-and-518-in-plain-english-47208ca8b7a6)
- [Python packaging - Past, Present, Future](https://bernat.tech/posts/pep-517-518/)
- [What is PEP 517/518 compatibility?](https://pydevtools.com/handbook/explanation/what-is-pep-517/)
- [Modern pip build process (–use-pep517)](https://fromkk.com/posts/modern-pip-build-process-use-pep517/)
- [What is a build backend?](https://pydevtools.com/handbook/explanation/what-is-a-build-backend/)
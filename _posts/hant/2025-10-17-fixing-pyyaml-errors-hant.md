---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 修復 PyYAML 安裝錯誤
translated: true
type: note
---

### 理解錯誤

這個輸出似乎是來自在 Linux 系統上使用 Python 3.13 執行 `python setup.py install` 或 `pip install pyyaml`（從原始碼安裝）的結果。主要有兩個問題：

1. **C 擴充功能編譯失敗**：
   - 建置過程試圖編譯 C 擴充功能（`yaml._yaml`），但找不到原始檔 `yaml/_yaml.c`。
   - 這是因為較新版本的 PyYAML（大約從 4.x 開始）會在建置過程中動態使用 Cython 生成 `_yaml.c` 檔案。PyPI 上的原始碼發行版不包含預先生成的 `.c` 檔案，因此必須預先安裝 Cython 來創建它。
   - 結果是，它回退到純 Python 版本（這可以工作，但速度較慢且缺少一些功能，如 libyaml 支援）。

2. **安裝期間權限被拒絕**：
   - 安裝嘗試寫入系統範圍的 Python 目錄（`/usr/local/lib/python3.13/dist-packages`），這需要 root 權限。
   - 這在沒有使用 `sudo` 或 `--user` 標誌的情況下很常見。

### 解決方案

#### 修復編譯問題
首先安裝 Cython，然後重試 PyYAML 安裝。這將生成缺失的 `_yaml.c` 檔案並允許建置 C 擴充功能。

- **使用 pip（推薦）**：
  ```
  pip install cython
  pip install pyyaml
  ```
  - 如果您想要更快的 C 擴充功能並帶有 libyaml 支援（需要透過您的套件管理器安裝系統 libyaml-dev，例如在 Ubuntu/Debian 上使用 `sudo apt install libyaml-dev`）：
    ```
    pip install cython libyaml
    pip install --upgrade --force-reinstall --no-cache-dir pyyaml
    ```

- **如果直接使用 setup.py**（不推薦，建議使用 pip）：
  ```
  pip install cython
  python setup.py build_ext --inplace
  python setup.py install
  ```

注意：Python 3.13 相對較新，因此請確保您使用最新的 Cython（例如 3.0.11 或更新版本）以確保相容性。如果您使用的是 free-threaded Python 建置版本，可能需要額外的編譯調整——請查看 PyYAML 的 GitHub issues 以獲取更新。

#### 修復權限問題
- **安裝到使用者目錄**（最安全，無需 sudo）：
  ```
  pip install --user cython pyyaml
  ```
  - 這會安裝到 `~/.local/lib/python3.13/site-packages`。

- **使用 sudo 進行系統範圍安裝**（請謹慎使用，因為它可能與套件管理器衝突）：
  ```
  sudo pip install cython pyyaml
  ```

- **最佳實踐：使用虛擬環境**：
  為了完全避免權限問題：
  ```
  python -m venv myenv
  source myenv/bin/activate  # 在 Linux/Mac 上
  pip install cython pyyaml
  ```
  這可以保持一切隔離。

安裝後，使用 `python -c "import yaml; print(yaml.__version__)"` 進行測試。如果它無錯誤地導入，那麼您就成功了。

如果這些方法無法解決問題（例如，由於特定的 Python 3.13 問題），請提供更多詳細資訊，例如您的確切指令和作業系統版本。

[在 Mac 上建置 - 找不到 _yaml.c](https://github.com/yaml/pyyaml/issues/122)  
[擴充功能 _yaml 未建置](https://github.com/yaml/pyyaml/issues/179)  
[在 MacOS 上安裝帶有 libyaml 支援的 Pyyaml](https://akasurde.github.io/installing-pyyaml-with-libyaml-on-macos.html)
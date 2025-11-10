---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 修復 Pyperclip 安裝錯誤
translated: true
type: note
---

在安裝 `pyperclip` 套件時發生錯誤，具體是在建置其 wheel 過程中，由於 `setuptools` 套件中 `install_layout` 屬性的問題所致。這很可能是由於 `setuptools` 版本與 Python 環境之間的不兼容性，或是 `pyperclip` 設定過程中使用已棄用的選項所引起。以下是解決方法：

### 解決步驟

1. **更新 `setuptools` 和 `pip`**  
   確保您擁有最新版本的 `setuptools` 和 `pip`，因為過時的版本可能導致兼容性問題。

   ```bash
   pip install --upgrade pip setuptools
   ```

2. **安裝特定版本的 `pyperclip`**  
   錯誤可能是由於 `pyperclip` 的版本過舊或不相容所致。嘗試安裝特定且穩定的 `pyperclip` 版本。

   ```bash
   pip install pyperclip==1.8.2
   ```

   如果 `1.8.2` 版本無效，您可以明確嘗試最新版本：

   ```bash
   pip install pyperclip
   ```

3. **使用 `--no-binary` 選項**  
   如果 wheel 建置過程失敗，您可以透過直接安裝原始碼發行版來繞過此問題：

   ```bash
   pip install pyperclip --no-binary pyperclip
   ```

   這會強制 `pip` 從原始碼進行安裝，而非嘗試建置 wheel。

4. **檢查 Python 版本兼容性**  
   確保您的 Python 版本與 `pyperclip` 兼容。截至 2025 年，`pyperclip` 支援 Python 3.6 及以上版本，但舊版本可能會有問題。請檢查您的 Python 版本：

   ```bash
   python3 --version
   ```

   如果您使用的是舊版 Python（例如 Python 3.5 或更早版本），請升級至較新版本（例如 Python 3.8+）。您可以使用如 `pyenv` 等工具來管理 Python 版本。

5. **清除 pip 快取**  
   損壞的 `pip` 快取可能導致問題。請清除快取後重試：

   ```bash
   pip cache purge
   ```

6. **使用虛擬環境**  
   為避免與系統套件發生衝突，請建立虛擬環境：

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows 系統：venv\Scripts\activate
   pip install --upgrade pip setuptools
   pip install pyperclip
   ```

7. **降級 `setuptools`（如有需要）**  
   如果更新 `setuptools` 無法解決問題，請嘗試降級至已知與 `pyperclip` 兼容的版本。例如：

   ```bash
   pip install setuptools==59.6.0
   pip install pyperclip
   ```

8. **檢查系統特定問題**  
   錯誤訊息中提及 `/usr/lib/python3/dist-packages`，表示您可能正在使用系統 Python 安裝（例如在 Ubuntu 上）。系統 Python 安裝可能具有權限限制或與全域安裝的套件發生衝突。使用虛擬環境（步驟 6）是避免此問題的最佳方式。或者，請確保您擁有安裝套件的權限：

   ```bash
   sudo pip install pyperclip
   ```

   但請盡量避免使用 `sudo`，除非必要，因為它可能會擾亂系統 Python。

9. **替代方案：透過 `apt` 安裝（Ubuntu/Debian）**  
   如果您在 Debian 系系統上且 `pip` 持續失敗，您可以使用系統套件管理器安裝 `pyperclip`：

   ```bash
   sudo apt update
   sudo apt install python3-pyperclip
   ```

10. **進一步除錯**  
    如果以上方法均無效，請查閱 `pyperclip` 的 GitHub 頁面或 PyPI 以了解已知問題或兼容性說明。您也可以嘗試直接從原始碼安裝：

    ```bash
    git clone https://github.com/asweigart/pyperclip.git
    cd pyperclip
    python3 setup.py install
    ```

### 補充說明
- 錯誤特別指向 `install_layout`，該屬性在較新版本的 `setuptools` 中已被移除。這表明 `pyperclip` 的設定腳本可能已過時或與您的 `setuptools` 版本不相容。
- 如果您在特定環境中工作（例如 Docker、WSL 或自訂 Python 建置），請確保所有依賴項（如用於編譯 wheel 的 `build-essential`）已安裝：

  ```bash
  sudo apt install build-essential python3-dev
  ```

- 如果問題仍然存在，請提供更多背景資訊（例如 Python 版本、作業系統以及是否使用虛擬環境）以獲得進一步協助。

### 參考資料
- [Pyperclip GitHub](https://github.com/asweigart/pyperclip)
- [Setuptools Documentation](https://setuptools.pypa.io/en/latest/)
- [Pip Documentation](https://pip.pypa.io/en/stable/)
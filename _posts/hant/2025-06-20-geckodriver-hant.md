---
audio: false
generated: true
lang: hant
layout: post
title: Ubuntu 安裝 Selenium GeckoDriver
translated: true
type: note
---

要在 Ubuntu 上安裝 Selenium Firefox 驅動程式 (geckodriver)，請按照以下步驟操作：

1. **安裝 Firefox**（如果尚未安裝）：
   ```bash
   sudo apt update
   sudo apt install firefox
   ```

2. **下載 geckodriver**：
   - 前往 [geckodriver 發布頁面](https://github.com/mozilla/geckodriver/releases)。
   - 選擇與你的 Firefox 版本相容的最新版本。對於 Ubuntu，請下載 Linux 64 位元版本（例如 `geckodriver-vX.XX.X-linux64.tar.gz`）。
   - 下載指令範例（請將 `X.XX.X` 替換為最新版本）：
     ```bash
     wget https://github.com/mozilla/geckodriver/releases/download/vX.XX.X/geckodriver-vX.XX.X-linux64.tar.gz
     ```

3. **解壓縮下載的檔案**：
   ```bash
   tar -xvzf geckodriver-vX.XX.X-linux64.tar.gz
   ```

4. **將 geckodriver 移至系統路徑**：
   - 將解壓後的 `geckodriver` 移至 `/usr/local/bin` 以使其在全系統範圍內可存取：
     ```bash
     sudo mv geckodriver /usr/local/bin/
     ```
   - 使其可執行：
     ```bash
     sudo chmod +x /usr/local/bin/geckodriver
     ```

5. **安裝適用於 Python 的 Selenium**（如果使用 Python）：
   ```bash
   pip install selenium
   ```

6. **驗證安裝**：
   - 檢查 geckodriver 版本：
     ```bash
     geckodriver --version
     ```
   - 使用簡單的 Python 腳本測試：
     ```python
     from selenium import webdriver

     driver = webdriver.Firefox()
     driver.get("https://www.example.com")
     print(driver.title)
     driver.quit()
     ```

**注意事項**：
- 請確保你的 Firefox 版本與 geckodriver 版本相容（請查閱 geckodriver GitHub 頁面上的發布說明）。
- 如果遇到問題，請確保已安裝 `python3-pip`：
  ```bash
  sudo apt install python3-pip
  ```
- 如果找不到 geckodriver，請將 `/usr/local/bin` 加入你的 `PATH`：
  ```bash
  export PATH=$PATH:/usr/local/bin
  ```

這樣應該就能在 Ubuntu 上設定好 Selenium Firefox 驅動程式。如果遇到任何問題，請告訴我！

---

`geckodriver-v0.36.0-linux-aarch64.tar.gz` 與 `geckodriver-v0.36.0-linux64.tar.gz` 的區別在於目標 CPU 架構：

- **linux-aarch64**：適用於 64 位元 ARM 架構（例如 ARMv8-A），常見於 Raspberry Pi、某些伺服器或現代基於 ARM 的 Linux 系統。"aarch64" 代表 64 位元 ARM 架構。

- **linux64**：適用於 64 位元 x86 架構（也稱為 x86_64 或 AMD64），這是大多數執行 Linux 的桌面電腦和伺服器 PC 的標準架構。

**關鍵點**：
- 如果你的系統使用 64 位元 ARM 處理器，請選擇 `linux-aarch64`。
- 如果你的系統使用 64 位元 x86 處理器，請選擇 `linux64`。
- 你可以在 Linux 系統上執行 `uname -m` 來檢查系統架構。如果輸出為 `aarch64`，請使用 ARM 版本；如果輸出為 `x86_64`，請使用 linux64 版本。

`.asc` 檔案是 GPG 簽名，用於驗證相應 `.tar.gz` 檔案的完整性和真實性。
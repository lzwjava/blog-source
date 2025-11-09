---
audio: false
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: Ubuntu 24.04 瀏覽器安裝指南
translated: true
type: note
---

除了 **Firefox** 和 **Chromium** 之外，您還可以在 **Ubuntu 24.04** 上安裝不少優秀的瀏覽器——這取決於您的優先考量（速度、隱私、相容性、資源使用等）。以下是有註解的分類清單：

---

### 🧠 主流瀏覽器

**1. Google Chrome**

* 基於 Chromium，但包含 Google 的同步功能、編解碼器和專有功能。
* 與網路應用程式（如 Google Docs、Meet 等）有出色的相容性。
* 可透過 Google 官方網站下載 `.deb` 安裝檔。

**2. Microsoft Edge（Linux 版本）**

* 基於 Chromium，具有精緻的使用者介面，並與 Microsoft 服務整合。
* 在記憶體處理上通常比 Chrome 更快。
* 可從 Microsoft 網站下載 `.deb` 安裝包。

---

### 🔒 注重隱私的瀏覽器

**3. Brave**

* 基於 Chromium 構建，但內建廣告攔截器、追蹤器阻擋和 Tor 視窗模式。
* 保持與 Chrome 擴充功能的相容性。
* 安裝方式：

  ```bash
  sudo apt install apt-transport-https curl
  sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg
  echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg] https://brave-browser-apt-release.s3.brave.com/ stable main" | sudo tee /etc/apt/sources.list.d/brave-browser-release.list
  sudo apt update
  sudo apt install brave-browser
  ```

**4. Vivaldi**

* 同樣基於 Chromium，但高度可自訂（分頁平鋪、鍵盤快捷鍵、側邊欄工具）。
* 比 Chrome 或 Edge 功能更豐富。
* 可從 [vivaldi.com](https://vivaldi.com) 下載 `.deb` 安裝檔。

**5. Tor Browser**

* 專注於匿名性和規避審查。
* 基於 Firefox ESR，透過 Tor 網路傳輸流量。
* 安裝方式：

  ```bash
  sudo apt install torbrowser-launcher
  ```

---

### 🪶 輕量級瀏覽器

**6. Falkon（Qt WebEngine）**

* 輕量級，介面簡潔，與 KDE/Qt 系統整合良好。
* 安裝方式：

  ```bash
  sudo apt install falkon
  ```

**7. Midori**

* 舊專案重新復興，追求簡潔和低資源使用。
* 適合簡單瀏覽，不適用於重度網路應用程式。
* 安裝方式：

  ```bash
  sudo apt install midori
  ```

**8. Epiphany（GNOME Web）**

* 預設的 GNOME 瀏覽器，基於 WebKit（非 Chromium）。
* 簡潔輕量，完美融入 GNOME 環境。
* 安裝方式：

  ```bash
  sudo apt install epiphany-browser
  ```

---

### 🧪 開發者／小眾瀏覽器

**9. Ungoogled Chromium**

* 移除了所有 Google 追蹤和 API 依賴的 Chromium。
* 需手動設定，但適合嚴格隱私需求。
* 通常可透過社群的 `.deb` 或 Flatpak 找到。

**10. Floorp**

* 一個現代的 Firefox 分支，強化了隱私和自訂功能。
* 由日本開發者製作，日漸受到歡迎。
* 可從 Flathub 取得 Flatpak 版本。

---

需要我根據您在 Ubuntu 上的工作流程，推薦一套組合（例如*一款注重隱私、一款輕量級、一款功能完整*）嗎？
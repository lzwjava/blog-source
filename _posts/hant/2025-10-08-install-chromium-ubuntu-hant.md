---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 在 Ubuntu 24.04 上安裝 Chromium
translated: true
type: note
---

要在 **Ubuntu 24.04** 上安裝 **Chromium**，你有幾個不錯的選擇 — 取決於你想要 **官方的 Snap 版本**、**APT（Debian 套件）** 版本，還是 **手動下載**。以下是每種方法的清晰指南：

---

### 🧩 選項 1：透過 Snap 安裝（官方 Ubuntu 方式）

這是 **預設** 且最穩定的方法。

```bash
sudo snap install chromium
```

然後執行：

```bash
chromium
```

✅ *優點：*

* 由 Canonical 官方維護。
* 自動更新。

⚠️ *缺點：*

* 啟動速度可能較慢。
* Snap 沙盒可能導致系統代理或檔案存取出現問題。

---

### ⚙️ 選項 2：透過 APT 安裝（Debian 套件，非 Snap）

如果你 **不喜歡 Snap**，可以從 **第三方軟體庫** 安裝 Chromium，例如由 **ungoogled-chromium** 或 **OBS** 提供的官方 Debian 版本。

1. 加入 OBS 軟體庫：

   ```bash
   sudo apt install wget gnupg
   wget -qO - https://download.opensuse.org/repositories/home:/ungoogled_chromium/Ubuntu_24.04/Release.key | sudo gpg --dearmor -o /usr/share/keyrings/ungoogled-chromium.gpg
   ```

2. 加入軟體庫：

   ```bash
   echo "deb [signed-by=/usr/share/keyrings/ungoogled-chromium.gpg] https://download.opensuse.org/repositories/home:/ungoogled_chromium/Ubuntu_24.04/ /" | sudo tee /etc/apt/sources.list.d/ungoogled-chromium.list
   ```

3. 安裝 Chromium：

   ```bash
   sudo apt update
   sudo apt install ungoogled-chromium
   ```

然後執行：

```bash
ungoogled-chromium
```

✅ *優點：*

* 無需依賴 Snap。
* 提供隱私加強版本。

⚠️ *缺點：*

* 更新速度比 Snap 慢。
* 部分功能（如 Google Sync）已被停用。

---

### 🧰 選項 3：從 Chromium 官方版本手動安裝

如果你想使用 **最新的開發者版本**：

```bash
sudo apt install chromium-browser
```

如果它重新導向到 Snap 而你想避免這種情況：

```bash
sudo apt purge chromium-browser
sudo apt install chromium
```

或者，手動下載 `.deb` 檔案：

```bash
wget https://commondatastorage.googleapis.com/chromium-browser-snapshots/Linux_x64/LAST_CHANGE -O /tmp/LAST_CHANGE
LATEST=$(cat /tmp/LAST_CHANGE)
wget "https://commondatastorage.googleapis.com/chromium-browser-snapshots/Linux_x64/${LATEST}/chrome-linux.zip"
unzip chrome-linux.zip
./chrome-linux/chrome
```

---

### 🌍 關於代理設定的注意事項

由於你的系統使用：

```
HTTP_PROXY=http://127.0.0.1:7890
HTTPS_PROXY=http://127.0.0.1:7890
```

請確保 Snap 和 APT 尊重你的代理設定，方法是將這些設定匯出到 `/etc/environment` 或你的 shell 設定檔中：

```bash
export http_proxy=http://127.0.0.1:7890
export https_proxy=http://127.0.0.1:7890
```

---

需要我示範如何讓 Chromium 自動使用該代理（使其始終透過代理連線）嗎？
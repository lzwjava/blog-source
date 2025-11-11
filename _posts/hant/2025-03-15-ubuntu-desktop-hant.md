---
audio: false
generated: true
lang: hant
layout: post
title: 在 Ubuntu 上安裝桌面環境
translated: true
type: note
---

聽起來你的 Ubuntu 系統可能沒有安裝圖形使用者介面（GUI），這解釋了為何你沒看到檔案瀏覽器（在 Linux 中常稱為檔案管理器）或任何類似「Finder」的工具。這種情況可能發生在你安裝了 Ubuntu Server 版本、選擇了最小安裝，或是存在某些問題阻止 GUI 載入。別擔心——我們可以透過安裝 GNOME（Ubuntu 預設的桌面環境）或其他你偏好的選項來解決這個問題。以下是逐步操作說明。

### 步驟 1：更新系統
在安裝任何軟體之前，最好先確保你的套件清單是最新的，並且系統已完全升級。開啟終端機並執行以下指令：

```bash
sudo apt update
```
這個指令會重新整理可用套件清單。

```bash
sudo apt upgrade
```
這個指令會將所有已安裝的套件更新至最新版本。如果出現提示，請按 `Y` 確認。

### 步驟 2：安裝 GNOME 桌面環境
既然你提到想要「像 GNOME 或其他」的 GUI，我們就從 GNOME 開始，因為它是 Ubuntu Desktop 的預設環境，並包含一個名為 Nautilus 的檔案管理器。執行以下指令來安裝：

```bash
sudo apt install ubuntu-desktop
```
這個指令會安裝完整的 GNOME 桌面環境，以及標準應用程式如檔案管理器、網頁瀏覽器等。安裝過程可能需要幾分鐘，具體取決於你的網路速度和系統效能。如果被要求選擇顯示管理員（例如 GDM 或 LightDM），通常可以按 Enter 鍵選擇預設選項（GNOME 的 GDM）。

### 步驟 3：重新啟動系統
安裝完成後，重新啟動系統以啟動 GUI：

```bash
sudo reboot
```
系統重啟後，你應該會看到圖形登入畫面。登入後，你將擁有一個功能完整的桌面環境，並可以使用檔案管理器（Nautilus）來瀏覽檔案。

### 如果仍然無法運作怎麼辦？
如果重啟後仍未看到 GUI，可能是顯示管理員或圖形驅動程式存在問題。你可以嘗試手動啟動顯示管理員來測試：

```bash
sudo systemctl start gdm
```
如果這樣能顯示登入畫面，那就太好了！為了確保每次開機時自動啟動，請執行：

```bash
sudo systemctl enable gdm
```
如果 GUI 仍然沒有出現，可以透過檢查系統日誌來尋找錯誤：

```bash
journalctl -b
```
查看與 `gdm`、`Xorg` 或圖形驅動程式相關的訊息，並歡迎你提供這些詳細資訊以尋求進一步協助。

### 其他 GUI 選項
如果你偏好使用 GNOME 以外的 GUI，以下是一些熱門替代方案：
- **KDE Plasma**（簡潔且可自訂）：
  ```bash
  sudo apt install kubuntu-desktop
  ```
- **XFCE**（輕量且快速）：
  ```bash
  sudo apt install xubuntu-desktop
  ```
- **LXDE**（非常輕量，適合舊硬體）：
  ```bash
  sudo apt install lubuntu-desktop
  ```
安裝任何一種後，使用 `sudo reboot` 重啟系統，你將獲得一個帶有檔案管理器的桌面環境（例如 KDE 的 Dolphin、XFCE 的 Thunar）。

### 為什麼我原本沒有 GUI？
你可能沒有看到 GUI 的原因包括：
- 你安裝了 Ubuntu Server，該版本預設不包含桌面環境。
- 你在安裝過程中選擇了最小安裝，跳過了 GUI。
- 極少數情況下，GUI 已安裝但由於配置或硬體問題而無法啟動。

如果是缺少 GUI 的問題，按照上述方法安裝 `ubuntu-desktop` 應該能解決。如果你懷疑是現有 GUI 存在問題，請告訴我，我們可以進一步進行故障排除！

### 總結
要在 Ubuntu 系統上安裝 GNOME 並獲得檔案瀏覽器：
1. `sudo apt update`
2. `sudo apt upgrade`
3. `sudo apt install ubuntu-desktop`
4. `sudo reboot`

你很快就會擁有一個帶有檔案管理器的圖形介面可供使用。享受你的 Ubuntu 桌面吧！
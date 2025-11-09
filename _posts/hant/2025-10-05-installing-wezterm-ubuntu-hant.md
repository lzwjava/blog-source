---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 在 Ubuntu 上安裝 WezTerm
translated: true
type: note
---

出現「無法找到 wezterm 套件」錯誤的原因是 WezTerm 並未收錄於 Ubuntu 的預設軟體庫中。你需要先加入官方的第三方軟體庫。以下是使用原生 APT 方法的逐步解決方案（推薦使用以獲得無縫整合體驗）：

1. 加入軟體庫的 GPG 金鑰：  
   ```
   curl -fsSL https://apt.fury.io/wez/gpg.key | sudo gpg --yes --dearmor -o /usr/share/keyrings/wezterm-fury.gpg
   ```

2. 將軟體庫加入軟體來源清單：  
   ```
   echo 'deb [signed-by=/usr/share/keyrings/wezterm-fury.gpg] https://apt.fury.io/wez/ * *' | sudo tee /etc/apt/sources.list.d/wezterm.list
   ```

3. 設定金鑰檔案的正確權限：  
   ```
   sudo chmod 644 /usr/share/keyrings/wezterm-fury.gpg
   ```

4. 更新套件清單：  
   ```
   sudo apt update
   ```

5. 現在安裝 WezTerm：  
   ```
   sudo apt install wezterm
   ```

安裝完成後，你可以在終端機中輸入 `wezterm` 執行。若想使用 nightly（最新測試）版本，請在步驟 5 改用 `sudo apt install wezterm-nightly`——但請注意此版本無法與穩定版共存。

### 替代方案：Flatpak（無需添加軟體庫）
若你希望採用沙盒式安裝且不修改 APT 來源：  
1. 若未安裝請先安裝 Flatpak：`sudo apt install flatpak`  
2. 加入 Flathub：`flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo`  
3. 安裝：`flatpak install flathub org.wezfurlong.wezterm`  
4. 執行：`flatpak run org.wezfurlong.wezterm`（或建立別名：`alias wezterm='flatpak run org.wezfurlong.wezterm'`）  

Flatpak 採用隔離環境，可能會限制部分進階功能，但更適合用於測試用途。

[WezTerm Linux 安裝指南](https://wezterm.org/install/linux.html)
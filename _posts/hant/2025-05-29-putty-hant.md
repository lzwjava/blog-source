---
audio: false
generated: true
lang: hant
layout: post
title: 在 Windows 上使用 PuTTY
translated: true
type: note
---

PuTTY 是一款免費開源的終端模擬器和 SSH 客戶端，廣泛用於建立遠端伺服器的安全連接。本指南詳細介紹了在 Windows 系統上下載、安裝、配置和使用 PuTTY 的完整流程，包括 SSH 金鑰認證、檔案傳輸和連接埠轉送等進階功能。同時也涵蓋了常見問題的疑難排解以及優化 PuTTY 使用體驗的實用技巧。

---

## 目錄
1. [什麼是 PuTTY？](#什麼是-putty)
2. [下載與安裝 PuTTY](#下載與安裝-putty)
3. [基本配置與連接伺服器](#基本配置與連接伺服器)
4. [進階配置選項](#進階配置選項)
5. [使用 PuTTYgen 進行 SSH 金鑰認證](#使用-puttygen-進行-ssh-金鑰認證)
6. [使用 PSFTP 與 PSCP 進行檔案傳輸](#使用-psftp-與-pscp-進行檔案傳輸)
7. [連接埠轉送與通道傳輸](#連接埠轉送與通道傳輸)
8. [圖形應用程式的 X11 轉送](#圖形應用程式的-x11-轉送)
9. [常見問題疑難排解](#常見問題疑難排解)
10. [技巧與最佳實踐](#技巧與最佳實踐)
11. [PuTTY 的替代方案](#putty-的替代方案)
12. [結論](#結論)

---

## 什麼是 PuTTY？

PuTTY 是由 Simon Tatham 開發的多功能終端模擬器和網路客戶端，主要針對 Windows 平台，同時也支援 Linux 和 macOS。它支援多種通訊協定，包括：

- **SSH（安全外殼）**：用於安全遠端存取伺服器。
- **Telnet**：用於未加密的連接（因安全考量較少使用）。
- **Rlogin**：用於遠端登入 Unix 系統。
- **SCP 與 SFTP**：用於安全檔案傳輸。
- **原始通訊端連接**：用於直接網路通訊。
- **序列連接**：用於與路由器等硬體裝置互動。

PuTTY 輕量且高度可配置，並包含 PuTTYgen（用於生成 SSH 金鑰）和 PSFTP/PSCP（用於檔案傳輸）等工具。它被系統管理員、開發人員和 IT 專業人士廣泛用於管理遠端伺服器。

---

## 下載與安裝 PuTTY

### 步驟 1：下載 PuTTY
1. 訪問官方 PuTTY 網站 [www.putty.org](https://www.putty.org/) 或下載頁面 [chiark.greenend.org.uk/~sgtatham/putty/latest.html](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)。
2. 選擇合適的安裝程式：
   - **32 位元或 64 位元 MSI 安裝程式**：根據您的系統選擇 `putty-<版本>-installer.msi`（建議現代電腦使用 64 位元版本）。
   - **獨立二進位檔案**：如果您不想使用安裝程式，可下載 `putty.exe`、`puttygen.exe`、`psftp.exe` 等檔案。
3. 如果不確定系統類型，32 位元版本具有普遍相容性。

### 步驟 2：安裝 PuTTY
1. 雙擊下載的 `.msi` 檔案以啟動 PuTTY 安裝精靈。
2. 在歡迎畫面上點擊 **Next**。
3. 接受預設的目標資料夾（通常為 `C:\Program Files\PuTTY\`）或選擇自訂位置，然後點擊 **Next**。
4. 選擇所需功能（例如建立桌面捷徑）並點擊 **Install**。
5. 如果 Windows 使用者帳戶控制提示，請點擊 **Yes**。
6. 安裝完成後，點擊 **Finish**。

### 步驟 3：驗證安裝
- 如果建立了桌面捷徑，雙擊 PuTTY 圖示。
- 或者在 Windows 開始功能表中搜尋 "PuTTY"，或導航至 `C:\Program Files\PuTTY\putty.exe`。

---

## 基本配置與連接伺服器

### 啟動 PuTTY
1. 從開始功能表或桌面捷徑開啟 PuTTY。這將開啟 **PuTTY 配置** 視窗，其中包含：
   - 左側窗格用於配置類別。
   - 中間部分用於輸入連接詳細資訊。
   - 右下部分用於儲存工作階段設定檔。

### 連接至伺服器
1. **輸入主機詳細資訊**：
   - 在 **Host Name (or IP address)** 欄位中，輸入伺服器的網域名稱（例如 `students.example.edu`）或 IP 位址（例如 `192.168.1.1`）。
   - 確保 **Port** 設定為 SSH 的預設值 `22`，或您的伺服器管理員指定的連接埠。
2. **選擇連接類型**：
   - 選擇 **SSH**（預設）以進行安全連接。其他選項包括 Telnet、Rlogin、Raw 或 Serial。
3. **儲存工作階段**（可選）：
   - 在 **Saved Sessions** 欄位中輸入名稱（例如 `MyServer`）。
   - 點擊 **Save** 以儲存配置供將來使用。
4. **連接**：
   - 點擊 **Open** 以啟動連接。
   - 如果是首次連接，可能會出現 **PuTTY Security Alert**，警告伺服器的主機金鑰尚未快取。點擊 **Yes** 以信任伺服器並繼續。

### 登入
- 在終端視窗中提示時輸入您的使用者名稱和密碼。
- 如果需要基於金鑰的認證，請按照 [使用 PuTTYgen](#使用-puttygen-進行-ssh-金鑰認證) 部分進行配置。

---

## 進階配置選項

PuTTY 的配置視窗提供了廣泛的自訂選項。以下是關鍵類別和設定：

### 工作階段
- **Saved Sessions**：載入、儲存或刪除工作階段設定檔以快速存取。
- **Close Window on Exit**：選擇在斷開連接後是否自動關閉終端（`Always`、`Never` 或 `Only on clean exit`）。

### 終端
- **Auto Wrap Mode**：啟用後將長文字行換行至下一行。如果停用，超出視窗寬度的文字可能無法顯示。
- **Scrollback Lines**：增加緩衝區中儲存的行數（預設為 200）以檢視更多終端輸出。
- **Keepalives**：設定一個值（以秒為單位）以發送空封包，防止因閒置而導致連接中斷。

### 視窗
- **外觀**：
   - 在 **Window > Appearance** 下變更字型設定（例如大小、樣式）。
   - 在 **Window > Colours** 下修改顏色以提高可讀性（確保前景和背景之間有足夠的對比度）。
- **Resize Behavior**：調整終端回應視窗大小調整的方式（例如縮放字型大小或調整終端尺寸）。

### 連接
- **Proxy Settings**：如果透過公司網路連接，請配置代理。
- **Auto-login**：指定使用者名稱以跳過登入提示。
- **SSH Settings**：
  - 選擇偏好的 SSH 通訊協定版本（建議使用 SSH-2 以確保安全）。
  - 選擇加密密碼（例如 AES、3DES）和金鑰交換演算法。

### 儲存與載入工作階段
1. 配置設定後，返回 **Session** 類別。
2. 在 **Saved Sessions** 欄位中輸入名稱，然後點擊 **Save**。
3. 要載入已儲存的工作階段，請從清單中選擇它，點擊 **Load**，然後點擊 **Open**。

---

## 使用 PuTTYgen 進行 SSH 金鑰認證

SSH 金鑰認證比密碼認證更安全。PuTTYgen 以 PuTTY 的 `.ppk` 格式生成金鑰對。

### 步驟 1：生成金鑰對
1. 從開始功能表或 `C:\Program Files\PuTTY\puttygen.exe` 開啟 **PuTTYgen**。
2. 選擇金鑰類型（例如 **RSA**、預設或 **ECDSA**）和位元長度（例如 RSA 的 2048 或 4096）。
3. 點擊 **Generate** 並移動滑鼠以產生隨機性，直到進度條完成。
4. 可選地，設定 **passphrase** 以增加安全性。
5. 將私密金鑰（`.ppk` 檔案）儲存到安全位置。
6. 複製顯示在 "Public key for pasting into OpenSSH authorized_keys file" 欄位中的公開金鑰。

### 步驟 2：配置伺服器
1. 使用密碼認證（或其他方法）連接至遠端伺服器。
2. 建立或編輯 `~/.ssh/authorized_keys` 檔案：
   - 執行 `mkdir ~/.ssh && chmod 700 ~/.ssh` 以建立 `.ssh` 目錄。
   - 使用文字編輯器開啟 `authorized_keys` 檔案（例如 `nano ~/.ssh/authorized_keys`）。
   - 貼上公開金鑰並儲存檔案。
   - 使用 `chmod 600 ~/.ssh/authorized_keys` 設定權限。
3. 登出伺服器。

### 步驟 3：配置 PuTTY 進行金鑰認證
1. 開啟 PuTTY 並載入您儲存的工作階段。
2. 導航至 **Connection > SSH > Auth > Credentials**。
3. 點擊 "Private key file for authentication" 旁邊的 **Browse**，然後選擇您的 `.ppk` 檔案。
4. 返回 **Session** 類別，儲存更新後的工作階段，然後點擊 **Open**。
5. 在提示時輸入您的 passphrase（如果設定了）。您現在應該可以在沒有密碼的情況下連接。

---

## 使用 PSFTP 與 PSCP 進行檔案傳輸

PuTTY 包含 **PSFTP**（用於 SFTP）和 **PSCP**（用於 SCP）以進行安全檔案傳輸。

### 使用 PSFTP
1. 從開始功能表或 `C:\Program Files\PuTTY\psftp.exe` 開啟 **PSFTP**。
2. 輸入 `open <主機名稱>`（例如 `open students.example.edu`）並按 Enter。
3. 使用您的憑證或私密金鑰登入。
4. 使用以下指令：
   - `ls` 或 `dir`：列出檔案。
   - `get <檔案名稱>`：下載檔案。
   - `put <檔案名稱>`：上傳檔案。
   - `cd <目錄>`：變更目錄。
   - `quit`：退出 PSFTP。

### 使用 PSCP
1. 開啟命令提示字元或 PowerShell。
2. 導航至 PuTTY 安裝目錄（例如 `cd C:\Program Files\PuTTY`）。
3. 執行以下指令：
   - `pscp <本機檔案> <使用者名稱>@<主機名稱>:<遠端路徑>` 以上傳。
   - `pscp <使用者名稱>@<主機名稱>:<遠端檔案> <本機路徑>` 以下載。
   - 添加 `-i <私密金鑰.ppk>` 以進行基於金鑰的認證。

### 注意
- PSFTP 是互動式的，而 PSCP 是基於命令列的。
- 對於圖形化檔案傳輸，可以考慮像 WinSCP 這樣的替代方案，它可以匯入 PuTTY 工作階段。

---

## 連接埠轉送與通道傳輸

PuTTY 支援 **SSH 通道傳輸**（連接埠轉送）以安全存取遠端伺服器上的服務。

### 本機連接埠轉送
1. 在 PuTTY 中，前往 **Connection > SSH > Tunnels**。
2. 輸入您本機機器上的 **Source port**（例如 `8080`）。
3. 輸入遠端服務的 **Destination**（例如 `remote_host:80`）。
4. 選擇 **Local** 並點擊 **Add**。
5. 儲存工作階段並連接。
6. 在本機存取服務（例如 `http://localhost:8080`）。

### 遠端連接埠轉送
- 與本機轉送類似，但選擇 **Remote** 並指定遠端伺服器上的一個連接埠以轉送到您的本機機器。

### 動態連接埠轉送
- 選擇 **Dynamic** 並指定一個本機連接埠（例如 `8080`）。這將建立一個 SOCKS 代理以進行動態路由（適用於透過伺服器瀏覽）。

---

## 圖形應用程式的 X11 轉送

PuTTY 支援 **X11 轉送**，以在遠端伺服器上運行圖形應用程式並在本機顯示它們。

1. 在 Windows 上安裝 X 伺服器（例如 **XMing**，一個免費選項）。
2. 在 PuTTY 中，前往 **Connection > SSH > X11**。
3. 勾選 **Enable X11 forwarding**。
4. 將 **X display location** 設定為 `localhost:0.0`。
5. 儲存工作階段並連接。
6. 在伺服器上運行圖形指令（例如 `xterm`），介面將透過 XMing 在本機顯示。

---

## 常見問題疑難排解

1. **「Access Denied」錯誤**：
   - 驗證使用者名稱、密碼或私密金鑰。
   - 確保伺服器上啟用了 SSH 存取（例如檢查主機控制面板設定）。
   - 檢查伺服器是否僅需要基於金鑰的認證。

2. **「Connection Reset by Peer」**：
   - 在 **Connection** 設定中啟用 **Keepalives** 以防止逾時。
   - 檢查可能關閉閒置連接的防火牆或網路裝置設定。

3. **「Server’s Host Key Not Cached」**：
   - 這是首次連接時的正常現象。點擊 **Yes** 以快取金鑰。如果重複出現，請驗證伺服器的真實性以排除中間人攻擊。

4. **登入嘗試失敗警告**：
   - 重設您的密碼或檢查伺服器上的暴力保護。
   - 如果被鎖定，請聯繫您的伺服器管理員。

5. **PuTTY 視窗意外關閉**：
   - 檢查伺服器日誌以尋找錯誤（例如 `~/.ssh/authorized_keys` 的權限不正確）。
   - 確保載入了正確的私密金鑰。

---

## 技巧與最佳實踐

- **儲存工作階段**：始終儲存工作階段設定檔以避免重新輸入設定。
- **使用金鑰認證**：比密碼更安全，並可防止暴力攻擊。
- **保護私密金鑰**：將 `.ppk` 檔案儲存在安全位置並使用 passphrase。
- **自訂外觀**：調整字型和顏色以提高可讀性，特別是在長時間工作階段中。
- **啟用 Keepalives**：防止在閒置期間連接中斷。
- **備份配置**：從 Windows 登錄檔（`HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions`）匯出已儲存的工作階段以進行備份或遷移。
- **定期更新**：下載最新版本的 PuTTY 以確保安全修補程式和新功能（例如近期版本中的橢圓曲線密碼學）。

---

## PuTTY 的替代方案

雖然 PuTTY 可靠，但現代替代方案提供了增強功能：
- **OpenSSH**：內建於 Windows 10/11、Linux 和 macOS。基於命令列但功能強大。
- **WinSCP**：一個圖形化檔案傳輸客戶端，可與 PuTTY 整合。
- **MobaXterm**：提供標籤式介面、整合的 X 伺服器和 SFTP 支援。
- **Bitvise SSH Client**：支援 GUI、指令碼和單擊通道傳輸。
- **Termius**：跨平台，具有 SSH 金鑰管理和現代化介面。

---

## 結論

PuTTY 是一個功能強大且靈活的工具，用於在 Windows 上管理遠端伺服器。本指南涵蓋了其核心功能，從安裝到進階功能，如 SSH 金鑰認證、檔案傳輸和通道傳輸。通過遵循概述的步驟和最佳實踐，您可以有效地使用 PuTTY 安全存取和管理遠端系統。對於額外功能或更現代的介面，可以考慮探索像 WinSCP 或 MobaXterm 這樣的替代方案。

有關更多詳細資訊或更新，請訪問官方 PuTTY 網站 [www.putty.org](https://www.putty.org/) 或查閱您的主機服務提供商提供的伺服器特定文件。

---

如果您有具體問題或需要有關特定 PuTTY 功能的幫助，請告訴我！
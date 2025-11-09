---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 在 Ubuntu 上安裝 IBM Db2
translated: true
type: note
---

### 在 Ubuntu 22.04 或 24.04 上從 `ibm_db2_v12.1.2_linuxx64_server_dec.tar.gz` 安裝 IBM Db2 12.1.2

IBM Db2 版本 12.1.2（修補包 2）支援最新的 Ubuntu 版本，包括 22.04（Jammy）和 24.04（Noble），只要您的系統符合硬體和軟體先決條件。此安裝使用 tar.gz 檔案中的圖形或靜默安裝程式。建議您查閱 IBM Db2 12.1 的官方文件（例如 IBM Knowledge Center 或 Db2 下載頁面）以獲取最新詳細資訊，因為要求可能因版本而異（此處為伺服器版）。

**開始前的重要注意事項：**
- **系統要求**：
  - 64 位元 x86_64 架構（Intel/AMD）。
  - 至少 4 GB RAM（建議 8 GB）和 2 GB 交換空間。
  - 10 GB 可用磁碟空間用於基礎安裝（資料儲存需要更多）。
  - Root 或 sudo 權限。
  - 核心版本：Ubuntu 22.04/24.04 應可運作，但請確保您的核心至少為 3.10（使用 `uname -r` 檢查）。
  - 防火牆：暫時停用或開啟連接埠（Db2 預設：50000 用於 TCP/IP）。
- **在 Ubuntu 上的潛在問題**：
  - Db2 主要在 RHEL/SUSE 上測試，但透過 Debian 套件支援 Ubuntu。您可能需要解決函式庫相依性問題。
  - 如果您使用 Ubuntu 24.04，它非常新——請先在虛擬機器中測試，因為完全認證可能滯後。
  - 此安裝為伺服器版。對於其他版本（例如 Express-C），請下載相應的 tar.gz 檔案。
- **備份**：在繼續之前備份您的系統。
- 從官方 IBM Passport Advantage 或 Db2 下載網站下載檔案（需要 IBM ID）。

#### 步驟 1：安裝先決條件
更新系統並安裝所需的函式庫。Db2 需要非同步 I/O、PAM 和其他執行時函式庫。

```bash
sudo apt update
sudo apt upgrade -y

# 安裝基本套件（Db2 在 Ubuntu/Debian 上的常見需求）
sudo apt install -y libaio1 libpam0g:i386 libncurses5 libstdc++6:i386 \
    unixodbc unixodbc-dev libxml2 libxslt1.1 wget curl

# 對於 Ubuntu 24.04，您可能還需要：
sudo apt install -y libc6:i386 libgcc-s1:i386

# 驗證 glibc 相容性（Db2 12.1 需要 glibc 2.17+）
ldd --version  # 在 Ubuntu 22.04/24.04 上應顯示 glibc 2.35+
```

如果遇到缺少 32 位元函式庫的問題（例如 Java 元件），啟用多架構：
```bash
sudo dpkg --add-architecture i386
sudo apt update
sudo apt install -y libc6:i386 libncurses5:i386 libstdc++6:i386
```

#### 步驟 2：準備安裝檔案
1. 建立用於解壓縮的臨時目錄（例如 `/tmp/db2_install`）：
   ```bash
   sudo mkdir -p /tmp/db2_install
   cd /tmp/db2_install
   ```

2. 將 tar.gz 檔案複製到此目錄（假設您已下載，例如在 `~/Downloads` 中）：
   ```bash
   cp ~/Downloads/ibm_db2_v12.1.2_linuxx64_server_dec.tar.gz .
   ```

3. 解壓縮歸檔：
   ```bash
   tar -xzf ibm_db2_v12.1.2_linuxx64_server_dec.tar.gz
   ```
   - 這將建立一個包含安裝程式檔案（例如 `db2setup`）的目錄，如 `db2` 或 `sqllib`。

4. 切換到解壓縮後的目錄：
   ```bash
   cd db2  # 或任何頂層目錄——使用 `ls` 檢查
   ```

#### 步驟 3：執行安裝程式
Db2 提供圖形安裝程式（`db2setup`）或回應檔案用於靜默安裝。以 root/sudo 執行。

**選項 A：圖形安裝程式（推薦用於首次設定）**
1. 確保您有顯示器（如果在沒有 GUI 的伺服器上，使用 SSH 的 X 轉發：`ssh -X user@host`）。
2. 執行安裝程式：
   ```bash
   sudo ./db2setup
   ```
   - 精靈將引導您：
     - 接受授權協議。
     - 為伺服器版選擇「典型」安裝。
     - 選擇安裝路徑（預設：`/opt/ibm/db2/V12.1`——確保 `/opt/ibm` 存在且可寫入；如果需要，使用 `sudo mkdir -p /opt/ibm` 建立）。
     - 建立 Db2 實例（例如 "db2inst1"）——這將設定資料庫管理員使用者。
     - 設定認證（例如本地或 LDAP）。
     - 啟用功能，如 SQL Procedural Language（如果需要）。
   - 安裝程式將編譯並設定實例。

**選項 B：靜默安裝（非互動式）**
如果您偏好腳本化：
1. 在試運行期間產生回應檔案：
   ```bash
   sudo ./db2setup -g  # 在目前目錄中產生 `db2setup.rsp`
   ```
   編輯 `db2setup.rsp`（例如設定 `LIC_AGREEMENT=ACCEPT`、`INSTALL_TYPE=TYPICAL`、`CREATE_DB2_INSTANCE=YES` 等）。

2. 執行靜默安裝：
   ```bash
   sudo ./db2setup -u db2setup.rsp
   ```

- 安裝需要 10-30 分鐘。請注意 `/tmp/db2setup.log` 中的錯誤。

#### 步驟 4：安裝後設定
1. **驗證安裝**：
   - 以實例擁有者身份登入（例如 `db2inst1`——在安裝期間建立）：
     ```bash
     su - db2inst1
     ```
   - 檢查 Db2 版本：
     ```bash
     db2level
     ```
   - 啟動實例：
     ```bash
     db2start
     ```
   - 測試連線：
     ```bash
     db2 connect to sample  # 如果不存在，則建立範例資料庫
     db2 "select * from sysibm.sysdummy1"
     db2 disconnect all
     db2stop  # 完成時執行
     ```

2. **建立資料庫（如果在安裝期間未完成）**：
   ```bash
   su - db2inst1
   db2sampl  # 可選：建立範例資料庫
   # 或建立自訂資料庫：
   db2 "create database MYDB"
   db2 connect to MYDB
   ```

3. **環境設定**：
   - 將 Db2 新增到實例使用者的 PATH（新增到 `~/.bashrc`）：
     ```bash
     export PATH=/opt/ibm/db2/V12.1/bin:$PATH
     export DB2INSTANCE=db2inst1
     ```
   - 重新載入：`source ~/.bashrc`。

4. **啟用遠端存取（可選）**：
   - 更新服務：
     ```bash
     su - db2inst1
     db2 update dbm cfg using SVCENAME db2i  # 或您的連接埠
     db2set DB2COMM=TCPIP
     db2start
     ```
   - 編輯 `/etc/services`（以 root 身份）以新增：
     ```
     db2i          50000/tcp
     ```
   - 重新啟動實例。

5. **防火牆設定**：
   ```bash
   sudo ufw allow 50000/tcp  # 用於 Db2 預設連接埠
   sudo ufw reload
   ```

#### 步驟 5：套用更新（推薦）
- 下載並套用最新的修補包（如果需要）（12.1.2 是 FP2；檢查 FP3+）：
  - 使用 `db2iupdt` 工具或 IBM 的更新安裝程式。
- 監控日誌：`/tmp/db2` 或 `/opt/ibm/db2/V12.1/instance/db2inst1/sqllib/db2dump`。

#### 常見問題疑難排解
- **「沒有合適的 Java 執行環境」**：安裝 OpenJDK：`sudo apt install openjdk-11-jre-headless`。
- **函式庫錯誤（例如 libaio.so）**：確保 `libaio1` 已安裝並執行 `sudo ldconfig`。
- **權限被拒絕**：以 root 身份執行安裝程式；確保 `/opt/ibm` 所有權：`sudo chown -R db2inst1:db2iadm1 /opt/ibm/db2`。
- **Glibc 不相容**：在 Ubuntu 22.04/24.04 上不太可能，但如果出現問題，考慮使用容器（Docker）安裝。
- **靜默安裝失敗**：檢查 `db2setup.log` 以獲取線索。
- **Ubuntu 24.04 特定問題**：如果函式庫相依性失敗，您可能需要新增 PPA 或編譯缺失的函式庫。首先在 22.04 上測試。
- 錯誤？搜尋 IBM 的支援論壇或以實例使用者身份執行 `db2diag`。

如果您遇到特定錯誤，請提供詳細資訊以獲得更有針對性的幫助。對於生產用途，考慮使用 IBM 認證的環境或諮詢支援。成功！您的 Db2 實例現在應已準備好用於資料庫建立和使用。
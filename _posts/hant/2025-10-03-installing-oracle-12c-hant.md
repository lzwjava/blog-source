---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 在Ubuntu上安裝Oracle 12c
translated: true
type: note
---

### 在 Ubuntu 22.04 x86_64 上從 Tarball 安裝 Oracle Database 12c Release 1 (12.1.0.2 含 patch 12.1.2?)

檔案 `v12.1.2_linuxx64_server_dec.tar.gz` 似乎是 Oracle Database 12c Release 1 的 tarball（可能是版本 12.1.0.2 捆綁了 12.1.2 patch，伺服器版本，"dec" 可能表示已解除配置）。這是較舊版本的 Oracle Database（約 2013-2014 年），而 Oracle **不正式支援 Ubuntu**。在 Ubuntu 22.04（使用現代函式庫如 glibc 2.35）上安裝可以運作，但可能需要解決相容性問題，例如函式庫連結或核心參數。請預期可能出現依賴項錯誤——請先在虛擬機器中測試。

**警告：**
- Oracle 12c 的延伸支援已結束生命週期（截至 2022 年），因此用於測試/生產環境需自行承擔風險。對於生產環境，請考慮使用較新版本，如 19c 或 23ai。
- 您需要 root/sudo 權限。
- 最低硬體要求：2 GB RAM（建議 8 GB）、2 個 CPU 核心、10 GB 可用軟體磁碟空間（資料庫需要更多）。
- 在繼續之前備份您的系統。
- 如果此 tarball 不是來自 Oracle 官方來源，請驗證其完整性（例如，校驗和）以避免惡意軟體。

#### 步驟 1：準備您的系統
1. **更新 Ubuntu**：
   ```
   sudo apt update && sudo apt upgrade -y
   ```

2. **安裝必要的依賴項**：
   Oracle 12c 需要特定的函式庫。透過 apt 安裝它們：
   ```
   sudo apt install -y oracle-java8-installer bc binutils libaio1 libaio-dev libelf-dev libnuma-dev libstdc++6 unixodbc unixodbc-dev
   ```
   - 如果 `oracle-java8-installer` 不可用（它在較舊的軟體庫中），請添加 Oracle 的 Java PPA 或手動下載 JDK 8：
     ```
     sudo add-apt-repository ppa:webupd8team/java -y
     sudo apt update
     sudo apt install oracle-java8-installer -y
     ```
     在安裝過程中接受許可協議。設定 JAVA_HOME：
     ```
     echo 'export JAVA_HOME=/usr/lib/jvm/java-8-oracle' >> ~/.bashrc
     source ~/.bashrc
     ```

3. **建立 Oracle 使用者和群組**：
   以 root 或使用 sudo 執行：
   ```
   sudo groupadd -g 54321 oinstall
   sudo groupadd -g 54322 dba
   sudo useradd -u 54321 -g oinstall -G dba -s /bin/bash oracle
   sudo passwd oracle  # 為 oracle 使用者設定密碼
   ```

4. **配置核心參數**：
   編輯 `/etc/sysctl.conf`：
   ```
   sudo nano /etc/sysctl.conf
   ```
   添加以下行（根據您的 RAM/磁碟進行調整；這些是最低值）：
   ```
   fs.file-max = 6815744
   kernel.sem = 250 32000 100 128
   kernel.shmmni = 4096
   kernel.shmall = 1073741824
   kernel.shmmax = 4398046511104
   kernel.panic_on_oops = 1
   net.core.rmem_default = 262144
   net.core.rmem_max = 4194304
   net.core.wmem_default = 262144
   net.core.wmem_max = 1048576
   fs.aio-max-nr = 1048576
   vm.swappiness = 0
   ```
   應用變更：
   ```
   sudo sysctl -p
   ```

5. **為 Oracle 使用者設定 Shell 限制**：
   編輯 `/etc/security/limits.conf`：
   ```
   sudo nano /etc/security/limits.conf
   ```
   添加：
   ```
   oracle soft nproc 2047
   oracle hard nproc 16384
   oracle soft nofile 1024
   oracle hard nofile 65536
   oracle soft stack 10240
   oracle hard stack 32768
   ```
   編輯 `/etc/pam.d/login` 並添加：
   ```
   sudo nano /etc/pam.d/login
   ```
   附加：`session required pam_limits.so`

6. **建立目錄**：
   ```
   sudo mkdir -p /u01/app/oracle/product/12.1.0/dbhome_1
   sudo mkdir -p /u01/app/oraInventory
   sudo chown -R oracle:oinstall /u01
   sudo chmod -R 775 /u01
   ```

7. **交換空間**（如果 RAM < 8 GB，添加交換空間）：
   對於 2 GB RAM，建立 2 GB 交換檔案：
   ```
   sudo fallocate -l 2G /swapfile
   sudo chmod 600 /swapfile
   sudo mkswap /swapfile
   sudo swapon /swapfile
   echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
   ```

8. **停用防火牆/SElinux**（如果已啟用）：
   ```
   sudo ufw disable  # 或者如果需要，配置端口 1521, 5500
   sudo apt remove apparmor -y  # 如果 AppArmor 干擾
   ```

#### 步驟 2：解壓縮 Tarball
切換到 oracle 使用者：
```
su - oracle
cd ~/Downloads  # 或檔案所在的任何位置
```
解壓縮（這將建立資料庫主目錄結構）：
```
tar -xzf v12.1.2_linuxx64_server_dec.tar.gz -C /u01/app/oracle/product/12.1.0/
```
- 這應該會建立 `/u01/app/oracle/product/12.1.0/dbhome_1`，其中包含像 `runInstaller` 這樣的檔案。
- 如果 tarball 解壓縮到不同的結構，請相應地調整路徑（例如，`database/` 目錄）。

#### 步驟 3：執行安裝程式
仍然作為 oracle 使用者：
```
cd /u01/app/oracle/product/12.1.0/dbhome_1
./runInstaller
```
- GUI 安裝程式將啟動（如果透過 SSH，需要 X11 轉發；使用 `ssh -X` 或啟用 X11）。
- **安裝選項**：
  - 選擇「僅建立和配置資料庫軟體」或「單一實例資料庫安裝」（適用於伺服器版本）。
  - ORACLE_HOME：`/u01/app/oracle/product/12.1.0/dbhome_1`
  - Inventory：`/u01/app/oraInventory`
  - 如果只是軟體（沒有建立資料庫），請選擇「僅安裝資料庫軟體」。
- 遵循精靈：在可能的地方接受預設值，但為 SYS/SYSTEM 設定密碼。
- 最初忽略任何「先決條件」警告——如果需要，在安裝後修復。

如果 GUI 失敗（例如，DISPLAY 錯誤），執行無訊息安裝：
```
./runInstaller -silent -responseFile /path/to/responsefile.rsp
```
您需要準備一個回應檔案（範例在解壓縮的目錄中，例如 `db_install.rsp`）。使用您的設定（ORACLE_HOME 等）編輯它並執行。

#### 步驟 4：安裝後設定
1. **執行 root.sh**（以 root 身份）：
   ```
   sudo /u01/app/oraInventory/orainstRoot.sh
   sudo /u01/app/oracle/product/12.1.0/dbhome_1/root.sh
   ```

2. **設定環境變數**（為 oracle 使用者，添加到 `~/.bash_profile`）：
   ```
   export ORACLE_HOME=/u01/app/oracle/product/12.1.0/dbhome_1
   export PATH=$ORACLE_HOME/bin:$PATH
   export ORACLE_SID=orcl  # 更改為您的 SID
   export LD_LIBRARY_PATH=$ORACLE_HOME/lib:/lib:/usr/lib
   export CLASSPATH=$ORACLE_HOME/jlib:$ORACLE_HOME/rdbms/jlib
   ```
   ```
   source ~/.bash_profile
   ```

3. **建立資料庫**（如果在安裝期間未完成）：
   ```
   dbca  # 資料庫配置助手 (GUI/無訊息)
   ```
   或使用 SQL*Plus 進行手動建立。

4. **啟動/停止服務**：
   ```
   sqlplus / as sysdba
   STARTUP;  # 或 shutdown
   ```
   添加到 systemd 以實現自動啟動（建立 `/etc/systemd/system/oracle.service`，其中 exec 指向 `dbstart`）。

#### 在 Ubuntu 22.04 上常見問題的疑難排解
- **Glibc/依賴項錯誤**：Oracle 12c 預期 glibc <=2.17。Ubuntu 22.04 有 2.35——使用 `ldd` 檢查，或安裝相容函式庫：
  ```
  sudo apt install libc6:i386 libncurses5:i386 libstdc++6:i386
  ```
  如果出現連結器錯誤，設定 `LD_PRELOAD` 或使用帶有 Oracle Linux 的 Docker 容器。
- **Java/顯示問題**：確保 JDK 8 已設定（`java -version` 應顯示 1.8）。對於無頭模式：`export DISPLAY=:0`。
- **記憶體不足**：增加 ulimit 或 RAM。如果需要，編輯 `runInstaller` 參數。
- **Patch 12.1.2**：如果未捆綁，請從 My Oracle Support 下載並在安裝後使用 `opatch` 應用。
- **日誌**：檢查 `/u01/app/oraInventory/logs/installActions*.log` 以獲取錯誤。
- **相容性修復**：一些使用者符號連結函式庫（例如，`sudo ln -s /lib/x86_64-linux-gnu/libpthread.so.0 /u01/app/oracle/product/12.1.0/dbhome_1/lib/libpthread_nonshared.a`——根據錯誤進行研究）。

#### 驗證
- 執行 `sqlplus / as sysdba` 並執行 `SELECT * FROM v$version;`。
- 監聽器：`lsnrctl start`。

如果您遇到特定錯誤，請提供日誌輸出以獲得更多幫助。有關官方（儘管以 RHEL 為中心）文件，請參閱 Oracle 的 12c 安裝指南。如果這是針對不同的產品（不是資料庫），請澄清 tarball 的內容！
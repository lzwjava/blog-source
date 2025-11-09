---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 解決 WebSphere 大型 EAR 檔案上傳錯誤
translated: true
type: note
---

### 了解問題
「multipart file upload error」（通常類似 `org.apache.commons.fileupload.FileUploadException: Processing of multipart/form-data request failed. File too large (errno:27)`）通常發生在透過 IBM WebSphere Application Server (WAS) 管理控制台更新 EAR 檔案時。對於較大的 EAR 檔案（例如 >20MB），由於檔案上傳限制、暫存儲存空間、堆積記憶體或作業系統資源限制，這種錯誤很常見。這並非 EAR 本身的問題，而是控制台處理 HTTP multipart 上傳的方式所致。

### 首先嘗試的快速解決方法
1. **將 EAR 複製到伺服器並在本機部署**：
   - 使用 FTP/SCP 將新的 EAR 檔案傳輸到 WAS 伺服器上的目錄（例如 `/opt/IBM/WebSphere/AppServer/installableApps/`）。
   - 在管理控制台中：前往 **Applications > Application Types > WebSphere enterprise applications**。
   - 選擇現有應用程式 > **Update**。
   - 選擇 **Replace or add a single module** 或 **Replace the entire application**，然後選擇 **Local file system** 並指向已複製的 EAR 路徑。
   - 這可以繞過透過 HTTP 進行的 multipart 上傳。

2. **提高作業系統檔案大小限制（UNIX/Linux 伺服器）**：
   - 錯誤 `errno:27` 通常表示檔案超過了程序的 ulimit。
   - 以 WAS 使用者身份（例如 `webadmin`）執行 `ulimit -f` 以檢查目前限制。
   - 將其設定為無限制：在使用者的 shell 設定檔（例如 `~/.bash_profile`）或伺服器啟動腳本中加入 `ulimit -f unlimited`。
   - 重新啟動 Deployment Manager (dmgr) 並重試上傳。

### WAS 中的配置變更
1. **增加 Deployment Manager 的堆積大小**：
   - 大型 EAR 可能在處理過程中導致記憶體不足。
   - 在管理控制台中：**Servers > Server Types > Administrative servers > Deployment Manager**。
   - 在 **Java and Process Management > Process definition > Java Virtual Machine** 下：
     - 將 **Initial heap size** 設定為 1024（或更高，例如對於非常大的 EAR 設定為 2048）。
     - 將 **Maximum heap size** 設定為 2048（或更高）。
   - 儲存、重新啟動 dmgr，然後重試。

2. **調整 HTTP 工作階段或 POST 大小限制（如果適用）**：
   - 對於 Web 容器限制：**Servers > Server Types > WebSphere application servers > [Your Server] > Web Container > HTTP transports**。
   - 如果設定過低，請增加 **Maximum post size**（以位元組為單位）。
   - 注意：這會間接影響管理控制台的 Web 應用程式。

### 建議的長期解決方案：使用 wsadmin 進行更新
對於大型或頻繁的更新，完全避免使用控制台——它對於大檔案不可靠。使用 wsadmin 指令碼工具（Jython 或 JACL）來更新應用程式。

#### 步驟：
1. 將新的 EAR 複製到伺服器可存取的路徑（例如 `/tmp/myapp.ear`）。
2. 啟動 wsadmin：  
   ```
   /opt/IBM/WebSphere/AppServer/bin/wsadmin.sh -lang jython -user admin -password pass
   ```
3. 執行此 Jython 指令碼進行更新：  
   ```python
   AdminApp.update('MyAppName', 'app', [-Map ModulesToApps, '[-MapWebModToVH [[default_host MyContext virtual_host]] ]'], [-Operation update], [-appname MyAppName], [-MapModulesToServers [[MyModule MyServer]]], [-nodefaultoptions], [-preCompileJSPs false], [-contextroot MyContext], [-noTxImport], [-connType SERVER], [ -contenturi /tmp/myapp.ear ])
   AdminConfig.save()
   ```
   - 將 `MyAppName` 替換為您的應用程式名稱，`MyContext` 替換為上下文根，`MyServer` 替換為目標伺服器/叢集，`/tmp/myapp.ear` 替換為 EAR 路徑。
4. 如果在叢集環境中，同步節點：`AdminControl.invoke(AdminControl.completeServers(), 'sync')`。
5. 重新啟動應用程式：**Applications > [App] > Restart**。

這種方法更快，可以避免上傳限制，並且可編寫指令碼以實現自動化（例如透過 Jenkins）。

### 其他提示
- **檢查日誌**：在 dmgr 設定檔中查看 `SystemOut.log` 和 `SystemErr.log` 以獲取詳細資訊（例如 `/opt/IBM/WebSphere/AppServer/profiles/Dmgr01/logs/dmgr/`）。
- **使用較小的 EAR 進行測試**：透過壓縮最小版本來驗證問題是否與大小相關。
- **WAS 版本**：確保您使用的是受支援的版本（例如 8.5、9.0）。如果需要，請套用最新的修補程式。
- 如果錯誤仍然存在（例如逾時），請在 **Environment > Web Application Servers > [Server] > Container Settings > Web Container Settings > Web container > Session management > Configuration > Timeout** 中增加 HTTP 逾時設定。

如果這些方法都無法解決問題，請分享確切的錯誤訊息和 WAS 版本以獲得更具體的建議。

### 參考資料
- [Error during deploy of war file on Websphere Application Server 7.0](https://coderanch.com/t/459530/application-servers/Error-deploy-war-file-Websphere)
- [OutOfMemory errors while deploying applications in WebSphere Application Server](https://www.ibm.com/support/pages/outofmemory-errors-while-deploying-applications-websphere-application-server)
- [Maximum size limit of an Ear that can be deployed in WAS](https://stackoverflow.com/questions/58748076/maximum-size-limit-of-an-ear-that-can-be-deployed-in-was)
- [Deploying the enterprise archive (EAR) using the WebSphere Administrative Console](https://www.ibm.com/docs/en/configurepricequote/9.5.0?topic=cwaso-deploying-enterprise-archive-ear-using-websphere-admin-console)
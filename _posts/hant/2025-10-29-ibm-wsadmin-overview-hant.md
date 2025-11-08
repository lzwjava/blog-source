---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: IBM WebSphere wsadmin 工具概覽
translated: true
type: note
---

### IBM WebSphere Application Server (WAS) 中的 wsadmin 概覽

`wsadmin` 工具是一個用於管理 WebSphere Application Server 的命令列指令碼介面。它允許您自動化任務，例如管理伺服器、部署應用程式、配置資源和監控運行時操作。指令碼可以使用 Jython（基於 Python）或 JACL（基於 Tcl）編寫，其中 Jython 由於其可讀性而更常用。

- **`wsadmin.bat`**：用於 Windows 系統。
- **`wsadmin.sh`**：用於 Unix/Linux/AIX 系統。

這兩種工具都位於 WebSphere 設定檔的 `bin` 目錄中（例如 `<WAS_HOME>/profiles/<ProfileName>/bin/`）或基礎安裝目錄（`<WAS_HOME>/bin/`）。建議從設定檔的 `bin` 目錄運行它們以確保正確的環境。

#### 互動式啟動 wsadmin
這將啟動一個 shell，您可以直接在其中輸入命令。

**語法：**
```
wsadmin[.bat|.sh] [options]
```

**基本範例（Windows）：**
```
cd C:\IBM\WebSphere\AppServer\profiles\AppSrv01\bin
wsadmin.bat -lang jython -user admin -password mypass
```

**基本範例（Unix/Linux）：**
```
cd /opt/IBM/WebSphere/AppServer/profiles/AppSrv01/bin
./wsadmin.sh -lang jython -user admin -password mypass
```

- `-lang jython`：指定 Jython（使用 `-lang jacl` 表示 JACL）。
- `-user` 和 `-password`：如果啟用了全域安全性，則需要（如果禁用則可以省略）。
- 如果省略，它將使用預設的 SOAP 連接器連接到本地伺服器（端口 8879）或 RMI（端口 2809）。

進入 wsadmin 提示符（例如 `wsadmin>`）後，您可以使用指令碼物件運行命令：
- **AdminConfig**：用於配置更改（例如創建資源）。
- **AdminControl**：用於運行時操作（例如啟動/停止伺服器）。
- **AdminApp**：用於應用程式部署/更新。
- **AdminTask**：用於高級任務（例如同步節點）。
- **Help**：用於內建幫助（例如 `Help.help()`）。

**Shell 中的範例命令：**
- 列出所有伺服器：`print AdminConfig.list('Server')`
- 啟動伺服器：`AdminControl.invoke(AdminControl.completeObjectName('type=ServerIndex,process=server1,*'), 'start')`
- 儲存更改：`AdminConfig.save()`
- 退出：`quit`

#### 運行指令碼檔案
使用 `-f` 選項以非互動方式執行 Jython（.py 或 .jy）或 JACL（.jacl）指令碼。

**範例指令碼（deployApp.py）：**
```python
# 連接並部署應用程式
appName = 'MyApp'
AdminApp.install('/path/to/MyApp.ear', '[-appname ' + appName + ']')
AdminConfig.save()
print 'Application ' + appName + ' deployed successfully.'
```

**在 Windows 上運行：**
```
wsadmin.bat -lang jython -f /path/to/deployApp.py -user admin -password mypass
```

**在 Unix/Linux 上運行：**
```
./wsadmin.sh -lang jython -f /path/to/deployApp.py -user admin -password mypass
```

#### 運行單一命令
使用 `-c` 選項執行一次性命令（適用於批次檔案或自動化）。

**範例（Windows 批次檔案片段）：**
```batch
@echo off
call "C:\IBM\WebSphere\AppServer\profiles\AppSrv01\bin\wsadmin.bat" -lang jython -c "print AdminConfig.list('Server')" -user admin -password mypass
```

**範例（Unix shell 指令碼片段）：**
```bash
#!/bin/bash
./wsadmin.sh -lang jython -c "print AdminConfig.list('Server')" -user admin -password mypass
```

#### 關鍵選項

| 選項 | 描述 | 範例 |
|--------|-------------|---------|
| `-conntype` | 連接器類型：`SOAP`（預設，端口 8879）或 `RMI`（端口 2809）。 | `-conntype RMI` |
| `-host` | 要連接的遠端主機。 | `-host myhost.example.com` |
| `-port` | 連接器端口。 | `-port 8879` |
| `-tracefile` | 將輸出記錄到檔案。 | `-tracefile wsadmin.log` |
| `-profile` | 在主指令碼之前運行設定檔指令碼。 | `-profile init.py` |
| `-c` | 執行單一命令（非互動式）。 | `-c "AdminConfig.save()"` |
| `-f` | 執行指令碼檔案。 | `-f myscript.py` |
| `-job` | 運行作業管理器命令。 | `-job deploy.xml` |

#### 提示與最佳實踐
- **安全性**：如果全域安全性關閉，請省略 `-user` 和 `-password`。對於安全設置，請使用加密憑證或金鑰檔案。
- **精簡客戶端模式**：用於遠端管理而無需完整 WAS 安裝，使用 `wsadmin -conntype NONE` 並搭配精簡客戶端 JAR（例如 `com.ibm.ws.admin.client_*.jar`）。
- **效能**：對於多個命令，使用單個 `-f` 指令碼，而不是重複使用 `-c` 呼叫，以避免 JVM 開銷。
- **錯誤處理**：在配置更改後始終呼叫 `AdminConfig.save()`。在 Jython 中使用 try-except 以增強穩健性。
- **生成命令**：在 WAS 管理控制台中，執行操作並點擊「查看最後操作的管理指令碼命令」以獲取等效的 wsadmin 命令。
- **版本注意事項**：行為在 WAS 8.5+ 和 9.0+ 中保持一致，但請查閱 IBM 文檔以獲取版本特定細節（例如，新版本中的 Jython 2.7）。

對於更高級的用法，探索 AdminTask 物件以獲取簡化命令，例如 `AdminTask.importFile('path/to/file')`。

### 參考資料
- [wsadmin 指令碼工具 - IBM 文檔](https://www.ibm.com/docs/en/was-nd/9.0.5?topic=scripting-wsadmin-tool)
- [開始使用 wsadmin 指令碼 - IBM 文檔](https://www.ibm.com/docs/SSAW57_8.5.5/com.ibm.websphere.nd.doc/ae/txml_script.html)
- [WAS - wsadmin (Jython) 教程](http://www.mtitek.com/tutorials/websphere/wsadmin_jython.php)
- [IBM WebSphere - 開始使用 wsadmin](https://www.freekb.net/Article?id=1563)
- [WSADMIN 教程 – 第1部分](https://websphereapplicationservernotes.wordpress.com/2012/12/25/wsadmin-tutorial-part1/)
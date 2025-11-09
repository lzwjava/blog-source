---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: WebSphere Application Server 中的 Jython
translated: true
type: note
---

### 在 IBM WebSphere Application Server 中使用 Jython

注意："jPython" 指的是 Jython，這是一種在 Java 虛擬機（JVM）上運行的 Python 實現。它常用於 WebSphere 的管理腳本編寫，也可整合到已部署的應用程式中。WebSphere Application Server (WAS) 捆綁了 Jython（通常為 2.1 或更高版本，具體取決於 WAS 版本），位於 `<WAS_HOME>/optionalLibraries/jython` 目錄下，因此通常無需單獨安裝。下面我將介紹兩種主要使用場景：管理任務和應用程式中的運行時使用。

#### 1. 使用 wsadmin 進行管理腳本編寫
在 WebSphere 中使用 Jython 最常見的方式是進行伺服器管理任務，例如部署應用程式、啟動/停止伺服器、配置資源以及列出已安裝的應用程式。這是通過 `wsadmin` 工具完成的，該工具支援 Jython 作為首選腳本語言（取代已棄用的 Jacl）。

**先決條件：**
- 確保 WebSphere 伺服器正在運行。
- 在 `<WAS_HOME>/bin/wsadmin.sh`（Linux/Unix）或 `wsadmin.bat`（Windows）中找到 `wsadmin`。
- Jython 已預先捆綁；對於較新的功能（例如 Python 2.5+ 語法），可能需要通過自定義類路徑進行升級（參見下方進階說明）。

**運行 Jython 腳本的基本步驟：**
1. 創建一個 Jython 腳本文件（例如 `example.py`）並寫入你的程式碼。使用 AdminConfig、AdminControl 和 AdminApp 物件進行 WebSphere 特定操作。
   
   列出所有已安裝應用程式的示例腳本 (`listApps.py`)：
   ```
   # 列出所有應用程式
   apps = AdminApp.list()
   print("已安裝的應用程式：")
   for app in apps.splitlines():
       if app.strip():
           print(app.strip())
   AdminConfig.save()  # 可選：保存配置更改
   ```

2. 使用 `wsadmin` 運行腳本：
   - 通過 SOAP 連接（遠端預設）：  
     ```
     wsadmin.sh -lang jython -f listApps.py -host <主機名> -port <soap_port> -user <管理員用戶> -password <管理員密碼>
     ```
   - 對於本地（無需主機/端口）：  
     ```
     wsadmin.sh -lang jython -f listApps.py
     ```
   - 示例輸出：列出應用程式，例如 `DefaultApplication`。

3. 對於互動模式 (REPL)：  
   ```
   wsadmin.sh -lang jython
   ```
   然後直接輸入 Jython 命令，例如 `print AdminApp.list()`。

**常見示例：**
- **部署 EAR/WAR：** 創建 `deployApp.py`：
  ```
  appName = 'MyApp'
  earPath = '/path/to/MyApp.ear'
  AdminApp.install(earPath, '[-appname ' + appName + ' -server server1]')
  AdminConfig.save()
  print('已部署 ' + appName)
  ```
  運行：`wsadmin.sh -lang jython -f deployApp.py`。

- **啟動/停止伺服器：**  
  ```
  server = AdminControl.completeObjectName('type=Server,process=server1,*')
  AdminControl.invoke(server, 'start')  # 或 'stop'
  ```

- **指定 Jython 版本（如果需要）：** 明確使用 Jython 2.1：  
  `wsadmin.sh -usejython21 true -f script.py`。對於自定義版本，添加到類路徑：`-wsadmin_classpath /path/to/jython.jar`。

**提示：**
- 使用 `AdminConfig.help('object_type')` 獲取命令幫助。
- 腳本可以在 CI/CD（例如 Jenkins）中通過在批次檔中調用 `wsadmin` 來自動化。
- 對於精簡客戶端（無完整 WAS 安裝）：從 IBM 下載客戶端 jar 並設置類路徑。

#### 2. 在已部署的應用程式中使用 Jython
要在運行於 WebSphere 上的 Java 應用程式（例如 servlet 或 EJB）中執行 Jython 程式碼，請將 Jython 運行時 (jython.jar) 包含在應用程式的類路徑中。這允許嵌入 Python 腳本或使用 Jython 作為腳本引擎。如果捆綁版本過時，請從官方 Jython 網站下載最新的 jython.jar。

有兩種主要方法：**類路徑**（伺服器範圍）或**共享庫**（跨應用程式可重用）。

**方法 1：類路徑（直接添加到 JVM）**
1. 將 `jython.jar` 保存到 WebSphere 主機上可訪問的路徑（例如 `/opt/IBM/WebSphere/AppServer/profiles/AppSrv01/mylibs/jython.jar`）。
2. 登入 WebSphere 管理控制台。
3. 導航至 **Servers > Server Types > WebSphere application servers > [你的伺服器]**。
4. 轉到 **Java and Process Management > Process definition > Java Virtual Machine > Classpath**。
5. 添加 `jython.jar` 的完整路徑（例如 `/opt/.../jython.jar`）。
6. 在 **Generic JVM arguments** 中，添加 Python 路徑：  
   `-Dpython.path=/opt/.../jython.jar/Lib`（指向 Jython 的標準庫）。
7. 點擊 **OK**，保存配置，然後重啟伺服器。
8. 如果在集群環境中，同步節點（通過 **System administration > Nodes > Synchronize**）。
9. 在你的 Java 程式碼中，使用 `org.python.util.PythonInterpreter` 來運行 Jython 腳本：
   ```
   import org.python.util.PythonInterpreter;
   PythonInterpreter interpreter = new PythonInterpreter();
   interpreter.exec("print('Hello from Jython in WebSphere!')");
   ```

**方法 2：共享庫（推薦用於多個應用程式）**
1. 將 `jython.jar` 放置在共享目錄中（例如 `/shared/libs/jython.jar`）。
2. 在管理控制台中：**Environment > Shared libraries > [Scope: Server or Cell] > New**。
3. 輸入名稱（例如 `JythonLib`），勾選 **Use a native library directory**，並將 **Classpath** 設置為 `/shared/libs/jython.jar`。
4. 保存。
5. 對於特定應用程式：**Applications > Application Types > WebSphere enterprise applications > [你的應用程式] > Reference shared libraries**。
6. 在 **Shared library references** 下，點擊 **Add**，選擇 `JythonLib`，並設置 **Classpath** 以匹配。
7. 保存，更新應用程式（如果需要則重啟），並同步節點。
8. 在程式碼中引用，如同類路徑方法。

**應用程式提示：**
- 對於基於 servlet 的 Jython 應用程式，使用 PyServlet（包含在 Jython 中）來處理 Python 處理程序。
- 在開發環境中測試；監控日誌以查找類路徑問題。
- 如果使用較新的 Jython（例如 2.7），請確保與 Java 8+ 相容。

#### 進階說明
- **版本相容性：** WAS 9.x 使用 Jython 2.7+。對於升級，請替換捆綁的 jar，但需徹底測試。
- **錯誤處理：** 在腳本中，使用 `try: ... except Exception as e: print(e)`。
- **IDE 支援：** 使用 IBM Rational Application Developer (RAD) 或帶有 WebSphere 外掛程式的 Eclipse 來調試 Jython/wsadmin 腳本。
- **資源：** 有關完整教程，請參閱書籍 *WebSphere Application Server Administration Using Jython* 或 IBM 的 wsadmin 文檔。

如果這不完全符合你的具體情況（例如特定的 WAS 版本或使用場景），請提供更多詳細信息以獲取量身定制的建議。

**參考資料：**  
- [使用 wsadmin 腳本與 Jython (IBM Docs)](https://www.ibm.com/docs/en/was/9.0.5?topic=scripting-using-wsadmin-jython)  
- [在 WebSphere 上部署 Jython (Oracle Guide)](https://docs.oracle.com/en/applications/jd-edwards/cross-product/9.2/eotos/deploying-jython-on-ais-server-on-ibm-websphere-application.html)  
- [WebSphere Jython 整合 (Stack Overflow)](https://stackoverflow.com/questions/25187577/will-the-ibm-websphere-application-server-run-the-python-jython-script-without-p)  
- [關於 WebSphere 的 Jython Wiki](https://wiki.python.org/jython/WebSphere)  
- [使用 Jython 示例部署應用程式](https://jobhunterssite.wordpress.com/2016/05/12/deploy-an-application-in-websphere-using-jython-automation/)
---
audio: false
generated: true
lang: hant
layout: post
title: OpenJDK 21 工具概覽
translated: true
type: note
---

目錄 `/usr/lib/jvm/java-21-openjdk-amd64/bin/` 包含由 OpenJDK 21 Java 開發工具包 (JDK) 提供的工具。這些工具用於 Java 開發、除錯、監控和封裝等各種任務。以下是每個工具及其常見用途的簡要說明。如需詳細用法，您可以在終端機中對大多數工具執行 `tool_name --help` 或 `man tool_name`。

---

### 1. **jar** - 建立和管理 Java 歸檔 (JAR) 檔案
- **用途**：將 Java 類別和資源打包成 JAR 檔案，或從 JAR 中提取內容。
- **常見用法**：
  ```bash
  jar cf myapp.jar *.class  # 建立 JAR 檔案
  jar xf myapp.jar          # 提取 JAR 的內容
  jar tf myapp.jar          # 列出 JAR 的內容
  ```
- **範例**：`jar cvfm myapp.jar manifest.txt *.class`（建立帶有清單檔案的 JAR）。

---

### 2. **java** - 啟動 Java 應用程式
- **用途**：透過執行類別檔案或 JAR 來執行 Java 程式。
- **常見用法**：
  ```bash
  java MyClass              # 執行類別檔案
  java -jar myapp.jar       # 執行 JAR 檔案
  java -cp . MyClass        # 使用特定類別路徑執行
  ```
- **範例**：`java -Xmx512m -jar myapp.jar`（以 512MB 最大堆記憶體執行 JAR）。

---

### 3. **javadoc** - 產生 API 文件
- **用途**：從 Java 原始碼註解建立 HTML 文件。
- **常見用法**：
  ```bash
  javadoc -d docs MyClass.java  # 在 'docs' 資料夾中產生文件
  ```
- **範例**：`javadoc -d docs -sourcepath src -subpackages com.example`（為套件產生文件）。

---

### 4. **jcmd** - 向執行中的 JVM 傳送診斷指令
- **用途**：與執行中的 Java 程序互動以進行診斷（例如，執行緒傾印、堆積資訊）。
- **常見用法**：
  ```bash
  jcmd <pid> help           # 列出 JVM 程序的可用指令
  jcmd <pid> Thread.print   # 列印執行緒傾印
  ```
- **範例**：`jcmd 1234 GC.run`（為程序 ID 1234 觸發垃圾收集）。

---

### 5. **jdb** - Java 除錯器
- **用途**：互動式除錯 Java 應用程式。
- **常見用法**：
  ```bash
  jdb MyClass               # 開始除錯類別
  java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=*:5005 MyClass  # 使用除錯代理執行
  jdb -attach localhost:5005  # 附加到執行中的 JVM
  ```
- **範例**：`jdb -sourcepath src MyClass`（使用原始碼除錯）。

---

### 6. **jdeps** - 分析類別和 JAR 相依性
- **用途**：識別 Java 應用程式或函式庫的相依性。
- **常見用法**：
  ```bash
  jdeps myapp.jar           # 分析 JAR 中的相依性
  jdeps -s MyClass.class    # 相依性摘要
  ```
- **範例**：`jdeps -v myapp.jar`（詳細相依性分析）。

---

### 7. **jhsdb** - Java HotSpot 除錯器
- **用途**：對 JVM 程序進行進階除錯和分析（例如，核心傾印）。
- **常見用法**：
  ```bash
  jhsdb jmap --heap --pid <pid>  # 分析執行中程序的堆積
  jhsdb hsdb                     # 啟動 HotSpot 除錯器 GUI
  ```
- **範例**：`jhsdb jmap --heap --pid 1234`（傾印程序 1234 的堆積資訊）。

---

### 8. **jinfo** - 檢視或修改 JVM 配置
- **用途**：檢查或變更執行中程序的 JVM 選項。
- **常見用法**：
  ```bash
  jinfo <pid>               # 檢視 JVM 旗標和屬性
  jinfo -flag +PrintGC <pid>  # 啟用 JVM 旗標
  ```
- **範例**：`jinfo -sysprops 1234`（顯示程序 1234 的系統屬性）。

---

### 9. **jmap** - 傾印 JVM 記憶體或堆積資訊
- **用途**：產生堆積傾印或記憶體統計資料。
- **常見用法**：
  ```bash
  jmap -heap <pid>          # 列印堆積摘要
  jmap -dump:file=dump.hprof <pid>  # 建立堆積傾印
  ```
- **範例**：`jmap -dump:live,format=b,file=dump.hprof 1234`（傾印存活物件）。

---

### 10. **jpackage** - 封裝 Java 應用程式
- **用途**：為 Java 應用程式建立原生安裝程式或可執行檔（例如 .deb、.rpm、.exe）。
- **常見用法**：
  ```bash
  jpackage --input target --name MyApp --main-jar myapp.jar --main-class MyClass
  ```
- **範例**：`jpackage --type deb --input target --name MyApp --main-jar myapp.jar`（建立 Debian 套件）。

---

### 11. **jps** - 列出執行中的 JVM 程序
- **用途**：顯示 Java 程序及其程序 ID (PID)。
- **常見用法**：
  ```bash
  jps                       # 列出所有 Java 程序
  jps -l                    # 包含完整類別名稱
  ```
- **範例**：`jps -m`（顯示主類別和參數）。

---

### 12. **jrunscript** - 在 Java 中執行指令碼
- **用途**：使用 Java 指令碼引擎執行指令碼（例如 JavaScript）。
- **常見用法**：
  ```bash
  jrunscript -e "print('Hello')"  # 執行單一指令碼指令
  jrunscript script.js            # 執行指令碼檔案
  ```
- **範例**：`jrunscript -l js -e "print(2+2)"`（執行 JavaScript 程式碼）。

---

### 13. **jshell** - 互動式 Java REPL
- **用途**：互動式執行 Java 程式碼片段以進行測試或學習。
- **常見用法**：
  ```bash
  jshell                    # 啟動互動式 shell
  jshell script.jsh         # 執行 JShell 指令碼
  ```
- **範例**：`jshell -q`（以安靜模式啟動 JShell）。

---

### 14. **jstack** - 產生執行緒傾印
- **用途**：擷取執行中 JVM 的執行緒堆疊追蹤。
- **常見用法**：
  ```bash
  jstack <pid>              # 列印執行緒傾印
  jstack -l <pid>           # 包含鎖定資訊
  ```
- **範例**：`jstack 1234 > threads.txt`（將執行緒傾印儲存到檔案）。

---

### 15. **jstat** - 監控 JVM 統計資料
- **用途**：顯示效能統計資料（例如垃圾收集、記憶體使用情況）。
- **常見用法**：
  ```bash
  jstat -gc <pid>           # 顯示垃圾收集統計資料
  jstat -class <pid> 1000   # 每秒顯示類別載入統計資料
  ```
- **範例**：`jstat -gcutil 1234 1000 5`（顯示 GC 統計資料 5 次，每次間隔 1 秒）。

---

### 16. **jstatd** - JVM 監控守護程式
- **用途**：執行遠端監控伺服器，允許 `jstat` 等工具遠端連線。
- **常見用法**：
  ```bash
  jstatd -J-Djava.security.policy=jstatd.policy
  ```
- **範例**：`jstatd -p 1099`（在連接埠 1099 上啟動守護程式）。

---

### 17. **keytool** - 管理加密金鑰和憑證
- **用途**：為安全的 Java 應用程式建立和管理金鑰儲存庫。
- **常見用法**：
  ```bash
  keytool -genkeypair -alias mykey -keystore keystore.jks  # 產生金鑰對
  keytool -list -keystore keystore.jks                     # 列出金鑰儲存庫內容
  ```
- **範例**：`keytool -importcert -file cert.pem -keystore keystore.jks`（匯入憑證）。

---

### 18. **rmiregistry** - 啟動 RMI 註冊表
- **用途**：為 Java 遠端方法呼叫 (RMI) 物件執行註冊表。
- **常見用法**：
  ```bash
  rmiregistry               # 在預設連接埠 (1099) 上啟動 RMI 註冊表
  rmiregistry 1234          # 在特定連接埠上啟動
  ```
- **範例**：`rmiregistry -J-Djava.rmi.server.codebase=file:./classes/`（使用程式碼庫啟動）。

---

### 19. **serialver** - 為類別產生 serialVersionUID
- **用途**：為實作 `Serializable` 的 Java 類別計算 `serialVersionUID`。
- **常見用法**：
  ```bash
  serialver MyClass         # 列印類別的 serialVersionUID
  ```
- **範例**：`serialver -classpath . com.example.MyClass`（為特定類別計算）。

---

### 20. **javac** - Java 編譯器
- **用途**：將 Java 原始檔編譯成位元組碼。
- **常見用法**：
  ```bash
  javac MyClass.java        # 編譯單一檔案
  javac -d bin *.java       # 編譯到特定目錄
  ```
- **範例**：`javac -cp lib/* -sourcepath src -d bin src/MyClass.java`（使用相依性編譯）。

---

### 21. **javap** - 反組譯類別檔案
- **用途**：檢視已編譯類別的位元組碼或方法簽章。
- **常見用法**：
  ```bash
  javap -c MyClass          # 反組譯位元組碼
  javap -s MyClass          # 顯示方法簽章
  ```
- **範例**：`javap -c -private MyClass`（顯示私有方法和位元組碼）。

---

### 22. **jconsole** - 圖形化 JVM 監控工具
- **用途**：透過 GUI 監控 JVM 效能（記憶體、執行緒、CPU）。
- **常見用法**：
  ```bash
  jconsole                  # 啟動 JConsole 並連線到本機 JVM
  jconsole <pid>            # 連線到特定程序
  ```
- **範例**：`jconsole localhost:1234`（連線到遠端 JVM）。

---

### 23. **jdeprscan** - 掃描已棄用的 API
- **用途**：識別 JAR 或類別檔案中已棄用 API 的使用情況。
- **常見用法**：
  ```bash
  jdeprscan myapp.jar       # 掃描 JAR 中的已棄用 API
  ```
- **範例**：`jdeprscan --release 11 myapp.jar`（針對 Java 11 API 進行檢查）。

---

### 24. **jfr** - Java Flight Recorder
- **用途**：管理和分析 Java Flight Recorder 分析資料。
- **常見用法**：
  ```bash
  jfr print recording.jfr   # 列印 JFR 檔案內容
  jfr summary recording.jfr # 摘要 JFR 檔案
  ```
- **範例**：`jfr print --events GC recording.jfr`（顯示 GC 事件）。

---

### 25. **jimage** - 檢查或提取 JIMAGE 檔案
- **用途**：處理 JIMAGE 檔案（用於 JDK 模組）。
- **常見用法**：
  ```bash
  jimage extract image.jimage  # 提取 JIMAGE 檔案的內容
  ```
- **範例**：`jimage list image.jimage`（列出 JIMAGE 的內容）。

---

### 26. **jlink** - 建立自訂 Java 執行期映像
- **用途**：僅使用所需模組建置最小 JRE。
- **常見用法**：
  ```bash
  jlink --module-path mods --add-modules java.base --output myjre
  ```
- **範例**：`jlink --add-modules java.base,java.sql --output custom-jre`（建立帶有特定模組的 JRE）。

---

### 27. **jmod** - 管理 JMOD 檔案
- **用途**：建立或管理 JMOD 檔案（用於 JDK 模組）。
- **常見用法**：
  ```bash
  jmod create --class-path classes mymod.jmod  # 建立 JMOD 檔案
  jmod list mymod.jmod                        # 列出內容
  ```
- **範例**：`jmod extract mymod.jmod`（提取 JMOD 內容）。

---

### 28. **jwebserver** - 簡易 HTTP 伺服器
- **用途**：執行基本網頁伺服器以提供靜態檔案。
- **常見用法**：
  ```bash
  jwebserver -d /path/to/dir  # 為目錄啟動伺服器
  jwebserver -p 8080          # 在特定連接埠上啟動
  ```
- **範例**：`jwebserver -d ./html -p 8000`（在連接埠 8000 上提供 ./html 中的檔案）。

---

### 進一步學習提示
- **文件**：執行 `tool_name --help` 或查閱 Oracle 的 JDK 文件（例如 https://docs.oracle.com/en/java/javase/21/docs/specs/man/）。
- **手冊頁**：對具有手冊頁的工具使用 `man tool_name`。
- **實作**：在測試專案中實驗以了解工具行為。
- **監控工具**：對於 `jcmd`、`jmap`、`jstack` 等，使用 `jps` 尋找 Java 程序的 PID。
- **除錯**：結合 `jdb`、`jhsdb` 或 `jconsole` 進行進階除錯。

如果您正在進行交易專案（如您的目錄所暗示），像 `javac`、`java`、`jar` 和 `jpackage` 這樣的工具可能與編譯、執行和封裝您的應用程式最相關。對於效能調校，請使用 `jstat`、`jmap` 或 `jfr`。如果您需要深入了解任何特定工具或需要協助您的交易專案，請告訴我！
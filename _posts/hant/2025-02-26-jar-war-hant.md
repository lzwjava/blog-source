---
audio: false
generated: true
lang: hant
layout: post
title: JAR 與 WAR 檔案之別
translated: true
type: note
---

在 Java 封裝中，**JAR**（Java 封存檔）和 **WAR**（網頁封存檔）都是基於 ZIP 結構的封存檔案格式，但它們具有不同的用途和特性。以下是它們差異的詳細說明：

---

### 1. 用途
- **JAR**：JAR 檔案是一種通用封存檔，用於封裝 Java 類別、函式庫或獨立應用程式。它通常用於分發可重複使用的函式庫（例如工具類別）或可在 Java 虛擬機（JVM）上執行的可執行 Java 程式。
- **WAR**：WAR 檔案專為網頁應用程式設計。它將網頁應用程式所需的所有組件（如 servlet、JSP（JavaServer Pages）、HTML、CSS、JavaScript 和配置檔案）封裝成單一單元，以便部署到網頁伺服器或應用程式伺服器（例如 Apache Tomcat、JBoss）上。

---

### 2. 內容
- **JAR**：包含 Java 類別檔案（`.class`）、一個提供元數據的 `MANIFEST.MF` 檔案（位於 `META-INF` 目錄下）（例如可執行 JAR 的主要類別），以及可選的資源，如配置檔案、圖片或屬性檔案。
- **WAR**：包含網頁特定的組件，並具有定義的結構：
  - **WEB-INF/**：一個必需的目錄，包含：
    - `web.xml`（用於配置 servlet、映射等的部署描述符），
    - `classes/`（已編譯的 Java 類別），
    - `lib/`（網頁應用程式使用的依賴 JAR 檔案）。
  - 靜態資源（例如 HTML、CSS、JavaScript）通常位於根目錄或 `WEB-INF` 外部的子目錄中，但 JSP 可能會放置在 `WEB-INF` 內部以限制直接訪問。

---

### 3. 結構
- **JAR**：具有扁平結構，主要由類別檔案和資源組成，清單檔案指定元數據。範例：
  ```
  myapp.jar
  ├── META-INF/
  │   └── MANIFEST.MF
  ├── com/
  │   └── example/
  │       └── MyClass.class
  └── resources/
      └── config.properties
  ```
- **WAR**：遵循為網頁應用程式量身定制的層次結構。範例：
  ```
  mywebapp.war
  ├── index.html
  ├── css/
  │   └── style.css
  ├── WEB-INF/
  │   ├── web.xml
  │   ├── classes/
  │   │   └── com/
  │   │       └── example/
  │   │           └── MyServlet.class
  │   └── lib/
  │       └── dependency.jar
  ```

---

### 4. 部署與使用
- **JAR**：
  - 包含在應用程式的 classpath 中以提供函式庫或可重複使用的程式碼。
  - 如果是可執行的（在清單中指定了 `Main-Class`），則可以直接使用 `java -jar myapp.jar` 運行。
- **WAR**：
  - 部署到 servlet 容器或應用程式伺服器（例如 Tomcat），伺服器會將其解壓縮並使網頁應用程式在特定的 URL（上下文路徑）下可訪問。
  - 不能獨立執行；它依賴伺服器來管理其生命週期。

---

### 5. 依賴處理
- **JAR**：本身不包含其他 JAR；依賴項在外部管理（例如通過 classpath 或像 Maven 這樣的建置工具）。
- **WAR**：可以將依賴的 JAR 捆綁在 `WEB-INF/lib/` 目錄內，確保網頁應用程式使用特定版本的函式庫，並與同一伺服器上的其他應用程式隔離。

---

### 6. 建立
JAR 和 WAR 檔案都可以使用 JDK 中的 `jar` 命令列工具或現代建置工具（如 Maven 或 Gradle）建立：
- **JAR 範例**：`jar cvf myapp.jar -C classes .`
- **WAR 範例**：`jar cvf mywebapp.war .`（假設目錄結構包含 `WEB-INF` 等）。
- 在 **Maven** 中，封裝類型在 `pom.xml` 中指定：
  - `<packaging>jar</packaging>` 用於 JAR。
  - `<packaging>war</packaging>` 用於 WAR。

---

### 總結表格

| 特性             | JAR                              | WAR                                   |
|------------------|----------------------------------|---------------------------------------|
| **全名**         | Java 封存檔                     | 網頁封存檔                           |
| **用途**         | 函式庫、獨立應用程式            | 網頁應用程式                         |
| **內容**         | 類別、清單檔、資源              | Servlet、JSP、HTML、WEB-INF 等       |
| **結構**         | 扁平                            | 層次結構（WEB-INF 等）               |
| **部署**         | Classpath 或 `java -jar`        | 網頁伺服器（例如 Tomcat）            |
| **依賴項**       | 外部管理                        | 捆綁在 `WEB-INF/lib/` 中             |

---

### 關鍵要點
本質上，**JAR** 是一種適用於通用 Java 程式碼的多功能封存檔，而 **WAR** 是一種專為網頁應用程式設計的特殊封存檔，具有為網頁伺服器部署量身定制的結構和組件。了解它們的不同角色可確保在 Java 開發和部署場景中的正確使用。
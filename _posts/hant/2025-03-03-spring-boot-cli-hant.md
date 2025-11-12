---
audio: false
generated: true
lang: hant
layout: post
title: 如何使用 Spring Boot 命令行介面
translated: true
type: note
---

Spring Boot CLI（命令行介面）是一款強大的工具，讓你能直接透過命令行快速開發、測試及原型化 Spring Boot 應用程式。它特別適用於執行 Groovy 腳本而無需建立完整專案結構、生成新專案或實驗 Spring Boot 功能。以下是如何有效安裝和使用 Spring Boot CLI 的完整指南。

---

## 安裝
在使用 Spring Boot CLI 前，你需要先安裝它。根據你的作業系統，主要有兩種安裝方法：

### 1. 使用 SDKMAN!（建議用於 Unix 系統如 Linux 或 macOS）
SDKMAN! 是一款管理軟體開發套件的工具，能輕鬆安裝 Spring Boot CLI。

- **步驟 1：安裝 SDKMAN!**
  開啟終端機並執行：
  ```bash
  curl -s "https://get.sdkman.io" | bash
  ```
  按照提示初始化 SDKMAN!，透過來源指令執行腳本：
  ```bash
  source "$HOME/.sdkman/bin/sdkman-init.sh"
  ```

- **步驟 2：安裝 Spring Boot CLI**
  執行以下指令：
  ```bash
  sdk install springboot
  ```

### 2. 手動安裝（適用於 Windows 或手動設定）
若你使用 Windows 或偏好手動安裝：
- 從 [Spring 官方網站](https://spring.io/projects/spring-boot) 下載 Spring Boot CLI ZIP 檔案。
- 將 ZIP 檔案解壓縮至你選擇的目錄。
- 將解壓縮資料夾中的 `bin` 目錄新增至系統的 PATH 環境變數。

### 驗證安裝
若要確認 Spring Boot CLI 是否正確安裝，請在終端機中執行以下指令：
```bash
spring --version
```
你應該會看到已安裝的 Spring Boot CLI 版本（例如 `Spring CLI v3.3.0`）。若成功顯示，代表你已準備好開始使用！

---

## Spring Boot CLI 的主要使用方式
Spring Boot CLI 提供多項功能，使其成為快速開發和原型化的理想工具。以下是主要使用方式：

### 1. 執行 Groovy 腳本
Spring Boot CLI 的突出功能之一是能直接執行 Groovy 腳本，無需完整專案設定。這非常適合快速原型化或實驗 Spring Boot 功能。

- **範例：建立簡單的 Web 應用程式**
  建立一個名為 `hello.groovy` 的檔案，內容如下：
  ```groovy
  @RestController
  class HelloController {
      @RequestMapping("/")
      String home() {
          "Hello, World!"
      }
  }
  ```

- **執行腳本**
  在終端機中，導航至包含 `hello.groovy` 的目錄並執行：
  ```bash
  spring run hello.groovy
  ```
  這將在埠 8080 啟動一個網頁伺服器。開啟瀏覽器並訪問 `http://localhost:8080`，即可看到顯示的 "Hello, World!"。

- **添加依賴項**
  你可以使用 `@Grab` 註解直接在腳本中包含依賴項。例如：
  ```groovy
  @Grab('org.springframework.boot:spring-boot-starter-data-jpa')
  @RestController
  class HelloController {
      @RequestMapping("/")
      String home() {
          "Hello, World!"
      }
  }
  ```
  這將為你的腳本添加 Spring Data JPA，而無需建置檔案。

- **執行多個腳本**
  若要執行當前目錄中的所有 Groovy 腳本，請使用：
  ```bash
  spring run *.groovy
  ```

### 2. 建立新的 Spring Boot 專案
Spring Boot CLI 能生成具有所需依賴項的新專案結構，為你節省啟動完整應用程式的時間。

- **範例：生成專案**
  執行以下指令來建立一個具有 web 和 data-jpa 依賴項的新專案：
  ```bash
  spring init --dependencies=web,data-jpa my-project
  ```
  這將建立一個名為 `my-project` 的目錄，其中包含一個配置了 Spring Web 和 Spring Data JPA 的 Spring Boot 應用程式。

- **自訂選項**
  你可以指定額外選項，例如：
  - 建置工具：`--build=maven` 或 `--build=gradle`
  - 語言：`--language=java`、`--language=groovy` 或 `--language=kotlin`
  - 封裝方式：`--packaging=jar` 或 `--packaging=war`

  例如：
  ```bash
  spring init --dependencies=web --build=gradle --language=kotlin my-kotlin-project
  ```

### 3. 封裝應用程式
Spring Boot CLI 允許你將腳本封裝成可執行的 JAR 或 WAR 檔案以便部署。

- **建立 JAR 檔案**
  ```bash
  spring jar my-app.jar *.groovy
  ```
  這將當前目錄中的所有 Groovy 腳本封裝到 `my-app.jar` 中。

- **建立 WAR 檔案**
  ```bash
  spring war my-app.war *.groovy
  ```
  這將生成適合部署到 servlet 容器的 `my-app.war` 檔案。

### 4. 執行測試
如果你有 Groovy 測試腳本，可以透過以下指令執行：
```bash
spring test *.groovy
```
這將執行當前目錄中的所有測試腳本。

### 5. 使用互動式 Shell
為了獲得互動式體驗，請啟動 Spring Boot CLI shell：
```bash
spring shell
```
在 shell 中，你可以互動式執行 `run`、`grab` 或 `jar` 等指令，這非常適合實驗性操作。

---

## 總結
Spring Boot CLI 是一款極佳的工具，適合希望從命令行快速高效地使用 Spring Boot 的開發者。以下是其使用方式的簡要說明：

1. **安裝**：使用 SDKMAN!（`sdk install springboot`）或手動下載 ZIP 並更新 PATH。
2. **執行 Groovy 腳本**：使用 `spring run <script.groovy>` 進行快速原型化。
3. **建立新專案**：使用 `spring init --dependencies=<deps> <project-name>`。
4. **封裝應用程式**：使用 `spring jar` 或 `spring war` 將應用程式封裝成 JAR 或 WAR 檔案。
5. **互動式實驗**：使用 `spring shell`。

無論你是原型化一個想法、學習 Spring Boot 還是自動化任務，Spring Boot CLI 都提供了一種輕量且靈活的方式來開始，而無需完整的 IDE 或專案設定的負擔。
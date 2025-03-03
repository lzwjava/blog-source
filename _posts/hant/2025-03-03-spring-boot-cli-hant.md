---
audio: false
generated: true
lang: hant
layout: post
title: 如何使用 Spring Boot CLI
translated: true
---

Spring Boot CLI（命令行界面）是一個強大的工具，允許你直接從命令行快速開發、測試和原型設計Spring Boot應用程序。它特別適合用於運行Groovy腳本而不需要設置完整的項目結構、生成新項目或實驗Spring Boot功能。以下是如何有效安裝和使用Spring Boot CLI的完整指南。

---

## 安裝
在使用Spring Boot CLI之前，你需要安裝它。根據你的操作系統，有兩種主要方法：

### 1. 使用SDKMAN!（推薦給基於Unix的系統如Linux或macOS）
SDKMAN!是一個用於管理軟件開發工具包的工具，使其成為安裝Spring Boot CLI的簡單方法。

- **步驟1：安裝SDKMAN!**
  打開你的終端並運行：
  ```bash
  curl -s "https://get.sdkman.io" | bash
  ```
  按照提示初始化SDKMAN!，通過源文件：
  ```bash
  source "$HOME/.sdkman/bin/sdkman-init.sh"
  ```

- **步驟2：安裝Spring Boot CLI**
  運行以下命令：
  ```bash
  sdk install springboot
  ```

### 2. 手動安裝（適用於Windows或手動設置）
如果你在Windows上或偏好手動安裝：
- 從[官方Spring網站](https://spring.io/projects/spring-boot)下載Spring Boot CLI ZIP文件。
- 將ZIP文件解壓縮到你選擇的目錄。
- 將解壓縮文件夾中的`bin`目錄添加到系統的PATH環境變量。

### 驗證安裝
要確認Spring Boot CLI已正確安裝，在終端中運行以下命令：
```bash
spring --version
```
你應該會看到已安裝的Spring Boot CLI版本（例如`Spring CLI v3.3.0`）。如果這樣做，你就可以開始使用它了！

---

## 使用Spring Boot CLI的主要方法
Spring Boot CLI提供了幾個功能，使其非常適合快速開發和原型設計。以下是主要的使用方法：

### 1. 運行Groovy腳本
Spring Boot CLI的突出特點之一是能夠直接運行Groovy腳本而不需要完整的項目設置。這對於快速原型設計或實驗Spring Boot非常理想。

- **示例：創建簡單的Web應用程序**
  創建一個名為`hello.groovy`的文件，內容如下：
  ```groovy
  @RestController
  class HelloController {
      @RequestMapping("/")
      String home() {
          "Hello, World!"
      }
  }
  ```

- **運行腳本**
  在終端中，導航到包含`hello.groovy`的目錄並運行：
  ```bash
  spring run hello.groovy
  ```
  這將在8080端口啟動一個Web伺服器。打開瀏覽器並訪問`http://localhost:8080`，你應該會看到顯示“Hello, World!”。

- **添加依賴**
  你可以使用`@Grab`註釋直接在腳本中包含依賴。例如：
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
  這將在不需要構建文件的情況下將Spring Data JPA添加到你的腳本中。

- **運行多個腳本**
  要運行當前目錄中的所有Groovy腳本，請使用：
  ```bash
  spring run *.groovy
  ```

### 2. 創建新的Spring Boot項目
Spring Boot CLI可以生成具有所需依賴的新項目結構，當開始完整應用程序時節省時間。

- **示例：生成項目**
  運行以下命令以創建具有Web和data-jpa依賴的新項目：
  ```bash
  spring init --dependencies=web,data-jpa my-project
  ```
  這將創建一個名為`my-project`的目錄，其中包含配置了Spring Web和Spring Data JPA的Spring Boot應用程序。

- **自定義選項**
  你可以指定其他選項，例如：
  - 构建工具：`--build=maven`或`--build=gradle`
  - 語言：`--language=java`、`--language=groovy`或`--language=kotlin`
  - 打包：`--packaging=jar`或`--packaging=war`

  例如：
  ```bash
  spring init --dependencies=web --build=gradle --language=kotlin my-kotlin-project
  ```

### 3. 打包應用程序
Spring Boot CLI允許你將腳本打包成可執行的JAR或WAR文件以進行部署。

- **創建JAR文件**
  ```bash
  spring jar my-app.jar *.groovy
  ```
  這將當前目錄中的所有Groovy腳本打包到`my-app.jar`中。

- **創建WAR文件**
  ```bash
  spring war my-app.war *.groovy
  ```
  這將生成一個適合部署到Servlet容器的`my-app.war`文件。

### 4. 運行測試
如果你有Groovy測試腳本，可以使用以下命令執行它們：
```bash
spring test *.groovy
```
這將運行當前目錄中的所有測試腳本。

### 5. 使用交互式Shell
對於交互式體驗，啟動Spring Boot CLI Shell：
```bash
spring shell
```
在Shell中，你可以交互式地運行命令，如`run`、`grab`或`jar`，這對於實驗非常有用。

---

## 摘要
Spring Boot CLI是一個適合從命令行快速高效地使用Spring Boot的優秀工具。以下是如何使用它的簡要說明：

1. **安裝它**使用SDKMAN!（`sdk install springboot`）或手動下載ZIP文件並更新你的PATH。
2. **運行Groovy腳本**使用`spring run <script.groovy>`進行快速原型設計。
3. **創建新項目**使用`spring init --dependencies=<deps> <project-name>`。
4. **打包應用程序**到JAR或WAR文件使用`spring jar`或`spring war`。
5. **交互式實驗**使用`spring shell`。

無論你是原型設計一個想法、學習Spring Boot還是自動化任務，Spring Boot CLI都提供了一種輕量級和靈活的方式來開始，而不需要完整的IDE或項目設置。
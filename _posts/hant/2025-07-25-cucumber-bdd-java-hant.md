---
audio: false
generated: true
image: false
lang: hant
layout: post
title: Java開發者的黃瓜行為驅動開發指南
translated: true
type: note
---

這是一份實用的端到端 **Cucumber** 入門指南——它是什么、團隊為何使用它，以及如何在 Java 中高效運用（並附上 JS/Python 用戶的快速說明）。

---

# Cucumber 是什麼（與不是什麼）

* **Cucumber** 是一個 **BDD（行為驅動開發）** 測試框架。它讓你能用純文字（Gherkin）描述行為，並將這些句子綁定到可執行的程式碼（步驟定義）。
* 當你希望產品、QA 和工程團隊之間達成**共同理解**，並需要兼具測試功能的**活文件**時，它是理想選擇。
* 它**並非**單元測試框架（JUnit/TestNG/Jest/PyTest）的替代品。它通過專注於**業務層級的驗收測試**來補充這些框架。

---

# 核心組件

**1) Gherkin（純文字規格）**

* 編寫在 `.feature` 檔案中。
* 關鍵字：`Feature`、`Scenario`、`Given/When/Then/And/But`、`Background`、`Scenario Outline` + `Examples`、`@tags`（以及較新 Gherkin 中可選的 `Rule`）。
* 自然語言風格；支援多種語系。

**2) 步驟定義（程式碼）**

* 透過 **Cucumber Expressions**（或正則表達式）將 Gherkin 步驟綁定到程式碼。
* 可呼叫頁面物件、API 客戶端、服務、資料庫輔助工具等。

**3) 執行器**

* 啟動 Cucumber，根據 glue 路徑、配置和標籤發現特徵和步驟。
* 在 JVM 上，通常透過 **JUnit**（4 或 5）或 **TestNG** 執行。

**4) 報告**

* 生成 HTML/JSON/JUnit XML；與 CI 儀表板和 **Allure** 等工具整合。

---

# 最小範例（Java, Maven）

**pom.xml（關鍵部分）**

```xml
<dependencies>
  <!-- JUnit 5 -->
  <dependency>
    <groupId>org.junit.jupiter</groupId>
    <artifactId>junit-jupiter</artifactId>
    <version>5.10.2</version>
    <scope>test</scope>
  </dependency>

  <!-- Cucumber JVM + JUnit Platform -->
  <dependency>
    <groupId>io.cucumber</groupId>
    <artifactId>cucumber-java</artifactId>
    <version>7.18.1</version>
    <scope>test</scope>
  </dependency>
  <dependency>
    <groupId>io.cucumber</groupId>
    <artifactId>cucumber-junit-platform-engine</artifactId>
    <version>7.18.1</version>
    <scope>test</scope>
  </dependency>
</dependencies>

<build>
  <plugins>
    <plugin>
      <artifactId>maven-surefire-plugin</artifactId>
      <version>3.2.5</version>
      <configuration>
        <!-- 如有需要，可按標籤執行、並行執行等 -->
      </configuration>
    </plugin>
  </plugins>
</build>
```

**專案結構**

```
src
 └─ test
     ├─ java
     │   └─ com/example/steps/...
     └─ resources
         └─ features/...
```

**特徵檔案 (`src/test/resources/features/login.feature`)**

```gherkin
Feature: 登入
  作為已註冊用戶
  我希望能夠登入
  以便存取我的帳戶

  Background:
    Given 應用程式正在執行

  @smoke
  Scenario: 成功登入
    Given 我在登入頁面上
    When 我使用用戶名 "alice" 和密碼 "secret" 登入
    Then 我應該看到 "Welcome, alice"

  Scenario Outline: 登入失敗
    Given 我在登入頁面上
    When 我使用用戶名 "<user>" 和密碼 "<pass>" 登入
    Then 我應該看到 "Invalid credentials"
    Examples:
      | user  | pass     |
      | alice | wrong    |
      | bob   | invalid  |
```

**步驟定義（Java, Cucumber Expressions）**

```java
package com.example.steps;

import io.cucumber.java.en.*;
import static org.junit.jupiter.api.Assertions.*;

public class LoginSteps {
  private String page;
  private String message;

  @Given("the application is running")
  public void app_running() {
    // 啟動測試應用程式 / 啟動伺服器 / 重置狀態
  }

  @Given("I am on the login page")
  public void i_am_on_the_login_page() {
    page = "login";
  }

  @When("I sign in with username {string} and password {string}")
  public void i_sign_in(String user, String pass) {
    // 呼叫 UI 或 API；此處為模擬：
    if ("alice".equals(user) && "secret".equals(pass)) {
      message = "Welcome, alice";
    } else {
      message = "Invalid credentials";
    }
  }

  @Then("I should see {string}")
  public void i_should_see(String expected) {
    assertEquals(expected, message);
  }
}
```

**JUnit 5 執行器（透過引擎發現）**

```java
// 使用 JUnit Platform 時不需要明確的執行器類別。
// 如果需要標籤過濾，可以建立測試套件：
import org.junit.platform.suite.api.*;

@Suite
@IncludeEngines("cucumber")
@SelectClasspathResource("features")
@ConfigurationParameter(key = "cucumber.glue", value = "com.example.steps")
@ConfigurationParameter(key = "cucumber.plugin", value = "pretty, html:target/cucumber.html, json:target/cucumber.json")
@ExcludeTags("wip") // 範例
public class RunCucumberTest {}
```

執行：

```bash
mvn -q -Dtest=RunCucumberTest test
```

---

# 日常使用的 Gherkin 要點

* **Background**：每個場景的通用設定（例如「Given 我已登入」）。
* **Scenario Outline + Examples**：無需複製貼上步驟的資料驅動測試。
* **Doc Strings**：步驟中的多行內容（例如 JSON 主體）。
* **Data Tables**：將步驟中的表格轉換為物件或映射。
* **Tags**：為 CI 流水線切割測試套件（`@smoke`、`@api`、`@slow`）。
* **Rule**（可選）：按業務規則分組場景以提高可讀性。

---

# Cucumber Expressions（比正則表達式更友好）

* 佔位符如 `{string}`、`{int}`、`{word}`、`{float}`。
* **自定義參數類型**讓你能解析領域物件：

```java
import io.cucumber.java.ParameterType;

public class ParameterTypes {
  @ParameterType("USD|CNY|EUR")
  public Currency currency(String code) { return Currency.getInstance(code); }
}
```

然後使用：`When I pay 100 {currency}`。

---

# 鉤子與測試生命週期

* JVM/JS/Ruby 變體中的 `@Before`、`@After`、`@BeforeStep`、`@AfterStep`。
* 使用鉤子進行**清理設定/拆卸**、失敗時截圖、資料庫重置等。
* 對於依賴注入，使用 **Spring** (cucumber-spring) 或 **PicoContainer** 來共享狀態：

  * 使用 Spring Boot 時，將步驟類別註解為 bean；使用 `@SpringBootTest` 進行連線並根據需要使用測試切片。

---

# 你可能需要的整合

* **Web UI**：Selenium/WebDriver, Playwright。封裝在**頁面物件**中並從步驟呼叫。
* **API**：REST Assured/HTTP 客戶端；使用 JSON 斷言驗證。
* **DB**：Flyway/Liquibase 用於架構，測試資料載入器，嵌入式資料庫。
* **Mocking**：WireMock/Testcontainers 用於外部系統。
* **報告**：內建 HTML/JSON；**Allure** 用於豐富的時間線和附件。
* **並行**：JUnit Platform（或在舊版堆疊中使用帶有 TestNG 的 `cucumber-jvm-parallel-plugin`）。保持場景隔離；避免共享可變狀態。

---

# CI/CD 與擴展

* **基於標籤的流水線**：在 PR 上執行 `@smoke`，每日執行 `@regression`，定時執行 `@slow`。
* **按檔案或標籤分片**到多個代理以提升速度。
* **成品**：發布 HTML/JSON/Allure 以及截圖/影片（UI）。
* **不穩定測試**：找出根本原因——不要透過「重試直到變綠」來解決。

---

# 良好實踐（經過實戰檢驗）

* **統一口吻**：保持步驟措辭一致；避免 UI 雜訊（「點擊藍色按鈕」）——專注於**意圖**（「提交憑證」）。
* **薄步驟，厚輔助**：步驟程式碼應委託給頁面物件/服務；將邏輯排除在步驟之外。
* **穩定的測試資料**：透過 API/資料庫固定資料種子；避免與類生產環境的隨機性耦合。
* **快速、獨立的場景**：沒有順序假設；每個場景都有乾淨狀態。
* **限制套件規模**：將 Cucumber 保留給**業務行為**；將單元測試保留在 JUnit/TestNG/Jest 中以處理低層級細節。

---

# 應避免的反模式

* 將 Cucumber 視為更漂亮的單元測試執行器。
* 過度使用帶有長程序序列的 `And`（命令式、脆弱）。
* 在步驟措辭中耦合到 CSS 選擇器或易變的 UI 細節。
* 隱藏每個場景實際所需內容的巨大 Background。

---

# 其他語言的快速說明

**JavaScript/TypeScript**

* 使用 **`@cucumber/cucumber`**。
* 典型腳本：

  ```bash
  npm i -D @cucumber/cucumber
  npx cucumber-js --require steps/**/*.ts --publish-quiet
  ```
* 與 **Playwright** 和 **Allure** 良好配合。

**Python**

* 使用 **behave**（類 Cucumber）或 **pytest-bdd**。
* 結構和概念相同：特徵 + 步驟 + 固定裝置。

**Ruby**

* 原始的 Cucumber 實現；慣用語法鏡像 JVM 和 JS 版本。

---

# 何時選擇 Cucumber

* 你希望非工程師也能閱讀**活文件**。
* 驗收標準需要是**可執行的**並且**可追溯**到發布版本。
* 跨職能團隊在實施**之前**就行為達成一致（BDD 三人組）。

如果團隊不願意維護 Gherkin，或者測試純屬技術性而單元/整合測試已能提供清晰度，則跳過它（或謹慎使用）。

---

如果你告訴我你的技術堆疊（Spring/Quarkus？REST/UI？部署/CI 方式？），我可以為你繪製一個可立即運行的 Cucumber 骨架，包含推薦的插件和適合你設定的範例流水線。
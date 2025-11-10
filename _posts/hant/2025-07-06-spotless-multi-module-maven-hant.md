---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: 無瑕的多模組 Maven 專案
translated: true
type: note
---

### 在多模組 Maven 專案中使用 Spotless

Spotless 是一款適用於 Maven 和 Gradle 的程式碼格式化外掛。根據您提到的 Maven `-pl`（專案清單）參數，我假設您正在多模組 Java 專案中使用 **Spotless Maven 外掛**。這讓您可以選擇性地在特定模組上執行格式化檢查（例如透過 `spotless:check`）或套用修復（例如透過 `spotless:apply`），對於大型專案非常高效，因為您可能只需要格式化特定模組（例如在開發特定子模組時）。

#### 前置條件
- 您的專案使用 Maven 並具有多模組結構（在父級 `pom.xml` 中透過 `<modules>...</modules>` 定義）。
- Spotless Maven 外掛已在專案中配置（通常在父級 POM 或個別模組 POM 中）。如果尚未配置，請將以下內容加入您的 POM：
  ```xml
  <build>
    <plugins>
      <plugin>
        <groupId>com.diffplug.spotless</groupId>
        <artifactId>spotless-maven-plugin</artifactId>
        <version>2.43.0</version>  <!-- 請使用最新版本 -->
        <configuration>
          <!-- 在此處設定您的格式化規則，例如針對 Java、Groovy -->
        </configuration>
      </plugin>
    </plugins>
  </build>
  ```
  - 常見規則包括 Google Java Format、Eclipse JDT for Java，或針對導入、間距等的自訂設定。
  - Spotless 支援多種檔案類型（Java、Kotlin、XML 等），並能與 CI 工具良好整合，用於預提交掛鉤（透過 `spotless:check` 目標，該目標會在程式碼未格式化時使建置失敗）。

#### 使用 `-pl` 控制模組格式化
Maven 的 `-pl`（專案清單）參數讓您可以指定以逗號分隔的模組清單來包含在建置/外掛執行中。預設情況下，Maven 會在所有模組上執行，但 `-pl` 可以限制執行範圍，節省時間並避免對未受影響的模組進行不必要的工作。

- **基本指令結構**：
  - 檢查格式化（不套用變更）：`mvn spotless:check -pl module1,module2`
  - 套用格式化修復：`mvn spotless:apply -pl module1,module2`
  - 將 `module1,module2` 替換為實際的模組名稱（例如從根目錄開始的相對路徑，如 `core,api`）。

- **範例**：
  1. **僅在 `core` 模組上檢查格式化**：
     ```
     mvn spotless:check -pl core
     ```
     - 這僅掃描並驗證 `core` 的原始碼檔案。如果存在任何格式化問題，建置將失敗並顯示詳細資訊（例如「請執行 `spotless:apply` 以修復」）。

  2. **對多個模組（`api` 和 `utils`）套用格式化**：
     ```
     mvn spotless:apply -pl api,utils
     ```
     - 這會就地修改檔案以符合您的 Spotless 規則。套用後請務必提交變更，以避免版本控制中的意外。

  3. **在完整專案執行中排除特定模組**：使用 `-pl !moduleToSkip` 在*除了*某些模組之外的所有模組上執行（Maven 3.2.1+ 支援使用 `!` 進行否定）。
     - 範例：`mvn spotless:check -pl !legacy`（在除 `legacy` 之外的所有模組上執行）。

- **效率提示**：
  - **並行執行**：加入 `-T 4` 進行多執行緒建置（例如 `mvn spotless:check -pl core,api -T 4`）。
  - **預覽執行**：先使用 `spotless:check` 預覽問題而不進行變更——這是冪等且安全的。
  - **與 IDE/版本控制整合**：在您的 IDE 中配置 Spotless 在儲存/提交時執行（例如透過 IntelliJ 的 Spotless 外掛），或將其用作預提交掛鉤（透過 pre-commit 或 Git hooks 等工具）進行自動化檢查。
  - **處理反應器解析**：如果模組依賴關係複雜，Maven 在使用 `-pl` 時會自動解析它們，確保需要時先處理依賴模組。
  - **常見問題**：
    - 如果 `-pl` 無效，請確保模組已在 `<modules>` 中定義，並在存在歧義時使用完整路徑（例如在多儲存庫設定中使用 `-pl :core`）。
    - 對於 Gradle 使用者（如果您指的是 Spotless Gradle 外掛），等效參數是 `-p` 用於專案路徑，但您的查詢指定了 `-pl`，因此假設為 Maven。如果是 Gradle，請切換到類似 `gradle task -p submodule` 的外掛。

完整文件請參閱 [Spotless Maven 外掛文件](https://github.com/diffplug/spotless/tree/v2.43.0/plugin-maven)。如果您的設定不同（例如使用 Gradle），請提供更多詳細資訊以獲得針對性建議。
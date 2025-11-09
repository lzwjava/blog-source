---
audio: false
date: 2025-09-08
generated: true
image: false
lang: hant
layout: post
title: 模組化 Spring 應用程式的 IT 覆蓋範圍
translated: true
type: note
---

### 整體設定評估
您目前的配置對於像這樣的小型多模組專案來說相當穩固，特別是您已經實現了核心流程：將 JaCoCo 代理附加到 Jetty、透過 Exec 外掛程式執行外部 Python 整合測試，並在 `PlaygroundWeb` 模組中生成報告。這能從 Python 的 `unittest` 測試的 API 端點捕獲運行時覆蓋率，這正是您在 Spring Web 應用程式中進行整合測試 (IT) 覆蓋率所需的。

主要優勢：
- **模組化且階段綁定**：使用 Maven 階段（`pre-integration-test` 啟動 Jetty、`integration-test` 執行 Python 測試、`post-integration-test` 停止、`verify` 生成報告）確保了可靠性和可重現性。
- **代理附加**：在 Jetty 上設定的 JVM 參數 (`-javaagent:...`) 能正確檢測運行時，並在 `jacoco.it.exec` 中捕獲覆蓋率。
- **外部測試整合**：Exec 外掛程式能妥善處理 Python，並將測試保留在儲存庫根目錄 (`${project.parent.basedir}/tests`) 使其與 Java 模組解耦。
- **避免不必要的重複**：您沒有在 `PlaygroundUtils`（沒有控制器）中運行 Jetty/Python，這樣很有效率。

您已識別的挑戰：
- **對於像 `PlaygroundUtils` 這樣的函式庫模組的覆蓋率**：由於 utils 程式碼在 `PlaygroundWeb` JVM 中運行（作為 WAR 中的依賴項），它會被檢測並出現在 `PlaygroundWeb` 的 `jacoco.it.exec` 中。但您的報告是模組特定的，因此除非進行聚合或包含，否則 `PlaygroundUtils` 的覆蓋率不可見。
- **JaCoCo 的非自包含性質**：與 Checkstyle/Spotless（僅分析原始碼/靜態產物）不同，JaCoCo 需要來自外部測試和代理附加的運行時資料 (`.exec` 檔案)。這使得它在沒有仔細協調的多模組設定中顯得脆弱。
- **聚合目標的限制**：`jacoco:report-aggregate` 期望每個模組的 `.exec` 檔案（例如來自單元測試），但您的覆蓋率純粹來自一個模組的 IT。強制聚合可能導致像 `PlaygroundUtils` 這樣的函式庫出現空報告。
- **擴展到 10+ 個模組的可擴展性**：在模組間複製 Jetty/Python 設定將是浪費的（冗餘的伺服器/測試）。像複製 `.exec` 檔案或運行所有內容兩次（如您所述）這樣的臨時解決方案會引入維護開銷和建置時間膨脹。

您回退到每個模組的報告是務實的，但我們可以優化覆蓋率的包含而無需重複。

### 推薦策略
重點在於**在運行應用程式的模組（此處為 `PlaygroundWeb`）中生成單一、全面的 IT 覆蓋率報告**，同時**包含像 `PlaygroundUtils` 這樣的依賴模組的覆蓋率資料**。這避免了多次運行測試，並利用了所有程式碼在一個 JVM 中執行的事實。

為什麼選擇這個而不是聚合？
- 聚合 (`report-aggregate`) 更適合跨模組的分佈式單元測試覆蓋率。對於來自單個運行時（您的情況）的 IT 覆蓋率，它過於繁瑣且不自然契合。
- 統一的報告提供了應用程式覆蓋率的整體視圖，這通常比孤立的每個模組報告更有用（例如，「整體 80%，但 utils 層只有 60%」）。
- 對於較大的專案，透過將「應用程式模組」（WAR/EAR）視為覆蓋率中心來擴展，並拉入依賴項。

#### 為您的 2 模組專案逐步實施
從小處著手：將其應用於您當前的設定（1 個應用程式模組 + 1 個函式庫）。測試它，然後擴展。

1. **僅在 `PlaygroundWeb` 中保留 IT 執行**：
   - 這裡不需要更改。Jetty 啟動 WAR（其中嵌入了 `PlaygroundUtils`），Python 測試觸及端點，覆蓋率被捕獲在 `${project.build.directory}/jacoco.it.exec` 中。
   - 確認 utils 程式碼被執行：如果您的 Python 測試呼叫使用 `PlaygroundUtils` 類別（例如 `SystemUtils`）的端點，它們的覆蓋率將在 `.exec` 檔案中。

2. **增強 `PlaygroundWeb` 中的 JaCoCo 報告以包含 `PlaygroundUtils`**：
   - 在 `report` 目標中使用 JaCoCo 的 `<additionalClassesDirectories>` 和 `<additionalSourceDirectories>`。這告訴 JaCoCo 針對相同的 `.exec` 檔案掃描來自 `PlaygroundUtils` 的類別/原始碼。
   - 更新 `PlaygroundWeb` 的 POM（在 `jacoco-maven-plugin` 配置中）：

     ```xml
     <plugin>
         <groupId>org.jacoco</groupId>
         <artifactId>jacoco-maven-plugin</artifactId>
         <executions>
             <!-- 現有的 prepare-agent -->
             <execution>
                 <id>prepare-agent</id>
                 <goals>
                     <goal>prepare-agent</goal>
                 </goals>
             </execution>
             <!-- 增強的報告：包含 utils 模組 -->
             <execution>
                 <id>report-it</id>
                 <phase>verify</phase>
                 <goals>
                     <goal>report</goal>
                 </goals>
                 <configuration>
                     <dataFile>${jacoco.it.exec}</dataFile>
                     <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
                     <!-- 添加這些以包含 PlaygroundUtils 的覆蓋率 -->
                     <additionalClassesDirectories>
                         <directory>${project.parent.basedir}/PlaygroundUtils/target/classes</directory>
                     </additionalClassesDirectories>
                     <additionalSourceDirectories>
                         <directory>${project.parent.basedir}/PlaygroundUtils/src/main/java</directory>
                     </additionalSourceDirectories>
                 </configuration>
             </execution>
         </executions>
     </plugin>
     ```

   - 這會生成一個報告（在 `PlaygroundWeb/target/site/jacoco-it` 中），涵蓋兩個模組。您將看到按套件/類別的細分，包括來自 utils 的 `org.lzw`。

3. **在 `PlaygroundUtils` 中停用/移除 JaCoCo**：
   - 由於它沒有自己的 IT，請移除任何 JaCoCo 配置/屬性（例如 `<jacoco.it.exec>`、`<it.report.skip>`）。它不需要生成自己的報告——覆蓋率在上游處理。
   - 如果 utils 中有單元測試，請為單元覆蓋率（預設的 `jacoco.exec`）保留單獨的 `prepare-agent` + `report`，但將其與 IT 隔離。

4. **建置並驗證**：
   - 從父項目運行 `mvn clean verify`。
   - Jetty/Python 僅運行一次（在 `PlaygroundWeb` 中）。
   - 檢查 `PlaygroundWeb/target/site/jacoco-it/index.html`：它應該顯示兩個模組類別的覆蓋率。
   - 如果 utils 覆蓋率為 0%，請確保您的 Python 測試執行了那些類別（例如，添加一個透過端點觸發 `SystemUtils` 的測試）。

5. **可選：強制執行覆蓋率閾值**：
   - 在 `PlaygroundWeb` 的 JaCoCo 外掛程式中添加一個 `check` 執行，如果覆蓋率低於閾值（例如整體行覆蓋率 70%）則使建置失敗。
     ```xml
     <execution>
         <id>check-it</id>
         <goals>
             <goal>check</goal>
         </goals>
         <configuration>
             <dataFile>${jacoco.it.exec}</dataFile>
             <rules>
                 <rule>
                     <element>BUNDLE</element>
                     <limits>
                         <limit>
                             <counter>LINE</counter>
                             <value>COVEREDRATIO</value>
                             <minimum>0.70</minimum>
                         </limit>
                     </limits>
                 </rule>
             </rules>
         </configuration>
     </execution>
     ```

#### 擴展到更大的專案（例如 10 個模組）
對於 10+ 個模組（例如多個函式庫 + 1-2 個應用程式/WAR 模組），擴展上述方法以避免複雜性：

- **在應用程式模組中集中 IT**：如果您有一個主要的 WAR（如 `PlaygroundWeb`），使其成為「覆蓋率中心」。為所有依賴的函式庫添加 `<additionalClassesDirectories>` 和 `<additionalSourceDirectories>`（例如透過父 POM 中的循環或屬性列表）。
  - 範例：在父屬性中定義路徑：
    ```xml
    <properties>
        <lib1.classes>${project.basedir}/Lib1/target/classes</lib1.classes>
        <lib1.sources>${project.basedir}/Lib1/src/main/java</lib1.sources>
        <!-- 為 10 個函式庫重複 -->
    </properties>
    ```
  - 在 WAR 的 JaCoCo 報告配置中：動態引用它們。

- **如果有多個應用程式/WAR**：建立專用的 IT 模組（例如 `App1-IT`、`App2-IT`），這些模組依賴於 WAR，在那裡配置 Jetty/Exec/JaCoCo，並僅包含相關依賴項的類別/原始碼。這使得建置模組化（例如 `mvn verify -pl App1-IT` 用於目標覆蓋率）。

- **避免每個模組的 IT 重複**：切勿在函式庫模組中運行 Jetty/Python——這是浪費的。如果一個函式庫需要隔離的 IT（罕見），請為其提供自己的迷你伺服器/測試套件。

- **用於報告的聚合（如果需要）**：如果您堅持要單獨的每個模組報告：
  - 在應用程式模組中生成 `.exec`。
  - 在父項目的 `post-integration-test` 中使用 Maven 的 `dependency:copy` 或自訂腳本（透過 Exec 外掛程式）將 `.exec` 複製到每個函式庫的 `target/`（例如作為 `jacoco-it.exec`）。
  - 然後，配置每個函式庫中的 `report` 以使用該複製的檔案。
  - 但這更複雜——除非利益相關者要求每個模組的指標，否則優先選擇統一的報告。

- **擴展的工具提示**：
  - **Maven 設定檔**：使用設定檔（例如 `-Pcoverage`）來切換 IT/報告以加快開發建置。
  - **CI 優化**：在 CI（例如 GitHub Actions）中，快取 Maven 依賴項，並僅在測試/端點變更時運行 IT。
  - **如果 JaCoCo 變得太複雜的替代方案**：考慮使用 SonarQube 進行聚合分析（它會跨模組攝取 JaCoCo 資料）。或者切換到像 OpenClover 這樣的運行時工具，但如果您堅持使用中心方法，JaCoCo 也沒問題。
  - **測試的測試**：在 Python 中添加一個冒煙測試以驗證伺服器啟動（例如輪詢 `http://localhost:8080/health`）。

此策略最小化了運行次數（每個應用程式一個 Jetty/Python），乾淨地處理了 JaCoCo 的依賴關係，並且在擴展時不會爆炸式增長。如果您分享更多細節（例如 utils 如何在端點中使用），我可以進一步完善 POM 片段。
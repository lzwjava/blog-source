---
audio: false
generated: true
lang: hant
layout: post
title: Java中的Spotless與Checkstyle
translated: true
type: note
---

您可以在 Java 專案中同時使用 **Spotless Maven Plugin** 和 **Checkstyle Maven Plugin**，因為它們具有互補的作用。然而，您是否*需要*同時使用兩者，則取決於專案的需求。以下我將解釋它們如何協同工作、它們的差異，以及何時選擇其中一個而非另一個。

### Spotless 與 Checkstyle 的主要差異

| **方面**            | **Spotless**                                                                 | **Checkstyle**                                                              |
|-----------------------|------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| **目的**           | 自動格式化程式碼以強制執行一致的風格並修復問題。   | 靜態分析程式碼以強制執行編碼標準並檢測違規。  |
| **操作**            | 修改程式碼（例如，修復縮排、導入順序、移除未使用的導入）。 | 報告違規而不修改程式碼；如果檢查失敗則使建置失敗。      |
| **配置**     | 配置格式化工具如 `palantir-java-format`、`google-java-format` 等。 | 使用規則集（例如 Google 或 Sun 檢查）來定義編碼標準。      |
| **輸出**            | 格式化後的原始碼檔案（使用 `mvn spotless:apply`）。                          | 報告（XML、HTML 或控制台）列出風格違規。                   |
| **使用情境**          | 確保在提交或建置前程式碼格式一致。             | 強制執行編碼標準並捕獲格式化工具可能未處理的問題，如複雜性或不良實踐。 |

### 同時使用 Spotless 和 Checkstyle

您可以結合 Spotless 和 Checkstyle 來實現**自動格式化**和**風格強制執行**。以下是它們如何互補：

1. **Spotless 用於格式化**：
   - Spotless 使用如 `palantir-java-format` 等工具應用格式化規則（例如縮排、導入順序）。
   - 它確保程式碼格式一致，減少手動操作。
   - 範例：修復 2 空格與 4 空格縮排、排序導入並移除未使用的導入。

2. **Checkstyle 用於驗證**：
   - Checkstyle 強制執行格式化之外的編碼標準，例如方法長度、命名約定或複雜性。
   - 它捕獲格式化工具可能未處理的問題，例如缺少 Javadoc 或過於複雜的方法。
   - 範例：標記參數過多的方法或強制在公開方法上使用 Javadoc。

3. **工作流程**：
   - 首先執行 Spotless (`mvn spotless:apply`) 來格式化程式碼。
   - 然後執行 Checkstyle (`mvn checkstyle:check`) 來驗證是否符合其他規則。
   - 這確保程式碼既經過格式化，又符合更廣泛的風格指南。

### `pom.xml` 中的範例配置

以下是如何在您的 `pom.xml` 中配置這兩個插件：

```xml
<build>
    <plugins>
        <!-- Spotless Plugin for Formatting -->
        <plugin>
            <groupId>com.diffplug.spotless</groupId>
            <artifactId>spotless-maven-plugin</artifactId>
            <version>2.43.0</version>
            <configuration>
                <java>
                    <includes>
                        <include>src/main/java/**/*.java</include>
                        <include>src/test/java/**/*.java</include>
                    </includes>
                    <palantirJavaFormat>
                        <version>2.53.0</version>
                        <style>GOOGLE</style> <!-- Use Google style -->
                    </palantirJavaFormat>
                    <indent>
                        <spacesPerTab>2</spacesPerTab> <!-- 2-space indentation -->
                    </indent>
                    <importOrder>
                        <order>java,javax,org,com,\\#</order>
                    </importOrder>
                    <removeUnusedImports/>
                    <trimTrailingWhitespace/>
                    <endWithNewline/>
                </java>
            </configuration>
            <executions>
                <execution>
                    <goals>
                        <goal>apply</goal>
                    </goals>
                    <phase>validate</phase>
                </execution>
            </executions>
        </plugin>

        <!-- Checkstyle Plugin for Validation -->
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-checkstyle-plugin</artifactId>
            <version>3.4.0</version>
            <configuration>
                <configLocation>google_checks.xml</configLocation> <!-- Use Google style or custom XML -->
                <includeTestSourceDirectory>true</includeTestSourceDirectory>
                <failOnViolation>true</failOnViolation> <!-- Fail build on violations -->
                <consoleOutput>true</consoleOutput> <!-- Output violations to console -->
            </configuration>
            <executions>
                <execution>
                    <goals>
                        <goal>check</goal>
                    </goals>
                    <phase>validate</phase>
                </execution>
            </executions>
            <dependencies>
                <!-- Specify Checkstyle version -->
                <dependency>
                    <groupId>com.puppycrawl.tools</groupId>
                    <artifactId>checkstyle</artifactId>
                    <version>10.17.0</version>
                </dependency>
            </dependencies>
        </plugin>
    </plugins>
</build>
```

### 關鍵配置注意事項

1. **共享風格規則**：
   - 為避免衝突，請對齊 Spotless 和 Checkstyle 的配置。例如，在 Spotless 中使用 `palantirJavaFormat` 並設定 `style>GOOGLE`，並在 Checkstyle 中使用 `google_checks.xml`。
   - 從 [Checkstyle 的 GitHub](https://github.com/checkstyle/checkstyle/blob/master/src/main/resources/google_checks.xml) 下載 `google_checks.xml` 或建立自訂規則集。

2. **執行順序**：
   - 在 `validate` 階段先執行 Spotless，然後執行 Checkstyle，以確保在驗證前程式碼已格式化。
   - 範例：`mvn spotless:apply checkstyle:check`。

3. **自訂 Checkstyle 規則**：
   - 自訂 `google_checks.xml` 或建立您自己的規則集（例如 `my_checks.xml`）以強制執行特定規則，例如：
     ```xml
     <module name="Indentation">
         <property name="basicOffset" value="2"/>
         <property name="lineWrappingIndentation" value="4"/>
     </module>
     <module name="ImportOrder">
         <property name="groups" value="java,javax,org,com"/>
         <property name="ordered" value="true"/>
         <property name="separated" value="true"/>
     </module>
     ```

4. **避免冗餘**：
   - 如果 Spotless 處理格式化（例如縮排、導入順序），請停用重疊的 Checkstyle 規則以避免重複檢查。例如，如果 Spotless 強制執行縮排，則停用 Checkstyle 的 `Indentation` 模組：
     ```xml
     <module name="Indentation">
         <property name="severity" value="ignore"/>
     </module>
     ```

### 何時使用一個或同時使用兩者

- **單獨使用 Spotless**：
  - 如果您只需要一致的程式碼格式化（例如縮排、導入順序、空白字元）。
  - 適合希望自動格式化而不需要嚴格風格強制執行的團隊。
  - 範例：小型專案或使用 IDE 基礎格式化的團隊。

- **單獨使用 Checkstyle**：
  - 如果您需要強制執行編碼標準（例如命名約定、Javadoc、方法複雜性）而不修改程式碼。
  - 適合開發人員手動格式化程式碼但需要驗證的專案。

- **同時使用兩者**：
  - 為了實現穩健的程式碼品質：Spotless 自動格式化程式碼，Checkstyle 捕獲其他問題（例如缺少 Javadoc、複雜方法）。
  - 常見於大型團隊或具有嚴格編碼標準的專案。
  - 範例：需要一致風格和品質檢查的企業專案或開源儲存庫。

### 實際考量

- **效能**：執行兩個插件會增加建置時間。在 CI 管道中使用 `spotless:check`（而非 `apply`）和 `checkstyle:check` 來驗證而不修改程式碼。
- **IDE 整合**：
  - Spotless：使用 Spotless Gradle/Maven 任務或 IDE 插件（例如 IntelliJ 的 `palantir-java-format`）。
  - Checkstyle：使用 IntelliJ 的 Checkstyle-IDEA 插件或 Eclipse Checkstyle 插件，並配置相同的 `google_checks.xml`。
- **CI/CD**：在您的 CI 管道（例如 Jenkins、GitHub Actions）中配置這兩個插件，以在拉取請求時強制執行格式化和風格檢查。
  ```yaml
  # Example GitHub Actions workflow
  name: CI
  on: [pull_request]
  jobs:
    build:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v3
        - name: Set up JDK 17
          uses: actions/setup-java@v3
          with: { java-version: '17' }
        - name: Run Spotless and Checkstyle
          run: mvn spotless:check checkstyle:check
  ```

### 潛在衝突與解決方案

- **重疊規則**：如果 Spotless 的程式碼格式化方式與 Checkstyle 的規則不同（例如 2 空格與 4 空格縮排），建置可能會失敗。解決方案：對齊配置（例如兩者都使用 `GOOGLE` 風格）。
- **建置失敗**：如果 Spotless 尚未執行，Checkstyle 的 `failOnViolation` 可能會導致建置中斷。解決方案：確保 Spotless 先執行，或使用 `spotless:check` 來驗證格式化。
- **團隊接受度**：開發人員可能抗拒自動格式化。解決方案：在 CI 中使用 `spotless:check` 並教育團隊有關 IDE 整合。

### 來源

- Spotless 文件：[GitHub](https://github.com/diffplug/spotless/tree/main/plugin-maven)
- Checkstyle Maven Plugin：[Maven Site](https://maven.apache.org/plugins/maven-checkstyle-plugin/)
- Stack Overflow 和 GitHub issues 上的社群討論

### 結論

同時使用 Spotless 和 Checkstyle 是維護程式碼品質的強大組合：Spotless 確保一致的格式化，而 Checkstyle 強制執行更廣泛的編碼標準。配置它們以對齊（例如相同的縮排和導入順序規則），並在建置過程中依序執行它們。如果您的專案只需要格式化，單獨使用 Spotless 可能就足夠；如果您需要嚴格的驗證，請考慮加入 Checkstyle。如果您需要特定配置或範例 `google_checks.xml` 檔案的協助，請告訴我！
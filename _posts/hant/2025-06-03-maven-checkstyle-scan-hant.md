---
audio: false
generated: true
lang: hant
layout: post
title: Maven Checkstyle：繼續掃描
translated: true
type: note
---

要讓 `mvn checkstyle:check` 在遇到違規時不立即失敗，而是繼續掃描所有模組，你需要配置 Checkstyle Maven 插件來停用 `failOnViolation` 選項。預設情況下，`failOnViolation` 設定為 `true`，這會導致在發現違規時立即停止建置。將其設為 `false` 可讓掃描在所有模組中完成，並回報所有違規而不中斷建置。

### 解決方案
更新你的 `pom.xml`，按以下方式配置 Checkstyle 插件：

```xml
<build>
  <plugins>
    <plugin>
      <groupId>org.apache.maven.plugins</groupId>
      <artifactId>maven-checkstyle-plugin</artifactId>
      <version>3.3.1</version> <!-- 使用最新版本 -->
      <configuration>
        <failOnViolation>false</failOnViolation>
        <logViolationsToConsole>true</logViolationsToConsole> <!-- 可選：將違規記錄到控制台 -->
      </configuration>
      <executions>
        <execution>
          <id>checkstyle</id>
          <phase>validate</phase> <!-- 或你偏好的階段 -->
          <goals>
            <goal>check</goal>
          </goals>
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

### 說明
- **`<failOnViolation>false</failOnViolation>`**：此設定可防止在檢測到 Checkstyle 違規時導致建置失敗，讓掃描能在所有模組中繼續進行。
- **`<logViolationsToConsole>true</logViolationsToConsole>`**：（可選）確保即使建置未失敗，違規資訊也會輸出到控制台以供查看。
- **執行階段**：`<phase>validate</phase>` 將 Checkstyle 檢查綁定到 Maven 生命週期的 `validate` 階段。如果需要在不同階段執行（例如 `compile`、`verify`），可調整此階段設定。

### 執行指令
再次執行指令：
```bash
mvn checkstyle:check
```
將 `failOnViolation` 設為 `false` 後，Maven 將會掃描所有模組，回報所有違規，並完成建置而不會提前停止。

### 注意事項
- 請確保你使用的是最新版本的 `maven-checkstyle-plugin`（例如範例中的 3.3.1）。如有需要，請在 Maven Central 檢查最新版本。
- 如果你在多模組專案中工作，此配置將應用於所有模組，除非在子 `pom.xml` 中被覆寫。
- 要生成違規報告，可考慮改為執行 `mvn checkstyle:checkstyle`，該指令預設會產生 HTML 報告且不會導致建置失敗。

如果你有特定需求（例如自訂 Checkstyle 規則或不同設定），請告知，我可以進一步調整解決方案！
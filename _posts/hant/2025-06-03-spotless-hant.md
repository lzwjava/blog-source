---
audio: false
generated: true
lang: hant
layout: post
title: 使用 Spotless 格式化代碼
translated: true
type: note
---

Maven Checkstyle Plugin 中並沒有 `mvn checkstyle:format` 指令。該插件主要用於根據 Checkstyle 配置檢查程式碼並回報違規情況，而非自動格式化程式碼。不過，您可以使用其他工具（例如 Spotless 或 Maven Formatter Plugin）來實現基於 Checkstyle 配置的程式碼格式化，這些工具可配置為符合您的 Checkstyle 規則。

以下將說明如何使用 **Spotless Maven Plugin** 根據您的 Checkstyle 配置來格式化程式碼，這是目前較為流行的選擇，且能與 Checkstyle 規則整合。

### 解決方案：使用 Spotless 與 Checkstyle 配置

Spotless Maven Plugin 可根據 Checkstyle 配置文件（例如 `checkstyle.xml`）來格式化 Java 程式碼。設定方式如下：

#### 1. 將 Spotless 加入您的 `pom.xml`
將 Spotless 插件加入您的 `pom.xml`，並配置其使用您的 Checkstyle 配置文件。

```xml
<build>
  <plugins>
    <plugin>
      <groupId>com.diffplug.spotless</groupId>
      <artifactId>spotless-maven-plugin</artifactId>
      <version>2.43.0</version> <!-- 請使用最新版本 -->
      <configuration>
        <java>
          <!-- 指向您的 Checkstyle 配置文件 -->
          <googleJavaFormat>
            <version>1.22.0</version> <!-- 可選：使用特定版本 -->
            <style>GOOGLE</style> <!-- 或 AOSP，或省略使用預設值 -->
          </googleJavaFormat>
          <formatAnnotations>
            <!-- 使用 Checkstyle 配置進行格式化 -->
            <checkstyle>
              <file>${project.basedir}/checkstyle.xml</file> <!-- 您的 Checkstyle 配置路徑 -->
              <version>10.17.0</version> <!-- 請與您的 Checkstyle 版本匹配 -->
            </checkstyle>
          </formatAnnotations>
        </java>
      </configuration>
      <executions>
        <execution>
          <goals>
            <goal>apply</goal> <!-- 自動格式化程式碼 -->
          </goals>
          <phase>process-sources</phase> <!-- 可選：綁定至特定階段 -->
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

#### 2. 確保您的 Checkstyle 配置存在
請確保您的專案中有 `checkstyle.xml` 文件（例如在根目錄或子目錄中）。此文件定義了 Spotless 用於格式化程式碼的編碼標準（例如縮排、空格等）。如果您使用標準格式（如 Google Java Format），可以引用它，或使用為您的專案量身定制的自定義 Checkstyle 配置。

基本格式化規則的 `checkstyle.xml` 範例片段：
```xml
<?xml version="1.0"?>
<!DOCTYPE module PUBLIC "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN" "https://checkstyle.sourceforge.io/dtds/configuration_1_3.dtd">
<module name="Checker">
  <module name="TreeWalker">
    <module name="Indentation">
      <property name="basicOffset" value="2"/>
      <property name="braceAdjustment" value="0"/>
    </module>
  </module>
</module>
```

#### 3. 執行 Spotless 以格式化程式碼
要根據 Checkstyle 配置格式化程式碼，請執行：
```bash
mvn spotless:apply
```

此指令將根據您的 Checkstyle 配置中定義的規則以及任何其他格式化設定（例如 Google Java Format）來格式化專案中的所有 Java 文件。

#### 4. 使用 Checkstyle 驗證格式化
格式化後，您可以執行 `mvn checkstyle:check` 來驗證格式化後的程式碼是否符合您的 Checkstyle 規則。如果您之前按照建議設定了 `<failOnViolation>false</failOnViolation>`，則它將回報任何剩餘的違規情況而不會停止建置。

### 替代方案：Maven Formatter Plugin
如果您不想使用 Spotless，也可以使用 **Maven Formatter Plugin**，它同樣支援基於規則的格式化，但較少直接與 Checkstyle 配置一起使用。基本設定如下：

```xml
<build>
  <plugins>
    <plugin>
      <groupId>net.revelc.code.formatter</groupId>
      <artifactId>formatter-maven-plugin</artifactId>
      <version>2.23.0</version> <!-- 請使用最新版本 -->
      <configuration>
        <configFile>${project.basedir}/checkstyle.xml</configFile> <!-- Checkstyle 配置路徑 -->
      </configuration>
      <executions>
        <execution>
          <goals>
            <goal>format</goal>
          </goals>
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

執行格式化指令：
```bash
mvn formatter:format
```

### 注意事項
- **無直接的 Checkstyle 格式化指令**：Checkstyle Maven Plugin 不提供 `format` 目標。需要使用 Spotless 或 Formatter Plugin 等工具來應用基於 Checkstyle 規則的格式化。
- **Checkstyle 版本相容性**：請確保在 Spotless（或 Formatter）中指定的 Checkstyle 版本與您 Checkstyle 插件中使用的版本一致，以避免規則不匹配。
- **自定義 Checkstyle 規則**：您的 `checkstyle.xml` 必須包含與格式化相關的規則（例如 `Indentation`、`WhitespaceAround` 等），Spotless 才能正確應用它們。
- **多模組專案**：在 Maven 多模組專案中，您可以將 Spotless/Formatter 配置放在父 `pom.xml` 中以應用於所有模組，或根據需要為每個模組單獨配置。
- **格式化後檢查**：格式化後請務必執行 `mvn checkstyle:check` 以確認符合規範，特別是當您的 Checkstyle 配置中包含非格式化規則（例如方法長度、複雜度）時。

如果您沒有 `checkstyle.xml` 或需要協助創建，請告知，我可以提供範例或進一步指導！此外，如果您偏好使用其他工具或有特定的格式化要求，請分享，我將相應調整解決方案。
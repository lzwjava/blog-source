---
audio: false
generated: true
lang: hant
layout: post
title: 停用 Checkstyle 中的 Javadoc 檢查
translated: true
type: note
---

要設定 Checkstyle 忽略所有 Javadoc 相關檢查並將其視為非違規，你需要修改 Checkstyle 設定檔（通常是 `checkstyle.xml`），以停用或抑制 Javadoc 相關模組。以下是具體做法：

### 選項 1：停用 Javadoc 相關檢查
Checkstyle 有多個 Javadoc 相關模組，例如 `JavadocMethod`、`JavadocType`、`JavadocVariable`、`JavadocStyle` 和 `JavadocPackage`。要停用它們，請確保在設定檔中移除或註解這些模組。例如：

```xml
<module name="Checker">
    <!-- 其他模組 -->
    <!-- 註解或移除 Javadoc 相關檢查 -->
    <!--
    <module name="JavadocMethod"/>
    <module name="JavadocType"/>
    <module name="JavadocVariable"/>
    <module name="JavadocStyle"/>
    <module name="JavadocPackage"/>
    -->
</module>
```

如果這些模組不存在於你的設定中，Checkstyle 將不會強制執行 Javadoc 檢查。

### 選項 2：使用抑制篩選器來抑制 Javadoc 檢查
你可以使用 Checkstyle 的 `SuppressionFilter` 來抑制整個程式碼庫中所有 Javadoc 相關檢查。將抑制規則新增到獨立的抑制檔案（例如 `suppressions.xml`）中，並在 Checkstyle 設定中引用該檔案。

1. **建立抑制檔案**（例如 `suppressions.xml`）：
   ```xml
   <!DOCTYPE suppressions PUBLIC
       "-//Checkstyle//DTD Suppression DTD 1.0//EN"
       "https://checkstyle.org/dtds/suppressions_1_0.dtd">
   <suppressions>
       <!-- 抑制所有 Javadoc 相關檢查 -->
       <suppress checks="Javadoc.*" files=".*"/>
   </suppressions>
   ```

   `checks="Javadoc.*"` 模式會匹配所有以 "Javadoc" 開頭的檢查（例如 `JavadocMethod`、`JavadocType` 等），而 `files=".*"` 會將抑制規則應用於所有檔案。

2. **在 Checkstyle 設定中引用抑制檔案**：
   ```xml
   <module name="Checker">
       <module name="SuppressionFilter">
           <property name="file" value="suppressions.xml"/>
       </module>
       <!-- 其他模組 -->
   </module>
   ```

### 選項 3：使用 `@SuppressWarnings` 註解
如果你只想針對特定類別或方法抑制 Javadoc 檢查，可以在 Java 程式碼中使用 `@SuppressWarnings("checkstyle:javadoc")` 註解。例如：

```java
@SuppressWarnings("checkstyle:javadoc")
public class MyClass {
    // 沒有 Javadoc 的程式碼將不會觸發違規
}
```

這種方法適用於針對性抑制，但需要在程式碼中新增註解，可能不適合全域停用 Javadoc 檢查。

### 注意事項
- **驗證設定**：修改設定後，請執行 Checkstyle 以確保不再報告 Javadoc 相關違規。例如使用指令：
  ```bash
  java -jar checkstyle.jar -c checkstyle.xml YourSourceFiles
  ```
- **常見 Javadoc 模組**：請確保處理所有相關模組，包括 `JavadocMethod`、`JavadocType`、`JavadocVariable`、`JavadocStyle`、`JavadocPackage`、`MissingJavadocMethod`、`MissingJavadocType` 和 `InvalidJavadocPosition`。
- **Checkstyle 版本**：確切的模組名稱和抑制語法可能因 Checkstyle 版本而略有不同。以上範例相容於 Checkstyle 8.x 及更高版本。
- **全域抑制**：`SuppressionFilter` 方法（選項 2）通常是停用所有 Javadoc 檢查最簡潔的方式，無需大幅修改核心設定。

如果你正在使用特定的建置工具（如 Maven 或 Gradle），請告訴我，我可以提供有關整合更新後 Checkstyle 設定的進一步指引！
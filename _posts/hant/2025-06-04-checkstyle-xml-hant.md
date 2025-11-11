---
audio: false
generated: true
lang: hant
layout: post
title: Checkstyle 配置
translated: true
type: note
---

這是一份以 XML 撰寫的 Checkstyle 設定檔，旨在根據 Sun 編碼規範、Java 語言規範、Javadoc 指南及額外最佳實踐，為 Java 程式碼強制執行編碼標準與最佳實踐。Checkstyle 是一種靜態程式碼分析工具，用於檢查 Java 原始碼是否符合預定義的規則集。以下將說明此設定檔的結構與關鍵元件。

---

### **概覽**
- **目的**：此檔案定義了檢查 Java、properties 及 XML 檔案是否違反編碼標準的規則，包括格式、命名約定、Javadoc 要求及程式碼結構。
- **結構**：設定採用階層式結構，使用 `<module>` 元素，從根模組 `Checker` 開始，其中包含其他用於特定檢查或篩選器的模組。
- **標準**：符合以下規範：
  - Java 語言規範 (Java SE 11)
  - Sun 編碼慣例
  - Javadoc 指南
  - JDK API 文件
  - 通用最佳實踐
- **關鍵特性**：
  - 可設定的嚴重性（設為 `error`）。
  - 支援副檔名：`.java`、`.properties`、`.xml`。
  - 允許透過抑制檔案或 `@SuppressWarnings` 註解來抑制特定檢查。

---

### **根模組：`<module name="Checker">`**
`Checker` 模組是頂層模組，負責協調所有檢查與篩選器。

- **屬性**：
  - `severity="error"`：將所有違規視為錯誤（其他選項包括 `warning` 或 `info`）。
  - `fileExtensions="java, properties, xml"`：將檢查應用於 `.java`、`.properties` 及 `.xml` 檔案。

- **子模組**：
  - **檔案篩選器**：
    - `BeforeExecutionExclusionFileFilter`：排除 `module-info.java` 檔案免受檢查（使用正規表達式 `module\-info\.java$`）。
  - **抑制篩選器**：
    - `SuppressionFilter`：從檔案載入抑制規則（預設：`checkstyle-suppressions.xml`）。若檔案不存在，則為可選（`optional="true"`）。
    - `SuppressWarningsFilter`：啟用透過程式碼中的 `@SuppressWarnings("checkstyle:...")` 註解來抑制特定檢查。
  - **雜項檢查**：
    - `JavadocPackage`：確保每個套件都有包含 Javadoc 的 `package-info.java` 檔案。
    - `NewlineAtEndOfFile`：檢查檔案是否以換行字元結尾。
    - `Translation`：驗證 properties 檔案（例如用於國際化）在翻譯中是否包含相同的鍵。
  - **大小檢查**：
    - `FileLength`：檢查檔案的總長度（除非覆寫，否則適用預設限制）。
    - `LineLength`：確保 `.java` 檔案中的行不超過預設長度（通常為 80 或 120 個字元，可設定）。
  - **空白字元檢查**：
    - `FileTabCharacter`：禁止原始檔中使用定位字元（強制使用空格進行縮排）。
    - `RegexpSingleline`：偵測行尾空白（以 `\s+$` 結尾的行），並回報訊息「行尾包含空白字元」。
  - **標頭檢查**（已註解）：
    - `Header`：若取消註解，將對 `.java` 檔案強制執行特定檔案標頭（例如版權聲明），從 `checkstyle.header.file` 指定的檔案中讀取。

---

### **子模組：`<module name="TreeWalker">`**
`TreeWalker` 模組處理 Java 原始碼的抽象語法樹（AST），以執行詳細檢查。它包含多個按類別分組的子模組。

#### **Javadoc 檢查**
這些檢查強制執行類別、方法及變數的正確 Javadoc 註解：
- `InvalidJavadocPosition`：確保 Javadoc 註解位置正確（例如在類別或方法之前，而非其他地方）。
- `JavadocMethod`：檢查方法是否有正確的 Javadoc 註解，包括參數、回傳型別及例外。
- `JavadocType`：確保類別、介面及列舉有 Javadoc 註解。
- `JavadocVariable`：要求公開/受保護欄位有 Javadoc。
- `JavadocStyle`：強制執行 Javadoc 的樣式規則（例如正確的 HTML 標籤，無格式錯誤的註解）。
- `MissingJavadocMethod`：標記缺少 Javadoc 註解的方法。

#### **命名約定**
這些檢查確保識別符（變數、方法、類別等）遵循命名約定：
- `ConstantName`：常數（例如 `static final`）必須遵循命名模式（通常為 `UPPER_CASE`）。
- `LocalFinalVariableName`：區域 `final` 變數必須遵循命名模式（例如 `camelCase`）。
- `LocalVariableName`：區域變數必須遵循命名模式（例如 `camelCase`）。
- `MemberName`：實例欄位必須遵循命名模式（例如 `camelCase`）。
- `MethodName`：方法必須遵循命名模式（例如 `camelCase`）。
- `PackageName`：套件必須遵循命名模式（例如小寫加點，如 `com.example`）。
- `ParameterName`：方法參數必須遵循命名模式（例如 `camelCase`）。
- `StaticVariableName`：靜態（非 final）欄位必須遵循命名模式。
- `TypeName`：類別/介面/列舉名稱必須遵循命名模式（例如 `UpperCamelCase`）。

#### **匯入檢查**
這些檢查規範 `import` 陳述式的使用：
- `AvoidStarImport`：禁止萬用字元匯入（例如 `import java.util.*`）。
- `IllegalImport`：阻止從受限制套件匯入（預設為 `sun.*`）。
- `RedundantImport`：標記重複或不必要的匯入。
- `UnusedImports`：偵測未使用的匯入（忽略 Javadoc 相關匯入，設 `processJavadoc="false"`）。

#### **大小檢查**
這些檢查限制方法與參數的大小：
- `MethodLength`：確保方法不超過最大行數（預設通常為 150）。
- `ParameterNumber`：限制方法中的參數數量（預設通常為 7）。

#### **空白字元檢查**
這些檢查強制程式碼中空白字元的一致性使用：
- `EmptyForIteratorPad`：檢查空 `for` 迴圈迭代器中的填充（例如 `for (int i = 0; ; i++)`）。
- `GenericWhitespace`：確保泛型型別周圍的間距正確（例如 `List<String>`）。
- `MethodParamPad`：檢查方法參數列表前的間距。
- `NoWhitespaceAfter`：禁止特定權杖後的空白字元（例如 `++` 或陣列）。
- `NoWhitespaceBefore`：禁止特定權杖前的空白字元（例如分號）。
- `OperatorWrap`：確保運算子（例如 `+`、`=`）位於正確的行。
- `ParenPad`：檢查括號內的間距（例如 `( x )` 對比 `(x)`）。
- `TypecastParenPad`：確保型別轉換中的間距正確。
- `WhitespaceAfter`：要求特定權杖後有空白字元（例如逗號、分號）。
- `WhitespaceAround`：確保運算子與關鍵字周圍有空白字元（例如 `if (x == y)`）。

#### **修飾符檢查**
這些檢查規範 Java 修飾符的使用：
- `ModifierOrder`：確保修飾符順序正確（例如 `public static final`，符合 JLS）。
- `RedundantModifier`：標記不必要的修飾符（例如 `final` 類別中的 `final`）。

#### **區塊檢查**
這些檢查強制程式碼區塊（`{}`）的正確使用：
- `AvoidNestedBlocks`：禁止不必要的巢狀區塊（例如 `{ { ... } }`）。
- `EmptyBlock`：標記空區塊（例如 `{}`），除非是故意的。
- `LeftCurly`：確保左大括號（`{`）位置正確（例如位於行尾）。
- `NeedBraces`：要求單一陳述式區塊使用大括號（例如 `if (x) y();` 必須為 `if (x) { y(); }`）。
- `RightCurly`：確保右大括號（`}`）位置正確（例如在新行或同一行，依樣式而定）。

#### **編碼問題檢查**
這些檢查識別常見的編碼問題：
- `EmptyStatement`：標記空陳述式（例如 `;;`）。
- `EqualsHashCode`：確保若覆寫 `equals()`，則也必須覆寫 `hashCode()`。
- `HiddenField`：偵測被區域變數或參數遮蔽的欄位。
- `IllegalInstantiation`：禁止特定類別的實例化（例如 `java.lang` 類別如 `String`）。
- `InnerAssignment`：不允許在表達式中進行賦值（例如 `if (x = y)`）。
- `MagicNumber`：標記硬編碼的數字字面值（例如 `42`），除非在特定情境中。
- `MissingSwitchDefault`：要求 `switch` 陳述式中有 `default` 情況。
- `MultipleVariableDeclarations`：禁止在單行中宣告多個變數（例如 `int x, y;`）。
- `SimplifyBooleanExpression`：標記過於複雜的布林表達式（例如 `if (x == true)`）。
- `SimplifyBooleanReturn`：簡化布林回傳陳述式（例如 `if (x) return true; else return false;`）。

#### **類別設計檢查**
這些檢查強制執行良好的類別設計實踐：
- `DesignForExtension`：確保非 final 類別有受保護或抽象方法以支援擴充。
- `FinalClass`：將僅有私有建構子的類別標記為 `final` 的候選。
- `HideUtilityClassConstructor`：確保工具類別（僅有靜態成員）有私有建構子。
- `InterfaceIsType`：禁止僅作為標記介面（無方法）使用的介面。
- `VisibilityModifier`：強制執行欄位的適當可見性（例如偏好私有欄位與 getter/setter）。

#### **雜項檢查**
- `ArrayTypeStyle`：強制執行一致的陣列宣告樣式（例如 `int[]` 對比 `int []`）。
- `FinalParameters`：要求方法參數盡可能為 `final`。
- `TodoComment`：標記程式碼中的 `TODO` 註解（用於追蹤未完成工作）。
- `UpperEll`：確保長整數字面值使用字母 `L`（例如 `100L` 而非 `100l`）。

#### **抑制篩選器（TreeWalker 內部）**
- `SuppressionXpathFilter`：允許使用檔案中定義的 XPath 表達式來抑制檢查（預設：`checkstyle-xpath-suppressions.xml`，可選）。
- `SuppressWarningsHolder`：支援 `@SuppressWarnings("checkstyle:...")` 註解，用於在 AST 內抑制特定檢查。

---

### **關鍵點**
- **可設定性**：大多數模組有預設設定，但可透過屬性自訂（例如 `LineLength` 可設定特定 `max` 長度）。
- **抑制**：設定支援透過外部檔案（`checkstyle-suppressions.xml`、`checkstyle-xpath-suppressions.xml`）或註解靈活抑制檢查。
- **可擴充性**：可新增額外檢查，並可透過註解或移除來停用現有檢查。
- **文件**：設定參考 Checkstyle 文件（例如 `https://checkstyle.org`）以取得各模組的詳細說明。
- **標頭檢查**：`Header` 模組已被註解，因此除非取消註解並設定標頭檔案，否則不會啟用。

---

### **使用方式**
1. **整合**：此檔案通常與建置工具如 Maven、Gradle 或 IDE 外掛一起使用，在建置過程或開發中執行 Checkstyle。
2. **違規回報**：當程式碼違反規則時（例如行超過最大長度），Checkstyle 會將其回報為錯誤（因 `severity="error"`）。
3. **抑制**：開發者可透過 `@SuppressWarnings("checkstyle:<check-name>")` 或在抑制檔案中定義規則來抑制特定違規。
4. **自訂**：屬性如 `basedir`、`checkstyle.header.file` 或抑制檔案路徑可外部設定（例如透過建置工具設定）。

---

### **違規範例**
- **JavadocMethod**：無 Javadoc 的公開方法將觸發錯誤。
- **LineLength**：`.java` 檔案中的行超過預設最大值（例如 80 個字元）將被標記。
- **AvoidStarImport**：使用 `import java.util.*` 將導致錯誤。
- **MagicNumber**：寫入 `int x = 42;` 而無命名常數將被標記。

---

若需特定模組的詳細說明、違規範例或自訂此設定的指引，請告知！
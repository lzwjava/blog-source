---
audio: false
generated: true
lang: hant
layout: post
title: 簡明解讀 Checkstyle 規則
translated: true
type: note
---

以下我將詳細說明您提供的 Checkstyle 配置文件中每個規則，並附上會**違反**該規則的簡短程式碼範例及觸發原因簡述。這些規則將按照您描述中的類別分組，我會保持解釋簡潔並確保清晰度。除非另有說明，每個範例皆假設規則使用預設設定啟用。對於可配置屬性的規則（例如行長度限制），除非另有說明，我將使用典型預設值（例如 LineLength 的 80 個字元）。

---

### 根模組：`<module name="Checker">`
`Checker` 模組是所有檢查與篩選器的頂層協調器。它適用於 `.java`、`.properties` 和 `.xml` 檔案，並將嚴重級別設定為 `error`。

#### 屬性
- **severity="error"**：所有違規皆視為錯誤。
- **fileExtensions="java, properties, xml"**：檢查適用於這些檔案類型。

---

### 檔案篩選器
這些篩選器決定哪些檔案需要接受檢查。

1. **BeforeExecutionExclusionFileFilter**
   - **目的**：排除符合正則表示式的檔案（例如 `module-info.java`）。
   - **違規範例**：
     ```java
     // module-info.java
     module com.example {
         requires java.base;
     }
     ```
   - **觸發原因**：此檔案符合正則表示式 `module\-info\.java$` 並被排除在檢查之外。此檔案不會產生違規，但其他檔案仍會被檢查。

2. **SuppressionFilter**
   - **目的**：根據檔案中的規則（例如 `checkstyle-suppressions.xml`）抑制檢查。
   - **違規範例**：如果 `checkstyle-suppressions.xml` 抑制了特定檔案的 `LineLength` 檢查，則該檔案中的長行不會被標記。若無抑制：
     ```java
     public class MyClass { // 這行非常長，超過了預設的 80 個字元最大長度限制，導致錯誤。
     }
     ```
   - **觸發原因**：若無抑制規則，長行會違反 `LineLength`。

3. **SuppressWarningsFilter**
   - **目的**：允許使用 `@SuppressWarnings("checkstyle:<check-name>")` 來抑制檢查。
   - **違規範例**：
     ```java
     public class MyClass {
         int my_field; // 違反 MemberName（非駝峰式命名）
     }
     ```
     ```java
     @SuppressWarnings("checkstyle:MemberName")
     public class MyClass {
         int my_field; // 因抑制而無違規
     }
     ```
   - **觸發原因**：未經抑制時，`my_field` 違反 `MemberName`（預期為駝峰式命名，例如 `myField`）。

---

### 雜項檢查
這些檢查適用於一般檔案屬性。

4. **JavadocPackage**
   - **目的**：確保每個套件都有包含 Javadoc 的 `package-info.java`。
   - **違規範例**：
     ```java
     // com/example/package-info.java（缺少或無 Javadoc）
     package com.example;
     ```
   - **觸發原因**：缺少 Javadoc 註釋（例如 `/** 套件描述 */`）。

5. **NewlineAtEndOfFile**
   - **目的**：確保檔案以換行符結尾。
   - **違規範例**：
     ```java
     public class MyClass {} // 結尾無換行符
     ```
   - **觸發原因**：檔案結尾缺少換行字元。

6. **Translation**
   - **目的**：驗證用於國際化的 `.properties` 檔案具有一致的鍵值。
   - **違規範例**：
     ```properties
     # messages.properties
     key1=Hello
     key2=World
     ```
     ```properties
     # messages_fr.properties
     key1=Bonjour
     # 缺少 key2
     ```
   - **觸發原因**：`messages_fr.properties` 缺少 `messages.properties` 中存在的 `key2`。

---

### 大小檢查
這些檢查強制執行檔案和行長度的限制。

7. **FileLength**
   - **目的**：限制檔案總行數（預設通常為 2000 行）。
   - **違規範例**：一個 2001 行的 Java 檔案。
   - **觸發原因**：超過預設行數限制。

8. **LineLength**
   - **目的**：確保行不超過最大長度（預設 80 個字元）。
   - **違規範例**：
     ```java
     public class MyClass { public void myMethodWithVeryLongNameToExceedEightyCharactersInALine() {} }
     ```
   - **觸發原因**：行超過 80 個字元。

---

### 空白字元檢查
這些檢查強制執行一致的空白字元使用。

9. **FileTabCharacter**
   - **目的**：禁止在原始碼檔案中使用定位字元（`\t`）。
   - **違規範例**：
     ```java
     public class MyClass {
     →    int x; // 使用定位字元進行縮排
     }
     ```
   - **觸發原因**：使用了定位字元而非空格。

10. **RegexpSingleline**
    - **目的**：偵測行尾空白字元（以 `\s+$` 結尾的行）。
    - **違規範例**：
      ```java
      public class MyClass {   // 結尾空格
      }
      ```
    - **觸發原因**：行尾包含空白字元。

---

### 標頭檢查（已註解）
11. **Header**
    - **目的**：強制執行特定的檔案標頭（例如版權宣告），來源自 `checkstyle.header.file`。
    - **違規範例**（若啟用）：
      ```java
      // 缺少標頭
      public class MyClass {}
      ```
    - **觸發原因**：缺少必要的標頭（例如 `// Copyright 2025 Example Inc.`）。

---

### 子模組：`<module name="TreeWalker">`
`TreeWalker` 處理 Java AST 以進行詳細檢查。

#### Javadoc 檢查
這些檢查強制執行正確的 Javadoc 註釋。

12. **InvalidJavadocPosition**
    - **目的**：確保 Javadoc 註釋位於類別/方法之前，而非其他地方。
    - **違規範例**：
      ```java
      public class MyClass {
          /** 這是錯誤放置的 Javadoc */
          int x;
      }
      ```
    - **觸發原因**：Javadoc 不在類別/方法宣告之前。

13. **JavadocMethod**
    - **目的**：檢查方法是否具有正確的 Javadoc（參數、傳回值、例外）。
    - **違規範例**：
      ```java
      public int add(int a, int b) { return a + b; }
      ```
    - **觸發原因**：公開方法缺少 Javadoc。

14. **JavadocType**
    - **目的**：確保類別/介面/列舉具有 Javadoc。
    - **違規範例**：
      ```java
      public class MyClass {}
      ```
    - **觸發原因**：類別缺少 Javadoc。

15. **JavadocVariable**
    - **目的**：要求公開/受保護欄位必須有 Javadoc。
    - **違規範例**：
      ```java
      public class MyClass {
          public int x;
      }
      ```
    - **觸發原因**：公開欄位缺少 Javadoc。

16. **JavadocStyle**
    - **目的**：強制執行 Javadoc 風格（例如有效的 HTML、無格式錯誤的註釋）。
    - **違規範例**：
      ```java
      /** 結尾缺少句點 */
      public class MyClass {}
      ```
    - **觸發原因**：Javadoc 結尾缺少句點。

17. **MissingJavadocMethod**
    - **目的**：標記缺少 Javadoc 的方法。
    - **違規範例**：
      ```java
      public void myMethod() {}
      ```
    - **觸發原因**：公開方法缺少 Javadoc。

---

#### 命名慣例
這些檢查強制執行命名模式。

18. **ConstantName**
    - **目的**：常數（`static final`）必須為 `UPPER_CASE`。
    - **違規範例**：
      ```java
      public class MyClass {
          static final int myConstant = 42;
      }
      ```
    - **觸發原因**：`myConstant` 應為 `MY_CONSTANT`。

19. **LocalFinalVariableName**
    - **目的**：區域 `final` 變數必須為 `camelCase`。
    - **違規範例**：
      ```java
      public void myMethod() {
          final int MY_VAR = 1;
      }
      ```
    - **觸發原因**：`MY_VAR` 應為 `myVar`。

20. **LocalVariableName**
    - **目的**：區域變數必須為 `camelCase`。
    - **違規範例**：
      ```java
      public void myMethod() {
          int MY_VAR = 1;
      }
      ```
    - **觸發原因**：`MY_VAR` 應為 `myVar`。

21. **MemberName**
    - **目的**：執行個體欄位必須為 `camelCase`。
    - **違規範例**：
      ```java
      public class MyClass {
          int my_field;
      }
      ```
    - **觸發原因**：`my_field` 應為 `myField`。

22. **MethodName**
    - **目的**：方法必須為 `camelCase`。
    - **違規範例**：
      ```java
      public void MyMethod() {}
      ```
    - **觸發原因**：`MyMethod` 應為 `myMethod`。

23. **PackageName**
    - **目的**：套件必須為小寫並包含點號（例如 `com.example`）。
    - **違規範例**：
      ```java
      package com.Example;
      ```
    - **觸發原因**：`Example` 應為 `example`。

24. **ParameterName**
    - **目的**：方法參數必須為 `camelCase`。
    - **違規範例**：
      ```java
      public void myMethod(int MY_PARAM) {}
      ```
    - **觸發原因**：`MY_PARAM` 應為 `myParam`。

25. **StaticVariableName**
    - **目的**：靜態（非常數）欄位必須遵循命名模式。
    - **違規範例**：
      ```java
      public class MyClass {
          static int MY_FIELD;
      }
      ```
    - **觸發原因**：`MY_FIELD` 應為 `myField`（假設為駝峰式命名）。

26. **TypeName**
    - **目的**：類別/介面/列舉名稱必須為 `UpperCamelCase`。
    - **違規範例**：
      ```java
      public class myClass {}
      ```
    - **觸發原因**：`myClass` 應為 `MyClass`。

---

#### 匯入檢查
這些檢查規範匯入陳述式。

27. **AvoidStarImport**
    - **目的**：禁止萬用字元匯入（例如 `import java.util.*`）。
    - **違規範例**：
      ```java
      import java.util.*;
      ```
    - **觸發原因**：使用了 `*` 而非具體匯入（例如 `import java.util.List`）。

28. **IllegalImport**
    - **目的**：阻止從受限制套件匯入（例如 `sun.*`）。
    - **違規範例**：
      ```java
      import sun.misc.Unsafe;
      ```
    - **觸發原因**：`sun.misc.Unsafe` 屬於受限制套件。

29. **RedundantImport**
    - **目的**：標記重複或不必要的匯入。
    - **違規範例**：
      ```java
      import java.util.List;
      import java.util.List;
      ```
    - **觸發原因**：重複匯入 `List`。

30. **UnusedImports**
    - **目的**：偵測未使用的匯入。
    - **違規範例**：
      ```java
      import java.util.List;
      public class MyClass {}
      ```
    - **觸發原因**：匯入了 `List` 但未使用。

---

#### 大小檢查
這些檢查限制方法和參數數量。

31. **MethodLength**
    - **目的**：限制方法長度（預設通常為 150 行）。
    - **違規範例**：一個 151 行的方法。
    - **觸發原因**：超過預設行數限制。

32. **ParameterNumber**
    - **目的**：限制方法參數數量（預設通常為 7 個）。
    - **違規範例**：
      ```java
      public void myMethod(int a, int b, int c, int d, int e, int f, int g, int h) {}
      ```
    - **觸發原因**：8 個參數超過預設限制 7 個。

---

#### 空白字元檢查
這些檢查強制執行程式碼中一致的空白字元使用。

33. **EmptyForIteratorPad**
    - **目的**：檢查空 `for` 迴圈迭代器中的填充。
    - **違規範例**：
      ```java
      for (int i = 0; ; i++) {}
      ```
    - **觸發原因**：空的迭代器區段應有空格（例如 `for (int i = 0; ; i++)`）。

34. **GenericWhitespace**
    - **目的**：確保泛型類型周圍的間距（例如 `List<String>`）。
    - **違規範例**：
      ```java
      List<String>list;
      ```
    - **觸發原因**：`>` 與 `list` 之間缺少空格。

35. **MethodParamPad**
    - **目的**：檢查方法參數列表前的間距。
    - **違規範例**：
      ```java
      public void myMethod (int x) {}
      ```
    - **觸發原因**：`(int x)` 前的空格不正確。

36. **NoWhitespaceAfter**
    - **目的**：禁止特定符號後出現空白字元（例如 `++`）。
    - **違規範例**：
      ```java
      int x = y ++ ;
      ```
    - **觸發原因**：`++` 後出現空格。

37. **NoWhitespaceBefore**
    - **目的**：禁止特定符號前出現空白字元（例如 `;`）。
    - **違規範例**：
      ```java
      int x = 1 ;
      ```
    - **觸發原因**：`;` 前出現空格。

38. **OperatorWrap**
    - **目的**：確保運算子位於正確的行上。
    - **違規範例**：
      ```java
      int x = 1 +
          2;
      ```
    - **觸發原因**：`+` 應位於第一行的結尾。

39. **ParenPad**
    - **目的**：檢查括號內的間距。
    - **違規範例**：
      ```java
      if ( x == y ) {}
      ```
    - **觸發原因**：`(` 和 `)` 內的間距不正確。

40. **TypecastParenPad**
    - **目的**：確保型別轉換中的間距。
    - **違規範例**：
      ```java
      Object o = ( String ) obj;
      ```
    - **觸發原因**：`( String )` 內的間距不正確。

41. **WhitespaceAfter**
    - **目的**：要求特定符號後必須有空白字元（例如逗號）。
    - **違規範例**：
      ```java
      int[] arr = {1,2,3};
      ```
    - **觸發原因**：逗號後缺少空格。

42. **WhitespaceAround**
    - **目的**：確保運算子/關鍵字周圍的空白字元。
    - **違規範例**：
      ```java
      if(x==y) {}
      ```
    - **觸發原因**：`==` 和 `if` 周圍缺少空格。

---

#### 修飾符檢查
這些檢查規範 Java 修飾符。

43. **ModifierOrder**
    - **目的**：確保修飾符順序正確（符合 JLS）。
    - **違規範例**：
      ```java
      static public final int x = 1;
      ```
    - **觸發原因**：順序錯誤；應為 `public static final`。

44. **RedundantModifier**
    - **目的**：標記不必要的修飾符。
    - **違規範例**：
      ```java
      public final class MyClass {
          public final void myMethod() {}
      }
      ```
    - **觸發原因**：`final` 類別中的方法使用 `final` 是多餘的。

---

#### 區塊檢查
這些檢查強制執行程式碼區塊的正確使用。

45. **AvoidNestedBlocks**
    - **目的**：禁止不必要的巢狀區塊。
    - **違規範例**：
      ```java
      public void myMethod() {
          { int x = 1; }
      }
      ```
    - **觸發原因**：不必要的巢狀區塊。

46. **EmptyBlock**
    - **目的**：標記空區塊。
    - **違規範例**：
      ```java
      if (x == 1) {}
      ```
    - **觸發原因**：空的 `if` 區塊。

47. **LeftCurly**
    - **目的**：確保左大括號位置正確。
    - **違規範例**：
      ```java
      public class MyClass
      {
      }
      ```
    - **觸發原因**：`{` 應與 `class` 位於同一行。

48. **NeedBraces**
    - **目的**：要求單陳述式區塊必須使用大括號。
    - **違規範例**：
      ```java
      if (x == 1) y = 2;
      ```
    - **觸發原因**：缺少大括號；應為 `{ y = 2; }`。

49. **RightCurly**
    - **目的**：確保右大括號位置正確。
    - **違規範例**：
      ```java
      public class MyClass {
      }
      ```
    - **觸發原因**：`}` 應位於新行（取決於風格）。

---

#### 編碼問題檢查
這些檢查識別常見的編碼問題。

50. **EmptyStatement**
    - **目的**：標記空陳述式。
    - **違規範例**：
      ```java
      int x = 1;; // 多餘的分號
      ```
    - **觸發原因**：多餘的 `;` 建立了空陳述式。

51. **EqualsHashCode**
    - **目的**：確保同時覆寫 `equals()` 和 `hashCode()`。
    - **違規範例**：
      ```java
      public class MyClass {
          @Override
          public boolean equals(Object o) { return true; }
      }
      ```
    - **觸發原因**：缺少 `hashCode()` 覆寫。

52. **HiddenField**
    - **目的**：偵測被區域變數/參數遮蔽的欄位。
    - **違規範例**：
      ```java
      public class MyClass {
          int x;
          public void setX(int x) { this.x = x; }
      }
      ```
    - **觸發原因**：參數 `x` 遮蔽了欄位 `x`。

53. **IllegalInstantiation**
    - **目的**：禁止特定類別的實體化。
    - **違規範例**：
      ```java
      String s = new String("test");
      ```
    - **觸發原因**：不必要的 `String` 實體化。

54. **InnerAssignment**
    - **目的**：不允許在表達式中進行賦值。
    - **違規範例**：
      ```java
      if (x = 1) {}
      ```
    - **觸發原因**：表達式中進行了賦值 `x = 1`。

55. **MagicNumber**
    - **目的**：標記硬編碼的數字常值。
    - **違規範例**：
      ```java
      int x = 42;
      ```
    - **觸發原因**：`42` 應為命名常數（例如 `static final int MY_CONST = 42;`）。

56. **MissingSwitchDefault**
    - **目的**：要求 `switch` 陳述式必須包含 `default` 情況。
    - **違規範例**：
      ```java
      switch (x) {
          case 1: break;
      }
      ```
    - **觸發原因**：缺少 `default` 情況。

57. **MultipleVariableDeclarations**
    - **目的**：禁止在單一宣告中宣告多個變數。
    - **違規範例**：
      ```java
      int x, y;
      ```
    - **觸發原因**：應為 `int x; int y;`。

58. **SimplifyBooleanExpression**
    - **目的**：標記複雜的布林表達式。
    - **違規範例**：
      ```java
      if (x == true) {}
      ```
    - **觸發原因**：應為 `if (x)`。

59. **SimplifyBooleanReturn**
    - **目的**：簡化布林傳回陳述式。
    - **違規範例**：
      ```java
      if (x) return true; else return false;
      ```
    - **觸發原因**：應為 `return x;`。

---

#### 類別設計檢查
這些檢查強制執行良好的類別設計。

60. **DesignForExtension**
    - **目的**：確保非 final 類別具有 protected/abstract 方法。
    - **違規範例**：
      ```java
      public class MyClass {
          public void myMethod() {}
      }
      ```
    - **觸發原因**：非 final 類別具有非 protected/abstract 方法。

61. **FinalClass**
    - **目的**：將具有私有建構子的類別標記為 `final` 的候選。
    - **違規範例**：
      ```java
      public class MyClass {
          private MyClass() {}
      }
      ```
    - **觸發原因**：由於無法被繼承，應為 `final`。

62. **HideUtilityClassConstructor**
    - **目的**：確保工具類別具有私有建構子。
    - **違規範例**：
      ```java
      public class MyUtils {
          public static void doSomething() {}
      }
      ```
    - **觸發原因**：工具類別缺少私有建構子。

63. **InterfaceIsType**
    - **目的**：禁止標記介面（無方法的介面）。
    - **違規範例**：
      ```java
      public interface MyMarker {}
      ```
    - **觸發原因**：介面沒有方法。

64. **VisibilityModifier**
    - **目的**：強制執行正確的欄位可見性（偏好 private 並搭配 getter/setter）。
    - **違規範例**：
      ```java
      public class MyClass {
          public int x;
      }
      ```
    - **觸發原因**：欄位 `x` 應為 `private` 並搭配存取器。

---

#### 雜項檢查
針對程式碼品質的額外檢查。

65. **ArrayTypeStyle**
    - **目的**：強制執行一致的陣列宣告風格（`int[]` 對比 `int []`）。
    - **違規範例**：
      ```java
      int x[];
      ```
    - **觸發原因**：應為 `int[] x`。

66. **FinalParameters**
    - **目的**：要求方法參數盡可能為 `final`。
    - **違規範例**：
      ```java
      public void myMethod(int x) {}
      ```
    - **觸發原因**：參數 `x` 應為 `final int x`。

67. **TodoComment**
    - **目的**：標記 `TODO` 註釋。
    - **違規範例**：
      ```java
      // TODO: 修復此問題
      public void myMethod() {}
      ```
    - **觸發原因**：偵測到 `TODO` 註釋。

68. **UpperEll**
    - **目的**：確保 long 常值使用 `L`（而非 `l`）。
    - **違規範例**：
      ```java
      long x = 100l;
      ```
    - **觸發原因**：`100l` 應為 `100L`。

---

#### 抑制篩選器（TreeWalker 內部）
這些允許在 AST 內進行抑制。

69. **SuppressionXpathFilter**
    - **目的**：使用來自檔案（例如 `checkstyle-xpath-suppressions.xml`）的 XPath 表達式來抑制檢查。
    - **違規範例**：類似 `SuppressionFilter`，但使用 XPath（例如抑制特定方法的 `JavadocMethod`）。

70. **SuppressWarningsHolder**
    - **目的**：在 AST 中支援 `@SuppressWarnings("checkstyle:...")`。
    - **違規範例**：
      ```java
      public class MyClass {
          int MY_FIELD; // 違反 MemberName
      }
      ```
      ```java
      @SuppressWarnings("checkstyle:MemberName")
      public class MyClass {
          int MY_FIELD; // 無違規
      }
      ```
    - **觸發原因**：未經抑制時，`MY_FIELD` 違反 `MemberName`。

---

### 關鍵注意事項
- **可配置性**：像 `LineLength` 或 `MethodLength` 這樣的規則可以自訂閾值（例如 `LineLength` 的 `max="120"`）。
- **抑制**：使用 `@SuppressWarnings("checkstyle:<check-name>")` 或抑制檔案來繞過特定檢查。
- **整合**：透過 Maven/Gradle 或 IDE 外掛執行；錯誤會在建置期間回報。
- **標頭檢查**：除非取消註解並使用 `checkstyle.header.file` 配置，否則處於非活動狀態。

如果您需要特定的自訂範例（例如將 `LineLength` 改為 120）、違規修復方法或整合細節，請告訴我！
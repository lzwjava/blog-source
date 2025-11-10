---
audio: false
generated: true
lang: ja
layout: post
title: Checkstyleルール簡潔解説
translated: true
type: note
---

以下に、提供されたCheckstyle設定ファイルの各ルールを、カテゴリ別に分けて説明します。また、各ルールに違反するコードの小さな例と、なぜフラグが立てられるのかの簡単な説明も記載します。各例は、特に明記しない限り、ルールがデフォルト設定で有効であることを前提としています。設定可能なプロパティを持つルール（例: LineLength）については、特に明記しない限り典型的なデフォルト値（例: LineLengthの80文字）を使用します。

---

### ルートモジュール: `<module name="Checker">`
`Checker`モジュールは、すべてのチェックとフィルターを統括する最上位のモジュールです。`.java`、`.properties`、`.xml`ファイルに適用され、違反の重大度を`error`に設定します。

#### プロパティ
- **severity="error"**: すべての違反はエラーとして扱われます。
- **fileExtensions="java, properties, xml"**: チェックはこれらのファイルタイプに適用されます。

---

### ファイルフィルター
これらのフィルターは、どのファイルをチェックするかを決定します。

1.  **BeforeExecutionExclusionFileFilter**
    - **目的**: 正規表現に一致するファイル（例: `module-info.java`）をチェック対象から除外します。
    - **違反例**:
      ```java
      // module-info.java
      module com.example {
          requires java.base;
      }
      ```
    - **フラグが立てられる理由**: このファイルは正規表現 `module\-info\.java$` に一致するため、チェックから除外されます。このファイル自体には違反は発生しませんが、他のファイルはチェックされます。

2.  **SuppressionFilter**
    - **目的**: ファイル（例: `checkstyle-suppressions.xml`）内のルールに基づいてチェックを抑制します。
    - **違反例**: `checkstyle-suppressions.xml` が特定のファイルに対する `LineLength` を抑制している場合、そのファイル内の長い行はフラグが立てられません。抑制がない場合:
      ```java
      public class MyClass { // この行は非常に長く、デフォルトの最大長80文字を超えているため、エラーになります。
      }
      ```
    - **フラグが立てられる理由**: 抑制ルールがない場合、長い行は `LineLength` に違反します。

3.  **SuppressWarningsFilter**
    - **目的**: `@SuppressWarnings("checkstyle:<check-name>")` を使用してチェックを抑制できるようにします。
    - **違反例**:
      ```java
      public class MyClass {
          int my_field; // MemberName（キャメルケースでない）に違反
      }
      ```
      ```java
      @SuppressWarnings("checkstyle:MemberName")
      public class MyClass {
          int my_field; // 抑制により違反なし
      }
      ```
    - **フラグが立てられる理由**: 抑制がない場合、`my_field` は `MemberName`（キャメルケース、例: `myField` を期待）に違反します。

---

### その他のチェック
これらはファイルの一般的なプロパティに適用されます。

4.  **JavadocPackage**
    - **目的**: 各パッケージがJavadocを持つ `package-info.java` ファイルを持つことを保証します。
    - **違反例**:
      ```java
      // com/example/package-info.java (Javadocがない、またはファイル自体がない)
      package com.example;
      ```
    - **フラグが立てられる理由**: Javadocコメント（例: `/** パッケージの説明 */`）が欠落しています。

5.  **NewlineAtEndOfFile**
    - **目的**: ファイルの末尾が改行で終わることを保証します。
    - **違反例**:
      ```java
      public class MyClass {} // 末尾に改行なし
      ```
    - **フラグが立てられる理由**: ファイルが改行文字なしで終了しています。

6.  **Translation**
    - **目的**: 国際化用の `.properties` ファイルにおいて、キーが一貫していることを検証します。
    - **違反例**:
      ```properties
      # messages.properties
      key1=Hello
      key2=World
      ```
      ```properties
      # messages_fr.properties
      key1=Bonjour
      # key2 が欠落
      ```
    - **フラグが立てられる理由**: `messages_fr.properties` には `messages.properties` に存在する `key2` がありません。

---

### サイズチェック
これらはファイルと行の長さの制限を強制します。

7.  **FileLength**
    - **目的**: ファイル内の総行数を制限します（デフォルトは通常2000行）。
    - **違反例**: 2001行のJavaファイル。
    - **フラグが立てられる理由**: デフォルトの行制限を超えています。

8.  **LineLength**
    - **目的**: 行が最大長（デフォルト80文字）を超えないようにします。
    - **違反例**:
      ```java
      public class MyClass { public void myMethodWithVeryLongNameToExceedEightyCharactersInALine() {} }
      ```
    - **フラグが立てられる理由**: 行が80文字を超えています。

---

### 空白チェック
これらは一貫した空白の使用を強制します。

9.  **FileTabCharacter**
    - **目的**: ソースファイル内のタブ文字（`\t`）を禁止します。
    - **違反例**:
      ```java
      public class MyClass {
      →    int x; // インデントにタブ文字を使用
      }
      ```
    - **フラグが立てられる理由**: スペースの代わりにタブが使用されています。

10. **RegexpSingleline**
    - **目的**: 末尾の空白（`\s+$` で終わる行）を検出します。
    - **違反例**:
      ```java
      public class MyClass {   // 末尾のスペース
      }
      ```
    - **フラグが立てられる理由**: 行が空白で終わっています。

---

### ヘッダーチェック (コメントアウト済み)
11. **Header**
    - **目的**: `checkstyle.header.file` から特定のファイルヘッダー（例: 著作権表示）を強制します。
    - **違反例** (有効な場合):
      ```java
      // ヘッダーが欠落
      public class MyClass {}
      ```
    - **フラグが立てられる理由**: 必要なヘッダー（例: `// Copyright 2025 Example Inc.`）がありません。

---

### サブモジュール: `<module name="TreeWalker">`
`TreeWalker` はJavaの抽象構文木(AST)を処理し、詳細なチェックを行います。

#### Javadoc チェック
これらは適切なJavadocコメントを強制します。

12. **InvalidJavadocPosition**
    - **目的**: Javadocコメントがクラス/メソッドの前にあることを保証し、他の場所にないことを確認します。
    - **違反例**:
      ```java
      public class MyClass {
          /** これは誤って配置されたJavadocです */
          int x;
      }
      ```
    - **フラグが立てられる理由**: Javadocがクラス/メソッド宣言の前にありません。

13. **JavadocMethod**
    - **目的**: メソッドに適切なJavadoc（パラメーター、戻り値、例外）があるかをチェックします。
    - **違反例**:
      ```java
      public int add(int a, int b) { return a + b; }
      ```
    - **フラグが立てられる理由**: publicメソッドにJavadocがありません。

14. **JavadocType**
    - **目的**: クラス/インターフェース/列挙型にJavadocがあることを保証します。
    - **違反例**:
      ```java
      public class MyClass {}
      ```
    - **フラグが立てられる理由**: クラスにJavadocがありません。

15. **JavadocVariable**
    - **目的**: public/protected フィールドにJavadocを要求します。
    - **違反例**:
      ```java
      public class MyClass {
          public int x;
      }
      ```
    - **フラグが立てられる理由**: publicフィールドにJavadocがありません。

16. **JavadocStyle**
    - **目的**: Javadocのスタイル（例: 有効なHTML、不正な形式のコメントがない）を強制します。
    - **違反例**:
      ```java
      /** 末尾にピリオドが欠落 */
      public class MyClass {}
      ```
    - **フラグが立てられる理由**: Javadocの末尾にピリオドがありません。

17. **MissingJavadocMethod**
    - **目的**: Javadocが欠落しているメソッドにフラグを立てます。
    - **違反例**:
      ```java
      public void myMethod() {}
      ```
    - **フラグが立てられる理由**: publicメソッドにJavadocがありません。

---

#### 命名規則
これらは命名パターンを強制します。

18. **ConstantName**
    - **目的**: 定数（`static final`）は `UPPER_CASE` でなければなりません。
    - **違反例**:
      ```java
      public class MyClass {
          static final int myConstant = 42;
      }
      ```
    - **フラグが立てられる理由**: `myConstant` は `MY_CONSTANT` であるべきです。

19. **LocalFinalVariableName**
    - **目的**: ローカルな `final` 変数は `camelCase` でなければなりません。
    - **違反例**:
      ```java
      public void myMethod() {
          final int MY_VAR = 1;
      }
      ```
    - **フラグが立てられる理由**: `MY_VAR` は `myVar` であるべきです。

20. **LocalVariableName**
    - **目的**: ローカル変数は `camelCase` でなければなりません。
    - **違反例**:
      ```java
      public void myMethod() {
          int MY_VAR = 1;
      }
      ```
    - **フラグが立てられる理由**: `MY_VAR` は `myVar` であるべきです。

21. **MemberName**
    - **目的**: インスタンスフィールドは `camelCase` でなければなりません。
    - **違反例**:
      ```java
      public class MyClass {
          int my_field;
      }
      ```
    - **フラグが立てられる理由**: `my_field` は `myField` であるべきです。

22. **MethodName**
    - **目的**: メソッドは `camelCase` でなければなりません。
    - **違反例**:
      ```java
      public void MyMethod() {}
      ```
    - **フラグが立てられる理由**: `MyMethod` は `myMethod` であるべきです。

23. **PackageName**
    - **目的**: パッケージは小文字とドット（例: `com.example`）でなければなりません。
    - **違反例**:
      ```java
      package com.Example;
      ```
    - **フラグが立てられる理由**: `Example` は `example` であるべきです。

24. **ParameterName**
    - **目的**: メソッドパラメーターは `camelCase` でなければなりません。
    - **違反例**:
      ```java
      public void myMethod(int MY_PARAM) {}
      ```
    - **フラグが立てられる理由**: `MY_PARAM` は `myParam` であるべきです。

25. **StaticVariableName**
    - **目的**: static（非final）フィールドは命名パターンに従わなければなりません。
    - **違反例**:
      ```java
      public class MyClass {
          static int MY_FIELD;
      }
      ```
    - **フラグが立てられる理由**: `MY_FIELD` は `myField`（キャメルケースを想定）であるべきです。

26. **TypeName**
    - **目的**: クラス/インターフェース/列挙型の名前は `UpperCamelCase` でなければなりません。
    - **違反例**:
      ```java
      public class myClass {}
      ```
    - **フラグが立てられる理由**: `myClass` は `MyClass` であるべきです。

---

#### import チェック
これらはimport文を規制します。

27. **AvoidStarImport**
    - **目的**: ワイルドカードimport（例: `import java.util.*`）を禁止します。
    - **違反例**:
      ```java
      import java.util.*;
      ```
    - **フラグが立てられる理由**: 特定のimport（例: `import java.util.List`）の代わりに `*` を使用しています。

28. **IllegalImport**
    - **目的**: 制限されたパッケージ（例: `sun.*`）からのimportをブロックします。
    - **違反例**:
      ```java
      import sun.misc.Unsafe;
      ```
    - **フラグが立てられる理由**: `sun.misc.Unsafe` は制限されたパッケージに含まれます。

29. **RedundantImport**
    - **目的**: 重複または不要なimportにフラグを立てます。
    - **違反例**:
      ```java
      import java.util.List;
      import java.util.List;
      ```
    - **フラグが立てられる理由**: `List` のimportが重複しています。

30. **UnusedImports**
    - **目的**: 使用されていないimportを検出します。
    - **違反例**:
      ```java
      import java.util.List;
      public class MyClass {}
      ```
    - **フラグが立てられる理由**: `List` がimportされているが使用されていません。

---

#### サイズチェック
これらはメソッドとパラメーターの数を制限します。

31. **MethodLength**
    - **目的**: メソッドの長さを制限します（デフォルトは通常150行）。
    - **違反例**: 151行のメソッド。
    - **フラグが立てられる理由**: デフォルトの行制限を超えています。

32. **ParameterNumber**
    - **目的**: メソッドパラメーターを制限します（デフォルトは通常7つ）。
    - **違反例**:
      ```java
      public void myMethod(int a, int b, int c, int d, int e, int f, int g, int h) {}
      ```
    - **フラグが立てられる理由**: 8つのパラメーターがデフォルト制限の7つを超えています。

---

#### 空白チェック
これらはコード内での一貫した空白を強制します。

33. **EmptyForIteratorPad**
    - **目的**: 空の `for` ループイテレーターのパディングをチェックします。
    - **違反例**:
      ```java
      for (int i = 0; ; i++) {}
      ```
    - **フラグが立てられる理由**: 空のイテレーターセクションにはスペースが必要です（例: `for (int i = 0; ; i++)`）。

34. **GenericWhitespace**
    - **目的**: ジェネリック型の周囲のスペース（例: `List<String>`）を保証します。
    - **違反例**:
      ```java
      List<String>list;
      ```
    - **フラグが立てられる理由**: `>` と `list` の間にスペースがありません。

35. **MethodParamPad**
    - **目的**: メソッドパラメーターリストの前のスペースをチェックします。
    - **違反例**:
      ```java
      public void myMethod (int x) {}
      ```
    - **フラグが立てられる理由**: `(int x)` の前のスペースが不正です。

36. **NoWhitespaceAfter**
    - **目的**: 特定のトークン（例: `++`）の後の空白を禁止します。
    - **違反例**:
      ```java
      int x = y ++ ;
      ```
    - **フラグが立てられる理由**: `++` の後にスペースがあります。

37. **NoWhitespaceBefore**
    - **目的**: 特定のトークン（例: `;`）の前の空白を禁止します。
    - **違反例**:
      ```java
      int x = 1 ;
      ```
    - **フラグが立てられる理由**: `;` の前にスペースがあります。

38. **OperatorWrap**
    - **目的**: 演算子が正しい行にあることを保証します。
    - **違反例**:
      ```java
      int x = 1 +
          2;
      ```
    - **フラグが立てられる理由**: `+` は最初の行の末尾にあるべきです。

39. **ParenPad**
    - **目的**: 括弧内のスペースをチェックします。
    - **違反例**:
      ```java
      if ( x == y ) {}
      ```
    - **フラグが立てられる理由**: `(` と `)` の内側のスペースが不正です。

40. **TypecastParenPad**
    - **目的**: 型キャスト内のスペースを保証します。
    - **違反例**:
      ```java
      Object o = ( String ) obj;
      ```
    - **フラグが立てられる理由**: `( String )` の内側のスペースが不正です。

41. **WhitespaceAfter**
    - **目的**: 特定のトークン（例: カンマ）の後に空白を要求します。
    - **違反例**:
      ```java
      int[] arr = {1,2,3};
      ```
    - **フラグが立てられる理由**: カンマの後にスペースがありません。

42. **WhitespaceAround**
    - **目的**: 演算子/キーワードの周囲の空白を保証します。
    - **違反例**:
      ```java
      if(x==y) {}
      ```
    - **フラグが立てられる理由**: `==` と `if` の周囲にスペースがありません。

---

#### 修飾子チェック
これらはJavaの修飾子を規制します。

43. **ModifierOrder**
    - **目的**: 修飾子が正しい順序（JLSに準拠）であることを保証します。
    - **違反例**:
      ```java
      static public final int x = 1;
      ```
    - **フラグが立てられる理由**: 順序が誤り。`public static final` であるべきです。

44. **RedundantModifier**
    - **目的**: 不要な修飾子にフラグを立てます。
    - **違反例**:
      ```java
      public final class MyClass {
          public final void myMethod() {}
      }
      ```
    - **フラグが立てられる理由**: `final` クラス内のメソッドの `final` は冗長です。

---

#### ブロックチェック
これらはコードブロックの適切な使用を強制します。

45. **AvoidNestedBlocks**
    - **目的**: 不必要なネストされたブロックを禁止します。
    - **違反例**:
      ```java
      public void myMethod() {
          { int x = 1; }
      }
      ```
    - **フラグが立てられる理由**: 不必要なネストされたブロックです。

46. **EmptyBlock**
    - **目的**: 空のブロックにフラグを立てます。
    - **違反例**:
      ```java
      if (x == 1) {}
      ```
    - **フラグが立てられる理由**: 空の `if` ブロックです。

47. **LeftCurly**
    - **目的**: 開きブレースが正しく配置されていることを保証します。
    - **違反例**:
      ```java
      public class MyClass
      {
      }
      ```
    - **フラグが立てられる理由**: `{` は `class` と同じ行にあるべきです。

48. **NeedBraces**
    - **目的**: 単一ステートメントのブロックにもブレースを要求します。
    - **違反例**:
      ```java
      if (x == 1) y = 2;
      ```
    - **フラグが立てられる理由**: ブレースが欠落。`{ y = 2; }` であるべきです。

49. **RightCurly**
    - **目的**: 閉じブレースが正しく配置されていることを保証します。
    - **違反例**:
      ```java
      public class MyClass {
      }
      ```
    - **フラグが立てられる理由**: `}` は新しい行にあるべきです（スタイルによります）。

---

#### コーディング問題チェック
これらは一般的なコーディングの問題を特定します。

50. **EmptyStatement**
    - **目的**: 空のステートメントにフラグを立てます。
    - **違反例**:
      ```java
      int x = 1;; // 余分なセミコロン
      ```
    - **フラグが立てられる理由**: 余分な `;` が空のステートメントを作成しています。

51. **EqualsHashCode**
    - **目的**: `equals()` と `hashCode()` の両方がオーバーライドされていることを保証します。
    - **違反例**:
      ```java
      public class MyClass {
          @Override
          public boolean equals(Object o) { return true; }
      }
      ```
    - **フラグが立てられる理由**: `hashCode()` のオーバーライドが欠落しています。

52. **HiddenField**
    - **目的**: ローカル変数/パラメーターによって隠蔽(シャドウ)されたフィールドを検出します。
    - **違反例**:
      ```java
      public class MyClass {
          int x;
          public void setX(int x) { this.x = x; }
      }
      ```
    - **フラグが立てられる理由**: パラメーター `x` がフィールド `x` をシャドウしています。

53. **IllegalInstantiation**
    - **目的**: 特定のクラスのインスタンス化を禁止します。
    - **違反例**:
      ```java
      String s = new String("test");
      ```
    - **フラグが立てられる理由**: `String` の不必要なインスタンス化です。

54. **InnerAssignment**
    - **目的**: 式内での代入を禁止します。
    - **違反例**:
      ```java
      if (x = 1) {}
      ```
    - **フラグが立てられる理由**: 式内での代入 `x = 1` です。

55. **MagicNumber**
    - **目的**: ハードコードされた数値リテラルにフラグを立てます。
    - **違反例**:
      ```java
      int x = 42;
      ```
    - **フラグが立てられる理由**: `42` は名前付き定数（例: `static final int MY_CONST = 42;`）であるべきです。

56. **MissingSwitchDefault**
    - **目的**: `switch` 文に `default` ケースを要求します。
    - **違反例**:
      ```java
      switch (x) {
          case 1: break;
      }
      ```
    - **フラグが立てられる理由**: `default` ケースが欠落しています。

57. **MultipleVariableDeclarations**
    - **目的**: 1つの宣言での複数変数を禁止します。
    - **違反例**:
      ```java
      int x, y;
      ```
    - **フラグが立てられる理由**: `int x; int y;` であるべきです。

58. **SimplifyBooleanExpression**
    - **目的**: 複雑なブール式にフラグを立てます。
    - **違反例**:
      ```java
      if (x == true) {}
      ```
    - **フラグが立てられる理由**: `if (x)` であるべきです。

59. **SimplifyBooleanReturn**
    - **目的**: ブールのreturn文を簡略化します。
    - **違反例**:
      ```java
      if (x) return true; else return false;
      ```
    - **フラグが立てられる理由**: `return x;` であるべきです。

---

#### クラス設計チェック
これらは良いクラス設計を強制します。

60. **DesignForExtension**
    - **目的**: non-finalクラスがprotected/abstractメソッドを持つことを保証します。
    - **違反例**:
      ```java
      public class MyClass {
          public void myMethod() {}
      }
      ```
    - **フラグが立てられる理由**: non-finalクラスにnon-protected/abstractメソッドがあります。

61. **FinalClass**
    - **目的**: privateコンストラクターを持つクラスを `final` の候補としてフラグを立てます。
    - **違反例**:
      ```java
      public class MyClass {
          private MyClass() {}
      }
      ```
    - **フラグが立てられる理由**: 拡張できないため `final` であるべきです。

62. **HideUtilityClassConstructor**
    - **目的**: ユーティリティクラスがprivateコンストラクターを持つことを保証します。
    - **違反例**:
      ```java
      public class MyUtils {
          public static void doSomething() {}
      }
      ```
    - **フラグが立てられる理由**: ユーティリティクラスにprivateコンストラクターが欠落しています。

63. **InterfaceIsType**
    - **目的**: マーカーインターフェース（メソッドなし）を禁止します。
    - **違反例**:
      ```java
      public interface MyMarker {}
      ```
    - **フラグが立てられる理由**: インターフェースにメソッドがありません。

64. **VisibilityModifier**
    - **目的**: 適切なフィールドの可視性（privateとgetter/setterを推奨）を強制します。
    - **違反例**:
      ```java
      public class MyClass {
          public int x;
      }
      ```
    - **フラグが立てられる理由**: フィールド `x` は `private` でアクセサを持つべきです。

---

#### その他のチェック
コード品質に関する追加のチェックです。

65. **ArrayTypeStyle**
    - **目的**: 配列宣言のスタイル（`int[]` vs `int []`）の一貫性を強制します。
    - **違反例**:
      ```java
      int x[];
      ```
    - **フラグが立てられる理由**: `int[] x` であるべきです。

66. **FinalParameters**
    - **目的**: メソッドパラメーターを可能な場合 `final` にすることを要求します。
    - **違反例**:
      ```java
      public void myMethod(int x) {}
      ```
    - **フラグが立てられる理由**: パラメーター `x` は `final int x` であるべきです。

67. **TodoComment**
    - **目的**: `TODO` コメントにフラグを立てます。
    - **違反例**:
      ```java
      // TODO: これを修正
      public void myMethod() {}
      ```
    - **フラグが立てられる理由**: `TODO` コメントが検出されました。

68. **UpperEll**
    - **目的**: longリテラルに `L`（`l` ではない）を使用することを保証します。
    - **違反例**:
      ```java
      long x = 100l;
      ```
    - **フラグが立てられる理由**: `100l` は `100L` であるべきです。

---

#### 抑制フィルター (TreeWalker内)
これらはAST内での抑制を可能にします。

69. **SuppressionXpathFilter**
    - **目的**: ファイル（例: `checkstyle-xpath-suppressions.xml`）からのXPath式を使用してチェックを抑制します。
    - **違反例**: `SuppressionFilter` と同様ですがXPathを使用（例: 特定のメソッドに対する `JavadocMethod` の抑制）。

70. **SuppressWarningsHolder**
    - **目的**: AST内での `@SuppressWarnings("checkstyle:...")` をサポートします。
    - **違反例**:
      ```java
      public class MyClass {
          int MY_FIELD; // MemberNameに違反
      }
      ```
      ```java
      @SuppressWarnings("checkstyle:MemberName")
      public class MyClass {
          int MY_FIELD; // 違反なし
      }
      ```
    - **フラグが立てられる理由**: 抑制がない場合、`MY_FIELD` は `MemberName` に違反します。

---

### 主な注意点
- **設定可能性**: `LineLength` や `MethodLength` のようなルールは、カスタムの閾値（例: `LineLength` に `max="120"`）を持つことができます。
- **抑制**: 特定のチェックをバイパスするには、`@SuppressWarnings("checkstyle:<check-name>")` または抑制ファイルを使用します。
- **統合**: Maven/Gradle または IDE プラグインで実行します。エラーはビルド中に報告されます。
- **ヘッダーチェック**: コメントを解除し `checkstyle.header.file` で設定しない限り非アクティブです。

特定のカスタマイズ例（例: `LineLength` を120に変更）、違反の修正、または統合の詳細が必要な場合は、お知らせください！
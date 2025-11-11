---
audio: false
generated: true
lang: ja
layout: post
title: チェックスタイル設定
translated: true
type: note
---

これはXMLで記述されたCheckstyle設定ファイルで、Sunのコーディング規約、Java言語仕様、Javadocガイドライン、および追加のベストプラクティスに基づいてJavaコードのコーディング標準とベストプラクティスを実施するように設計されています。Checkstyleは、定義されたルールセットへの準拠をJavaソースコードに対してチェックする静的コード解析ツールです。以下では、この設定ファイルの構造と主要コンポーネントについて説明します。

---

### **概要**
- **目的**: このファイルは、Java、プロパティ、XMLファイルに対して、書式設定、命名規則、Javadoc要件、コード構造などのコーディング標準違反をチェックするためのルールを定義します。
- **構造**: 設定は `<module>` 要素を使用して階層的に構成され、特定のチェックまたはフィルターのための他のモジュールを含むルート `Checker` モジュールから始まります。
- **標準**: 以下に準拠しています:
  - Java言語仕様 (Java SE 11)
  - Sunコード規約
  - Javadocガイドライン
  - JDK APIドキュメント
  - 一般的なベストプラクティス
- **主な機能**:
  - 設定可能な重大度 (「error」に設定)。
  - ファイル拡張子のサポート: `.java`, `.properties`, `.xml`。
  - 抑制ファイルまたは `@SuppressWarnings` アノテーションによる特定のチェックの抑制を許可。

---

### **ルートモジュール: `<module name="Checker">`**
`Checker` モジュールは、すべてのチェックとフィルターを調整するトップレベルのモジュールです。

- **プロパティ**:
  - `severity="error"`: すべての違反をエラーとして扱います (他のオプションには `warning` や `info` があります)。
  - `fileExtensions="java, properties, xml"`: `.java`、`.properties`、`.xml` ファイルにチェックを適用します。

- **サブモジュール**:
  - **ファイルフィルター**:
    - `BeforeExecutionExclusionFileFilter`: `module-info.java` ファイルをチェックから除外します (正規表現 `module\-info\.java$` を使用)。
  - **抑制フィルター**:
    - `SuppressionFilter`: ファイル (デフォルト: `checkstyle-suppressions.xml`) から抑制ルールを読み込みます。ファイルが存在しない場合はオプション (`optional="true"`) です。
    - `SuppressWarningsFilter`: コード内の `@SuppressWarnings("checkstyle:...")` アノテーションを使用して特定のチェックを抑制できるようにします。
  - **その他のチェック**:
    - `JavadocPackage`: 各パッケージにJavadocを含む `package-info.java` ファイルがあることを確認します。
    - `NewlineAtEndOfFile`: ファイルが改行文字で終了していることをチェックします。
    - `Translation`: プロパティファイル (例: 国際化用) に、翻訳間で同じキーが含まれていることを検証します。
  - **サイズチェック**:
    - `FileLength`: ファイルの総長をチェックします (デフォルトの制限が適用されます。上書きされない限り)。
    - `LineLength`: `.java` ファイルの行がデフォルトの長さ (通常は80または120文字、設定可能) を超えないようにします。
  - **空白チェック**:
    - `FileTabCharacter`: ソースファイル内のタブ文字を禁止します (インデントにはスペースを強制)。
    - `RegexpSingleline`: 末尾の空白 (`\s+$` で終わる行) を検出し、「Line has trailing spaces.」というメッセージで報告します。
  - **ヘッダーチェック** (コメントアウト済み):
    - `Header`: コメントを解除すると、`.java` ファイルに対して `checkstyle.header.file` で指定されたファイルからの特定のファイルヘッダー (例: 著作権表示) を強制します。

---

### **サブモジュール: `<module name="TreeWalker">`**
`TreeWalker` モジュールは、Javaソースコードの抽象構文木 (AST) を処理して詳細なチェックを実行します。カテゴリ別にグループ化されたさまざまなサブモジュールを含みます。

#### **Javadocチェック**
これらは、クラス、メソッド、変数に対する適切なJavadocコメントを強制します:
- `InvalidJavadocPosition`: Javadocコメントが正しく配置されていることを確認します (例: クラスやメソッドの前、それ以外の場所ではない)。
- `JavadocMethod`: メソッドにパラメーター、戻り値の型、例外を含む適切なJavadocコメントがあることをチェックします。
- `JavadocType`: クラス、インターフェース、列挙型にJavadocコメントがあることを確認します。
- `JavadocVariable`: public/protected フィールドにJavadocを要求します。
- `JavadocStyle`: Javadocの文体ルールを強制します (例: 適切なHTMLタグ、不正な形式のコメントがないこと)。
- `MissingJavadocMethod`: Javadocコメントが欠落しているメソッドにフラグを立てます。

#### **命名規則**
これらは、識別子 (変数、メソッド、クラスなど) が命名規則に従うことを確認します:
- `ConstantName`: 定数 (例: `static final`) は命名パターン (通常は `UPPER_CASE`) に従わなければなりません。
- `LocalFinalVariableName`: ローカル `final` 変数は命名パターン (例: `camelCase`) に従わなければなりません。
- `LocalVariableName`: ローカル変数は命名パターン (例: `camelCase`) に従わなければなりません。
- `MemberName`: インスタンスフィールドは命名パターン (例: `camelCase`) に従わなければなりません。
- `MethodName`: メソッドは命名パターン (例: `camelCase`) に従わなければなりません。
- `PackageName`: パッケージは命名パターン (例: `com.example` のような小文字とドット) に従わなければなりません。
- `ParameterName`: メソッドパラメーターは命名パターン (例: `camelCase`) に従わなければなりません。
- `StaticVariableName`: 静的 (非final) フィールドは命名パターンに従わなければなりません。
- `TypeName`: クラス/インターフェース/列挙型名は命名パターン (例: `UpperCamelCase`) に従わなければなりません。

#### **インポートチェック**
これらは `import` 文の使用を規定します:
- `AvoidStarImport`: ワイルドカードインポート (例: `import java.util.*`) を禁止します。
- `IllegalImport`: 制限されたパッケージ (デフォルトは `sun.*`) からのインポートをブロックします。
- `RedundantImport`: 重複または不要なインポートにフラグを立てます。
- `UnusedImports`: 未使用のインポートを検出します (`processJavadoc="false"` でJavadoc関連のインポートを無視)。

#### **サイズチェック**
これらはメソッドとパラメーターのサイズを制限します:
- `MethodLength`: メソッドが最大行数 (デフォルトは通常150) を超えないようにします。
- `ParameterNumber`: メソッド内のパラメーター数を制限します (デフォルトは通常7)。

#### **空白チェック**
これらはコード内での空白の一貫した使用を強制します:
- `EmptyForIteratorPad`: 空の `for` ループイテレーター内のパディングをチェックします (例: `for (int i = 0; ; i++)`)。
- `GenericWhitespace`: ジェネリック型の周囲の適切な間隔を確保します (例: `List<String>`)。
- `MethodParamPad`: メソッドパラメーターリストの前の間隔をチェックします。
- `NoWhitespaceAfter`: 特定のトークン (例: `++` や配列) の後の空白を禁止します。
- `NoWhitespaceBefore`: 特定のトークン (例: セミコロン) の前の空白を禁止します。
- `OperatorWrap`: 演算子 (例: `+`, `=`) が正しい行にあることを確認します。
- `ParenPad`: 括弧内の間隔をチェックします (例: `( x )` 対 `(x)`)。
- `TypecastParenPad`: タイプキャストでの適切な間隔を確保します。
- `WhitespaceAfter`: 特定のトークン (例: カンマ、セミコロン) の後の空白を要求します。
- `WhitespaceAround`: 演算子とキーワードの周囲の空白を確保します (例: `if (x == y)`)。

#### **修飾子チェック**
これらはJava修飾子の使用を規定します:
- `ModifierOrder`: 修飾子が正しい順序であることを確認します (例: JLSに従った `public static final`)。
- `RedundantModifier`: 不要な修飾子 (例: `final` クラス内の `final`) にフラグを立てます。

#### **ブロックチェック**
これらはコードブロック (`{}`) の適切な使用を強制します:
- `AvoidNestedBlocks`: 不必要なネストされたブロック (例: `{ { ... } }`) を禁止します。
- `EmptyBlock`: 意図的でない限り、空のブロック (例: `{}`) にフラグを立てます。
- `LeftCurly`: 開始ブレース (`{`) が正しく配置されていることを確認します (例: 行末)。
- `NeedBraces`: 単一文ブロックに対してブレースを要求します (例: `if (x) y();` は `if (x) { y(); }` でなければなりません)。
- `RightCurly`: 終了ブレース (`}`) が正しく配置されていることを確認します (例: スタイルに応じて新しい行または同じ行)。

#### **コーディング問題チェック**
これらは一般的なコーディングの問題を特定します:
- `EmptyStatement`: 空の文 (例: `;;`) にフラグを立てます。
- `EqualsHashCode`: `equals()` がオーバーライドされている場合、`hashCode()` もオーバーライドされていることを確認します。
- `HiddenField`: ローカル変数またはパラメーターによってシャドウされたフィールドを検出します。
- `IllegalInstantiation`: 特定のクラス (例: `java.lang` クラス like `String`) のインスタンス化を禁止します。
- `InnerAssignment`: 式内での代入 (例: `if (x = y)`) を禁止します。
- `MagicNumber`: 特定のコンテキストでない限り、ハードコードされた数値リテラル (例: `42`) にフラグを立てます。
- `MissingSwitchDefault`: `switch` 文に `default` ケースを要求します。
- `MultipleVariableDeclarations`: 単一行での複数の変数宣言 (例: `int x, y;`) を禁止します。
- `SimplifyBooleanExpression`: 過度に複雑なブール式 (例: `if (x == true)`) にフラグを立てます。
- `SimplifyBooleanReturn`: ブール戻り文を簡素化します (例: `if (x) return true; else return false;`)。

#### **クラス設計チェック**
これらは良いクラス設計のプラクティスを強制します:
- `DesignForExtension`: 非finalクラスが拡張性のためにprotectedまたはabstractメソッドを持つことを確保します。
- `FinalClass`: プライベートコンストラクタのみを持つクラスを `final` の候補としてフラグを立てます。
- `HideUtilityClassConstructor`: ユーティリティクラス (静的メンバーのみ) がプライベートコンストラクタを持つことを確保します。
- `InterfaceIsType`: メソッドのないマーカーインターフェースとしてのみ使用されるインターフェースを禁止します。
- `VisibilityModifier`: フィールドに対する適切な可視性を強制します (例: ゲッター/セッターを持つプライベートフィールドを推奨)。

#### **その他のチェック**
- `ArrayTypeStyle`: 一貫した配列宣言スタイルを強制します (例: `int[]` 対 `int []`)。
- `FinalParameters`: メソッドパラメーターを可能な場合に `final` にすることを要求します。
- `TodoComment`: コード内の `TODO` コメントにフラグを立てます (未完了の作業を追跡するのに便利)。
- `UpperEll`: longリテラルに文字 `L` が使用されることを確保します (例: `100l` ではなく `100L`)。

#### **抑制フィルター (TreeWalker内)**
- `SuppressionXpathFilter`: ファイル (デフォルト: `checkstyle-xpath-suppressions.xml`, オプション) で定義されたXPath式を使用したチェックの抑制を許可します。
- `SuppressWarningsHolder`: AST内で特定のチェックを抑制するための `@SuppressWarnings("checkstyle:...")` アノテーションをサポートします。

---

### **重要なポイント**
- **設定可能性**: ほとんどのモジュールにはデフォルト設定がありますが、プロパティ (例: `LineLength` は特定の `max` 長を設定可能) を介してカスタマイズできます。
- **抑制**: 設定は、外部ファイル (`checkstyle-suppressions.xml`, `checkstyle-xpath-suppressions.xml`) またはアノテーションを介したチェックの柔軟な抑制をサポートします。
- **拡張性**: 追加のチェックを追加でき、既存のチェックはコメントアウトまたは削除することで無効にできます。
- **ドキュメント**: 設定は、各モジュールの詳細についてCheckstyleのドキュメント (例: `https://checkstyle.org`) を参照しています。
- **ヘッダーチェック**: `Header` モジュールはコメントアウトされているため、コメントを解除してヘッダーファイルで設定しない限りアクティブではありません。

---

### **使用方法**
1. **統合**: このファイルは通常、Maven、GradleなどのビルドツールまたはIDEプラグインと共に使用され、ビルドプロセス中または開発中にCheckstyleを実行します。
2. **違反報告**: コードがルールに違反した場合 (例: 行が最大長を超える)、Checkstyleはそれをエラーとして報告します (`severity="error"` のため)。
3. **抑制**: 開発者は、`@SuppressWarnings("checkstyle:<check-name>")` を使用するか、抑制ファイルでルールを定義することで、特定の違反を抑制できます。
4. **カスタマイズ**: `basedir`, `checkstyle.header.file`, または抑制ファイルパスなどのプロパティは、外部で (例: ビルドツールの設定を介して) 設定できます。

---

### **違反の例**
- **JavadocMethod**: Javadocのないpublicメソッドはエラーを引き起こします。
- **LineLength**: デフォルトの最大値 (例: 80文字) を超える `.java` ファイル内の行にフラグが立てられます。
- **AvoidStarImport**: `import java.util.*` を使用するとエラーが発生します。
- **MagicNumber**: 名前付き定数なしで `int x = 42;` と書くとフラグが立てられます。

---

特定のモジュールの詳細な説明、違反の例、またはこの設定のカスタマイズに関するガイダンスが必要な場合は、お知らせください!
---
audio: false
generated: true
lang: ja
layout: post
title: IntelliJ 構造置換テンプレート
translated: true
type: note
---

以下に、分かりやすく分類したIntelliJの構造的置換テンプレート10例を紹介します。これらはリファクタリング、コーディング標準の強制、一般的なコード変換の自動化に非常に強力です。

**基本的なリファクタリングと簡略化:**

1.  **`if (condition) return true; else return false;` を `return condition;` に置換**

      * **検索テンプレート:**
        ```java
        if ($CONDITION$) {
            return true;
        } else {
            return false;
        }
        ```
      * **置換テンプレート:**
        ```java
        return $CONDITION$;
        ```
      * **コンテキスト:** ブール値のreturn文を簡略化します。

2.  **`if (condition) { statement; }` を `if (!condition) { continue/break/return; }` に置換 (ガード節)**

      * **検索テンプレート:**
        ```java
        if ($CONDITION$) {
            $STATEMENTS$;
        }
        ```
      * **置換テンプレート:** (これは変換の提案であり、内部は手動で調整する必要があります)
        ```java
        if (!$CONDITION$) {
            // continue、break、または return をここで検討してください
        }
        $STATEMENTS$;
        ```
      * **コンテキスト:** よりクリーンなコードフローのためにガード節の使用を促進します。通常、構造を検出した後に「置換」アクションを使用します。

**コレクションとストリーム操作:**

3.  **`for (Type item : collection) { if (item.getProperty() == value) { ... } }` を Stream `filter` に置換**

      * **検索テンプレート:**
        ```java
        for ($TYPE$ $ITEM$ : $COLLECTION$) {
            if ($ITEM$.$METHOD$($VALUE$)) {
                $STATEMENTS$;
            }
        }
        ```
      * **置換テンプレート:**
        ```java
        $COLLECTION$.stream()
            .filter($ITEM$ -> $ITEM$.$METHOD$($VALUE$))
            .forEach($ITEM$ -> $STATEMENTS$); // または .map().collect() など
        ```
      * **コンテキスト:** フィルタリングのための従来のループからJavaストリームへの移行。これは一般的な例です。`map`、`collect`などには、より具体的なテンプレートがおそらく必要です。

4.  **`new ArrayList<>().add(item1); new ArrayList<>().add(item2);` を `List.of(item1, item2);` に置換**

      * **検索テンプレート:** (これは複数の`add`呼び出しに対して複数のテンプレート、または`add`呼び出しに対するより複雑な正規表現を必要とする場合があります。2つのアイテムに対するより単純なアプローチ):
        ```java
        java.util.ArrayList<$TYPE$> $LIST$ = new java.util.ArrayList<>();
        $LIST$.add($ITEM1$);
        $LIST$.add($ITEM2$);
        ```
      * **置換テンプレート:**
        ```java
        java.util.List<$TYPE$> $LIST$ = java.util.List.of($ITEM1$, $ITEM2$);
        ```
      * **コンテキスト:** 不変リストのためにJava 9+の`List.of()`を使用します。

**エラーハンドリングとリソース管理:**

5.  **`try { ... } catch (Exception e) { e.printStackTrace(); }` をより具体的なロギングに置換**

      * **検索テンプレート:**
        ```java
        try {
            $STATEMENTS$;
        } catch (java.lang.Exception $EXCEPTION$) {
            $EXCEPTION$.printStackTrace();
        }
        ```
      * **置換テンプレート:**
        ```java
        try {
            $STATEMENTS$;
        } catch (java.lang.Exception $EXCEPTION$) {
            // 好みのロギングフレームワークに置き換えてください。例:
            // logger.error("An error occurred", $EXCEPTION$);
            throw new RuntimeException($EXCEPTION$); // または特定の例外を再スロー
        }
        ```
      * **コンテキスト:** スタックトレースの単なる出力ではなく、適切なエラーロギングを促進します。

6.  **`try { ... } finally { closeable.close(); }` を `try-with-resources` に置換**

      * **検索テンプレート:**
        ```java
        java.io.Closeable $CLOSEABLE$ = null;
        try {
            $CLOSEABLE$ = $INITIALIZATION$;
            $STATEMENTS$;
        } finally {
            if ($CLOSEABLE$ != null) {
                $CLOSEABLE$.close();
            }
        }
        ```
      * **置換テンプレート:**
        ```java
        try ($CLOSEABLE$ = $INITIALIZATION$) {
            $STATEMENTS$;
        }
        ```
      * **コンテキスト:** リソース管理を`try-with-resources` (Java 7+) を使用するように近代化します。

**クラスとメソッド構造:**

7.  **`final` にできるフィールドを検索**

      * **検索テンプレート:**
        ```java
        class $CLASS$ {
            $TYPE$ $FIELD$;
        }
        ```
      * **置換テンプレート:** (これは検索用であり、その後クイックフィックスを使用します)
        ```java
        class $CLASS$ {
            // 一度だけ代入される場合は、これをfinalにすることを検討してください
            final $TYPE$ $FIELD$;
        }
        ```
      * **コンテキスト:** 不変性を改善する機会を特定します。複数の代入がないフィールドのみを表示するようにフィルターを設定します。

8.  **`private static final Logger logger = LoggerFactory.getLogger(MyClass.class);` をカスタムロガーユーティリティに置換**

      * **検索テンプレート:**
        ```java
        private static final org.slf4j.Logger $LOGGER_VAR$ = org.slf4j.LoggerFactory.getLogger($CLASS_NAME$.class);
        ```
      * **置換テンプレート:**
        ```java
        private static final org.slf4j.Logger $LOGGER_VAR$ = com.yourcompany.util.LoggerProvider.getLogger(); // またはユーティリティからのより具体的な getLogger($CLASS_NAME$.class)
        ```
      * **コンテキスト:** コードベース全体で特定のロギング初期化パターンを強制します。

**アノテーションとボイラープレート:**

9.  **スーパークラスのメソッドをオーバーライドするメソッドに `@Override` を追加 (欠落している場合)**

      * **検索テンプレート:** (これはより複雑で、多くの場合IntelliJの組み込みインスペクションで処理する方が良いですが、デモ用です)
        ```java
        class $CLASS$ {
            $RETURN_TYPE$ $METHOD$($PARAMS$) {
                $STATEMENTS$;
            }
        }
        ```
      * **置換テンプレート:** (これも検索用であり、その後クイックフィックスを適用します)
        ```java
        class $CLASS$ {
            @Override // スーパークラスのメソッドをオーバーライドする場合は追加
            $RETURN_TYPE$ $METHOD$($PARAMS$) {
                $STATEMENTS$;
            }
        }
        ```
      * **コンテキスト:** 良い習慣を強制し、タイポを捕捉します。メソッドがスーパークラス/インターフェースに存在するかチェックするフィルターを使用します。

10. **繰り返しの `getter/setter` メソッドを Lombok アノテーションに置換**

      * **検索テンプレート:** (単一のゲッターの場合、クラスに対してこれは非常に繰り返しになります)
        ```java
        public $TYPE$ get$PROPERTY_NAME$() {
            return this.$FIELD_NAME$;
        }
        ```
      * **置換テンプレート:** (これは概念的です。ゲッターを削除し、フィールドまたはクラスに`@Getter`を追加します)
        ```java
        // フィールドの @lombok.Getter での置換を検討してください:
        // @lombok.Getter
        // private $TYPE$ $FIELD_NAME$;
        ```
      * **コンテキスト:** Lombokへの移行を自動化します。完全なクラスの場合、クラス自体をターゲットとし、これらのメソッドの存在に基づいて`@Data`または`@Getter/@Setter`アノテーションを提案する場合があります。これはより高度で、潜在的に複数ステップの変換の一つです。

**IntelliJでの使用方法:**

1.  `Analyze` -> `Inspect Code...` に移動します。
2.  `Inspection Profile` ウィンドウで、プロファイル名の隣の`...`をクリックして編集します。
3.  `Java` -> `General` -> `Structural Search Inspection` に移動します。
4.  `+` ボタンをクリックして新しい検索/置換テンプレートを追加します。
5.  `Search Template` と `Replacement Template` を定義します。
6.  `Variables` タブを使用して変数に対する制約 (例: 型、テキスト、カウント) を定義します。
7.  コードに対してインスペクションを実行します。IntelliJが置換を提案したり、検出結果を強調表示したりします。

これらの例は、Structural Search and Replaceの多様性を示しています。テンプレートが具体的で制約が多ければ多いほど、置換は正確で有用になります。
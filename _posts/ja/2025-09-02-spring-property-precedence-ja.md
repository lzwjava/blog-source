---
audio: false
generated: true
image: false
lang: ja
layout: post
title: Springプロパティ優先順位ルールの解説
translated: true
type: note
---

Springでは、**重複したプロパティキー**が設定ソース（例: `application.properties`、`application.yml`、環境変数、コマンドライン引数など）に存在する場合、**優先順位が最も高い最後の設定が適用されます**。

以下に詳細な動作を説明します:

### 1. プロパティソースの順序付け

Spring Bootは明確に定義された**プロパティソースの順序**を適用します。例:

* コマンドライン引数
* `application.properties` / `application.yml`（プロファイル固有のものが最初、その後デフォルト）
* 環境変数
* システムプロパティ
* コード内のデフォルト値（`@Value("${...:default}")`）

同じプロパティキーが複数のソースに存在する場合、Springは**最も優先順位の高いソース**の値を選択します。

### 2. 同一ファイル内の場合

**単一ファイル内**（例: `application.properties`）で同じプロパティキーが繰り返し定義されている場合、Springは**最後に宣言された値**を使用します。
例（`application.properties`）:

```properties
server.port=8080
server.port=9090
```

この場合、`server.port=9090`が有効になります。

### 3. 複数ファイル間の場合

`application.properties`と`application-dev.properties`の両方で同じプロパティを定義し、`dev`プロファイルを有効にした場合、`application-dev.properties`の値がデフォルトの値を上書きします。

### 4. `@PropertySource`を使用する場合

`@PropertySource`を使用して複数のプロパティファイルを読み込む場合、宣言順序が重要になります。`ignoreResourceNotFound`でマークするか、優先順位を明示的に制御しない限り、後から読み込まれたファイルの値が前の値を上書きします。

---

✅ **まとめ:**

* Springはプロパティを**ソースの優先順位**に基づいて解決します。
* **同一ファイル内**では、**最後のキー定義**が優先されます。
* ファイル/プロファイル間では、**アクティブなプロファイルまたは後から読み込まれたファイルのプロパティ**が前の値を上書きします。

**正確なSpring Bootのプロパティ優先順位階層（最高から最低まで）** もお見せしましょうか？これにより、どこで上書きが発生するかが非常に明確になります。
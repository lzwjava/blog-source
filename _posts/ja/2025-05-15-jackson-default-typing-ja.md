---
audio: false
generated: true
image: false
lang: ja
layout: post
title: Jacksonのデフォルトタイピングの説明と無効化
translated: true
type: note
---

Jackson (`com.fasterxml.jackson.databind`ライブラリ)において、**default typing**は`ObjectMapper`の機能で、オブジェクトが元のポリモーフィックな型に逆シリアル化できるように、シリアル化されたJSONに型メタデータ（`@class`や`@type`など）を自動的に含めるものです。

例えば、`Dog`と`Cat`の両方を含む`List<Animal>`をシリアル化する場合、default typingは追加のJSONフィールドを追加し、後でどのサブクラスを再インスタンス化するかをJacksonが認識できるようにします。

---

### 無効化の仕組み

**default typingを無効化**すると、Jacksonはこれらの追加の型メタデータフィールドの注入を停止します。これは以下を意味します：

* JSON出力は`@class`/`@type`ヒントなしで「よりクリーン」になります。
* 逆シリアル化時、Jacksonは元のランタイム型ではなく、宣言された静的な型（渡されたターゲット型）を使用してのみオブジェクトを再構築できます。
* `@JsonTypeInfo`、`@JsonSubTypes`、またはカスタムモジュールを明示的に設定しない限り、ポリモーフィックな使用例は機能しなくなります。

---

### 関連メソッド

* **有効化** (2.10以前のスタイル):

  ```java
  objectMapper.enableDefaultTyping();
  ```

  (非推奨。過度に寛容でセキュリティリスクを導入するため)

* **無効化**:

  ```java
  objectMapper.disableDefaultTyping();
  ```

  または新しいバージョン(2.10+)では、以下を呼び出します:

  ```java
  objectMapper.activateDefaultTyping(PolymorphicTypeValidator, ObjectMapper.DefaultTyping.NON_FINAL);
  ```

  *無効化*するには、このメソッドを**呼び出さない**だけです（有効にしない限りdefault typingはありません）、または以下を呼び出すこともできます:

  ```java
  objectMapper.deactivateDefaultTyping();
  ```

---

### セキュリティと理論的根拠

* **default typingは現代のJacksonバージョンではデフォルトで無効化**されています。これは、悪用される可能性があるためです（攻撃者が危険なクラスをインスタンス化するJSONを作成する可能性があります）。
* 無効化すると、Jacksonは「より安全な」モードで動作し、逆シリアル化は明示的にバインドした型に対してのみ機能し、任意のランタイム型に対しては機能しません。
* ポリモーフィックなサポートが必要な場合は、グローバルなdefault typingに依存するのではなく、クラスに`@JsonTypeInfo`を注釈して設定すべきです。

---

✅ **要約:**
default typingを無効化すると、JacksonはJSONに型メタデータを含め**ない**ように指示します。つまり、逆シリアル化時にポリモーフィックなサブタイプを自動的に再構築しなくなります。これは柔軟性を低下させますが、より安全でJSONをクリーンに保ちます。

default typingを有効化した場合と無効化した場合の**前後のJSON例**を示しましょうか？
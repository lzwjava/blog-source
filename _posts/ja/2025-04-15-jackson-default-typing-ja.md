---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: Jacksonデフォルトタイピングの解説
translated: true
type: note
---

### JacksonのObjectMapperにおけるDefault Typingとは

Jacksonの`ObjectMapper`は、JavaオブジェクトをJSONにシリアライズし、JSONをオブジェクトにデシリアライズするためのJackson JSONライブラリのコアクラスです。「Default typing」は、ポリモーフィックな型（例えば、フィールドが異なるサブクラスを保持できる場合）の処理を強化する機能です。この機能は、シリアライゼーション中にJSON出力に型情報を埋め込み、デシリアライゼーション中に正しい具象クラスをインスタンス化するためにマッパーが使用します。

Default typingが無効の場合、Jacksonは宣言された型（例えば、抽象基底クラスやインターフェース）に依存し、サブタイプを指定するために`@JsonTypeInfo`アノテーションのようなカスタム設定が必要になることがあります。Default typingを有効にすると、ポリモーフィズムに対するグローバルまたはセミグローバルなフォールバックを提供し、特に混合型を持つコレクションやマップで有用です。

### 仕組み

Default typingを有効にすると、シリアライゼーションプロセスが変更されます：
1. **シリアライゼーション**: オブジェクトグラフをシリアライズする際、Jacksonはポリモーフィックなオブジェクトのランタイム型を示すために、特別な`@class`フィールドまたは類似のメタデータをJSONに追加します。これは、宣言された型が具象クラスを完全に指定しない型（例えば、`String`オブジェクトと`Integer`オブジェクトを含む`List`、または抽象クラスのフィールド）に対してのみ発生します。

2. **デシリアライゼーション**: デシリアライゼーション中、マッパーはこの埋め込まれた型情報を使用して正確なクラスを検索し、インスタンス化します。これはJacksonの`TypeFactory`を活用して型を動的に解決します。

有効にするには、`ObjectMapper`インスタンスに対して以下のいずれかのメソッドを呼び出します：
- `mapper.enableDefaultTyping()`: 定数時間のポリモーフィック型包含を有効にする非推奨メソッド（セキュリティ問題の影響を受けやすい）。
- `mapper.activateDefaultTyping(ObjectMapper.DefaultTyping policy)`: Jackson 2.10で導入された、より安全で推奨される代替手段。`DefaultTyping` enum値を指定できます。例：
  - `JAVA_LANG_OBJECT`: すべての`Object`参照に対して型情報を含めます。
  - `NON_CONCRETE_AND_ARRAYS`: 抽象/非具象型および配列に対して型情報を含めます。
  - `NON_FINAL`: 非finalクラスに対して型情報を含めます。

使用例：
```java
import com.fasterxml.jackson.databind.ObjectMapper;
import static com.fasterxml.jackson.databind.ObjectMapper.DefaultTyping;

ObjectMapper mapper = new ObjectMapper();
mapper.activateDefaultTyping(DefaultTyping.NON_CONCRETE_AND_ARRAYS);
```

有効にしない場合、混合型を持つ`List<Object>`をシリアライズすると、JSONは型の詳細を省略する可能性があり、デシリアライゼーションエラーの原因となります。有効にすると、JSONには型ヒントが含まれます。例：`[{"@class": "java.lang.String", "value": "hello"}, {"@class": "java.lang.Integer", "value": 42}]`。

### セキュリティ考慮事項と制限

- **脆弱性**: Default typing（特に古い`enableDefaultTyping()`）を盲目的に有効にすると、細工されたJSONを介して任意のクラスをデシリアライズできるため、データ抽出などの攻撃に対してシステムを公開する可能性があります。Jacksonは新しいバージョンではデフォルトでこれを制限し、カスタマイズされない限り一般的な型のみを許可します。
- **ユースケースへの適合**: ポリモーフィックなデータを持つ信頼された環境（例えば、内部API）に最適です。公開APIでは、セキュリティを強化するために明示的な型アノテーションまたはカスタムシリアライザー/デシリアライザーを優先してください。
- **パフォーマンス**: 埋め込まれた型情報によりJSONサイズが増加し、わずかなオーバーヘッドが追加されます。

これが別の「object mapper」（例えば、Elasticsearchのものや他のライブラリ）に関するものである場合は、合わせた説明のために詳細なコンテキストを提供してください。完全な詳細については、Jacksonの公式ドキュメントを参照してください。
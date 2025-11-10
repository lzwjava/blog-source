---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: Jackson多相デシリアライゼーションの概要
translated: true
type: note
---

### Jacksonのポリモーフィックなデシリアライゼーション概要

JacksonはJSONのシリアライゼーションとデシリアライゼーションを行うJavaライブラリです。ポリモーフィックなデシリアライゼーションにより、JacksonはJSONに埋め込まれた型情報に基づいて、デシリアライゼーション中に基底クラスの正しいサブクラスを自動的にインスタンス化できます。これは継承階層を扱う際に有用で、JSONデータから適切なオブジェクト型が作成されることを保証します。

主な構成要素:
- **@JsonTypeInfo**: JSON内で型情報がどこに、どのように格納されるかを制御するアノテーション
- **@JsonSubTypes**: サブクラス（サブタイプ）とその識別子をリストするアノテーション
- Jacksonのサブタイプ解決がマッピングを処理

これらがない場合、Jacksonはすべてのオブジェクトを基底クラスとしてデシリアライズし、サブクラス固有のデータが失われる可能性があります。

### 仕組みのステップバイステップ解説

1. **基底クラスへのアノテーション**:
   - `@JsonTypeInfo`を使用して、型情報が埋め込まれる場所を指定（例：JSONオブジェクト内のプロパティとして）
   - 例:
     ```java
     @JsonTypeInfo(use = JsonTypeInfo.Id.NAME, include = JsonTypeInfo.As.PROPERTY, property = "@type")
     @JsonSubTypes({
         @JsonSubType(value = Cat.class, name = "cat"),
         @JsonSubType(value = Dog.class, name = "dog")
     })
     public abstract class Animal {
         public String name;
     }
     ```
     - `use = JsonTypeInfo.Id.NAME`: 型に名前（文字列識別子）を使用
     - `include = JsonTypeInfo.As.PROPERTY`: 型情報をJSONオブジェクト内のプロパティ（"@type"）として追加
     - `@JsonSubTypes`: サブクラス名をJavaクラスにマッピング（例："cat" → Cat.class）

2. **シリアライゼーションプロセス**:
   - CatまたはDogオブジェクトをシリアライズする際、Jacksonは型識別子をJSONに追加
   - 出力例: `{"@type": "cat", "name": "Whiskers", "purr": true}`（Catに"purr"フィールドがある場合）

3. **デシリアライゼーションプロセス**:
   - JacksonはJSONを読み込み、型情報（例："@type"プロパティ）をチェック
   - 識別子（"cat"）を`@JsonSubTypes`を使用して登録済みサブクラス（Cat.class）にマッピング
   - 正しいサブクラスをインスタンス化し、そのフィールドを設定
   - 一致するものがない場合や型情報が欠落している場合、基底クラスにデフォルト設定されるか、例外がスローされる（`defaultImpl`で設定可能）

4. **サポートされる型情報フォーマット**:
   - `@JsonTypeInfo.As.PROPERTY`: フィールドとしての型（例：`{"@type": "cat", ...}`）
   - `@JsonTypeInfo.As.WRAPPER_OBJECT`: 型をキーとしてオブジェクトをラッパーで包む（例：`{"cat": {...}}`）
   - `@JsonTypeInfo.As.WRAPPER_ARRAY`: 配列フォーマットを使用
   - `@JsonTypeInfo.As.EXTERNAL_PROPERTY`: 別個のフィールドに型情報（高度な設定、XML様の構造用）

### 高度な設定とエッジケース

- **カスタム名マッパー**: `@JsonTypeInfo(use = JsonTypeInfo.Id.CLASS)`を使用して、完全修飾クラス名をJSONに直接埋め込む（例：`{"@class": "com.example.Cat", ...}`）。リファクタリング時に脆弱になる可能性あり
- **デフォルト実装**: `defaultImpl = Animal.class`を追加して、型情報が欠落している場合のフォールバックを設定
- **可視性とミックスイン**: ソースクラスを変更できない場合、ミックスインクラスを介してアノテーションを適用
- **エラーハンドリング**: 型情報が登録済みサブタイプと一致しない場合、Jacksonは`JsonMappingException`をスロー。カスタムデシリアライザで処理可能
- **パフォーマンス**: 効率的なルックアップによりデシリアライゼーション中のオーバーヘッドは最小限だが、型情報の埋め込みによりJSONペイロードサイズが増加

詳細なドキュメントは、Jacksonの公式ガイドを参照してください：[Polymorphic Type Handling](https://github.com/FasterXML/jackson-docs/wiki/JacksonPolymorphicDeserialization)。この機能はJackson 2.x以降で安定しており、Gsonなどの他のJSONライブラリでも同様の概念があります。さらにカスタマイズする場合は、信頼できない入力に対するセキュリティのために`PolymorphicTypeValidator`を拡張してください。
---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: RustとJavaにおける最速のJSONライブラリ
translated: true
type: note
---

### RustとJavaで最速のJSONライブラリ

RustとJavaで最速のJSONライブラリを比較するには、コア操作であるパース（デシリアライゼーション）とシリアライゼーションのパフォーマンスを見る必要があります。パフォーマンスは通常、スループット（例：GB/秒）またはtwitter.json（中規模サイズのオブジェクト配列）、canada.json（大規模な数値配列）、citm_catalog.json（ネストされたオブジェクト）などの標準データセットに対する処理時間で測定されます。これらのデータセットはJSONベンチマークで一般的です。

#### Rustで最速: sonic-rs
- **概要**: sonic-rsは、CloudWeGoによるSIMDアクセラレーションを備えたRust用高速JSON処理ライブラリです。simd-jsonの「テープ」のような中間ステップを経ずに、Rustの構造体に直接パースするため、デシリアライゼーションが高速です。構造化（構造体へ）と非構造化（DOMライクへ）の両方のパースをサポートします。
- **主なパフォーマンスハイライト** (Intel Xeon Platinum 8260 @ 2.40GHzでのベンチマークより):
  - 構造体へのデシリアライゼーション (時間、ms、低いほど良い):
    - twitter.json: ~0.7 ms
    - canada.json: ~3.8 ms
    - citm_catalog.json: ~1.2 ms
  - これにより、sonic-rsはデシリアライゼーションにおいて、simd-json（もう一つのトップRustライブラリ）よりも1.5-2倍高速で、serde_json（標準ライブラリ）よりも3-4倍高速です。
  - シリアライゼーション: simd-jsonと同等かわずかに高速（例: twitter.jsonで ~0.4 ms）。
  - スループット: 文字列、数値、空白に対するSIMD最適化により、大規模な入力に対してしばしば2-4 GB/sを超えます。
- **長所**: 可能な場合はゼロコピー、低メモリ使用量、安全（チェック済み）モードと高速化のための安全でない（未チェック）モード。
- **短所**: 新しいライブラリであり、serde_jsonよりもエコシステムが未成熟。

#### Javaで最速: DSL-JSON または simdjson-java (ユースケースに応じて同率)
- **概要**:
  - DSL-JSONは、コンパイル時のコード生成（@CompiledJsonのようなアノテーション経由）を使用してリフレクションを回避しGCを最小化するため、高負荷シナリオでのデシリアライゼーションが非常に高速です。
  - simdjson-javaは、simdjson C++ライブラリのJavaポートであり、SIMDを使用してギガバイト/秒級のパースを実現します。大規模な入力に対して特に強力ですが、初期バージョンでは部分的なUnicodeサポートなどの制限があります。
- **主なパフォーマンスハイライト**:
  - DSL-JSON: 密なループ（例: 中規模オブジェクト ~500バイト）でのデシリアライゼーションにおいて、Jacksonよりも3-5倍高速。特定のデータセット数値は少ないですが、Protobufのようなバイナリコーデックと同等と主張されています。一般的なベンチマークでは、シリアライゼーションとパースでJacksonを3倍以上上回ります。
  - simdjson-java: Intel Core i5-4590での典型的な操作で ~1450 ops/sec、Jackson、Jsoniter、Fastjson2よりも3倍高速。大規模な入力では、C++版と同様に1-3 GB/sに近づきます。比較では、パースにおいてJsoniterよりも3倍高速です。
  - Jsoniter (名誉ある言及): Jacksonよりも2-6倍高速。整数でJacksonの3.22倍、オブジェクトリストで2.91倍といったデコード速度を実現（JMHベンチマークにおけるスループット比）。
  - 参考までに、Jackson（人気はあるが最速ではない）は標準データセットをこれらのリーダーの2-3倍の時間で処理します。
- **長所**: DSL-JSONは低GC、高スループットのアプリ向け。simdjson-javaは大規模データに対する生の速度向け。両者ともJVMの制約をうまく扱います。
- **短所**: DSL-JSONは最大速度のためにアノテーションが必要。simdjson-javaには機能ギャップがある（例: 古いバージョンでの完全な浮動小数点数のパース）。

#### 直接比較: Rust vs Java
- **パフォーマンスギャップ**: Rustのsonic-rsは、同様のタスクにおいてJavaのトップライブラリよりも一般的に2-5倍高速です。例:
  - 1GBのJSONログを処理する（ストリーミング＋パース）実世界のAWS Lambdaベンチマークでは、simd-jsonを使用したRustは約2秒（0.5 GB/s）かかったのに対し、Jsoniterを使用したJavaは8-10秒（0.1 GB/s）かかりました。simdjson-javaを使用すればギャップを約3秒（0.3 GB/s）に縮められますが、ネイティブコンパイル、GCポーズなし、より優れたSIMD活用により、依然としてRustが勝ります。
  - 標準データセットでは、sonic-rsはcanada.jsonを約4 msでデシリアライズするのに対し、JsoniterやDSL-JSONのようなJavaライブラリは同等のセットアップで10-20 msかかります（直接対決は稀なため間接的）。
  - シリアライゼーションはより接近し、Rustが時に1.5-2倍高速なだけの場合もあります。
- **Rustが高速な理由**: ネイティブコード、JVMオーバーヘッドなし、ゼロコスト抽象化、メモリに対するより優れた制御。JavaライブラリはGCとバイトコードによって制限されますが、コンパイル時生成（DSL-JSON）のような最適化が役立ちます。
- **その他の要因**:
  - 機能: Rustライブラリは柔軟性のためにserdeエコシステムとよく統合されます。JacksonのようなJavaライブラリは複雑なスキーマに対してより多くのプラグインを持ちます。
  - ユースケース: Rustは超高パフォーマンス（例: サーバー、CLIツール）向け。Javaはより容易な統合性を持つエンタープライズ向け。
  - 注意点: ベンチマークはハードウェア、データセット、JVMバージョン（例: Java 21+はGCを改善）によって変動します。Rustの安全性チェックは、未チェックモードを使用しない場合、オーバーヘッドを追加する可能性があります。

特定のデータセットやユースケース（例: シリアライゼーションのみ）があれば、さらに深く調査できます。

### 参考文献
- sonic-rs GitHub (Rustベンチマーク) (https://github.com/cloudwego/sonic-rs)
- simdjson GitHub (RustおよびJavaポートの基盤) (https://github.com/simdjson/simdjson)
- Serverless Speed: Rust vs. Go, Java, and Python in AWS Lambda (ベンチマーク) (https://scanner.dev/blog/serverless-speed-rust-vs-go-java-and-python-in-aws-lambda-functions)
- The Lightning Fast JSON Parser Library For Java (simdjson-java) (https://www.i-programmer.info/news/80-java/16553-the-lightning-fast-json-parser-library-for-java.html)
- Jsoniter Benchmark (Java比較) (https://jsoniter.com/benchmark.html)
- DSL-JSON vs Jackson (Javaデシリアライゼーション) (https://medium.com/@vishalpriyadarshi/dsl-json-vs-jackson-who-deserializes-faster-in-java-7f0ee164606a)
- Optimizing JSON Performance in Java - 2025 Edition (https://medium.com/towardsdev/optimizing-json-performance-in-java-what-actually-works-2025-edition-4f124e24d786)
---
audio: false
date: 2025-09-11
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: MavenライフサイクルとJaCoCoの理解
translated: true
type: note
---

良い質問です — これは Maven の*ライフサイクルフェーズ*と、プラグインがそれらにどのようにバインドされるかに関係しています。

### ライフサイクルの基本

Maven には3つの標準的なライフサイクルがあります: `clean`、`default` (時々 *build* と呼ばれる)、そして `site` です。
*default* ライフサイクル内では、重要なフェーズは以下の順序で進みます:

* `validate`
* `compile`
* `test`
* `package`
* `verify`
* `install`
* `deploy`

各フェーズは、それ以前のすべてのフェーズを含みます (`mvn verify` を実行すると、Maven は `validate` から `verify` までのすべてを実行します)。`mvn package` を実行すると、アーティファクト (JAR/WAR) を作成した後で停止し、`verify` は実行しません。

### JaCoCo が関与する理由

JaCoCo Maven プラグインは通常、その **`prepare-agent`** ゴールを、設定に応じて `initialize` または `verify` フェーズにバインドします。

* もし `verify` にバインドされている場合 (カバレッジレポートの一般的な設定)、`mvn verify` がそれをトリガーします。
* `mvn package` はライフサイクルでそこまで進まないため、`verify` フェーズ (したがって JaCoCo のステップ) はスキップされます。

これが、`mvn verify` を実行したときには JaCoCo が実行され、`mvn package` を実行したときには実行されない理由です。

### 実用的な要点

* ビルドアーティファクトだけが必要な場合は **`mvn package`** を使用します (高速で、余分なチェックなし)。
* *結合テスト、チェック、カバレッジレポート、または後のフェーズにバインドされた QA プラグイン*を実行したい場合は **`mvn verify`** を使用します。

👉 `mvn package` でも常に JaCoCo を実行したい場合は、`pom.xml` で `prepare-agent` ゴールを `test` や `package` のようなより早いフェーズに再バインドできます。

JaCoCo の `prepare-agent` を `verify` ではなく `test` ですでに実行するようにする具体的な `pom.xml` スニペットをお見せしましょうか？
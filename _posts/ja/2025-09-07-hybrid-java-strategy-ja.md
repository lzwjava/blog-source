---
audio: false
date: 2025-09-07
generated: true
image: false
lang: ja
layout: post
title: ハイブリッドJava開発戦略
translated: true
type: note
---

短い結論：大規模なJavaコードベースでは、**ハイブリッド**なアプローチが最適です。**VS Code**をAIファーストのコックピットとして使い（Claude Code + Copilot = より高速な反復とボイラープレート生成）、**IntelliJ IDEA**は「外科手術」用に保持します（大規模なリファクタリング、インスペクション、高度なSpring/Gradle/Mavenウィザード）。一つの宗教を選ぶ必要はありません。🙂

以下が私の考え方です - 表はなく、本質のみ：

### VS Codeが輝く場面

* **AIワークフロー**：Copilotのインライン補完は依然としてVS Codeが最高で、Claude Codeのリポジトリレベルの推論もここではより軽快に感じられます。サービスの草案作成、テスト、マッパー、SQL、迅速な再設計に最適です。
* **軽量でモジュラー**：必要なものだけを追加できます。巨大なモノレポでも、起動時間とメモリ使用量はより扱いやすいものです。
* **「ジャンプ」+ LSP**：Java拡張機能により、「定義/実装へ移動」、型階層、呼び出し階層、シンボル検索は日々の作業には十分に堅牢です。

推奨拡張機能（IDで検索）：

* `vscjava.vscode-java-pack`（以下のほとんどをバンドル）
* `redhat.java` (Language Support for Java)
* `vscjava.vscode-java-debug` / `vscjava.vscode-java-test`
* `vscjava.vscode-maven` / `vscjava.vscode-gradle`
* `vscjava.vscode-spring-boot-dashboard` + `vscjava.vscode-spring-initializr`
* `sonarsource.sonarlint-vscode`（静的チェック）
* `streetsidesoftware.code-spell-checker`（JavaDocで驚くほど役立つ）
* Claude Code + GitHub Copilot

大規模プロジェクト向けパフォーマンス調整（`.vscode/settings.json`に記述）：

```json
{
  "java.maxConcurrentBuilds": 4,
  "java.jdt.ls.vmargs": "-Xms512m -Xmx4g -XX:+UseG1GC -XX:+UseStringDeduplication",
  "java.errors.incompleteClasspath.severity": "ignore",
  "java.referencesCodeLens.enabled": false,
  "java.implementationsCodeLens.enabled": false,
  "files.watcherExclude": {
    "**/target/**": true,
    "**/.gradle/**": true,
    "**/node_modules/**": true
  }
}
```

ヒント：

* **Gradle**または**Maven**としてインポート（可能であれば混合ビルドは避ける）。
* 複数サービスの実行/デバッグには**Spring Boot Dashboard**を有効にする。
* Claude/Copilotにクラスとテストの草案を作成させるが、**SonarLint**と単体テストをガードレールとして使用する。

### IntelliJ IDEAが依然として優位な場面

* **リファクタリングの深さと正確さ**：巨大な階層、ジェネリクスを多用するAPI、Lombok、XML設定、Spring Beanのワイヤリングにわたる名前変更/移動/抽出 - IDEAのセマンティックモデルは圧倒的です。
* **インスペクションとクイックフィックス**：組み込みのコードインスペクション（および構造的検索/置換）は、ほとんどのVS Code設定よりも微妙なコードの臭いを捕捉します。
* **UMLとナビゲーションの利便性**：データフロー（ここから/ここへ）、依存関係図、高度な検索スコープは、複雑なドメインでの時間を節約します。

実用的なパターン：

* **探索、スキャフォールディング、反復的な編集**は、VS CodeでClaude/Copilotを使用して行う。
* **些細でないリファクタリング**（例：コアモジュールの分割、40モジュールにわたるAPI契約の変更、Spring設定の移行）が必要な場合、同じリポジトリをIDEAで開き、一度インデックス作成させた後、安全にリファクタリングを実行し、プッシュしてからVS Codeに戻る。

### 「Codex」について

OpenAIの旧**Codex**モデルは以前に提供終了となりました。現在は主に**GitHub Copilot**（内部ではOpenAI技術を使用）と**Claude Code**を使用します。「Codex」は歴史的なものとして扱い、現在のスタックは**Copilot + Claude Code**であるべきです。

### VS Codeでの静的解析と品質

* VS Codeの**SonarLint**は、ほぼIDEAのような感覚を与えます；CIのSonarQube/SonarCloudゲートと組み合わせて使用します。
* **SpotBugs**と**Checkstyle**をGradle/Mavenプラグイン経由で追加し、品質チェックが（ローカルだけでなく）CIでも実行されるようにします。
* **JUnit**テストエクスプローラーと**Coverage Gutters**拡張機能を使用して、タイトなレッド・グリーン・ループを維持します。

### Spring/エンタープライズ特有の事項

* VS Codeの**Springツーリング**は、実行/デバッグ、アクチュエーターエンドポイント、プロパティのヒントに優れています。複雑な自動設定やメタアノテーションについては、IDEAが依然としてより確実に解決します - アノテーションが「不可解」に感じられる時に使用してください。
* **Gradle**のマルチモジュール巨大プロジェクトの場合：デーモンと並列ビルドを有効にし、ワークスペースのサイズを制限するためにコンポジットビルドを検討してください。

### スケーラブルなAIワークフロー

* **Copilotインライン**：入力時の小さな編集用。
* **Claude Code**チャット：リポジトリ全体にわたる推論用（「`LedgerPosting`のコンストラクタを変更した場合の副作用は？」/「カスタムリトライをresilience4jに置き換えるPRを草案して」）。
* モデルに**リファクタリング計画とチェックリスト**の作成を依頼し、変更を小さなレビュー可能なコミットで適用します。
* **モデルの出力をテスト下に置く**：AIが生成したPRには、単体/統合テストの差分も含めることを必須とします。

### では…どちらをメインにすべきか？

* あなたの一日が**コーディング + 反復 + 多数のAI支援**である場合 → **VS Code**をプライマリエディタとして使用するのが現時点では快適です。
* あなたの一日が**設計 + 大規模リファクタリング + フレームワークのエッジケースのデバッグ**である場合 → それらの瞬間のために**IntelliJ**を開いたままにします。
* 多くのシニアエンジニアは両方を行き来しています。それは非効率ではなく、リスクレベルに応じて適切なツールを使用しているのです。

必要であれば、あなたのモノレポに合わせて調整された、一度限りの**VS Code Javaブートストラップ**（extensions.json, settings.json, 推奨タスク/起動設定）と、「重機を呼び出す」瞬間のための短いIDEAチェックリストを生成できます。
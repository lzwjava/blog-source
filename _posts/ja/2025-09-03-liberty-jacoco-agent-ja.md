---
audio: false
generated: true
image: false
lang: ja
layout: post
title: リバティエージェントとJaCoCoエージェントの比較
translated: true
type: note
---

WebSphere Liberty (WLP) において、`ws-javaagent.jar` は IBM 独自の Java インストルメンテーションエージェントです。これは主に、ランタイムモニタリング、診断、および Application Performance Management (APM)、Health Center、あるいは Liberty 自身のモニタリング機能との連携に使用されます。これを有効にすると、Liberty はプロファイリング、ガベージコレクション、スレッド、その他の JVM レベルのメトリクスを自動的に収集できます。

一方、JaCoCo の `jacocoagent.jar` は、特化した **コードカバレッジエージェント** です。その目的は、テスト実行やアプリケーション実行時にカバレッジデータ (例えば、どのクラス、メソッド、ブランチが実行されたか) を生成できるように、ランタイムでバイトコードをインストルメント化することです。

したがって、区別は以下の通りです:

* **`ws-javaagent.jar`** → Liberty および IBM ツール群のための一般的なモニタリング、プロファイリング、診断。
* **`jacocoagent.jar`** → Liberty に依存しない、テスト/コードカバレッジレポート生成。

JaCoCo のエージェントを Liberty のものに置き換えるべきではありません。もしあなたの目的が **テストカバレッジレポートの生成** (CI パイプライン、SonarQube、Maven/Gradle レポートなど向け) であるならば、**JaCoCo エージェント** を使い続けなければなりません。Liberty エージェントは JaCoCo の `.exec` カバレッジファイルを生成しません。

しかし、必要であれば両方を *同時に* 実行することは可能です — Java は複数の `-javaagent` 引数をサポートしています。例:

```bash
-javaagent:/path/to/ws-javaagent.jar
-javaagent:/path/to/jacocoagent.jar=destfile=jacoco.exec,output=file
```

👉 要約:
カバレッジには **`jacocoagent.jar`** を使用。
Liberty の診断/プロファイリングが必要な場合は **`ws-javaagent.jar`** を使用。
これらは異なる目的に役立ち、互換性はありません。

これらを Liberty サーバーの JVM オプションファイルで一緒に設定する方法もお見せしましょうか？
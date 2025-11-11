---
audio: false
generated: true
image: false
lang: ja
layout: post
title: YourKit Java Profiler による Liberty のプロファイリング
translated: true
type: note
---

WebSphere Liberty は、単なる別の JVM ベースのランタイムであるため、YourKit Java Profiler と非常にスムーズに統合できます。その仕組みは以下の通りです。

---

### 1. 統合の仕組み

YourKit Java Profiler は Liberty 固有のプラグインを必要としません。Liberty が動作する JVM プロセスにアタッチすることで動作します。一度アタッチされると、メソッド呼び出し、メモリ割り当て、スレッドアクティビティ、その他のランタイムイベントをインターセプトします。
Liberty は OpenJ9 (または HotSpot) JVM 上で動作するため、Liberty の起動時に YourKit エージェントを追加することでプロファイリングを有効にできます。

---

### 2. YourKit エージェントのアタッチ方法

主に2つの方法があります:

* **起動時アタッチ (サーバー推奨)**
  YourKit エージェントオプションを Liberty の `jvm.options` ファイル (`<wlp_home>/usr/servers/<server_name>/` 内) に追加します。
  例:

  ```
  -agentpath:/path/to/yourkit/bin/linux-x86-64/libyjpagent.so=port=10001,listen=all
  ```

  これにより、サーバー起動と同時にプロファイラエージェントがロードされます。

* **オンデマンド (動的) アタッチ**
  Liberty が既に実行中の場合は、YourKit GUI 経由でアタッチできます。YourKit は実行中の JVM をスキャンし、再起動せずに接続できます。本番環境のデバッグに便利ですが、権限 (同一ユーザー / JDK tools.jar) が必要です。

---

### 3. Liberty コンテキストでのプロファイリング

Liberty 上で実行する場合、以下のことが役立つかもしれません:

* **アプリケーションパッケージでフィルタリング** して、Liberty の内部コードに埋もれないようにする。
* **コールツリー / ホットスポットビューを使用** して、遅いサーブレット、JAX-RS エンドポイント、または CDI Bean を分析する。
* **JDBC とスレッドプールを監視** する。Liberty アプリケーションはコンテナ管理リソースに依存することが多いため。YourKit は JDBC 呼び出しをトレースし、待機時間を計測できます。
* **複数アプリの扱い** – Liberty が複数のアプリをホストする場合、YourKit のスレッドおよびクラスフィルタを使用して、対象のアプリにプロファイリングを絞り込む。

---

### 4. パフォーマンスに関する考慮事項

* プロファイリングには常にオーバーヘッドが伴います。開発時はフル CPU/メモリプロファイリングを使用しても問題ありませんが、本番環境では *instrumentation* ではなく *sampling* モードを使用してください。
* Liberty のモジュラークラスローディングにより、クラス名が重複することがあります。YourKit は通常これを処理しますが、フィルタリング時は注意してください。
* Liberty で IBM JDK を使用する場合は、HotSpot 用だけでなく、IBM J9/OpenJ9 用にビルドされた YourKit エージェントをダウンロードしてください。

---

### 5. 典型的なワークフロー

1.  開発マシンに YourKit をインストールする。
2.  エージェントのパスを指定して Liberty の `jvm.options` を修正する。
3.  Liberty を起動する。
4.  YourKit GUI から Liberty JVM に (ソケット経由またはアタッチで) 接続する。
5.  エンドポイント、メモリ使用量、またはスレッドロックをプロファイルする。
6.  オフライン分析用にスナップショットを保存する。

---

👉 **OpenJ9** (Liberty のデフォルト JVM) 上で動作する Liberty と YourKit の **ステップバイステップの設定例**、CPU プロファイリングとメモリプロファイリングのサンプル `jvm.options` 設定を含めてお伝えしましょうか？
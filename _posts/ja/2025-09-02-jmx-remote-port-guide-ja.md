---
audio: false
generated: true
image: false
lang: ja
layout: post
title: JMXリモートエージェントポートガイド
translated: true
type: note
---

**JMXリモートエージェント**は、Java Management Extensions（JMX）テクノロジーの一部です。これにより、管理者や監視ツールが、通常はTCP/IPを介して、JVMプロセスの外部から実行中のJavaアプリケーションに接続できるようになります。これは、本番環境でのJavaアプリケーションの監視、診断、管理によく使用されます。

以下に詳細を示します：

### 1. JMXリモートエージェントとは

* JVMの内部情報（メモリ使用量、スレッドアクティビティ、ガベージコレクション、クラスローディングなど）を*Managed Beans（MBeans）*として公開します。
* リモート（例：**jconsole**、**VisualVM**、またはPrometheusエクスポーターなどの監視ツールを介して）接続できます。
* 通常、以下のようなJVM起動フラグで有効になります：

  ```bash
  -Dcom.sun.management.jmxremote
  -Dcom.sun.management.jmxremote.port=9091
  -Dcom.sun.management.jmxremote.authenticate=false
  -Dcom.sun.management.jmxremote.ssl=false
  ```
* 有効にすると、JVMは指定されたポートにバインドされたRMI（Remote Method Invocation）コネクタサーバーを実行します。

### 2. ポート9091について

* 数字の**9091**自体には特別な意味はありません。JMX接続用に設定する単なるTCPポートです。
* 管理者は、利便性や標準ポートとの競合を避けるために、9091（または9010、9999など）を選択することがよくあります。
* `9091`でリッスンしている場合、JVMはそのポートでリモートJMX接続を受け入れます。
* セキュリティ保護されていない状態（`authenticate=false, ssl=false`）のままにすると、ネットワークアクセス権限を持つ誰でもJVMを制御または監視できるようになります。これは重大なセキュリティリスクです。

### 3. 典型的な使用方法

* **JConsole**による監視：

  ```bash
  jconsole host:9091
  ```
* 監視システム（例：Prometheus JMX Exporter）との統合。
* トラブルシューティング時のリモート管理（例：ヒープダンプ、スレッド、GC動作の確認）。

### 4. セキュリティに関する考慮事項

* JMXポートは常に以下で保護してください：

  * ネットワークファイアウォール（アクセス制限）。
  * 認証（`password`ファイルと`access`ファイル）。
  * 必要に応じてSSL。
* そうでない場合、セキュリティなしで9091を公開することは、JVMのリモートシェルレベルの制御権を付与するのと同じです。

---

✅ 要約すると：**ポート9091のJMXリモートエージェント**は、JVMがTCPポート9091を介して管理および監視インターフェースを公開していることを意味し、JConsoleやPrometheusなどのツールで使用できますが、セキュリティで保護する必要があります。

（セキュアでないモードではなく）パスワード認証で有効にするための**正確なJVMフラグ**をお見せしましょうか？
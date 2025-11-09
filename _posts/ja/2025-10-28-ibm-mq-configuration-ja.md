---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: IBM MQ WebSphere アプリケーションサーバー構成
translated: true
type: note
---

### 前提条件
IBM WebSphere Application Server (WAS) で IBM MQ (旧称 WebSphere MQ) を構成する前に、以下を確認してください：
- IBM MQ が専用サーバーにインストールされている (または、ローカルバインディングモードの場合は WAS と同じサーバー)。
- IBM MQ でキュー・マネージャーが作成されている (例: `crtmqm QMNAME` を使用)。
- 必要なキューがキュー・マネージャーに作成されている (例: MQ Explorer または `runmqsc` を使用)。
- IBM MQ クライアント・ライブラリ (JAR ファイル、例: `com.ibm.mq.allclient.jar`, `com.ibm.mqjms.jar`) が利用可能である。WAS が MQ からリモートの場合、WAS マシンに IBM MQ クライアントをインストールする。
- 権限のために WAS プロセスユーザーを `mqm` グループに追加する。
- Unix 系システムでの非 root ユーザーの場合、`setmqaut` を使用して権限を付与する。

### ステップバイステップの構成
この構成は、WAS 管理コンソールで JMS プロバイダー、接続ファクトリー、および宛先を設定することを含みます。これは、TCP/IP を介した分散 (クライアント) モード接続を想定しています。ローカルの場合はバインディングモードに調整してください。

1. **WAS 管理コンソールにアクセス**:
   - WAS サーバーを起動する。
   - ブラウザを開き、`https://localhost:9043/ibm/console` に移動する (ホスト/ポートを置き換えてください)。
   - 管理者資格情報でログインする。

2. **IBM MQ JMS プロバイダーを構成**:
   - **リソース > JMS > プロバイダー** に移動する。
   - **新規** をクリックする。
   - **WebSphere MQ メッセージング・プロバイダー** を選択する。
   - 詳細を入力する：
     - **名前**: 例: `MQProvider`。
     - **説明**: オプション。
     - **クラス・パス**: MQ JAR ファイルへのパス (例: `/opt/mqm/java/lib/*` または `<WAS_HOME>/lib/ext` にコピー)。
     - **ネイティブ・ライブラリー・パス**: バインディングモードで必須 (MQ ライブラリーへのパス、例: `/opt/mqm/lib64`)。
     - **外部初期コンテキスト・ファクトリー名**: `com.ibm.mq.jms.context.WMQInitialContextFactory` (クライアントモード用)。
     - **外部コンテキスト・プロバイダー URL**: 例: `host:1414/CHANNEL` (host = MQ サーバー IP, 1414 = デフォルトポート, CHANNEL = 例: `SYSTEM.DEF.SVRCONN`)。
   - 構成を保存する。

3. **キュー接続ファクトリーを作成**:
   - **リソース > JMS > キュー接続ファクトリー** に移動する (サーバーまたはセルにスコープを設定)。
   - **新規** をクリックする。
   - ステップ 2 で作成したプロバイダーを選択する。
   - 入力する：
     - **名前**: 例: `MQQueueCF`。
     - **JNDI 名**: 例: `jms/MQQueueCF`。
     - **キュー・マネージャー**: あなたの MQ キュー・マネージャー名 (例: `QM1`)。
     - **ホスト**: MQ サーバーのホスト名または IP。
     - **ポート**: 1414 (デフォルト)。
     - **チャネル**: 例: `SYSTEM.DEF.SVRCONN`。
     - **トランスポート・タイプ**: `CLIENT` (TCP/IP 用) または `BINDINGS` (ローカル用)。
     - **セキュリティー資格情報**: 必要な場合はユーザー ID とパスワード。
   - オプションの詳細プロパティー: 接続プールサイズを設定 (例: 負荷に基づいた最大接続数)。
   - 保存する。

4. **キュー宛先を作成**:
   - **リソース > JMS > キュー** に移動する。
   - **新規** をクリックする。
   - プロバイダーを選択する。
   - 各キューに対して：
     - **名前**: 例: `MyQueue`。
     - **JNDI 名**: 例: `jms/MyQueue`。
     - **キュー名**: MQ 内の正確なキュー名 (例: `MY.LOCAL.QUEUE`)。
     - **キュー・マネージャー**: 上記と同じ。
     - **ターゲット・クライアント・タイプ**: `MQ` または `JMS`。
   - 保存する。Pub/Sub を使用する場合はトピックについても繰り返す。

5. **(オプション) バインディングモード用に WebSphere MQ サーバーを構成**:
   - ローカルバインディングを使用する場合、**サーバー > サーバー・タイプ > WebSphere MQ サーバー** に移動する。
   - **新規** をクリックする。
   - **名前**、**キュー・マネージャー名** を設定する。
   - **MQ インストール** (MQ インストールへのパス) を指定する。
   - 保存し、サーバーを再始動する。

6. **JCA リソース・アダプターを構成 (MDB 用)**:
   - **リソース > リソース・アダプター > J2C 接続ファクトリー** に移動する。
   - 組み込みの MQ RA を使用する場合、それがデプロイされていることを確認する (WAS には `wmq.jmsra.rar` が含まれる)。
   - 最大接続数などのプロパティーを設定する (例: 負荷に基づいて 10-50)。

7. **構成をテスト**:
   - サンプル JMS アプリケーションをデプロイするか、WAS JMS サンプルを使用する。
   - エラーのログを確認する (例: ポート 1414 での接続拒否)。
   - MQ で確認する: MQ Explorer を使用してキューの深さとチャネルを監視する。

8. **セキュリティーと高度なセットアップ**:
   - SSL を有効化: WAS と MQ でキーストアを構成する (チャネルで `SSLCIPH` を使用)。
   - 認証を設定: MQ ユーザーグループまたは代替ユーザー ID を使用する。
   - クラスターの場合: ノード間で構成を同期する。

### トラブルシューティングのヒント
- **ClassNotFoundException**: MQ JAR がクラスパスにあることを確認する。
- **接続失敗**: ポート 1414 のファイアウォール、チャネルステータスを確認する (runmqsc で `DISPLAY CHSTATUS(*)`)。
- **バインディングモードの問題**: ネイティブ・ライブラリーと `mqm` グループ内のユーザーを確認する。
- 変更後は WAS を再始動する。

バージョン固有の詳細 (例: WAS 9.x と MQ 9.x) については、公式 IBM ドキュメントを参照してください。

[Using WebSphere Application Server with IBM MQ](https://www.ibm.com/docs/en/ibm-mq/9.2.x?topic=together-using-websphere-application-server-mq)  
[Configuring WebSphere Application Server for use with IBM MQ](https://help.hcl-software.com/commerce/9.0.0/integration/tasks/tcvconfigure_was_for_mq.html)  
[Creating a WebSphere MQ server definition](https://www.ibm.com/docs/SSAW57_8.5.5/com.ibm.websphere.nd.multiplatform.doc/ae/tjfp0004_.html)
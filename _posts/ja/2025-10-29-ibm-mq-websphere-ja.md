---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: WebSphereでのIBM MQ設定
translated: true
type: note
---

### IBM WebSphere Application Server でのメッセージキュー構成 (IBM MQ をプロバイダーとして使用)

IBM WebSphere Application Server (WAS) は、IBM MQ (旧称 WebSphere MQ) との Java Message Service (JMS) 統合を通じてメッセージキューイングをサポートします。構成は通常、**WebSphere Integrated Solutions Console** (管理インターフェース) を介して行われ、`https://your-server:9043/ibm/console` (デフォルトのセキュアポート。必要に応じて調整) でアクセスできます。このガイドは、従来のフルプロファイル WAS (例: バージョン 9.0+) に焦点を当てていますが、WebSphere Liberty でも手順はほぼ同様です (若干の調整が必要)。

#### 前提条件
- IBM MQ がインストールされ、実行中で、アクセス可能であること (例: キュー・マネージャーが起動している)。
- WAS サーバーが起動しており、コンソールへの管理者アクセス権があること。
- IBM MQ JMS クライアント・ライブラリー (例: `com.ibm.mq.allclient.jar`) を、まだ存在しない場合は WAS の共有ライブラリー (**環境 > 共有ライブラリー**) にダウンロードしてインストールすること。
- WebSphere MQ メッセージング・プロバイダーが構成されていること (**リソース > JMS > JMS プロバイダー**)。構成されていない場合は、ホスト、ポート (デフォルト 1414)、キュー・マネージャー名などの詳細を指定して作成します。

構成後、変更を保存し (上部の **保存** ボタン)、アプリケーション・サーバーを再起動して変更を有効にします。

#### ステップ 1: JMS キュー接続ファクトリーの作成
接続ファクトリーは、IBM MQ キュー・マネージャーへの接続を確立します。

1. WAS 管理コンソールにログインします。
2. ナビゲーション・ペインで、**リソース > JMS > キュー接続ファクトリー** を展開します。
3. ドロップダウンから適切な **スコープ** (例: セル、ノード、サーバー) を選択し、**適用** をクリックします。
4. **新規** をクリックします。
5. **WebSphere MQ メッセージング・プロバイダー** を選択し、**OK** をクリックします。
6. 次の画面で:
   - **名前**: 説明的な名前を入力します (例: `MyMQQueueConnectionFactory`)。
   - **JNDI 名**: JNDI バインディングを入力します (例: `jms/MyQueueConnectionFactory`)。
   - **次へ** をクリックします。
7. 接続の詳細を入力します:
   - **キュー・マネージャー**: IBM MQ キュー・マネージャーの名前 (例: `QM1`)。
   - **ホスト名**: IBM MQ サーバーのホスト名または IP アドレス。
   - **ポート**: リスナー・ポート (デフォルト: 1414)。
   - **トランスポート・タイプ**: CHANNEL (クライアント・モード用) または BINDINGS (組み込み用)。
   - **チャネル**: デフォルトのチャネル名 (例: `SYSTEM.DEF.SVRCONN`)。
   - **ユーザー ID** および **パスワード**: MQ 認証用の資格情報 (必要な場合)。
   - **次へ** をクリックします。
8. サマリーを確認し、**完了** をクリックします。
9. 新しいファクトリーを選択し、**追加プロパティー > 接続プール** (オプション) に移動し、**最大接続数** (例: 予想される負荷に基づく) などの設定を調整します。
10. **接続のテスト** をクリックして検証します。

#### ステップ 2: JMS キュー宛先の作成
これは、メッセージの送受信のための実際のキュー・エンドポイントを定義します。

1. ナビゲーション・ペインで、**リソース > JMS > キュー** を展開します。
2. 接続ファクトリーと一致する適切な **スコープ** を選択し、**適用** をクリックします。
3. **新規** をクリックします。
4. **WebSphere MQ メッセージング・プロバイダー** を選択し、**OK** をクリックします。
5. プロパティーを指定します:
   - **名前**: 説明的な名前 (例: `MyRequestQueue`)。
   - **JNDI 名**: JNDI バインディング (例: `jms/MyRequestQueue`)。
   - **ベース・キュー名**: IBM MQ 内の正確なキュー名 (例: `REQUEST.QUEUE`。MQ 内に存在するか作成されている必要があります)。
   - **ターゲット・クライアント**: JMS (JMS アプリケーション用) または MQ (ネイティブ MQ アプリケーション用)。
   - **ターゲット宛先モード**: 一度のみ (信頼性のためのデフォルト)。
   - **OK** をクリックします。
6. (オプション) **追加プロパティー** で、永続性、有効期限、または優先度の設定を構成します。
7. 構成を保存します。

#### ステップ 3: (オプション) メッセージ駆動型 Bean (MDB) のアクティベーション仕様の作成
メッセージを非同期的に消費するために MDB を使用する場合:

1. ナビゲーション・ペインで、**リソース > JMS > アクティベーション仕様** を展開します。
2. **スコープ** を選択し、**新規** をクリックします。
3. **WebSphere MQ メッセージング・プロバイダー** を選択し、**OK** をクリックします。
4. 以下を入力します:
   - **名前**: 例: `MyQueueActivationSpec`。
   - **JNDI 名**: 例: `jms/MyQueueActivation`。
   - **宛先タイプ**: キュー。
   - **宛先 JNDI 名**: キューの JNDI (例: `jms/MyRequestQueue`)。
   - **接続ファクトリー JNDI 名**: 接続ファクトリーの JNDI (例: `jms/MyQueueConnectionFactory`)。
   - メッセージ・セレクター (オプション): メッセージをフィルタリングするための JMS セレクター。
5. **追加プロパティー > メッセージ・リスナー・サービス > リスナー・ポート** で、必要に応じてポートを作成します:
   - **名前**: 例: `MyListenerPort`。
   - **接続ファクトリー JNDI**: 上記と同じ。
   - **宛先 JNDI**: 上記と同じ。
   - **コンポーネント**: MDB のデプロイメント記述子。
6. **OK** をクリックし、保存します。

#### ステップ 4: 検証とテスト
- **コンソールでのテスト**: ファクトリーと仕様で **接続のテスト** を使用します。
- **アプリケーションのデプロイ**: 単純な JMS クライアントまたは MDB アプリケーションを作成、デプロイし、IBM MQ ツール (例: MQ Explorer) を介してメッセージを送信/テストします。
- **モニタリング**: **モニタリングおよびチューニング > パフォーマンス・ビューアー** または **トラブルシューティング > ログ** で、JMS 関連のエラーを確認します。
- 一般的な問題:
  - 接続失敗: ファイアウォール、MQ チャネル状態 (`DISPLAY CHANNEL`)、資格情報を確認します。
  - JNDI ルックアップ・エラー: バインディングが正しく、アプリケーションが正しいスコープを使用していることを確認します。
  - 永続性: WAS と MQ 間の耐久性設定を一致させます。

コマンドラインの代替手段 (wsadmin スクリプト) については、IBM のドキュメントを参照してください。バージョンに基づいて調整します (例: WAS 9.0.5+ は JMS 2.0 をサポート)。

#### 参考文献
- [Configuring JMS resources in WebSphere Application Server](https://www.ibm.com/docs/en/ibm-mq/9.2.x?topic=resources-configuring-jms-in-websphere-application-server)
- [WebSphere MQ messaging provider queue settings](https://www.ibm.com/docs/en/was/8.5.5?topic=settings-websphere-mq-messaging-provider-queue)
- [Creating a WebSphere MQ messaging provider queue connection factory](https://help.hcl-software.com/commerce/7.0.0/com.ibm.commerce.integration.doc/tasks/tcvjmsqueuefactory.html)
- [Configure a JMS queue destination for WebSphere MQ](http://www.setgetweb.com/p/i5/portal/WAS60/Configure_JMS_queue_destinationfor_WebSphere_MQ.html)
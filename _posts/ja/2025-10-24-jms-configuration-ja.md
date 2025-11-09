---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: WebSphereにおけるJMSリソースの構成
translated: true
type: note
---

### 前提条件
- IBM WebSphere Application Server (WAS) 統合ソリューションコンソール（管理コンソール）への管理者アクセス権限があることを確認してください。
- サーバーが実行中であり、リソースのスコープ（例：セル、ノード、サーバー）を決定する必要があります。
- このガイドは、WAS に組み込まれている JMS プロバイダーである Default Messaging Provider（Service Integration Bus または SIBus を使用）に焦点を当てています。WebSphere MQ を使用する場合は、MQ プロバイダーの追加設定が必要です。
- メジャーな変更後にプロンプトが表示された場合は、サーバーを再起動してください。

### ステップ 1: サービス統合バスの作成
サービス統合バスは、JMS リソースのメッセージング基盤として機能します。

1. WebSphere 統合ソリューションコンソールにログインします。
2. **サービス統合 > バス** に移動します。
3. **新規** をクリックします。
4. 一意のバス名（例: `MyJMSBus`）を入力します。
5. 必要な場合を除き、**バス・セキュリティー** オプションをクリアします。
6. **次へ**、次に **完了** をクリックしてバスを作成します。

### ステップ 2: サーバーをバスメンバーとして追加
これにより、サーバーがバス上でメッセージングエンジンをホストできるようになります。

1. 作成したバス（例: `MyJMSBus`）を選択します。
2. **追加プロパティー** で、**バス・メンバー** をクリックします。
3. **追加** をクリックします。
4. **新しいバスメンバーの追加** ウィザードで：
   - バスメンバータイプとして **メッセージング・エンジン** を選択します。
   - リストからサーバー（例: `server1`）を選択します。
   - メッセージストアについては、非クラスター環境のデフォルトである **ファイルストア**、またはデータベース永続性の場合は **データストア** を選択し、必要に応じてプロパティを設定します。
5. **次へ**、次に **完了** をクリックします。
6. バスメンバーを有効化するために、WebSphere Application Server を再起動します。

### ステップ 3: JMS 接続ファクトリーの作成
JMS クライアントをプロバイダーに接続するには、接続ファクトリーが必要です。

1. **リソース > JMS > 接続ファクトリー** に移動します。
2. 適切なスコープ（例: `server1` のサーバースコープ）を選択し、**新規** をクリックします。
3. **Default messaging provider** を選択し、**OK** をクリックします。
4. 詳細を入力します：
   - **名前**: 例: `MyJMSConnectionFactory`。
   - **JNDI 名**: 例: `jms/MyConnectionFactory`。
   - **バス名**: ドロップダウンから `MyJMSBus` を選択します。
   - その他はデフォルト（例: プロバイダーエンドポイントは自動検出）のままにします。
5. **適用** をクリックし、次に **保存** をクリックしてマスター設定に保存します。

### ステップ 4: JMS キューの作成
これは、ポイントツーポイントメッセージングのためのキュー宛先を定義します。

1. **リソース > JMS > キュー** に移動します。
2. 適切なスコープを選択し、**新規** をクリックします。
3. **Default messaging provider** を選択し、**OK** をクリックします。
4. 詳細を入力します：
   - **名前**: 例: `MyJMSQueue`。
   - **JNDI 名**: 例: `jms/MyQueue`。
   - **バス名**: `MyJMSBus` を選択します。
   - **キュー名**: **サービス統合バス宛先の作成** を選択し、一意の識別子（例: `MyQueueDestination`）を入力して、先に作成したバスメンバーを選択します。
   - **ベース・キュー名**: 例: `$MyJMSBus:MyQueueDestination`（自動生成）。
5. 必要に応じて追加のプロパティ（例: 配信モード、有効期限）を設定します。
6. **適用** をクリックし、次に **保存** をクリックしてマスター設定に保存します。

### ステップ 5: (オプション) メッセージ駆動 Bean (MDB) のアクティベーション仕様の作成
キューからの消費に MDB を使用する場合は、アクティベーション仕様を設定します。

1. **リソース > JMS > アクティベーション仕様** に移動します。
2. 適切なスコープを選択し、**新規** をクリックします。
3. **Default messaging provider** を選択し、**OK** をクリックします。
4. 詳細を入力します：
   - **名前**: 例: `MyActivationSpec`。
   - **JNDI 名**: 例: `jms/activation/MyActivationSpec`。
   - **バス名**: `MyJMSBus` を選択します。
   - **宛先タイプ**: キュー。
   - **宛先**: キューの JNDI 名（例: `jms/MyQueue`）を入力します。
5. **適用** をクリックし、次に **保存** をクリックしてマスター設定に保存します。

### 検証とテスト
- 保存後、クラスター環境の場合はノードを同期します。
- サーバーを再起動します。
- JMS クライアントアプリケーションを使用して、JNDI 名を介したメッセージの送受信をテストします。
- **サービス統合 > バス > [対象のバス] > バス・メンバー > [対象のメンバー] > メッセージング・エンジン** で監視します。

高度な設定（例: セキュリティ、クラスタリング）については、IBM のドキュメントを参照してください。

[Configuring IBM WebSphere Application Server for Decision Server](https://docs.redhat.com/en/documentation/red_hat_decision_manager/7.4/html/installing_and_configuring_decision_server_on_ibm_websphere_application_server/was-configure-proc)  
[Managing messaging with the default messaging provider](https://www.ibm.com/docs/en/was/9.0.5?topic=resources-managing-messaging-default-messaging-provider)
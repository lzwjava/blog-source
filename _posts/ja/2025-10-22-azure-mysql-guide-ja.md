---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Azure Database for MySQL フレキシブル サーバー ガイド
translated: true
type: note
---

Azure Database for MySQL は、MySQL Community Edition を基盤とするフルマネージドなリレーショナル データベース サービスです。バックアップ、パッチ適用、監視などの定期的なタスクを処理するため、アプリケーションの開発に集中できます。推奨されるデプロイ オプションは **Flexible Server** であり、従来の Single Server（廃止予定）よりも多くの構成オプションと優れたパフォーマンスを提供します。

このガイドでは、サーバーの作成、接続、および基本的な操作の実行について説明します。簡単のため、Azure portal を使用した手順を基にしています。

## 前提条件
- アクティブな Azure サブスクリプション（必要に応じて [azure.microsoft.com](https://azure.microsoft.com/free/) で作成）。
- Azure portal (portal.azure.com) へのアクセス権。
- MySQL の概念に関する基本的な知識。
- ポート 3306（MySQL のデフォルト）でのアウトバウンド ネットワーク アクセス。
- 接続用に MySQL Workbench がインストールされていること（[mysql.com](https://dev.mysql.com/downloads/workbench/) からダウンロード）。

## ステップ 1: Azure Portal で Flexible Server を作成する
以下の手順に従ってサーバーをプロビジョニングします。

1. [Azure portal](https://portal.azure.com) にサインインします。

2. 上部の検索バーで「Azure Database for MySQL Flexible Servers」を検索し、選択します。

3. **作成** をクリックしてウィザードを開始します。

4. **基本** タブで以下を構成します：
   - **サブスクリプション**: ご利用のサブスクリプションを選択します。
   - **リソース グループ**: 新規作成（例: `myresourcegroup`）または既存のものを選択します。
   - **サーバー名**: 一意の名前（例: `mydemoserver`）、3～63 文字、小文字/数字/ハイフン。完全なホスト名は `<名前>.mysql.database.azure.com` となります。
   - **リージョン**: ユーザーに最も近い地域を選択します。
   - **MySQL バージョン**: 8.0（最新のメジャー バージョン）。
   - **ワークロードの種類**: 開発（テスト用。本番環境では Small/Medium を使用）。
   - **コンピューティング + ストレージ**: バースト可能層、Standard_B1ms (1 vCore)、10 GiB ストレージ、100 IOPS、7 日間のバックアップ。必要に応じて調整（例：移行時は IOPS を増加）。
   - **可用性ゾーン**: 設定なし（またはアプリのゾーンに合わせる）。
   - **高可用性**: 初期設定では無効（本番環境ではゾーン冗長を有効化）。
   - **認証**: MySQL と Microsoft Entra（柔軟性のため）。
   - **管理者ユーザー名**: 例: `mydemouser`（root/admin などは不可、最大 32 文字）。
   - **パスワード**: 強力なパスワード（8～128 文字、大文字/小文字/数字/記号の組み合わせ）。

5. **ネットworking** タブに切り替えます：
   - **接続方法**: パブリック アクセス（簡単のため。本番環境のセキュリティにはプライベート VNet を推奨）。
   - **ファイアウォール規則**: 現在のクライアント IP を追加（または Azure サービスを許可）。後から変更できません。

6. **確認および作成** で設定を確認し、**作成** をクリックします。デプロイには 5～10 分かかります。通知で進捗を確認します。

7. 完了したら、ダッシュボードにピン留めし、リソースの **概要** ページに移動します。デフォルトのデータベースには `information_schema`、`mysql` などが含まれます。

## ステップ 2: サーバーに接続する
GUI 接続には MySQL Workbench を使用します。（代替手段: Azure Data Studio、mysql CLI、または Azure Cloud Shell。）

1. ポータルでサーバーの **概要** に移動し、以下を確認します：
   - サーバー名（例: `mydemoserver.mysql.database.azure.com`）。
   - 管理者ユーザー名。
   - 必要に応じてパスワードをリセット。

2. MySQL Workbench を開きます。

3. **新しい接続** をクリック（または既存の接続を編集）。

4. **パラメーター** タブで：
   - **接続名**: 例: `Demo Connection`。
   - **接続方法**: 標準 (TCP/IP)。
   - **ホスト名**: 完全なサーバー名。
   - **ポート**: 3306。
   - **ユーザー名**: 管理者ユーザー名。
   - **パスワード**: 入力し、ボルトに保存。

5. **接続テスト** をクリックします。失敗した場合：
   - ポータルから詳細を確認します。
   - ファイアウォールがあなたの IP を許可していることを確認します。
   - TLS/SSL が強制されます（TLS 1.2）。必要に応じて [DigiCert](https://dl.cacerts.digicert.com/DigiCertGlobalRootCA.crt.pem) から CA 証明書をダウンロードし、Workbench でバインドします（SSL タブで：SSL 使用 > 必須 を選択し、CA ファイルを指定）。

6. **OK** をクリックして保存します。接続タイルをダブルクリックしてクエリ エディターを開きます。

## ステップ 3: データベースの作成と管理
接続後、ポータルまたはクライアントでデータベースを管理します。

### Azure Portal 経由：
1. サーバー ページで、左メニューから **データベース** を選択します。
2. **+ 追加** をクリック：
   - **データベース名**: 例: `testdb`。
   - **文字セット**: utf8（デフォルト）。
   - **照合順序**: utf8_general_ci。
3. **保存** をクリックします。

削除するには：データベースを選択し、**削除** をクリックします。

### MySQL Workbench（SQL クエリ）経由：
クエリ エディターで以下を実行します：

- データベースの作成: `CREATE DATABASE testdb CHARACTER SET utf8 COLLATE utf8_general_ci;`
- データベースの一覧表示: `SHOW DATABASES;`
- データベースの使用: `USE testdb;`
- テーブルの作成: `CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50));`
- データの挿入: `INSERT INTO users (name) VALUES ('Alice');`
- クエリ: `SELECT * FROM users;`

自動コミットでない場合は、`COMMIT;` で変更をコミットします。

## 基本的な使用のヒント
- **スケーリング**: **概要** > **コンピューティング + ストレージ** から、vCore/ストレージ/IOPS を調整（ほとんどの変更でダウンタイムなし）。
- **バックアップ**: 自動化された毎日のバックアップ。最大 35 日間のポイントインタイム リストアが可能（**バックアップ** 設定で構成）。
- **監視**: **メトリック** を使用して CPU/ストレージの分析情報を取得。アラートを設定。
- **セキュリティ**: 常に SSL を使用（強制）。本番環境では、高可用性、プライベート ネットワーキング、および Entra ID 認証を有効にします。
- **移行**: 小規模な DB には mysqldump を、大規模なものには DMS を使用。
- **コスト**: コンピューティング/ストレージに対して課金。小規模から開始し、スケールします。計算機は [azure.microsoft.com](https://azure.microsoft.com/pricing/calculator/) で利用可能。
- **クリーンアップ**: リソース グループを削除してサーバーを削除し、課金を回避します。

読み取りレプリカやサーバー パラメーターなどの高度な機能については、ポータルの左メニューを探索してください。

## 参考資料
- [クイックスタート: Azure Portal を使用した Flexible Server の作成](https://learn.microsoft.com/ja-jp/azure/mysql/flexible-server/quickstart-create-server-portal)
- [MySQL Workbench を使用した接続](https://learn.microsoft.com/ja-jp/azure/mysql/flexible-server/connect-workbench)
- [データベースの作成と管理](https://learn.microsoft.com/ja-jp/azure/mysql/flexible-server/how-to-create-manage-databases)
- [Azure Database for MySQL のドキュメント](https://learn.microsoft.com/ja-jp/azure/mysql/)
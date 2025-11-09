---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Amazon RDS for MySQLの使い方
translated: true
type: note
---

Amazon RDS (Relational Database Service) for MySQL は、クラウドでMySQLデータベースのセットアップ、運用、スケーリングを容易にするマネージドデータベースサービスです。バックアップ、パッチ適用、スケーリングなどの日常的なタスクを処理するため、アプリケーション開発に集中できます。このガイドでは、MySQL DBインスタンスの作成、接続、基本的な操作の基本を説明します。簡単のため、AWS Management Consoleを使用します。

**コストに関する注意:** AWS無料利用枠は新規アカウントに限定的な利用を提供しますが、それを超えるリソースには料金が発生します。予期しない請求を避けるため、リソースは使用後必ず削除してください。本番環境では、VPC、暗号化、最小権限のアクセスなどのセキュリティベストプラクティスに従ってください。

## 前提条件
- AWSアカウント（必要に応じて[aws.amazon.com](https://aws.amazon.com)でサインアップ）
- AWSコンソールとMySQLの基本的な知識
- 安全な接続テストのために、同じVPC（Virtual Private Cloud）内にEC2インスタンスを作成します。SSHアクセスのためにパブリックIPアドレス（例: [checkip.amazonaws.com](https://checkip.amazonaws.com)経由）を確認してください。
- お近くのAWSリージョン（例: US East (N. Virginia)）を選択してください。

**ベストプラクティス:** 信頼できるリソースのみにアクセスを制限するため、VPC内にプライベートDBインスタンスを使用してください。暗号化された接続のためSSL/TLSを有効にしてください。

## ステップ 1: 接続用EC2インスタンスの作成
これは、プライベートDBインスタンスに接続するためのシンプルなLinuxサーバーをセットアップします。

1. [AWS Management Console](https://console.aws.amazon.com)にサインインし、EC2コンソールを開きます。
2. リージョンを選択します。
3. **インスタンスを起動**をクリックします。
4. 設定:
   - **名前:** `ec2-database-connect`
   - **AMI:** Amazon Linux 2023 (無料利用枠対象)
   - **インスタンスタイプ:** t3.micro (無料利用枠対象)
   - **キーペア:** SSHアクセスのため、新規作成または既存のものを選択
   - **ネットワーク設定:** 編集 > SSHトラフィックを**マイIP**（または特定のIP、例: `192.0.2.1/32`）から許可。セキュリティのため`0.0.0.0/0`は避けてください。
   - ストレージとタグはデフォルトのままにします。
5. **インスタンスを起動**をクリックします。
6. インスタンスの詳細からインスタンスID、パブリックIPv4 DNS、キーペア名をメモします。
7. ステータスが**実行中**になるまで待ちます（2～5分）。

**セキュリティのヒント:** SSHアクセスを自身のIPのみに制限してください。キーペア（.pemファイル）は安全にダウンロードしてください。

## ステップ 2: MySQL DBインスタンスの作成
「簡単作成」を使用してデフォルト設定で素早くセットアップします。

1. [RDSコンソール](https://console.aws.amazon.com/rds/)を開きます。
2. EC2インスタンスと同じリージョンを選択します。
3. ナビゲーションペインで、**データベース** > **データベースの作成**をクリックします。
4. **簡単作成**を選択します。
5. **設定**で:
   - エンジンのタイプ: **MySQL**
   - テンプレート: **無料利用枠**（または有料アカウントでは**サンドボックス**）
   - DBインスタンス識別子: `database-test1`（または任意の名前）
   - マスターユーザー名: `admin`（またはカスタム）
   - マスターパスワード: 自動生成または強力なパスワードを設定（安全に記録）
6. （オプション）**接続**で、**EC2コンピュートリソースに接続**を選択し、EC2インスタンスを選択するとセットアップが容易になります。
7. **データベースの作成**をクリックします。
8. 資格情報ポップアップ（ユーザー名/パスワード）を確認し、保存してください。パスワードは後で取得できないためです。
9. ステータスが**利用可能**になるまで待ちます（最大10～20分）。**接続とセキュリティ**タブから**エンドポイント**（DNS名）とポート（デフォルト: 3306）をメモします。

**ベストプラクティス:** 本番環境では、「標準作成」を使用してVPC、バックアップ（自動化を有効化）、ストレージをカスタマイズしてください。削除保護とマルチAZを有効にして高可用性を実現してください。

## ステップ 3: DBインスタンスへの接続
EC2インスタンスからMySQLクライアントを使用して接続します。

1. EC2インスタンスにSSH接続:
   ```
   ssh -i /path/to/your-key-pair.pem ec2-user@your-ec2-public-dns
   ```
   （詳細を置き換えてください。例: `ssh -i ec2-database-connect-key-pair.pem ec2-user@ec2-12-345-678-90.compute-1.amazonaws.com`）

2. EC2インスタンス上でパッケージを更新:
   ```
   sudo dnf update -y
   ```

3. MySQLクライアントをインストール:
   ```
   sudo dnf install mariadb105 -y
   ```

4. DBに接続:
   ```
   mysql -h your-db-endpoint -P 3306 -u admin -p
   ```
   プロンプトが表示されたらマスターパスワードを入力します。

成功すると、MySQLプロンプト（`mysql>`）が表示されます。

**トラブルシューティング:** セキュリティグループがEC2インスタンスからのポート3306でのインバウンドトラフィックを許可していることを確認してください。外部接続の場合、DBをパブリックに設定する（非推奨）か、踏み台ホスト/VPNを使用してください。

**セキュリティのヒント:** 暗号化された接続には`--ssl-mode=REQUIRED`を使用: `mysql -h endpoint -P 3306 -u admin -p --ssl-mode=REQUIRED`

## ステップ 4: 基本的な使用法
接続後、SQLコマンドを実行できます。例:

- データベースの表示: `SHOW DATABASES;`
- サンプルデータベースの作成: `CREATE DATABASE myapp;`
- 使用するデータベースの選択: `USE myapp;`
- テーブルの作成:
  ```
  CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100)
  );
  ```
- データの挿入: `INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');`
- クエリ: `SELECT * FROM users;`
- 終了: `EXIT;`

アプリケーション（例: Python、Node.js）からは、エンドポイント、ポート、ユーザー名、パスワードを接続文字列として標準のMySQLドライバーを使用します。

**ベストプラクティス:** CloudWatchでパフォーマンスを監視し、自動バックアップを有効化し、必要に応じて垂直スケーリング（インスタンスサイズ）または水平スケーリング（読み取りレプリカ）を行ってください。

## クリーンアップ: リソースの削除
課金を停止するには:

1. **EC2インスタンスの削除:** EC2コンソール > インスタンスを選択 > **インスタンスの状態** > **終了** > 確認
2. **DBインスタンスの削除:** RDSコンソール > DBを選択 > **アクション** > **削除** > スナップショット作成のチェックを外す > 確認

AWS請求コンソールで実行中のリソースがないか確認してください。

移行、パフォーマンスチューニング、API/CLIの使用などのより高度なトピックについては、AWSドキュメントを参照してください。

## 参考資料
- [MySQL DBインスタンスの作成と接続](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.MySQL.html)
- [Amazon RDS for MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MySQL.html)
- [Amazon RDS の使用開始](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.html)
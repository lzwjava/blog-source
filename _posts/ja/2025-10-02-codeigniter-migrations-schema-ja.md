---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: CodeIgniterマイグレーションデータベーススキーマ管理
translated: true
type: note
---

### CodeIgniter Migrationsとは？

CodeIgniter（CI）Migrationsは、FlywayやLiquibaseのようなツールと同様に、データベーススキーマの変更をバージョン管理する機能です。PHPスクリプトでデータベースの変更（テーブルの作成、カラムの追加、データの修正など）を定義し、順次実行することで、環境間でスキーマを最新の状態に保ちます。これにより、手動SQLのミスを防ぎ、ロールバックもサポートします。

Migrationsの仕組み：
- マイグレーションファイルをディレクトリ（デフォルト：`application/migrations/`）に保存
- データベーステーブルで適用済みのマイグレーション「バージョン」を追跡
- 必要に応じてスクリプトを順方向（up）または逆方向（down）に実行

共有された設定ファイル（`migration.php`）は、マイグレーションの動作を制御します。PHP配列を使用してオプションを設定します。以下で主要な設定を例とともに説明します。

### 主要な設定項目

| 設定項目 | コード内の値 | 説明 | 動作詳細 |
|---------|---------------------|-------------|-------------|
| `migration_enabled` | `FALSE` | マイグレーションをグローバルに有効/無効にする。`FALSE`の場合、マイグレーションを実行できない（DBを変更するため、セキュリティ上の理由）。 | CIはマイグレーションコマンド実行前にこれをチェック。開発中は`TRUE`に設定し、本番環境では`FALSE`に戻す。例：有効時、コントローラーで`$this->migration->current()`を実行。 |
| `migration_type` | `'timestamp'` | ファイル命名スタイル：`'sequential'`（例：`001_add_blog.php`）または`'timestamp'`（例：`20121031104401_add_blog.php`）。バージョン管理にはタイムスタンプが推奨。 | ファイルは時系列順に読み込まれる。タイムスタンプは`YYYYMMDDHHIISS`形式（例：`20121031104401`は2012年10月31日10時44分01秒）。 |
| `migration_table` | `'migrations'` | 適用済みマイグレーションを追跡するDBテーブル名。必須。 | CIはこのテーブルが存在しない場合に作成。最新のマイグレーションバージョンを保存。このテーブルを削除または更新するとマイグレーション履歴がリセットされる。 |
| `migration_auto_latest` | `FALSE` | `TRUE`かつ`migration_enabled`が`TRUE`の場合、Migrationライブラリの読み込み時（例：ページ読み込み時）に最新バージョンまで自動実行。 | 開発環境でスキーマを自動同期するのに便利。本番環境では制御のため手動実行するよう`FALSE`に設定（より安全）。 |
| `migration_version` | `0` | マイグレーション対象のバージョン/番号。ファイル名の接頭辞に設定（例：`20121031104401`）。`0`はマイグレーション未適用を意味。 | `$this->migration->version(20121031104401)`を実行するとそのポイントまでアップ。対象を指定したロールバックに使用—負の数でダウングレード。 |
| `migration_path` | `APPPATH.'migrations/'` | マイグレーションファイルが保存されるディレクトリ。`APPPATH`は`application/`を指すCI定数。 | CIはこのフォルダをスキャンし、命名規則に合致するPHPファイルを探す。Webサーバーによる書き込み可能である必要。`BASEPATH.'custom/migrations/'`のようなカスタムパスも可能。 |

### マイグレーションの使用方法（ステップバイステップ）

1. **マイグレーションを有効化**：設定ファイルで一時的に`$config['migration_enabled'] = TRUE;`を設定。

2. **マイグレーションファイルを作成**：`application/migrations/`に`20121031104401_add_blog.php`のような名前のPHPファイルを追加。内部でCIのMigrationクラスを使用：
   ```php
   defined('BASEPATH') OR exit('No direct script access allowed');

   class Migration_Add_blog extends CI_Migration {
       public function up() {
           $this->dbforge->add_field('id');
           $this->dbforge->create_table('blogs');
       }

       public function down() {
           $this->dbforge->drop_table('blogs');
       }
   }
   ```
   - `up()`は変更を適用（例：テーブル作成）。
   - `down()`は変更を元に戻す（例：テーブル削除）。

3. **マイグレーションを実行**：
   - ライブラリを読み込み：`$this->load->library('migration');`
   - 最新まで：`$this->migration->current();`
   - 特定バージョンまで：`$this->migration->version('20121031104401');`
   - コマンドラインから（CLI有効時）：`php index.php migrate current`

4. **一般的なコマンド**：
   - `$this->migration->latest()`：`current()`のエイリアス。
   - `$this->migration->find_migratables()`：利用可能なファイルを一覧表示。
   エラーはCIのログファイルに記録されるか、例外をスロー。

5. **ベストプラクティス**：
   - マイグレーションは冪等性を保つ（再実行安全）。
   - 本番環境での自動マイグレートを有効にせず、誤ったスキーマ変更を防ぐため、まず開発環境でテスト。
   - DBがサポートする場合はトランザクションを使用し、アトミックな変更を。
   - 使用後は無効化：セキュリティのため`FALSE`に戻す。

問題が発生した場合（例：パスの権限）、CIのログまたは[codeigniter.com/user_guide/libraries/migration.html](https://codeigniter.com/user_guide/libraries/migration.html)のドキュメントを確認。より適切なアドバイスが必要な場合は、使用しているCIバージョンを指定してください！
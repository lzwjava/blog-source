---
audio: false
generated: true
lang: ja
layout: post
title: PostgreSQLデータベース管理ガイド
translated: true
type: note
---

以下は、強力なオープンソースリレーショナルデータベース管理システムであるPostgreSQLの使用手順です:

### 1. **インストール**
- **Windows**: [postgresql.org/download](https://www.postgresql.org/download/)からダウンロード（pgAdmin GUIを含む）
- **macOS**: Homebrewを使用（`brew install postgresql`）またはインストーラーをダウンロード
- **Linux** (Debian/Ubuntu):
  ```bash
  sudo apt update
  sudo apt install postgresql postgresql-contrib
  sudo systemctl start postgresql.service
  ```

### 2. **PostgreSQLへの接続**
- デフォルト管理者ユーザー: `postgres`
  ```bash
  sudo -u postgres psql  # Linux/macOS
  psql -U postgres       # Windows (PSQLコマンドライン経由)
  ```
- 特定のデータベースに接続:
  ```bash
  psql -U username -d dbname -h localhost -p 5432
  ```

### 3. **基本的なデータベース操作**
- **ユーザー/ロールの作成**:
  ```sql
  CREATE USER myuser WITH PASSWORD 'mypassword';
  ALTER ROLE myuser WITH CREATEDB;
  ```
- **データベースの作成**:
  ```sql
  CREATE DATABASE mydb;
  GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;
  ```
- **基本的なSQLコマンド**:
  ```sql
  -- テーブルの作成
  CREATE TABLE users (
      id SERIAL PRIMARY KEY,
      name VARCHAR(50),
      email VARCHAR(100) UNIQUE
  );

  -- データの挿入
  INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');

  -- データのクエリ
  SELECT * FROM users WHERE name LIKE 'A%';

  -- データの更新
  UPDATE users SET email = 'new@email.com' WHERE id = 1;

  -- データの削除
  DELETE FROM users WHERE id = 2;
  ```

### 4. **高度な機能**
- **結合**:
  ```sql
  SELECT orders.id, users.name 
  FROM orders
  INNER JOIN users ON orders.user_id = users.id;
  ```
- **JSONサポート**:
  ```sql
  CREATE TABLE products (
      id SERIAL PRIMARY KEY,
      details JSONB
  );
  ```
- **全文検索**:
  ```sql
  SELECT * FROM documents 
  WHERE to_tsvector('english', content) @@ to_tsquery('search & term');
  ```

### 5. **メンテナンス**
- **バックアップ**:
  ```bash
  pg_dump mydb > backup.sql
  pg_dumpall > all_databases.sql
  ```
- **復元**:
  ```bash
  psql -U username -d mydb -f backup.sql
  ```
- **Vacuum**（ストレージの再利用）:
  ```sql
  VACUUM ANALYZE;
  ```

### 6. **セキュリティ**
- 読み取り専用ユーザーの作成:
  ```sql
  CREATE USER readonly WITH PASSWORD 'readpass';
  GRANT CONNECT ON DATABASE mydb TO readonly;
  GRANT USAGE ON SCHEMA public TO readonly;
  GRANT SELECT ON ALL TABLES IN SCHEMA public TO readonly;
  ```

### 7. **便利なコマンド**
- データベース一覧: `\l`
- データベース切り替え: `\c dbname`
- テーブル一覧: `\dt`
- テーブル構造: `\d tablename`
- ユーザー表示: `\du`
- psql終了: `\q`

### 8. **GUIツール**
- **pgAdmin**: Windowsインストーラーに含まれる
- **DBeaver**: 人気のクロスプラットフォームGUI
- **TablePlus**: ネイティブな感覚のモダンなインターフェース

### 9. **学習リソース**
- 公式ドキュメント: [postgresql.org/docs](https://www.postgresql.org/docs/)
- インタラクティブチュートリアル: [postgresqltutorial.com](https://www.postgresqltutorial.com/)
- 練習問題: [pgexercises.com](https://pgexercises.com/)

**ヒント**: 本番環境に適用する前に、必ず開発環境で変更をテストしてください。重要な操作にはトランザクション（`BEGIN`/`COMMIT`）を使用してください。
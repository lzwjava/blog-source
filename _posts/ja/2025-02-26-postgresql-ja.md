---
audio: false
lang: ja
layout: post
title: 'PostgreSQL: データベース管理ガイド'
translated: true
---

PostgreSQLを使用するためのステップバイステップガイドです。PostgreSQLは、強力なオープンソースのリレーショナルデータベース管理システムです。

### 1. **インストール**
- **Windows**: [postgresql.org/download](https://www.postgresql.org/download/)からダウンロード（pgAdmin GUIを含む）
- **macOS**: Homebrewを使用 (`brew install postgresql`) またはインストーラをダウンロード
- **Linux** (Debian/Ubuntu):
  ```bash
  sudo apt update
  sudo apt install postgresql postgresql-contrib
  sudo systemctl start postgresql.service
  ```

### 2. **PostgreSQLに接続**
- デフォルトの管理ユーザー: `postgres`
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
- **ジョイン**:
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
- **フルテキスト検索**:
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
- **Vacuum** (ストレージの回収):
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
- データベースのリスト表示: `\l`
- データベースの切替: `\c dbname`
- テーブルのリスト表示: `\dt`
- テーブルの説明: `\d tablename`
- ユーザーの表示: `\du`
- psqlの終了: `\q`

### 8. **GUIツール**
- **pgAdmin**: Windowsインストーラーに含まれる
- **DBeaver**: 人気のあるクロスプラットフォームGUI
- **TablePlus**: モダンなインターフェースでネイティブな感覚

### 9. **学習リソース**
- 公式ドキュメント: [postgresql.org/docs](https://www.postgresql.org/docs/)
- インタラクティブチュートリアル: [postgresqltutorial.com](https://www.postgresqltutorial.com/)
- 練習: [pgexercises.com](https://pgexercises.com/)

**ヒント**: 変更をテストする前に、開発環境でテストしてください。重要な操作にはトランザクション (`BEGIN`/`COMMIT`) を使用してください。
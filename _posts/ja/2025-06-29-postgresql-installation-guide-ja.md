---
audio: false
generated: true
lang: ja
layout: post
title: PostgreSQLをインストールしてpsycopg2を修正
translated: true
type: note
---

発生しているエラーは、`psycopg2` パッケージがソースからビルドするために PostgreSQL の `pg_config` 実行ファイルを必要としているが、システム上に見つからないことを示しています。これは、必要な依存関係を提供するために、macOS システムに PostgreSQL をインストールする必要があることを意味します。以下に、macOS に PostgreSQL をインストールし、問題を解決する手順を示します。

### macOS への PostgreSQL インストール手順

#### 1. **Homebrew を使用した PostgreSQL のインストール (推奨)**
Homebrew は、macOS で PostgreSQL をインストールおよび管理する最も簡単な方法です。

1. **Homebrew のインストール (未インストールの場合)**:
   - ターミナルを開き、以下を実行:
     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```
   - 画面の指示に従って Homebrew のインストールを完了させます。

2. **PostgreSQL のインストール**:
   - ターミナルで、以下を実行:
     ```bash
     brew install postgresql
     ```
   - このコマンドは、`psycopg2` に必要な `pg_config` 実行ファイルを含む、PostgreSQL とその依存関係をインストールします。

3. **PostgreSQL の起動**:
   - PostgreSQL サービスを起動するには、以下を実行:
     ```bash
     brew services start postgresql
     ```
   - または、単一セッションで手動起動する場合:
     ```bash
     pg_ctl -D /opt/homebrew/var/postgres start
     ```

4. **インストールの確認**:
   - PostgreSQL がインストールされ、実行されているか確認:
     ```bash
     psql --version
     ```
   - PostgreSQL のバージョン (例: `psql (PostgreSQL) 17.0`) が表示されるはずです。
   - PostgreSQL シェルにログインして確認することもできます:
     ```bash
     psql -U $(whoami)
     ```

#### 2. **PostgreSQL インストール後の `psycopg2` インストール**
PostgreSQL のインストール後、`psycopg2` のインストールを再試行してください。`pg_config` 実行ファイルが PATH で利用可能になっているはずです。

1. **`psycopg2` のインストール**:
   - 以下を実行:
     ```bash
     pip install psycopg2
     ```
   - 要件ファイルを使用している場合:
     ```bash
     pip install -r scripts/requirements/requirements.local.txt
     ```

2. **代替案: `psycopg2-binary` のインストール (より簡単なオプション)**:
   - (PostgreSQL の依存関係を必要とする) ソースからの `psycopg2` ビルドを避けたい場合は、プリコンパイルされた `psycopg2-binary` パッケージをインストールできます:
     ```bash
     pip install psycopg2-binary
     ```
   - 注意: `psycopg2-binary` は、潜在的な互換性の問題から本番環境では推奨されませんが、開発やテストには問題ありません。

#### 3. **オプション: PATH への `pg_config` の追加 (必要な場合)**
PostgreSQL をインストールした後も `pg_config` 実行ファイルが見つからない場合は、手動で PATH に追加する必要があるかもしれません。

1. `pg_config` の場所を特定:
   - Homebrew は通常、PostgreSQL を `/opt/homebrew/bin` (Apple Silicon の場合) または `/usr/local/bin` (Intel Mac の場合) にインストールします。
   - 場所を確認:
     ```bash
     find /opt/homebrew -name pg_config
     ```
     または
     ```bash
     find /usr/local -name pg_config
     ```

2. PATH への追加:
   - `pg_config` が見つかった場合 (例: `/opt/homebrew/bin` 内)、シェル設定ファイル (例: `~/.zshrc` または `~/.bash_profile`) を編集して PATH に追加:
     ```bash
     echo 'export PATH="/opt/homebrew/bin:$PATH"' >> ~/.zshrc
     ```
   - 変更を適用:
     ```bash
     source ~/.zshrc
     ```

3. `pg_config` の確認:
   - 以下を実行:
     ```bash
     pg_config --version
     ```
   - バージョンが返されれば、PATH は正しく設定されています。

#### 4. **トラブルシューティング**
- **エラーが解消しない場合**: `pip install psycopg2` がまだ失敗する場合は、必要なビルドツールが揃っていることを確認してください:
  - Xcode Command Line Tools のインストール:
    ```bash
    xcode-select --install
    ```
  - 必要に応じて `libpq` (PostgreSQL クライアントライブラリ) を明示的にインストール:
    ```bash
    brew install libpq
    ```

- **Python バージョンの互換性**: 使用している Python バージョン (あなたの場合は 3.13) が `psycopg2` と互換性があることを確認してください。問題が解決しない場合は、少し古い Python バージョン (例: 3.11 または 3.12) を使用した仮想環境の使用を検討してください:
  ```bash
  python3.11 -m venv venv
  source venv/bin/activate
  pip install psycopg2
  ```

- **Homebrew の確認**: Homebrew が最新であることを確認:
  ```bash
  brew update
  brew upgrade
  ```

#### 5. **代替インストール方法 (オプション)**
Homebrew を使用したくない場合は、以下の方法で PostgreSQL をインストールできます:
- **Postgres.app**:
  - [postgresapp.com](https://postgresapp.com/) からダウンロード。
  - セットアップ手順に従って PostgreSQL をインストールし起動。
  - 上記で説明したように `bin` ディレクトリ (例: `/Applications/Postgres.app/Contents/Versions/latest/bin`) を PATH に追加。
- **公式 PostgreSQL インストーラー**:
  - [postgresql.org](https://www.postgresql.org/download/macosx/) から macOS インストーラーをダウンロード。
  - インストールウィザードに従ってインストール。

#### 6. **プロジェクトの再試行**
PostgreSQL と `psycopg2` (または `psycopg2-binary`) をインストールした後、プロジェクトの実行または要件の再インストールを再試行してください:
```bash
pip install -r scripts/requirements/requirements.local.txt
```

### 追加の注意点
- **エラーが発生した理由**: `psycopg2` パッケージは、ソースからビルドするために PostgreSQL の開発ライブラリ (特に `libpq`) を必要とします。Homebrew 経由で PostgreSQL をインストールすると、これらのライブラリが提供されます。
- **本番環境に関する考慮事項**: 本番環境では、`psycopg2-binary` ではなく `psycopg2` を使用し、PostgreSQL のバージョンがターゲット環境と一致していることを確認してください。
- **ドキュメント**: 詳細については、`psycopg2` インストールガイド [psycopg.org/docs/install.html](https://www.psycopg.org/docs/install.html) を参照してください。

さらに問題が発生した場合は、具体的なエラーメッセージを共有していただければ、さらにトラブルシューティングをお手伝いします！
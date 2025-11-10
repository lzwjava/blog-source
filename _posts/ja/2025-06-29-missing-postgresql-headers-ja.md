---
audio: false
generated: true
lang: ja
layout: post
title: psycopg2用のlibpq-fe.hが見つかりません
translated: true
type: note
---

Pythonパッケージ `psycopg2` のインストールを試みた際、wheelのビルドが失敗するエラーに遭遇しました。エラーメッセージの重要な部分は以下の通りです：

```
In file included from psycopg/adapter_asis.c:28:
./psycopg/psycopg.h:36:10: fatal error: libpq-fe.h: No such file or directory
   36 | #include <libpq-fe.h>
      |          ^~~~~~~~~~~~
compilation terminated.
```

このエラーは、PostgreSQLクライアントライブラリのヘッダーファイル `libpq-fe.h` がシステム上に存在しないために発生します。`psycopg2` パッケージは、PythonをPostgreSQLデータベースに接続するためのインターフェースを提供するため、ソースからビルドする際にこのファイルを必要とします。以下で、この問題が発生する理由と、それを解決するためのステップバイステップの方法を説明します。

---

### エラーが発生する理由
`psycopg2` パッケージはPython用のPostgreSQLアダプタであり、`pip` を使用してインストールする際、C拡張機能のコンパイルを試みます。これらの拡張機能は、PostgreSQLクライアントライブラリ、特に `libpq-fe.h` のような開発用ヘッダーに依存しています。エラーメッセージはこれを確認しています：

```
It appears you are missing some prerequisite to build the package from source.
```

あなたのシステム（`x86_64-linux-gnu-gcc` の使用から判断してDebianベースのLinuxディストリビューションと思われます）には、必要なPostgreSQL開発ファイルが不足しています。これらがないと、コンパイルが失敗し、`psycopg2` のwheelをビルドできません。

エラーはまた、2つの選択肢を示唆しています：
1. PyPI経由で事前ビルドされたバイナリパッケージ `psycopg2-binary` をインストールする。
2. 不足している前提条件をインストールし、`psycopg2` をソースからビルドする。

あなたのプロジェクトでは要件ファイルに `psycopg2`（`psycopg2-binary` ではない）が指定されており、互換性やカスタマイズのためにソースからのビルドが必要な場合があるため、ここではビルドプロセスを修正することに焦点を当てます。ただし、完全を期すためにバイナリオプションについても後述します。

---

### エラーの修正方法
これを解決するには、`libpq-fe.h` やその他の必要なファイルを提供するPostgreSQLクライアント開発パッケージをインストールする必要があります。その方法は以下の通りです：

#### ステップ 1: システムの特定
ビルド出力に `x86_64-linux-gnu-gcc` が含まれていることから、おそらくUbuntuなどのDebianベースのシステムを使用していると推測されます。解決策はこれに合わせて説明しますが、他のディストリビューション用の代替案も後述します。

#### ステップ 2: PostgreSQL開発パッケージのインストール
Debianベースのシステム（例：Ubuntu）では、パッケージ `libpq-dev` にPostgreSQLクライアントライブラリのヘッダー（`libpq-fe.h` を含む）が含まれています。以下のコマンドでインストールします：

```bash
sudo apt-get update
sudo apt-get install libpq-dev
```

- **`sudo apt-get update`**: パッケージリストを最新の状態にします。
- **`sudo apt-get install libpq-dev`**: PostgreSQLクライアントライブラリの開発ファイルをインストールします。

このパッケージは `libpq-fe.h` を標準的な場所（通常は `/usr/include/postgresql`）に配置します。これはビルドプロセスが検索するパス（インクルードパス `-I/usr/include/postgresql` としてビルド出力に表示されています）と一致します。

#### ステップ 3: インストールの再試行
`libpq-dev` のインストール後、要件のインストールを再試行します：

```bash
pip install -r scripts/requirements/requirements.local.txt
```

これで、不足していた `libpq-fe.h` ファイルが利用可能になるため、`psycopg2` のwheelのビルドが成功するはずです。

---

### 修正の確認
インストールがまだ失敗する場合は、PostgreSQLヘッダーが正しくインストールされていることを確認してください：
- `pg_config --includedir` を実行して、ヘッダーが配置されている場所（例：`/usr/include/postgresql`）を確認します。
- これがビルドコマンドのインクルードパス（`-I/usr/include/postgresql`）と一致していることを確認します。

あなたのビルド出力には `-DPG_VERSION_NUM=140018` と表示されており、PostgreSQL 14を対象としていることがわかります。`libpq-dev` パッケージはバージョンに依存せず、PostgreSQL 14のヘッダーで動作するはずです。

---

### 代替案: バイナリパッケージの使用
特定の最適化や互換性のために `psycopg2` をソースからビルドする必要がない場合は、事前ビルドされた `psycopg2-binary` を代わりにインストールできます：

```bash
pip install psycopg2-binary
```

これをプロジェクトで使用するには、`scripts/requirements/requirements.local.txt` を更新して `psycopg2` を `psycopg2-binary` に置き換えてください。ただし、`psycopg2-binary` には制限がある可能性がある（例：特定のPostgreSQLバージョンとの互換性問題）ため、プロジェクトで必要とされる場合はソースからのビルドが推奨されます。

---

### 他のディストリビューションの場合
Debianベースのシステムでない場合は、同等のパッケージをインストールしてください：
- **Red Hat/CentOS/Fedora**: `sudo yum install postgresql-devel` または `sudo dnf install postgresql-devel`
- **Arch Linux**: `sudo pacman -S postgresql-libs`
- **macOS (Homebrew使用)**: `brew install libpq`

その後、`pip install` コマンドを再試行してください。

---

### まとめ
このエラーは、PostgreSQLクライアント開発ファイルの一部である `libpq-fe.h` が不足しているために発生します。Debianベースのシステムでは、`sudo apt-get install libpq-dev` で `libpq-dev` をインストールすることで問題が解決するはずです。その後、`pip install` コマンドを再実行すると、`psycopg2` は正常にビルドされます。より迅速な修正を希望し、ソースからのコンパイルが必要ない場合は、代わりに `psycopg2-binary` を使用してください。
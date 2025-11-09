---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: UbuntuへのIBM Db2インストール
translated: true
type: note
---

### IBM Db2 12.1.2 を Ubuntu 22.04 または 24.04 に `ibm_db2_v12.1.2_linuxx64_server_dec.tar.gz` からインストール

IBM Db2 バージョン 12.1.2 (Fix Pack 2) は、お使いのシステムがハードウェアおよびソフトウェアの前提条件を満たしていれば、Ubuntu 22.04 (Jammy) や 24.04 (Noble) などの最近の Ubuntu バージョンでサポートされています。このインストールでは、tar.gz ファイルからグラフィカルまたはサイレントインストーラーを使用します。要件はエディションによって異なる可能性があるため、最新の詳細については、IBM Knowledge Center や Db2 ダウンロードページなどの公式 IBM ドキュメントを確認することをお勧めします (ここでは Server Edition を使用します)。

**開始前の重要な注意点:**
- **システム要件**:
  - 64 ビット x86_64 アーキテクチャ (Intel/AMD)。
  - 少なくとも 4 GB RAM (8 GB 推奨) および 2 GB のスワップ領域。
  - ベースインストール用に 10 GB の空きディスク容量 (データ用にはさらに必要)。
  - Root または sudo アクセス。
  - カーネルバージョン: Ubuntu 22.04/24.04 は動作するはずですが、カーネルが少なくとも 3.10 であることを確認してください (`uname -r` で確認)。
  - ファイアウォール: 一時的に無効化するか、ポートを開放してください (Db2 デフォルト: TCP/IP 用 50000)。
- **Ubuntu での潜在的な問題**:
  - Db2 は主に RHEL/SUSE でテストされていますが、Debian パッケージを介して Ubuntu がサポートされています。ライブラリの依存関係を解決する必要があるかもしれません。
  - Ubuntu 24.04 を使用している場合、これは非常に新しいバージョンです。完全な認定が遅れる可能性があるため、まず VM でテストしてください。
  - これは Server Edition をインストールします。他のエディション (例: Express-C) の場合は、適切な tar.gz をダウンロードしてください。
- **バックアップ**: 続行する前にシステムをバックアップしてください。
- ファイルは公式 IBM Passport Advantage または Db2 ダウンロードサイトからダウンロードしてください (IBM ID が必要です)。

#### ステップ 1: 前提条件のインストール
システムを更新し、必要なライブラリをインストールします。Db2 には非同期 I/O、PAM、およびその他のランタイムライブラリが必要です。

```bash
sudo apt update
sudo apt upgrade -y

# 必須パッケージをインストール (Ubuntu/Debian での Db2 用共通)
sudo apt install -y libaio1 libpam0g:i386 libncurses5 libstdc++6:i386 \
    unixodbc unixodbc-dev libxml2 libxslt1.1 wget curl

# Ubuntu 24.04 の場合、以下も必要かもしれません:
sudo apt install -y libc6:i386 libgcc-s1:i386

# glibc の互換性を確認 (Db2 12.1 は glibc 2.17+ が必要)
ldd --version  # Ubuntu 22.04/24.04 では glibc 2.35+ が表示されるはず
```

32 ビットライブラリ (例: Java コンポーネント用) が見つからない場合は、マルチアーキテクチャを有効にします:
```bash
sudo dpkg --add-architecture i386
sudo apt update
sudo apt install -y libc6:i386 libncurses5:i386 libstdc++6:i386
```

#### ステップ 2: インストールファイルの準備
1. 展開用の一時ディレクトリを作成 (例: `/tmp/db2_install`):
   ```bash
   sudo mkdir -p /tmp/db2_install
   cd /tmp/db2_install
   ```

2. tar.gz ファイルをこのディレクトリにコピー (例: `~/Downloads` にダウンロード済みと仮定):
   ```bash
   cp ~/Downloads/ibm_db2_v12.1.2_linuxx64_server_dec.tar.gz .
   ```

3. アーカイブを展開:
   ```bash
   tar -xzf ibm_db2_v12.1.2_linuxx64_server_dec.tar.gz
   ```
   - これにより、インストーラーファイル (例: `db2setup`) を含む `db2` や `sqllib` のようなディレクトリが作成されます。

4. 展開されたディレクトリに移動:
   ```bash
   cd db2  # またはトップレベルディレクトリに応じて変更 - `ls` で確認
   ```

#### ステップ 3: インストーラーの実行
Db2 はグラフィカルインストーラー (`db2setup`) またはサイレントインストール用のレスポンスファイルを提供します。root/sudo として実行します。

**オプション A: グラフィカルインストーラー (初回セットアップ推奨)**
1. ディスプレイがあることを確認 (GUI なしのサーバーの場合、SSH で X 転送を使用: `ssh -X user@host`)。
2. インストーラーを実行:
   ```bash
   sudo ./db2setup
   ```
   - ウィザードに従います:
     - ライセンスに同意。
     - Server Edition の場合は「Typical」インストールを選択。
     - インストールパスを選択 (デフォルト: `/opt/ibm/db2/V12.1` - `/opt/ibm` が存在し書き込み可能であることを確認。必要に応じて `sudo mkdir -p /opt/ibm` で作成)。
     - Db2 インスタンスを作成 (例: "db2inst1") - これによりデータベース管理者ユーザーがセットアップされます。
     - 認証を設定 (例: ローカルまたは LDAP)。
     - 必要に応じて SQL Procedural Language などの機能を有効化。
   - インストーラーはコンパイルを行い、インスタンスをセットアップします。

**オプション B: サイレントインストール (非対話式)**
スクリプト化を希望する場合:
1. ドライラン中にレスポンスファイルを生成:
   ```bash
   sudo ./db2setup -g  # カレントディレクトリに `db2setup.rsp` を生成
   ```
   `db2setup.rsp` を編集 (例: `LIC_AGREEMENT=ACCEPT`, `INSTALL_TYPE=TYPICAL`, `CREATE_DB2_INSTANCE=YES` などを設定)。

2. サイレントインストールを実行:
   ```bash
   sudo ./db2setup -u db2setup.rsp
   ```

- インストールには 10-30 分かかります。エラーは `/tmp/db2setup.log` で確認してください。

#### ステップ 4: インストール後のセットアップ
1. **インストールの確認**:
   - インスタンス所有者 (例: インストール中に作成された `db2inst1`) としてログイン:
     ```bash
     su - db2inst1
     ```
   - Db2 バージョンを確認:
     ```bash
     db2level
     ```
   - インスタンスを開始:
     ```bash
     db2start
     ```
   - 接続をテスト:
     ```bash
     db2 connect to sample  # サンプル DB が存在しない場合は作成
     db2 "select * from sysibm.sysdummy1"
     db2 disconnect all
     db2stop  # 終了時
     ```

2. **データベースの作成 (インストール中に行われていない場合)**:
   ```bash
   su - db2inst1
   db2sampl  # オプション: サンプル DB を作成
   # またはカスタム DB を作成:
   db2 "create database MYDB"
   db2 connect to MYDB
   ```

3. **環境設定**:
   - インスタンスユーザーの PATH に Db2 を追加 (`~/.bashrc` に追加):
     ```bash
     export PATH=/opt/ibm/db2/V12.1/bin:$PATH
     export DB2INSTANCE=db2inst1
     ```
   - リロード: `source ~/.bashrc`.

4. **リモートアクセスの有効化 (オプション)**:
   - サービスを更新:
     ```bash
     su - db2inst1
     db2 update dbm cfg using SVCENAME db2i  # または使用するポート
     db2set DB2COMM=TCPIP
     db2start
     ```
   - `/etc/services` (root として) を編集して追加:
     ```
     db2i          50000/tcp
     ```
   - インスタンスを再起動。

5. **ファイアウォール設定**:
   ```bash
   sudo ufw allow 50000/tcp  # Db2 デフォルトポート用
   sudo ufw reload
   ```

#### ステップ 5: アップデートの適用 (推奨)
- 必要に応じて最新の Fix Pack をダウンロードして適用 (12.1.2 は FP2; FP3+ を確認):
  - `db2iupdt` ツールまたは IBM のアップデートインストーラーを使用。
- ログを監視: `/tmp/db2` または `/opt/ibm/db2/V12.1/instance/db2inst1/sqllib/db2dump`.

#### 一般的な問題のトラブルシューティング
- **"No suitable Java runtime"**: OpenJDK をインストール: `sudo apt install openjdk-11-jre-headless`.
- **ライブラリエラー (例: libaio.so)**: `libaio1` がインストールされていることを確認し、`sudo ldconfig` を実行。
- **Permission Denied**: インストーラーを root として実行。`/opt/ibm` の所有権を確認: `sudo chown -R db2inst1:db2iadm1 /opt/ibm/db2`.
- **Glibc 非互換**: Ubuntu 22.04/24.04 では可能性は低いですが、問題が発生した場合はコンテナ (Docker) インストールを検討。
- **サイレントインストールの失敗**: `db2setup.log` で手がかりを確認。
- **Ubuntu 24.04 固有**: ライブラリの依存関係で失敗する場合、PPA を追加するか不足しているライブラリをコンパイルする必要があるかもしれません。まず 22.04 でテストしてください。
- エラー? IBM のサポートフォーラムを検索するか、インスタンスユーザーとして `db2diag` を実行。

特定のエラーが発生した場合は、詳細を提供してより具体的なヘルプを受けてください。本番環境での使用には、IBM の認定環境またはコンサルティングサポートの利用を検討してください。成功しました! これで Db2 インスタンスはデータベースの作成と使用の準備が整いました。
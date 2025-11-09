---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: UbuntuへのOracle 12cインストール
translated: true
type: note
---

### Oracle Database 12c Release 1（12.1.0.2 with patch 12.1.2?）をUbuntu 22.04 x86_64でTarballからインストール

ファイル `v12.1.2_linuxx64_server_dec.tar.gz` は、Oracle Database 12c Release 1（おそらくバージョン12.1.0.2にパッチ12.1.2がバンドルされたサーバーエディションで、"dec" はdeconfiguredを意味する可能性があります）のtarballです。これは古いバージョンのOracle Database（〜2013-2014年リリース）であり、Oracleは**Ubuntuを公式にサポートしていません**。Ubuntu 22.04（glibc 2.35などのモダンなライブラリを使用）へのインストールは可能ですが、ライブラリのリンクやカーネルパラメータなど、互換性の問題に対する回避策が必要になる場合があります。依存関係に関するエラーが発生する可能性があるため、まずはVMでテストしてください。

**警告:**
- Oracle 12cは延長サポートのサポート終了（2022年以降）となっているため、テスト/本番環境での使用は自己責任で行ってください。本番環境では19cや23aiなどの新しいバージョンの使用を検討してください。
- root/sudoアクセスが必要です。
- 最小ハードウェア要件: 2 GB RAM（推奨8 GB）、2 CPUコア、ソフトウェア用に10 GBの空きディスク容量（データベース用にはさらに多く）。
- 作業前にシステムをバックアップしてください。
- このtarballがOracleの公式ソースからのものでない場合、マルウェアを避けるために整合性（チェックサムなど）を確認してください。

#### ステップ 1: システムの準備
1. **Ubuntuの更新**:
   ```
   sudo apt update && sudo apt upgrade -y
   ```

2. **必要な依存関係のインストール**:
   Oracle 12cには特定のライブラリが必要です。aptでインストールします:
   ```
   sudo apt install -y oracle-java8-installer bc binutils libaio1 libaio-dev libelf-dev libnuma-dev libstdc++6 unixodbc unixodbc-dev
   ```
   - `oracle-java8-installer` が利用できない場合（古いリポジトリにある）、OracleのJava PPAを追加するか、手動でJDK 8をダウンロードしてください:
     ```
     sudo add-apt-repository ppa:webupd8team/java -y
     sudo apt update
     sudo apt install oracle-java8-installer -y
     ```
     インストール中にライセンスに同意してください。JAVA_HOMEを設定します:
     ```
     echo 'export JAVA_HOME=/usr/lib/jvm/java-8-oracle' >> ~/.bashrc
     source ~/.bashrc
     ```

3. **Oracleユーザーとグループの作成**:
   rootまたはsudoで実行:
   ```
   sudo groupadd -g 54321 oinstall
   sudo groupadd -g 54322 dba
   sudo useradd -u 54321 -g oinstall -G dba -s /bin/bash oracle
   sudo passwd oracle  # oracleユーザーのパスワードを設定
   ```

4. **カーネルパラメータの設定**:
   `/etc/sysctl.conf` を編集:
   ```
   sudo nano /etc/sysctl.conf
   ```
   これらの行を追加（RAM/ディスクに応じて調整。これらは最小値）:
   ```
   fs.file-max = 6815744
   kernel.sem = 250 32000 100 128
   kernel.shmmni = 4096
   kernel.shmall = 1073741824
   kernel.shmmax = 4398046511104
   kernel.panic_on_oops = 1
   net.core.rmem_default = 262144
   net.core.rmem_max = 4194304
   net.core.wmem_default = 262144
   net.core.wmem_max = 1048576
   fs.aio-max-nr = 1048576
   vm.swappiness = 0
   ```
   変更を適用:
   ```
   sudo sysctl -p
   ```

5. **Oracleユーザーのシェル制限の設定**:
   `/etc/security/limits.conf` を編集:
   ```
   sudo nano /etc/security/limits.conf
   ```
   追加:
   ```
   oracle soft nproc 2047
   oracle hard nproc 16384
   oracle soft nofile 1024
   oracle hard nofile 65536
   oracle soft stack 10240
   oracle hard stack 32768
   ```
   `/etc/pam.d/login` を編集し、追加:
   ```
   sudo nano /etc/pam.d/login
   ```
   追加: `session required pam_limits.so`

6. **ディレクトリの作成**:
   ```
   sudo mkdir -p /u01/app/oracle/product/12.1.0/dbhome_1
   sudo mkdir -p /u01/app/oraInventory
   sudo chown -R oracle:oinstall /u01
   sudo chmod -R 775 /u01
   ```

7. **スワップスペース**（RAM < 8 GBの場合、スワップを追加）:
   2 GB RAMの場合、2 GBのスワップファイルを作成:
   ```
   sudo fallocate -l 2G /swapfile
   sudo chmod 600 /swapfile
   sudo mkswap /swapfile
   sudo swapon /swapfile
   echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
   ```

8. **ファイアウォール/SElinuxの無効化**（有効な場合）:
   ```
   sudo ufw disable  # またはポート1521、5500を必要に応じて設定
   sudo apt remove apparmor -y  # AppArmorが干渉する場合
   ```

#### ステップ 2: Tarballの展開
oracleユーザーに切り替え:
```
su - oracle
cd ~/Downloads  # またはファイルがある場所
```
展開（これによりデータベースホームディレクトリ構造が作成されます）:
```
tar -xzf v12.1.2_linuxx64_server_dec.tar.gz -C /u01/app/oracle/product/12.1.0/
```
- これにより `/u01/app/oracle/product/12.1.0/dbhome_1` が作成され、`runInstaller` のようなファイルが含まれているはずです。
- tarballが異なる構造に展開される場合は、パスを適宜調整してください（例: `database/` ディレクトリ）。

#### ステップ 3: インストーラーの実行
引き続きoracleユーザーとして:
```
cd /u01/app/oracle/product/12.1.0/dbhome_1
./runInstaller
```
- GUIインストーラーが起動します（SSHの場合はX11転送が必要。`ssh -X` を使用するかX11を有効化）。
- **インストールオプション**:
  - 「Create and configure a database software only」または「Single instance database installation」（サーバーエディション用）を選択。
  - ORACLE_HOME: `/u01/app/oracle/product/12.1.0/dbhome_1`
  - Inventory: `/u01/app/oraInventory`
  - ソフトウェアのみ（データベース作成なし）の場合、「Install database software only」を選択。
- ウィザードに従う: 可能な場合はデフォルトを受け入れ、SYS/SYSTEMのパスワードを設定。
- 前提条件チェックの警告は最初は無視してください。必要に応じてインストール後に修正。

GUIが失敗する場合（例: DISPLAYエラー）、サイレントインストールを実行:
```
./runInstaller -silent -responseFile /path/to/responsefile.rsp
```
レスポンスファイル（抽出されたディレクトリ内のサンプル、例: `db_install.rsp`）を準備する必要があります。設定（ORACLE_HOMEなど）を編集して実行します。

#### ステップ 4: インストール後
1. **root.shの実行**（rootとして）:
   ```
   sudo /u01/app/oraInventory/orainstRoot.sh
   sudo /u01/app/oracle/product/12.1.0/dbhome_1/root.sh
   ```

2. **環境変数の設定**（oracleユーザー用、`~/.bash_profile` に追加）:
   ```
   export ORACLE_HOME=/u01/app/oracle/product/12.1.0/dbhome_1
   export PATH=$ORACLE_HOME/bin:$PATH
   export ORACLE_SID=orcl  # あなたのSIDに変更
   export LD_LIBRARY_PATH=$ORACLE_HOME/lib:/lib:/usr/lib
   export CLASSPATH=$ORACLE_HOME/jlib:$ORACLE_HOME/rdbms/jlib
   ```
   ```
   source ~/.bash_profile
   ```

3. **データベースの作成**（インストール中に行われなかった場合）:
   ```
   dbca  # Database Configuration Assistant (GUI/サイレント)
   ```
   または手動作成のためにSQL*Plusを使用。

4. **サービスの開始/停止**:
   ```
   sqlplus / as sysdba
   STARTUP;  # または shutdown
   ```
   systemdに自動起動用に追加（`/etc/systemd/system/oracle.service` を作成し、execを `dbstart` に設定）。

#### Ubuntu 22.04での一般的な問題のトラブルシューティング
- **Glibc/依存関係エラー**: Oracle 12cはglibc <=2.17を想定。Ubuntu 22.04は2.35—`ldd` で確認、または互換性ライブラリをインストール:
  ```
  sudo apt install libc6:i386 libncurses5:i386 libstdc++6:i386
  ```
  リンカーエラーの場合、`LD_PRELOAD` を設定するか、Oracle LinuxのDockerコンテナを使用。
- **Java/Displayの問題**: JDK 8が設定されていることを確認（`java -version` が1.8を表示）。ヘッドレスの場合: `export DISPLAY=:0`。
- **メモリ不足**: ulimitまたはRAMを増加。必要に応じて `runInstaller` パラメータを編集。
- **パッチ12.1.2**: バンドルされていない場合、My Oracle Supportからダウンロードし、インストール後に `opatch` で適用。
- **ログ**: エラーについては `/u01/app/oraInventory/logs/installActions*.log` を確認。
- **互換性修正**: 一部のユーザーはライブラリをシンボリックリンク（例: `sudo ln -s /lib/x86_64-linux-gnu/libpthread.so.0 /u01/app/oracle/product/12.1.0/dbhome_1/lib/libpthread_nonshared.a`—エラーごとに調査）。

#### 検証
- `sqlplus / as sysdba` を実行し、`SELECT * FROM v$version;` を実行。
- リスナー: `lsnrctl start`。

特定のエラーが発生した場合は、詳細なヘルプのためにログ出力を提供してください。公式（ただしRHEL中心）のドキュメントについては、Oracleの12cインストールガイドを参照してください。これが別の製品（データベース以外）用の場合、tarballの内容を明確にしてください！
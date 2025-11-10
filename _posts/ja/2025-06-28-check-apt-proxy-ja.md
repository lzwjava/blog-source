---
audio: false
generated: true
lang: ja
layout: post
title: UbuntuでのAPTプロキシ設定の確認
translated: true
type: note
---

Ubuntuで`apt`がプロキシを使用しているか確認するには、以下の手順に従ってください：

1. **APT設定ファイルの確認**:
   - `/etc/apt/apt.conf`または`/etc/apt/apt.conf.d/`にあるAPT設定ファイルを開きます（このディレクトリ内の`70debconf`や`proxy.conf`などのファイルにプロキシ設定が含まれている可能性があります）。
   - 以下のコマンドを使用します：
     ```bash
     sudo cat /etc/apt/apt.conf
     ```
     または
     ```bash
     sudo grep -r Proxy /etc/apt/apt.conf.d/
     ```
   - 以下のような行を探します：
     ```
     Acquire::http::Proxy "http://proxy-server:port";
     Acquire::https::Proxy "https://proxy-server:port";
     Acquire::ftp::Proxy "ftp://proxy-server:port";
     ```
     これらの行が存在する場合、`apt`はプロキシを使用するように設定されています。

2. **環境変数の確認**:
   - `apt`は`http_proxy`、`https_proxy`、`ftp_proxy`などの環境変数で定義されたプロキシ設定を使用する可能性があります。
   - 以下を実行します：
     ```bash
     env | grep -i proxy
     ```
   - `http_proxy=http://proxy-server:port`のような出力が表示された場合、`apt`はこれらの設定を使用している可能性があります。

3. **システム全体のプロキシ設定の確認**:
   - デスクトップ環境（例：GNOME）を使用している場合は、システムのプロキシ設定を確認します：
     - *設定 > ネットワーク > プロキシ*または類似の場所に移動します（使用しているデスクトップ環境によって異なります）。
     - 特定のAPTプロキシが設定されていない場合、これらの設定が`apt`に適用される可能性があります。

4. **コマンドでのAPTテスト**:
   - `apt`コマンドを実行して動作を観察します：
     ```bash
     sudo apt update
     ```
   - `apt`がプロキシ経由で接続する場合、遅延、特定のエラーメッセージ、またはプロキシ関連のログが表示される可能性があります。さらにデバッグするには、以下を使用します：
     ```bash
     sudo apt -o Debug::pkgProblemResolver=yes update
     ```
     これにより詳細な出力が表示され、プロキシの使用状況が示される可能性があります。

5. **`/etc/environment`でのプロキシ確認**:
   - 一部のシステムでは`/etc/environment`でプロキシが定義されています。以下で確認します：
     ```bash
     cat /etc/environment
     ```
   - 以下のような行を探します：
     ```
     http_proxy="http://proxy-server:port"
     ```

これらのいずれもプロキシ設定を表示しない場合、`apt`はおそらくプロキシを使用していません。リアルタイムで確認するには、`tcpdump`や`wireshark`などのツールを使用してネットワークトラフィックを監視し、`apt`接続がプロキシサーバーを経由するかどうかを確認できます。

特定の出力の分析やプロキシの設定にヘルプが必要な場合は、お知らせください！
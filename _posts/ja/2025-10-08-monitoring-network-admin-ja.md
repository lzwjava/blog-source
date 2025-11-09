---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: 管理者権限によるネットワーク活動の監視
translated: true
type: note
---

### HTTPリクエストとTCP接続の管理者権限による監視

Linux/Unix系システム（Ubuntu、CentOSなど）でroot/管理者権限を持っていることを前提に、トラブルシューティング、セキュリティ監査、またはペンテストのために倫理的にネットワーク活動を監視する方法を説明します。**重要：自分が所有するシステム、または明示的な許可を得たシステムでのみ実行してください。無許可での監視は違法です。** GUIを必要としない軽量なコマンドラインツールに焦点を当てます。

#### 1. **すべてのTCP接続の監視**
   組み込みツールの`ss`（`netstat`の現代的代替）や`tcpdump`をリアルタイムキャプチャに使用します。これらはアクティブな接続、ポート、プロセスを表示します。

   - **すべての現在のTCP接続を一覧表示（静的ビュー）：**
     ```
     sudo ss -tunap
     ```
     - `-t`: TCPのみ。
     - `-u`: 必要に応じてUDP（ただし今回はTCPを指定）。
     - `-n`: 数値ポート（DNS解決なし）。
     - `-a`: すべての状態（established、listeningなど）。
     - `-p`: 所有プロセスを表示。
     出力例：
     ```
     tcp   ESTAB  0      0      192.168.1.10:80     10.0.0.5:54321    users:(("nginx",pid=1234,fd=5))
     ```
     リスニングソケットのみ：`sudo ss -tlnp`。

   - **watchによるリアルタイム監視：**
     ```
     watch -n 1 'sudo ss -tunap'
     ```
     1秒ごとに更新。

   - **ライブTCPトラフィックのキャプチャ（パケットレベル）：**
     `tcpdump`がインストールされていない場合：`sudo apt update && sudo apt install tcpdump`（Debian/Ubuntu）または`sudo yum install tcpdump`（RHEL/CentOS）。
     ```
     sudo tcpdump -i any tcp -n -v
     ```
     - `-i any`: すべてのインターフェース。
     - `-n`: 名前解決なし。
     - `-v`: 詳細表示。
     HTTP/HTTPSをフィルタするには`port 80 or port 443`を追加：`sudo tcpdump -i any tcp port 80 or tcp port 443 -n -v -A`（`-A`でASCIIペイロード、HTTPヘッダーを表示）。

     後で分析するためにファイルに保存：`sudo tcpdump -i any tcp -w capture.pcap`。

#### 2. **HTTPリクエストログの監視**
   HTTPログは使用しているWebサーバー（Apache、Nginxなど）に依存します。Webサーバーが実行されていない場合は、ネットワークキャプチャ（上記）を使用してHTTPトラフィックを検査します。サーバー固有のログの場合：

   - **Apache（httpd）：**
     ログは通常`/var/log/apache2/access.log`（Ubuntu）または`/var/log/httpd/access_log`（CentOS）にあります。
     ```
     sudo tail -f /var/log/apache2/access.log
     ```
     - リアルタイムでリクエストを表示：IP、タイムスタンプ、メソッド（GET/POST）、URL、ステータスコード。
     例：`192.168.1.100 - - [08/Oct/2025:10:00:00 +0000] "GET /index.html HTTP/1.1" 200 1234`。

     すべてのログ：`sudo grep "GET\|POST" /var/log/apache2/access.log | less`。

   - **Nginx：**
     ログは`/var/log/nginx/access.log`にあります。
     ```
     sudo tail -f /var/log/nginx/access.log
     ```
     Apacheと同様の形式。

   - **Webサーバーがない場合（一般的なHTTPスニッフィング）：**
     上記の`tcpdump`を`-A`オプションで使用してHTTPペイロードをダンプするか、正規表現マッチングのために`ngrep`をインストール：
     ```
     sudo apt install ngrep  # 必要に応じてインストール
     sudo ngrep -d any 'GET|POST|HTTP' -O http_capture.pcap
     ```
     これによりHTTPメソッドがフィルタされログに記録されます。

   - **高度な設定：完全なロギングのための透過プロキシをセットアップ。**
     Squidプロキシをインストール：`sudo apt install squid`。
     `/etc/squid/squid.conf`を設定してすべてのHTTPをログに記録（`access_log /var/log/squid/access.log squid`を追加）。
     iptablesでトラフィックをリダイレクト：`sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 3128`。
     その後Squidログをtail：`sudo tail -f /var/log/squid/access.log`。

#### 「ハッキング」のためのヒント（倫理的ペンテスト）
- **ツールの組み合わせ：** `tcpdump`を`grep`にパイプして特定のパターンを検索、例：`sudo tcpdump -i any tcp port 80 -A | grep "User-Agent"`。
- **Wiresharkで可視化：** GUI分析のためにWiresharkをインストール（`sudo apt install wireshark`）、rootとして実行し、`.pcap`ファイルを開く。
- **セキュリティ強化：** 監視後、センシティブなログをクリア：`sudo truncate -s 0 /var/log/access.log`。
- **クロスプラットフォーム注意：** Windows（管理者権限）では`netstat -anob`をTCPに、イベントビューアをログに使用。macOSでは`netstat -an`と`tcpdump`。

このセットアップで外部ツールなしで包括的な可視性が得られます。まずはVMでテストしてください。

[Linux ssコマンドマニュアルページ](https://man7.org/linux/man-pages/man8/ss.8.html)  
[Tcpdumpチュートリアル](https://www.tcpdump.org/manpages/tcpdump.1.html)  
[Apacheアクセスログフォーマット](https://httpd.apache.org/docs/2.4/logs.html)
---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: ルーターネットワークトラフィックの監視
translated: true
type: note
---

### 360 Wi-Fi 6 ルーター T7 での HTTP リクエストと TCP 接続の監視

360 T7 はカスタマイズされた Linux ベースのファームウェアを実行しており（初期状態では完全な OpenWrt ではありません）、標準設定ではフル Linux シェルと比較して監視機能が制限されています。管理者権限（Web UI 経由）を使用すると、基本的なログにアクセスできます。リアルタイムの HTTP リクエストログや TCP 接続追跡のような、より深い「ハッキング」を行うには、倫理的に最適なアプローチは、OpenWrt（公式サポートあり）をフラッシュし、SSH を有効にして、標準的な Linux ツールを使用することです。**警告: カスタムファームウェアのフラッシュは保証を無効にし、文鎮化するリスクがあります—最初にバックアップを取り、ガイドを注意深く実行してください。自身が所有するデバイスのみで実行してください。**

#### 1. **標準ファームウェアでの管理者権限の取得**
   - ルーターの Wi-Fi またはイーサネット経由で接続します。
   - ブラウザを開き、`http://ihome.360.cn` または `http://192.168.0.1`（デフォルト IP）にアクセスします。
   - ログイン：デフォルトユーザー名 `admin`、パスワードはルーターのラベルに記載（多くの場合 `admin` または `360XXXXXX` のような固有の文字列—底面のステッカーを確認）。
   - ログイン後、**システム > ログ** または **セキュリティ > ログ** に移動して、基本的なシステムログとトラフィックログを表示します。これにより、ファイアウォールブロック、接続、一部の HTTP アクティビティ（例：ブロックされたサイトや侵入）が表示されますが、完全な HTTP リクエストの詳細は表示されません。

   **Web UI 経由の基本的な監視:**
   - **システムログ**: 最近のイベント（TCP 接続試行やエラーを含む）を表示します。ログをエクスポート（復号化にはラベルのパスワードが必要な場合あり）。
   - **トラフィック統計**: **ステータス > ネットワーク** または **詳細設定 > トラフィックモニター** で、デバイス/IP ごとの帯域幅使用状況を確認できますが、詳細な HTTP/TCP 情報はありません。
   - 制限事項: リアルタイムの HTTP ペイロード検査は不可。ログは高レベルであり、認証なしではエクスポートできません。

#### 2. **高度な監視: シェルアクセスのための OpenWrt フラッシュ**
   360 T7 (MT7981B チップセット) は OpenWrt 23.05+ スナップショットでサポートされています。フラッシュすると、SSH 経由で完全な root シェルアクセスが可能になり、`tcpdump` などのツールをパケットキャプチャに、`logread` をログ表示に使用できます。

   **OpenWrt フラッシュ手順（概要；公式ガイドを使用）:**
   1. OpenWrt ダウンロードからファクトリーイメージをダウンロード（"Qihoo 360T7 sysupgrade.bin" またはファクトリーイメージを検索）。
   2. 標準ファームウェアのバックアップ: Web UI で、**システム > バックアップ** に移動し、設定/ファームウェアをダウンロード。
   3. Web UI 経由でアップロード: **システム > ファームウェアアップグレード**、.bin ファイルを選択し、適用（ルーターは OpenWrt で再起動）。
   4. フラッシュ後: `http://192.168.1.1`（LuCI インターフェース）で Web UI にアクセス、ユーザー名 `root`、初期パスワードなし—SSH または UI 経由で直ちに設定。
   5. SSH 有効化: デフォルトでポート 22 で有効。PC から接続: `ssh root@192.168.1.1`（Windows では PuTTY を使用）。

   **リスク軽減**: 問題が発生した場合は、TFTP リカバリ（起動中にリセットボタンを押し続ける）またはシリアルコンソール（UART アダプタ必要）を使用。

#### 3. **OpenWrt での監視（SSH シェル経由）**
   root として SSH 接続後、ルーターは最小限の Linux システムのように動作します。必要に応じて `opkg update && opkg install tcpdump` 経由でパッケージをインストール（内蔵ストレージは 128MB のため、軽量に保つ）。

   - **すべての現在の TCP 接続を一覧表示（静的ビュー）:**
     ```
     ss -tunap
     ```
     - 確立/待機中の TCP ソケット、ポート、プロセスを表示（例: `tcp ESTAB 0 0 192.168.1.1:80 192.168.1.100:54321 users:(("uhttpd",pid=1234,fd=3))`）。
     - リアルタイム表示: `watch -n 1 'ss -tunap'`。

   - **リアルタイム TCP トラフィックキャプチャ:**
     必要に応じてインストール: `opkg update && opkg install tcpdump`。
     ```
     tcpdump -i any tcp -n -v
     ```
     - `-i any`: すべてのインターフェース（LAN 用 br-lan、WAN 用 eth0.2）。
     - HTTP フィルタ: `tcpdump -i any tcp port 80 -n -v -A`（`-A` は HTTP ヘッダー/リクエストの ASCII ペイロードを表示）。
     - ファイルに保存: `tcpdump -i any tcp -w /tmp/capture.pcap`（SCP 経由でダウンロード: `scp root@192.168.1.1:/tmp/capture.pcap .`）。
     - HTTPS（ポート 443）の場合、ペイロードは暗号化されていることに注意—オフライン分析には Wireshark を使用。

   - **HTTP リクエストログの監視:**
     - システムログ（uhttpd 使用時の Web サーバーを含む）: `logread | grep uhttpd` またはリアルタイム表示 `logread -f`。
     - 詳細な HTTP ログを有効化: `/etc/config/uhttpd`（Web サーバー設定）を編集し、`option log_file '/var/log/uhttpd.log'` を追加、その後 `/etc/init.d/uhttpd restart`。表示: `tail -f /var/log/uhttpd.log`（GET/POST リクエスト、IP、URL を表示）。
     - フルネットワーク HTTP の場合: 上記の `tcpdump` を使用、または `ngrep` をインストール（`opkg install ngrep`）: `ngrep -d any 'GET|POST|HTTP' -O /tmp/http.pcap`。

   - **ファイアウォール/接続ログ:**
     - ルールでログを有効化: `uci set firewall.@rule[0].log='1'; uci commit; /etc/init.d/firewall restart`。
     - 表示: `logread | grep fw`（ドロップ/許可された TCP 接続を表示）。

#### 倫理的「ハッキング」のためのヒント
- **セキュリティ**: 設定後、root パスワードを変更（`passwd`）、`/etc/ssh/sshd_config` でパスワード認証を無効にしてキーのみとし、ファイアウォールで SSH を LAN のみに制限。
- **パフォーマンス**: T7 は 256MB RAM—OOM を防ぐため、長期間の重いキャプチャは避ける。
- **標準ファームウェアに戻す**: 360 のサイトから公式ファームウェアをダウンロードし、OpenWrt の sysupgrade 経由でアップロード（必要に応じて `--force` 付き）。
- 安全な環境でテスト。GUI 分析の場合、.pcap を SCP で PC に転送し、Wireshark で開く。

これにより包括的な可視性が得られます。標準 UI で基本的な要件が満たされる場合は、フラッシュを避けてそこに留まってください。

[OpenWrt Techdata: Qihoo 360T7](https://openwrt.org/toh/hwdata/qihoohardware/qihoohardware_360t7)  
[360 T7U マニュアル（ログセクション）](https://ipc-pr-cdn.jia.360.cn/ipc-pr/luyouqiT7U.pdf)  
[OpenWrt ログガイド](https://openwrt.org/docs/guide-user/base-system/log.essentials)  
[360 フォーラム: ログエクスポート](https://bbs.360.cn/forum-7007-1.html)
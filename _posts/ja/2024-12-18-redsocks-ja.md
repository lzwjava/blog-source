---
audio: false
generated: false
image: false
lang: ja
layout: post
title: Redsocksの活用
translated: true
type: post
---

もちろんです！Macコンピュータを使用してShadowsocksプロキシを設定し、OpenWRTルーターを構成して、接続されたすべてのデバイスのトラフィックをこのプロキシ経由でルーティングする手順をご案内します。このセットアップには、以下の主要なステップが含まれます：

1. macOSにShadowsocksクライアントを設定する（Shadowsocks-NGまたはClashを使用）
2. macOSを外部プロキシ接続を許可するように設定する
3. Macに静的IPを割り当てる
4. OpenWRTにRedsocksをインストールして設定する
5. OpenWRTのトラフィックをmacOSのプロキシ経由にリダイレクトする
6. プロキシ設定をテストする

各ステップについて詳しく見ていきましょう。

---

## 1. macOSでのShadowsocksクライアントの設定

Shadowsocksクライアントとして、Shadowsocks-NGまたはClashのどちらかを使用できます。以下にそれぞれの設定手順を記載します。

### オプションA: Shadowsocks-NGを使用する

Shadowsocks-NGは、macOS向けの人気で使いやすいShadowsocksクライアントです。

#### ステップ1: Shadowsocks-NGをダウンロードしてインストールする

1. Shadowsocks-NGをダウンロードする：
   - [Shadowsocks-NG GitHub Releasesページ](https://github.com/shadowsocks/ShadowsocksX-NG/releases)にアクセスします。
   - 最新の`.dmg`ファイルをダウンロードします。

2. アプリケーションをインストールする：
   - ダウンロードした `.dmg` ファイルを開きます。
   - ShadowsocksX-NG アプリを「アプリケーション」フォルダにドラッグします。

3. Shadowsocks-NGを起動する：
   - アプリケーションフォルダからShadowsocksX-NGを開きます。
   - システム環境設定でアプリに必要な権限を付与する必要があるかもしれません。

#### ステップ2: Shadowsocks-NGの設定

1. 設定を開く：
   - メニューバーのShadowsocksX-NGアイコンをクリックします。
   - 「ShadowsocksX-NGを開く」＞「設定」を選択します。

2. 新しいサーバーを追加:
   - 「Servers」タブに移動します。
   - 「+」ボタンをクリックして新しいサーバーを追加します。

3. Shadowsocks URLをインポートする:
   - Shadowsocks URLをコピー:
     ```
     ss://[ENCRYPTED_PASSWORD]@xxx.xxx.xxx.xxx:xxxxx/?outline=1
     ```
   - インポート方法:
     - 「インポート」をクリック。
     - Shadowsocks URLを貼り付ける。
     - Shadowsocks-NGが自動的にサーバーの詳細を解析し、入力してくれるはずです。

4. ローカルプロキシを設定する：
   - 「SOCKS5プロキシを有効にする」にチェックが入っていることを確認します。
   - ローカルポート（デフォルトは通常 `1080`）をメモしておきます。

5. 保存して有効化:
   - 「OK」をクリックしてサーバーを保存します。
   - 「Shadowsocksを有効にする」スイッチをONに切り替えます。

### オプションB: Clashを使用する

Clashは、Shadowsocksを含む複数のプロトコルをサポートする多機能なプロキシクライアントです。

#### ステップ1: Clashをダウンロードしてインストールする

1. Clash for macOS をダウンロード:
   - [Clash GitHub Releases ページ](https://github.com/Dreamacro/clash/releases) にアクセスします。
   - 最新の Clash for macOS バイナリをダウンロードします。

2. アプリケーションをインストールする：
   - ダウンロードしたClashアプリケーションを「アプリケーション」フォルダに移動します。

3. Clashを起動する：
   - アプリケーションフォルダからClashを開きます。
   - システム環境設定で必要な権限を付与する必要があるかもしれません。

#### ステップ2: Clashの設定

1. 設定ファイルにアクセスする:
   - ClashはYAML設定ファイルを使用します。TextEditやVisual Studio Codeなどのテキストエディタを使って、作成または編集できます。

2. Shadowsocksサーバーを追加する:
   - 以下の内容で設定ファイル（例: `config.yaml`）を作成します:

```yaml
port: 7890
socks-port: 7891
allow-lan: true
mode: Rule
log-level: info
```

```yaml
proxies:
  - name: "MyShadowsocks"
    type: ss
    server: xxx.xxx.xxx.xxx
    port: xxxxx
    cipher: chacha20-ietf-poly1305
    password: "xxxxxx"
```

```yaml
proxy-groups:
  - name: "Default"
    type: select
    proxies:
      - "MyShadowsocks"
      - "DIRECT"
```

```yaml
rules:
  - MATCH,Default
```

     メモ:
     - `port` と `socks-port` は、ClashがリッスンするHTTPおよびSOCKS5プロキシポートを定義します。
     - `allow-lan: true` は、LANデバイスがプロキシを使用できるようにします。
     - `proxies` セクションには、Shadowsocksサーバーの詳細が含まれています。
     - `proxy-groups` と `rules` は、トラフィックのルーティング方法を決定します。

3. 設定ファイルを使用してClashを開始:
   - Clashを起動し、`config.yaml`ファイルを使用するように設定します。
   - Clashを起動する際に、設定ファイルのパスを指定する必要があるかもしれません。

4. プロキシが動作していることを確認する:
   - Clashがアクティブで、Shadowsocksサーバーに接続されていることを確認します。
   - メニューバーのアイコンでステータスを確認します。

---

## 2. macOSを外部プロキシ接続を許可するように設定する

デフォルトでは、Shadowsocksクライアントはプロキシを`localhost`（`127.0.0.1`）にバインドするため、Macのみがこのプロキシを使用できます。OpenWRTルーターがこのプロキシを使用できるようにするには、プロキシをMacのLAN IPにバインドする必要があります。

### Shadowsocks-NGの場合:

1. 設定を開く:
   - メニューバーのShadowsocksX-NGアイコンをクリックします。
   - 「ShadowsocksX-NGを開く」＞「設定」を選択します。

2. 詳細設定タブに移動：
   - 「詳細設定」タブに移動します。

3. リスニングアドレスの設定:
   - 「Listen Address」を`127.0.0.1`から`0.0.0.0`に変更し、任意のインターフェースからの接続を許可します。
   - または、MacのLAN IP（例: `192.168.1.xxx`）を指定します。

4. Shadowsocks-NGを保存して再起動:
   - 「OK」をクリックして変更を保存します。
   - 新しい設定を適用するために、Shadowsocks-NGクライアントを再起動します。

### Clashの場合:

1. 設定ファイルを編集する:
   - `config.yaml` 内で `allow-lan: true` 設定が有効になっていることを確認してください。

2. すべてのインターフェースにバインドする:
   - 設定で `allow-lan: true` を設定すると、通常、プロキシはLANを含むすべての利用可能なインターフェースにバインドされます。

3. Clashを再起動：
   - 変更を適用するためにClashクライアントを再起動します。

---

## 3. Macに静的IPを割り当てる

OpenWRTルーターとMac間の接続を安定させるために、ローカルネットワーク内でMacに静的IPを割り当ててください。

### macOSで静的IPを割り当てる手順:

1. システム環境設定を開く：
   - Appleメニューをクリックし、「システム環境設定」を選択します。

2. ネットワーク設定に移動します：
   - 「ネットワーク」をクリックします。

3. アクティブな接続を選択:
   - Macがルーターに接続されている方法に応じて、左側のサイドバーから「Wi-Fi」または「Ethernet」を選択します。

4. IPv4設定を構成する：
   - 「詳細...」をクリックします。
   - 「TCP/IP」タブに移動します。
   - 「IPv4を構成」を「DHCPを使用」から「手動」に変更します。

5. 静的IPアドレスの設定:
   - IPアドレス: ルーターのDHCP範囲外のIPを選び、競合を防ぎます（例: `192.168.1.xxx`）。
   - サブネットマスク: 通常は `255.255.255.0`。
   - ルーター: ルーターのIPアドレス（例: `192.168.1.1`）。
   - DNSサーバー: ルーターのIPを使用するか、`8.8.8.8`のような他のDNSサービスを利用できます。

6. 設定を適用する：
   - 「OK」をクリックし、次に「適用」をクリックして変更を保存します。

---

## 4. OpenWRTへのRedsocksのインストールと設定

Redsocksは、ネットワークトラフィックをSOCKS5プロキシ経由でルーティングできる透過型のSOCKSリダイレクターです。ここでは、Redsocksを使用して、Mac上で動作しているShadowsocksプロキシを介してOpenWRTのトラフィックをリダイレクトします。

### ステップ1: Redsocksのインストール

1. パッケージリストの更新:

```bash
ssh root@<router_ip>
opkg update
```

2. Redsocksをインストール:

```bash
opkg install redsocks
```

*もしOpenWRTのリポジトリにRedsocksが利用できない場合、手動でコンパイルするか、代替パッケージを使用する必要があるかもしれません。*

### ステップ2: Redsocksの設定

1. Redsocks設定ファイルの作成または編集:

```bash
vi /etc/redsocks.conf
```

2. 以下の設定を追加:

```conf
   base {
       log_debug = on;
       log_info = on;
       log = "file:/var/log/redsocks.log";
       daemon = on;
       redirector = iptables;
   }
```

```plaintext
redsocks {
       local_ip = 0.0.0.0;
       local_port = 12345;  # Redsocksがリッスンするローカルポート
       ip = xxx.xxx.xxx.xxx;  # Macの静的IPアドレス
       port = xxxxx;          # Shadowsocks-NGのローカルSOCKS5プロキシポート
       type = socks5;
       login = "";           # プロキシが認証を必要とする場合
       password = "";
   }
```

   メモ:
   - `local_port`: Redsocksがiptablesのリダイレクトからの接続を待ち受けるポート。
   - `ip` と `port`: MacのShadowsocks SOCKS5プロキシを指す (`xxx.xxx.xxx.xxx:xxxxx` は前の手順に基づく)。
   - `type`: Shadowsocksが提供するSOCKS5プロキシであるため、`socks5` に設定。

3. 保存して終了:
   - `ESC`を押し、`:wq`と入力して、`Enter`を押します。

4. ログファイルの作成:

```bash
touch /var/log/redsocks.log
chmod 644 /var/log/redsocks.log
```

### ステップ3: Redsocksサービスを開始する

1. 起動時にRedsocksを有効にする:

```bash
/etc/init.d/redsocks enable
```

2. Redsocksを起動:

```bash
   /etc/init.d/redsocks start
   ```

3. Redsocksが動作していることを確認する:

```bash
ps | grep redsocks
```

Redsocksプロセスが実行されているのが確認できるはずです。

---

## 5. OpenWRTのトラフィックをmacOSプロキシ経由にリダイレクトする

OpenWRTにRedsocksが設定されたので、iptablesを設定して、すべての発信TCPトラフィックをRedsocks経由でリダイレクトし、それがMacのShadowsocksプロキシを経由するようにします。

### ステップ1: iptablesルールの設定

1. トラフィックをリダイレクトするためのiptablesルールを追加:

```bash
   # すべてのTCPトラフィックをRedsocksにリダイレクト（プロキシ自体へのトラフィックを除く）
   iptables -t nat -N REDSOCKS
   iptables -t nat -A REDSOCKS -d xxx.xxx.xxx.xxx -p tcp --dport xxxxx -j RETURN
   iptables -t nat -A REDSOCKS -p tcp -j REDIRECT --to-ports 12345
```

# すべての発信トラフィックにREDSOCKSチェーンを適用する
```bash
iptables -t nat -A OUTPUT -p tcp -j REDSOCKS
iptables -t nat -A PREROUTING -p tcp -j REDSOCKS
```

   説明:
   - 新しいチェーンを作成: `REDSOCKS`
   - プロキシトラフィックを除外: プロキシ自体へのトラフィックがリダイレクトされないようにします。
   - その他のTCPトラフィックをリダイレクト: 他のTCPトラフィックをRedsocksのリスニングポート（`12345`）に転送します。

2. iptablesルールの保存:

これらのルールを再起動後も永続的にするには、ファイアウォールの設定に追加してください。

```bash
vi /etc/firewall.user
```

   iptablesルールを追加:

```bash
   # すべてのTCPトラフィックをRedsocksにリダイレクト（プロキシを除く）
   iptables -t nat -N REDSOCKS
   iptables -t nat -A REDSOCKS -d xxx.xxx.xxx.xxx -p tcp --dport xxxxx -j RETURN
   iptables -t nat -A REDSOCKS -p tcp -j REDIRECT --to-ports 12345
```

# REDSOCKSチェーンの適用
```bash
iptables -t nat -A OUTPUT -p tcp -j REDSOCKS
iptables -t nat -A PREROUTING -p tcp -j REDSOCKS
```

保存して終了:
   - `ESC`を押し、`:wq`と入力して、`Enter`を押します。

3. 変更を適用するためにファイアウォールを再起動:

```bash
/etc/init.d/firewall restart
```

### ステップ2: トラフィックがリダイレクトされていることを確認する

1. Redsocksのログを確認する:

```bash
cat /var/log/redsocks.log
```

Redsocksを介してトラフィックが処理されていることを示すログが表示されるはずです。

2. クライアントデバイスからのテスト:
   - OpenWRTルーターにデバイスを接続します。
   - インターネットを使用するウェブサイトにアクセスするか、何らかのアクションを実行します。
   - 外部IPアドレス（例：[WhatIsMyIP.com](https://www.whatismyip.com/)）を確認して、トラフィックがShadowsocksプロキシを経由していることを確認します。プロキシのIPが反映されているかどうかを確認します。

---

## 6. プロキシ設定のテスト

以下のテストを実行して、セットアップ全体が意図した通りに動作することを確認してください。

### ステップ1: MacでのShadowsocks接続を確認する

1. Shadowsocksクライアントのステータスを確認する：
   - Shadowsocks-NGまたはClashがShadowsocksサーバーにアクティブに接続されていることを確認します。
   - ローカルプロキシ（例：`xxx.xxx.xxx.xxx:xxxxx`）がアクセス可能かどうかを確認します。

2. プロキシをローカルでテストする：
   - Macでブラウザを開き、SOCKS5プロキシとして`localhost:1080`を使用するように設定します。
   - [WhatIsMyIP.com](https://www.whatismyip.com/)にアクセスし、IPがShadowsocksサーバーと一致することを確認します。

### ステップ2: OpenWRTのトラフィックがプロキシを経由していることを確認する

1. OpenWRTの外部IPを確認する:
   - OpenWRTに接続されたデバイスから、[WhatIsMyIP.com](https://www.whatismyip.com/)にアクセスし、IPがShadowsocksサーバーのIPを反映しているかどうかを確認します。

2. Redsocksのログを監視する:
   - OpenWRT上で、Redsocksのログを監視し、トラフィックがリダイレクトされていることを確認します。
   
   ```bash
   tail -f /var/log/redsocks.log
   ```

3. 必要に応じてトラブルシューティングを行う:
   - トラフィックが正しくルーティングされない場合:
     - Mac上のShadowsocksクライアントが実行中でアクセス可能であることを確認する。
     - iptablesのルールが正しく設定されていることを確認する。
     - MacとOpenWRTの両方のファイアウォール設定を確認する。

---

## 追加の考慮事項

### 1. セキュリティ

- プロキシのセキュリティを確保する:
  - 信頼できるデバイスのみがプロキシにアクセスできるようにします。すべてのトラフィックをRedsocks経由でリダイレクトしているため、MacのファイアウォールがOpenWRTルーターからの接続のみを許可するように設定します。

macOSの場合:

- システム環境設定 > セキュリティとプライバシー > ファイアウォールに移動します。
- ファイアウォールを設定し、OpenWRTルーターのIPからのみプロキシポート（`xxxxx`）への着信接続を許可します。

- 認証:
  - Shadowsocksは暗号化を通じてある程度のセキュリティを提供しています。強力なパスワードと暗号化方式を確保してください。

### 2. パフォーマンス

- ルーターのリソース:
  - Redsocksのようなプロキシサービスを実行すると、OpenWRTルーターのCPUとメモリを余分に消費する可能性があります。ルーターに十分なリソースがあることを確認してください。

- Macのパフォーマンス:
  - プロキシの可用性を維持するために、Macが電源に接続され、ネットワークに接続されていることを確認してください。

### 3. メンテナンス

- ログの監視:
  - RedsocksとShadowsocksのログを定期的にチェックし、異常な活動やエラーがないか確認します。

- ソフトウェアの更新:
  - OpenWRT、Redsocks、およびShadowsocksクライアントを最新の状態に保ち、セキュリティパッチやパフォーマンスの向上を活用しましょう。

### 4. 代替アプローチ

Macを中間プロキシサーバーとして使用することは可能ですが、以下の代替案を検討することで、より簡単な設定ができるかもしれません：

- OpenWRTを直接Shadowsocksクライアントとして設定する:
  - OpenWRTは`shadowsocks-libev`のようなパッケージを通じて直接Shadowsocksをサポートしています。この方法では、Macを仲介する必要がなくなります。

- 専用のプロキシ/VPNデバイスを使用する:
  - Raspberry Piのようなデバイスはプロキシサービスを実行し、専用のゲートウェイとして機能させることができます。

---

## 結論

上記の手順に従うことで、MacをShadowsocksプロキシサーバーとして設定し、OpenWRTルーターを構成して、接続されたすべてのデバイスのトラフィックをこのプロキシ経由でルーティングするようにしました。この設定により、Shadowsocksプロトコルを活用してネットワークのプライバシーと制御が強化されます。

要点のまとめ：

1. MacでのShadowsocksクライアント：
   - 提供されたShadowsocks URLを使用して、Shadowsocks-NGまたはClashをインストールおよび設定しました。
   - クライアントをMacのLAN IPでリッスンするように設定しました。

2. プロキシのアクセシビリティ:
   - Macに静的IPを割り当て、プロキシへの一貫したアクセスを確保しました。
   - macOSのファイアウォールを設定し、着信プロキシ接続を許可しました。

3. OpenWRTの設定：
   - Redsocksをインストールし、すべての外向きTCPトラフィックをShadowsocksプロキシ経由でリダイレクトするように設定しました。
   - トラフィックリダイレクトを強制するために必要なiptablesルールを適用しました。

4. テスト:
   - 接続されたデバイスからのトラフィックがShadowsocksプロキシを経由していることを確認するため、外部IPアドレスをチェックしました。

おすすめ：

- **安定性を確保する**: プロキシの可用性を維持するために、Macの電源を入れ、接続を維持してください。
- **セキュリティを最優先に**: すべてのコンポーネントを定期的に更新し、ログを監視して不正アクセスから保護してください。
- **ルーターの直接設定を検討する**: より効率的なセットアップのために、OpenWRTルーター上で直接Shadowsocksを設定する方法を探ってみてください。

特定の設定で問題が発生したり、さらなるサポートが必要な場合は、お気軽にお問い合わせください！

```
base {
    log_debug = on;
    log_info = on;
    log = "file:/var/log/redsocks.log";
    daemon = on;
    redirector = generic;
}
```

この設定は、`redsocks`の基本的な設定を定義しています。以下に各設定項目の説明を示します：

- `log_debug = on;`: デバッグログを有効にします。
- `log_info = on;`: 情報ログを有効にします。
- `log = "file:/var/log/redsocks.log";`: ログを`/var/log/redsocks.log`ファイルに出力します。
- `daemon = on;`: `redsocks`をデーモンとして実行します。
- `redirector = generic;`: ジェネリックなリダイレクタを使用します。

この設定は、`redsocks`がバックグラウンドで動作し、ログを指定されたファイルに出力するように指示しています。

```redsocks {
    local_ip = 0.0.0.0;
    local_port = 7891;
    ip = xxx.xxx.xxx.xxx;
    port = xxxxx;
    type = http-connect;
    login = "";
    password = "";
}
```
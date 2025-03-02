---
audio: false
generated: false
lang: ja
layout: post
title: テレビでYouTubeを見る方法
translated: true
---

ここでは、科学的上網（インターネットアクセス）の方法を知っていると仮定します。では、テレビでYouTubeを見るにはどうすればよいでしょうか。ルーターを改造するのは少し面倒です。ここでは、一つのアプリを利用します。

## SmartYoutubeTV

![スマート](assets/images/youtube-tv/smart.jpg)

それをダウンロードして、USBメモリを使ってテレビにインストールします。

![clash](assets/images/youtube-tv/clash.jpg)

次に、科学上网アプリのクライアントで、`Allow connect from Lan`（LANからの接続を許可する）を選択します。これは、ローカルネットワーク上の他のデバイスがこのデバイスを介してインターネットに接続することをサポートすることを意味します。

次に、`SmartYoutubeTV`の設定オプションでポートを設定するだけでOKです。

![proxy1](assets/images/youtube-tv/proxy1.jpeg)

設定が完了したら、`テスト`ボタンをクリックして試してみてください。ここでは`SOCKS`タイプのプロキシを使用していることに注意してください。`HTTP`で試したところ、何度か失敗しました。テストが成功したら、`OK`をクリックして、再度テストを行ってみてください。また、あなたの環境では`192.168.1.3`に設定する必要はなく、あなたのコンピュータのローカルネットワークアドレスによって異なります。

こうやって見ることができて、とても便利です。

![tan](assets/images/youtube-tv/tan.jpeg)

## gfreezy/seeker

これはGitHubのプロジェクトです。プロジェクトのホームページには使用方法が記載されています。ここでは主にいくつかの追加のポイントを補足します。

![seeker](assets/images/youtube-tv/seeker.jpg)

これは、tun を使用して透過プロキシを実現しています。Surge の拡張モードやゲートウェイモードに似た機能を実装しています。

最初から、私は`seeker`を使って自分のコンピュータを科学的上網ルーターに変えていました。ここで私の設定について話しましょう：

```yml
verbose: true
dns_start_ip: 10.0.0.10
dns_servers:
  - 223.5.5.5:53
  - 114.114.114.114:53  
dns_timeout: 1s
tun_name: utun4
tun_ip: 10.0.0.1
tun_cidr: 10.0.0.0/16
dns_listen: 0.0.0.0:53
gateway_mode: true
ping_timeout: 2s
probe_timeout: 30ms
connect_timeout: 1s
read_timeout: 30s
write_timeout: 5s
max_connect_errors: 2
```

この設定ファイルは、ネットワーク設定に関するものです。以下に各項目の説明を記載します。

- `verbose: true`: 詳細なログ出力を有効にします。
- `dns_start_ip: 10.0.0.10`: DNSサーバーの開始IPアドレスを指定します。
- `dns_servers`: 使用するDNSサーバーのリストです。
  - `223.5.5.5:53`: 1つ目のDNSサーバーのIPアドレスとポート番号。
  - `114.114.114.114:53`: 2つ目のDNSサーバーのIPアドレスとポート番号。
- `dns_timeout: 1s`: DNSクエリのタイムアウト時間を1秒に設定します。
- `tun_name: utun4`: 使用するTUNインターフェースの名前を指定します。
- `tun_ip: 10.0.0.1`: TUNインターフェースのIPアドレスを指定します。
- `tun_cidr: 10.0.0.0/16`: TUNインターフェースのCIDRブロックを指定します。
- `dns_listen: 0.0.0.0:53`: DNSサーバーがリッスンするIPアドレスとポート番号を指定します。
- `gateway_mode: true`: ゲートウェイモードを有効にします。
- `ping_timeout: 2s`: Pingのタイムアウト時間を2秒に設定します。
- `probe_timeout: 30ms`: プローブのタイムアウト時間を30ミリ秒に設定します。
- `connect_timeout: 1s`: 接続のタイムアウト時間を1秒に設定します。
- `read_timeout: 30s`: 読み取りのタイムアウト時間を30秒に設定します。
- `write_timeout: 5s`: 書き込みのタイムアウト時間を5秒に設定します。
- `max_connect_errors: 2`: 最大接続エラー数を2に設定します。

```yaml
servers:
  - name: httpプロキシサーバー
    addr: 0.0.0.0:7890
    protocol: Http
```

```yaml
  - name: httpsプロキシサーバー
    addr: 0.0.0.0:7890
    protocol: Https
```

rules:
  - 'MATCH,PROXY'
```

最初、私は `socks5` プロキシを使用していました。設定は次のように書きました：

```yml
servers:
  - name: socks5 プロキシサーバー
    addr: 0.0.0.0:7891
    protocol: Socks5
```

しかし、いくつかの問題があります。頻繁に接続できないことがあります。ドキュメントには以下のような記述があります：

> socks5 プロキシを使用する場合、すべての直接接続するドメインを設定ファイルに含める必要があります。ss や vmess などを使用する場合、ss や vmess サーバーのドメインも設定ファイルに追加する必要があります。そうしないと、無限ループが発生し、正常に使用できなくなる可能性があります。

この理由かもしれません。

`seeker`を使う場合、それをルーターとして機能させるために、常にコンピュータを稼働させておく必要があります。一方、`proxy`設定の方法はより柔軟です。iPhoneやAndroidスマートフォンを使ってプロキシポートを共有することができます。

## テレビスクリーンショット

この記事を書いている際、テレビでスクリーンショットを撮る方法について考えました。私の家ではXiaomiのテレビを使用しています。リモコンの`Home`ボタンを2回連打することで、アプリ管理メニューを呼び出すことができます。

![tv_screen](assets/images/youtube-tv/tv_screen.jpeg)

スクリーンショットボタンが見えますか。それから、WeChatに簡単に共有することもできます。ここでは、アプリケーションをすべて閉じることもできます。もし一部のアプリケーションがフリーズした場合、このように処理することができます。

さあ、大画面テレビで世界を見てみましょう。
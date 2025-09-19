---
audio: false
generated: true
image: true
lang: ja
layout: post
title: テレビでYouTubeを視聴する方法
translated: true
---

このガイドは、既にgeo-restrictionsを回避する方法を持っていることを前提としています。ルーターにカスタムファームウェアを書き込むことなく、アプリを使用してTVでYouTubeを視聴する方法を紹介します。

---

## **SmartYouTubeTV**

![SmartYouTubeTV](assets/images/youtube-tv/smart.jpg)

1. **ダウンロードとインストール**:
   アプリをダウンロードし、USBドライブを使用してTVにサイドロードします。

2. **プロキシの設定**:
   - プロキシクライアント（例: Clash）で、**"Allow connections from LAN"** を有効にし、ローカルネットワークデバイスがあなたのマシンを経由してトラフィックをルーティングできるようにします。
   - **SmartYouTubeTV** で設定メニューを開き、プロキシの詳細を入力します（例: `192.168.1.3:7890`）。
     *注意*: **SOCKS5** を使用してください（HTTPプロキシはテストで失敗しました）。`192.168.1.3` はあなたのマシンのローカルIPに置き換えてください。

3. **テストと確認**:
   アプリ内で **"Test"** をクリックして接続を確認します。成功したら設定を保存し、ストリーミングを開始します。

![Proxy Setup](assets/images/youtube-tv/proxy1.jpeg)
![Success](assets/images/youtube-tv/tan.jpeg)

---

## **gfreezy/seeker (Transparent Proxy)**
コンピューターをプロキシゲートウェイとして機能させるGitHubプロジェクト（**TUN**を使用、Surgeのenhanced/gatewayモードに類似）。以下に主要なメモと動作する設定を示します。

### **設定 (`config.yml`)**
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

servers:
  - name: http proxy server
   addr: 0.0.0.0:7890
   protocol: Http
  - name: https proxy server
   addr: 0.0.0.0:7890
   protocol: Https

rules:
  - 'MATCH,PROXY'
```

### **なぜSOCKS5ではないのか？**
当初はSOCKS5を試しました：
```yml
servers:
  - name: socks5 proxy server
   addr: 0.0.0.0:7891
   protocol: Socks5
```
しかし、[ドキュメント](https://github.com/gfreezy/seeker)によると**接続ループ**が発生し、ドメインに対する明示的な直接接続ルールが必要になりました。**HTTP/HTTPSプロキシ**の方が安定して動作しました。

### **トレードオフ**
- **Seeker**: 専用のマシンがルーターとして機能する必要があります。
- **プロキシモード (SmartYouTubeTV)**: 柔軟性があり、プロキシポートを共有するスマホやタブレットでも使用可能です。

![Seeker](assets/images/youtube-tv/seeker.jpg)

---

## **TVのスクリーンショット (Xiaomi TV)**
スクリーンショットを撮影するには：
1. リモコンの **`Home` ボタンをダブルクリック** し、アプリマネージャーを開きます。
2. **スクリーンショットボタン** を選択し、WeChat（または他のアプリ）で共有します。
3. このメニューを使用して **フリーズしたアプリを強制終了** します。

![TV Screenshot](assets/images/youtube-tv/tv_screen.jpeg)

---

大画面での視聴をお楽しみください！

---

## **更新情報 (2025年9月)**

Apple TVはネイティブでVPNソフトウェアをサポートするようになりました。**Shadowrocket** をインストールしてプロキシサーバーに接続し、直接YouTube TVをストリーミングできます。
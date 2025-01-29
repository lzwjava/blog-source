---
audio: true
lang: ja
layout: post
title: ヘツナー・クラウド
translated: true
---

最近、このクラウドプラットフォームに試すことに非常に興奮しています。

{: .centered }
![](assets/images/hertzner/h.jpg){: .responsive }
*Source: Hetzner*{: .caption }

ヘルシンキのサーバーで、2つのAMD VCPU、2GBのRAM、40GBのSSD、および20TBのトラフィックを搭載した構成は、1ヶ月に4.49ドルでご利用いただけます。

追加でIPv4アドレスを1ヶ月に0.60ドルで提供するため、合計は5.09ドルになります。

彼らは以下の6か所でサービスを提供しています：

- ドイツのヌーレンベルク
- ドイツのファルケンシュタイン
- フィンランドのヘルシンキ
- シンガポール
- アメリカのオレゴン州のヒルスボロ
- アメリカのバージニア州のアッシュバーン

流行りの人気の場所を選ぶトレンドに従わないことが興味深いです。彼らの場所はVultrやDigital Oceanの場所とは異なります。

ファイアウォールの設定は使いやすいです。初めて使ったのですが、プロキシサーバーの正しい構成を迅速に設定することができました。

> sudo bash -c "$(wget -qO- https://raw.githubusercontent.com/Jigsaw-Code/outline-server/master/src/server_manager/install_scripts/install_server.sh)"

ヘルシンキのHetznerサーバーの速度は非常に速いです。Speedtest iOSアプリを使用してダウンロード速度は423 Mbps、アップロード速度は56.1 Mbpsです。

ShadowrocketでのPingは1175 msですが、これは重大な問題ではありません。
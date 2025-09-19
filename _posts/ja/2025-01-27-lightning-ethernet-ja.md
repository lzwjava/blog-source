---
audio: false
generated: false
image: true
lang: ja
layout: post
title: 雷光へのイーサネットアダプター
translated: true
---

最近、使ったことのない新しい製品を試しました。JD.comで44元で購入しました。類似の製品はWalmart.comで15米ドルほどです。

動作は完全で、追加の設定は必要ありません。アダプタを接続すると「Ethernet」メニュー項目が表示されます。

Speedtest iOSアプリを使用して速度をテストしました。結果は以下に示します。

| ネットワークタイプ                     | 距離     | ダウンロード速度 (MBPS) | アップロード速度 (MBPS) | 線             |
|----------------------------------|------------|-----------------------|---------------------|------------------|
| モデム -> TP-LINKルーター -> 電話 | 約30m | 2.90                  | 4.82                | 広州 -> マカオ |
| モデム -> ケーブル -> 電話          | 約30m | 84.9                  | 59.7                | 広州 -> マカオ |

1つのテストでは、ping (ms) 応答性の結果は以下に示します:

| メトリック   | 値 | ジョイタ |
|----------|-------|--------|
| アイドル     | 33    | 68     |
| ダウンロード | 1885  | 110    |
| アップロード   | 127   | 54     |

これは somewhat naiveなテストです。スピードの違いの1つの理由は、モデム -> TP-LINKルーターの接続が約20m、TP-LINKルーター -> 電話の接続が約10mであることです。さらに、TP-LINKルーターは無線ブリッジを使用してモデムに接続されています。

Speedtestは便利なツールです。Alibaba Cloudのサーバーを使用し、帯域を5Mbpsに設定すると、アプリを使用してテストすると結果が約5Mbpsになります。

興味深いことに、Wi-FiとEthernetの両方に接続すると、どちらを優先する方法はなく、この構成ではEthernetを使用するだけです。Wi-Fiを使用するには、Ethernetアダプタを外してください。

{: .centered }
![](assets/images/lightning/l1.jpg){: .responsive }
*ソース: iOS*{: .caption }

{: .centered }
![](assets/images/lightning/l2.jpg){: .responsive }
*ソース: Walmart.com*{: .caption }

{: .centered }
![](assets/images/lightning/n.jpg){: .responsive }
*ソース: network_plot.py*{: .caption }
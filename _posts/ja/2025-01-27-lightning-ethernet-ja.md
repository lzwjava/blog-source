---
audio: true
lang: ja
layout: post
title: Lightning to Ethernetアダプター
translated: true
---

最近、私はこれまで使ったことのない新しい製品を試してみました。JD.comで約44元で購入しました。Walmart.comでは似たような製品が約15ドルで販売されています。

この製品は完璧に動作し、追加の設定は必要ありませんでした。アダプターを接続すると、「Ethernet」というメニュー項目が表示されます。

Speedtest iOSアプリを使って速度をテストしました。結果は以下の通りです。

| ネットワークタイプ                     | 距離       | ダウンロード速度 (MBPS) | アップロード速度 (MBPS) | 回線             |
|----------------------------------|------------|-----------------------|---------------------|------------------|
| モデム -> TP-LINKルーター -> スマホ | 約30m      | 2.90                  | 4.82                | 広州 -> マカオ   |
| モデム -> ケーブル -> スマホ      | 約30m      | 84.9                  | 59.7                | 広州 -> マカオ   |

これはやや単純なテストです。速度の違いの一因として、モデム -> TP-LINKルーター間の接続が約20m、TP-LINKルーター -> スマホ間の接続が約10mであることが考えられます。さらに、TP-LINKルーターは無線ブリッジを使用してモデムに接続しています。

{: .centered }
![](assets/images/lightning/l1.jpg){: .responsive }
*出典: iOS*{: .caption }

{: .centered }
![](assets/images/lightning/l2.jpg){: .responsive }
*出典: Walmart.com*{: .caption }

{: .centered }
![](assets/images/network_speed_chart.jpg){: .responsive }
*出典: network_plot.py*{: .caption }
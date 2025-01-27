---
audio: true
lang: ja
layout: post
title: Lightning to Ethernetアダプター
translated: true
---

最近、私はこれまで使ったことのない新しい製品を試してみました。JD.comで約44元で購入しました。Walmart.comでは同様の製品が約15ドルで販売されています。

この製品は完璧に動作し、追加の設定は必要ありません。アダプターを接続すると、「Ethernet」メニュー項目が表示されます。

Speedtest iOSアプリを使用して速度をテストしました。結果は以下の通りです。

| ネットワークタイプ                     | 距離       | ダウンロード速度 (MBPS) | アップロード速度 (MBPS) | 回線             |
|----------------------------------|------------|-----------------------|---------------------|------------------|
| モデム -> TP-LINKルーター -> スマートフォン | 約30m      | 2.90                  | 4.82                | 広州 -> マカオ     |
| モデム -> ケーブル -> スマートフォン          | 約30m      | 84.9                  | 59.7                | 広州 -> マカオ     |

あるテストでは、ping（ms）の応答性の結果は以下の通りでした：

| メトリック   | 値    | ジッター |
|----------|-------|--------|
| アイドル     | 33    | 68     |
| ダウンロード | 1885  | 110    |
| アップロード   | 127   | 54     |

これはやや単純なテストです。速度の違いの一因として、モデム -> TP-LINKルーター間の接続が約20m、TP-LINKルーター -> スマートフォン間の接続が約10mであること、さらにTP-LINKルーターがモデムに無線ブリッジで接続していることが考えられます。

興味深いのは、Wi-FiとEthernetの両方を接続した場合、どちらかを優先する方法がないことです。この設定ではEthernetしか使用できません。Wi-Fiを使用したい場合は、Ethernetアダプターを抜く必要があります。

{: .centered }
![](assets/images/lightning/l1.jpg){: .responsive }
*出典: iOS*{: .caption }

{: .centered }
![](assets/images/lightning/l2.jpg){: .responsive }
*出典: Walmart.com*{: .caption }

{: .centered }
![](assets/images/lightning/n.jpg){: .responsive }
*出典: network_plot.py*{: .caption }
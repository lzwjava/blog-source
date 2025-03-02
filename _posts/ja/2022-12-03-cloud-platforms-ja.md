---
audio: false
generated: false
lang: ja
layout: post
title: いくつかのグローバルクラウドプラットフォーム
translated: true
---

<div align="center"><img src="/assets/images/cloud/platform.jpg" width="400px"/><img/></div>

* [Azure](#azure)
* [AWS Lightsail](#aws-lightsail)
* [Digital Ocean](#digital-ocean)
* [Vultr](#vultr)
* [Google Cloud - 失敗](#google-cloud---fail)
* [概要](#outline)
* [まとめ](#summary)

最近、いくつかのクラウドプラットフォームを試してみました。それを使って自分のプロキシサーバーを設定しました。以前は、サードパーティのプロキシサーバーを使っていましたが、そのサーバーは多くのユーザーに利用されているため、時々速度が遅くなることがありました。この問題を解決するために、自分でサーバーを設定してみることにしました。

## Azure

Azureは良い選択肢です。ここで3つの仮想マシンを作成しました。なぜなら、プラットフォームが無料で200ドルのクレジットを提供してくれたからです。私のマシンはカタール、アメリカ、そして香港にあります。私の広州のラップトップからカタールのサーバーへのping時間は150msです。現在、アメリカのサーバーへのpingパケットは100%失われています。2日前はpingが成功していました。そして、香港のサーバーへのpingパケットも100%失われています。iOSのプロキシクライアントでテストしましたが、接続できませんでした。これらをシャットダウンする必要があります。コストは無料ですが、失われたサーバーは私にとって役に立ちません。

<div align="center"><img src="/assets/images/cloud/azure.png" /><img/></div>

コンソールとネットワークタブを見てみましょう。上と下に表示されています。

<div align="center"><img src="/assets/images/cloud/network.png" /><img/></div>

私のカスタムネットワーク設定はシンプルです。プロトコルに関係なく、1024から65535までの任意のポートを開放しています。これは私のプロキシサーバーだからです。内部に秘密のデータやプログラムはありません。そのため、Outlineアプリの提案に従ってこのように設定しています。

## AWS Lightsail

LightsailはAWSの軽量な製品です。AWSには多くの製品がありますが、時にはその中に仮想マシンを作成したいだけのこともあります。そこで、AWSはLightsailを提供しています。

<div align="center"><img src="/assets/images/cloud/lightsail.png" /><img/></div>

## Digital Ocean

海外のクラウドプラットフォームの中でも、特に2016年から2018年にかけて、Digital Oceanをよく利用していました。毎月5ドルを費やしていました。

次のようにしてドロップレットを作成します：

<div align="center"><img src="/assets/images/cloud/do.png" /><img/></div>

以下が私の請求履歴です:

<div align="center"><img src="/assets/images/cloud/bill.png" /><img/></div>

## Vultr

2018年から2020年までVultrを使用していました。

<div align="center"><img src="/assets/images/cloud/vultr.png" /><img/></div>

## Google Cloud - 失敗

私もGoogle Cloudを試してみたいのですが、失敗しました。彼らは中国のユーザーをサポートしていません。他の国の市民として偽の情報を提供することはできますが、登録を成功させるための対応するクレジットカードを持っていないのです。

<div align="center"><img src="/assets/images/cloud/google.png" /><img/></div>

## アウトライン

Outlineはクラウドプラットフォームではありません。それはプロキシツールです。私がプロキシサーバーを設定するのを助けてくれるので、それについて別の段落を書いて称賛しなければなりません。それは本当に役に立ちます。オンラインで検索することでそれについて学ぶことができます。

<div align="center"><img src="/assets/images/cloud/outline.png" /><img/></div>

## 概要

最も安価で最低限の構成のサーバーは、通常月額5ドル程度です。数人のユーザーが使用するプロキシサーバーとして十分な性能を持っています。シンガポール、香港、その他のアジア地域のサーバーは、通常、アメリカやヨーロッパのサーバーよりも高速に接続されます。また、サーバーを設定した直後は非常に快適に動作することがありますが、数日経つとゾンビのように動作が遅くなることがあります。そのため、速度と安定性に関しては、日常の使用の中で真実を見つけるしかありません。
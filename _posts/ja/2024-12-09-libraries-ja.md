---
audio: false
generated: false
image: false
lang: ja
layout: post
title: ライブラリ使用時のアップグレードを検討する
translated: true
type: post
---

私のスタートアッププロジェクト、[Fun Live](https://github.com/lzwjava/live-server)でCodeIgniterを使用しました。プロジェクトは終了しましたが、数年経った今、それを記念して復活させたいと思いました。しかし、2016年当時はCodeIgniter 3を使用していましたが、現在の最新バージョンはCodeIgniter 4です。

アップグレードが困難であることが判明しました。私のコードはCodeIgniterフレームワークと密接に結合しているためです。[https://codeigniter4.github.io/CodeIgniter4/installation/upgrade_4xx.html](https://codeigniter4.github.io/CodeIgniter4/installation/upgrade_4xx.html)にあるアップグレードガイドに従うと、コードベースを更新するには多大な労力が必要であることがわかります。

この経験から、重要な教訓を得ました。コードを書く際には、将来の更新をどのように扱うかを慎重に考慮すべきです。私たちが制御できるコードの部分と、サードパーティの依存関係によって制御される部分を考えることが重要です。
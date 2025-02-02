---
audio: false
lang: ja
layout: post
title: タブキラー
translated: true
---

これは GitHub プロジェクト [https://github.com/lzwjava/TabsKiller](https://github.com/lzwjava/TabsKiller) の README.md です。

---

# TabsKiller

ブラウザが多すぎるタブで混乱しているときに、自動的に最も古いタブを閉じる Chrome プラグインをご紹介します。もはや散らかったブラウザの経験とはお別れです！

神奇な Chrome プラグインです。開いているページが多すぎるときに、自動的に最も古いページを閉じて、ブラウザを清潔に保ちます！

![xxqq20160114-1 2x](https://cloud.githubusercontent.com/assets/5022872/12328379/25a749c2-bb16-11e5-8400-6e5c67027a61.png)

=>

![qq20160114-2 2x](https://cloud.githubusercontent.com/assets/5022872/12328400/3906a1ca-bb16-11e5-853c-0da4ce65cd6a.png)

# プラグイン

![qq20151003-2 2x](https://cloud.githubusercontent.com/assets/5022872/10262499/b39deb34-69fc-11e5-93b8-35bf10cedaaa.jpg)

# 特性

1. タブの数が設定した制限を超えると、自動的に最も古いタブを閉じます。
2. 最大タブ数（x）を好みに合わせてカスタマイズできます。
3. 特定の URL パターンをロックして、そのパターンに一致するタブが多くても開いたままにすることができます。

1. 開いているページが一定数を超えたときに、自動的に最も古いページを閉じます。
2. 最大のタブ数を設定できます。
3. ロックのルールを設定して、そのルールに合致するページを閉じられないようにします。

## ストーリー

私は Chrome でたくさんのタブを開くことが多いです。だから、Ctrl + W を押してたくさん閉じます。繰り返し。繰り返し。だから、私の問題を解決するために拡張機能を書きたいと考えていました。その後、「Tab Wrangler」拡張機能を見つけました。x 分間アクティブでないタブを閉じます。それを学び、x タブを超えたときに最も古いタブを閉じる拡張機能を作りました。そして、特定の URL パターンに一致するタブをロックしました。とても役立っています。もうタブを気にする必要はありません。タブが多くなりすぎることはありません。私の生活が楽になりました。これをお好きになることを願っています。

## デモ

![killer](https://cloud.githubusercontent.com/assets/5022872/10262518/cd196a60-69fd-11e5-93bf-0589d65eeb19.gif)

## インストール

Chrome ストアにアクセスしてください https://chrome.google.com/webstore/detail/tabs-killer/hgmdeeoighmhomddlghfjcidkdcpbllf/ 、または手動でインストールします：

まず、`chrome://extensions` に移動し、開発者モードを選択し、アンパッケージ化された拡張機能を読み込みます。完了です。

![chrome](https://cloud.githubusercontent.com/assets/5022872/10262586/ddc451b0-6a00-11e5-8b10-da16c9658221.jpg)

詳細については、Chromeの「Get Started」[チュートリアル](https://developer.chrome.com/extensions/getstarted#unpacked)を参照してください。

中文：

Chrome ストアにアクセスしてください https://chrome.google.com/webstore/detail/tabs-killer/hgmdeeoighmhomddlghfjcidkdcpbllf/、または手動でインストールします：

右側の Download ZIP をクリックしてソースコードをダウンロードし、展開します。次に、`chrome://extensions` を開きます（ブラウザのアドレスバーにコピーして開きます）、`開発者モード` を選択し、`アンパッケージ化された拡張機能を読み込む` をクリックします。これで、次のように表示されます。その後、ファイル選択ダイアログが表示されます。先ほどダウンロードしたソースコードディレクトリを選択します。これで、このプラグインがインストールされました。
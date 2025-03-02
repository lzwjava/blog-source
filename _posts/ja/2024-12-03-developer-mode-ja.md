---
audio: false
generated: false
lang: ja
layout: post
title: iOSのデベロッパーモードとideviceinstaller
translated: true
---

## デベロッパーモード

私はかつて、しばらくの間iOS開発者でした。しかし、私のキャリアの焦点は他の技術に移りました。とはいえ、現在はプロのiOS開発者ではないにせよ、iOS開発の知識を応用することは非常に役立ちます。

最近、インストールしたアプリを共有したいと思いました。しかし、ホーム画面や設定のアプリリストからすべてのアプリのスクリーンショットを撮ると、ごちゃごちゃになってしまいます。そこで、インストールされているすべてのアプリを表示する方法を見つける必要がありました。

以下は、Xcodeを使用してインストールされているすべてのアプリを表示する手順です：

1. iPhoneをUSBでMacに接続します
2. Xcodeを開きます
3. Window → Devices and Simulators に移動します（または Shift + Cmd + 2 を押します）
4. 左サイドバーからiPhoneを選択します
5. メインパネルで、"Installed Apps"セクションまでスクロールします

他の便利な機能もあります：

1. スクリーンショットを撮る
2. 最近のログを開く
3. コンソールを開く

## xcrun

`xcrun` は、Xcode コマンドラインツールの一部で、開発者がコマンドラインから Xcode の機能やツールにアクセスするためのユーティリティです。`xcrun` を使用することで、特定のツールやフレームワークを簡単に呼び出したり、Xcode のバージョン管理を行ったりすることができます。

例えば、`xcrun` を使って Swift コンパイラを呼び出すことができます：

```bash
xcrun swiftc -o hello hello.swift
```

このコマンドは、`hello.swift` ファイルをコンパイルし、`hello` という実行可能ファイルを生成します。

`xcrun` は、Xcode のインストールパスやツールチェーンの管理を自動化するため、開発者が手動でパスを設定する手間を省くことができます。

```bash
(base) lzwjava@192 Downloads % xcrun devicectl device info apps --device 00008120-xxxx --verbose
詳細ログを有効にしています。
2024-12-03 16:24:18.579+0800  デベロッパーディスクイメージサービスを有効にしています。
2024-12-03 16:24:18.637+0800  使用権を取得しました。
インストールされているアプリ:
  - 0 要素
```

コマンドが完了しました、0.120秒かかりました
```

## ideviceinstaller

```bash
brew install ideviceinstaller
ideviceinstaller -l
```

上記のコマンドは、`ideviceinstaller`をインストールし、接続されているiOSデバイスにインストールされているアプリのリストを表示するものです。このコマンドはそのまま使用できます。

```bash
(base) lzwjava@192 Downloads % ideviceinstaller -l
CFBundleIdentifier, CFBundleVersion, CFBundleDisplayName
com.huawei.smarthome-ios, "14.1.1.325", "HUAWEI AI Life"
com.sf-express.waybillcn, "9.70.0.1", "顺丰速运"
com.roblox.robloxmobile, "2.652.762", "Roblox"
co.alphaexploration.clubhouse, "3273", "Clubhouse"
com.dbs.mbanking.cn, "11", "DBS digibank"
global.longbridge.ios, "59579", "Longbridge"
imgurmobile, "416", "Imgur"
com.creditkarma.mobile, "17316145", "Credit Karma"
...
```
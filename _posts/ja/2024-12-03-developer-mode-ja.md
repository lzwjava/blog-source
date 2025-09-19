---
audio: false
generated: false
image: false
lang: ja
layout: post
title: iOSとideviceinstallerのデベロッパーモード
translated: true
---

## デベロッパーモード

私は一時期iOSデベロッパーとして働いていました。しかし、現在のキャリアは他の技術にシフトしています。それでも、プロのiOSデベロッパーではない現在でも、iOS開発の知識は非常に役立ちます。

最近、インストール済みのアプリを共有したくなりました。しかし、ホーム画面や設定のアプリ一覧からすべてのアプリのスクリーンショットを撮ると、ごちゃごちゃしてしまいます。そこで、インストール済みのアプリをすべて表示する方法を探す必要がありました。

Xcodeを使ってインストール済みのアプリをすべて表示する手順は以下の通りです：

1. iPhoneをUSBケーブルでMacに接続
2. Xcodeを開く
3. ウィンドウ → デバイスとシミュレーター（またはShift + Cmd + 2を押す）
4. 左サイドバーからiPhoneを選択
5. メインパネルで「Installed Apps」セクションまでスクロール

その他の便利な機能もあります：

1. スクリーンショットの撮影
2. 最近のログの表示
3. コンソールの開く

## xcrun

```bash
(base) lzwjava@192 Downloads % xcrun devicectl device info apps --device 00008120-xxxx --verbose
Using verbose logging.
2024-12-03 16:24:18.579+0800  Enabling developer disk image services.
2024-12-03 16:24:18.637+0800  Acquired usage assertion.
Apps installed:
  - 0 elements

Command Completed, took 0.120 seconds
```

## ideviceinstaller

```bash
brew install ideviceinstaller
ideviceinstaller -l
```

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

---

## クイックスワイプ入力

*2024.12.01*

iOSで「threads」と入力したい場合、文字「threads」の位置を素早くなぞるだけで入力できます。実際の動作を見てみましょう。

<video width="50%" controls>
  <source src="/assets/images/input/in.mp4" type="video/mp4">
  お使いのブラウザはvideoタグに対応していません。
</video>

これは偶然見つけました。指で素早く入力エリアにタッチすると、線が表示されます。その意味がわからなかったので、実験してみたところ、上記の発見に至りました。
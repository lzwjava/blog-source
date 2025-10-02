---
audio: false
generated: false
image: true
lang: ja
layout: post
title: Pixel USB、iOS開発者ツール、スワイプタイピング
translated: true
---

### 目次

1. [PixelのUSBオプション](#pixels-usb-options)
   - Pixelをウェブカメラとして使用
   - 設定で開発者モードを有効にする
   - 接続のためにUSBデバッグをアクティブにする
   - ADBコマンドで接続を確認

2. [iOSの開発者モードとideviceinstaller](#developer-mode-of-ios-and-ideviceinstaller)
   - Xcode経由でインストールされているアプリを表示
   - スクリーンショットとログにXcodeを使用
   - xcrunコマンドでアプリを一覧表示
   - ideviceinstallerツールのインストールと使用

3. [クイックスワイプ入力](#quick-swipe-typing)
   - 文字の上をスワイプして単語を入力
   - 偶然発見された機能
   - 高速タッチ中に線が表示される


## PixelのUSBオプション

<div style="text-align: center;">  
    <img class="responsive" src="/assets/images/pixel/pixel.jpg" alt="Pixel" width="50%" />  
</div>

PixelはいくつかのUSBオプションを提供しており、特に興味深い機能の1つは、ウェブカメラとして機能する能力です。macOSでは、QuickTimeがAndroidウェブカメラをビデオソースとしてアクセスでき、シンプルで効果的なソリューションを提供します。

これを設定するには：

1. 設定で「電話について」に移動し、ビルド番号を7回タップして開発者モードを有効にします。
2. 開発者向けオプションを開き、USBデバッグを有効にします。
3. PixelをUSB経由でコンピューターに接続し、ターミナルで次のコマンドを実行して接続を確認します。
   ```bash
   adb devices
   ```

---

## iOSの開発者モードとideviceinstaller

*2024.12.03*

## 開発者モード

私はかつてしばらくiOS開発者でした。しかし、私のキャリアの焦点は他のテクノロジーに移りました。しかし、私は今プロのiOS開発者ではありませんが、iOS開発の知識を適用することは依然として非常に役立ちます。

最近、私はインストールしたアプリを共有したいと思いました。しかし、ホーム画面から、または設定のアプリリストからすべてのアプリのスクリーンショットを撮ると、めちゃくちゃになります。そのため、すべてのインストール済みアプリを見る方法を見つける必要がありました。

Xcodeを使ってインストールされているすべてのアプリを見る手順は以下の通りです：

1. iPhoneをUSB経由でMacに接続します
2. Xcodeを開きます
3. 「Window」→「Devices and Simulators」（またはShift + Cmd + 2を押す）に進みます
4. 左側のサイドバーからiPhoneを選択します
5. メインパネルで、「Installed Apps」セクションまでスクロールします

これには他にも便利な機能があります：

1. スクリーンショットを撮る
2. 最近のログを開く
3. コンソールを開く

## xcrun

```bash
(base) lzwjava@192 Downloads % xcrun devicectl device info apps --device 00008120-xxxx --verbose
Using verbose logging.
2024-12-03 16:24:18.579+0800 Enabling developer disk image services.
2024-12-03 16:24:18.637+0800 Acquired usage assertion.
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

iOSで「threads」と入力したい場合、文字「threads」の位置を素早く線でなぞるだけで結果が得られます。その仕組みを見てみましょう。

<video width="50%" controls>
  <source src="/assets/images/input/in.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

これを偶然発見しました。指が入力エリアを素早くタッチすると、線が表示されます。それが何を意味するのかは分かりません。いくつかの実験の後、上記の発見をしました。
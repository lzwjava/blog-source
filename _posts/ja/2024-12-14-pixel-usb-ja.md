---
audio: false
generated: false
image: true
lang: ja
layout: post
title: PixelのUSBオプション
translated: true
---

<div style="text-align: center;">  
    <img class="responsive" src="/assets/images/pixel/pixel.jpg" alt="Pixel" width="50%" />  
</div>

PixelはいくつかのUSBオプションを提供しており、特に興味深い機能の一つは、ウェブカメラとして機能する能力です。macOSでは、QuickTimeがAndroidのウェブカメラをビデオソースとしてアクセスできるため、シンプルで効果的なソリューションを提供します。

これを設定するには:

1. 設定から「端末情報」に移動し、「ビルド番号」を7回タップして開発者モードを有効にします。  
2. 「開発者向けオプション」を開き、USBデバッグを有効にします。  
3. PixelをUSBでコンピュータに接続し、ターミナルで以下のコマンドを実行して接続を確認します:  
   ```bash
   adb devices
   ```
---
audio: false
generated: true
lang: ja
layout: post
title: ブートセルモードでのRaspberry Pi Pico
translated: true
type: note
---

`Bus 001 Device 009: ID 2e8a:0003 Raspberry Pi RP2 Boot` と表示されているデバイスは、BOOTSELモードにあるRaspberry Pi Pico（または同様のRP2040ベースのボード）です。以下に詳細を示します：

- **ID 2e8a:0003**: これは、RP2040マイクロコントローラがBOOTSELモードにある時に、Raspberry Piに割り当てられたUSBベンダーID（2e8a）とプロダクトID（0003）です。
- **Raspberry Pi RP2 Boot**: このデバイスが、そのブートローダーモードに入ったRaspberry Pi Pico（またはPico W、カスタムボードなどの他のRP2040ベースのボード）であることを示します。このモードでは、デバイスはUSBマスストレージデバイスとして表示され、ファームウェア（例：.uf2ファイル）をドライブにコピーすることでアップロードできます。

### BOOTSELモードとは？
BOOTSELモードは、Raspberry Pi PicoのBOOTSELボタンを押しながらUSBポートに接続するか、ボタンを押しながらリセットすることで起動されます。このモードは、RP2040マイクロコントローラに新しいファームウェアやプログラムを書き込むために使用されます。このモードでは、Picoはコンピュータ上でリムーバブルドライブ（`RPI-RP2`という名前）として表示されます。

### なぜこのように表示されるのか？
お使いのデバイスがBOOTSELモードになっている可能性がある理由：
1. ファームウェアを更新または書き込むために、意図的にBOOTSELボタンを押した。
2. デバイスがプログラムを実行しておらず、ブートローダーモードにデフォルトでなっている（例：フラッシュの失敗後やリセット後）。
3. ファームウェアや接続に問題があり、ブートローダーモードのままになっている可能性がある。例えば、フラッシュメモリの問題や不適切なフラッシュ処理により、デバイスがこのモードに戻ることがある。[](https://forums.raspberrypi.com/viewtopic.php?p=2078375)

### 次に取るべき措置
- **ファームウェアを書き込みたい場合**: 有効な`.uf2`ファイル（例：MicroPythonやCircuitPythonのファームウェア、またはコンパイルされたプログラム）を`RPI-RP2`ドライブにコピーします。デバイスは自動的にファームウェアをフラッシュし、再起動してBOOTSELモードを終了します。[](https://forum.arduino.cc/t/solved-nano-rp2040-connect-does-not-accept-uf2/888152)
- **BOOTSELモードでスタックしている場合**: これはフラッシュメモリまたはファームウェアに問題があることを示している可能性があります。以下を試してください：
  1. 公式Raspberry Pi WebサイトのMicroPythonファームウェアなど、動作が確認されている`.uf2`ファイルで再フラッシュする。
  2. 故障したケーブルが問題を引き起こす可能性があるため、USBケーブルとポートを確認する。[](https://raspberrypi.stackexchange.com/questions/139506/raspberry-pi-pico-doesnt-create-tty-file)
  3. `picotool`のようなツールを使用して、デバイスの状態を確認したり、リセットしたりする。例えば、`picotool info`を実行してデバイスの状態を確認する。[](https://forums.raspberrypi.com/viewtopic.php?p=2078375)
  4. カスタムRP2040ボードを使用している場合、フラッシュチップが適切に接続および設定されていることを確認する。QSPI信号やフラッシュICの問題が正常なフラッシュを妨げる可能性がある。[](https://forums.raspberrypi.com/viewtopic.php?p=2078375)
- **BOOTSELモードを終了したい場合**: 有効なファームウェアが既にフラッシュされている場合は、デバイスのプラグを抜き、BOOTSELボタンが押されていないことを確認してから、再度接続します。デバイスはプログラムされたモード（例：MicroPythonスクリプトやCプログラムの実行）で起動するはずです。

### 追加の注意点
- RP2040は、Raspberry Pi Pico、Pico W、および他のボードで使用されているマイクロコントローラです。`RP2 Boot`という指定は、特にRP2040チップのブートローダーモードを指します。[](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html)
- Raspberry Pi Pico Wを使用している場合、ワイヤレス機能が含まれていますが、これらはBOOTSELモードではアクティブではありません。[](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html)
- エラーが発生した場合（例：`picotool`の検証またはロードの失敗）、ハードウェアの問題（故障したフラッシュチップやカスタムボードのはんだ付け問題）または破損したファームウェアファイルが原因である可能性があります。[](https://forums.raspberrypi.com/viewtopic.php?p=2078375)

具体的なヘルプ（例：ファームウェアのフラッシュ、トラブルシューティング、正確なボードの識別）が必要な場合は、お使いのセットアップや達成しようとしていることについての詳細を教えてください！
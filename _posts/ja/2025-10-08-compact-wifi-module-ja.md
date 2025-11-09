---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: コンパクトWiFiモジュール for IoT
translated: true
type: note
---

ESP-01Sは、Espressif SystemsのESP8266マイクロコントローラチップをベースにしたコンパクトなWiFiモジュールです。オリジナルのESP-01のアップグレード版であり、ArduinoやRaspberry Piのような他のマイクロコントローラに無線接続機能を追加する必要があるIoT（モノのインターネット）アプリケーションを主な目的として設計されています。

### 主な特徴:
- **WiFi機能**: 802.11 b/g/n規格をサポートし、スタンドアロンのWiFiアクセスポイント、ステーション、またはその両方として動作します。ネットワーク統合を容易にするためのTCP/IPプロトコルスタックを内蔵しています。
- **プロセッサとメモリ**: 80 MHz（160 MHzまでオーバークロック可能）で動作するTensilica L106 32ビットRISC CPUを搭載。コードとデータ保存用に1MB（バリアントによっては4MBの場合もある）のSPIフラッシュメモリを備えています。
- **I/Oピン**: シリアル通信（UART）およびLEDやリレーの切り替えなどの基本的なGPIO制御のための8ピンレイアウト（VCC, GND, CH_PD, RST, TX, RX, GPIO0, GPIO2）。
- **電源とサイズ**: 3.3Vで動作（5V耐性なし）、低消費電力（送信時約80mA）、サイズは約24.75 x 14.5 mmで、小型プロジェクトに理想的です。
- **ESP-01からの改良点**: WiFi信号強度を改善したより良いPCBレイアウト、より多くのフラッシュメモリ（512KB対1MB）、TXではなくGPIO2に配置された青色ステータスLED。

### 一般的な用途:
- センサーやデバイスをインターネットに接続し、遠隔監視/制御を実現。
- Arduino IDE（ESP8266ボードサポートを使用）またはシリアル経由のATコマンドによるプログラミング。
- WiFi対応スイッチや気象ステーションなどのスマートホームガジェットのプロトタイピング。

使い始めるには、組み込みUSBポートがないため、ファームウェア書き込み用にUSB-to-シリアル変換アダプタ（FTDIなど）が必要です。安価（5ドル未満）で広く入手可能ですが、ピンを損傷しないよう取り扱いには注意が必要です。

[ESP-01Sモジュールの使用方法](https://www.taydaelectronics.com/datasheets/files/ESP-01S.pdf)  
[ESP8266 ESP-01を使ってみる](https://www.instructables.com/Getting-Started-With-the-ESP8266-ESP-01/)  
[ESP-01S 紹介](https://lonelybinary.com/en-us/blogs/learn/what-is-esp-01s)  
[ESP-01S / ESP01S ESP8266 モジュール](https://hobbycomponents.com/esp8266/1176-esp-01s-esp01s-esp8266-module)
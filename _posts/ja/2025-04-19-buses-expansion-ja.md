---
audio: false
generated: true
lang: ja
layout: post
title: パート5：バスと拡張
translated: true
type: note
---

### 1. システムバス規格

#### システムバスとは

システムバスは、CPUとメモリ、周辺機器を接続する通信経路です。データ転送、アドレス信号、制御信号をこれらのコンポーネント間で仲介し、CPUがコンピュータシステムの他の部分と効率的に連携することを可能にします[^3]。

---

### 2. ISAバス概要

- **ISA (Industry Standard Architecture)** は、1980年代にIBM PC ATで導入された、最も初期のシステムバス規格の一つです。
- 4.77 MHzで動作する16ビットバスであり、最大約9 MB/sのデータ転送速度を実現します[^5]。
- ISAは複数の拡張カードをサポートし、各カードは独自の割り込み要求ラインを持ち、ネットワークカード、シリアルポート、ビデオカードなどのデバイス接続を可能にします。
- このバスは古い8ビットのPC XTシステムとの下位互換性があり、2つのエッジコネクタを1つのスロットに結合した98ピンコネクタを使用します。
- ISAは非同期信号方式とバスマスタリングを使用しますが、メインメモリの最初の16 MBにしか直接アクセスできません[^5]。
- 旧式のため、ISAはほぼ時代遅れですが、後続のバス設計の基礎として歴史的に重要です。

---

### 3. PCIバス概要

- **PCI (Peripheral Component Interconnect)** は、ISAの制限を克服するために設計された、より近代的な同期式パラレルバス規格です[^1][^3]。
- PCIバスは33 MHzで動作し、32ビットの多重化されたアドレス/データバスを備え、基本帯域幅は44から66 MB/sを提供します。
- 連続したメモリアクセスの場合、PCIはアドレスを再送信する必要なく1クロックサイクルごとに1つの32ビットワードを転送することで、最大132 MB/sを達成できます[^1]。
- PCIはCPUバスに接続するためにブリッジインターフェースを使用し、データをバッファリングしてメモリアクセスを最適化します。これにより、周辺機器との通信中もCPUはウェイト状態なしで実行を継続できます[^1]。
- PCIはバスマスタリングとDMA (Direct Memory Access) をサポートしており、デバイスがバスの制御を取得して直接データを転送できます。
- 帯域幅をさらに増加させる64ビット拡張版のPCIも存在します。
- PCIデバイスは、バス番号、デバイス番号、機能によって識別され、設定レジスタはベンダー、デバイスタイプ、メモリおよびI/Oアドレス、割り込みを指定します[^3]。
- PCIトランザクションはアドレスフェーズとデータフェーズを含み、メモリ読み書きやI/O読み書きなどの様々なコマンドをサポートします[^3]。

---

### 4. モダンなインターフェース技術

周辺機器通信は、パラレルバスよりもシンプルで柔軟なシリアルインターフェースへと移行しています。

---

#### USB (Universal Serial Bus)

- USBは、キーボード、マウス、ストレージデバイスなどの周辺機器を接続するために設計された、広く使用されている高速シリアルインターフェースです。
- プラグアンドプレイとホットスワップをサポートし、電源を落とさずにデバイスの接続と切断を可能にします。
- USBは階層型スター拓扑を採用し、1.5 Mbps (低速) から10 Gbps (USB 3.1以降) までのデータレートをサポートします。
- デバイスに電力を供給し、標準化されたプロトコルを持つ複数のデバイスクラスをサポートします。
- USBコントローラは、エンドポイントとパイプを使用してデータ転送を管理し、制御、バルク、インタラプト、アイソクロナスなどの異なる転送タイプをサポートします。

---

#### SPI (Serial Peripheral Interface)

- SPIは、センサー、EEPROM、ディスプレイなどの周辺デバイスとの短距離通信で一般的に使用される同期式シリアル通信バスです[^4]。
- 4つの信号を使用します: SCLK (クロック)、MOSI (マスタ出力・スレーブ入力)、MISO (マスタ入力・スレーブ出力)、CS (チップセレクト)。
- SPIは全二重通信であり、データの送信と受信を同時に行うことができます。
- シンプルで高速ですが、デバイスごとに1本のチップセレクトラインが必要なため、拡張性が制限される場合があります。
- SPIのモード設定には、クロック極性と位相が含まれ、これらはデータがいつサンプリングされシフトされるかを定義します[^6]。
- SPIは、組み込みシステムやマイクロコントローラアプリケーションで一般的に使用されます。

---

#### I²C (Inter-Integrated Circuit)

- I²Cは、マイクロコントローラとセンサーやEEPROMなどの周辺機器間の通信に使用される2線式シリアルバスです[^4]。
- 2つの双方向ラインを使用します: SDA (データ) と SCL (クロック)。
- I²Cは同じバス上で複数のマスタとスレーブをサポートし、デバイスは一意の7ビットまたは10ビットアドレスによって識別されます。
- 半二重通信をサポートし、オープンドレイン/オープンコレクタ出力とプルアップ抵抗を使用します。
- I²CはSPIよりも低速ですが、より少ないピン数で済み、配線がシンプルなマルチデバイス通信をサポートします。
- 標準的な速度は、100 kHz (標準モード)、400 kHz (高速モード)、および新しい仕様ではより高速なものもあります。

---

### 比較表: ISA vs PCI vs USB vs SPI vs I²C

| 特徴 | ISA | PCI | USB | SPI | I²C |
| :-- | :-- | :-- | :-- | :-- | :-- |
| バスタイプ | パラレル、非同期 | パラレル、同期 | シリアル、非同期 | シリアル、同期 | シリアル、同期 |
| データ幅 | 8 または 16 ビット | 32 または 64 ビット (多重化) | シリアル (1 ビット) | 1ビット/ライン、全二重 | 1ビット/ライン、半二重 |
| クロック速度 | 4.77 MHz | 33 MHz (基本 PCI) | 最大 10 Gbps (USB 3.1) | 通常 数 MHz まで | 通常 400 kHz+ まで |
| 最大帯域幅 | ~9 MB/s | 44-132 MB/s | USB バージョンにより異なる | クロック速度に依存 | SPI より低い |
| 配線数 | 多数 (アドレス、データ、制御) | 多数 (多重化ライン) | 4本 (電源、グランド、D+, D-) | 4本 (SCLK, MOSI, MISO, CS) | 2本 (SDA, SCL) |
| デバイスアドレス指定 | スロットベース | バス/デバイス/機能番号 | デバイス列挙 | デバイスごとのチップセレクト | アドレス指定されたデバイス |
| 典型的な使用例 | レガシー拡張カード | モダンな拡張カード | 外部周辺機器 | 組み込み周辺機器 | 組み込み周辺機器 |
| バスマスタリング | あり | あり | ホストコントローラ管理 | マスタ/スレーブ | マルチマスタ対応 |

---

### SPIとI²C使用に関する実践的注意点

- Raspberry Piのようなプラットフォームでは、SPIおよびI²Cインターフェースはデフォルトでは有効になっておらず、システム設定 (例: `raspi-config`) による設定が必要です[^4]。
- `wiringPi`、`spidev` (SPI用)、`smbus` (I²C用) などのライブラリは、これらのバス上のデバイスと通信するためのC/C++およびPythonでのプログラミングインターフェースを提供します。
- SPIの設定には、モード (クロック極性と位相)、ビット順序 (MSBまたはLSBファースト)、正しいチップセレクトピンの選択が含まれます[^6]。
- I²C通信には、デバイスアドレスの指定と、データ転送のためのスタート/ストップ条件の処理が含まれます。

---

このチュートリアルは、システムバスとモダンな周辺機器インターフェースの基本概念と実践的な側面を概説し、マイクロコンピュータのバスアーキテクチャと拡張技術を理解するための強固な基礎を提供します。

<div style="text-align: center">⁂</div>

[^1]: https://people.ece.ubc.ca/~edc/464/lectures/lec17.pdf

[^2]: https://spotpear.com/wiki/USB-TO-UART-I2C-SPI-JTAG-Wiki.html

[^3]: https://home.mit.bme.hu/~rtamas/rendszerarchitekturak/eloadas/08_bus_introduction.pdf

[^4]: https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial/all

[^5]: https://www.techtarget.com/searchwindowsserver/definition/ISA-Industry-Standard-Architecture

[^6]: https://www.ratocsystems.com/english/download/pdffiles/usb61_e_10.pdf

[^7]: https://webstor.srmist.edu.in/web_assets/srm_mainsite/files/files/PCI.pdf

[^8]: https://www.infineon.com/dgdl/Infineon-USB-Serial_VCP_I2CSPI_API_Guide-Software-v01_00-EN.pdf?fileId=8ac78c8c7d0d8da4017d0f6a8b015fe6\&da=t

[^9]: https://network.nvidia.com/pdf/whitepapers/PCI_3GIO_IB_WP_120.pdf

[^10]: https://people.scs.carleton.ca/~sivarama/org_book/org_book_web/slides/chap_1_versions/ch5_1.pdf

[^11]: https://www.youtube.com/watch?v=BBobCtfOjbM

[^12]: https://www.sciencedirect.com/topics/engineering/peripheral-component-interconnect-bus

[^13]: http://mcatutorials.com/mca-tutorials-bus-standards-and-types.php

[^14]: https://www.youtube.com/watch?v=YRJ9gWaxfJY

[^15]: https://docs.nxp.com/bundle/UM12018/page/topics/connecting_to_a_target_through_a_usb-to-spi_or_usb.html

[^16]: https://www.i2ctools.com/Downloads/USBtoI2Cpro/USB-to-SPI_Software_Users_Manual.pdf

[^17]: https://www.youtube.com/watch?v=WIIR77fCHYc

[^18]: https://ftdichip.com/wp-content/uploads/2021/08/AN_255_USB-to-I2C-Example-using-the-FT232H-and-FT201X-devices.pdf

[^19]: https://www.youtube.com/watch?v=IyGwvGzrqp8
---
audio: false
generated: true
lang: ja
layout: post
title: UbuntuでのRaspberry Pi Picoセットアップ
translated: true
type: note
---

**Raspberry Pi Pico** を **Ubuntu** で使用するには、開発環境をセットアップし、必要なソフトウェアをインストールし、Pico をプログラムするためのツールを設定する必要があります。Pico は **MicroPython**、**C/C++**、または **CircuitPython** でのプログラミングをサポートしています。以下では、それぞれのアプローチに必要な手順とソフトウェアを、最も一般的なセットアップに焦点を当てて概説します。

### 一般的な前提条件
- **Raspberry Pi Pico** (または Pico W) と USB ケーブル (Pico は Micro-USB、Pico 2 は USB-C)。
- **Ubuntu** システム (例: Ubuntu 20.04, 22.04 以降。これらの説明は 24.04 のような最近のバージョンを想定しています)。
- ターミナルの基本的な知識。

### オプション 1: MicroPython でのプログラミング
MicroPython は、Pico をプログラムする最も初心者向けの方法です。これはマイクロコントローラ向けに設計された軽量な Python 実装です。

#### インストールするソフトウェア
1.  **MicroPython ファームウェア**
    - [公式 MicroPython ウェブサイト](https://micropython.org/download/rp2-pico/) または [Raspberry Pi Pico ページ](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html) から、Raspberry Pi Pico 用の最新の MicroPython UF2 ファームウェアファイルをダウンロードします。
    - Pico W または Pico 2 の場合は、適切なファームウェア (例: Pico W 用の `rp2-pico-w`) を選択してください。

2.  **Python 3**
    - Ubuntu には通常、Python 3 がデフォルトで含まれています。以下で確認します:
      ```bash
      python3 --version
      ```
    - インストールされていない場合は、インストールします:
      ```bash
      sudo apt update
      sudo apt install python3 python3-pip
      ```

3.  **Thonny IDE** (初心者におすすめ)
    - Thonny は、MicroPython で Pico をプログラムするためのシンプルな IDE です。
    - Thonny をインストールします:
      ```bash
      sudo apt install thonny
      ```
    - または、`pip` を使用して最新バージョンをインストールします:
      ```bash
      pip3 install thonny
      ```

4.  **オプション: `picotool` (高度な管理用)**
    - MicroPython ファームウェアの管理や Pico の検査に便利です。
    - `picotool` をインストールします:
      ```bash
      sudo apt install picotool
      ```

#### セットアップ手順
1.  **MicroPython ファームウェアのインストール**
    - **BOOTSEL** ボタンを押しながら Pico を Ubuntu マシンに USB で接続します (これにより Pico がブートローダーモードになります)。
    - Pico は USB ストレージデバイス (例: `RPI-RP2`) として表示されます。
    - ダウンロードした MicroPython の `.uf2` ファイルを Pico のストレージにドラッグ＆ドロップします。Pico は自動的に再起動し、MicroPython がインストールされます。

2.  **Thonny の設定**
    - ターミナルで `thonny` を実行するか、アプリケーションメニューから Thonny を開きます。
    - **ツール > オプション > インタープリタ** に移動します。
    - インタープリタとして **MicroPython (Raspberry Pi Pico)** を選択します。
    - 正しいポート (例: `/dev/ttyACM0`) を選択します。必要に応じて、ターミナルで `ls /dev/tty*` を実行してポートを特定します。
    - Thonny が Pico に接続され、Python スクリプトを記述して実行できるようになります。

3.  **プログラムのテスト**
    - Thonny で、簡単なスクリプトを記述します。例:
      ```python
      from machine import Pin
      led = Pin(25, Pin.OUT)  # オンボード LED (Pico は GP25)
      led.toggle()  # LED のオン/オフを切り替え
      ```
    - **Run** ボタンをクリックして、コードを Pico で実行します。

4.  **オプション: `picotool` の使用**
    - Pico のステータスを確認します:
      ```bash
      picotool info
      ```
    - 必要に応じて、Pico が接続されブートローダーモードであることを確認します。

### オプション 2: C/C++ でのプログラミング
より上級ユーザー向けに、Pico は公式の **Pico SDK** を使用して C/C++ でプログラムできます。

#### インストールするソフトウェア
1.  **Pico SDK とツールチェーン**
    - C/C++ プログラムをビルドするための必要なツールをインストールします:
      ```bash
      sudo apt update
      sudo apt install cmake gcc-arm-none-eabi libnewlib-arm-none-eabi build-essential git
      ```

2.  **Pico SDK**
    - Pico SDK リポジトリをクローンします:
      ```bash
      git clone -b master https://github.com/raspberrypi/pico-sdk.git
      cd pico-sdk
      git submodule update --init
      ```
    - `PICO_SDK_PATH` 環境変数を設定します:
      ```bash
      export PICO_SDK_PATH=~/pico-sdk
      echo 'export PICO_SDK_PATH=~/pico-sdk' >> ~/.bashrc
      ```

3.  **オプション: Pico の例**
    - 参考のために Pico の例をクローンします:
      ```bash
      git clone -b master https://github.com/raspberrypi/pico-examples.git
      ```

4.  **Visual Studio Code (オプション)**
    - より良い開発体験のために VS Code をインストールします:
      ```bash
      sudo snap install code --classic
      ```
    - VS Code で **CMake Tools** と **C/C++** 拡張機能をインストールします。

#### セットアップ手順
1.  **プロジェクトのセットアップ**
    - 新しいプロジェクト用のディレクトリを作成します (例: `my-pico-project`)。
    - `pico-examples` からサンプルの `CMakeLists.txt` をコピーするか、新しく作成します:
      ```cmake
      cmake_minimum_required(VERSION 3.13)
      include($ENV{PICO_SDK_PATH}/pico_sdk_init.cmake)
      project(my_project C CXX ASM)
      pico_sdk_init()
      add_executable(my_project main.c)
      pico_add_extra_outputs(my_project)
      target_link_libraries(my_project pico_stdlib)
      ```
    - 簡単な C プログラム (例: `main.c`) を記述します:
      ```c
      #include "pico/stdlib.h"
      int main() {
          const uint LED_PIN = 25;
          gpio_init(LED_PIN);
          gpio_set_dir(LED_PIN, GPIO_OUT);
          while (true) {
              gpio_put(LED_PIN, 1);
              sleep_ms(500);
              gpio_put(LED_PIN, 0);
              sleep_ms(500);
          }
      }
      ```

2.  **ビルドと書き込み**
    - プロジェクトディレクトリに移動します:
      ```bash
      cd my-pico-project
      mkdir build && cd build
      cmake ..
      make
      ```
    - これにより `.uf2` ファイル (例: `my_project.uf2`) が生成されます。
    - Pico の **BOOTSEL** ボタンを押しながら USB で接続し、`.uf2` ファイルを Pico のストレージにコピーします:
      ```bash
      cp my_project.uf2 /media/$USER/RPI-RP2/
      ```

3.  **デバッグ (オプション)**
    - デバッグ用に `openocd` をインストールします:
      ```bash
      sudo apt install openocd
      ```
    - デバッガ (例: デバッグプローブとして別の Pico) を使用し、以下を実行します:
      ```bash
      openocd -f interface/raspberrypi-swd.cfg -f target/rp2040.cfg
      ```

### オプション 3: CircuitPython でのプログラミング
CircuitPython は、MicroPython に似た別の Python ベースのオプションですが、Adafruit のエコシステムに焦点を当てています。

#### インストールするソフトウェア
1.  **CircuitPython ファームウェア**
    - [Adafruit CircuitPython ウェブサイト](https://circuitpython.org/board/raspberry_pi_pico/) から Pico 用の CircuitPython UF2 ファイルをダウンロードします。
    - Pico W または Pico 2 の場合は、適切なファームウェアを選択してください。

2.  **Python 3 とツール**
    - MicroPython と同じです (Python 3, Thonny など)。

#### セットアップ手順
1.  **CircuitPython ファームウェアのインストール**
    - MicroPython と同様です: **BOOTSEL** を押しながら Pico を接続し、CircuitPython の `.uf2` ファイルを Pico のストレージにコピーします。
    - Pico は `CIRCUITPY` という名前の USB ドライブとして再起動します。

2.  **Thonny またはテキストエディタでのプログラミング**
    - MicroPython のセクションで説明したように、Thonny を使用し、インタープリタとして **CircuitPython** を選択します。
    - または、任意のテキストエディタを使用して `CIRCUITPY` ドライブ上の `code.py` を直接編集します。
    - `code.py` の例:
      ```python
      import board
      import digitalio
      import time
      led = digitalio.DigitalInOut(board.LED)
      led.direction = digitalio.Direction.OUTPUT
      while True:
          led.value = True
          time.sleep(0.5)
          led.value = False
          time.sleep(0.5)
      ```

### 追加の注意点
- **権限**: Pico のポート (例: `/dev/ttyACM0`) にアクセスできない場合は、ユーザーを `dialout` グループに追加します:
  ```bash
  sudo usermod -a -G dialout $USER
  ```
  適用するには、ログアウトして再度ログインします。

- **Pico W の考慮事項**: Pico W の場合は、それ専用のファームウェア (例: Wi-Fi サポート付きの MicroPython) を使用していることを確認してください。Wi-Fi プログラミングには、MicroPython 用の `network` のような追加のライブラリが必要です。

- **Pico 2**: 新しい Raspberry Pi Pico 2 (RP2350 搭載) では、更新されたファームウェアまたは SDK バージョンが必要な場合があります。互換性については公式の Raspberry Pi ドキュメントを確認してください。

- **トラブルシューティング**:
  - Pico がブートローダーモードで表示されない場合は、USB ケーブル (給電専用ではなくデータ通信をサポートするもの) を再確認してください。
  - `lsusb` または `dmesg` を実行して、Pico が Ubuntu によって検出されていることを確認します。
  - C/C++ ビルドの場合、Pico SDK のパスが正しく設定されていることを確認します。

### 推奨アプローチ
- **初心者向け**: シンプルさと簡単なセットアップのために、**Thonny を使った MicroPython** を使用します。
- **上級ユーザー向け**: パフォーマンスと低レベル制御のために、**Pico SDK を使った C/C++** を使用します。
- **Adafruit エコシステムユーザー向け**: Adafruit のライブラリやハードウェアを使用する予定がある場合は、**CircuitPython** を使用します。

特定のプロジェクトやプログラミングの好みがあれば、お知らせください。さらに手順を調整できます！
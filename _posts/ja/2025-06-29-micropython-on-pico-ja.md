---
audio: false
generated: true
lang: ja
layout: post
title: PicoへのMicroPythonのアップロード
translated: true
type: note
---

MicroPythonをRaspberry Pi Picoに書き込んだ後（前述の`.uf2`ファイルを使用）、Thonny IDEのようなツールを使って簡単なMicroPythonプログラムをアップロードして実行できます。Thonnyは初心者向けで、MicroPython開発に広く使用されています。以下はMicroPythonのセットアップとPicoへの簡単なプログラムのアップロード手順です。

---

### 前提条件
1. **MicroPythonの書き込み済み**: `RPI_PICO-20250415-v1.25.0.uf2`を`RPI-RP2`ドライブにコピー済みで、Picoが再起動していること（`RPI-RP2`ドライブは表示されなくなっているはず）。
2. **USB接続**: Picoがデータ転送対応のUSBケーブルでコンピュータに接続されていること。
3. **Thonny IDE**: 未インストールの場合はThonnyをインストール：
   - **Linux**: パッケージマネージャーでインストール、または[thonny.org](https://thonny.org)からダウンロード。
     ```bash
     sudo apt update
     sudo apt install thonny
     ```
   - または`pip`を使用：
     ```bash
     pip install thonny
     ```
   - Windows/macOSは[thonny.org](https://thonny.org)からダウンロードしてインストール。

---

### 簡単なMicroPythonプログラムのアップロード手順

1. **Picoの接続とThonnyの起動**:
   - PicoをコンピュータのUSBポートに接続。
   - Thonny IDEを開く。

2. **ThonnyのMicroPython設定**:
   - Thonnyで**Tools > Options > Interpreter**（または**Run > Select interpreter**）を選択。
   - インタプリタのドロップダウンから**MicroPython (Raspberry Pi Pico)**を選択。
   - Picoのシリアルポート（例: Linuxでは`/dev/ttyACM0`）が自動表示されない場合：
     - ドロップダウンで利用可能なポートを確認、またはターミナルで`ls /dev/tty*`を実行してPicoのポートを特定（通常`/dev/ttyACM0`など）。
     - 正しいポートを手動で選択。
   - **OK**をクリックして保存。

3. **MicroPythonの動作確認**:
   - Thonnyの**Shell**（下部パネル）にMicroPython REPLプロンプトが表示されるはず：
     ```
     >>> 
     ```
   - 簡単なコマンドでテスト、例：
     ```python
     print("Hello, Pico!")
     ```
     Enterを押すと、Shellに出力が表示される。

4. **簡単なMicroPythonプログラムの作成**:
   - Thonnyのメインエディタで新規ファイルを作成し、簡単なプログラムを記述。例：PicoのオンボードLEDを点滅させるプログラム（PicoはGPIO 25、Pico Wは"LED"を使用）：
     ```python
     from machine import Pin
     import time

     # オンボードLEDの初期化
     led = Pin(25, Pin.OUT)  # Pico Wの場合は25の代わりに"LED"を使用

     # LEDの点滅
     while True:
         led.on()           # LEDを点灯
         time.sleep(0.5)    # 0.5秒待機
         led.off()          # LEDを消灯
         time.sleep(0.5)    # 0.5秒待機
     ```
   - 注：Pico Wを使用する場合は`Pin(25, Pin.OUT)`を`Pin("LED", Pin.OUT)`に置き換え。

5. **プログラムをPicoに保存**:
   - **File > Save As**をクリック。
   - ダイアログで保存先として**Raspberry Pi Pico**を選択（コンピュータではない）。
   - ファイル名を`main.py`（MicroPythonは起動時に`main.py`を自動実行）または`blink.py`などに設定。
   - **OK**をクリックしてPicoのファイルシステムに保存。

6. **プログラムの実行**:
   - Thonnyで緑色の**Run**ボタン（または**F5**キー）をクリックしてプログラムを実行。
   - または、`main.py`として保存した場合は、Picoをリセット（抜き差し、またはRESETボタン押下）するとプログラムが自動実行。
   - オンボードLEDが0.5秒間隔で点滅するはず。

7. **プログラムの停止**（必要時）:
   - 実行中のスクリプトを中断するには、ThonnyのShellで**Ctrl+C**を押す。
   - 自動実行される`main.py`を削除するには：
     - Thonnyで**View > Files**を選択、Picoのファイルシステムを選択し、`main.py`を右クリックして**Delete**を選択。

---

### テストとトラブルシューティング
- **REPLプロンプトが表示されない**:
  - インタプリタ設定で正しいポートが選択されているか確認。
  - MicroPythonが正しく書き込まれているか確認。問題あれば前述の手順で`.uf2`ファイルを再書き込み。
  - USBケーブル（データ通信対応）とポートを確認、別のポートを試す。
- **LEDが点滅しない**: 正しいGPIOピンを使用しているか確認（Picoは`25`、Pico Wは`"LED"`）。それでも動作しない場合はREPLコマンドでLEDをテスト：
  ```python
  from machine import Pin
  led = Pin(25, Pin.OUT)
  led.on()
  ```
- **ファイルが保存できない**: ThonnyがPicoに接続され、インタプリタがMicroPython (Raspberry Pi Pico)に設定されているか確認。

---

### 追加のヒント
- **他のツールの使用**: Thonny以外に`rshell`や`ampy`でPicoのファイルを管理可能：
  ```bash
  pip install rshell
  rshell --port /dev/ttyACM0
  cp blink.py /pyboard/main.py
  ```
- **その他のサンプルプログラム**:
  - ボタン押下の読み取り（例：GPIO 14）：
    ```python
    from machine import Pin
    button = Pin(14, Pin.IN, Pin.PULL_UP)
    while True:
        print(button.value())
    ```
  - GPIOピン番号を調整して外部LEDや他の周辺機器を制御。
- **自動実行**: ファイルを`main.py`として保存すると起動時に自動実行。`boot.py`は`main.py`の前に実行されるセットアップコード用。

特定の問題（ポート検出、Thonnyでのエラー、ハードウェア問題など）が発生した場合、または別のプログラムを試したい場合は、お知らせください。さらに詳しく案内します！
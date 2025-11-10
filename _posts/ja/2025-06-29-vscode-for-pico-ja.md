---
audio: false
generated: true
lang: ja
layout: post
title: Raspberry Pi Pico MicroPython用VSCode
translated: true
type: note
---

はい、Visual Studio Code（VSCode）を使用して、Thonnyと同様にRaspberry Pi PicoでMicroPythonプログラムを記述、アップロード、実行できます。VSCodeは強力なエディタであり、適切な拡張機能とツールを使用することで、MicroPython開発を効果的に扱うことができます。以下は、MicroPythonが既にフラッシュされていることを前提に（`.uf2`ファイルで行ったように）、簡単なMicroPythonプログラムをPicoにアップロードするためにVSCodeをセットアップするステップバイステップガイドです。

---

### 前提条件
1. **MicroPythonのフラッシュ**: PicoにMicroPythonがインストールされていること（例: `RPI_PICO-20250415-v1.25.0.uf2`ファイルから）。
2. **VSCodeのインストール**: まだの場合、[code.visualstudio.com](https://code.visualstudio.com)からVSCodeをダウンロードしてインストールしてください。
3. **Pythonのインストール**: MicroPythonツールに必要なPythonをインストールします:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```
4. **USB接続**: Picoがデータ転送可能なUSBケーブルでコンピュータに接続されていること。

---

### VSCodeでRaspberry Pi Pico用MicroPythonを使用するステップバイステップガイド

1. **必要なVSCode拡張機能のインストール**:
   - VSCodeを開きます。
   - 拡張機能ビュー（`Ctrl+Shift+X`またはmacOSでは`Cmd+Shift+X`）に移動します。
   - 以下の拡張機能をインストールします:
     - **Python** (Microsoft提供): PythonおよびMicroPythonのシンタックスハイライトとIntelliSense用。
     - **Pico-W-Go** (任意ですが推奨): Raspberry Pi PicoでのMicroPython開発用の専用拡張機能。「Pico-W-Go」を検索してインストールします。
       - 注: Pico-W-Goはファイル転送とREPLアクセスを簡素化しますが、追加のセットアップが必要です（後述）。
     - または、手動制御を希望する場合は、**Remote-SSH**や**Serial Monitor**などの汎用拡張機能を使用できます。

2. **Pico-W-Goのセットアップ（推奨）**:
   - **依存関係のインストール**: Pico-W-Goには`pyserial`と`esptool`が必要です。pip経由でインストールします:
     ```bash
     pip3 install pyserial esptool
     ```
   - **Pico-W-Goの設定**:
     - VSCodeのコマンドパレット（`Ctrl+Shift+P`または`Cmd+Shift+P`）を開きます。
     - **Pico-W-Go > Configure Project**を入力して選択します。
     - プロンプトに従ってプロジェクトをセットアップします:
       - Picoのシリアルポート（例: `/dev/ttyACM0`）を選択します。ターミナルで`ls /dev/tty*`を実行して見つけます。
       - インタプリタとしてMicroPythonを選択します。
       - 新しいプロジェクトフォルダを作成するか、既存のものを使用します。
     - Pico-W-Goは`.picowgo`設定ファイルを含むワークスペースを作成します。

3. **簡単なMicroPythonプログラムの記述**:
   - VSCodeで、プロジェクトフォルダ内に新しいファイル（例: `main.py`）を作成します。
   - オンボードLEDを点滅させる簡単なプログラムを記述します:
     ```python
     from machine import Pin
     import time

     led = Pin(25, Pin.OUT)  # Pico Wの場合は "LED" を使用
     while True:
         led.on()
         time.sleep(0.5)
         led.off()
         time.sleep(0.5)
     ```
   - ファイルを保存します（`Ctrl+S`または`Cmd+S`）。

4. **プログラムをPicoにアップロード**:
   - **Pico-W-Goを使用**:
     - Picoが接続され、正しいポートが選択されていることを確認します（必要に応じて`Pico-W-Go > Configure Project`で確認）。
     - コマンドパレット（`Ctrl+Shift+P`）を開きます。
     - **Pico-W-Go > Upload Project to Pico**を選択します。
     - これにより、プロジェクトフォルダ内のすべてのファイル（例: `main.py`）がPicoのファイルシステムにアップロードされます。
     - ファイルを`main.py`と命名した場合、起動時に自動的に実行されます。
   - **`rshell`を使用した手動アップロード** (Pico-W-Goを使用しない場合):
     - `rshell`をインストール:
       ```bash
       pip3 install rshell
       ```
     - Picoに接続:
       ```bash
       rshell --port /dev/ttyACM0
       ```
     - ファイルをPicoにコピー:
       ```bash
       cp main.py /pyboard/main.py
       ```
     - `exit`で`rshell`を終了。

5. **プログラムの実行とテスト**:
   - **Pico-W-Goを使用**:
     - コマンドパレットを開き、**Pico-W-Go > Run**を選択します。
     - これにより、現在のファイルが実行されるか、手動コマンド用にREPLが開きます。
     - 上記の例を使用している場合、LEDが点滅しているのが見えるはずです。
   - **VSCodeのターミナルまたはREPLを使用**:
     - Pico-W-GoでREPLを開く（`Pico-W-Go > Open REPL`）か、`rshell`を使用:
       ```bash
       rshell --port /dev/ttyACM0 repl
       ```
     - コマンドを直接テスト、例:
       ```python
       from machine import Pin
       led = Pin(25, Pin.OUT)
       led.on()
       ```
     - REPLで実行中のプログラムを停止するには`Ctrl+C`を押します。
   - ファイルが`main.py`の場合、Picoをリセット（抜き差し、またはRESETボタンを押す）して自動実行します。

6. **デバッグとファイル管理**:
   - **Pico-W-Go**: **Pico-W-Go > Download Project from Pico**を使用してPicoからファイルを取得するか、**Pico-W-Go > Delete All Files**でファイルシステムをクリアします。
   - **rshell**: 以下のコマンドでファイルをリスト:
     ```bash
     rshell ls /pyboard
     ```
     ファイルを削除:
     ```bash
     rshell rm /pyboard/main.py
     ```
   - VSCodeのターミナルまたはREPLでプログラムの出力を確認します。

---

### 代替案: Pico-W-Goを使用しない手動ワークフロー
Pico-W-Goを使用したくない場合は、MicroPython開発を手動で管理できます:
1. VSCodeでコードを記述し、`main.py`として保存します。
2. `ampy`（別のMicroPythonツール）を使用してアップロード:
   ```bash
   pip3 install adafruit-ampy
   ampy --port /dev/ttyACM0 put main.py
   ```
3. `minicom`や`screen`などのターミナルツールでREPLにアクセス:
   ```bash
   screen /dev/ttyACM0 115200
   ```
   `Ctrl+C`を押して実行中のプログラムを停止し、REPLに入ります。

---

### トラブルシューティング
- **ポートが見つからない**: `ls /dev/tty*`を実行してPicoのポート（例: `/dev/ttyACM0`）を確認してください。Picoが接続され、MicroPythonがフラッシュされていることを確認してください。
- **Pico-W-Goエラー**: `pyserial`と`esptool`がインストールされ、正しいポートが選択されていることを確認してください。必要に応じてVSCodeを再起動します。
- **プログラムが実行されない**: 自動実行のためにファイルが`main.py`として保存されていることを確認するか、REPLまたは`ampy run main.py`経由で手動で実行してください。
- **LEDが点滅しない**: GPIOピン（Picoは`25`、Pico Wは`"LED"`）を確認してください。REPLでテスト:
  ```python
  from machine import Pin
  led = Pin(25, Pin.OUT)
  led.on()
  ```

---

### Thonnyに対するVSCodeの利点
- 優れたコード編集機能（IntelliSense、Git統合、カスタマイズ可能なワークフローなど）。
- 複数ファイルを含む大規模なプロジェクトをサポート。
- Pico-W-GoはThonnyのような体験を提供しつつ、VSCodeの強力な機能を活用。

### 制限事項
- セットアップはThonnyより少し複雑。
- REPL統合は、Thonnyのオールインワンインターフェースと比べてややシームレスさに欠ける場合がある。

特定のVSCode設定、ツールのインストール、またはより複雑なMicroPythonプログラムの記述に関するヘルプが必要な場合は、お知らせください！
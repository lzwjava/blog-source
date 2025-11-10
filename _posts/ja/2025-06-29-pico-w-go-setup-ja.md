---
audio: false
generated: true
lang: ja
layout: post
title: VSCode Pico W Go for MicroPython
translated: true
type: note
---

**Raspberry Pi Pico**拡張機能をVisual Studio Code（VSCode）で使用することは、Raspberry Pi PicoでのMicroPython開発において優れた選択肢です。Thonnyと同様に合理化されたワークフローを、VSCodeの強力な編集環境内で提供します。おそらく言及されている拡張機能は**Pico-W-Go**（または**Pico-Go**のような類似の拡張機能）であり、これはRaspberry Pi PicoおよびPico WのMicroPython開発に特化して設計されています。以下では、（MicroPythonが既にフラッシュされている（使用した`RPI_PICO-20250415-v1.25.0.uf2`ファイルから）ことを前提に、**Pico-W-Go**拡張機能（最も人気がありメンテナンスされているオプション）をセットアップして使用し、簡単なMicroPythonプログラムをPicoにアップロードする手順を説明します。

---

### 前提条件
1.  **MicroPythonがフラッシュ済み**: お使いのPicoにMicroPythonがインストール済み（既にフラッシュ済み）。
2.  **VSCodeがインストール済み**: VSCodeがインストールされていることを確認してください（[code.visualstudio.com](https://code.visualstudio.com)）。
3.  **Pythonがインストール済み**: Pico-W-Goの依存関係に必要です:
    ```bash
    sudo apt update
    sudo apt install python3 python3-pip
    ```
4.  **USB接続**: Picoがデータ転送対応のUSBケーブルで接続されていること。

---

### VSCodeでRaspberry Pi Pico（Pico-W-Go）拡張機能を使用するステップバイステップガイド

1.  **Pico-W-Go拡張機能をインストール**:
    *   VSCodeを開きます。
    *   拡張機能ビュー（`Ctrl+Shift+X`またはmacOSでは`Cmd+Shift+X`）に移動します。
    *   **Pico-W-Go**を検索し、インストールします（Paul Obermeier他によって開発）。
    *   注意: 別の拡張機能（例: Pico-Go）を意味していた場合はお知らせください。ただし、Pico MicroPython開発ではPico-W-Goが最も一般的に使用されています。

2.  **Pico-W-Goの依存関係をインストール**:
    *   Pico-W-Goはシリアル通信とフラッシュのために`pyserial`と`esptool`を必要とします:
      ```bash
      pip3 install pyserial esptool
      ```
    *   これらがPython環境にインストールされていることを確認してください（`pip3 list`で確認）。

3.  **Pico-W-Goを設定**:
    *   VSCodeでコマンドパレット（`Ctrl+Shift+P`または`Cmd+Shift+P`）を開きます。
    *   **Pico-W-Go > Configure Project**と入力して選択します。
    *   プロンプトに従います:
        *   **Serial Port**: Picoのポート（例: `/dev/ttyACM0`）を選択します。次を実行して見つけます:
          ```bash
          ls /dev/tty*
          ```
          Picoが接続されると表示される`/dev/ttyACM0`または類似のものを探します。
        *   **Interpreter**: MicroPython (Raspberry Pi Pico)を選択します。
        *   **Project Folder**: プロジェクト用のフォルダを選択または作成します（例: `~/PicoProjects/MyProject`）。
    *   Pico-W-Goはプロジェクトフォルダ内に設定を保存する`.picowgo`設定ファイルを作成します。

4.  **簡単なMicroPythonプログラムを書く**:
    *   VSCodeでプロジェクトフォルダを開きます（ファイル > フォルダを開く）。
    *   `main.py`という名前の新しいファイルを作成します（MicroPythonは起動時に`main.py`を自動実行します）。
    *   オンボードLEDを点滅させる簡単なプログラムを追加します:
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
    *   ファイルを保存します（`Ctrl+S`）。

5.  **プログラムをPicoにアップロード**:
    *   Picoが接続されており、正しいポートが選択されていることを確認します（必要に応じて**Pico-W-Go > Configure Project**を再実行）。
    *   コマンドパレット（`Ctrl+Shift+P`）を開きます。
    *   **Pico-W-Go > Upload Project to Pico**を選択します。
        *   これにより、プロジェクトフォルダ内のすべてのファイル（例: `main.py`）がPicoのファイルシステムにアップロードされます。
    *   代替として、単一ファイルをアップロードするには:
        *   VSCodeのファイルエクスプローラーで`main.py`を右クリックします。
        *   **Pico-W-Go > Upload File to Pico**を選択します。
    *   ファイルがPicoに転送され、`main.py`の場合、起動時に自動実行されます。

6.  **プログラムを実行してテスト**:
    *   **自動実行**: `main.py`をアップロードした場合、Picoをリセットします（抜き差しするか、利用可能な場合はRESETボタンを押す）。LEDが点滅し始めるはずです。
    *   **手動実行**:
        *   コマンドパレットを開き、**Pico-W-Go > Run**を選択します。
        *   これにより、現在のファイルがPico上で実行されます。
    *   **REPLを使用**:
        *   コマンドパレットを開き、**Pico-W-Go > Open REPL**を選択します。
        *   REPLがVSCodeのターミナルに表示され、コマンドをテストできます:
          ```python
          from machine import Pin
          led = Pin(25, Pin.OUT)
          led.on()
          ```
        *   REPLで実行中のプログラムを停止するには`Ctrl+C`を押します。

7.  **Pico上のファイルを管理**:
    *   **ファイル一覧表示**: **Pico-W-Go > Download Project from Pico**を使用して、Picoのファイルシステムからファイルを表示または取得します。
    *   **ファイル削除**: コマンドパレットを開き、**Pico-W-Go > Delete All Files**を選択してPicoのファイルシステムをクリアするか、REPLを使用します:
      ```python
      import os
      os.remove('main.py')
      ```
    *   **出力を確認**: プログラムの出力（例: `print`文）は、REPLまたは設定されたVSCodeのターミナルに表示されます。

---

### トラブルシューティング
*   **ポートが検出されない**:
    *   `ls /dev/tty*`を実行してPicoのポート（例: `/dev/ttyACM0`）を確認します。
    *   USBケーブルがデータ転送をサポートしていることを確認し、別のポートを試します。
    *   **Pico-W-Go > Configure Project**でポートを再設定します。
*   **アップロードが失敗する**:
    *   `pyserial`と`esptool`がインストールされていることを確認します（`pip3 list`）。
    *   MicroPythonが実行されていることを確認します（REPLにアクセスできるはず）。
    *   必要に応じて、BOOTSELモードに再入し、`.uf2`ファイルをコピーしてMicroPythonを再フラッシュします。
*   **LEDが点滅しない**:
    *   正しいGPIOピン（Picoは`25`、Pico Wは`"LED"`）を確認します。
    *   REPLでテストします:
      ```python
      from machine import Pin
      led = Pin(25, Pin.OUT)
      led.on()
      ```
*   **Pico-W-Goコマンドがない**: 拡張機能がインストールされ、有効化されていることを確認します。必要に応じてVSCodeを再起動します。

---

### VSCodeでのPico-W-Goの利点
*   **統合ワークフロー**: コード編集、ファイル管理、REPLアクセスをVSCode内で結合します。
*   **高度な機能**: VSCodeのGit統合、拡張機能、カスタマイズを活用できます。
*   **クロスプラットフォーム**: Linux、Windows、macOSで動作します。

### Thonnyとの比較における制限
*   セットアップがやや複雑（例: `pyserial`のインストール、ポートの設定）。
*   REPL統合は、Thonnyのオールインワンインターフェースほどシームレスに感じない場合があります。
*   初めてのMicroPythonユーザーにとっては、あまり初心者に優しくありません。

---

### 代替拡張機能
別の拡張機能（例: **Pico-Go**）を意味していた場合、Pico-GoはPico-W-Goの古い代替品であり、機能やアップデートが少ない可能性があることに注意してください。セットアップは似ていますが、活発な開発とPicoおよびPico Wの両方のサポートのためにPico-W-Goが推奨されます。別の特定の拡張機能を使用している場合は、明確にしていただければ、説明を調整できます。

---

### ワークフローの例
1.  Pico-W-Goと依存関係をインストール。
2.  正しいシリアルポート（`/dev/ttyACM0`）でプロジェクトを設定。
3.  LED点滅コードで`main.py`を書き込み、保存。
4.  **Pico-W-Go > Upload Project to Pico**を使用してアップロード。
5.  Picoをリセットするか、**Pico-W-Go > Run**を使用してLEDの点滅を確認。
6.  REPLを使用して対話的にテストまたはデバッグ。

特定のPico-W-Goコマンド、別のプログラム例、またはトラブルシューティング（例: ポートの問題、拡張機能エラー）についてヘルプが必要な場合は、お知らせください！
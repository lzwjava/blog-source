---
audio: false
generated: true
lang: ja
layout: post
title: UF2によるPicoファームウェアのフラッシュ
translated: true
type: note
---

Raspberry Pi Pico（またはRP2040ベースのボード）にBOOTSELモードでファームウェアを書き込むには、`.uf2`ファイルを`RPI-RP2`ドライブにコピーします。以下の手順に従ってください。

### ステップバイステップガイド
1. **デバイスがBOOTSELモードであることを確認**:
   - デバイスをコンピュータに接続すると、`RPI-RP2`という名前のUSBドライブとして表示されるはずです（`Bus 001 Device 009: ID 2e8a:0003 Raspberry Pi RP2 Boot`と表示される状態）。
   - BOOTSELモードでない場合は、デバイスの電源を切り、PicoのBOOTSELボタンを押したままコンピュータのUSBポートに接続します。数秒後にボタンを離します。

2. **有効な`.uf2`ファイルを入手**:
   - **MicroPython**: [公式MicroPythonウェブサイト](https://micropython.org/download/rp2-pico/)からRaspberry Pi Pico用の最新MicroPythonファームウェアをダウンロードします。PicoまたはPico W用の`.uf2`ファイル（例: `rp2-pico-latest.uf2`）を選択してください。
   - **CircuitPython**: [CircuitPythonウェブサイト](https://circuitpython.org/board/raspberry_pi_pico/)からPicoまたはPico W用のCircuitPythonファームウェアをダウンロードします。
   - **カスタムプログラム**: プログラム（例: Pico SDKを使用したC/C++）を書いた場合、コンパイルして`.uf2`ファイルを生成します。例えば、Pico SDKやArduino IDEを使用してプロジェクトをビルドします。
   - `.uf2`ファイルをコンピュータのアクセスしやすい場所（例: デスクトップやダウンロードフォルダ）に保存します。

3. **RPI-RP2ドライブを探す**:
   - コンピュータでファイルエクスプローラーを開きます:
     - **Windows**: 「PC」で`RPI-RP2`がリムーバブルドライブとして表示されます。
     - **macOS**: デスクトップまたはFinderの「デバイス」にドライブが表示されます。
     - **Linux**: `/media`または`/mnt`以下を確認するか、`lsblk`を使用して接続されたドライブを一覧表示します。
   - ドライブが表示されない場合は、USBケーブルがデータ転送対応であることを確認し、別のUSBポートまたはケーブルを試してください。

4. **`.uf2`ファイルをRPI-RP2ドライブにコピー**:
   - `.uf2`ファイルを`RPI-RP2`ドライブにドラッグ＆ドロップするか、ファイルエクスプローラーを使用してコピー＆ペーストします。
   - または、ターミナルコマンドを使用します（Linux/macOS）:
     ```bash
     cp /path/to/your/file.uf2 /media/your_username/RPI-RP2/
     ```
     `/path/to/your/file.uf2`をあなたの`.uf2`ファイルのパスに置き換え、マウントポイントを必要に応じて調整してください。

5. **フラッシュプロセスを待機**:
   - `.uf2`ファイルがコピーされると、Raspberry Pi Picoは自動的にファームウェアをフラッシュします。デバイスが再起動すると`RPI-RP2`ドライブは消え（アンマウントされ）、プロセスが完了したことを示します。
   - 通常、数秒かかります。この間はデバイスの接続を切らないでください。

6. **デバイスを確認**:
   - フラッシュ後、PicoはBOOTSELモードを終了し、新しいファームウェアを実行します。
   - MicroPythonまたはCircuitPythonの場合、ターミナル（例: PuTTY、screen、Thonny IDE）を使用してUSBシリアルポート（例: Windowsでは`COM3`、Linux/macOSでは`/dev/ttyACM0`）経由でデバイスに接続します。Python REPLプロンプトが表示されるはずです。
   - カスタムプログラムの場合、期待される動作（例: LED点滅、シリアル出力など）を確認します。
   - `RPI-RP2`ドライブが再表示される場合、フラッシュが失敗した可能性があります。別の`.uf2`ファイルを試すか、ハードウェアの問題（例: USBケーブル、フラッシュチップ）を確認してください。

### トラブルシューティング
- **ドライブが表示されない**: PicoがBOOTSELモードであること、およびUSBケーブルがデータ転送をサポートしていることを確認してください。BOOTSELを押した後、RESETボタン（利用可能な場合）を接続中に短く押してみてください。
- **コピーが失敗する、またはドライブが再表示される**: `.uf2`ファイルが破損しているか、フラッシュメモリに障害がある可能性があります。新しい`.uf2`ファイルをダウンロードするか、MicroPythonなどの最小限のファイルでテストしてください。それでも解決しない場合は、`picotool`を使用して診断します:
  ```bash
  picotool info
  ```
  `picotool`は[Raspberry Pi Pico SDK](https://github.com/raspberrypi/picotool)からインストールできます。
- **フラッシュ後に応答がない**: MicroPython/CircuitPythonを使用している場合、IDE（例: Thonny）が正しいシリアルポートに設定されていることを確認してください。カスタムプログラムの場合、コードが正しくコンパイルされたことを確認してください。

### 例: MicroPythonのフラッシュ
1. [micropython.org](https://micropython.org/download/rp2-pico/)からMicroPythonの`.uf2`ファイルをダウンロードします。
2. BOOTSELを押したままPicoを接続し、BOOTSELを離します。
3. ファイルエクスプローラーを開き、`RPI-RP2`ドライブを見つけて、`.uf2`ファイルをコピーします。
4. ドライブが消えるのを待ちます。
5. Thonny IDEを開き、Picoのシリアルポートを選択して、MicroPythonでのコーディングを開始します。

特定の`.uf2`ファイル、ツール、またはセットアップ（例: `picotool`のインストールやThonnyの使用）についてヘルプが必要な場合は、お知らせください！
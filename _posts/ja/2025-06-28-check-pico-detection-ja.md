---
audio: false
generated: true
lang: ja
layout: post
title: UbuntuでのRaspberry Pi Pico検出確認
translated: true
type: note
---

Raspberry Pi Picoを接続した後にUbuntuで認識されているか確認するには、以下の手順に従ってください。

1. **USBデバイスの確認**:
   - ターミナルを開き、以下を実行:
     ```bash
     lsusb
     ```
   - `Raspberry Pi Pico`というエントリ、またはベンダーID `2E8A`（Raspberry PiのベンダーID）のデバイスを探します。例:
     ```
     Bus XXX Device XXX: ID 2e8a:0003 Raspberry Pi Pico
     ```

2. **シリアルポートの確認**:
   - PicoがBOOTSELモード（ファームウェア書き込み用）の場合、またはシリアル出力のあるMicroPython/Arduinoプログラムを実行中の場合は、シリアルポートを確認:
     ```bash
     ls /dev/tty*
     ```
   - `/dev/ttyACM0` や `/dev/ttyUSB0` のようなデバイスを探します。PicoはMicroPython実行時には通常 `/dev/ttyACM0` として表示されます。

3. **ディスクデバイスの確認（BOOTSELモード）**:
   - PicoがBOOTSELモード（接続時にBOOTSELボタンを押しながら）の場合、Mass Storageデバイスとして表示されます。以下を実行:
     ```bash
     lsblk
     ```
   - `/dev/sdb`（または類似）のデバイスで、マウントポイントが `RPI-RP2` と表示されているものを探します。

4. **カーネルログの確認（`dmesg`の使用）**:
   - 以下を実行:
     ```bash
     dmesg | tail -n 20
     ```
   - Picoが検出されたことを示すメッセージを確認します。例:
     ```
     [1234.567890] usb 1-1: New USB device found, idVendor=2e8a, idProduct=0003
     [1234.567891] usb 1-1: Product: Pico
     [1234.567892] cdc_acm 1-1:1.0: ttyACM0: USB ACM device
     ```
   - これにより、Picoが認識されポート（例: `ttyACM0`）が割り当てられたことが確認できます。

5. **MicroPythonでのテスト（インストール済みの場合）**:
   - MicroPythonを使用している場合、`picocom` や `minicom` などのツールをインストール:
     ```bash
     sudo apt install picocom
     ```
   - Picoのシリアルポートに接続:
     ```bash
     picocom /dev/ttyACM0
     ```
   - 認識されていれば、MicroPythonのRELプロンプト（>>>）が表示されます。終了するには `Ctrl+C` を押します。

**注意点**:
- Picoが適切なUSBケーブル（電力供給のみではなくデータ通信可能なもの）で正しく接続されていることを確認してください。
- BOOTSELモードの場合、Picoはシリアルデバイスではなくストレージデバイスとして表示されます。
- 認識されない場合は、別のUSBポートやケーブルを試すか、ドライバ（シリアル用の `cdc_acm` など）がロードされているか確認:
  ```bash
  lsmod | grep cdc_acm
  ```

これらのチェックでPicoが表示されない場合は、詳細（例: Picoのモード、実行しようとしている内容）をお知らせいただければ、さらにトラブルシューティングをお手伝いします！
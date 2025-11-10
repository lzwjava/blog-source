---
audio: false
generated: true
lang: ja
layout: post
title: Bluetoothキーボード接続問題の解決
translated: true
type: note
---

`bluetoothctl`の出力に`[DEL] Device`が表示される場合の正確な解決策は以下の通りです：

### 接続削除問題の即時修正
1. **既存のデバイスレコードを削除**（古い設定の削除が重要）:
   ```bash
   bluetoothctl
   remove F4:73:35:78:28:4E  # キーボードを削除
   remove 24:27:30:24:C8:31   # 干渉する可能性のあるデバイスを削除
   exit
   ```

2. **Bluetoothスタックをリセット**:
   ```bash
   sudo systemctl stop bluetooth
   sudo rm -rf /var/lib/bluetooth/*
   sudo systemctl start bluetooth
   ```

3. **正しい手順でペアリング**:
   ```bash
   bluetoothctl
   power on
   discoverable on
   pairable on
   agent on  # パスキーエージェントを有効化
   scan on
   ```
   - **K380をペアリングモードに**（LEDが速く点滅）
   - キーボードが表示されたら:
     ```bash
     pair F4:73:35:78:28:4E
     ```
   - **画面に表示された6桁のパスコード**（例: `123456`）を**キーボードで即座に入力**しEnterを押す

4. **ペアリング成功後にのみ接続**:
   ```bash
   connect F4:73:35:78:28:4E
   trust F4:73:35:78:28:4E
   scan off
   quit
   ```

### 発生原因
- `[DEL] Device`が発生する理由:
  - Bluetoothスタックが接続失敗を検出しデバイスレコードを削除
  - 接続試行前の**ペアリング手順の欠落**
  - 他のデバイス（`midea`デバイスなど）からのRF干渉の可能性

### 追加の重要チェック
1. **アンテナ接続を確認**:
   - MSIマザーボードの背面I/OパネルにBluetoothアンテナが確実に接続されていることを確認

2. **カーネルドライバーを確認**:
   ```bash
   dmesg | grep -i bluetooth
   ```
   `hci0: command timeout`や`Firmware failed to start`のようなエラーを探す

3. **ファームウェアを更新**（タイムアウトエラーが表示される場合）:
   ```bash
   sudo apt install linux-firmware
   ```

4. **最小環境でのテスト**:
   ```bash
   sudo rfkill unblock all
   sudo systemctl stop NetworkManager  # 一時停止
   sudo systemctl restart bluetooth
   ```

### まだ失敗する場合
1. **代替ペアリング方法**（エージェントをバイパス）:
   ```bash
   echo -e 'remove F4:73:35:78:28:4E\npair F4:73:35:78:28:4E\nconnect F4:73:35:78:28:4E\ntrust F4:73:35:78:28:4E' | bluetoothctl
   ```

2. **キーボードのバッテリーを確認**（Bluetoothにとって重要）:
   - 電圧が低い場合はバッテリーを交換（K380はCR2032 x 2を使用）

3. **USB Bluetoothアダプターテスト**:
   - 内蔵Bluetoothに問題がある場合、$10のCSR4.0 USBアダプターを試す

**期待される成功指標**:
- `Pairing successful`メッセージ
- bluetoothctlでの`Connection successful`
- `HIDP: Bluetooth HID device driver`を表示する`dmesg`

ペアリング後、K380は再起動後も維持されるはずです。切断が再発生する場合は、`journalctl -u bluetooth -f`でリアルタイムエラーを確認してください。
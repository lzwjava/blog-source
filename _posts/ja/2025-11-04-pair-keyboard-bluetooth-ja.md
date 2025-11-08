---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: LogitechキーボードをBluetooth CLIでペアリング
translated: true
type: note
---

### 前提条件
- Bluetooth 5.3 エミッター（ドングル）が USB 3.0 ポートに接続され、Ubuntu で認識されていることを確認してください。ターミナルで `lsusb` を実行し、表示されるか確認します（「Bluetooth」やベンダー ID などを探してください）。表示されない場合は、別の USB ポートを試すか、再起動してください。
- Bluetooth ツールがインストールされていない場合はインストールしてください:  
  ```
  sudo apt update
  sudo apt install bluez bluetooth bluez-tools
  ```
- 必要に応じて Bluetooth のブロックを解除してください:  
  ```
  rfkill unblock bluetooth
  ```
- Bluetooth サービスを再起動してください:  
  ```
  sudo systemctl restart bluetooth
  ```

### bluetoothctl を使用したペアリング手順（CLI 推奨）
`bluetoothctl` ツールは、Linux/Ubuntu で Bluetooth を管理する標準的な方法です。Logitech キーボード（MX Keys、K380 など）は、多くの場合、キーボード自体でペアリング PIN を入力する必要があります。

1. **Bluetooth コンソールを開く**:  
   ```
   bluetoothctl
   ```
   これにより対話型シェルに入ります（プロンプトが `[bluetooth]#` に変わります）。

2. **アダプターを有効にする**:  
   ```
   power on
   ```
   （「No default controller available」と表示された場合は、`list` を実行してアダプターを確認し、複数ある場合は `select <アダプターのMACアドレス>` を実行してください。）

3. **ペアリングエージェントを設定する**:  
   ```
   agent on
   default-agent
   ```
   これにより PIN 処理が有効になり、セッションがペアリングのデフォルトとして設定されます。

4. **デバイスのスキャンを開始する**:  
   ```
   scan on
   ```
   このまま実行し続けてください。Logitech キーボードは約 10～20 秒後に表示されるはずです（例: 「Logitech K380」など、MAC アドレス `XX:XX:XX:XX:XX:XX` のような形式で表示されます）。

5. **Logitech キーボードをペアリングモードにする**:  
   - 電源を入れます（電源スイッチがある場合）。  
   - Bluetooth ペアリングボタンを長押しします（通常は側面または上面にあります。お使いのモデルを確認してください。MX Keys などのマルチデバイスモデルの場合は、チャンネルボタン 1/2/3 を 3～5 秒間長押しし、LED が速く点滅するまで待ちます）。  
   - シングルデバイスモデルの場合は、メインのペアリングボタンを長押しします。

6. **デバイスをペアリングする**:  
   スキャン中に表示されたら（Enter キーを押して更新）、次を実行します:  
   ```
   pair <MAC_ADDRESS>
   ```
   - 例: `pair 12:34:56:78:9A:BC`  
   - Ubuntu は PIN の入力を求めます（Logitech では多くの場合 0000 または 1234 です。まずはデフォルト値を試してください）。  
   - **Logitech の場合の重要なステップ**: PIN を*物理キーボード*で直接入力し、Enter キーを押します。（GUI 通知が表示されない場合、これが重要です。CLI ではしばしばこれを回避できますが、`gnome-control-center` > 通知 でシステム通知を有効にする必要があると報告するユーザーもいます。）

7. **信頼して接続する**:  
   ```
   trust <MAC_ADDRESS>
   connect <MAC_ADDRESS>
   ```
   - これにより、今後は自動的に接続されます。

8. **コンソールを終了する**:  
   ```
   exit
   ```

### トラブルシューティング
- **デバイスがスキャンされない**: キーボードがペアリングモード（LED 点滅）であることを確認してください。`scan off` を実行した後、再度 `scan on` を実行してください。最大 30 秒待ちます。
- **ペアリングに失敗する（例: "AuthenticationCanceled"）**: まずデバイスを削除し（`remove <MAC>`）、再度試してください。頑固な Logitech モデルの場合は、ペアリングボタンをより長く押し続けるか、チャンネルを切り替えてみてください。
- **PIN プロンプトが表示されない**: 一部のキーボードは PIN なしでペアリングします。その場合は接続に進んでください。行き詰まった場合は、ログを確認してください: ペアリング中に `sudo journalctl -u bluetooth -f` を実行します。
- **アダプターの問題**: USB Bluetooth 5.3 ドングルを使用している場合は、カーネルサポートを確認してください（Ubuntu 22.04 以降は BT 5.3 を適切に処理します）。古い Ubuntu を使用している場合はカーネルを更新してください: `sudo apt install linux-generic-hwe-22.04`。
- **GUI での代替方法**: 設定 > Bluetooth を開き、トグルをオンにして、そこからペアリングします。ただし、Logitech の特性上、CLI の方が信頼性が高いです。
- テスト: ペアリング後、ターミナルで入力して動作を確認してください。動作する場合は、`bluetoothctl` または crontab を使用してスタートアップ時の自動接続を追加してください。

特定の Logitech モデル（例: MX Keys Mini）に固有の問題がある場合は、正確なモデルを提供してください。具体的な手順をご案内します。

### 参考資料
- [Pairing LOGITECH K380 in Ubuntu 20.04](https://unix.stackexchange.com/questions/590221/pairing-logitech-k380-in-ubuntu-20-04)  
- [Logitech MX Keys won't pair with Bluetooth](https://askubuntu.com/questions/1270419/20-04-logitech-mx-keys-wont-pair-with-bluetooth)  
- [Pair Logitech MX Keys with Xubuntu via Bluetooth](https://zroupas.github.io/linux/2021/08/25/pair_mxkeys_xubuntu_bt.html)  
- [Ubuntu 20.04 cannot pair Bluetooth Keyboard](https://askubuntu.com/questions/1398096/ubuntu-20-04-cannot-pair-bluetooth-keyboard)
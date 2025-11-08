---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: ロジテックBluetoothペアリング問題の解決
translated: true
type: note
---

### AuthenticationCanceled エラーのトラブルシューティング

このエラーは、Logitech Bluetooth キーボード（お使いの MAC アドレス `F4:73:35:78:28:4E` は Logitech の OUI プレフィックスと一致）で、Ubuntu のペアリング中に、認証タイムアウト、PIN プロンプトの欠落、または BlueZ でのエージェントの不適切な処理が原因で頻繁に発生します。ログに短時間の接続/切断が記録されていることは、キーボードが応答しているが、プロセスが完了前にタイムアウトしていることを示唆しています。他のデバイス（`54:2B:FC:F1:1C:D8` など）が表示される場合は干渉の原因となる可能性があるため、まずこれらを削除してください。

#### クイック準備ステップ
1.  **すべてのペアリング済みデバイスを削除**して競合を避ける:  
    `bluetoothctl` で、`devices` を実行して一覧表示し、それぞれに対して `remove <MAC>` を実行します（例: `remove 54:2B:FC:F1:1C:D8`）。`exit` で終了します。

2.  **Bluetooth サービスを再起動**:  
    ```
    sudo systemctl restart bluetooth
    sudo systemctl status bluetooth  # アクティブであることを確認
    ```

3.  **キーボードをペアリングモードにする**: ペアリングボタン（例: Easy-Switch チャネルまたは Bluetooth ボタン）を LED が速く点滅するまで押し続けます。毎回新しい試行の度に行ってください。

#### bluetoothctl での拡張ペアリング手順
`bluetoothctl` を再度開き、以下の手順を**正確に**実行してください。エージェントの設定が重要であり、最初に信頼することで一部のタイムアウトを回避できることがよくあります。Logitech モデル（例: K380, K480, MX Keys）の場合、`pair` コマンドの直後に、物理キーボードで（画面上にエコーされなくても）任意の PIN を**画面確認せずに**入力してください。

1.  **bluetoothctl を起動**:  
    ```
    bluetoothctl
    ```

2.  **電源を入れ、エージェントを設定**:  
    ```
    power on
    agent on
    default-agent
    ```

3.  **スキャンとデバイスの確認**:  
    ```
    scan on
    ```  
    `F4:73:35:78:28:4E` が表示されるのを待ちます（必要に応じて Enter キーを押して更新）。その後:  
    ```
    scan off  # スキャンを停止して集中
    ```

4.  **デバイスを信頼**（再接続時の自動受け入れに役立つ）:  
    ```
    trust F4:73:35:78:28:4E
    ```

5.  **ペアリング**:  
    ```
    pair F4:73:35:78:28:4E
    ```  
    - PIN/パスキーが表示された場合（例: `[agent] PIN code: 390412` または `[agent] Passkey: 299595`）、**直ちに物理キーボードで入力**し、Enter キーを押します。プロンプトがアクティブに見えなくても、画面確認せずに行います。
    - PIN が表示されない場合（一部の Logitech 製品で一般的）、とにかくキーボードで `0000` または `1234` を入力して Enter キーを押してみてください。
    - `[CHG] Paired: yes` を確認します。一時的に接続されてから切断される場合は、直後に `connect F4:73:35:78:28:4E` を再実行します。

6.  **接続と信頼**:  
    ```
    connect F4:73:35:78:28:4E
    trust F4:73:35:78:28:4E  # 以前に行っていない場合
    ```

7.  **終了とテスト**:  
    ```
    exit
    ```  
    テキストエディタまたはターミナルを開き、入力して動作を確認します。動作すれば、ウェイクアップ時に自動的に再接続されるはずです。

#### それでも失敗する場合
-   **GUI フォールバック**: Ubuntu の設定 > Bluetooth（トグルをオンにし、デバイスを選択）を使用します。これは多くの場合、目に見える PIN プロンプトを表示します。CLI エージェントが失敗した場合、GUI の pinentry がより適切に処理します。
-   **画面確認しない PIN 再試行**: 表示されるコードがなくても、`pair` の直後に `0000` + Enter キーを入力することで成功するユーザーもいます。キーボードは暗黙的に認証します。
-   **ログの手がかり**: ペアリング中に別のターミナルで `sudo journalctl -u bluetooth -f` を実行します。"PIN code" またはタイムアウトメッセージを探してください。
-   **BlueZ の更新**: 最新版を確認します（Ubuntu 24.04+ は Logitech のサポートが改善された BlueZ 5.72+ を搭載）:  
    ```
    sudo apt update && sudo apt upgrade bluez
    ```
-   **USB ドングルの特性**: お使いの USB 3.0 上の BT 5.3 エミッタは問題ありませんが、USB 2.0 ポートでテストしてください。まれに干渉が報告されています。
-   **モデル固有**: K480/MX Keys の場合、ペアリングボタンを 5 秒以上押し続けてください。マルチデバイス対応モデルの場合、まず使用されていないチャネルに切り替えてください。

これで解決するはずです。Logitech の場合、ほとんどの原因は画面確認しない PIN 入力ステップにあります。正確なモデルまたは完全なログを共有していただければ、さらに詳細な対応策をご案内できます。

[Bluetooth ペアリング - AuthenticationCanceled (AskUbuntu)](https://askubuntu.com/questions/1373574/bluetooth-pairing-authenticationcanceled)  
[[解決済み] Bluetooth キーボード: ペアリングできません (Arch Linux フォーラム)](https://bbs.archlinux.org/viewtopic.php?id=174239)  
[Barely able to pair Logitech K480 on bluez 5.72 (GitHub)](https://github.com/bluez/bluez/issues/654)
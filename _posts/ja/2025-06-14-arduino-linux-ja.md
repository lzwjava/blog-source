---
audio: false
generated: true
lang: ja
layout: post
title: UbuntuへのArduino IDEインストール
translated: true
type: note
---

Ubuntu LinuxにArduino IDEをインストールするには、以下の手順に従ってください：

1. **Arduino IDEのダウンロード**：
   - 公式Arduinoウェブサイト[https://www.arduino.cc/en/software](https://www.arduino.cc/en/software)にアクセスします。
   - 「Arduino IDE」セクションで、「Linux 64 bits」ダウンロードオプション（またはお使いのシステムに適したバージョン、例：Raspberry Pi用のLinux ARM）を選択します。

2. **ダウンロードしたファイルの展開**：
   - ダウンロードしたファイルは圧縮された`.tar.xz`アーカイブです（例：`arduino-1.8.19-linux64.tar.xz`）。
   - ターミナルを開き、ダウンロードディレクトリに移動します（例：`cd ~/Downloads`）。
   - 以下のコマンドでファイルを展開します：
     ```bash
     tar -xf arduino-*.tar.xz
     ```
   - これにより`arduino-1.8.19`のようなフォルダが作成されます。

3. **適切なディレクトリへの移動（オプション）**：
   - システム全体でアクセスできるようにするには、展開したフォルダを`/opt`に移動します（スーパーユーザー権限が必要）：
     ```bash
     sudo mv arduino-1.8.19 /opt/arduino
     ```

4. **インストールスクリプトの実行**：
   - Arduinoフォルダに移動します：
     ```bash
     cd /opt/arduino
     ```
   - インストールスクリプトを実行します：
     ```bash
     sudo ./install.sh
     ```
   - これによりデスクトップショートカットが作成され、必要な権限が設定されます。

5. **ユーザーをdialoutグループに追加**：
   - Arduinoボードにシリアルポート経由でアクセスするには、ユーザーを`dialout`グループに追加します：
     ```bash
     sudo usermod -a -G dialout $USER
     ```
   - グループ変更を反映させるには、ログアウトして再度ログインするか、再起動します。

6. **Arduino IDEの起動**：
   - `install.sh`スクリプトを実行した場合、アプリケーションメニューからまたは「Arduino IDE」を検索してIDEを起動できます。
   - または、ターミナルから直接実行します：
     ```bash
     /opt/arduino/arduino
     ```

7. **Arduinoボードの権限更新（必要な場合）**：
   - Arduinoを接続する際に、検出されていることを確認します（例：`/dev/ttyACM0`や`/dev/ttyUSB0`）。
   - 権限の問題が発生した場合は、正しい権限を設定します：
     ```bash
     sudo chmod a+rw /dev/ttyACM0
     ```
   - `/dev/ttyACM0`を適切なポートに置き換えてください。

8. **インストールの確認**：
   - ArduinoボードをUSBで接続します。
   - IDEを開き、**ツール > ボード**に移動してArduinoモデル（例：Arduino Uno）を選択します。
   - **ツール > ポート**に移動してポート（例：`/dev/ttyACM0`）を選択します。
   - サンプルスケッチ（例：**ファイル > スケッチ例 > 01.Basics > Blink**）をアップロードして、すべてが正常に動作することを確認します。

**代替方法：SnapまたはFlatpak経由でのインストール**：
- **Snap**：
  ```bash
  sudo snap install arduino
  ```
- **Flatpak**：
  ```bash
  sudo flatpak install flathub cc.arduino.ArduinoIDE
  ```
- これらの方法はインストールを簡素化しますが、権限やボードの検出に制限がある場合があります。

**注意点**：
- Arduino IDEにはJavaが必要です。必要に応じてインストールしてください：
  ```bash
  sudo apt update
  sudo apt install default-jre
  ```
- 最新バージョンやトラブルシューティングについては、Arduinoフォーラムまたは[公式ドキュメント](https://www.arduino.cc/en/Guide/Linux)を確認してください。

問題が発生した場合は、Ubuntuのバージョンや具体的なエラーを教えてください！

---

Arduino UnoがUbuntuのArduino IDEで検出され、ブレッドボードや外部部品を使用せずに簡単な例を求めている場合、Arduino Uno（デジタルピン13に接続）の内蔵LEDを点滅させる基本的なスケッチを以下に示します。追加のハードウェアは必要ありません。

```cpp
void setup() {
  // put your setup code here, to run once:
  pinMode(LED_BUILTIN, OUTPUT); // 内蔵LEDピン（ピン13）を出力に設定
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(LED_BUILTIN, HIGH); // LEDを点灯
  delay(1000);                     // 1秒待機
  digitalWrite(LED_BUILTIN, LOW);  // LEDを消灯
  delay(1000);                     // 1秒待機
}
```

### 実行方法：
1. Arduino IDEを開きます。
2. 上記のコードをIDEにコピー＆ペーストします。
3. Arduino UnoがUSB経由で接続され、検出されていることを確認します：
   - **ツール > ボード**に移動して**Arduino Uno**を選択します。
   - **ツール > ポート**に移動してポート（例：`/dev/ttyACM0`や`/dev/ttyUSB0`）を選択します。
4. **アップロード**ボタン（右矢印アイコン）をクリックして、スケッチをコンパイルしArduino Unoにアップロードします。
5. アップロードが完了すると、内蔵LED（ボード上の「L」と表示されたLED）が1秒間点灯、1秒間消灯を繰り返します。

### 動作内容：
- `setup()`では、`pinMode`関数が内蔵LEDピンを出力として設定します。
- `loop()`では、`digitalWrite`関数がLEDを点灯（`HIGH`）および消灯（`LOW`）し、`delay`で各状態の間に1秒間一時停止し、点滅効果を作り出します。

### 注意点：
- Arduino Unoにはピン13に内蔵LEDがあるため、外部部品は必要ありません。
- LEDが点滅しない場合は、ポート選択を再確認するか、ボードが正しく接続されていることを確認してください。`setup()`に`Serial.begin(9600);`を追加し、`loop()`に`Serial.println("Blink");`のようなメッセージを印刷して**シリアルモニター**（ツール > シリアルモニター）を開くことでデバッグすることもできます。
- 点滅速度を変更したい場合は、`delay(1000)`の値を調整してください（例：より速く点滅させるには`delay(500)`）。

問題が発生した場合や別の簡単な例が必要な場合はお知らせください！

---

エラーメッセージは、UbuntuでArduino Unoにスケッチをアップロードしようとした際の権限問題を示しています。Arduino IDEがシリアルポート`/dev/ttyUSB0`にアクセスするための十分な権限を持っていません。以下はこの問題を修正する方法です：

### 解決策：シリアルポートの権限を修正

1. **ユーザーを`dialout`グループに追加**：
   - `dialout`グループは通常、Ubuntuでシリアルポートへのアクセスを制御します。ユーザーをこのグループに追加します：
     ```bash
     sudo usermod -a -G dialout $USER
     ```
   - このコマンドを実行後、変更を反映させるためにログアウトして再度ログインするか、システムを再起動します：
     ```bash
     sudo reboot
     ```

2. **ポートの確認**：
   - 再起動後、Arduino Unoを再接続し、Arduino IDEを開きます。
   - **ツール > ポート**に移動し、`/dev/ttyUSB0`（または一部のArduinoボードでは`/dev/ttyACM0`）が選択されていることを確認します。ポートが表示されない場合は、USB接続を確認するか、別のケーブル/ポートを試してください。

3. **ポートの権限を一時的に変更（オプション）**：
   - ユーザーを`dialout`グループに追加した後も問題が解決しない場合、手動でポートの権限を設定できます（これは一時的な修正です。権限は再起動時にリセットされます）：
     ```bash
     sudo chmod a+rw /dev/ttyUSB0
     ```
   - ポートが異なる場合は`/dev/ttyUSB0`を正しいポートに置き換えてください（例：`/dev/ttyACM0`）。

4. **再度アップロードを試行**：
   - Arduino IDEで**アップロード**ボタンをクリックしてスケッチ（例：前述の点滅LEDスケッチ）をアップロードします。
   - 正常にアップロードされると、Arduino Unoの内蔵LEDが点滅し始めるはずです。

### 追加のトラブルシューティング

- **Arduinoボードとケーブルの確認**：
  - Arduino UnoがUSB経由で正しく接続され、Ubuntuで認識されていることを確認します。このコマンドを実行して接続されているデバイスを一覧表示します：
    ```bash
    ls /dev/tty*
    ```
    ボードが接続されているときに`/dev/ttyUSB0`または`/dev/ttyACM0`を探します。
  - ボードが検出されない場合は、別のUSBケーブルまたはポートを試してください。

- **ボードとポート設定の確認**：
  - Arduino IDEで、**ツール > ボード**が**Arduino Uno**に設定されていることを確認します。
  - `/dev/ttyUSB0`が表示されない場合は、ボードを抜き差しした後で**ツール > ポート**を試してください。

- **ルートとしてArduino IDEを実行（一時的な回避策）**：
  - 上記の手順で問題が解決しない場合、権限問題を回避するためにスーパーユーザー権限でIDEを実行できます（長期的には推奨されません）：
    ```bash
    sudo arduino
    ```
    `arduino`がシステムのPATHにない場合は、正しいパスに置き換えてください（例：`/opt/arduino/arduino`）。

- **競合ソフトウェアの確認**：
  - 他のソフトウェア（例：点字ディスプレイドライバの`brltty`）がシリアルポートと干渉する可能性があります。インストールされている場合は削除します：
    ```bash
    sudo apt remove brltty
    ```

- **ドライバの問題**：
  - 一部のArduinoクローンはCH340/CH341チップを使用しており、ドライバが必要です。必要な場合はインストールします：
    ```bash
    sudo apt install linux-modules-extra-$(uname -r)
    ```
    その後、ボードを再接続します。

### 修正の確認
権限が解決したら、前述の点滅スケッチを再度アップロードしてみてください：
```cpp
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
}
```

まだ問題が発生する場合は、新しいエラーメッセージを共有するか、ターミナルで`ls -l /dev/ttyUSB0`を実行して出力を提供し、さらに診断できるようにしてください。

---

Arduino IDEを使用してUbuntuでArduino Unoにスケッチをアップロードしようとしている際に問題が発生しているようです。提供されたエラーメッセージは以下の通りです：

```
avrdude: ser_open(): can't open device "/dev/ttyUSB0": Permission denied
Failed uploading: uploading error: exit status 1
```

このエラーは、Arduino IDEがArduino Unoが接続されているシリアルポート（`/dev/ttyUSB0`）にアクセスするための必要な権限を持っていないことを示しています。これは、シリアルポートアクセスの管理方法により、UbuntuなどのLinuxシステムでよくある問題です。以下にこの問題を修正するためのステップバイステップガイドを示します。

---

### 解決策：シリアルポートの権限問題を修正

#### 1. ユーザーを`dialout`グループに追加
Ubuntuでは、`dialout`グループがシリアルポートへのアクセスを制御します。権限問題を解決するには、ユーザーをこのグループに追加する必要があります。

- `Ctrl + Alt + T`を押してターミナルを開きます。
- 以下のコマンドを実行します：
  ```bash
  sudo usermod -a -G dialout $USER
  ```
- このコマンドは現在のユーザーを`dialout`グループに追加します。`$USER`変数は自動的にユーザー名を使用します。

#### 2. ログアウトして再度ログイン
グループ変更を反映させるには、現在のセッションからログアウトして再度ログインする必要があります。または、システムを再起動することもできます。

- **ログアウトして再度ログインするには：**
  - 開いている作業を保存します。
  - Ubuntuデスクトップの右上隅にあるユーザー名をクリックし、「ログアウト」を選択します。
  - ユーザー名とパスワードで再度ログインします。
- **再起動（オプション）：**
  - ターミナルでこのコマンドを実行します：
    ```bash
    sudo reboot
    ```
  - システムが再起動するのを待ちます。

#### 3. シリアルポートの確認
再度ログインした後、Arduino Unoがシステムによって正しく認識されていることを確認します。

- Arduino UnoをUSBポートに再接続します。
- Arduino IDEを開きます。
- メニューの**ツール > ポート**に移動し、`/dev/ttyUSB0`（または一部のArduinoボードでは`/dev/ttyACM0`）がリストされ選択されていることを確認します。
- ポートが表示されない場合：
  - Arduino Unoを抜き差しします。
  - USB接続を確認するか、別のケーブル/ポートを試してください。

#### 4. スケッチを再度アップロード
正しいポートが選択された状態で、スケッチを再度アップロードしてみてください：

```cpp
void setup() {
  pinMode(LED_BUILTIN, OUTPUT); // 内蔵LEDピン（ピン13）を出力に設定
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH); // LEDを点灯
  delay(1000);                     // 1秒待機
  digitalWrite(LED_BUILTIN, LOW);  // LEDを消灯
  delay(1000);                     // 1秒待機
}
```

- Arduino IDEで**アップロード**ボタン（右矢印アイコン）をクリックします。
- 成功した場合、Arduino Unoの内蔵LEDが点滅し始めます（1秒点灯、1秒消灯）。

---

### 追加のトラブルシューティング
上記の手順で問題が解決しない場合は、以下の追加チェックを試してください：

#### グループメンバーシップの確認
ユーザーが`dialout`グループの一部であることを確認します：
- ターミナルでこのコマンドを実行します：
  ```bash
  groups $USER
  ```
- 出力に`dialout`があるか確認します。ない場合は、ステップ1を繰り返し、ログアウト/ログインまたは再起動を確実に行ってください。

#### 一時的な権限修正（長期的には推奨されません）
迅速な修正が必要な場合は、シリアルポートの権限を手動で変更できます：
- 実行：
  ```bash
  sudo chmod a+rw /dev/ttyUSB0
  ```
- その後、再度アップロードを試みます。注意：これは一時的であり、Arduinoを抜き差しするか再起動するとリセットされます。

#### 競合ソフトウェアの確認
`brltty`（点字ディスプレイドライバ）などの一部のソフトウェアがシリアルポートと干渉する可能性があります。削除するには：
- 実行：
  ```bash
  sudo apt remove brltty
  ```
- Arduinoを再接続し、再度試してください。

#### Arduino接続の確認
UbuntuがArduinoを認識していることを確認します：
- 実行：
  ```bash
  ls /dev/tty*
  ```
- Arduinoが接続されているときに`/dev/ttyUSB0`または`/dev/ttyACM0`を探します。ない場合は、USBケーブルまたはポートを確認してください。

#### ルートとしてArduino IDEを実行（一時的な回避策）
最後の手段として、スーパーユーザー権限でIDEを実行できます：
- Arduino IDEを閉じます。
- ターミナルを開き、実行：
  ```bash
  sudo arduino-ide
  ```
- 必要に応じて`arduino-ide`を正しいコマンドまたはパスに置き換えます（例：`/home/lzw/arduino-ide_2.3.6_Linux_64bit/arduino-ide`）。
- 再度アップロードを試みます。この方法は安全性が低いため、定期的な使用は避けてください。

---

### 修正の確認
これらの手順を実行した後、スケッチは正常にアップロードされ、Arduino UnoのLEDが期待通りに点滅するはずです。まだ問題が発生する場合は、以下の詳細を提供してください：
- `ls -l /dev/ttyUSB0`の出力（権限を確認するため）。
- Arduino IDEからの新しいエラーメッセージ。

さらに支援が必要な場合はお知らせください！
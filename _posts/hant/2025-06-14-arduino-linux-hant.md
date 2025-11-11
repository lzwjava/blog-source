---
audio: false
generated: true
lang: hant
layout: post
title: 在 Ubuntu 上安裝 Arduino IDE
translated: true
type: note
---

要在 Ubuntu Linux 上安裝 Arduino IDE，請按照以下步驟操作：

1. **下載 Arduino IDE**：
   - 前往 Arduino 官方網站：[https://www.arduino.cc/en/software](https://www.arduino.cc/en/software)
   - 在「Arduino IDE」部分，選擇「Linux 64 bits」下載選項（或適合您系統的版本，例如適用於 Raspberry Pi 的 Linux ARM）

2. **解壓下載的檔案**：
   - 下載的檔案是壓縮的 `.tar.xz` 歸檔檔案（例如 `arduino-1.8.19-linux64.tar.xz`）
   - 打開終端機並導航到下載目錄（例如 `cd ~/Downloads`）
   - 使用以下指令解壓檔案：
     ```bash
     tar -xf arduino-*.tar.xz
     ```
   - 這會建立一個類似 `arduino-1.8.19` 的資料夾

3. **移動到適當的目錄（可選）**：
   - 為了讓系統全域存取，請將解壓後的資料夾移動到 `/opt`（需要超級使用者權限）：
     ```bash
     sudo mv arduino-1.8.19 /opt/arduino
     ```

4. **執行安裝腳本**：
   - 導航到 Arduino 資料夾：
     ```bash
     cd /opt/arduino
     ```
   - 執行安裝腳本：
     ```bash
     sudo ./install.sh
     ```
   - 這會建立桌面捷徑並設定必要的權限

5. **將使用者加入 Dialout 群組**：
   - 為了透過序列埠存取 Arduino 開發板，請將您的使用者加入 `dialout` 群組：
     ```bash
     sudo usermod -a -G dialout $USER
     ```
   - 登出並重新登入，或重新啟動系統以使群組變更生效

6. **啟動 Arduino IDE**：
   - 如果您執行了 `install.sh` 腳本，可以從應用程式選單或搜尋「Arduino IDE」來啟動 IDE
   - 或者，直接從終端機執行：
     ```bash
     /opt/arduino/arduino
     ```

7. **更新 Arduino 開發板的權限（如果需要）**：
   - 連接 Arduino 時，請確保它被偵測到（例如 `/dev/ttyACM0` 或 `/dev/ttyUSB0`）
   - 如果遇到權限問題，請設定正確的權限：
     ```bash
     sudo chmod a+rw /dev/ttyACM0
     ```
   - 將 `/dev/ttyACM0` 替換為適當的埠

8. **驗證安裝**：
   - 透過 USB 連接您的 Arduino 開發板
   - 開啟 IDE，前往 **Tools > Board** 並選擇您的 Arduino 型號（例如 Arduino Uno）
   - 前往 **Tools > Port** 並選擇埠（例如 `/dev/ttyACM0`）
   - 嘗試上傳範例程式（例如 **File > Examples > 01.Basics > Blink**）以確認一切正常

**替代方法：透過 Snap 或 Flatpak 安裝**：
- **Snap**：
  ```bash
  sudo snap install arduino
  ```
- **Flatpak**：
  ```bash
  sudo flatpak install flathub cc.arduino.ArduinoIDE
  ```
- 這些方法簡化了安裝過程，但可能在權限或開發板偵測方面有限制

**注意事項**：
- 確保已安裝 Java，因為 Arduino IDE 需要它。如果需要，請安裝：
  ```bash
  sudo apt update
  sudo apt install default-jre
  ```
- 如需最新版本或疑難排解，請查閱 Arduino 論壇或[官方文件](https://www.arduino.cc/en/Guide/Linux)

如果您遇到問題，請告訴我您的 Ubuntu 版本或具體錯誤訊息以獲得針對性幫助！

---

既然您的 Arduino Uno 在 Ubuntu 上的 Arduino IDE 中被偵測到，並且您想要一個不使用麵包板或外部元件的簡單範例，這裡提供一個基本的程式，用於讓 Arduino Uno 上的內建 LED（連接到數位引腳 13）閃爍。這不需要任何額外硬體。

```cpp
void setup() {
  // put your setup code here, to run once:
  pinMode(LED_BUILTIN, OUTPUT); // 將內建 LED 引腳（引腳 13）設定為輸出
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(LED_BUILTIN, HIGH); // 開啟 LED
  delay(1000);                     // 等待 1 秒
  digitalWrite(LED_BUILTIN, LOW);  // 關閉 LED
  delay(1000);                     // 等待 1 秒
}
```

### 如何執行：
1. 開啟 Arduino IDE
2. 將上述程式碼複製並貼到 IDE 中
3. 確保您的 Arduino Uno 已透過 USB 連接並被偵測到：
   - 前往 **Tools > Board** 並選擇 **Arduino Uno**
   - 前往 **Tools > Port** 並選擇埠（例如 `/dev/ttyACM0` 或 `/dev/ttyUSB0`）
4. 點擊 **Upload** 按鈕（右箭頭圖示）以編譯並將程式上傳到您的 Arduino Uno
5. 上傳完成後，內建 LED（開發板上標記為「L」）應該會閃爍：亮起 1 秒，然後熄滅 1 秒，如此重複

### 功能說明：
- 在 `setup()` 中，`pinMode` 函數將內建 LED 引腳配置為輸出
- 在 `loop()` 中，`digitalWrite` 函數開啟 LED（`HIGH`）和關閉 LED（`LOW`），`delay` 在每個狀態之間暫停 1 秒，創造閃爍效果

### 注意事項：
- 不需要外部元件，因為 Arduino Uno 在引腳 13 上有一個內建 LED
- 如果 LED 沒有閃爍，請雙重檢查埠選擇或確保開發板正確連接。您也可以開啟 **Serial Monitor**（Tools > Serial Monitor）進行除錯，如果在 `setup()` 中加入 `Serial.begin(9600);` 並在 `loop()` 中列印訊息如 `Serial.println("Blink");`
- 如果想修改閃爍速度，請調整 `delay(1000)` 的值（例如 `delay(500)` 可實現更快的閃爍）

如果您遇到問題或想要另一個簡單範例，請告訴我！

---

錯誤訊息表明在嘗試將程式上傳到 Ubuntu 上的 Arduino Uno 時出現權限問題。Arduino IDE 無法存取序列埠 `/dev/ttyUSB0`，因為權限不足。以下是修復方法：

### 解決方案：修復序列埠權限

1. **將使用者加入 `dialout` 群組**：
   - 在 Ubuntu 中，`dialout` 群組通常控制對序列埠的存取。將您的使用者加入此群組：
     ```bash
     sudo usermod -a -G dialout $USER
     ```
   - 執行此指令後，登出並重新登入，或重新啟動系統以使變更生效：
     ```bash
     sudo reboot
     ```

2. **驗證埠**：
   - 重新啟動後，重新連接您的 Arduino Uno 並開啟 Arduino IDE
   - 前往 **Tools > Port** 並確保選擇了 `/dev/ttyUSB0`（或對於某些 Arduino 開發板為 `/dev/ttyACM0`）。如果沒有出現任何埠，請檢查 USB 連接或嘗試不同的纜線/埠

3. **暫時變更埠權限（可選）**：
   - 如果將使用者加入 `dialout` 群組後問題仍然存在，您可以手動設定埠的權限（這是暫時修復，權限在重新啟動後會重設）：
     ```bash
     sudo chmod a+rw /dev/ttyUSB0
     ```
   - 如果埠不同（例如 `/dev/ttyACM0`），請將 `/dev/ttyUSB0` 替換為正確的埠

4. **再次嘗試上傳**：
   - 在 Arduino IDE 中，點擊 **Upload** 按鈕上傳您的程式（例如之前的 LED 閃爍程式）
   - 如果上傳成功，您應該會看到 Arduino Uno 上的內建 LED 開始閃爍

### 其他疑難排解

- **檢查 Arduino 開發板和纜線**：
  - 確保 Arduino Uno 已透過 USB 正確連接並被 Ubuntu 識別。執行此指令以列出已連接的裝置：
    ```bash
    ls /dev/tty*
    ```
    當開發板插入時，尋找 `/dev/ttyUSB0` 或 `/dev/ttyACM0`
  - 如果開發板未被偵測到，請嘗試不同的 USB 纜線或埠

- **驗證開發板和埠設定**：
  - 在 Arduino IDE 中，確認 **Tools > Board** 設定為 **Arduino Uno**
  - 如果 `/dev/ttyUSB0` 沒有出現，請在拔下並重新插入開發板後嘗試 **Tools > Port**

- **以 Root 身份執行 Arduino IDE（暫時解決方法）**：
  - 如果上述步驟無效，您可以使用超級使用者權限執行 IDE 以繞過權限問題（不建議長期使用）：
    ```bash
    sudo arduino
    ```
    如果 Arduino IDE 可執行檔不在系統的 PATH 中，請將 `arduino` 替換為您的 Arduino IDE 可執行檔路徑（例如 `/opt/arduino/arduino`）

- **檢查衝突軟體**：
  - 其他軟體（例如 `brltty`，盲文顯示器驅動程式）可能會干擾序列埠。如果已安裝，請移除：
    ```bash
    sudo apt remove brltty
    ```

- **驅動程式問題**：
  - 一些 Arduino 複製版使用 CH340/CH341 晶片，需要驅動程式。如果需要，請安裝：
    ```bash
    sudo apt install linux-modules-extra-$(uname -r)
    ```
    然後重新連接開發板

### 確認修復
一旦權限問題解決，請再次嘗試上傳先前的閃爍程式：
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

如果您仍然遇到問題，請分享新的錯誤訊息或在終端機中執行 `ls -l /dev/ttyUSB0` 並提供輸出以協助進一步診斷

---

看來您在嘗試使用 Arduino IDE 在 Ubuntu 上上傳程式到 Arduino Uno 時遇到了問題。您提供的錯誤訊息是：

```
avrdude: ser_open(): can't open device "/dev/ttyUSB0": Permission denied
Failed uploading: uploading error: exit status 1
```

此錯誤表明 Arduino IDE 沒有必要的權限來存取您的 Arduino Uno 所連接的序列埠（`/dev/ttyUSB0`）。這在像 Ubuntu 這樣的 Linux 系統上是一個常見問題，原因是序列埠存取的管理方式。以下是修復此問題的逐步指南。

---

### 解決方案：修復序列埠權限問題

#### 1. 將使用者加入 `dialout` 群組
在 Ubuntu 中，`dialout` 群組控制對序列埠的存取。為了解決權限問題，您需要將您的使用者加入此群組。

- 按 `Ctrl + Alt + T` 開啟終端機
- 執行以下指令：
  ```bash
  sudo usermod -a -G dialout $USER
  ```
- 此指令將您目前的使用者加入 `dialout` 群組。`$USER` 變數會自動使用您的使用者名稱

#### 2. 登出並重新登入
為了使群組變更生效，您需要登出目前的工作階段並重新登入。或者，您可以重新啟動系統。

- **登出並重新登入：**
  - 儲存任何開啟的工作
  - 點擊 Ubuntu 桌面右上角的使用者名稱並選擇「Log Out」
  - 使用您的使用者名稱和密碼重新登入
- **重新啟動（可選）：**
  - 在終端機中執行此指令：
    ```bash
    sudo reboot
    ```
  - 等待系統重新啟動

#### 3. 驗證序列埠
重新登入後，確保您的 Arduino Uno 被系統正確識別。

- 重新連接您的 Arduino Uno 到 USB 埠
- 開啟 Arduino IDE
- 在選單中前往 **Tools > Port** 並檢查是否列出並選擇了 `/dev/ttyUSB0`（或對於某些 Arduino 開發板為 `/dev/ttyACM0`）
- 如果埠沒有出現：
  - 拔下並重新插入 Arduino Uno
  - 檢查 USB 連接或嘗試不同的纜線/埠

#### 4. 再次上傳程式
選擇正確的埠後，再次嘗試上傳您的程式：

```cpp
void setup() {
  pinMode(LED_BUILTIN, OUTPUT); // 將內建 LED 引腳（引腳 13）設定為輸出
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH); // 開啟 LED
  delay(1000);                     // 等待 1 秒
  digitalWrite(LED_BUILTIN, LOW);  // 關閉 LED
  delay(1000);                     // 等待 1 秒
}
```

- 點擊 Arduino IDE 中的 **Upload** 按鈕（右箭頭圖示）
- 如果成功，您 Arduino Uno 上的內建 LED 應該開始閃爍（亮起 1 秒，熄滅 1 秒）

---

### 其他疑難排解
如果上述步驟無法解決問題，請嘗試這些額外檢查：

#### 檢查群組成員資格
驗證您的使用者是否是 `dialout` 群組的一部分：
- 在終端機中執行此指令：
  ```bash
  groups $USER
  ```
- 在輸出中尋找 `dialout`。如果缺少，請重複步驟 1 並確保您登出/登入或重新啟動

#### 暫時權限修復（不建議長期使用）
如果您需要快速修復，可以手動變更序列埠的權限：
- 執行：
  ```bash
  sudo chmod a+rw /dev/ttyUSB0
  ```
- 然後再次嘗試上傳。注意：這是暫時的，會在拔下 Arduino 或重新啟動後重設

#### 檢查衝突軟體
某些軟體，如 `brltty`（盲文顯示器驅動程式），可能會干擾序列埠。要移除它：
- 執行：
  ```bash
  sudo apt remove brltty
  ```
- 重新連接您的 Arduino 並再次嘗試

#### 驗證 Arduino 連接
確保 Ubuntu 識別您的 Arduino：
- 執行：
  ```bash
  ls /dev/tty*
  ```
- 當 Arduino 插入時，尋找 `/dev/ttyUSB0` 或 `/dev/ttyACM0`。如果缺少，請檢查您的 USB 纜線或埠

#### 以 Root 身份執行 Arduino IDE（暫時解決方法）
作為最後的手段，您可以使用超級使用者權限執行 IDE：
- 關閉 Arduino IDE
- 開啟終端機並執行：
  ```bash
  sudo arduino-ide
  ```
- 如果需要，請將 `arduino-ide` 替換為正確的指令或路徑（例如 `/home/lzw/arduino-ide_2.3.6_Linux_64bit/arduino-ide`）
- 再次嘗試上傳。避免經常使用此方法，因為它較不安全

---

### 確認修復
按照這些步驟操作後，您的程式應該會成功上傳，並且 Arduino Uno 上的 LED 應該會按預期閃爍。如果您仍然遇到問題，請提供其他詳細資訊，例如：
- `ls -l /dev/ttyUSB0` 的輸出（用於檢查權限）
- Arduino IDE 中的任何新錯誤訊息

如果您需要進一步協助，請告訴我！
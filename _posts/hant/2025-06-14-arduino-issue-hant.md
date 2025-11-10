---
audio: false
generated: true
lang: hant
layout: post
title: Arduino 問題
translated: true
type: note
---

您看到的錯誤訊息表明 Arduino IDE（透過 `avrdude`）無法與您的 Arduino 開發板通訊以上傳程式。`stk500_recv(): programmer is not responding` 和 `stk500_getsync(): not in sync: resp=0x00` 錯誤通常表示電腦與 Arduino 之間的通訊出現問題。由於您使用的是 `/dev/ttyUSB0`（如您之前的查詢所示），這表明是 USB 轉序列埠連接，很可能是 Arduino Uno 或帶有獨立 USB 轉序列埠晶片的相容開發板（例如 CH340、FT232R）。

以下是逐步疑難排解和解決問題的指南，以及在上傳成功後如何驗證和監控日誌。

### 理解錯誤
- **程式大小**：程式使用 2678 位元組（佔 32,256 位元組的 8%）和 314 位元組的 RAM（佔 2048 位元組的 15%），這完全在 Arduino 的限制範圍內，因此程式碼本身不是問題。
- **錯誤原因**：`stk500` 錯誤表示 `avrdude`（用於上傳程式的工具）無法與 Arduino 的開機程式建立連線。這可能是由於：
  - 不正確的埠或開發板設定。
  - 實體連接問題（傳輸線、USB 埠或開發板）。
  - `/dev/ttyUSB0` 的權限問題。
  - USB 轉序列埠晶片的驅動程式問題。
  - 開機程式或開發板故障。

### 疑難排解步驟
請按照以下步驟解決問題：

1. **驗證開發板和序列埠設定**
   - 在 Arduino IDE 中：
     - 前往 `Tools > Board` 並確保選擇了正確的開發板（例如，對於 Uno 或相容開發板，選擇 “Arduino Uno”）。
     - 前往 `Tools > Port` 並確認選擇了 `/dev/ttyUSB0`。如果未列出，則可能系統未偵測到 Arduino。
   - 在終端機中執行 `ls /dev/ttyUSB*` 以確認序列埠存在。如果缺少該埠，則表示系統未偵測到 Arduino。
   - 如果出現多個序列埠（例如 `/dev/ttyUSB1`），請逐一嘗試。

2. **檢查 `/dev/ttyUSB0` 的權限**
   - 您之前執行的 `ls -alrt /dev/ttyUSB0` 輸出顯示 `crw-rw---- 1 root dialout`，這表示只有 `root` 和 `dialout` 群組可以存取該序列埠。
   - 確保您的使用者位於 `dialout` 群組中：
     ```bash
     groups
     ```
     如果未列出 `dialout`，請新增您的使用者：
     ```bash
     sudo usermod -a -G dialout $USER
     ```
     登出並重新登入（或重新啟動）以使變更生效。
   - 或者，以 root 身份執行 Arduino IDE（不建議長期使用）：
     ```bash
     sudo arduino
     ```
   - 如果權限正確但問題仍然存在，請繼續下一步。

3. **檢查實體連接**
   - **USB 傳輸線**：確保您使用的是**資料 USB 傳輸線**，而不是僅供充電的傳輸線。一些廉價傳輸線不支援資料傳輸。
   - **USB 埠**：嘗試使用電腦上的其他 USB 埠或另一台電腦。
   - **Arduino 開發板**：檢查是否有生命跡象（例如，電源 LED 亮起，或如果先前的程式正在執行，則 LED 閃爍）。如果開發板無回應，則可能已損壞或未通電。
   - **重設開發板**：在上傳時短按 Arduino 上的重設按鈕。這會強制重新啟動開機程式，有助於與 `avrdude` 同步。

4. **檢查 USB 轉序列埠驅動程式**
   - 由於您使用的是 Linux 且使用 `/dev/ttyUSB0`，您的開發板可能使用 USB 轉序列埠晶片，例如 CH340/CH341、FT232R 或 ATmega16U2。
   - 驗證驅動程式是否已安裝：
     ```bash
     lsmod | grep usbserial
     ```
     您應該會看到 `ch341`、`ftdi_sio` 或類似的模組。
   - 如果未偵測到序列埠，請安裝常見晶片的驅動程式：
     ```bash
     sudo apt-get install linux-modules-extra-$(uname -r)
     ```
   - 對於 CH340/CH341 晶片，您可能需要特定的驅動程式。檢查裝置是否被識別：
     ```bash
     dmesg | grep usb
     ```
     尋找提及 `ch341`、`ftdi` 或 USB 裝置的行。如果沒有出現任何內容，則可能不支援該晶片，或者開發板/傳輸線有故障。

5. **強制進入開機程式模式**
   - 一些 Arduino 開發板在快速按兩下重設按鈕時會進入開機程式模式。請嘗試以下操作：
     1. 按兩下重設按鈕（您可能會看到板載 LED 快速閃爍）。
     2. 立即在 Arduino IDE 中開始上傳。
   - 這確保開機程式在上傳嘗試期間處於活動狀態。

6. **使用最簡程式進行測試**
   - 為了排除先前程式的問題，請嘗試上傳一個最簡程式：
     ```cpp
     void setup() {
       Serial.begin(9600);
       pinMode(LED_BUILTIN, OUTPUT);
     }
     void loop() {
       Serial.println("Test");
       digitalWrite(LED_BUILTIN, HIGH);
       delay(1000);
       digitalWrite(LED_BUILTIN, LOW);
       delay(1000);
     }
     ```
   - 如果此程式上傳成功，則問題可能與先前的程式有關（考慮到程式大小正常，這種可能性不大）。

7. **檢查硬體問題**
   - 如果上述步驟失敗，則 Arduino 的開機程式或 USB 轉序列埠晶片可能已損壞，或者開發板可能已損壞。
   - 如果有其他 Arduino 開發板，請進行測試。
   - 如果您懷疑是開機程式問題，則可能需要使用 ISP 程式設計器或另一個 Arduino 作為 ISP 來重新燒錄開機程式。

### 上傳成功後檢視日誌
解決上傳問題並上傳修改後的 Fibonacci 程式（來自先前的回覆）後，您可以檢視日誌：

1. **Arduino IDE 序列監控視窗**：
   - 上傳後，前往 `Tools > Serial Monitor` 或按 `Ctrl+Shift+M`。
   - 將鮑率設定為 **9600**（與程式碼中的 `Serial.begin(9600)` 匹配）。
   - 您應該會看到類似以下的輸出：
     ```
     Starting Fibonacci LED Blink...
     Index: 0, Delay: 0s, Direction: Forward
     Index: 1, Delay: 1s, Direction: Forward
     ...
     ```

2. **終端機程式（minicom 或 screen）**：
   - 使用 `minicom`：
     ```bash
     minicom -D /dev/ttyUSB0 -b 9600
     ```
     按 `Ctrl+A`，然後按 `X` 退出。
   - 或使用 `screen`：
     ```bash
     screen /dev/ttyUSB0 9600
     ```
     按 `Ctrl+A`，然後按 `\` 退出。
   - 確保您的使用者在 `dialout` 群組中以避免權限問題。

3. **驗證序列埠**：
   - 如果 `/dev/ttyUSB0` 無效，請檢查 `dmesg` 以找到正確的序列埠：
     ```bash
     dmesg | grep tty
     ```
     尋找類似 `[1234.567890] usb 1-1: ch341-uart converter now attached to ttyUSB0` 的行。

### 日誌輸出範例
如果上傳成功，您將看到類似以下的日誌：
```
Starting Fibonacci LED Blink...
Index: 0, Delay: 0s, Direction: Forward
Index: 1, Delay: 1s, Direction: Forward
Index: 2, Delay: 1s, Direction: Forward
Index: 3, Delay: 2s, Direction: Forward
...
Switching to Backward
Index: 7, Delay: 13s, Direction: Backward
...
```

### 其他提示
- **詳細上傳輸出**：在 Arduino IDE 中，前往 `File > Preferences`，勾選 “Show verbose output during: Upload”，然後再次嘗試上傳。這可能會提供有關失敗的更多線索。
- **開發板複製品或非標準晶片**：如果您使用的是非官方 Arduino（例如帶有 CH340 晶片的開發板），請確保驅動程式已安裝且開發板類型匹配（例如，在某些情況下，即使對於複製品，也選擇 “Arduino Uno”）。
- **重設時機**：如果開發板有自動重設問題，請在 IDE 狀態列顯示 “Uploading…” 時手動按下重設按鈕。

### 如果問題仍然存在
如果這些步驟都無效，請提供：
- 確切的 Arduino 開發板型號（例如 Uno、Mega 或複製品）。
- 插入 Arduino 後 `dmesg | grep usb` 的輸出。
- 開發板的電源 LED 或其他 LED 是否亮起。
- 嘗試使用不同 USB 傳輸線或電腦的結果。

這將有助於縮小問題範圍，確定是硬體、驅動程式還是設定問題。目前，請先從檢查序列埠、權限和傳輸線開始，因為這些是最常見的原因。

---

根據您提供的日誌，您似乎在使用 Arduino IDE 於 Linux 上對 Arduino 開發板進行除錯和上傳程式時遇到問題。以下是逐步疑難排解和解決這些問題的指南：

---

### **1. 解決除錯錯誤**
- **問題**：日誌重複顯示 `arduino:avr:uno` 開發板不支援除錯。
- **說明**：Arduino Uno 不支援 Arduino IDE 中的除錯功能。除錯僅在特定開發板上可用，例如 Arduino Zero 或 MKR 系列。
- **解決方案**：
  - 如果您嘗試對程式進行除錯，則需要切換到支援除錯的開發板（例如 Arduino Zero 或 MKR 系列）。
  - 如果您並非有意進行除錯，而只是想上傳程式，則此錯誤不會阻止上傳。您可以忽略它並專注於下面的上傳問題。確保您沒有意外點擊 IDE 中的 "Start Debugging" 選項。

---

### **2. 解決上傳序列埠偵測問題**
- **問題**：日誌顯示 "Upload port detection failed" 和 "User abort" 錯誤，表明 IDE 無法可靠地偵測或存取序列埠（`/dev/ttyUSB0`）。
- **說明**：這可能是由於權限問題、不正確的設定或實體連接問題，這些問題在 Linux 系統上很常見。
- **解決方案**：

#### **檢查 `/dev/ttyUSB0` 的權限**
- 在 Linux 上，Arduino IDE 需要權限才能存取序列埠，這些序列埠通常由 `dialout` 群組擁有。
- **步驟**：
  1. 檢查您的使用者是否在 `dialout` 群組中：
     ```bash
     groups
     ```
     在輸出中尋找 `dialout`。
  2. 如果未列出，請將您的使用者新增至群組：
     ```bash
     sudo usermod -a -G dialout $USER
     ```
  3. 登出並重新登入（或重新啟動）以使變更生效。
  4. 重新連接您的 Arduino，並檢查 `/dev/ttyUSB0` 是否出現在 IDE 的 `Tools > Port` 下。

#### **驗證開發板和序列埠設定**
- 確保 IDE 設定正確：
  - 前往 `Tools > Board` 並選擇 **Arduino Uno**（如果您使用其他開發板，請選擇正確的型號）。
  - 前往 `Tools > Port` 並選擇 **/dev/ttyUSB0**。如果未列出，請繼續下一步。

#### **檢查實體連接**
- **步驟**：
  1. 確認 Arduino 是透過**資料 USB 傳輸線**連接（而非僅充電傳輸線）。一些傳輸線僅提供電力，無法用於上傳。
  2. 嘗試使用電腦上的其他 USB 埠或不同的傳輸線，以排除硬體問題。
  3. 確保 Arduino 已通電（電源 LED 應亮起）。
  4. 執行以下指令檢查是否偵測到序列埠：
     ```bash
     ls /dev/ttyUSB*
     ```
     如果未出現 `/dev/ttyUSB0`，則表示系統未識別開發板（請參閱下面的「檢查驅動程式問題」）。

---

### **3. 疑難排解上傳失敗**
- **問題**："User abort" 訊息表明上傳過程被中斷或無法與開發板同步。
- **解決方案**：

#### **上傳期間手動重設**
- 有時 Arduino 的開機程式需要手動重設才能與 IDE 同步。
- **步驟**：
  1. 在 IDE 中，點擊**上傳**按鈕（右箭頭圖示）。
  2. 當 "Compiling sketch..." 訊息變為 "Uploading..." 時，按下並放開 Arduino 上的**重設按鈕**。
  3. 這確保開發板準備好接收程式。

#### **檢查驅動程式問題**
- 如果未偵測到 `/dev/ttyUSB0`，則可能存在驅動程式問題，特別是對於使用 CH340/CH341 等晶片（而非標準 FTDI 或 ATmega16U2）的複製開發板。
- **步驟**：
  1. 插入 Arduino 後，執行：
     ```bash
     dmesg | grep usb
     ```
     尋找提及 `ch341`、`ftdi` 或類似 USB 轉序列埠驅動程式的行。
  2. 如果沒有出現任何內容，或者出現錯誤，您可能需要安裝驅動程式：
     - 對於 CH340/CH341 晶片（常見於複製品）：
       ```bash
       sudo apt-get install linux-modules-extra-$(uname -r)
       ```
     - 重新插入 Arduino 並使用 `ls /dev/ttyUSB*` 再次檢查。
  3. 如果仍未偵測到序列埠，則您的開發板或傳輸線可能故障。

#### **嘗試最簡程式**
- 使用簡單的程式進行測試以隔離問題：
  - 開啟 IDE，前往 `File > Examples > 01.Basics > Blink`。
  - 上傳此程式。如果成功，則問題可能與您的原始程式有關。

---

### **4. 其他疑難排解提示**
- **啟用詳細輸出**：
  - 在 IDE 中前往 `File > Preferences`，並勾選 **Show verbose output during: Upload**。
  - 這在您嘗試上傳時提供更詳細的錯誤訊息，有助於找出問題。
- **監控序列輸出**：
  - 上傳成功後，使用序列監控視窗（`Tools > Serial Monitor`）檢查程式的輸出（例如 `Serial.println` 陳述式）。
  - 或者，使用終端機程式：
    ```bash
    minicom -D /dev/ttyUSB0 -b 9600
    ```
    將鮑率（例如 9600）與您程式中的 `Serial.begin()` 匹配。

---

### **修復摘要**
- **除錯**：Arduino Uno 不支援除錯。如果需要除錯，請使用支援的開發板，否則請忽略此錯誤以上傳程式。
- **權限**：將您的使用者新增至 `dialout` 群組以存取 `/dev/ttyUSB0`。
- **序列埠偵測**：確保 `/dev/ttyUSB0` 在 `Tools > Port` 下列出且開發板已實體連接。
- **上傳同步**：在上傳期間按下重設按鈕以協助開機程式同步。

如果您按照這些步驟操作後仍然遇到問題，請嘗試使用不同的 Arduino 開發板或傳輸線，或在 Arduino 論壇上尋求幫助，並提供有關您的設定的詳細資訊（例如開發板類型、Linux 發行版和確切錯誤）。請告訴我進展如何！
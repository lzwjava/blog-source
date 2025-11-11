---
audio: false
generated: true
lang: hant
layout: post
title: 將 iPad 連接至 HDMI 顯示器
translated: true
type: note
---

要使用 HDMI 將 iPad 連接到顯示器並觀看電影（例如透過 Infuse 等應用程式從 Ubuntu 筆記型電腦的 Nginx 伺服器串流），您需要合適的轉接器和簡單的設定。iPad 沒有原生 HDMI 埠，但 Apple 提供官方轉接器，也有第三方選擇。以下是逐步操作指南，專門針對您想無縫在顯示器上觀看電影的目標。

### 所需設備
1. **配備 Lightning 或 USB-C 埠的 iPad**
   - 檢查您的 iPad 型號：舊款 iPad（如 iPad Air 2、iPad Mini 4）使用 Lightning 埠，而新款（如 2018 年以後的 iPad Pro、第 4 代 iPad Air 及以上）使用 USB-C。
   - 您未指定 iPad 型號，因此我將涵蓋兩種可能性。

2. **HDMI 轉接器**
   - **Lightning iPad**：Apple 的 **Lightning 轉 HDMI 轉接器**（官方名稱為「Lightning Digital AV Adapter」，約 49 美元）。
   - **USB-C iPad**：Apple 的 **USB-C Digital AV Multiport Adapter**（約 69 美元）或第三方 USB-C 轉 HDMI 轉接器（確保支援視訊輸出，約 15-30 美元）。
   - 第三方轉接器可用，但可能不支援所有功能（如 HDR 或高更新率）；Apple 的轉接器在即插即用方面更可靠。

3. **HDMI 線**
   - 任何標準 HDMI 線（例如，若您的顯示器和 iPad 支援 4K，則使用 HDMI 2.0）。長度取決於您的設定 — 5-10 英尺適用於近距離連接。

4. **具備 HDMI 輸入的顯示器**
   - 您已擁有此設備，請確保其已開機並設定為正確的 HDMI 輸入。

5. **可選：電源**
   - Apple 的轉接器通常有一個額外埠（Lightning 或 USB-C）用於充電。若觀看時間較長，請連接 iPad 充電器以保持電力。

### 將 iPad 連接到顯示器的步驟
1. **選擇正確的轉接器**
   - Lightning iPad：將 Lightning Digital AV Adapter 插入 iPad 的 Lightning 埠。
   - USB-C iPad：將 USB-C Digital AV Multiport Adapter（或 USB-C 轉 HDMI 轉接器）插入 iPad 的 USB-C 埠。

2. **連接 HDMI 線**
   - 將 HDMI 線的一端插入轉接器的 HDMI 埠。
   - 將另一端插入顯示器的 HDMI 輸入埠。

3. **連接電源（可選）**
   - 若需長時間使用，請將 iPad 充電器連接到轉接器的額外埠（Lightning 或 USB-C）並插入電源插座，以避免電池耗盡。

4. **開啟顯示器**
   - 開啟顯示器，並使用其輸入/來源按鈕選擇您連接的 HDMI 埠（例如 HDMI 1 或 HDMI 2）。

5. **iPad 螢幕鏡像輸出**
   - 連接後，iPad 螢幕應自動鏡像到顯示器。您將在顯示器上看到 iPad 的主畫面。
   - 若未自動鏡像：
     - 從右上角向下滑動（配備 Face ID 的 iPad）或從底部向上滑動（配備主畫面按鈕的舊款 iPad）以開啟 **控制中心**。
     - 點擊 **螢幕鏡像輸出** 圖示（兩個重疊的矩形）。
     - 選擇轉接器（可能顯示為「Apple AV Adapter」或類似名稱）。鏡像應開始。

6. **調整顯示設定（可選）**
   - 在 iPad 上，前往 **設定 > 顯示器與亮度**。
     - 若顯示器支援更高解析度（如 1080p 或 4K），iPad 會自動調整，但您可在此微調縮放或亮度。
     - 大多數內容（如電影）會縮放以符合顯示器的長寬比。

7. **播放電影**
   - 在 iPad 上開啟 **Infuse**（或任何視訊播放器）。
   - 若使用 Infuse 從 Ubuntu Nginx 伺服器串流：
     - 設定 Infuse 連接到您的伺服器（例如 `http://<筆記型電腦-ip>:80/movies`，其中 `<筆記型電腦-ip>` 是您 Ubuntu 機器的 IP，如 `192.168.1.100`）。
     - 選擇電影，點擊播放，它將在顯示器上以全螢幕顯示。
   - 將 iPad 旋轉至橫向模式，或在應用程式中點擊全螢幕圖示以獲得最佳觀看體驗。

### 音訊考量
- **顯示器具備揚聲器**：音訊應透過 HDMI 從顯示器揚聲器播放（若支援）。
- **顯示器無揚聲器**：使用 iPad 的揚聲器，或將有線耳機連接到轉接器的 Lightning/USB-C 埠（可能需要 3.5mm 轉接器），或將藍牙耳機與 iPad 配對。

### 設定提示
- **解析度支援**：Lightning 轉接器最高支援 1080p；USB-C 轉接器最高支援 4K（取決於您的 iPad 和顯示器）。請檢查顯示器的最高解析度和電影檔案品質。
- **控制**：您將直接在 iPad 觸控螢幕上控制播放。由於 Infuse 不支援網路遙控（如前所述），您需要直接操作 iPad — 將其放在附近或使用支架。
- **Nginx 伺服器存取**：確保您的 Ubuntu 筆記型電腦和 iPad 處於同一 Wi-Fi 網路。在 iPad 上開啟瀏覽器並訪問 `http://<筆記型電腦-ip>` 以測試 Nginx 伺服器 — 若設定正確，您應看到電影檔案。

### 疑難排解
- **無視訊**：確保所有連接牢固、顯示器輸入源正確，且轉接器相容（某些廉價第三方轉接器可能失效）。
- **延遲或卡頓**：若從 Nginx 串流，請檢查 Wi-Fi 訊號強度或電影檔案大小 — 大型 4K 檔案可能需要更強的連接。
- **黑邊**：若電影未填滿螢幕，是由於長寬比差異（例如 16:9 電影在 4:3 顯示器上播放）。使用 Infuse 的縮放選項進行調整。

### 總結
此設定讓 iPad 作為播放設備，從 Ubuntu 筆記型電腦串流並透過 HDMI 輸出到顯示器。連接後非常簡單 — 只需插入轉接器，在 Infuse 中選擇電影即可觀看。由於您希望盡量簡便且無需額外設備（如 Fire TV Stick），此方法有效利用了您現有的 iPad 和顯示器。若您的 iPad 較舊或儲存空間不足，直接從 Nginx 串流可保持輕量級運作。祝您觀影愉快！
---
audio: false
generated: true
lang: hant
layout: post
title: 控制台應用程式
translated: true
type: note
---

要對 Infuse（一款 Mac 應用程式）中的「解複用串流時無法開啟輸入串流」錯誤進行疑難排解並查看更詳細的日誌，你可以使用 Mac 上的工具。由於查詢中提到「iOS 或 Xcode 工具」但指定 Infuse 為 Mac 應用程式，很可能你是想使用 Xcode 或相關的 macOS 工具來檢查 Mac 版 Infuse 的日誌。以下是逐步指引，協助你存取這些日誌。

### 適用於 Mac 版 Infuse（主要方法：Console 應用程式）
根據你的查詢，Infuse 被識別為 Mac 應用程式，查看其日誌最直接的方法是使用 **Console** 應用程式，該應用程式內建於 macOS，專用於顯示系統和應用程式日誌。

1. **開啟 Console 應用程式**：
   - 啟動 **Console** 應用程式，位於 **應用程式** > **工具程式** > **Console**，或使用 Spotlight 搜尋（按下 Cmd + 空格鍵，然後輸入 "Console"）。

2. **篩選 Infuse 的日誌**：
   - 在 Console 應用程式中，使用右上角的搜尋欄。
   - 輸入 "Infuse" 或應用程式的程序名稱（可能是 "Infuse" 或類似名稱）來篩選與該應用程式相關的日誌。

3. **重現錯誤**：
   - 在 Console 應用程式開啟且篩選功能啟用的情況下，播放 Infuse 中觸發「解複用串流時無法開啟輸入串流」錯誤的影片。
   - 這可確保相關日誌被即時捕捉。

4. **分析日誌**：
   - 尋找錯誤訊息、警告或詳細輸出，這些可能解釋為何在解複用（分離音訊和視訊串流的過程）期間無法開啟輸入串流。
   - 關鍵字如 "error"、"fail" 或 "demux" 可能有助於找出問題。

### 若你指的是 iOS 版 Infuse（使用 Xcode）
若你原本想為 iOS 版 Infuse 進行除錯（儘管查詢中說是「Mac 應用程式」），你可以使用 **Xcode**（Apple 的開發工具）來存取 iOS 裝置的日誌。方法如下：

1. **連接你的 iOS 裝置**：
   - 使用 USB 線將 iPhone 或 iPad 連接到 Mac。

2. **開啟 Xcode**：
   - 在 Mac 上啟動 **Xcode**。如果尚未安裝，請從 Mac App Store 下載。

3. **存取裝置與模擬器**：
   - 在 Xcode 中，從選單列前往 **Window** > **Devices and Simulators**。

4. **選擇你的裝置**：
   - 在開啟的視窗中，於左側邊欄找到已連接的 iOS 裝置並點選它。

5. **查看日誌**：
   - 點擊 **Open Console** 或 **View Device Logs**（選項可能因 Xcode 版本而異）。
   - 這將開啟一個日誌檢視器，顯示來自你裝置的所有活動。

6. **篩選 Infuse 的日誌**：
   - 使用日誌檢視器中的搜尋或篩選選項，輸入 "Infuse" 或應用程式的套件識別碼（例如，若已知為 `com.firecore.Infuse`）來縮小條目範圍。
   - 在控制台開啟時，於 iOS 裝置上重現錯誤以捕捉相關日誌。

### 其他選項
- **檢查崩潰報告**：
  - **Mac**：如果 Infuse 崩潰，請檢查 `~/Library/Logs/DiagnosticReports` 或 `/Library/Logs/DiagnosticReports` 中名為 "Infuse" 並帶有時間戳記的崩潰日誌。
  - **iOS**：在 Xcode 的 **Devices and Simulators** 視窗中，Infuse 的崩潰日誌可能會出現在你裝置的日誌下。

- **在 Infuse 中啟用除錯日誌記錄**：
  - 某些應用程式（包括 Infuse）可能提供除錯模式或詳細日誌記錄選項。開啟 Mac（或 iOS 裝置）上 Infuse 的設定或偏好設定，查看是否有此功能。若啟用，這可能會產生更詳細的日誌，可透過上述方法查看。

- **iOS 的替代方案（Console 應用程式）**：
  - 將 iOS 裝置連接到 Mac，開啟 **Console** 應用程式，並從左側邊欄選擇你的裝置。透過 "Infuse" 篩選日誌，即可查看即時輸出，無需使用 Xcode。

### 注意事項
- 「解複用串流時無法開啟輸入串流」錯誤表示 Infuse 嘗試處理的媒體檔案或網路串流出現問題。日誌可能揭示是否為檔案損毀、編解碼器不相容或連線問題。
- 由於 Infuse 是第三方應用程式，進階除錯（例如將 Xcode 附加至程序）若沒有開發者存取權限則不太可能實現，因此 Console 應用程式（適用於 Mac）或裝置日誌（適用於 iOS）是你最佳的選擇。

遵循這些步驟，你將能夠收集更多日誌來診斷 Infuse 中的錯誤，無論是在 Mac 還是 iOS 上。若問題持續，請考慮查看 Infuse 的支援文件或論壇以獲取應用程式特定的日誌記錄提示。
---
audio: false
generated: true
lang: hant
layout: post
title: 樹莓派 5：強勁多用途
translated: true
type: note
---

Raspberry Pi 5 由樹莓派基金會於 2023 年 10 月推出，是廣受歡迎的單板電腦系列最新版本，專為愛好者、教育工作者及專業人士提供高效能、多功能且價格相宜的解決方案。承襲前代產品的成功基礎，Raspberry Pi 5 在處理效能、連接性與功能方面均有顯著升級，使其適用於從教育項目到工業自動化及進階運算任務等廣泛應用場景。以下將全面介紹 Raspberry Pi 5，涵蓋其歷史、規格、特色、設定流程及應用領域。

---

### **概述與歷史**
樹莓派系列始於 2012 年，其使命在於提供一個價格實惠、易於使用的程式設計與計算學習平台。最初針對學生與愛好者設計，樹莓派憑藉其緊湊設計、低功耗與多功能性，迅速在開發者與工程師群體中流行起來。每一代產品皆在效能與功能上有所提升，而 Raspberry Pi 5 更標誌著相較 2019 年推出的 Raspberry Pi 4 實現了重大飛躍。

Raspberry Pi 5 於 2023 年 9 月 28 日發布並隨即開放預購，是首款採用自行設計晶片（RP1 I/O 控制器）的型號，並引入了如 PCIe 支援等先進功能，以實現更快的儲存選項。其價格為 4GB 型號 60 美元、8GB 型號 80 美元、2GB 型號（2024 年 8 月推出）50 美元，以及 16GB 型號（2025 年 1 月推出）120 美元，持續提供經濟實惠且功能強大的運算解決方案。[](https://www.raspberrypi.com/products/raspberry-pi-5/)[](https://www.raspberrypi.com/news/introducing-raspberry-pi-5/)

---

### **關鍵規格**
Raspberry Pi 5 搭載一系列強勁的硬體組件，提供較 Raspberry Pi 4 高出 2–3 倍的效能表現。其核心規格如下：

- **處理器**：Broadcom BCM2712，一款 2.4GHz 四核 64 位元 ARM Cortex-A76 CPU，具備加密擴充功能、每核 512KB L2 快取及 2MB 共享 L3 快取。此 CPU 效能遠勝 Raspberry Pi 4 的 Cortex-A72，能更好地應對桌面運算與模擬等需求較高的任務。[](https://www.raspberrypi.com/products/raspberry-pi-5/)[](https://www.zimaspace.com/blog/raspberry-pi-5-everything-you-need-to-know.html)
- **GPU**：VideoCore VII GPU，支援 OpenGL ES 3.1 與 Vulkan 1.2，可透過 micro HDMI 端口驅動雙 4K 顯示器 @60Hz。[](https://www.linkedin.com/pulse/introduction-raspberry-pi-5-specs-harshvardhan-mishra-wkbmf)
- **記憶體**：提供 2GB、4GB、8GB 及 16GB LPDDR4X-4267 SDRAM 版本，記憶體頻寬較 Raspberry Pi 4 更快。[](https://wagnerstechtalk.com/rpi5/)[](https://www.raspberrypi.com/products/raspberry-pi-5/)
- **儲存**：
  - 支援高速 SDR104 模式的 MicroSD 卡插槽（建議：Raspberry Pi OS 使用 32GB 或更高，Lite 版使用 16GB）。由於 MBR 限制，不支援超過 2TB 的容量。
  - 透過可選的 HAT 提供 PCIe 介面以連接 M.2 NVMe SSD，實現更快的啟動與資料傳輸速度。[](https://www.raspberrypi.com/documentation/computers/getting-started.html)[](https://www.raspberrypi.com/products/raspberry-pi-5/)
- **連接性**：
  - 雙頻 2.4GHz 與 5GHz 802.11ac Wi-Fi。
  - Bluetooth 5.0 與 Bluetooth Low Energy (BLE)。
  - 具備 Power over Ethernet (PoE) 支援的 Gigabit 乙太網路（需搭配 PoE+ HAT）。
  - 2x USB 3.0 端口（5Gbps 同步運作）與 2x USB 2.0 端口。
  - 40 針 GPIO 接頭，用於連接感測器、顯示器及其他周邊裝置。
  - 2x micro HDMI 端口，支援雙 4K@60Hz 輸出。
  - 2x 4 通道 MIPI 相機/顯示器收發器（可互換用於一組相機與一組顯示器，或兩組相同裝置）。
  - 專用 UART 連接器，用於除錯（921,600bps）。[](https://www.linkedin.com/pulse/introduction-raspberry-pi-5-specs-harshvardhan-mishra-wkbmf)[](https://www.waveshare.com/wiki/Raspberry_Pi_5)
- **電源**：需使用 5V/5A USB-C 電源供應器（例如 Raspberry Pi 27W USB-C 電源供應器）。電源供應不足可能導致系統不穩定。[](https://www.raspberrypi.com/products/raspberry-pi-5/)
- **即時時鐘 (RTC)**：內建 RTC 並配備電池備份連接器 (J5)，無需在斷電時使用外部時鐘模組。[](https://en.wikipedia.org/wiki/Raspberry_Pi)
- **其他功能**：
  - RP1 I/O 控制器，由樹莓派自行設計的客製化晶片，用於提升 I/O 效能。
  - 電源開關按鈕，為系列中首見。
  - 相容 M.2 HAT+，可連接 NVMe SSD 及其他 PCIe 裝置。[](https://www.tomshardware.com/reviews/raspberry-pi-5)[](https://www.raspberrypi.com/news/introducing-raspberry-pi-5/)

---

### **外觀設計**
Raspberry Pi 5 保留了前代旗艦型號的信用卡尺寸外形（85mm x 56mm），確保與多數現有設定的相容性。然而，由於佈局變更與熱管理需求提升，需使用新款外殼。官方 Raspberry Pi 5 外殼（10 美元）包含整合式風扇以實現主動散熱，而主動式散熱器（5 美元）則建議用於高負載工作以防熱節流。該電路板亦因改進的製造流程（如連接器的侵入式回焊與路由面板分離）而具備更整潔的邊緣。[](https://www.raspberrypi.com/products/raspberry-pi-5/)[](https://www.raspberrypi.com/news/introducing-raspberry-pi-5/)

---

### **作業系統與軟體**
推薦使用的作業系統為 **Raspberry Pi OS**（基於 Debian Bookworm），專為 Raspberry Pi 5 的硬體優化。提供以下版本：
- **完整版**：包含桌面環境與預裝軟體，適用於一般用途。
- **標準版**：具桌面環境，僅含基本軟體。
- **精簡版**：僅限命令列操作，適合無頭設定或輕量級應用。

其他支援的作業系統包括：
- **Ubuntu**：適用於桌面與伺服器用途的穩健 Linux 發行版。
- **Arch Linux ARM**：極簡且高度可自訂。
- **LibreELEC**：用於運行 Kodi 媒體中心的輕量級作業系統。
- **Batocera/Recalbox**：用於復古遊戲。
- **Windows 10/11**：實驗性支援桌面使用（非官方推薦）。[](https://www.jaycon.com/ultimate-guide-to-raspberry-pi/)[](https://wagnerstechtalk.com/rpi5/)

**Raspberry Pi Imager** 是官方工具，用於將作業系統燒錄至 microSD 卡或 SSD。它允許使用者選擇並設定作業系統，包括預先配置主機名稱、使用者帳戶與 SSH（用於無頭操作），從而簡化設定流程。[](https://wagnerstechtalk.com/rpi5/)[](https://www.scribd.com/document/693937166/Bash-A-Getting-started-with-Raspberry-Pi-5-A-beginners-Guide-2023)

---

### **設定流程**
設定 Raspberry Pi 5 過程直接明瞭，但需進行特定的硬體與軟體準備。以下為逐步指南：

1. **準備硬體**：
   - Raspberry Pi 5（2GB、4GB、8GB 或 16GB 型號）。
   - MicroSD 卡（建議 32GB 以上，Class 10 以確保效能）。
   - 5V/5A USB-C 電源供應器。
   - Micro HDMI 轉 HDMI 線材用於顯示輸出。
   - USB 鍵盤與滑鼠（或藍牙替代品）。
   - 可選：顯示器、乙太網路線、M.2 SSD 與 HAT、具散熱功能的外殼。[](https://robocraze.com/blogs/post/how-to-setup-your-raspberry-pi-5)

2. **準備 MicroSD 卡**：
   - 從樹莓派官方網站下載 Raspberry Pi Imager。
   - 使用 SDFormatter 等工具格式化 microSD 卡。
   - 使用 Imager 選擇並將 Raspberry Pi OS (Bookworm) 寫入卡片。[](https://www.waveshare.com/wiki/Raspberry_Pi_5)

3. **連接周邊裝置**：
   - 將 microSD 卡插入 Raspberry Pi 5。
   - 將顯示器連接至 HDMI0 端口（若使用雙顯示器，請使用兩個 micro HDMI 端口）。
   - 連接鍵盤、滑鼠與乙太網路（若未使用 Wi-Fi）。
   - 插入 USB-C 電源供應器。[](https://www.raspberrypi.com/documentation/computers/getting-started.html)

4. **啟動與設定**：
   - 開啟 Raspberry Pi 5 電源。紅色電源 LED 應保持亮起，綠色 ACT LED 將在啟動過程中閃爍。
   - 依照螢幕提示設定 Raspberry Pi OS，包括時區、Wi-Fi 與使用者憑證。
   - 對於無頭設定，可透過 Imager 啟用 SSH 或經由 UART 連接進行除錯。[](https://www.waveshare.com/wiki/Raspberry_Pi_5)

5. **可選配件**：
   - 使用 M.2 HAT+ 安裝 M.2 SSD 以獲得更快儲存速度。
   - 在 RTC 連接器上添加電池，以便在斷電時保持時間記錄。
   - 針對密集型任務，使用具主動散熱功能的外殼。[](https://www.theengineeringprojects.com/2023/10/introduction-to-raspberry-pi-5.html)[](https://www.raspberrypi.com/products/raspberry-pi-5/)

---

### **主要功能與改進**
Raspberry Pi 5 相較 Raspberry Pi 4 引入了多項進展：
- **效能**：Cortex-A76 CPU 與 VideoCore VII GPU 提供 2–3 倍更快的處理與圖形效能，適用於 PS2 模擬、桌面運算與 AI 工作負載等任務。在適當散熱下，CPU 可超頻至 3GHz。[](https://wagnerstechtalk.com/rpi5/)[](https://www.tomshardware.com/reviews/raspberry-pi-5)
- **PCIe 支援**：新增 PCIe 介面允許連接 NVMe SSD 及其他高速周邊裝置，顯著提升啟動與資料傳輸速度。[](https://www.raspberrypi.com/news/introducing-raspberry-pi-5/)
- **RP1 I/O 控制器**：此客製化晶片增強了 USB 3.0 頻寬、相機/顯示器連接性及整體 I/O 效能。[](https://www.raspberrypi.com/products/raspberry-pi-5/)
- **雙 4K 顯示器支援**：兩個 micro HDMI 端口實現同步 4K@60Hz 輸出，適合多媒體與生產力設定。[](https://www.linkedin.com/pulse/introduction-raspberry-pi-5-specs-harshvardhan-mishra-wkbmf)
- **內建 RTC**：整合式即時時鐘配備電池備份，確保在無網路連接下仍能準確計時。[](https://en.wikipedia.org/wiki/Raspberry_Pi)
- **電源按鈕**：專用開關按鈕簡化電源管理。[](https://www.tomshardware.com/reviews/raspberry-pi-5)
- **改進的散熱設計**：40nm 製程與可選的主動式散熱器提升了熱效率，但對於持續高效能運作仍建議使用主動散熱。[](https://robocraze.com/blogs/post/how-to-setup-your-raspberry-pi-5)

---

### **應用領域**
Raspberry Pi 5 的增強功能使其適用於多種專案：
- **教育**：利用 40 針 GPIO 接頭學習程式設計（Python、C++、Java）與電子學，連接感測器、LED 及機器人裝置。[](https://www.rs-online.com/designspark/introduction-to-raspberry-pi-5-specifications-and-features)
- **家庭自動化**：使用 IoT 框架控制智慧家庭裝置，如燈光、門鎖與攝影機。[](https://www.rs-online.com/designspark/introduction-to-raspberry-pi-5-specifications-and-features)
- **媒體中心**：透過 LibreELEC 運行 Kodi，在雙 4K 顯示器上進行串流與媒體播放。[](https://www.jaycon.com/ultimate-guide-to-raspberry-pi/)
- **復古遊戲**：使用 Batocera 或 Recalbox 模擬最高至 PS2 的遊戲主機。[](https://wagnerstechtalk.com/rpi5/)
- **伺服器**：託管輕量級網頁伺服器、VPN 或家庭自動化中樞（例如 HomeBridge）。[](https://arstechnica.com/gadgets/2024/01/what-i-learned-from-using-a-raspberry-pi-5-as-my-main-computer-for-two-weeks/)
- **工業與嵌入式系統**：基於 Raspberry Pi 5 的 Compute Module 5 非常適合客製化嵌入式應用。
- **AI 與機器學習**：利用改進的 CPU/GPU 進行邊緣 AI 專案，例如影像處理或語音識別，並搭配相容的 AI HAT。[](https://www.jaycon.com/ultimate-guide-to-raspberry-pi/)[](https://www.raspberrypi.com/documentation/)
- **桌面運算**：作為低成本、高能效的桌面電腦，用於瀏覽網頁、文書處理與輕量生產力任務。[](https://arstechnica.com/gadgets/2024/01/what-i-learned-from-using-a-raspberry-pi-5-as-my-main-computer-for-two-weeks/)

---

### **相容性與挑戰**
儘管 Raspberry Pi 5 提供顯著升級，但仍存在一些相容性問題：
- **外殼**：由於佈局變更，Raspberry Pi 5 無法放入 Raspberry Pi 4 的外殼。請使用官方 Raspberry Pi 5 外殼或相容的第三方選項。[](https://www.raspberrypi.com/products/raspberry-pi-5/)
- **HAT 與附加模組**：部分舊款 HAT 可能缺乏對 Raspberry Pi 5 的軟體支援，需等待社群更新。GPIO 程式設計亦可能需要調整。[](https://www.dfrobot.com/blog-13550.html)
- **電源供應**：需使用 5V/5A USB-C 電源供應器以避免不穩定，不同於 Raspberry Pi 4 使用的 5V/3A。[](https://www.waveshare.com/wiki/Raspberry_Pi_5)
- **作業系統**：僅最新版 Raspberry Pi OS (Bookworm) 完全優化。舊版作業系統可能不支援 PCIe 等新功能。[](https://www.waveshare.com/wiki/Raspberry_Pi_5)

樹莓派社群正積極應對這些挑戰，分享解決方案與韌體更新以提升相容性。[](https://www.dfrobot.com/blog-13550.html)

---

### **配件與生態系統**
Raspberry Pi 5 擁有豐富的配件生態系統支援：
- **官方配件**：
  - Raspberry Pi 5 外殼（10 美元），含整合式風扇。
  - 主動式散熱器（5 美元），適用於高負載工作。
  - 27W USB-C 電源供應器（12 美元）。
  - 用於 NVMe SSD 的 M.2 HAT+（10–20 美元）。
  - 樹莓派品牌 NVMe SSD（256GB 或 512GB）。[](https://www.theengineeringprojects.com/2023/10/introduction-to-raspberry-pi-5.html)[](https://www.raspberrypi.com/products/raspberry-pi-5/)
- **第三方配件**：如 CanaKit、Pimoroni 與 Pineboards 等公司提供專為 Raspberry Pi 5 設計的套件、HAT 與儲存解決方案。[](https://wagnerstechtalk.com/rpi5/)[](https://www.tomshardware.com/reviews/raspberry-pi-5)
- **文件與資源**：
  - 官方《Raspberry Pi Beginner’s Guide (第五版)》由 Gareth Halfacree 撰寫，涵蓋設定、程式設計與專案內容。可透過 Raspberry Pi Bookshelf 應用程式免費取得 PDF 版本。[](https://www.raspberrypi.com/news/available-now-the-official-raspberry-pi-beginners-guide-5th-edition/)
  - 社群資源如 Wagner’s TechTalk 與 Raspberry Pi subreddit 提供教學與專案點子。[](https://wagnerstechtalk.com/rpi5/)[](https://www.reddit.com/r/RASPBERRY_PI_PROJECTS/comments/16upxc0/total_beginner_with_raspberry_pi_where_do_i_start/)

---

### **效能與使用案例**
Raspberry Pi 5 的效能使其成為低功耗 ARM 架構迷你電腦的可行替代方案。在測試中，它已成功用作一般桌面電腦，進行網頁瀏覽、文件編輯與輕量多工處理，儘管在處理重度瀏覽器工作負載（例如多個 Chrome 分頁）時可能較為吃力。其運行 PS2 模擬與處理雙 4K 顯示器的能力，使其成為復古遊戲與媒體中心的熱門選擇。超頻至 3GHz 與 GPU 至 1.1GHz 可進一步提升效能，但主動散熱至關重要。[](https://arstechnica.com/gadgets/2024/01/what-i-learned-from-using-a-raspberry-pi-5-as-my-main-computer-for-two-weeks/)[](https://www.tomshardware.com/reviews/raspberry-pi-5)

對於專業應用，16GB 型號支援更需求高的任務，如軟體開發與伺服器託管。Compute Module 5 與 Raspberry Pi 500（鍵盤整合版本）則針對嵌入式系統與一體式運算需求而設計。[](https://www.jaycon.com/ultimate-guide-to-raspberry-pi/)[](https://en.wikipedia.org/wiki/Raspberry_Pi)

---

### **社群與支援**
樹莓派社群是其關鍵優勢所在，論壇、subreddit 及 raspberrypi.org 等網站提供廣泛支援。樹莓派基金會定期發布韌體更新，例如啟用雙 NVMe 驅動器支援與改進超頻功能。《MagPi》雜誌與官方文件則提供專案點子與技術細節。[](https://www.linkedin.com/pulse/introduction-raspberry-pi-5-specs-harshvardhan-mishra-wkbmf)[](https://www.raspberrypi.com/documentation/)

---

### **結論**
Raspberry Pi 5 是一款功能強大、多用途且價格相宜的單板電腦，它承襲了前代產品的優良傳統，同時引入了如 PCIe 支援、客製化 RP1 晶片與內建 RTC 等尖端功能。憑藉最高 16GB 的記憶體選項、雙 4K 顯示器支援及 2–3 倍的效能提升，它非常適合教育、愛好者專案、家庭自動化、復古遊戲與工業應用。儘管存在相容性挑戰，但活躍的社群與定期更新確保了流暢的使用體驗。無論您是初學 Python 的新手，還是建構 IoT 系統的工程師，Raspberry Pi 5 皆以親民的價格點提供了無限可能，實現了運算的民主化。[](https://www.zimaspace.com/blog/raspberry-pi-5-everything-you-need-to-know.html)[](https://www.rs-online.com/designspark/introduction-to-raspberry-pi-5-specifications-and-features)

欲了解更多詳情，請造訪樹莓派官方網站 (raspberrypi.com) 或探索 Wagner’s TechTalk 與《The MagPi》雜誌等社群資源。[](https://wagnerstechtalk.com/rpi5/)[](https://www.linkedin.com/pulse/introduction-raspberry-pi-5-specs-harshvardhan-mishra-wkbmf)
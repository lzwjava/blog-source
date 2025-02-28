---
audio: false
lang: hant
layout: post
title: 延遲數據
translated: true
---

### 關鍵要點
- 根據影片標題和相關線上內容，影片似乎討論了程序員應該知道的標準延遲數字。
- 研究表明，這些數字包括操作的時間，如 L1 快取訪問（0.5 納秒）和網絡往返（最多 150 毫秒），具體數字會因硬件而異。
- 這些數字似乎是近似值，隨著技術進步（特別是 SSD 和網絡）而更新。

### 介紹
影片「程序員應該知道的延遲數字：系統設計速成課程 #1」可能涵蓋了計算機操作的基本延遲數字，這對系統設計至關重要。這些數字有助於程序員了解性能影響並優化系統。

### 延遲數字及其重要性
延遲是從啟動到完成操作之間的延遲，如訪問記憶體或通過網絡發送數據。影片可能列出了典型的延遲，例如：
- L1 快取參考 0.5 納秒（ns），是最快的記憶體訪問。
- 同一數據中心內的往返時間為 500 微秒（us）或 0.5 毫秒（ms），影響分佈式系統。

這些數字雖然是近似值，但指導系統設計中的決策，如選擇記憶體和磁碟存儲。

### 系統設計中的背景
了解這些延遲有助於優化代碼、做出權衡並提升用戶體驗。例如，知道磁碟搜索需要 10 毫秒可以影響數據庫設計，以最小化這類操作。

### 意外細節
一個有趣的方面是，這些數字，如 SSD 讀取時間，隨著技術的進步而改善，但核心 CPU 延遲，如 L1 快取訪問，保持穩定，顯示硬件演進的不均衡影響。

---

### 調查筆記：影片中延遲數字的詳細分析

這篇筆記提供了對影片「程序員應該知道的延遲數字：系統設計速成課程 #1」中可能討論的延遲數字的全面探討，基於可用的線上內容和相關資源。分析旨在為程序員和系統設計師綜合信息，提供總結和詳細見解，這些數字的重要性。

#### 背景和背景
影片可在 [YouTube](https://www.youtube.com/watch?v=FqR5vESuKe0) 上訪問，是系統設計系列的一部分，專注於程序員關鍵的延遲數字。延遲，定義為操作啟動和完成之間的時間延遲，對理解系統性能至關重要。根據影片標題和相關搜索，它似乎涵蓋了 Jeff Dean 等人推廣的標準延遲數字，這些數字在程序員社區中經常引用。

線上搜索揭示了幾個討論這些數字的資源，包括一個名為「每個程序員都應該知道的延遲數字」的 GitHub Gist ([GitHub Gist](https://gist.github.com/jboner/2841832)) 和 2023 年的一篇 Medium 文章 ([Medium 文章](https://medium.com/@bojanskr/latency-numbers-every-programmer-should-know-d85f8d3f8e6a))。這些來源，加上 2013 年的 High Scalability 文章 ([High Scalability](https://highscalability.com/more-numbers-every-awesome-programmer-must-know/))，為編譯影片可能的內容提供了基礎。

#### 延遲數字的編譯
根據收集到的信息，以下表格總結了影片中可能討論的標準延遲數字，並對每個操作進行了說明：

| 操作                                      | 延遲 (ns) | 延遲 (us) | 延遲 (ms) | 說明                                                          |
|-------------------------------------------|--------------|--------------|--------------|----------------------------------------------------------------------|
| L1 快取參考                            | 0.5          | -            | -            | 訪問 CPU 附近的 Level 1 快取，最快的記憶體。 |
| 分支誤預測                              | 5            | -            | -            | CPU 當條件分支預測錯誤時的懲罰。       |
| L2 快取參考                            | 7            | -            | -            | 訪問 Level 2 快取，比 L1 大但慢。           |
| 互斥鎖/解鎖                              | 25           | -            | -            | 多線程程序中獲取和釋放互斥鎖的時間。        |
| 主記憶體參考                          | 100          | -            | -            | 從主隨機存取記憶體 (RAM) 訪問數據。                  |
| 使用 Zippy 算法壓縮 1K 字節                   | 10,000       | 10           | -            | 使用 Zippy 算法壓縮 1 千字節的時間。                |
| 通過 1 Gbps 網絡發送 1 KB 字節            | 10,000       | 10           | -            | 通過 1 吉比特每秒網絡傳輸 1 千字節的時間。      |
| 從 SSD 隨機讀取 4 KB                    | 150,000      | 150          | -            | 從固態硬碟隨機讀取 4 千字節。                  |
| 從記憶體順序讀取 1 MB             | 250,000      | 250          | -            | 從主記憶體順序讀取 1 兆字節。                       |
| 同一數據中心內的往返              | 500,000      | 500          | 0.5          | 同一數據中心內的網絡往返時間。                   |
| 從 SSD 順序讀取 1 MB                | 1,000,000    | 1,000        | 1            | 從 SSD 順序讀取 1 兆字節。                            |
| HDD 搜索                                      | 10,000,000   | 10,000       | 10           | 硬碟驅動器尋找新位置的時間。                 |
| 從磁碟順序讀取 1 MB              | 20,000,000   | 20,000       | 20           | 從 HDD 順序讀取 1 兆字節。                            |
| 發送封包 CA-> 荷蘭-> CA                | 150,000,000  | 150,000      | 150          | 從加利福尼亞到荷蘭的網絡封包往返時間。  |

這些數字主要來自 2012 年，並且在最近的討論中進行了更新，特別是 SSD 和網絡，因為技術進步。

#### 分析和影響
這些延遲數字並非固定，可能會因具體硬件和配置而異。例如，2020 年 Ivan Pesin 的博客文章 ([Pesin Space](http://pesin.space/posts/2020-09-22-latencies/)) 指出，由於更好的 SSD（NVMe）和更快的網絡（10/100Gb），磁碟和網絡延遲已有所改善，但核心 CPU 延遲，如 L1 快取訪問，保持穩定。這種不均衡的演進強調了系統設計中的上下文重要性。

在實踐中，這些數字指導了幾個方面：
- **性能優化**：最小化高延遲操作，如磁碟搜索（10 毫秒），可以顯著提高應用程序速度。例如，將頻繁訪問的數據緩存到記憶體（250 微秒讀取 1 MB）而不是磁碟，可以減少等待時間。
- **權衡決策**：系統設計師經常面臨選擇，如使用內存緩存還是數據庫。知道主記憶體參考（100 納秒）比 L1 快取參考（0.5 納秒）快 200 倍，可以幫助做出這些決策。
- **用戶體驗**：在網絡應用中，網絡延遲，如數據中心往返（500 微秒），會影響頁面加載時間，從而影響用戶滿意度。2024 年的 Vercel 博客文章 ([Vercel 博客](https://vercel.com/blog/latency-numbers-every-web-developer-should-know)) 強調了這一點，指出網絡瀑布可以累積延遲。

#### 歷史背景和更新
這些原始數字由 Jeff Dean 提出並由 Peter Norvig 普及，可追溯到約 2010 年，研究人員如 Colin Scott ([Interactive Latencies](https://colin-scott.github.io/personal_website/research/interactive_latency.html)) 進行了更新。2019 年 Dan Hon 的 Medium 文章 ([Dan Hon Medium](https://medium.com/@hondanhon/more-latency-numbers-every-programmer-should-know-3142f0cf614d)) 添加了幽默但相關的延遲，如重新啟動 MacBook Pro（90 秒），說明了更廣泛的技術相關延遲。然而，核心延遲數字變化不大，GitHub Gist 表示它們在 2023 年仍然「非常相似」，基於物理限制。

#### 結論和建議
對程序員和系統設計師來說，記住這些延遲數字提供了一個性能調整的心理模型。應將其視為指南，並對具體硬件進行實際基準測試。隨著新興技術（如量子計算或 5G 網絡）的發展，保持更新將至關重要。資源如 GitHub Gist 和 Medium 文章提供了進一步探索的起點。

這項分析基於影片可能的內容，並補充了廣泛的線上研究，強調了延遲數字在計算中的持久相關性，並呼籲適應技術變化以實現最佳系統設計。

#### 關鍵引用
- [每個程序員都應該知道的延遲數字 GitHub Gist](https://gist.github.com/jboner/2841832)
- [程序員應該知道的延遲數字 YouTube 影片](https://www.youtube.com/watch?v=FqR5vESuKe0)
- [更新的延遲數字 Medium 文章](https://medium.com/@bojanskr/latency-numbers-every-programmer-should-know-d85f8d3f8e6a)
- [每個優秀程序員都應該知道的更多數字 High Scalability](https://highscalability.com/more-numbers-every-awesome-programmer-must-know/)
- [每個網絡開發者都應該知道的延遲數字 Vercel 博客](https://vercel.com/blog/latency-numbers-every-web-developer-should-know)
- [每個工程師都應該知道的延遲數字 Pesin Space 博客](http://pesin.space/posts/2020-09-22-latencies/)
- [每個程序員都應該知道的更多延遲數字 Dan Hon Medium](https://medium.com/@hondanhon/more-latency-numbers-every-programmer-should-know-3142f0cf614d)
- [每年每個程序員都應該知道的數字 Interactive Latencies](https://colin-scott.github.io/personal_website/research/interactive_latency.html)
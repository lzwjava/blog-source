---
audio: false
generated: true
lang: hant
layout: post
title: 延遲數字
translated: true
type: note
---

### 重點摘要
- 根據影片標題及相關網路內容推測，該影片很可能探討程式設計師應了解的標準延遲數字。
- 研究顯示這些數字包含 L1 快取存取（0.5 奈秒）與網路往返（最高 150 毫秒）等操作時間，實際數值會因硬體設備而異。
- 現有證據傾向認為這些數字屬近似值，且會隨著技術進步（特別是 SSD 與網路技術）持續更新。

### 前言
《程式設計師應該知道的延遲數字：系統設計速成課程 #1》這部影片很可能涵蓋電腦運算中的關鍵延遲數據，這些對系統設計至關重要。這些數字能幫助程式設計師理解效能影響並優化系統。

### 延遲數字及其重要性
延遲指的是從發起操作到完成操作之間的時間延遲，例如存取記憶體或透過網路傳送資料。影片中可能列出的典型延遲數據包括：
- L1 快取存取：0.5 奈秒（ns），是最快的記憶體存取速度
- 同資料中心內往返：500 微秒（us）或 0.5 毫秒（ms），這會影響分散式系統效能

這些數字雖然是近似值，但能為系統設計提供決策依據，例如在記憶體與磁碟儲存之間做選擇。

### 在系統設計中的脈絡
理解這些延遲數據有助於優化程式碼、進行取捨決策並提升使用者體驗。舉例來說，了解磁碟尋道需要 10 毫秒，就能影響資料庫設計以盡量減少這類操作。

### 特別值得注意的細節
有個有趣的現象是，像 SSD 讀取時間這類數字會隨著技術進步而改善，但核心 CPU 延遲（如 L1 快取存取）卻保持穩定，這顯示了硬體演進的不均衡影響。

---

### 調查筆記：影片中延遲數字的詳細分析

本筆記基於可取得的網路內容與相關資源，對影片《程式設計師應該知道的延遲數字：系統設計速成課程 #1》中可能討論的延遲數字進行全面探討。此分析旨在為程式設計師和系統設計師整合資訊，提供這些數字的摘要與詳細見解。

#### 背景與脈絡
這部可於 [YouTube](https://www.youtube.com/watch?v=FqR5vESuKe0) 觀看的影片是系統設計系列的一部分，聚焦於程式設計師必須掌握的關鍵延遲數字。延遲定義為操作發起與完成之間的時間延遲，對理解系統效能至關重要。根據影片標題與相關搜尋結果，其內容很可能涵蓋由 Google 的 Jeff Dean 等人推廣的標準延遲數據，這些數字常在程式設計社群中被引用。

網路搜尋發現了多個討論這些數字的資源，包括 GitHub Gist 的《每個程式設計師都應該知道的延遲數字》([GitHub Gist](https://gist.github.com/jboner/2841832)) 與 2023 年的 Medium 文章 ([Medium Article](https://medium.com/@bojanskr/latency-numbers-every-programmer-should-know-d85f8d3f8e6a))。這些資源連同 2013 年的 High Scalability 文章 ([High Scalability](https://highscalability.com/more-numbers-every-awesome-programmer-must-know/))，為彙整影片可能內容提供了基礎。

#### 延遲數字彙整
根據收集到的資訊，下表總結了影片中可能討論的標準延遲數字，並附上各操作的解釋：

| 操作項目                                       | 延遲 (ns)    | 延遲 (us) | 延遲 (ms) | 說明                                                              |
|------------------------------------------------|--------------|-----------|-----------|-------------------------------------------------------------------|
| L1 快取存取                           | 0.5          | -         | -         | 存取 L1 快取中的資料，這是 CPU 附近最快的記憶體。                   |
| 分支預測失敗                             | 5            | -         | -         | CPU 錯誤預測條件分支時產生的效能損失。                             |
| L2 快取存取                           | 7            | -         | -         | 存取 L2 快取中的資料，容量比 L1 大但速度較慢。                     |
| 互斥鎖定/解鎖                              | 25           | -         | -         | 在多執行緒程式中取得和釋放互斥鎖的時間。                           |
| 主記憶體存取                          | 100          | -         | -         | 從主記憶體（RAM）存取資料。                                        |
| 使用 Zippy 壓縮 1KB 資料                  | 10,000       | 10        | -         | 使用 Zippy 演算法壓縮 1KB 資料所需的時間。                         |
| 透過 1 Gbps 網路傳送 1KB 資料            | 10,000       | 10        | -         | 透過 1 Gbps 網路傳輸 1KB 資料所需的時間。                          |
| 從 SSD 隨機讀取 4KB                      | 150,000      | 150       | -         | 從固態硬碟隨機讀取 4KB 資料的時間。                                |
| 從記憶體循序讀取 1MB            | 250,000      | 250       | -         | 從主記憶體循序讀取 1MB 資料的時間。                                |
| 同資料中心內往返              | 500,000      | 500       | 0.5       | 同一資料中心內的網路往返時間。                                     |
| 從 SSD 循序讀取 1MB                | 1,000,000    | 1,000     | 1         | 從 SSD 循序讀取 1MB 資料的時間。                                   |
| HDD 尋道時間                             | 10,000,000   | 10,000    | 10        | 硬碟驅動器尋道至新位置所需的時間。                                 |
| 從硬碟循序讀取 1MB              | 20,000,000   | 20,000    | 20        | 從 HDD 循序讀取 1MB 資料的時間。                                   |
| 資料包從加州→荷蘭→加州往返                | 150,000,000  | 150,000   | 150       | 網路資料包從加州到荷蘭再返回的往返時間。                           |

這些數字主要源自 2012 年並有部分更新，反映了典型硬體效能，但近期討論特別指出 SSD 和網路技術因科技進步而有所變化。

#### 分析與影響
延遲數字並非固定不變，會因具體硬體和配置而異。例如 Ivan Pesin 2020 年的部落格文章 ([Pesin Space](http://pesin.space/posts/2020-09-22-latencies/)) 指出，磁碟和網路延遲因更優異的 SSD（NVMe）和更快網路（10/100Gb）而改善，但核心 CPU 延遲（如 L1 快取存取）保持穩定。這種不均衡的演進凸顯了在系統設計中考量具體情境的重要性。

在實務中，這些數字引導多個面向：
- **效能優化**：盡量減少高延遲操作（如磁碟尋道 10 ms）能顯著提升應用程式速度。例如將頻繁存取的資料快取在記憶體中（讀取 1MB 需 250 us），而非磁碟，可減少等待時間。
- **取捨決策**：系統設計師常需做出選擇，例如使用記憶體快取還是資料庫。了解主記憶體存取（100 ns）比 L1 快取存取（0.5 ns）快 200 倍，能為這類決策提供依據。
- **使用者體驗**：在網路應用中，像資料中心往返（500 us）這樣的網路延遲會影響頁面載入時間，進而影響使用者滿意度。Vercel 2024 年的部落格文章 ([Vercel Blog](https://vercel.com/blog/latency-numbers-every-web-developer-should-know)) 特別針對前端開發強調了這一點，指出網路瀑布流如何疊加延遲效應。

#### 歷史脈絡與更新
原始數字可追溯至約 2010 年，歸功於 Jeff Dean 並經 Peter Norvig 推廣，後由 Colin Scott 等研究人員更新 ([Interactive Latencies](https://colin-scott.github.io/personal_website/research/interactive_latency.html))。Dan Hon 2019 年的 Medium 文章 ([Dan Hon Medium](https://medium.com/@hondanhon/more-latency-numbers-every-programmer-should-know-3142f0cf614d)) 加入了幽默且相關的延遲數據，如重啟 MacBook Pro（90 秒），說明了更廣泛的技術相關延遲。然而核心延遲數字變化極小，GitHub Gist 指出截至 2023 年這些數字仍「相當類似」，這主要是受物理限制影響。

#### 結論與建議
對程式設計師和系統設計師而言，記住這些延遲數字能為效能調校提供心智模型。這些數字應視為指導原則，實際應用中需針對特定硬體進行基準測試。持續關注新興技術（如量子運算或 5G 網路）的更新至關重要。GitHub Gist 和 Medium 文章等資源可作為進一步探索的起點。

本分析以影片可能內容為基礎，並輔以廣泛的網路研究，強調了延遲數字在計算領域的持久重要性，同時呼籲應適應技術變遷以實現最佳系統設計。

#### 主要參考文獻
- [每個程式設計師都應該知道的延遲數字 GitHub Gist](https://gist.github.com/jboner/2841832)
- [程式設計師應該知道的延遲數字 YouTube 影片](https://www.youtube.com/watch?v=FqR5vESuKe0)
- [更新的延遲數字 Medium 文章](https://medium.com/@bojanskr/latency-numbers-every-programmer-should-know-d85f8d3f8e6a)
- [每個優秀程式設計師必須知道的更多數字 High Scalability](https://highscalability.com/more-numbers-every-awesome-programmer-must-know/)
- [每個網頁開發者應該知道的延遲數字 Vercel 部落格](https://vercel.com/blog/latency-numbers-every-web-developer-should-know)
- [每個工程師應該知道的延遲數字 Pesin Space 部落格](http://pesin.space/posts/2020-09-22-latencies/)
- [每個程式設計師應該知道的更多延遲數字 Dan Hon Medium](https://medium.com/@hondanhon/more-latency-numbers-every-programmer-should-know-3142f0cf614d)
- [按年份列出的每個程式設計師應該知道的數字 Interactive Latencies](https://colin-scott.github.io/personal_website/research/interactive_latency.html)
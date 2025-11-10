---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 後起之秀的迅速崛起
translated: true
type: note
---

幾種相對較晚出現（2000年後）的程式語言，在技術進步、AI整合及強大社群支援的推動下，近年來展現出快速的普及態勢，這與Rust的發展軌跡頗為相似。以下我將重點介紹幾種符合這種「起步晚但追趕快」模式的關鍵語言，聚焦於它們的成長軌跡、應用場景及促成其崛起的因素。我會在適當處將其普及表現與Java、C和C++等老牌語言進行比較，並基於現有數據和趨勢進行分析，避免推測性論斷。

### 起步雖晚但普及迅速的語言

1. **Go (Golang)**
   - **起始與背景**：由Google於2009年發布，Go專為大規模系統的簡潔性、效能和可擴展性而設計，旨在解決C++和Java等語言中諸如語法複雜和編譯速度慢等問題。
   - **普及表現**：Go的受歡迎程度穩步攀升。截至2025年中，它在TIOBE指數中排名約第8至10位（相較於2022年的第13位有所上升），評分約為2-3%，並且在PYPL排行榜上位列前十。估計有200至300萬開發者使用Go，而Java的開發者數量為1200至1500萬，C++則為600至800萬。Stack Overflow的2024年調查顯示，13%的開發者使用Go，其在雲端和DevOps領域的增長強勁。
   - **為何能快速追趕**：
     - **技術進步**：Go的並行模型（goroutines）和快速編譯使其成為雲端原生應用、微服務和容器（例如Docker和Kubernetes均使用Go編寫）的理想選擇。在雲端工作負載的資源效率方面，它優於Java。
     - **AI整合**：像GitHub Copilot這樣的AI工具提升了Go的開發速度，能夠生成地道的程式碼並減少樣板程式碼。由於其效能，Go在AI基礎設施（例如在Google內部）中的使用正在增長。
     - **開源社群**：Go的簡潔設計和活躍社群（pkg.go.dev上有超過30,000個套件）推動了其普及。Uber、Twitch和Dropbox等公司使用Go，提升了其可信度。
   - **成長證據**：2024年至2025年間，Go的採用率年增長約20%，尤其在雲端運算領域。對Go開發者的職位需求激增，並且在新的雲端專案中，其速度已超過Java。然而，與Java或C++相比，其較小的生態系統限制了其更廣泛的主導地位。
   - **參考資料**：[Top Computer Languages 2025](https://statisticstimes.com/tech/top-computer-languages.php), [Top 10 programming languages in 2025](https://www.pluralsight.com/resources/blog/software-engineering/top-programming-languages), [History of Programming Languages](https://devskiller.com/history-of-programming-languages/).

2. **TypeScript**
   - **起始與背景**：由微軟於2012年開發，TypeScript是JavaScript的超集，增加了靜態型別以提升大型網頁專案的可擴展性和可維護性。
   - **普及表現**：TypeScript在TIOBE（2025年，約3-4%）和PYPL中排名第5至7位，擁有約300萬開發者（相比之下，JavaScript有1500至2000萬開發者）。Stack Overflow的2024年調查指出，28%的開發者使用TypeScript，高於2020年的20%，使其成為網頁開發的首選之一。
   - **為何能快速追趕**：
     - **技術進步**：TypeScript的靜態型別減少了大型JavaScript專案中的錯誤，使其成為React、Angular和Vue.js等框架的關鍵。它廣泛應用於企業級網頁應用（例如Slack、Airbnb）。
     - **AI整合**：AI驅動的IDE（例如Visual Studio Code）提供即時型別檢查和自動完成功能，加速了TypeScript的普及。其與AI驅動開發工具的整合使其對初學者更加友好。
     - **開源社群**：TypeScript的社群非常強大，超過90%的頂級JavaScript框架都支援它。微軟的支持和npm生態系統（數百萬個套件）推動了其成長。
   - **成長證據**：2022年至2025年間，TypeScript在GitHub儲存庫中的使用量每年增長約30%，在新的前端專案中已超越JavaScript。它正在縮小與JavaScript的差距，但由於JavaScript具有普遍的瀏覽器支援，因此不太可能完全超越它。
   - **參考資料**：[Top Computer Languages 2025](https://statisticstimes.com/tech/top-computer-languages.php), [Comparing tag trends with our Most Loved programming languages](https://stackoverflow.blog/2025/07/31/comparing-tag-trends-with-our-most-loved-programming-languages/), [The rise and fall in programming languages' popularity](https://www.zdnet.com/article/the-rise-and-fall-in-programming-languages-popularity-since-2016/).

3. **Kotlin**
   - **起始與背景**：由JetBrains於2011年推出，1.0版於2016年發布，Kotlin是Java的現代替代品，專為簡潔語法和安全性而設計，尤其適用於Android開發。
   - **普及表現**：Kotlin在TIOBE（2025年，約1-2%）和PYPL中排名約第12至15位，擁有約200萬開發者。Google於2017年將其列為Android開發的一級語言，促進了其快速成長；到2024年，20%的Android應用使用Kotlin（高於2018年的5%）。
   - **為何能快速追趕**：
     - **技術進步**：Kotlin的空值安全性和簡潔語法減少了與Java相比的樣板程式碼，使其在行動和後端開發中更高效。它與Java完全互通，便於遷移。
     - **AI整合**：像IntelliJ IDEA這樣的IDE中的AI工具可以生成Kotlin程式碼，提高生產力。由於其效率，Kotlin在AI驅動的行動應用中的使用正在增長。
     - **開源社群**：在JetBrains和Google的支持下，Kotlin的生態系統（例如用於伺服器的Ktor、用於UI的Compose）正在擴展。其社群規模雖小於Java，但成長迅速，Maven上有數千個函式庫。
   - **成長證據**：Kotlin在Android開發中的採用率每年增長約25%，並且在後端（例如Spring Boot）中也日益普及。由於Java在企業級領域的主導地位，Kotlin不太可能在全球範圍內超越Java，但在行動和伺服器端利基市場中正在快速追趕。
   - **參考資料**：[Top Computer Languages 2025](https://statisticstimes.com/tech/top-computer-languages.php), [Top 10 programming languages in 2025](https://www.pluralsight.com/resources/blog/software-engineering/top-programming-languages), [History of Programming Languages](https://devskiller.com/history-of-programming-languages/).

4. **Swift**
   - **起始與背景**：由蘋果公司於2014年發布，Swift是一種現代、安全且快速的語言，適用於iOS、macOS和伺服器端開發，旨在取代Objective-C。
   - **普及表現**：Swift在TIOBE（2025年，約1%）和PYPL中排名約第15至16位，擁有約150至200萬開發者。Stack Overflow的2024年調查報告顯示，8%的開發者使用Swift，高於2020年的5%。它在iOS開發中佔主導地位，約70%的新iOS應用使用Swift。
   - **為何能快速追趕**：
     - **技術進步**：Swift在原生應用中的效能可與C++媲美，其安全功能（例如可選型別）相較於Objective-C減少了崩潰情況。它正擴展到伺服器端（例如Vapor框架）和跨平台開發。
     - **AI整合**：Xcode的AI輔助編碼工具（例如程式碼補全、除錯）使Swift更易上手。其在AI驅動的iOS應用（例如AR/ML）中的使用正在增長。
     - **開源社群**：Swift於2015年開源，擁有不斷成長的社群，Swift Package Manager上有數千個套件。蘋果生態系統的鎖定效應確保了其普及，但伺服器端的成長增加了其多功能性。
   - **成長證據**：Swift的採用率每年增長約20%，已超越Objective-C（後者目前在TIOBE中排名第33位）。它並未在廣泛領域挑戰C/C++或Java，但在其利基市場中佔主導地位，並正擴展到蘋果生態系統之外。
   - **參考資料**：[Top Computer Languages 2025](https://statisticstimes.com/tech/top-computer-languages.php), [10 dying or 'dead' programming languages](https://www.techtarget.com/searchsoftwarequality/feature/10-dying-or-dead-programming-languages), [Top 10 programming languages in 2025](https://www.pluralsight.com/resources/blog/software-engineering/top-programming-languages).

5. **Julia**
   - **起始與背景**：於2012年推出，Julia專為高效能數值和科學計算而設計，在數據科學和AI領域與Python和R競爭。
   - **普及表現**：Julia在TIOBE中排名約第20至25位（2025年，約0.5-1%），但在科學社群中快速攀升。擁有約100萬開發者，遠落後於Python的1000至1200萬開發者。Stack Overflow的2024年調查指出，其使用率為2%，高於2020年的不到1%。
   - **為何能快速追趕**：
     - **技術進步**：Julia的速度（接近C語言水平）和動態型別使其成為機器學習、模擬和大數據的理想選擇。像Flux.jl這樣的函式庫可與Python的PyTorch媲美。
     - **AI整合**：AI工具可以生成用於科學任務的Julia程式碼，其在AI/ML工作負載（例如微分方程）中的效能吸引了研究人員。
     - **開源社群**：Julia的社群規模較小但非常活躍，JuliaHub上有超過7,000個套件。學術界和科技公司（例如Julia Computing）的支持推動了其成長。
   - **成長證據**：Julia在數據科學領域的採用率每年增長約30%，尤其在學術界和AI研究中。它並未超越Python，但在效能至關重要的領域開拓了自己的利基市場。
   - **參考資料**：[Comparing tag trends with our Most Loved programming languages](https://stackoverflow.blog/2025/07/31/comparing-tag-trends-with-our-most-loved-programming-languages/), [Top Computer Languages 2025](https://statisticstimes.com/tech/top-computer-languages.php).

### 與Rust普及情況的比較
- **Rust的基準**：Rust約25%的年增長率、約230萬開發者以及TIOBE第13至15位的排名設定了標準。由於其安全性和效能，它在系統程式設計、雲端和AI領域表現出色。
- **Go和TypeScript**：這些語言的增長率（約20-30%）與Rust相當或更高，排名也更靠前（分別為第8至10位和第5至7位）。Go在雲端領域的主導地位和TypeScript在網頁領域的主導地位，使它們比Rust的系統專注領域擁有更廣泛的影響力。
- **Kotlin和Swift**：這些語言具有相似的增長率（約20-25%），但更為利基（分別專注於Android和iOS）。它們在各自領域中正在追趕Java/Objective-C，但普遍吸引力不如Rust。
- **Julia**：其增長率（約30%）強勁，但僅限於科學計算，用戶基礎較小。與Rust相比，它在廣泛領域中與C/C++/Java競爭的可能性較低。

### 這些語言成功的原因
- **技術契合度**：每種語言在特定情境下都比老牌語言更好地滿足了現代需求（Go適合雲端、TypeScript適合網頁、Kotlin/Swift適合行動裝置、Julia適合科學計算）。
- **AI加速**：AI工具降低了入門門檻，能夠生成程式碼和教程，尤其對於遺留負擔較少的新語言而言更是如此。
- **社群與產業**：強大的支持（例如Google支持Go/Kotlin、微軟支持TypeScript、蘋果支持Swift）和開源生態系統推動了普及，這與Rust的模式相似。

### 限制
- **生態系統規模**：沒有一種語言能與Java（Maven）、C++（Boost）或C（POSIX）成熟的函式庫相媲美。這減緩了廣泛普及的速度。
- **學習曲線**：TypeScript和Kotlin比Rust更容易上手，但Go、Swift和Julia對初學者來說可能具有挑戰性。
- **遺留系統主導地位**：C/C++/Java在企業、作業系統和遺留系統中的根深蒂固意味著這些新語言是在新專案中追趕，而非取代舊有專案。

### 結論
Go、TypeScript、Kotlin、Swift和Julia是2000年後起步且普及迅速的傑出語言，它們的發展軌跡與Rust相似。Go和TypeScript在廣泛影響力方面最接近Rust，而Kotlin和Swift在特定生態系統中佔主導地位，Julia則在利基市場中表現卓越。它們的成長受到現代技術需求、AI工具和開源動力的推動，但由於遺留系統的根深蒂固，沒有一種語言能在未來5到10年內完全「追趕上」Java/C/C++。儘管如此，它們正在顯著重塑各自的領域。

**參考資料**  
[Top Computer Languages 2025](https://statisticstimes.com/tech/top-computer-languages.php)  
[Top 10 programming languages in 2025](https://www.pluralsight.com/resources/blog/software-engineering/top-programming-languages)  
[Comparing tag trends with our Most Loved programming languages](https://stackoverflow.blog/2025/07/31/comparing-tag-trends-with-our-most-loved-programming-languages/)  
[History of Programming Languages](https://devskiller.com/history-of-programming-languages/)  
[10 dying or 'dead' programming languages](https://www.techtarget.com/searchsoftwarequality/feature/10-dying-or-dead-programming-languages)  
[The rise and fall in programming languages' popularity](https://www.zdnet.com/article/the-rise-and-fall-in-programming-languages-popularity-since-2016/)
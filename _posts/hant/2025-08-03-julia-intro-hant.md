---
audio: false
generated: true
image: false
lang: hant
layout: post
title: Julia：高效能計算語言
translated: true
type: note
---

Julia 是一種高階、高效能的動態程式語言，主要專為數值與科學計算、資料科學、機器學習及平行計算而設計。其目標在於彌合易用性（如 Python 或 MATLAB）與原始效能（如 C 或 Fortran）之間的差距，讓使用者能夠編寫既易讀又快速的程式碼，無需因應不同任務切換語言。Julia 是開源軟體，採用 MIT 許可證釋出，並擁有不斷成長的生態系統，包含數千個套件。由於其透過 LLVM 進行即時編譯，能生成高效的原生程式碼，因此在需要大量計算的領域特別受歡迎，例如物理模擬、最佳化與大數據分析。

## 歷史

Julia 的開發始於 2009 年，由麻省理工學院的 Jeff Bezanson、Stefan Karpinski、Viral B. Shah 和 Alan Edelman 發起，他們對現有技術計算語言中的取捨感到不滿。他們希望創造一種免費、開源、高階且速度可媲美編譯語言的程式語言。該專案於 2012 年 2 月 14 日透過一篇闡述其目標的部落格文章正式對外公布。

早期版本演變迅速，語法與語義在 2018 年 8 月釋出的 1.0 版本中趨於穩定，該版本承諾 1.x 系列將保持向後相容性。在版本 0.7（亦於 2018 年釋出，作為邁向 1.0 的橋樑）之前，語言規格經常變動。此後，Julia 持續穩定釋出新版，包括長期支援版本如 1.6（後由 1.10.5 取代）以及不斷的改進。

關鍵里程碑包括：
- Julia 1.7（2021 年 11 月）：更快的隨機數生成。
- Julia 1.8（2022 年）：改進編譯後程式的分發。
- Julia 1.9（2023 年 5 月）：增強套件預編譯功能。
- Julia 1.10（2023 年 12 月）：平行垃圾回收與新解析器。
- Julia 1.11（2024 年 10 月，2025 年 7 月釋出修補版本 1.11.6）：引入 `public` 關鍵字以提升 API 安全性。
- 截至 2025 年 8 月，Julia 1.12.0-rc1 處於預覽階段，並每日更新邁向 1.13.0-DEV。

Julia 社群已顯著成長，在 GitHub 上擁有超過 1,000 位貢獻者。2014 年，它成為 NumFOCUS 贊助的專案，並獲得戈登與貝蒂·摩爾基金會、美國國家科學基金會、DARPA 及 NASA 等機構的資助。2015 年，創始人們成立了 Julia Computing（現為 JuliaHub, Inc.）以提供商業支援，並在直至 2023 年的多輪融資中籌集超過 4,000 萬美元。年度 JuliaCon 大會始於 2014 年，並在 2020 及 2021 年轉為線上舉行，吸引數萬名參與者。創始團隊曾獲得多項獎項，包括 2019 年 James H. Wilkinson 數值軟體獎與 IEEE Sidney Fernbach 獎。

## 主要特性

Julia 的設計原則強調效能、靈活性與可用性，使其與眾不同：
- **多重分派**：核心範式，函數行為由所有引數的型別決定，實現高效且可擴展的多型程式碼。這以組合取代了傳統的物件導向繼承。
- **具型別推斷的動態型別系統**：Julia 為動態型別語言，但利用型別推斷提升效能，允許可選的型別標註。它採用指名、參數化且強型別的系統，萬物皆物件。
- **即時編譯**：程式碼在執行時編譯為原生機器碼，使 Julia 在許多任務的基準測試中速度可媲美 C。
- **互通性**：透過內建巨集（如 `@ccall`）與套件（例如 PyCall.jl、RCall.jl），無縫呼叫 C、Fortran、Python、R、Java、Rust 等語言。
- **內建套件管理器**：透過 `Pkg.jl` 輕鬆安裝与管理套件，支援可重現的環境。
- **平行與分散式計算**：原生支援多執行緒、GPU 加速（透過 CUDA.jl）與分散式處理。
- **Unicode 支援**：廣泛使用數學符號（例如 `∈` 表示「屬於」、`π` 表示圓周率），並在 REPL 中支援 LaTeX 風格的輸入。
- **超程式設計**：類似 Lisp 的巨集，用於程式碼生成與操作。
- **可重現性**：提供工具建立隔離環境，並將應用程式打包為可執行檔或網頁應用。

Julia 亦支援通用程式設計，包括網頁伺服器、微服務，甚至透過 WebAssembly 在瀏覽器中編譯。

## 為何 Julia 適合科學計算

Julia 從零開始為科學與數值計算打造，旨在解決「雙語言問題」——即原型通常以緩慢的高階語言編寫，隨後需用更快的語言重寫。其速度可與 Fortran 或 C 匹敵，同時保持類似 MATLAB 或 Python 的語法，使其成為模擬、最佳化與資料分析的理想選擇。

關鍵優勢：
- **效能**：基準測試顯示，Julia 在數值任務上表現優於 Python 與 R，通常領先數個數量級，這歸功於 JIT 與型別特化。
- **生態系統**：擁有超過 10,000 個套件，包括：
  - DifferentialEquations.jl：用於求解常微分方程/偏微分方程。
  - JuMP.jl：用於數學最佳化。
  - Flux.jl 或 Zygote.jl：用於機器學習與自動微分。
  - Plots.jl：用於視覺化。
  - 領域特定工具，如生物學（BioJulia）、天文學（AstroPy 對應套件）與物理學。
- **平行處理**：能處理大規模計算，例如 Celeste.jl 專案在超級電腦上實現了 1.5 PetaFLOP/s 的天文影像分析效能。
- **互動性**：REPL 支援互動式探索、除錯與效能分析，並提供 Debugger.jl 與 Revise.jl 等工具以實現即時代碼更新。

知名應用包括 NASA 的模擬、藥物建模、聯準會的經濟預測與氣候模擬。它被學術界、產業界（如 BlackRock、Capital One）與研究實驗室廣泛使用。

## 語法與範例程式碼

Julia 的語法簡潔、基於表達式，且對 Python、MATLAB 或 R 的使用者來說十分熟悉。它採用 1-based 索引（類似 MATLAB），以 `end` 結束區塊而非依賴縮排，並原生支援向量化操作。

以下為一些基礎範例：

### Hello World
```julia
println("Hello, World!")
```

### 定義函數
```julia
function square(x)
    return x^2  # ^ 表示指數運算
end

println(square(5))  # 輸出：25
```

### 矩陣運算
```julia
A = [1 2; 3 4]  # 2x2 矩陣
B = [5 6; 7 8]
C = A * B  # 矩陣乘法

println(C)  # 輸出：[19 22; 43 50]
```

### 迴圈與條件判斷
```julia
for i in 1:5
    if i % 2 == 0
        println("$i is even")
    else
        println("$i is odd")
    end
end
```

### 繪圖（需安裝 Plots.jl 套件）
首先，在 REPL 中安裝套件：`using Pkg; Pkg.add("Plots")`
```julia
using Plots
x = range(0, stop=2π, length=100)
y = sin.(x)  # 向量化 sin
plot(x, y, label="sin(x)", xlabel="x", ylabel="y")
```

### 多重分派範例
```julia
greet(::Int) = "Hello, integer!"
greet(::String) = "Hello, string!"

println(greet(42))    # 輸出：Hello, integer!
println(greet("Hi"))  # 輸出：Hello, string!
```

這些範例可在 Julia REPL 中執行以進行互動測試。

## 安裝

Julia 支援 Windows、macOS、Linux 與 FreeBSD。請從官方網站下載二進位檔。例如：
- 執行安裝程式並將 Julia 加入 PATH。
- 在終端機中使用 `julia` 啟動 REPL 以管理套件。
詳細說明：支援平台包括 x86-64、ARM 等。

## 社群與資源

Julia 擁有一個充滿活力且包容的社群，擁有超過 1,000 位貢獻者。資源包括：
- Discourse 論壇、Zulip 聊天、Slack、Twitter（@JuliaLanguage）、YouTube 頻道、LinkedIn 與 Twitch 直播。
- 年度 JuliaCon 大會。
- 文件位於 docs.julialang.org。
- GitHub 儲存庫：github.com/JuliaLang/julia。
- JuliaHub 提供雲端計算與套件託管服務。

社群強調多元性並歡迎初學者。

## 近期發展（截至 2025 年 8 月）

近期版本聚焦於效能與可用性，例如 Julia 1.11 的公開 API 增強與 1.12 預覽版中改進的 Unicode 與解析器更新。2025 年 5 月的社群通訊突出了套件生態系統的成長與相關活動。透過 JuliaHub，資金與商業應用持續擴展。

[Julia 官方網站](https://julialang.org/)  
[Julia 維基百科頁面](https://en.wikipedia.org/wiki/Julia_(programming_language))
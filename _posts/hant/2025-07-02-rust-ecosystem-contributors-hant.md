---
audio: false
generated: true
lang: hant
layout: post
title: Rust 頂尖貢獻者與創始人
translated: true
type: note
---

Rust 生態圈充滿活力且持續成長，有許多個人與組織貢獻卓著。以下整理主要貢獻者、程式設計師、具影響力專案及創始人：

### Rust 創始人

Rust 程式語言的主要創始人為：

* **Graydon Hoare**：他於 2006 年在 Mozilla 工作期間將 Rust 作為個人專案啟動，旨在創造一種能解決 C 與 C++ 中常見記憶體安全問題的系統程式語言。他奠定了這門語言的基礎原則。

其他在 Mozilla 參與 Rust 早期開發與演進的關鍵人物包括：

* **Niko Matsakis**：長期貢獻 Rust 編譯器與語言設計，特別是在借用檢查器方面。
* **Patrick Walton**
* **Felix Klock**
* **Manish Goregaokar**

### 頂尖 Rust 生態圈貢獻者與程式設計師（廣受認可的開源工作）

由於貢獻形式多元且分散於眾多個人與團隊之間，很難給出確切的「前 30 名」。不過，以下列出一些因開源工作及對 Rust 社群影響力而備受推崇的程式設計師與關鍵貢獻者：

* **Steve Klabnik**：多產作家、教育家及核心團隊成員，以貢獻 Rust 文件（如《The Rust Programming Language》書籍）及推廣 Rust 聞名。他現任職於 Oxide Computer Company，將 Rust 應用於硬體/軟體系統。
* **Nicholas Matsakis (nikomatsakis)**：對 Rust 編譯器設計與實作貢獻卓著，特別是構成 Rust 記憶體安全核心的借用檢查器。他在 AWS 從事 Rust 相關工作。
* **Mara Bos**：Rust 程式庫團隊重要成員，活躍於社群並參與標準程式庫各面向與語言演進。她同時是 Fusion Engineering 共同創辦人。
* **Carol Nichols**：社群另一位關鍵人物，合著《The Rust Programming Language》並擔任 Rust Foundation 董事會成員，積極推動 Rust 的採用與永續發展。
* **Jon Gjengset (jonhoo)**：以深入剖析 Rust 內部機制（特別是並行處理）聞名，其優質教學內容與直播幫助許多人學習進階 Rust 概念。
* **Alex Crichton**：多個 Rust 專案的重要貢獻者，包括 `rust-lang/rust` 與 `crates.io-index`，在生態圈基礎建設扮演關鍵角色。
* **Ralf Jung**：以開發 Miri（Rust 的 UBM 未定義行為機器解譯器）聞名，該工具能協助偵測 Rust 程式碼中的未定義行為。
* **Bryan Cantrill**：Oxide Computer Company 技術長暨共同創辦人，大力倡導在系統程式設計與產業中採用 Rust。
* **Josh Triplett**：長期 Rust 貢獻者與核心團隊成員，參與語言開發的多個面向。
* **Armin Ronacher (mitsuhiko)**：Python Flask 框架創建者，成為推動 Rust 採用的重要推手，特別是在 Sentry 公司。
* **Andrew Gallant (BurntSushi)**：以開發高效能且廣泛使用的 Rust 套件聞名，例如 `ripgrep`（快速的 grep 替代工具）與 `regex`。
* **Syrus Akbary**：Wasmer 創建者，這是以 Rust 驅動的 WebAssembly 執行環境。
* **Frank McSherry**：以差分數據流研究聞名，其專案探索 Rust 中的進階並行處理與數據處理。
* **Jeremy Soller**：在 System76 與 Oxide Computer Company 的工作展現了 Rust 在作業系統層級的可行性。
* **Guillaume Gomez**：Rust 編譯器與 GTK-RS 專案（GTK 的 Rust 綁定）的多產貢獻者。
* **Pietro Albini**：對 Rust 關鍵基礎建設貢獻卓著，同時是 Rust 核心團隊成員。
* **Dirkjan Ochtman**：維護 `rustls` 與 `quinn`，這是在 Rust 中實現安全通訊的重要程式庫。
* **Gary Guo**：維護 Rust for Linux，這是將 Rust 整合至 Linux 核心的關鍵計畫。
* **Manish Goregaokar**：Google 資深軟體工程師，貢獻多個 Rust 專案包括 Unicode 相關工作。

### 頂尖開源 Rust 專案（具高度影響力）

許多開源專案展現了 Rust 的優勢並產生顯著影響：

1.  **Rust Lang/Rust（Rust 編譯器與標準程式庫）**：核心專案本身，讓所有人能建構可靠且高效的軟體。
2.  **Tauri Apps/Tauri**：用於建構更輕量、快速且安全的桌面與行動應用程式框架，採用網頁前端，類似 Electron 但效率更高。
3.  **RustDesk/RustDesk**：開源遠端桌面應用程式，是 TeamViewer 的熱門替代方案。
4.  **Alacritty/Alacritty**：跨平台 OpenGL 終端機模擬器，以高效能著稱。
5.  **Tokio/Tokio**：Rust 的基礎非同步執行環境，廣泛用於建構高效能網路應用程式。
6.  **Hyper/Hyper**：快速且正確的 Rust HTTP 程式庫，常與 Tokio 搭配使用。
7.  **Actix/Actix-web**：強大、快速且高度並行的 Rust 網頁框架。
8.  **Axum/Axum**：基於 Tokio 與 Hyper 建構的網頁應用框架，強調人體工學與強型別。
9.  **Ripgrep (BurntSushi/ripgrep)**：面向行的搜尋工具，可遞迴搜尋目錄中的正規表示式模式，速度顯著快於 `grep`。
10. **Bat (sharkdp/bat)**：具備進階功能的 `cat(1)` 替代工具，提供語法突顯、Git 整合等功能。
11. **Fd (sharkdp/fd)**：簡潔、快速且使用者友善的 `find` 替代方案。
12. **Meilisearch/Meilisearch**：強大、快速且相關性佳的搜尋引擎。
13. **Polars/Polars**：極速的 DataFrame 程式庫，常被視為 Rust 生態中數據操作的 Pandas 替代方案。
14. **BevyEngine/Bevy**：以 Rust 建構的清新簡潔數據驅動遊戲引擎。
15. **Helix Editor/Helix**：受 Neovim 與 Kakoune 啟發的現代模態文字編輯器，以 Rust 編寫。
16. **Nushell/Nushell（或 Nu）**：現代化 shell，旨在將程式語言概念引入命令列。
17. **Deno/Deno**：JavaScript 與 TypeScript 的安全執行環境，以 Rust 與 V8 建構。
18. **Firecracker MicroVM/Firecracker**：由 AWS 開發的輕量級虛擬化技術，用於無伺服器運算。
19. **Crates.io**：Rust 程式語言的官方套件登記庫，對生態圈至關重要。
20. **Rustlings (rust-lang/rustlings)**：透過小型練習幫助使用者熟悉閱讀與編寫 Rust 程式碼，對初學者極具價值。
21. **Yewstack/Yew**：使用 WebAssembly 建構用戶端網頁應用程式的現代 Rust 框架。
22. **DioxusLabs/Dioxus**：另一款熱門的宣告式 Rust UI 程式庫，用於建構跨平台應用程式。
23. **Servo/Servo**：以 Rust 編寫的高效能並行瀏覽器引擎，由 Mozilla 開發後移交 Linux Foundation。
24. **Rocket/Rocket**：Rust 網頁框架，以型別安全與開發者體驗聞名。
25. **Solana/Solana**：高效能區塊鏈平台，其核心元件大量使用 Rust 編寫。
26. **Substrate/Substrate**：用於建構自訂區塊鏈的框架，同樣大量運用 Rust。
27. **Wasmtime/Wasmtime**：獨立的 JIT 風格 WebAssembly 與 WASI 執行環境。
28. **Delta (dandavison/delta)**：適用於 `diff`、`git` 與 `merge` 輸出的語法突顯分頁工具。
29. **Spotify TUI (Rigellute/spotify-tui)**：Spotify 的終端機使用者介面。
30. **mdBook (rust-lang/mdBook)**：從 Markdown 檔案建立書籍的命令列工具，用於許多 Rust 專案，包括《The Rust Programming Language》書籍。

此清單未能盡錄，Rust 生態圈持續演進，新的影響力專案不斷湧現。社群的優勢在於其協作特性與高品質的開源貢獻。
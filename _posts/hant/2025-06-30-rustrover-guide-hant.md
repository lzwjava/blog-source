---
audio: false
generated: true
lang: hant
layout: post
title: 精通 RustRover：JetBrains 的 Rust IDE
translated: true
type: note
---

以下是 RustRover 的完整指南，這是 JetBrains 專為 Rust 程式設計開發的整合式開發環境。本指南涵蓋其功能、設定、工作流程以及提升生產力的技巧，適合 Rust 新手及資深開發者。

# RustRover 完整指南：JetBrains 專屬 Rust IDE

## 簡介
RustRover 是由 JetBrains 開發的獨立整合式開發環境，專為 Rust 程式設計而設計。它於 2023 年推出，旨在滿足日益壯大的 Rust 社群需求，提供進階的編碼、除錯和管理 Rust 專案工具。與之前的 IntelliJ Rust 外掛不同，RustRover 是一個量身打造的解決方案，深度整合 Rust 生態系統，包括 Cargo、rust-analyzer 等工具，在利用 JetBrains 穩健 IDE 框架的同時，簡化開發流程。本指南將探討 RustRover 的功能、設定流程、工作流程及最佳實踐，協助開發者最大化生產力。[](https://blog.jetbrains.com/rust/2023/09/13/introducing-rustrover-a-standalone-rust-ide-by-jetbrains/)[](https://www.infoq.com/news/2023/09/rustrover-ide-early-access/)

## RustRover 主要功能
RustRover 旨在提升 Rust 開發體驗，其功能針對 Rust 的獨特特性（如記憶體安全性和所有權）而設計。以下是其核心功能：

### 1. **智能程式碼編輯**
- **語法突顯與程式碼完成**：RustRover 提供由 rust-analyzer 驅動的上下文感知程式碼完成功能，適用於變數、函數及 Rust 特定結構（如生命週期和巨集）。行內提示會顯示型別資訊和參數名稱，提升程式碼可讀性。[](https://blog.nashtechglobal.com/exploring-rust-rover-jetbrains-new-rust-ide/)[](https://www.jetbrains.com/help/rust/quick-start-guide-rustrover.html)
- **程式碼導覽**：使用快捷鍵或專案視圖輕鬆跳至定義、尋找用法，並導覽複雜的 Rust 程式碼庫。
- **巨集展開**：行內展開 Rust 巨集，協助開發者理解和除錯複雜的巨集生成程式碼。[](https://appmaster.io/news/jetbrains-launches-rustrover-exclusive-ide-for-rust-language)
- **快速文件**：一鍵或使用快捷鍵（Windows/Linux 為 Ctrl+Q，macOS 為 Ctrl+J）存取 crate 層級和標準函式庫文件。[](https://www.risein.com/blog/top-ides-for-rust-development-in-2025)

### 2. **程式碼分析與錯誤偵測**
- **即時檢查**：RustRover 執行 Cargo Check 並整合外部 linter（如 Clippy），在您輸入時偵測錯誤、借用檢查器問題和程式碼不一致之處。它可視化變數生命週期，協助解決借用檢查器錯誤。[](https://www.jetbrains.com/help/rust/quick-start-guide-rustrover.html)
- **快速修復**：針對常見問題（如新增遺漏的導入或修正語法錯誤）提供自動修復建議。[](https://www.jetbrains.com/rust/whatsnew/)
- **Rustfmt 整合**：使用 Rustfmt 或內建格式化工具自動格式化程式碼，確保風格一致。可透過設定 > Rust > Rustfmt 進行配置。[](https://www.jetbrains.com/help/rust/quick-start-guide-rustrover.html)

### 3. **整合式除錯器**
- **中斷點與變數檢查**：設定中斷點、檢查變數並即時監控堆疊追蹤。支援記憶體和反組譯視圖，用於低階除錯。[](https://blog.nashtechglobal.com/exploring-rust-rover-jetbrains-new-rust-ide/)[](https://www.jetbrains.com/help/rust/quick-start-guide-rustrover.html)
- **除錯配置**：為特定進入點或 Cargo 指令建立自訂除錯配置，可透過工具列或行號列圖示存取。[](https://www.jetbrains.com/help/rust/quick-start-guide-rustrover.html)

### 4. **Cargo 整合**
- **專案管理**：直接在 IDE 內建立、匯入和更新 Rust 專案。透過 Cargo 工具視窗或行號列圖示執行 `cargo build`、`cargo run` 和 `cargo test`。[](https://serverspace.io/support/help/rustrover-a-new-standalone-ide-from-jetbrains-for-rust-developers/)
- **相依性管理**：自動更新相依性和專案配置，簡化與外部 crate 的協作。[](https://serverspace.io/support/help/rustrover-a-new-standalone-ide-from-jetbrains-for-rust-developers/)
- **測試執行器**：一鍵執行單元測試、文件測試和基準測試，結果顯示於 Cargo 工具視窗。[](https://www.jetbrains.com/help/rust/quick-start-guide-rustrover.html)

### 5. **版本控制系統整合**
- 無縫整合 Git、GitHub 及其他 VCS，用於提交、分支和合併。支援透過 Rust Playground 建立 GitHub Gist 以分享程式碼片段。[](https://blog.nashtechglobal.com/exploring-rust-rover-jetbrains-new-rust-ide/)[](https://www.jetbrains.com/help/rust/quick-start-guide-rustrover.html)
- 在編輯器中顯示 VCS 變更，並提供直接從 IDE 提交或還原的選項。

### 6. **網頁與資料庫支援**
- **HTTP 用戶端**：內建 HTTP 用戶端，用於測試 REST API，對使用 Actix 或 Rocket 等框架的 Rust 網頁開發非常實用。[](https://www.infoq.com/news/2023/09/rustrover-ide-early-access/)
- **資料庫工具**：連線至資料庫（如 PostgreSQL、MySQL）並直接在 IDE 內執行查詢，適合全端 Rust 專案。[](https://saltmarch.com/insight/jetbrains-rustrover-pathfinder-of-rust-development-or-off-road)

### 7. **跨平台與外掛支援**
- **跨平台相容性**：可在 Windows、macOS 和 Linux 上使用，確保在不同作業系統間體驗一致。[](https://blog.nashtechglobal.com/exploring-rust-rover-jetbrains-new-rust-ide/)
- **外掛生態系統**：支援 JetBrains Marketplace 外掛以擴展功能，例如額外語言支援或 Docker 等工具。[](https://blog.nashtechglobal.com/exploring-rust-rover-jetbrains-new-rust-ide/)

### 8. **AI 驅動輔助**
- **Junie 編碼代理**：於 RustRover 2025.1 引入，Junie 可自動執行程式碼重構、測試生成和改進等任務，提升生產力。[](https://www.jetbrains.com/rust/whatsnew/)
- **AI 助手**：提供離線和雲端 AI 模型，用於程式碼建議和錯誤解釋，可透過設定配置。[](https://www.jetbrains.com/rust/whatsnew/)

### 9. **使用者介面增強**
- **精簡化 UI**：在 Windows/Linux 上合併主選單和工具列，提供更整潔的介面（可在設定 > 外觀與行為中配置）。[](https://www.jetbrains.com/rust/whatsnew/)
- **Markdown 搜尋**：在 Markdown 預覽（如 README.md）中搜尋，快速存取專案文件。[](https://www.jetbrains.com/rust/whatsnew/)
- **原生檔案對話框**：使用原生 Windows 檔案對話框，提供熟悉體驗，並可選擇還原為 JetBrains 自訂對話框。[](https://www.jetbrains.com/rust/whatsnew/)

## 設定 RustRover
請遵循以下步驟安裝並配置 RustRover 以進行 Rust 開發：

### 1. **安裝**
- **下載**：前往 JetBrains 網站，下載適用於您作業系統（Windows、macOS 或 Linux）的最新版 RustRover。[](https://www.jetbrains.com/rust/download/)
- **系統需求**：確保您擁有 Java 17 或更高版本（隨 RustRover 捆綁），以及至少 8GB RAM 以獲得最佳效能。
- **安裝流程**：執行安裝程式並遵循提示。在 Windows 上，您可能需要 Visual Studio Build Tools 以支援除錯。[](https://saltmarch.com/insight/jetbrains-rustrover-pathfinder-of-rust-development-or-off-road)

### 2. **Rust 工具鏈設定**
- **Rustup 安裝**：若未安裝 Rust 工具鏈（編譯器、Cargo、標準函式庫），RustRover 會提示安裝 Rustup。或者，開啟設定 > 語言與框架 > Rust 並點擊「Install Rustup」。[](https://www.jetbrains.com/help/idea/rust-plugin.html)
- **工具鏈偵測**：安裝後，RustRover 會自動偵測工具鏈和標準函式庫路徑。請在設定 > 語言與框架 > Rust 中驗證。[](https://www.jetbrains.com/help/idea/rust-plugin.html)

### 3. **建立新專案**
1. 啟動 RustRover，在歡迎畫面上點擊 **New Project**，或前往 **File > New > Project**。
2. 在左側窗格中選擇 **Rust**，指定專案名稱和位置，並選擇專案範本（例如 binary、library）。
3. 若工具鏈遺失，RustRover 會提示下載 Rustup。點擊 **Create** 初始化專案。[](https://www.jetbrains.com/help/rust/quick-start-guide-rustrover.html)

### 4. **匯入現有專案**
1. 前往 **File > New > Project from Version Control**，或在歡迎畫面上點擊 **Get from VCS**。
2. 輸入儲存庫 URL（例如 GitHub）和目標目錄，然後點擊 **Clone**。RustRover 會自動配置專案。[](https://www.jetbrains.com/help/rust/quick-start-guide-rustrover.html)

### 5. **配置 Rustfmt**
- 開啟 **Settings > Rust > Rustfmt**，並啟用「Use Rustfmt instead of built-in formatter」核取方塊，以確保程式碼格式化一致。Rustfmt 用於整個檔案和 Cargo 專案，而內建格式化工具則處理程式碼片段。[](https://www.jetbrains.com/help/rust/quick-start-guide-rustrover.html)

## RustRover 工作流程
RustRover 簡化了常見的 Rust 開發任務。以下是關鍵工作流程及範例步驟：

### 1. **編寫與格式化程式碼**
- **範例**：建立一個簡單的 Rust 程式來問候使用者。

```rust
fn main() {
    let name = "Rust Developer";
    greet(name);
}

fn greet(user: &str) {
    println!("Hello, {}!", user);
}
```

- **格式化**：選擇 **Code > Reformat File** (Ctrl+Alt+Shift+L)，使用 Rustfmt 或內建格式化工具格式化程式碼。[](https://www.w3resource.com/rust-tutorial/rust-rover-ide.php)

### 2. **執行與測試**
- **執行程式**：在編輯器中，點擊 `fn main()` 旁行號列的綠色「Run」圖示，或使用 Cargo 工具視窗雙擊 `cargo run`。[](https://www.jetbrains.com/help/rust/quick-start-guide-rustrover.html)
- **執行測試**：對於測試函數，點擊行號列的「Run」圖示，或在 Cargo 工具視窗中雙擊測試目標。範例：
```rust
#[cfg(test)]
mod tests {
    #[test]
    fn test_greet() {
        assert_eq!(2 + 2, 4); // 佔位測試
    }
}
```
- **自訂執行配置**：從工具列選擇配置，以使用特定參數執行。[](https://www.jetbrains.com/help/rust/quick-start-guide-rustrover.html)

### 3. **除錯**
- **設定中斷點**：點擊程式碼行旁的行號列以設定中斷點。
- **開始除錯**：點擊行號列的「Debug」圖示，或從工具列選擇除錯配置。使用除錯器 UI 檢查變數並逐步執行程式碼。[](https://www.jetbrains.com/help/rust/quick-start-guide-rustrover.html)
- **範例**：除錯 `greet` 函數，在執行階段檢查 `user` 變數。

### 4. **分享程式碼**
- 選擇程式碼片段，右鍵點擊並選擇 **Rust > Share in Playground**。RustRover 會建立 GitHub Gist 並提供 Rust Playground 連結。[](https://www.jetbrains.com/help/rust/quick-start-guide-rustrover.html)

### 5. **管理相依性**
- 開啟 `Cargo.toml` 檔案，新增相依性（例如 `serde = "1.0"`），RustRover 會透過 `cargo update` 自動更新專案。[](https://serverspace.io/support/help/rustrover-a-new-standalone-ide-from-jetbrains-for-rust-developers/)

## 使用 RustRover 的最佳實踐
1. **善用行內提示**：啟用行內提示（設定 > 編輯器 > Inlay Hints），以視覺化型別和生命週期，特別是在複雜的所有權情境中。
2. **使用外部 Linter**：在設定 > Rust > External Linters 中配置 Clippy，以進行進階程式碼品質檢查。[](https://www.jetbrains.com/help/rust/quick-start-guide-rustrover.html)
3. **自訂快捷鍵**：在設定 > Keymap 中調整快捷鍵以符合您的工作流程（例如 VS Code 或 IntelliJ 預設）。
4. **啟用 AI 輔助**：使用 Junie 和 AI 助手進行自動程式碼建議和測試生成，特別適用於大型專案。[](https://www.jetbrains.com/rust/whatsnew/)
5. **定期更新外掛**：在設定 > 外觀與行為 > 系統設定 > 更新中啟用自動更新，以保持 RustRover 功能的最新狀態。[](https://www.jetbrains.com/rust/whatsnew/)
6. **參與 EAP**：加入早期存取計劃，測試新功能並提供回饋，協助塑造 RustRover 的發展。[](https://serverspace.io/support/help/rustrover-a-new-standalone-ide-from-jetbrains-for-rust-developers/)[](https://www.neos.hr/meet-rustrover-jetbrains-dedicated-rust-ide/)

## 授權與定價
- **EAP 期間免費**：RustRover 在早期存取計劃期間（已於 2024 年 9 月結束）免費。[](https://blog.jetbrains.com/rust/2023/09/13/introducing-rustrover-a-standalone-rust-ide-by-jetbrains/)
- **商業模式**：EAP 結束後，RustRover 為付費 IDE，提供獨立訂閱或作為 JetBrains All Products Pack 的一部分。定價詳情請參閱 https://www.jetbrains.com/rustrover。[](https://saltmarch.com/insight/jetbrains-rustrover-pathfinder-of-rust-development-or-off-road)[](https://www.neos.hr/meet-rustrover-jetbrains-dedicated-rust-ide/)
- **非商業使用免費**：包含於 JetBrains Student Pack 中，供符合資格的用戶使用。[](https://www.jetbrains.com/help/idea/rust-plugin.html)
- **Rust 外掛**：開源的 IntelliJ Rust 外掛仍可用，但 JetBrains 不再積極開發。它與 IntelliJ IDEA Ultimate 和 CLion 相容，但缺乏新功能。[](https://saltmarch.com/insight/jetbrains-rustrover-pathfinder-of-rust-development-or-off-road)[](https://www.infoq.com/news/2023/09/rustrover-ide-early-access/)

## 社群與支援
- **Rust 支援入口**：透過 Rust 支援入口（rustrover-support@jetbrains.com）回報錯誤和請求功能，而非 GitHub 問題追蹤器。[](https://github.com/intellij-rust/intellij-rust/issues/10867)
- **社群回饋**：Rust 社群對 RustRover 轉向商業模式反應不一。部分開發者欣賞專屬 IDE，而其他則偏好免費替代方案，如 VS Code 搭配 rust-analyzer。[](https://www.reddit.com/r/rust/comments/16hiw6o/introducing_rustrover_a_standalone_rust_ide_by/)[](https://users.rust-lang.org/t/rust-official-ide/103656)
- **Rust Foundation**：JetBrains 是 Rust Foundation 成員，支援 Rust 生態系統的成長。[](https://blog.jetbrains.com/rust/2023/09/13/introducing-rustrover-a-standalone-rust-ide-by-jetbrains/)

## 與其他 Rust IDE 的比較
- **VS Code**：輕量、免費且高度可自訂，搭配 rust-analyzer 和 CodeLLDB 擴充功能。最適合優先考慮靈活性而非一體化解決方案的開發者。[](https://www.risein.com/blog/top-ides-for-rust-development-in-2025)
- **IntelliJ Rust 外掛**：提供與 RustRover 類似的功能，但焦點較不集中且不再積極開發。適合在 IntelliJ IDEA 或 CLion 中進行多語言專案。[](https://www.jetbrains.com/help/idea/rust-plugin.html)
- **CLion**：透過 IntelliJ Rust 外掛支援 Rust，適合 C/C++ 和 Rust 專案，但缺乏 RustRover 的專屬功能。[](https://analyticsindiamag.com/ai-trends/6-ides-built-for-rust/)
- **Neovim/Emacs**：對進階用戶高度可自訂，但需手動設定 Rust 支援。[](https://www.risein.com/blog/top-ides-for-rust-development-in-2025)[](https://metaschool.so/articles/best-ide-for-developing-in-rust)

RustRover 因其深度整合 Rust 生態系統、專業級工具和 JetBrains 精緻的 UI 而脫穎而出，非常適合團隊和大型 Rust 專案。[](https://www.risein.com/blog/top-ides-for-rust-development-in-2025)

## 限制與注意事項
- **學習曲線**：與 VS Code 等輕量編輯器相比，RustRover 功能豐富的介面可能對初學者造成負擔。[](https://metaschool.so/articles/best-ide-for-developing-in-rust)
- **資源使用**：作為完整的 IDE，它比文字編輯器更消耗系統資源。[](https://www.risein.com/blog/top-ides-for-rust-development-in-2025)
- **商業成本**：訂閱模式可能阻礙業餘愛好者，儘管 Student Pack 和 EAP 對部分用戶有所緩解。[](https://users.rust-lang.org/t/rust-official-ide/103656)
- **外掛不確定性**：IntelliJ Rust 外掛在 RustRover 穩定版發布後的長期可用性尚不明確。[](https://saltmarch.com/insight/jetbrains-rustrover-pathfinder-of-rust-development-or-off-road)

## 結論
RustRover 是一個功能強大的 Rust 專用 IDE，透過智能程式碼編輯、穩健的除錯和無縫的 Cargo 整合來提升生產力。其量身打造的功能解決了 Rust 的複雜性（如所有權和記憶體安全性），使其成為專業 Rust 開發者的首選。儘管其商業模式和資源需求可能不適合所有人，但其全面的工具集和 JetBrains 對 Rust 生態系統的承諾，使其成為嚴肅專案的寶貴投資。請透過 JetBrains 網站試用 RustRover，並加入 EAP 以塑造其未來。[](https://blog.nashtechglobal.com/exploring-rust-rover-jetbrains-new-rust-ide/)[](https://blog.jetbrains.com/rust/2023/09/13/introducing-rustrover-a-standalone-rust-ide-by-jetbrains/)

如需進一步詳情，請造訪 [JetBrains RustRover 文件](https://www.jetbrains.com/rustrover) 或探索 [Rust 支援入口](mailto:rustrover-support@jetbrains.com)。
---
audio: false
generated: true
lang: hant
layout: post
title: Rust於大型科技企業的崛起
translated: true
type: note
---

Rust 因其對記憶體安全、效能和並行處理的強力專注，在大型科技公司中正獲得顯著關注。許多主要科技公司正在各種關鍵專案中採用 Rust。以下是一些知名範例的詳細說明：

**1. 亞馬遜 (AWS)**
* **Firecracker：** 一種微虛擬機，專為安全大規模執行容器工作負載而設計，為 AWS Lambda 和 Fargate 提供支援。
* **AWS Nitro System：** 用於開發新元件，包括安全且隔離的 EC2 環境。
* **其他服務：** Rust 用於 Amazon S3、Amazon EC2、Amazon CloudFront 和 Amazon Route 53 的元件中。
* **Bottlerocket：** 一個以 Rust 編寫的 Linux 基礎容器作業系統。

**2. 微軟**
* **Windows 元件：** 微軟正積極以 Rust 重寫部分 Windows 元件，包括核心元件，以提升安全性和可維護性。
* **Azure 服務：** Rust 已整合到 Azure IoT Edge 和 Kusto（Azure Data Explorer 的核心查詢與儲存引擎）中。
* **`windows-rs`：** 一個允許使用 Rust 呼叫 Windows API 的專案。

**3. Meta (Facebook)**
* **內部原始碼控制工具：** Meta 使用 Rust 重建了其內部原始碼控制系統（Mononoke）的部分元件，以更好地處理其大型單一儲存庫的並行處理和速度。
* **Diem（前身為 Libra）區塊鏈：** 該加密貨幣專案的區塊鏈主要使用 Rust 編寫。

**4. Google**
* **Android 開放原始碼計畫 (AOSP)：** Rust 越來越多地用於在 Android 中編寫安全的系統元件，減少了媒體處理和檔案系統存取等關鍵功能中的記憶體錯誤。
* **Fuchsia OS：** Fuchsia OS 的內部程式碼有相當大比例是以 Rust 編寫。
* **Chromium：** Chromium 中存在對 Rust 的實驗性支援。

**5. Dropbox**
* **同步引擎：** Rust 取代了 Dropbox 檔案同步引擎中舊有的 Python 和 C++ 程式碼，從而降低了 CPU 使用率、改善了並行處理並使同步更順暢。
* **核心檔案儲存系統：** 其核心檔案儲存系統的數個元件均以 Rust 編寫。

**6. Discord**
* **後端服務：** Discord 使用 Rust 處理關鍵後端服務，如訊息路由和線上狀態追蹤，從而提升了效能和可靠性。他們將「讀取狀態」服務從 Go 切換到 Rust，以避免延遲飆升。
* **客戶端與伺服器端：** Discord 程式碼庫的客戶端和伺服器端均包含 Rust 元件。

**7. Cloudflare**
* **Pingora：** 一個以 Rust 編寫的高效能網路代理，用於取代 NGINX，從而降低了 CPU 使用率並改善了連線管理。
* **核心邊緣邏輯：** Rust 用於 Cloudflare 的核心邊緣邏輯，以取代像 C 這類記憶體不安全的語言。
* **Cloudflare Workers：** 支援使用 Rust 進行無伺服器程式碼部署。

**8. Mozilla**
* **Firefox (Stylo)：** Rust 的原始創造者 Mozilla，使用該語言構建了 Firefox 中的 CSS 引擎 Stylo，顯著提升了效能和安全性。
* **Servo：** 一個完全以 Rust 構建的原型網頁瀏覽器引擎。

**9. npm (Node Package Manager)**
* **驗證服務：** npm 使用 Rust 重寫了其部分驗證服務，以提升安全性、處理負載並減少延遲。

**其他值得注意的採用者與專案：**
* **Linux 核心：** Rust 現已成為 Linux 核心開發的第二官方語言，允許開發更安全的裝置驅動程式和其他模組。
* **Figma：** 他們的多人同步引擎從 TypeScript 重寫為 Rust，以提升效能。
* **1Password：** 使用單一共享的 Rust 程式碼庫為其最新的桌面和行動應用程式提供支援。
* **Hugging Face：** 其 AI 生態系統中的許多元件，包括 `safetensors`、`tokenizer` 和 `candle`，均使用 Rust 實作。
* **Polkadot：** 此區塊鏈平台完全以 Rust 構建，以確保安全性和速度。
* **Solana：** 另一個利用 Rust 的高效能區塊鏈平台。
* **Brave Browser：** 在其部分元件中使用 Rust。
* **Atlassian：** 在一項用於分析 PB 級原始碼的服務中使用 Rust。
* **華為：** 將其部分程式碼庫遷移至 Rust，用於電信設備和基礎設施工具。

這些主要科技公司對 Rust 的採用，凸顯了它在構建可靠、高效且安全的軟體方面日益增長的重要性，特別是在系統級程式設計、基礎設施和高效能應用領域。
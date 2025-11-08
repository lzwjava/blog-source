---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Union ZK 跨鏈基礎設施協議
translated: true
type: note
---

### 概述
GitHub 儲存庫 [https://github.com/unionlabs/union](https://github.com/unionlabs/union) 是 **Union** 的官方開源程式碼庫，這是由 Union Labs 開發的零知識（ZK）基礎設施協議。Union 旨在實現不同區塊鏈之間的無縫安全互通，讓資產和數據能夠跨鏈流動，無需依賴傳統橋接器、託管方或可信中介。它利用 ZK 證明來驗證交易和狀態轉換，專注於多鏈生態系統中的可擴展性、隱私性和可組合性。

### 主要功能
- **ZK 輕客戶端**：使用零知識證明進行輕量級、最小化信任的區塊鏈狀態和共識驗證，減少對重型中繼器的依賴。
- **互通性基礎元件**：支援跨鏈訊息傳遞、資產轉移（例如代幣、NFT）以及在 EVM 兼容鏈及其他鏈之間的任意數據傳輸。
- **模組化架構**：基於 Cosmos SDK 和 Tendermint 共識構建，但可擴展至其他框架。包含 Union 中繼器、證明生成器和驗證器合約等組件。
- **安全優先**：強調使用 Groth16 證明和 BLS 簽名等密碼學基礎元件，以防範常見的橋接攻擊。

### 開發狀態（截至 2025 年 11 月）
- 該儲存庫積極維護中，近期提交專注於測試網整合（例如 Union Testnet v2 於 2025 年中啟動）。
- 已獲得超過 500 個星標，有 50 多名開發者貢獻，並採用 Apache-2.0 許可證。
- 文檔包含運行節點、部署合約以及與 MetaMask 等錢包整合的設置指南。

### 應用場景
- DeFi 協議在 Ethereum、Solana 和 Cosmos 生態系統之間橋接流動性。
- 需要跨鏈可移植性的遊戲和 NFT 項目。
- 需要在分類帳之間進行私有、可驗證數據共享的企業應用程式。

如果您是開發者，可以克隆該儲存庫並從 `make install` 開始安裝依賴項，然後使用 `make build` 進行編譯。更多資訊，請查閱 [文檔文件夾](https://github.com/unionlabs/union/tree/main/docs) 或 Union Labs 的網站。

[Union Labs 網站](https://union.build/)  
[Union 白皮書](https://union.build/whitepaper)  
[GitHub 儲存庫](https://github.com/unionlabs/union)
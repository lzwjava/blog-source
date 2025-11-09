---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: NanoChat 緊湊型全端大型語言模型
translated: true
type: note
---

### 什麼是 NanoChat？

NanoChat 是一個精簡、全堆疊的大型語言模型（LLM）系統實作，類似 ChatGPT，建構於單一且極簡的程式碼庫中，易於修改且依賴項極少。由 Andrej Karpathy（以其在 AI 領域的貢獻聞名，例如 nanoGPT）創建，它設計用於在負擔得起的硬體（例如單一 8xH100 GPU 節點）上運行完整的 LLM 流程——從分詞化和預訓練到微調、評估、推理，甚至提供一個簡單的網頁界面與你的模型對話。

它被定位為「100 美元能買到的最佳 ChatGPT」，作為預算友好型 LLM 開發（總成本低於 1,000 美元）的基準。這使其成為 Eureka Labs 即將推出的 LLM101n 課程的頂點項目，強調簡潔性而非複雜配置。

### 主要功能
- **端到端流程**：以約 2,000 行程式碼（及一個極小的 `uv.lock` 依賴文件）處理所有步驟。在約 24 美元/小時的 8xH100 設置上，約 4 小時內訓練出一個具有 4e19 FLOPs 能力的模型。
- **類 ChatGPT 界面**：訓練完成後，可啟動網頁伺服器與模型互動，就像使用真正的 ChatGPT 一樣。
- **評估報告**：自動生成 `report.md` 報告，包含在 ARC-Challenge、GSM8K、HumanEval、MMLU 等任務上的基準測試分數。例如，一個 100 美元的運行樣本顯示了各階段（BASE、MID、SFT、RL）的逐步改進：

| 指標          | BASE   | MID    | SFT    | RL     |
|---------------|--------|--------|--------|--------|
| CORE          | 0.2219 | -      | -      | -      |
| ARC-Challenge | -      | 0.2875 | 0.2807 | -      |
| ARC-Easy      | -      | 0.3561 | 0.3876 | -      |
| GSM8K         | -      | 0.0250 | 0.0455 | 0.0758 |
| HumanEval     | -      | 0.0671 | 0.0854 | -      |
| MMLU          | -      | 0.3111 | 0.3151 | -      |
| ChatCORE      | -      | 0.0730 | 0.0884 | -      |

（總時間：完整運行約 3 小時 51 分鐘。）
- **硬體靈活性**：可在 Ampere 8xA100（較慢）、單一 GPU（帶自動梯度累積）或低 VRAM 設置上運行，只需調整批次大小。使用標準 PyTorch；可透過調整適應其他設備。
- **數據來源**：從 Hugging Face 數據集（如 FineWeb 和 SmolTalk）獲取數據。
- **額外功能**：包含測試（例如用於 Rust 分詞器的測試），且易於打包整個程式庫（約 330KB）以供其他 LLM 查詢。

它受到 Karpathy 早期 nanoGPT 項目和 modded-nanoGPT 的啟發，但擴展為完整的對話體驗。

### 如何開始使用
最快的方式是使用 `speedrun.sh` 腳本，該腳本在 8xH100（例如透過 Lambda Labs）上端到端處理 100 美元級別的模型：

1. 啟動一個 8xH100 實例並克隆程式庫。
2. 運行：
   ```
   bash speedrun.sh
   ```
   （或在 screen 會話中運行以記錄日誌：`screen -L -Logfile speedrun.log -S speedrun bash speedrun.sh`。使用 Ctrl+A+D 分離並 tail 日誌。）

3. 完成後（約 4 小時），啟動環境（`source .venv/bin/activate`）並啟動網頁界面：
   ```
   python -m scripts.chat_web
   ```
   打開本地 URL（例如 http://your-ip:8000）與你的模型對話。查看 `report.md` 獲取結果。

對於更大的模型（例如 300 美元級別，約 12 小時，在某些分數上超越 GPT-2），編輯 `speedrun.sh` 以下載更多數據分片並調整深度/批次大小。運行測試如 `python -m pytest tests/test_rustbpe.py -v -s`。

它採用 MIT 許可證，並開放貢獻以推動微型模型的進一步發展。詳細指南請查閱程式庫的 Discussions。

[nanoChat GitHub 程式庫](https://github.com/karpathy/nanochat)
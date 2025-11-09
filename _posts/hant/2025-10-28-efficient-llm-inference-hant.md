---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 高效 LLM 推理：使用 vLLM
translated: true
type: note
---

### vLLM：高效的大型語言模型推理與服務

vLLM 是一個專為快速、記憶體高效的大型語言模型推理與服務而設計的開源函式庫。最初由加州大學柏克萊分校的 Sky Computing Lab 開發，現已成為廣泛應用於生產環境的社群驅動項目，用於部署如 Llama 或 GPT 變體等大型語言模型。其核心創新是 **PagedAttention**，這項技術將鍵值快取記憶體視為虛擬記憶體分頁，減少浪費並透過動態分配非連續區塊實現更高吞吐量。

#### 運作原理
- **連續批次處理**：與傳統系統等待完整批次不同，vLLM 在執行過程中動態新增/移除請求，最大限度減少解碼期間的 GPU 閒置時間。
- **記憶體管理**：PagedAttention 避免 KV 快取中的碎片化（其大小隨序列長度增長），支援更長上下文而不會出現記憶體不足錯誤。
- **最佳化執行**：使用 CUDA/HIP 圖實現更快的核心啟動，與 FlashAttention/FlashInfer 整合進行注意力計算，並支援量化（如 AWQ、GPTQ、FP8）以將記憶體使用量減少高達 4 倍。
- **進階功能**：包括推測解碼（猜測詞元並驗證）、分塊預填充（用於長輸入）、多 LoRA（即時調整模型）以及分散式平行處理（張量、管道、專家）。

vLLM 提供 OpenAI 相容的 API 伺服器，與 Hugging Face 模型無縫整合，並可在多種硬體上執行（NVIDIA/AMD/Intel GPU、TPU、CPU）。它非常適合高吞吐量場景，在服務基準測試中比 Hugging Face Transformers 等基線實現 2-10 倍的速度提升。

#### 主要應用場景
- 用於聊天機器人或具有串流輸出的 API 的在線服務。
- 用於摘要生成等任務的離線批次推理。
- 無需自訂底層架構即可擴展至多 GPU 叢集。

### Ray：用於擴展 AI 和 Python 應用程式的統一框架

Ray 是一個開源分散式計算框架，可輕鬆將 Python 程式碼（尤其是 AI/ML 工作負載）從單一機器擴展到大規模叢集。由 Anyscale（源自加州大學柏克萊分校）創建，它抽象了分散式系統的複雜性，如排程、容錯和協調，讓開發人員能專注於邏輯。

#### 主要元件
- **Ray Core**：基礎架構 — 提供 Python 風格的基礎元件，用於任務（平行函式）、參與者（有狀態服務）和物件（分散式資料共享）。它自動處理自動擴展、重試和資源分配。
- **Ray AI 函式庫**：基於 Core 構建的領域特定工具：
  - **Ray Data**：用於預處理資料集的可擴展 ETL。
  - **Ray Train**：具有整合功能（PyTorch、TensorFlow、Hugging Face）的分散式訓練。
  - **Ray Tune**：大規模超參數優化。
  - **Ray Serve**：用於推理的模型部署，包含路由、批次處理和 A/B 測試。
  - **RLlib**：強化學習工具包。
- **Ray 叢集**：用於在雲端（AWS、GCP）、Kubernetes 或本地部署的受管基礎設施層，可根據需求自動擴展。

#### 運作原理
Ray 以守護行程形式在節點上執行，形成一個以頭節點進行協調的叢集。您可以使用 `@ray.remote` 裝飾函式以實現平行處理，它會將執行分佈到 CPU/GPU 上。對於 ML，像 Serve 這樣的函式庫處理 HTTP 端點和負載平衡，而 Core 確保容錯擴展（例如重啟失敗的任務）。

#### 在 ML/AI 中的主要應用場景
- 端到端管道：資料載入 → 訓練 → 調優 → 服務。
- 在數百個 GPU 上進行超參數掃掠。
- 即時推理集群，如推薦系統中的應用。
- 自訂分散式應用程式，例如模擬。

Ray 的優勢在於其統一的 API：編寫一次，隨處擴展，與 Spark 或 Dask 相比，樣板程式碼更少。

### vLLM 與 Ray 的關係
在如 SLOs-Serve（我們先前討論過的）這樣的系統中，vLLM 負責底層的 LLM 批次處理/推理，而 Ray 則協調多副本部署，跨節點路由請求以處理突發流量和擴展。

[vLLM 文件](https://docs.vllm.ai/en/latest/)  
[Ray 文件](https://docs.ray.io/en/latest/ray-overview/index.html)
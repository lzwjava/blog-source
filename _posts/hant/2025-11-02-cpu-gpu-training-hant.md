---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: CPU 與 GPU 訓練效能比較
translated: true
type: note
---

在筆記型電腦上運行 NanoGPT 訓練時出現的低 MFU（0.01%）問題，源於您指令中的 `--device=cpu` 旗標，這會強制將整個工作負載交由 CPU 處理，而非利用 GPU 加速。以下是問題成因及與 4070 Ti 設定的對照分析：

### 筆記型電腦 MFU 偏低的主要原因
- **CPU 與 GPU 架構不匹配**：像 NanoGPT 中的 Transformer 模型（即使是微型配置：4 層、128 嵌入維度、批次大小 12）本質上是高度可並行化的矩陣運算（例如注意力機制、前饋神經網絡），這類運算正是 GPU 透過數千核心與高頻寬記憶體的強項。CPU（即使是您筆電配備的 Intel Alder Lake-P 系列）則是以序列化或有限並行方式處理這類任務。PyTorch 在 CPU 上雖會使用優化過的 BLAS（如 OpenBLAS），但對此類模型的 FLOPs 吞吐量仍不及 GPU 的 1%。MFU 衡量的是「相對於理論峰值 FLOPs 的利用率」，因此以 CPU 為主的運行自然會呈現如 0.01% 的極低數值——這並非「故障」，只是對此任務效率低下。

- **未啟用 GPU 卸載機制**：您的筆電硬體（來自 Alder Lake-P 的 Intel UHD 顯示晶片）不支援 CUDA，因此 PyTorch 在未調整設定時會預設使用 CPU。`get_gpu_info.py` 的輸出顯示整合式 Intel iGPU 被誤標為「AMD」（可能是腳本解析 `lspci` 時的錯誤），但即使可正常識別，標準 PyTorch 也無法直接透過 Intel/AMD iGPU 加速訓練。您需要額外安裝 Intel oneAPI（透過 `torch.backends.mps` 或擴充套件）或 AMD ROCm 等工具，但這些方案仍屬實驗性質，效能也無法與 NVIDIA 媲美。

- **模型與工作負載規模**：這是個在小型資料集（莎士比亞字元集，block_size=64）上運行的微型模型。在 CPU 環境中，資料載入、Python 迴圈及非 FLOP 運算的負擔會更加明顯，進一步拉低 MFU。您的 max_iters=2000 與 log_interval=1 設定意味著頻繁的檢查點與評估操作，加劇了 CPU 瓶頸。

### 與 4070 Ti（10% MFU）的對照
- **硬體吞吐量差距**：4070 Ti（RTX 40 系列，約 29 TFLOPs FP16）處理此模型的速度可比筆電 CPU（對機器學習任務的有效運算力約 0.5-1 TFLOPs）快 10-20 倍。在小型模型上達到 10% MFU 對 NanoGPT 而言已屬理想——未達 100% 是因為核心啟動負擔、記憶體頻寬限制及非最佳化批次大小所致。若將 batch_size 提高（例如 128+）或使用 FP16/bfloat16，可將 MFU 提升至 15-20%，但您的設定較為保守。

- **隱性 GPU 模式**：在 4070 Ti 環境中，您很可能使用 `--device=cuda` 運行（NanoGPT 在偵測到可用 GPU 時的預設值），這能啟用完整的張量並行化及 cuBLAS/cuDNN 核心優化，從而大幅提升 MFU。

| 比較維度         | 筆記型電腦 (CPU)                  | 4070 Ti (GPU)                     |
|------------------|-----------------------------------|-----------------------------------|
| **運算裝置**     | CPU（強制使用）                   | CUDA GPU                          |
| **峰值 FLOPs**   | ~0.5-1 TFLOPs（針對 ML 優化）     | ~29 TFLOPs（FP16）                |
| **達成 MFU**     | 0.01%（CPU 負擔為主因）           | 10%（並行化優勢顯現）             |
| **訓練時間預估（2000 次迭代）** | 10-30+ 分鐘（I/O 緩慢） | <1 分鐘（極速）                   |
| **瓶頸**         | 序列化執行、記憶體限制            | 記憶體頻寬、核心效率              |

### 提升筆記型電腦訓練效能的快速解決方案
- **盡可能切換至 GPU 環境**：若可透過 SSH 遠端操作 4070 Ti（例如使用 `torchrun`），請直接於該環境運行。若欲使用本地 Intel iGPU，可嘗試：
  ```
  pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu  # 確保 CPU 後備模式
  # 或使用 Intel oneAPI（實驗性功能）：
  conda install intel-extension-for-pytorch -c intel
  ```
  接著測試 `--device=cuda`（會報錯）或於啟用 IPEX 時使用 `device='xpu'`。預期最佳 MFU 僅 1-5%——仍不理想。

- **優化 CPU 運行模式**：
  - 在記憶體許可下將 `batch_size` 增至 24-48（您的 Ubuntu 24.04 系統搭配 glibc2.39 有充足記憶體）。
  - 加入 `--compile=True`（PyTorch 2.0+ 動態編譯可提升 CPU 速度約 20-50%）。
  - 在資料載入器中設定 `num_workers=4` 實現 I/O 並行化。
  - 使用 `taskset -c 0-7` 將進程綁定至效能核心（可透過 `lscpu` 確認核心配置）。

- **進行基準測試**：在 4070 Ti 設備上以 `--device=cuda` 重新運行，取得直接對照結果（應可達到約 10% MFU）。若您提供確切的 NanoGPT 儲存庫版本，我可進一步建議設定調整方向。

此為正常現象——CPU 本就不適用於正式環境的機器學習訓練。若問題持續存在，請提供完整訓練日誌以便深入除錯！
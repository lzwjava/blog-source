---
audio: false
generated: true
lang: hant
layout: post
title: 混合硬件環境下的 Ray 分散式訓練
translated: true
type: note
---

是的，你可以使用 Python 在 MacBook Air M2（採用 Apple Silicon，使用 MPS 後端進行 GPU 加速）和配備 NVIDIA 4070Ti 的 Intel i9 桌面電腦（支援 CUDA）之間進行機器學習模型的分散式訓練。然而，這種設置是異構的（不同的架構、作業系統和加速器），因此不如同構集群（例如全部使用 NVIDIA GPU）那麼直接。由於後端不相容，像 PyTorch 這樣的框架中的原生分散式訓練無法開箱即用無縫工作——PyTorch 在你的 Mac 上使用 MPS，而在桌面電腦上使用 CUDA，並且像 NCCL（高效 GPU 到 GPU 同步所需）這樣的通訊庫僅限於 NVIDIA，在 Apple Silicon 上不可用。

話雖如此，你可以使用像 Ray 這樣的高階編排庫來實現分散式訓練，它抽象化了硬體差異。其他選項如 Dask 或自訂框架也存在，但在深度學習方面較為有限。我將在下面概述可行性、推薦方法和替代方案。

### 推薦方法：使用 Ray 進行分散式訓練
Ray 是一個基於 Python 的分散式計算框架，它與硬體無關，並支援在混合機器（例如，Apple Silicon 的 macOS 和 NVIDIA 的 Windows/Linux）上擴展 ML 工作負載。它在兩個平台上都能安裝，並且可以通過在每台機器的可用硬體（Mac 上的 MPS，桌面電腦上的 CUDA）上運行任務來處理異構加速器。

#### 工作原理
- **設置**：通過 pip 在兩台機器上安裝 Ray（`pip install "ray[default,train]"`）。啟動一個 Ray 集群：一台機器作為頭節點（例如你的桌面電腦），並將 Mac 作為工作節點通過網絡連接。Ray 通過自己的協議處理通訊。
- **訓練模式**：使用 Ray Train 來擴展像 PyTorch 或 TensorFlow 這樣的框架。對於異構設置：
  - 採用「參數伺服器」架構：一個中央協調器（在一台機器上）管理模型權重。
  - 定義在特定硬體上運行的工作節點：對你的 NVIDIA 桌面電腦（CUDA）使用像 `@ray.remote(num_gpus=1)` 這樣的裝飾器，對 Mac（MPS 或 CPU 後備）使用 `@ray.remote(num_cpus=2)` 或類似裝飾器。
  - 每個工作節點在其本地設備上計算梯度，將其發送到參數伺服器進行平均，並接收更新後的權重。
  - Ray 自動分發數據批次並在機器之間同步。
- **示例工作流程**：
  1. 在 PyTorch 中定義你的模型（在 Mac 上設置設備為 `"mps"`，在桌面電腦上設置為 `"cuda"`）。
  2. 使用 Ray 的 API 來包裝你的訓練循環。
  3. 在頭節點上運行腳本；Ray 將任務分派給工作節點。
- **性能**：由於網絡開銷且沒有直接的 GPU 到 GPU 通訊（例如通過 NCCL），訓練將比純 NVIDIA 集群慢。Mac 的 M2 GPU 比 4070Ti 弱，因此要相應地平衡工作負載（例如在 Mac 上使用較小的批次）。
- **限制**：
  - 最適合數據並行訓練或超參數調整；在異構設置中，模型並行（將大模型拆分到多個設備上）更為棘手。
  - 對於非常大的模型（例如 10 億+ 參數），需添加像混合精度、梯度檢查點或與 DeepSpeed 整合這樣的技術。
  - 機器之間的網絡延遲可能成為瓶頸；確保它們在同一個快速區域網路上。
  - 測試過的例子顯示它在 Apple M4（類似 M2）+ 較舊的 NVIDIA GPU 上可行，但要針對你的 4070Ti 的優勢進行優化。

一個實用範例和程式碼可在名為 "distributed-hetero-ml" 的框架中找到，它簡化了異構硬體的設置。

#### 為什麼 Ray 適合你的設置
- 跨平台：適用於 macOS（Apple Silicon）、Windows 和 Linux。
- 與 PyTorch 整合：使用 Ray Train 來擴展你現有的程式碼。
- 不需要相同的硬體：它會檢測並使用 Mac 上的 MPS 和桌面電腦上的 CUDA。

### 替代方案：使用 Dask 處理分散式工作負載
Dask 是另一個用於平行計算的 Python 庫，適用於分散式數據處理和一些 ML 任務（例如通過 Dask-ML 或 XGBoost）。
- **方法**：設置一個 Dask 集群（一個調度程序在你的桌面電腦上，工作節點在兩台機器上）。在 NVIDIA 端使用像 CuPy/RAPIDS 這樣的庫進行 GPU 加速，在 Mac 上則後備使用 CPU/MPS。
- **使用案例**：適合集成方法、超參數搜索或 scikit-learn 風格的模型。對於深度學習，可與 PyTorch/TensorFlow 配對使用，但同步是手動的且效率低於 Ray。
- **限制**：未針對同步深度學習訓練進行優化（例如沒有內建的參數伺服器）；更適合易平行任務。GPU 支援在 NVIDIA 上需要 CUDA，但 Mac 將使用 CPU 或有限的 MPS 整合。
- **設置**：`pip install dask distributed`，然後啟動集群並提交作業。

### 其他選項和注意事項
- **Horovod**：這個分散式訓練包裝器（用於 PyTorch/TensorFlow）可以安裝在 macOS 上，但缺乏明確的 MPS 支援。它可以使用 Gloo 或 MPI 進行通訊（跨平台），但在 Mac 上沒有 NCCL 效率會下降。可能可行，但未針對你的具體混合環境進行測試——如果 Ray 不適合，可以嘗試它。
- **自訂框架**：像 HetSeq 這樣的工具允許異構 GPU 訓練，但它們主要針對混合 NVIDIA/AMD，而非 Apple Silicon + CUDA。
- **所有方案的挑戰**：
  - 作業系統差異：假設你的桌面電腦運行 Linux/Windows；確保相容的 Python 版本（推薦 3.10+）。
  - 依賴項：在 Mac 上安裝帶有 MPS 的 PyTorch（`pip install torch --extra-index-url https://download.pytorch.org/whl/cpu`），在桌面電腦上安裝帶有 CUDA 的 PyTorch。
  - 數據共享：使用共享文件系統（例如 NFS）或雲端儲存來處理數據集。
  - 測試：從小規模開始——訓練一個簡單的 CNN 在 MNIST 上進行驗證。
- **何時避免**：如果模型較小，僅在 4070Ti 上訓練（更快）。對於生產環境，考慮使用雲端 GPU 以實現同構性。

如果你能提供更多細節（例如框架如 PyTorch/TensorFlow、模型類型、桌面電腦的作業系統），我可以進一步細化這一點。

[身為 GPU 貧民激發創意](https://www.dilawar.ai/2025/07/04/Multi-Cluster%20Distributed%20Training%20on%20Heterogeneous%20Hardware/)  
[Ray 文檔 - 安裝](https://docs.ray.io/en/latest/ray-overview/installation.html)  
[Ray Train：可擴展的模型訓練](https://docs.ray.io/en/latest/train/train.html)  
[Dask 文檔 - GPU](https://docs.dask.org/en/stable/gpu.html)  
[Horovod 安裝指南](https://horovod.readthedocs.io/en/latest/install_include.html)  
[HetSeq GitHub](https://github.com/yifding/hetseq)  
[在 Mac 上加速 PyTorch 訓練](https://developer.apple.com/metal/pytorch/)
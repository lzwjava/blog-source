---
audio: false
generated: true
image: false
lang: hant
layout: post
title: CUDA 函式庫與套件
translated: true
type: note
---

以下是你即將安裝的各個套件簡介：

* **nvidia-cusparselt-cu12**
  NVIDIA 的 cuSPARSELt 函式庫，用於在 CUDA 12 上執行超高效能的低精度稀疏矩陣運算。

* **nvidia-cusparse-cu12**
  cuSPARSE 函式庫，提供在 CUDA 12 上執行通用稀疏線性代數常式（例如稀疏求解器）。

* **nvidia-cudnn-cu12**
  cuDNN 函式庫，為深度神經網路提供高度優化的基礎運算（卷積、池化、激活函數等）於 CUDA 12 環境。

* **nvidia-cublas-cu12**
  cuBLAS 函式庫，實現在 CUDA 12 上高效能的密集線性代數（BLAS）常式。

* **nvidia-cufft-cu12**
  cuFFT 函式庫，用於在 CUDA 12 裝置上計算快速傅立葉轉換。

* **nvidia-cusolver-cu12**
  cuSOLVER 函式庫，包含用於密集與稀疏直接求解器、特徵值問題等常式，支援 CUDA 12。

* **nvidia-curand-cu12**
  cuRAND 函式庫，用於在 CUDA 12 上生成高品質隨機數。

* **nvidia-cufile-cu12**
  cuFile 函式庫，實現直接在 CUDA 12 上進行非同步 GPU 加速檔案 I/O。

* **nvidia-nvtx-cu12**
  NVTX（NVIDIA 工具擴展），用於在 CUDA 12 上標註和分析程式碼範圍。

* **nvidia-nvjitlink-cu12**
  NVJITLink 函式庫，用於在 CUDA 12 上於執行階段即時連結 CUDA 核心。

* **nvidia-cuda-nvrtc-cu12**
  NVRTC 執行階段編譯器，用於在 CUDA 12 環境下即時編譯 CUDA C 核心。

* **nvidia-cuda-cupti-cu12**
  CUPTI（CUDA 分析工具介面），用於在 CUDA 12 上收集細粒度分析與追蹤資料。

* **nvidia-cuda-runtime-cu12**
  核心 CUDA 執行階段函式庫，用於在 CUDA 12 上管理和啟動核心。

* **nvidia-nccl-cu12**
  NCCL 函式庫，提供在 CUDA 12 上高效能的多 GPU 與多節點集合通訊基礎操作。

* **torch**
  主要 PyTorch 函式庫，用於張量運算、自動微分和建構深度學習模型。

* **networkx**
  用於建立、操作和分析複雜網絡與圖結構的 Python 套件。

* **mpmath**
  用於任意精度實數與複數運算的純 Python 函式庫。

* **sympy**
  用於符號數學（代數、微積分、方程式求解等）的 Python 函式庫。

* **triton**
  一種語言和編譯器，讓你能比原始 CUDA 更輕鬆地編寫自訂高效能 GPU 核心。
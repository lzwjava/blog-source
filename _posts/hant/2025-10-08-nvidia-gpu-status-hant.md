---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: NVIDIA GPU 狀態概覽
translated: true
type: note
---

### 概覽
這是 `nvidia-smi` 指令的輸出結果，該工具用於監控和管理 Linux 系統（從路徑來看，似乎是 Ubuntu 或類似發行版）上的 NVIDIA GPU。它提供了 GPU 狀態的快照，包括硬體詳細資訊、使用率、功耗、記憶體使用情況以及正在執行的處理程序。該指令於 2025 年 10 月 7 日凌晨 3:16:58 在 nanoGPT 專案（一個基於 PyTorch 的熱門 GPT 訓練程式庫）相關目錄中執行。

輸出分為三個主要部分：包含軟體版本的標頭、總結 GPU 當前狀態的表格，以及使用 GPU 的處理程序表格。我將逐步解析各部分。

### 標頭
```
Tue Oct  7 03:16:58 2025       
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 535.247.01             Driver Version: 535.247.01   CUDA Version: 12.2     |
```
- **時間戳記**：指令執行的時間。
- **NVIDIA-SMI 版本**：535.247.01（工具本身版本）。
- **驅動程式版本**：535.247.01（系統上安裝的 NVIDIA 核心驅動程式版本）。
- **CUDA 版本**：12.2（用於 GPU 加速計算的 CUDA 工具包版本，例如 PyTorch 或 TensorFlow）。

此配置相容於現代機器學習工作負載，例如在 nanoGPT 中訓練模型。

### GPU 狀態表格
此表格顯示了檢測到的單一 GPU（索引 0）的詳細資訊。表格欄位包含硬體 ID、顯示狀態、錯誤校正以及即時指標。

```
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  NVIDIA GeForce RTX 4070        On  | 00000000:01:00.0  On |                  N/A |
| 32%   47C    P2              74W / 215W |   3144MiB / 12282MiB |      2%      Default |
|                                         |                      |                  N/A |
```
- **GPU 0**：第一個（且唯一）的 GPU。
- **名稱**：NVIDIA GeForce RTX 4070（消費級 GPU，配備 12GB GDDR6X 視訊記憶體，適用於遊戲和機器學習訓練）。
- **Persistence-M**：「On」表示 GPU 驅動程式即使在沒有應用程式使用時仍保持載入（減少應用程式的啟動延遲）。
- **Bus-Id**：00000000:01:00.0（PCIe 插槽位址；對於多 GPU 設定除錯很有用）。
- **Disp.A**：「On」表示 GPU 正在驅動顯示器（例如您的螢幕）。
- **Volatile Uncorr. ECC**：N/A（記憶體錯誤校正碼；消費級 GPU 如 4070 不支援/啟用）。
- **風扇**：32% 轉速（冷卻風扇以中等速度運行）。
- **溫度**：47°C（當前溫度；安全，因為 RTX 4070 最高可承受約 90°C）。
- **效能**：P2（效能狀態；P0 為最大加速，P8 為閒置—P2 為平衡的中等狀態）。
- **功耗：使用/上限**：74W 當前功耗，上限為 215W（低功耗，表示輕負載）。
- **記憶體使用量**：3144MiB 已使用，總共 12282MiB（約 3GB/12GB；約 26% 滿載—尚有空間容納更大模型）。
- **GPU 使用率**：2%（核心使用率；非常低，表示 GPU 大部分處於閒置狀態）。
- **計算模式**：Default（計算模式；允許多個處理程序共享 GPU）。
- **MIG 模式**：N/A（多實例 GPU 分割；此消費級顯示卡不支援）。

總體而言，您的 GPU 狀態健康且負載較輕—可能僅在處理桌面圖形和一些背景任務。

### 處理程序表格
此表格列出了當前使用 GPU 記憶體或計算資源的所有處理程序。欄位包括 GPU 索引、處理程序 ID（此處 GI/CI 為 N/A，因為它們用於進階多實例追蹤）、PID（處理程序 ID）、類型（G=圖形，如渲染；C=計算，如機器學習訓練）、處理程序名稱和記憶體使用量。

```
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
|    0   N/A  N/A      2927      G   /usr/lib/xorg/Xorg                          814MiB |
|    0   N/A  N/A      3072      G   /usr/bin/gnome-shell                        158MiB |
|    0   N/A  N/A     24177      G   firefox                                     235MiB |
|    0   N/A  N/A    213795      G   /proc/self/exe                              112MiB |
|    0   N/A  N/A    213796      G   ...erProcess --variations-seed-version       96MiB |
|    0   N/A  N/A    232689      C   python3.10                                 1708MiB |
```
- **2927 G /usr/lib/xorg/Xorg**：814MiB—X11 顯示伺服器（處理圖形桌面；因渲染而占用較多記憶體）。
- **3072 G /usr/bin/gnome-shell**：158MiB—GNOME 桌面環境（UI 效果和視窗管理）。
- **24177 G firefox**：235MiB—Firefox 瀏覽器（用於網頁渲染/影片的 GPU 加速）。
- **213795 G /proc/self/exe**：112MiB—可能是一個瀏覽器渲染器處理程序（在沙盒化應用程式如 Chrome 中常見的自參照路徑）。
- **213796 G ...erProcess --variations-seed-version**：96MiB—可能是一個 Chrome 渲染器子處理程序（省略號隱藏了完整路徑；標誌與功能實驗相關）。
- **232689 C python3.10**：1708MiB—處於計算模式的 Python 3.10 處理程序（這是主要占用—可能是您的 nanoGPT 訓練腳本或使用 PyTorch/CUDA 的 Jupyter 會話；占用了約 1.7GB 視訊記憶體）。

GPU 記憶體總使用量約為 3.1GB，與之前的記憶體使用統計相符。Python 處理程序是此處主要的計算工作負載。

### 快速提示
- 如果您正在 nanoGPT 中訓練模型，請注意高 GPU 使用率（>80%）和記憶體接近 12GB 的情況—如果出現記憶體不足（OOM）錯誤，請考慮調整批次大小。
- 執行 `nvidia-smi -l 1` 可每秒更新即時狀態。
- 要終止處理程序：使用 `kill <PID>`（例如，如果 Python 無回應）。

此快照顯示系統穩定、負載較低，已準備好執行 GPU 任務！
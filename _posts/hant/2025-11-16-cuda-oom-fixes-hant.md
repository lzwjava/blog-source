---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: CUDA記憶體不足錯誤解決方案
translated: true
type: note
---

### 問題分析
nanoGPT 的訓練腳本在初始損失估計（`estimate_loss()`）的前向傳遞過程中，因 CUDA 記憶體不足（OOM）錯誤而失敗。這發生在模型初始化與編譯之後。關鍵問題在於分配模型輸出 logits 的大型緩衝區時記憶體耗盡：

- **緩衝區細節**：形狀為 `(65536, 50304)` 的張量，採用 `bfloat16`（每個元素 2 位元組），約佔 6.14 GiB。這對應於：
  - 批次大小：64
  - 序列長度（block_size）：1024
  - 總 token 數：64 × 1024 = 65,536
  - 詞彙大小：50,304（GPT-2 預設值）
- **GPU 狀態**：您的 GPU（可能是 RTX 3060 或類似型號，具 12 GB VRAM）總容量為 11.69 GiB，但在分配時僅剩 2.68 GiB 可用。程序已使用約 7.04 GiB（其中 PyTorch 佔用 6.78 GiB），在考慮模型（約 1.24 億參數 × bfloat16 的 2 位元組 ≈ 248 MB）、優化器狀態（AdamW 約 1-2 GB）、編譯快取、激活函數與開銷後，剩餘空間不足。

這在消費級 GPU 上使用大型批次大小或序列長度訓練 GPT-2 規模模型（1.24 億參數）時很常見，尤其是啟用 torch.compile 後，其在圖形捕捉與優化期間可能暫時增加記憶體使用量。

### 根本原因
1. **高批次大小（64）**：結合 block_size=1024，產生了巨大的中間張量（例如 logits、注意力輸出）。每次迭代的有效 token 數（65,536）觸及了 VRAM 限制。
2. **模型編譯**：預設啟用的 `torch.compile` 使用 Torch Inductor，其會生成臨時 CUDA 核心與緩衝區。警告 `[0/0] Not enough SMs to use max_autotune_gemm mode` 表明您的 GPU 串流多處理器（SM）數量有限，無法進行積極的自動調優，可能加劇記憶體碎片化。
3. **資料類型與精度**：使用 `bfloat16`（透過 `torch.cuda.amp`），但過時的 `GradScaler` 警告顯示可能存在效率問題。其他程序或先前的運行可能導致了 VRAM 碎片化。
4. **評估開銷**：`estimate_loss()` 在評估資料上執行前向傳遞（eval_iters=200，但已批次化），在訓練開始前加劇了問題。
5. **預先存在的記憶體使用**：約 7 GB 已分配，表明模型、優化器與資料集載入器已預先佔用空間。非 PyTorch 記憶體（程序佔用 224.90 MiB）可能包含 CUDA 上下文或函式庫。

### 建議修復方法
從修改 `config/train_openwebtext.py`（或透過命令列覆寫）中最簡單的更改開始。每次調整後重新運行以隔離有效方法。目標：將峰值 VRAM 降至約 8-9 GB，同時保持訓練品質。

#### 1. **降低批次大小（主要修復）**
   - 設定 `batch_size = 4`（或初始設為 1-2），將 logits 緩衝區降至約 0.38 GiB（批次=4 時）。
   - 透過 `gradient_accumulation_steps = 16` 補償（有效批次=64，但峰值記憶體較低）。
   - **原因**：批次大小與大多數張量的記憶體使用呈線性關係。這是解決 OOM 最有效的方法，且不會過度減慢訓練速度。
   - 更新後的配置片段：
     ```
     batch_size = 4
     gradient_accumulation_steps = 16  # 調整以匹配原始有效批次
     ```
   - 預期 VRAM：總計約 4-6 GB。

#### 2. **停用或優化編譯**
   - 新增 `compile = False` 以跳過 torch.compile，避免 Inductor 開銷（約 1-2 GB 暫時性峰值）。
   - 若保留編譯，新增 `mode='reduce-overhead'` 以使用更快但較少優化的核心。
   - 更新配置：
     ```
     compile = False
     ```
   - **替代方案**：在腳本中執行 `torch._dynamo.config.suppress_errors = True` 進行除錯，但請先修復 OOM。

#### 3. **縮短序列長度**
   - 設定 `block_size = 512`（上下文減半），將每次迭代的 token 數降至約 32,768，logits 記憶體減半（約 3.07 GiB）。
   - 權衡：較短的上下文可能輕微影響模型品質，但可透過更多訓練恢復。
   - 配置：
     ```
     block_size = 512
     ```

#### 4. **記憶體管理調整**
   - **碎片化的環境變數**：如錯誤建議，在運行前設定 `export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True`。這允許 PyTorch 在 CUDA 12+ 上使用可擴展的記憶體區段（減少保留但未使用區塊的浪費）。
   - **手動清除快取**：在 `train.py` 的模型初始化後（約第 100 行）新增 `torch.cuda.empty_cache()`，但這僅是權宜之計。
   - **使用 CPU 卸載**：僅用於評估，修改 `estimate_loss()` 以使用較小批次或將非關鍵部分移至 CPU，但這會減慢速度。
   - **監控 VRAM**：在另一個終端機中執行 `nvidia-smi -l 1` 以即時觀察使用情況。

#### 5. **其他配置調整**
   - 增加 `eval_interval = 1000` 並減少 `eval_iters = 50` 以減輕評估負載（早期減少記憶體波動）。
   - 若為多 GPU 設定，啟用 DDP，但此處似乎為單 GPU。
   - 對於 bfloat16 問題：確保您的 GPU 支援它（Ampere+ 如 RTX 30 系列）。若不支援，在腳本中強制使用 `dtype = 'float16'`。
   - 過時警告修復：在 `train.py` 第 196 行，更改為 `scaler = torch.amp.GradScaler('cuda', enabled=(dtype == 'float16'))`。

#### 6. **硬體/設定檢查**
   - **釋放 VRAM**：終止其他 GPU 程序（使用 `nvidia-smi` 列出 PID，然後 `kill -9 <PID>`）。重新啟動您的終端機/工作階段。
   - **資料集**：確保 `openwebtext_local` 被高效載入；大型資料集可能透過 DataLoader 預載到 RAM/VRAM。
   - **PyTorch/CUDA 版本**：驗證相容性（例如 PyTorch 2.4+ 與 CUDA 12）。若需要，重新安裝：`pip install torch --index-url https://download.pytorch.org/whl/cu121`。
   - **降級至 CPU**：用於測試，新增 `device = 'cpu'` 與 `compile = False`，但預期訓練速度極慢（每迭代小時數，對比 GPU 的秒數）。

### 預期結果
使用 `batch_size=4`、`gradient_accumulation_steps=16` 與 `compile=False`，您應能解決 OOM 並開始訓練。由於梯度累積，max_iters=20,000 的總運行時間將更長，但可透過 `log_interval=100` 監控損失。若仍失敗，進一步降低批次大小並在後期擴增。

若這些方法未解決問題，請分享您的 GPU 型號（`nvidia-smi`）、PyTorch 版本（`torch.__version__`）與更新後的配置/日誌，以獲得更有針對性的建議。
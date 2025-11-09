---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 修復 NumPy 記憶體映射記憶體洩漏問題
translated: true
type: note
---

### Stack Overflow 貼文內容

該貼文討論了處理儲存在磁碟上的大型資料集時，NumPy 的 `np.memmap` 常見問題。原提問者描述透過遍歷一個巨型矩陣（例如透過打亂的索引）以分塊讀取行時，發現即使每行僅被存取一次，RAM 和虛擬記憶體使用量在過程中仍持續增加，導致系統變慢。提問者希望將記憶體使用量限制在當前分塊內，並詢問是否有替代方案，例如基於生成器的迭代或直接檔案 I/O（但註明後者速度較慢）。

被引用的答案（ID 61472122，已採納）指出「記憶體洩漏」問題源於 NumPy 的 memmap 在唯讀模式和單次存取情況下，仍會將整個陣列保留在記憶體中作為快取。該答案提出了兩種解決方案：

1. **為每個分塊重新建立 memmap 物件**：針對每個批次或分塊刪除並重新初始化 `np.memmap`。這可防止整個陣列在 RAM 中累積，保持較低的記憶體使用量（與分塊大小相關）。雖然重新建立會帶來少量 CPU 開銷，但可忽略不計。範例程式碼：
   ```python:disable-run
   def process_chunks(data_filename, chunk_size=4096):
       for start in range(0, total_size, chunk_size):
           # 每次重新建立全新的 memmap
           data = np.memmap(data_filename, dtype=np.float32, mode='r', shape=full_shape)
           # 僅處理當前分塊
           chunk = data[start:start + chunk_size]
           # ... 進行處理 ...
           del data  # 明確丟棄
   ```

2. **使用帶有 OS 記憶體建議的自訂 mmap**：存取 memmap 中的底層 `mmap` 物件，並使用 Python 3.8+ 的 `madvise`（例如 `MADV_DONTNEED` 或 `MADV_DONTDUMP`）來通知作業系統釋放未使用的記憶體分頁。這種方法更為底層，但避免了重新建立的開銷。答案中包含了從 NumPy 原始碼中擷取的存取 mmap 的程式碼片段。

該答案建議使用如 `memory-profiler` 等分析工具來驗證修復效果。

### NanoGPT 採用此方法的原因

在 NanoGPT（一個用於語言模型訓練的精簡 GPT 實現）提供的程式碼中，`get_batch` 函數內部重新建立 `np.memmap` 的做法，正是嚴格遵循了該答案的第一種解決方案——目的是在從大型二進位檔案（例如經過 tokenize 的訓練資料）重複取樣批次時，避免記憶體洩漏問題。

NanoGPT 在龐大的資料集（例如數十億個 token）上進行訓練，因此將整個檔案載入記憶體是不可行的。取而代之的是使用 memmap 進行高效的磁碟存取，但若不進行重新建立，隨著 NumPy 快取愈來愈多的檔案內容，記憶體使用量會在多個訓練週期中不斷膨脹。透過在每個批次重新建立映射（透過 `if split == 'train': data = np.memmap(...)` 這行程式碼），確保了 RAM 使用量保持低位且穩定——這對於在硬體資源有限（例如單一 GPU）的環境下進行長時間訓練至關重要。程式碼註解明確指出此「記憶體洩漏避免技巧」歸功於該 Stack Overflow 貼文。這種做法使資料載入器保持輕量，同時支援對 x/y 輸入-目標對進行隨機取樣（`torch.randint`）。

[Stack Overflow: numpy memmap memory usage - want to iterate once](https://stackoverflow.com/questions/45132940/numpy-memmap-memory-usage-want-to-iterate-once/61472122#61472122)
```
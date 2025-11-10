---
audio: false
generated: true
lang: hant
layout: post
title: Python 3.13 的 CuPy 錯誤
translated: true
type: note
---

### 問題描述

你在執行一個使用 CuPy 函式庫進行 GPU 運算的 Python 指令碼時，遇到了 `AttributeError`。這個錯誤發生在 `import cupy as cp` 語句期間，導致指令碼無法執行。回溯追蹤指向 CuPy 內部程式碼的問題，具體在 `cupy/cuda/device.pyx` 的第 105 行，一個 `memoize` 裝飾器嘗試修改內建函數或方法的 `__name__` 屬性。錯誤訊息如下：

```
AttributeError: attribute '__name__' of 'builtin_function_or_method' objects is not writable
```

這個問題似乎與你使用的 Python 3.13 有關，它可能與你安裝的 CuPy 版本存在相容性問題。

### 錯誤原因

錯誤的產生原因如下：

- **CuPy 的 `memoize` 裝飾器**：CuPy 使用 `memoize` 裝飾器來快取函數結果以優化效能。此裝飾器依賴 Python 的 `functools.update_wrapper` 來將屬性（如 `__name__`）從原始函數複製到包裝函數。
- **內建函數**：在 Python 中，內建函數（以 C 實現）的 `__name__` 屬性是唯讀的。當 `update_wrapper` 嘗試設定此屬性時，會失敗並拋出 `AttributeError`。
- **Python 3.13 相容性**：在 CuPy 的 `device.pyx 中被 memoize 的快取函數很可能是一個內建函數，而 Python 3.13 可能比之前的版本實施了更嚴格的規則或以不同方式處理內建函數，從而暴露了此問題。

由於錯誤發生在導入 CuPy 期間，這是一個與函式庫初始化相關的系統性問題，而非你的指令碼邏輯問題。

### 建議解決方案

最簡單且實用的解決方法是使用已知與 CuPy 相容的較早 Python 版本（例如 Python 3.11 或 3.12）來執行你的指令碼。這樣可以避免 Python 3.13 的相容性問題，而無需修改 CuPy 的原始碼或採用複雜的解決方法。

#### 為何此方法有效

- **相容性**：CuPy 直到最新版本（例如 v11）都在 Python 3.11 和 3.12 等版本上經過測試並獲得支援，在這些版本中不會發生此特定錯誤。
- **無需修改程式碼**：你用於對 GPU 排序進行基準測試的指令碼可以在較早的 Python 環境中按原樣執行，確保了基準測試的完整性。
- **易於實施**：使用虛擬環境或 `conda` 等工具切換 Python 版本非常簡單。

### 逐步解決方法

以下是解決問題的步驟：

#### 選項 1：使用 `virtualenv`

1. **安裝 Python 3.11 或 3.12**
   - 確保系統上安裝了 Python 3.11 或 3.12（例如透過套件管理員或官方 Python 網站）。

2. **建立虛擬環境**
   ```bash
   virtualenv -p python3.11 venv
   ```
   這會建立一個名為 `venv` 的虛擬環境，使用 Python 3.11。如果偏好 Python 3.12，請將 `python3.11` 替換為 `python3.12`。

3. **啟動虛擬環境**
   ```bash
   source venv/bin/activate
   ```

4. **安裝 CuPy**
   ```bash
   pip install cupy
   ```
   這會安裝適用於 Python 3.11 的最新相容版本 CuPy。

5. **執行你的指令碼**
   ```bash
   python scripts/benchmark/cudamark.py
   ```
   你的指令碼現在應該可以執行而不會出現 `AttributeError`。

6. **停用虛擬環境（完成後）**
   ```bash
   deactivate
   ```

#### 選項 2：使用 `conda`

1. **建立 Conda 環境**
   ```bash
   conda create -n cudabench python=3.11
   ```
   這會建立一個名為 `cudabench` 的環境，並使用 Python 3.11。如果偏好 Python 3.12，請使用 `python=3.12`。

2. **啟動環境**
   ```bash
   conda activate cudabench
   ```

3. **安裝 CuPy**
   ```bash
   pip install cupy
   ```

4. **執行你的指令碼**
   ```bash
   python scripts/benchmark/cudamark.py
   ```

5. **停用環境（完成後）**
   ```bash
   conda deactivate
   ```

### 驗證修復

設定環境並執行指令碼後，你應該會看到類似以下的輸出：

```
CPU cores: <your_cpu_cores>
Threads: 1, Time taken: X.XXXX seconds
Threads: 2, Time taken: X.XXXX seconds
...
ThreadCount,TimeTakenSeconds
1,X.XXXXXX
2,X.XXXXXX
...
```

如果指令碼執行時沒有出現 `AttributeError`，則修復成功。

### 補充說明

- **指令碼中的執行緒數量**：你的指令碼遍歷了多個執行緒數量（`1, 2, 4, 8, 16, 32, 64, 128`），但 `parallel_sort_gpu` 函數使用 CuPy 基於 GPU 的排序（`cp.sort`），它並不直接使用 CPU 執行緒。執行緒數量的循環可能不會如預期般影響 GPU 排序效能。如果這是為了未來的修改（例如加入 CPU 多執行緒）而故意為之，則沒有問題；否則，你可能可以簡化基準測試，僅專注於 GPU 效能。
- **CuPy 版本**：如果你懷疑 CuPy 版本過舊，請執行 `pip install cupy --upgrade` 以確保安裝最新版本。然而，這裡的主要問題是 Python 3.13 的相容性，而不僅僅是 CuPy 版本。
- **長期解決方案**：如果你必須使用 Python 3.13，可以考慮查看 CuPy 的 GitHub 儲存庫或問題追蹤器，以獲取支援 Python 3.13 的更新（截至 2025 年 6 月，可能已有支援）。或者，你可以 fork CuPy 並修補 `memoize` 裝飾器以處理內建函數，但這較為複雜，且對於基準測試來說並非必要。

通過使用 Python 3.11 或 3.12，你可以可靠地執行 GPU 基準測試，而不會遇到此錯誤。
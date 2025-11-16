---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 修正數據集分割錯誤
translated: true
type: note
---

錯誤發生的原因是您的本地資料集檔案 (`/home/lzw/projects/nanoGPT/data/openwebtext_local/openwebtext.txt`) 僅包含 1 個樣本（可能只有單行或近乎空白的內容），但腳本嘗試使用 `test_size=0.1` 將其分割為訓練/測試集。這會分配約 0.1 個樣本到測試集（四捨五入為 1 個樣本），並導致訓練集為 0 個樣本，而 `datasets.train_test_split()` 為避免空訓練集而拒絕此操作。

### 快速修復方法
1. **使用更大型/更完整的資料集**：
   - nanoGPT 的 OpenWebText 準備程序預期需要大量文本語料庫（數百萬份文件）。您的本地 `openwebtext.txt` 似乎不完整——可能只是佔位符或下載失敗。
   - 下載適當的 OpenWebText 樣本或子集：
     - 將 OpenWebText 存儲庫克隆到 `data/openwebtext_local/`：`git clone https://github.com/jcpeterson/openwebtext.git`
     - 或使用 Hugging Face 的預處理版本：如果尚未安裝 `datasets`，請先安裝（`pip install datasets`），然後修改 `prepare.py` 透過 `load_dataset("openwebtext", split="train")` 加載，而非使用本地檔案。
     - 用於測試時，在 `openwebtext.txt` 中創建一個虛擬多行檔案，包含至少 10 行以上的樣本文本（例如，重複多次「Hello world.」）以通過分割步驟。

2. **修改 `prepare.py` 中的分割設定**（約第 50 行）：
   - 如果必須使用此小型檔案進行調試，請更改分割參數：
     ```python
     # 原始設定（導致錯誤）：
     split_dataset = dataset.train_test_split(test_size=0.1, seed=2357, shuffle=True)

     # 選項 A：完全跳過分割（無測試集，僅使用全部資料訓練）：
     split_dataset = {"train": dataset}  # 或設定 test_size=0

     # 選項 B：使用適用於 n=1 的較小 test_size（例如 0，或處理極小資料集）：
     if len(dataset) <= 1:
         split_dataset = {"train": dataset}
     else:
         split_dataset = dataset.train_test_split(test_size=0.1, seed=2357, shuffle=True)
     ```
   - 重新運行：`python data/openwebtext_local/prepare.py`

3. **驗證您的資料集大小**：
   - 在 `prepare.py` 的分割步驟前（約第 45 行）添加打印語句：
     ```python
     print(f"Dataset size: {len(dataset)}")
     ```
   - 再次運行以確認——它應輸出 `1`。如果檔案為空或損壞，請重新生成或檢查檔案權限/編碼（預期為 UTF-8）。

### nanoGPT 的建議後續步驟
- 若要進行完整訓練，請遵循 nanoGPT 的官方資料準備說明：參閱 [nanoGPT README](https://github.com/karpathy/nanoGPT#data) 以正確下載/準備 Shakespeare 或 OpenWebText。OpenWebText 需要大量存儲空間（未壓縮時約 40GB）。
- 如果此為本地測試用途，請切換至內建的 Shakespeare 資料集（較小，無需外部下載）：編輯 `prepare.py` 以加載 `load_dataset("tiny_shakespeare")` 或使用 nanoGPT 的 `data/shakespeare_char/prepare.py`。
- 確保依賴項已安裝：`pip install datasets torch`（以及 nanoGPT 的 `requirements.txt` 中的其他套件）。

如果您能提供更多 `prepare.py` 的內容或檔案內容，我可以提供修補版本。
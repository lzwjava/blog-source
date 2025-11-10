---
audio: false
generated: true
image: false
lang: hant
layout: post
title: CuPy Python 3.13 相容性修正
translated: true
type: note
---

該錯誤是由於 `cupy` 與 Python 3.13 之間的兼容性問題所致，具體發生在 `functools.py` 模組中嘗試設定內建函數或方法的 `__name__` 屬性時，而此屬性在 Python 3.13 中不可寫入。間接透過 `srsly` 和 `spacy` 使用的 `cupy` 函式庫導致了此問題。由於您的腳本嘗試使用 `spacy` 和其他依賴項執行翻譯任務，因此錯誤會中斷執行。

以下是解決此問題的逐步方法：

### 1. **理解依賴鏈**
   - 您的腳本 `translate_client.py` 使用 `translate_utils.py`，後者匯入了 `spacy`。
   - `spacy` 依賴於 `thinc`，而 `thinc` 依賴於 `confection`，`confection` 又依賴於 `srsly`。
   - `srsly` 嘗試匯入 `cupy`（一個用於 GPU 加速計算的函式庫），由於與 Python 3.13 不相容而導致錯誤。

### 2. **根本原因**
   - 錯誤發生在 `cupy` 與 Python 3.13 的 `functools.py` 互動時，其中 `setattr` 嘗試修改內建函數的 `__name__` 屬性，而這在 Python 3.13 中不再允許。
   - Python 3.13 引入了對內建物件屬性修改的更嚴格規則，而 `cupy` 尚未完全更新以應對此變更。

### 3. **解決方案**
以下是幾種解決問題的方法，從最直接的方法開始：

#### 選項 1：降級 Python 至 3.12
   - Python 3.13 相對較新（於 2024 年 10 月發布），許多函式庫（包括 `cupy`）可能尚未完全相容。
   - 降級至 Python 3.12，該版本對於 `cupy` 和 `spacy` 等函式庫更穩定。

   **步驟**：
   1. 解除安裝 Python 3.13（如有必要，取決於您的系統）。
   2. 使用您的套件管理器或 `pyenv` 安裝 Python 3.12：
      ```bash
      # 在 Ubuntu/Debian 上
      sudo apt update
      sudo apt install python3.12

      # 或使用 pyenv
      pyenv install 3.12
      pyenv global 3.12
      ```
   3. 重新建立您的虛擬環境（如果使用）：
      ```bash
      python3.12 -m venv venv
      source venv/bin/activate
      ```
   4. 重新安裝依賴項：
      ```bash
      pip install -r requirements.txt
      ```
      或手動安裝所需套件：
      ```bash
      pip install spacy srsly langdetect
      ```
   5. 再次執行您的腳本：
      ```bash
      python scripts/translation/translate_client.py "Hello world" --target zh --model mistral-medium --original-lang en
      ```

#### 選項 2：停用 CuPy 依賴
   - 由於 `cupy` 是透過 `srsly`（經由 `msgpack_numpy`）引入的，而您的翻譯腳本可能不需要 GPU 加速，您可以透過確保 `srsly` 使用基於 CPU 的後端來繞過 `cupy`。
   - `srsly` 嘗試匯入 `cupy` 以進行 NumPy 陣列序列化，但如果 `cupy` 不可用，它應回退到標準的 `msgpack`。

   **步驟**：
   1. 解除安裝 `cupy` 以防止其被使用：
      ```bash
      pip uninstall cupy
      ```
   2. 如果 `srsly` 仍嘗試匯入 `cupy`，您可能需要修改 `srsly` 的行為。一種方法是確保安裝的 `msgpack` 不支援 `cupy`：
      ```bash
      pip install msgpack
      ```
   3. 如果問題仍然存在，請檢查 `srsly` 是否有停用 GPU 支援的選項，或修補 `srsly/msgpack/_msgpack_numpy.py` 中的匯入以跳過 `cupy`。例如，編輯該檔案（例如 `/home/lzw/.local/lib/python3.13/site-packages/srsly/msgpack/_msgpack_numpy.py`）並註解掉 `cupy` 的匯入：
      ```python
      # import cupy
      ```
      將其替換為回退或條件式跳過匯入：
      ```python
      try:
          import cupy
      except ImportError:
          cupy = None
      ```
   4. 再次測試您的腳本。

#### 選項 3：更新或修補 CuPy
   - 檢查是否有支援 Python 3.13 的較新版本 `cupy`。截至 2025 年 8 月，`cupy` 可能已發布修復此問題的版本。
   - 或者，使用解決 Python 3.13 相容性問題的預發布版或開發版 `cupy`。

   **步驟**：
   1. 更新 `cupy`：
      ```bash
      pip install --upgrade cupy
      ```
   2. 如果沒有穩定版本支援 Python 3.13，請嘗試安裝開發版本：
      ```bash
      pip install cupy --pre
      ```
   3. 如果問題仍然存在，請檢查 `cupy` GitHub 儲存庫中是否有針對 Python 3.13 的修補程式或解決方法：
      [CuPy GitHub](https://github.com/cupy/cupy)

#### 選項 4：使用替代翻譯函式庫
   - 如果您的腳本主要目標是翻譯，考慮透過使用不依賴 `cupy` 或 `srsly` 的不同翻譯函式庫來完全繞過 `spacy` 及其依賴項。
   - 例如，使用 Hugging Face 的 `transformers` 或 `googletrans` 進行翻譯任務。

   **步驟**：
   1. 安裝替代函式庫：
      ```bash
      pip install transformers
      ```
   2. 重寫您的腳本以使用 `transformers` 進行翻譯。範例：
      ```python
      from transformers import pipeline

      translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-zh")
      result = translator("Hello world", max_length=40)
      print(result[0]['translation_text'])  # 應列印中文翻譯
      ```
   3. 更新您的腳本，將基於 `spacy` 的語言檢測和翻譯邏輯替換為 `transformers` 或其他函式庫。

#### 選項 5：隔離環境
   - 建立一個乾淨的虛擬環境以隔離依賴項並避免衝突：
      ```bash
      python3 -m venv clean_env
      source clean_env/bin/activate
      pip install spacy langdetect
      ```
   - 除非需要，否則避免安裝不必要的依賴項（如 `cupy`）。

### 4. **推薦方法**
考慮到您的腳本用於翻譯且可能不需要 GPU 加速，**選項 2（停用 CuPy 依賴）** 或 **選項 4（使用替代翻譯函式庫）** 可能是最快的解決方法。如果您需要 `spacy` 執行其他任務，**選項 1（降級 Python 至 3.12）** 是最可靠的，因為 `cupy` 及其依賴項的 Python 3.13 相容性問題可能持續存在。

### 5. **補充說明**
- 確保您的 `requirements.txt` 或依賴項列表明確指定版本，以避免引入不相容的更新。
- 如果您使用特定的 `spacy` 模型（例如用於語言檢測），請確保已安裝：
  ```bash
  python -m spacy download en_core_web_sm
  ```
- 如果 `mistral-medium` 模型是外部 API 或服務（例如 xAI 的 API）的一部分，請驗證其可存取且配置正確。有關 xAI API 的詳細資訊，請參閱：
  [xAI API](https://x.ai/api)

### 6. **測試**
套用上述其中一種解決方案後，重新執行您的腳本：
```bash
python scripts/translation/translate_client.py "Hello world" --target zh --model mistral-medium --original-lang en
```
如果仍然失敗，請分享新的錯誤訊息或 `translate_client.py` 和 `translate_utils.py` 的內容以進行進一步除錯。

如果您需要協助實施任何這些步驟或遇到新的錯誤，請告訴我！
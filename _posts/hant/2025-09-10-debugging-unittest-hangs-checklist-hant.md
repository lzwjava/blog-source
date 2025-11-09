---
audio: false
date: 2025-09-10
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: 除錯單元測試卡住檢查清單
translated: true
type: note
---

在 `unittest` 中出現的程式停滯通常源於死結（執行緒/非同步）、卡住的 I/O 操作、子行程/多行程問題，或是測試正在等待網路呼叫。以下是一份精簡檢查清單，協助您*定位停滯點*並*解決問題*——適用於 Python 3.9–3.11 版本。

### 1) 以詳細模式執行 unittest（並確保正確執行）

```bash
# 若 xx.py 調用 unittest.main()
python xx.py -v

# 或使用探索模式（推薦）
python -m unittest -v
python -m unittest discover -v -s tests -p "test_*.py"
```

> 注意：`python -v` 是**直譯器導入詳細模式**，非測試詳細模式。請使用 `-m unittest -v` 來顯示測試名稱與進度。

### 2) 啟用 faulthandler + 開發者模式（停滯時輸出堆疊轉儲，強化警告提示）

```bash
# 單次執行
python -X faulthandler -X dev -u -m unittest -v
# 或透過環境變數設定
export PYTHONFAULTHANDLER=1
python -X dev -u -m unittest -v
```

* `-X faulthandler` 讓 Python 在收到致命信號或超時時輸出執行緒堆疊追蹤。
* `-X dev` 強化警告與錯誤提示。
* `-u` 取消標準輸出/錯誤的緩衝，即時顯示輸出內容。

### 3) 當程式看似停滯時強制輸出追蹤記錄

選項 A — 從另一個終端機（Linux/macOS）：

```bash
kill -SIGUSR1 <pid>  # 啟用 faulthandler 後，會輸出所有執行緒堆疊
```

選項 B — 在測試啟動程式碼頂部添加（位於 `xx.py` 頂端）：

```python
import faulthandler, signal, sys
faulthandler.enable()
# 收到 SIGUSR1 時輸出堆疊：
faulthandler.register(signal.SIGUSR1, all_threads=True)
# 若停滯超過 120 秒亦自動輸出：
faulthandler.dump_traceback_later(120, repeat=True)
```

### 4) 逐步追蹤執行過程（耗資源但效果明確）

```bash
python -m trace --trace xx.py
# 或
python -m trace --trace -m unittest discover -v
```

您將看到每行執行的程式碼；當輸出「凍結」時，即為停滯發生處。

### 5) 立即使用偵錯工具

```bash
python -m pdb xx.py         # 若 xx.py 調用 unittest.main()
# 在可疑程式碼行設定中斷點：
# (Pdb) b mymodule.py:123
# (Pdb) c
```

對於探索模式執行，請在可疑位置添加 `import pdb; pdb.set_trace()`。

### 6) 常見原因與快速解決方案

* **在 macOS/Windows 上使用多行程**：務必保護測試進入點。

  ```python
  if __name__ == "__main__":
      import unittest
      unittest.main()
  ```

  若在 macOS 的測試中產生行程：

  ```python
  import multiprocessing as mp
  if __name__ == "__main__":
      mp.set_start_method("fork")  # 相較預設 "spawn" 有時可避免停滯
  ```

  （僅在確認程式碼支援 fork 時使用此方法。）

* **執行緒死結**：檢查未設定超時的 `join()`、未釋放的鎖，或背景執行緒等待主執行緒的情況。將：

  ```python
  t.join()
  ```

  替換為：

  ```python
  t.join(timeout=5); assert not t.is_alive()
  ```

* **非同步測試**：確保使用 `IsolatedAsyncioTestCase`（3.8+ 版本）或 `asyncio.run()`。重複的事件循環或遺漏的 `await` 常導致停滯。

* **網路呼叫**：在所有地方加入**短超時設定**：

  ```python
  requests.get(url, timeout=5)
  ```

* **標準輸入等待**：移除 `input()` 或在測試中加以保護；CI/標準輸入可能永久阻塞。

* **Mock 使用不當**：模擬方法未解析 `Future`/promise，或未啟動的模擬伺服器。

### 7) 額外可視化工具

* 若懷疑記憶體洩漏或循環執行，查看記憶體配置：

  ```bash
  python -X tracemalloc=25 -m unittest -v
  ```
* 顯示導入詳細資訊（對停滯問題較少需要）：

  ```bash
  python -v -m unittest -v
  ```

### 8) 若僅在特定 Python 版本發生停滯

* 分別測試兩種版本：

  ```bash
  pyenv local 3.11.9
  python -X faulthandler -X dev -m unittest -v

  pyenv local 3.9.19
  python -X faulthandler -X dev -m unittest -v
  ```

  差異通常出現在 `multiprocessing`、`asyncio` 或 C 擴充套件行為相關部分。

---

若您提供 `faulthandler` 的追蹤記錄（或 `trace --trace` 的最後幾行輸出），我將協助定位確切問題根源並提供針對性解決方案。
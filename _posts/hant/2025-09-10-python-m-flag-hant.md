---
audio: false
date: 2025-09-10
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: 使用 Python 的 -m 標誌執行模組
translated: true
type: note
---

是的，`-m` 表示**將模組作為腳本執行**。讓我們透過你的範例來詳細說明：

### `python -m unittest`

這行指令告訴 Python：

* 查找 `unittest` 模組（屬於標準函式庫的一部分）
* 將其作為腳本執行（這就是 `-m` 的作用）
* 因此你可以這樣操作：

  ```bash
  python -m unittest test_example.py
  python -m unittest discover
  ```

  即使你的專案中沒有獨立的 `unittest` 檔案，這依然能正常運作——因為它屬於標準函式庫模組。

### `python -m pip`

這是相同的模式：

* 查找已安裝的 `pip` 模組
* 將其當作 `pip` 可執行檔來運行
* 所以 `python -m pip install requests` 是「官方推薦」的安全執行方式，因為它能確保你使用的 pip 與當前 `python` 直譯器相匹配
  （有時系統中的 `pip` 可能指向不同的 Python 安裝版本，使用 `python -m pip` 可避免混淆）

### 與 `python test_xx.py` 的區別

當你執行：

```bash
python test_xx.py
```

你是在直接運行特定檔案，而非使用 `unittest` 的測試探索功能或執行器。

* 如果 `test_xx.py` 底部包含 `unittest.main()`，則會執行測試
* 但若想要 Python 自動探索目錄下的所有測試，通常需依賴 `python -m unittest discover`

---

✅ **重點整理**：

* `-m` = 將模組作為腳本執行
* `python -m unittest` 執行標準函式庫的測試執行器
* `python -m pip` 確保 pip 與當前 Python 直譯器相對應
* `python test_xx.py` 僅執行單一檔案，不啟動通用測試執行器

需要我進一步說明 **pytest** 的差異化處理方式嗎？畢竟你可能會比較 `unittest` 與 `pytest` 的差異？
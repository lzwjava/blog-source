---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 專案目錄結構最佳實踐
translated: true
type: note
---

好問題。

一般約定是：

* **`scripts/`** 用於存放應用程式代碼（需要在生產環境或項目中運行的內容）。
* **`tests/`** 用於存放測試代碼（用於驗證腳本/模組正確性的內容）。

所以如果你要新增測試檔案，通常應該放在 **`tests/llm/`** 目錄下，而非 `scripts/`。

例如：

```
scripts/
  llm/
    main.py
    utils.py
tests/
  llm/
    test_main.py
    test_utils.py
```

這樣你的測試代碼就能與實現代碼分離，而像 `pytest` 這樣的工具也能輕鬆發現它們。

👉 你現在可以新增類似這樣的內容：

```python
# tests/llm/test_basic.py
import pytest
from scripts.llm import utils

def test_addition():
    assert utils.add(2, 3) == 5
```

然後執行：

```bash
pytest tests/llm/
```

需要我同時示範如何設置 `conftest.py`，讓你能在 `tests/llm/` 檔案間共享 fixtures 嗎？
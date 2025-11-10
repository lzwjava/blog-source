---
audio: false
generated: true
image: false
lang: hant
layout: post
title: PyCharm 安全智能檔案重新命名
translated: true
type: note
---

是的——如果你使用 **PyCharm 的重構功能**（在檔案上右鍵 → Refactor → Rename，或直接對檔案名稱按下 `Shift+F6`），它不僅會重新命名磁碟上的檔案，還會更新專案內所有指向該檔案的**引用和導入語句**，只要這些引用在專案內可被解析。

有幾個重要細節需要注意：

* **重構範圍**：PyCharm 會分析整個專案，因此專案內其他 Python 檔案中的導入語句都會自動更新。
* **未解析/動態導入**：如果某些導入是動態建構的（例如使用 `__import__`、`importlib` 或基於字串的模組路徑），PyCharm 將無法檢測到這些情況，因此不會更新它們。
* **多根目錄/外部腳本**：如果其他腳本位於 PyCharm 專案外部或未被索引（例如不在專案源根目錄中），PyCharm 也無法捕捉這些引用。
* **測試與相對導入**：如果你使用相對導入（`from . import something`）且資料夾結構發生變化，可能需要單獨檢查這些部分。

因此，對於專案內常規的 `import mymodule.something` 情況，使用 PyCharm 重構進行重新命名將保持所有內容的一致性。

需要我進一步說明**如何在重新命名後安全測試**以確保沒有破壞任何功能嗎？
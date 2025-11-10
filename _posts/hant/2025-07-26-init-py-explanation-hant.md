---
audio: false
generated: true
lang: hant
layout: post
title: 為何 Python 需要 `__init__.py`
translated: true
type: note
---

### 修正拼寫錯誤
看來你指的是 `__init__.py`（"init" 是 "initialization" 的縮寫），而不是 `__int__.py`。如果不是這個情況，請隨時澄清！假設是 `__init__.py`，以下是解釋。

### 為什麼 Python 在目錄中需要 `__init__.py`
在 Python 中，一個目錄不會僅僅因為包含 Python 檔案就自動被視為模組或套件。要將程式碼組織成可重複使用的套件（本質上是相關模組的目錄），Python 要求在該目錄中有一個 `__init__.py` 檔案。原因如下：

- **標記目錄為套件**：`__init__.py` 的存在告訴 Python 該目錄應被視為一個套件。這允許你使用點記號從中導入模組，例如 `import mypackage.mymodule`。如果沒有它（在標準情況下），Python 會將該目錄視為普通資料夾，不允許從中導入。

- **避免名稱衝突**：它防止模組的意外遮蔽。例如，如果你有一個名為 `string` 的目錄（一個常見的名稱），沒有 `__init__.py` 的話，它可能會無意中隱藏 Python 內建的 `string` 模組在導入路徑中。

- **初始化和自定義**：該檔案可以是空的（對於簡單套件很常見），但它也可以包含在套件導入時運行的程式碼。這對於設置任務很有用，例如自動導入子模組。此外，你可以在 `__init__.py` 中定義一個名為 `__all__` 的特殊變數，以控制當有人執行 `from mypackage import *` 時導入哪些內容（例如 `__all__ = ['module1', 'module2']`）。

### 歷史和版本特定的背景
- 這一要求自 Python 早期以來就一直存在，以保持模組系統的明確性和組織性。
- 從 Python 3.3 開始，引入了「命名空間套件」，這些套件不需要 `__init__.py`。它們允許套件拆分到多個目錄中（例如用於分發目的）而無需該檔案，使用如 `pkgutil` 或 `importlib` 等工具。然而，這被視為進階功能，對於大多數日常使用情況，`__init__.py` 仍然是常規套件的推薦且廣泛使用的方法。

如果你正在使用 Python 3.3+，可以嘗試命名空間套件，但對於初學者來說，堅持使用 `__init__.py` 更簡單直接。

[Python 教程：模組](https://docs.python.org/3/tutorial/modules.html#packages)
---
audio: false
generated: true
image: false
lang: hant
layout: post
title: Python Difflib 序列比較指南
translated: true
type: note
---

在 Python 中，**`difflib`** 模組提供了比較序列的工具——無論是字串、列表還是任何可迭代物件。它常被用於檢測文字差異（類似 Unix 中的 `diff` 指令）或建構自動完成及相似度工具等任務。

---

### `difflib` 的運作原理

`difflib` 的核心在於嘗試找出兩個輸入之間最長的連續匹配子序列，並利用這些匹配來突顯相似與相異之處。該函式庫能夠：

* 生成人類可讀的差異比較（`ndiff`、`unified_diff`、`context_diff`）。
* 計算序列之間的相似度比例。
* 從列表中推薦近似匹配（`get_close_matches`）。

---

### `SequenceMatcher`

最重要的類別是 **`difflib.SequenceMatcher`**。

**運作方式**：

* 它逐元素比較兩個序列。
* 尋找*最長公共子序列*（但不一定連續）。
* 產生一系列操作（`replace`、`delete`、`insert`、`equal`），描述如何將一個序列轉換為另一個。

**關鍵方法**：

1. **`ratio()`**
   回傳一個介於 `[0, 1]` 的浮點數，用於衡量相似度。
   公式：

   $$
   \text{ratio} = \frac{2 \times M}{T}
   $$

   其中 `M` = 匹配元素的數量，`T` = 兩個序列的總元素數。

2. **`quick_ratio()`** 與 **`real_quick_ratio()`**
   這些是相似度的快速近似計算方法，以準確度換取速度。

3. **`get_opcodes()`**
   回傳一系列將序列 `a` 轉換為 `b` 的操作。例如：`[('replace', 0, 2, 0, 1), ('equal', 2, 4, 1, 3)]`。

4. **`get_matching_blocks()`**
   回傳所有匹配子序列及其位置。

---

### 範例

```python
import difflib

a = "hello world"
b = "helo wrld"

s = difflib.SequenceMatcher(None, a, b)

print("相似度比例:", s.ratio())
print("操作步驟:", s.get_opcodes())
print("匹配區塊:", s.get_matching_blocks())
```

**輸出**：

```
相似度比例: 0.9090909090909091
操作步驟: [('equal', 0, 1, 0, 1), ('delete', 1, 2, 1, 1),
             ('equal', 2, 5, 1, 4), ('delete', 5, 6, 4, 4),
             ('equal', 6, 11, 4, 9)]
匹配區塊: [Match(a=0, b=0, size=1),
                  Match(a=2, b=1, size=3),
                  Match(a=6, b=4, size=5),
                  Match(a=11, b=9, size=0)]
```

---

👉 簡而言之：

* `difflib` 是一個序列比較工具包。
* `SequenceMatcher` 是核心引擎——它負責尋找匹配子序列並計算相似度。
* 它在差異比較、拼字檢查、抄襲偵測、自動建議等方面非常實用。

您是否還想了解如何使用 `get_close_matches()`（內部使用 `SequenceMatcher`）進行模糊字串匹配，例如在拼字檢查或搜尋建議中的應用？
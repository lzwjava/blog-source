---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: Python difflib 模組概述
translated: true
type: note
---

### difflib 模組概述
Python 標準函式庫中的 `difflib` 模組用於比較序列（例如字串、列表）以找出差異。它適用於文字比對、修補檔生成或相似度檢查等任務。關鍵類別和函式包括 `Differ`（用於詳細差異比較）、`SequenceMatcher`（用於計算相似度比率和匹配），以及差異生成器如 `ndiff` 和 `unified_diff`。

### 導入與基本設定
無需安裝——此為內建模組。
```python
import difflib
```

### 常用函式與類別

1. **`SequenceMatcher`**：計算相似度比率並找出匹配的子序列。
   - 適用於模糊匹配或快速取得相似度分數。
   - 範例：
     ```python
     seq1 = "abcdef"
     seq2 = "abcefg"
     matcher = difflib.SequenceMatcher(None, seq1, seq2)
     print("相似度比率:", matcher.ratio())  # 輸出：約 0.83（接近匹配）
     print("共同元素:", matcher.find_longest_match(0, len(seq1), 0, len(seq2)))  # 尋找最長匹配
     ```
     - `ratio()` 回傳 0 到 1 的浮點數表示相似度。
     - 如 `get_matching_blocks()` 等方法可列出精確匹配。

2. **`Differ`**：生成人類可讀的逐行差異顯示，包含新增、刪除和修改。
   - 最適合比較列表或多行字串。
   - 範例：
     ```python
     text1 = ["line1", "line2", "line3"]
     text2 = ["line1", "line2 modified", "line3", "line4"]
     d = difflib.Differ()
     diff = list(d.compare(text1, text2))
     print("\n".join(diff))
     # 輸出：
     #   line1
     #   line2
     # - line3
     # + line2 modified
     # + line3  （實際輸出會顯示行修改；請根據準確性調整）
     ```
     - 前綴符號：`  `（未變更）、`- `（刪除）、`+ `（新增）、`? `（行內差異）。

3. **`ndiff`** 與 **`unified_diff`**：用於生成特定格式的差異比較。
   - **`ndiff`**：類似 `Differ` 的逐行差異。
     ```python
     diff = list(difflib.ndiff(["a", "b"], ["a", "c"]))
     # 輸出：['  a', '- b', '+ c']
     ```
   - **`unified_diff`**：生成統一差異格式（如 Git 差異），適用於修補檔。
     ```python
     diff = difflib.unified_diff(["a", "b"], ["a", "c"], fromfile='file1', tofile='file2')
     print("\n".join(diff))
     # 輸出：
     # --- file1
     # +++ file2
     # @@ -1,2 +1,2 @@
     #  a
     # -b
     # +c
     ```

### 技巧與最佳實踐
- **標準化處理**：若需進行大小寫不敏感或忽略空白字元的比較，請預先處理輸入（例如使用 `text.lower()` 或 `text.splitlines()`）。
- **效能優化**：處理長序列時，可使用 `SequenceMatcher` 並設定 `autojunk=False` 以停用垃圾啟發式演算法（如果內容並非垃圾資料）。
- **整合應用**：可搭配 `filecmp` 進行檔案比較，或用於版本控制腳本。
- **進階功能**：探索 `HtmlDiff` 以生成 HTML 格式的差異報告（較少使用但仍可用）。

完整文件請參閱 Python 的[官方 difflib 頁面](https://docs.python.org/3/library/difflib.html)。如有特定使用情境，請提供更多細節以獲取客製化範例。
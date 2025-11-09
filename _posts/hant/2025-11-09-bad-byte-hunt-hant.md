---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 追捕壞字節
translated: true
type: note
---

### 為何未能找出錯誤位元組
你取得的 `hexdump` 輸出匹配的是**檔案偏移量**（`000008d0`），而非實際內容中的 `\x8D` 位元組。Grep 是對整行文字進行搜尋，而「8d」出現在十六進位位址中（例如 `08d0`），因此它提取了這行不相關的內容。該處的資料位元組（`6f 67 20 ...`）只是普通的 ASCII 字元，對應 `"og = og_images[i"`，並無問題。

### 更好的方法來尋找 `\x8D`
請在你的專案目錄中（`_layouts/default.html` 旁邊）嘗試以下指令。它們會直接掃描檔案的位元組。

1. **改進的 Hexdump（在資料中搜尋位元組）**：
   此指令搜尋 ` 8d `（前後加上空格以匹配十六進位位元組，而非偏移量）：
   ```
   hexdump -C _layouts/default.html | grep ' 8d '
   ```
   - 如果找到匹配，你會看到偏移量（左側欄位）及周圍的位元組。記下偏移量，然後在編輯器中跳轉到該位置（例如，VS Code：Ctrl+G > 位元組偏移量 / 16 以取得大致行數）。
   - 若命中時的範例輸出：`00001234  ...  8d  20  61  62  ... |... ab...|`

2. **使用 `xxd`（通常比 Hexdump 更好）**：
   macOS 內建 `xxd`：
   ```
   xxd _layouts/default.html | grep 8d
   ```
   - 類似：匹配十六進位位元組中的「8d」。如果沒有輸出，表示該位元組不存在（較罕見，但若位元組位於其他檔案中則可能發生）。

3. **二進位 Grep（直接位元組搜尋）**：
   ```
   grep -a -o -P '\x8d' _layouts/default.html | hexdump -C
   ```
   - 此指令提取與位元組完全匹配的內容並以十六進位形式顯示。如果為空，則表示沒有 `\x8D`。

4. **Ruby 單行指令（精確定位）**：
   如同我之前建議的——執行此指令以取得位元組索引：
   ```
   ruby -e "File.open('_layouts/default.html', 'rb') { |f| f.read.each_byte.with_index { |b, i| puts \"Found at byte #{i}: #{b.chr(Encoding::ASCII_8BIT).inspect}\" if b == 0x8D } }"
   ```
   - 輸出範例：`Found at byte 1234: "\x8D"`。然後進行編輯：開啟檔案，跳轉至大約第 1234 個字元（或行數約為 1234/80），並刪除該隱藏字元（它可能看起來像空無一物；選取並刪除其周圍內容）。

### 如果沒有匹配？
- `\x8D` 可能位於**其他檔案**中（例如，透過佈局中的 `{{ content }}` 渲染的 `_posts/` 目錄下的文章）。掃描整個網站：
  ```
  find . -name "*.md" -o -name "*.html" | xargs grep -l $'\x8D'
  ```
  （或對每個可疑檔案使用 Ruby 腳本。）
- 或者它是檔案開頭的 BOM/隱藏字元：在編輯器中開啟，刪除首行（如果為空），並重新儲存為 UTF-8。

一旦你將其刪除，再次執行 `bundle exec jekyll serve --incremental`。如果問題仍然存在，請貼上其中一個指令（或 Ruby 指令）的輸出，我們將徹底解決它。

[用於位元組搜尋的 Hexdump 技巧](https://unix.stackexchange.com/questions/38331/finding-bad-characters-in-hex-dump)
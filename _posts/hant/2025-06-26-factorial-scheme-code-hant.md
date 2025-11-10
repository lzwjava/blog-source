---
audio: false
generated: true
lang: hant
layout: post
title: Chez Scheme 階乘程式
translated: true
type: note
---

這是一個簡單的 Chez Scheme 程式，用於計算數字的階乘。請將其儲存為 `factorial.scm`：

```scheme
(define (factorial n)
  (if (<= n 1)
      1
      (* n (factorial (- n 1)))))

(display "5 的階乘是：")
(display (factorial 5))
(newline)
```

執行方法：
1. 將程式碼儲存至名為 `factorial.scm` 的檔案中
2. 在終端機中切換至包含該檔案的目錄
3. 執行：`scheme --script factorial.scm`

將會輸出：
```
5 的階乘是：120
```

此程式定義了一個遞迴的 `factorial` 函數，並計算 5 的階乘。如 `scheme --help` 輸出所示，`--script` 選項可讓您直接執行檔案。
---
audio: false
generated: true
lang: hant
layout: post
title: Scheme 程式設計教程
translated: true
type: note
---

Scheme 是 Lisp 的極簡主義方言，以其簡潔優雅著稱。本教程將涵蓋基礎知識，助你入門。

## 1. 基本語法與概念

### 執行 Scheme
- 你需要一個 Scheme 直譯器（如 Racket、Guile 或 Chez Scheme）
- 程式碼通常寫在 `.scm` 檔案中，或在 REPL（讀取-求值-輸出循環）中輸入

### 表達式與括號
- Scheme 中的所有內容都是會返回值的表達式
- 括號用於函數呼叫和分組
- 格式：`(函數 參數1 參數2 ...)`

## 2. 基本資料類型

```scheme
; 數字
42          ; 整數
3.14        ; 浮點數
1/2         ; 有理數

; 布林值
#t          ; 真
#f         ; 假

; 字串
"hello"     ; 字串字面值

; 符號
'hello      ; 符號（用 ' 引號表示）
```

## 3. 基本運算

```scheme
; 算術運算
(+ 2 3)        ; 5
(- 10 4)       ; 6
(* 3 4)        ; 12
(/ 15 3)       ; 5

; 比較運算
(= 5 5)        ; #t
(< 3 7)        ; #t
(> 10 5)       ; #t
```

## 4. 定義變數

```scheme
; 定義全域變數
(define x 10)

; 使用變數
(+ x 5)        ; 15
```

## 5. 函數

### 定義函數
```scheme
; 基本函數定義
(define square
  (lambda (x)    ; lambda 建立匿名函數
    (* x x)))

(square 4)     ; 16
```

### 多個參數
```scheme
(define add
  (lambda (x y)
    (+ x y)))

(add 3 5)      ; 8
```

### 簡寫定義
```scheme
; 替代語法（語法糖）
(define (multiply x y)
  (* x y))

(multiply 2 3) ; 6
```

## 6. 條件語句

### If 語句
```scheme
(define (is-positive? n)
  (if (> n 0)
      #t
      #f))

(is-positive? 5)   ; #t
(is-positive? -2)  ; #f
```

### Cond（多重條件）
```scheme
(define (number-type n)
  (cond
    ((> n 0) "正數")
    ((< n 0) "負數")
    (else "零")))

(number-type 5)    ; "正數"
(number-type 0)    ; "零"
```

## 7. 列表

### 建立列表
```scheme
; 使用 quote
'(1 2 3)          ; 數字列表

; 使用 list 函數
(list 1 2 3)      ; 同上

; 使用 cons（建構）
(cons 1 '(2 3))   ; 同上
```

### 列表操作
```scheme
(car '(1 2 3))    ; 1（首個元素）
(cdr '(1 2 3))    ; (2 3)（列表其餘部分）
(null? '())       ; #t（檢查是否為空）
(length '(1 2 3)) ; 3
```

## 8. 遞迴

### 簡單遞迴
```scheme
(define (factorial n)
  (if (= n 0)
      1
      (* n (factorial (- n 1)))))

(factorial 5)     ; 120 (5 * 4 * 3 * 2 * 1)
```

### 列表遞迴
```scheme
(define (sum-list lst)
  (if (null? lst)
      0
      (+ (car lst) (sum-list (cdr lst)))))

(sum-list '(1 2 3 4))  ; 10
```

## 9. 高階函數

### 映射
```scheme
(map square '(1 2 3 4))    ; (1 4 9 16)
(map + '(1 2 3) '(4 5 6))  ; (5 7 9)
```

### 過濾
```scheme
(define (even? n) (= (remainder n 2) 0))
(filter even? '(1 2 3 4 5 6))  ; (2 4 6)
```

## 10. Let 綁定

```scheme
; 區域變數綁定
(define (circle-area r)
  (let ((pi 3.14159))
    (* pi (square r))))

(circle-area 2)    ; 12.56636
```

## 11. 輸入/輸出

```scheme
; 顯示輸出
(display "Hello, Scheme!")
(newline)

; 讀取輸入（實現方式可能不同）
(define name (read))
(display "Hello, ")
(display name)
```

## 12. 範例程式

以下是一個結合多個概念的完整程式：

```scheme
; 計算數字列表平均值的程式
(define (average lst)
  (define (sum lst)
    (if (null? lst)
        0
        (+ (car lst) (sum (cdr lst)))))
  (define len (length lst))
  (if (= len 0)
      0
      (/ (sum lst) len)))

; 測試程式
(display (average '(1 2 3 4 5)))  ; 3
(newline)
(display (average '()))           ; 0
```

## Scheme 的主要特性

1. **極簡主義**：核心語言小巧但功能強大
2. **函數式**：強調純函數和不可變性
3. **前綴表示法**：所有運算使用前綴語法
4. **一級函數**：函數可作為參數傳遞
5. **尾遞迴優化**：高效的遞迴處理

## 學習技巧

1. 在 REPL 中練習以查看即時結果
2. 從簡單函數開始，逐步增加複雜度
3. 處理列表時採用遞迴思維
4. 使用適當縮排來管理括號
5. 嘗試使用高階函數

本教程涵蓋了 Scheme 的核心概念。要深入理解，請嘗試：
- 編寫更複雜的遞迴函數
- 探索宏系統（進階主題）
- 建構小型專案，如計算器或列表處理器
- 研究 Scheme 的標準函式庫（因實現而異）

需要我詳細說明任何特定部分或提供更多範例嗎？
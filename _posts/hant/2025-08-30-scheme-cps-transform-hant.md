---
audio: false
generated: true
image: false
lang: hant
layout: post
title: Scheme CPS 轉換程式碼解析
translated: true
type: note
---

```scheme
(define cps
  (lambda (exp)
    (letrec
        ([trivial? (lambda (x) (memq x '(zero? add1 sub1)))]
         [id (lambda (v) v)]
         [ctx0 (lambda (v) `(k ,v))]   ; 尾端上下文
         [fv (let ([n -1])
               (lambda ()
                 (set! n (+ 1 n))
                 (string->symbol (string-append "v" (number->string n)))))]
         [cps1
          (lambda (exp ctx)
            (pmatch exp
              [,x (guard (not (pair? x))) (ctx x)]
              [(if ,test ,conseq ,alt)
               (cps1 test
                     (lambda (t)
                       (cond
                         [(memq ctx (list ctx0 id))
                          `(if ,t ,(cps1 conseq ctx) ,(cps1 alt ctx))]
                         [else
                          (let ([u (fv)])
                            `(let ([k (lambda (,u) ,(ctx u))])
                               (if ,t ,(cps1 conseq ctx0) ,(cps1 alt ctx0))))])))]
              [(lambda (,x) ,body)
               (ctx `(lambda (,x ,k) ,(cps1 body ctx0)))]
              [(,op ,a ,b)
               (cps1 a
                     (lambda (v1)
                       (cps1 b
                             (lambda (v2)
                               (ctx `(,op ,v1 ,v2))))))]
              [(,rator ,rand)
               (cps1 rator
                     (lambda (r)
                       (cps1 rand
                             (lambda (d)
                               (cond
                                 [(trivial? r) (ctx `(,r ,d))]
                                 [(eq? ctx ctx0) `(,r ,d ,k)] ; 尾端呼叫
                                 [else
                                  (let ([u (fv)])
                                    `(,r ,d (lambda (,u) ,(ctx u))))]))))))]))]
      (cps1 exp id))))
```

---

## 程式功能說明

這是一個針對小型 Scheme 類語言的**續體傳遞風格（CPS）轉換器**實作。CPS 是一種重寫程式的方法，通過傳遞*續體函數*來顯式化控制流程。

### 核心組件

1. **簡單操作**

   ```scheme
   (trivial? (lambda (x) (memq x '(zero? add1 sub1))))
   ```

   將某些基本運算符標記為簡單操作（無需 CPS 包裝）。

2. **續體上下文**

   ```scheme
   [id (lambda (v) v)]      ; 恆等上下文
   [ctx0 (lambda (v) `(k ,v))] ; 預設尾端續體
   ```

   `id` 直接返回參數，而 `ctx0` 表示「將值返回給續體 `k`」。

3. **新穎變數**

   ```scheme
   [fv ...] ; 產生符號 v0, v1, v2, ...
   ```

   在需要新綁定時使用。

4. **主要轉換器**

   ```scheme
   cps1
   ```

   這個函數透過遞迴方式，逐個案例將表達式轉換為 CPS 形式。

   * **變數與常數**
     若 `x` 非配對類型（原子性），直接應用續體上下文。

   * **條件語句**

     ```scheme
     (if test conseq alt)
     ```

     先對測試條件進行 CPS 轉換。
     若上下文簡單（`ctx0` 或 `id`），產生直接的 `if` 語句。
     否則，生成新的續體 `k` 並用 `ctx0` 對兩個分支進行 CPS 處理。

   * **Lambda 表達式**

     ```scheme
     (lambda (x) body)
     ```

     轉換為 `(lambda (x k) <body 的 CPS 形式>)`，即 lambda 現在顯式接受續體參數。

   * **二元運算**

     ```scheme
     (op a b)
     ```

     對兩個運算元進行 CPS 處理後組合。

   * **函數應用**

     ```scheme
     (rator rand)
     ```

     對運算符與運算元進行 CPS 處理。根據簡單性區分：

     * 若運算符是基本操作，直接應用。
     * 若處於尾端位置（`ctx = ctx0`），直接呼叫 `(r d k)`。
     * 否則，用新續體進行包裝。

5. **進入點**

   ```scheme
   (cps exp)
   ```

   以 `id` 作為初始上下文呼叫 `cps1`。

---

## 範例說明

假設對以下程式進行 CPS 轉換：

```scheme
((lambda (x) (add1 x)) 5)
```

CPS 轉換會將其改寫為類似：

```scheme
((lambda (x k)
   (k (add1 x)))
 5
 k)
```

其中 `k` 是處理結果的續體。函數不再返回值，而是透過呼叫 `k` 來傳遞結果。

---

## 程式檢視

* **優點**

  * 實作了所有核心 CPS 轉換規則：變數、條件語句、lambda 表達式、函數應用。
  * 正確區分基本運算符與高階呼叫。
  * 特別處理尾端呼叫（對 Scheme 語義至關重要）。
  * 使用衛生型新穎變數生成（`fv`）。

* **潛在問題**

  * 支援的基本操作有限（`zero?`, `add1`, `sub1`）——需要擴展 `trivial?` 以支援更豐富的語言。
  * 使用 `pmatch`（模式匹配器）——需要依賴宏庫支援。
  * 新穎變數生成器（`fv`）會改變全域 `n`——適合小型實驗，但在並行或模組化使用時不安全。
  * 不支援多參數 lambda（僅限單參數）。
  * 不支援 let 綁定或函數應用之外的序列操作。

---

✅ 總結：這是針對教學用 Scheme 子集的一個簡潔*教育性實作*。它清晰展示了續體傳遞的機制：添加 `k` 參數、包裝分支語句，以及顯式化控制流程。

---

是否需要我**逐步演示具體範例**（例如展示 `(if (zero? x) (add1 y) (sub1 y))` 的逐步 CPS 轉換過程）？這樣您就能清楚看到此程式碼的實際轉換過程。
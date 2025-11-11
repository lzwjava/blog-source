---
audio: false
generated: true
lang: hant
layout: post
title: CPS變壓器
translated: true
type: note
---

```scheme
;; 一個簡單的CPS轉換器，能處理正確的尾呼叫，且不會為if表達式複製上下文。
;; 作者：Yin Wang (yw21@cs.indiana.edu)
(load "pmatch.scm") ; 載入Scheme的模式匹配函式庫，方便處理不同表達式結構。

(define cps
  (lambda (exp)
    (letrec
        ([trivial? (lambda (x) (memq x '(zero? add1 sub1)))] ; 檢查給定符號是否為原始運算子：zero?、add1、sub1。這些在轉換中會特殊處理。
         [id (lambda (v) v)] ; 恆等函數，作為頂層表達式的初始續體。
         [ctx0 (lambda (v) `(k ,v))]      ; 尾上下文。建立一個續體，僅將當前續體'k'應用於值'v'。用於當前呼叫處於尾位置時。
         [fv (let ([n -1]) ; 建立新鮮變數名稱的產生器。
               (lambda ()
                 (set! n (+ 1 n))
                 (string->symbol (string-append "v" (number->string n)))))]
         [cps1
          (lambda (exp ctx) ; 執行CPS轉換的核心遞迴函數。接受表達式'exp'和續體'ctx'作為參數。續體代表如何處理'exp'的求值結果。
            (pmatch exp ; 使用模式匹配分析表達式結構。
              [,x (guard (not (pair? x))) (ctx x)] ; 基本情況：若表達式'x'不是序對（即為字面值或變數），表示它已是值。將當前續體'ctx'應用於此值。

              [(if ,test ,conseq ,alt) ; 匹配帶有測試、結果和替代項的'if'表達式。
               (cps1 test ; 遞迴轉換'test'表達式。
                     (lambda (t) ; 'test'表達式的續體。以't'接收測試結果（布林值）。
                       (cond
                        [(memq ctx (list ctx0 id)) ; 若當前上下文'ctx'是尾上下文'ctx0'或初始恆等上下文'id'，表示'if'表達式本身處於尾位置。
                         `(if ,t ,(cps1 conseq ctx) ,(cps1 alt ctx))] ; 此情況下，'if'表達式在CPS化程式碼中仍保持'if'結構。結果項和替代項以相同上下文'ctx'進行CPS轉換，避免重複上下文。
                        [else ; 若當前上下文非尾上下文，表示'if'表達式的結果需傳遞給後續計算。
                         (let ([u (fv)]) ; 產生新鮮變數名稱'u'來保存'if'表達式的結果。
                           `(let ([k (lambda (,u) ,(ctx u))]) ; 建立新續體'k'，接收結果'u'並對其應用原始上下文'ctx'。
                              (if ,t ,(cps1 conseq ctx0) ,(cps1 alt ctx0))))])))] ; 用'let'包裹'if'表達式引入新續體'k'。結果項和替代項以尾上下文'ctx0'進行CPS轉換，因其結果將立即傳遞給'k'。

              [(lambda (,x) ,body) ; 匹配帶單一參數'x'和主體的lambda表達式。
               (ctx `(lambda (,x k) ,(cps1 body ctx0)))] ; lambda表達式轉換為接受額外參數'k'（續體）的新lambda表達式。原始lambda的主體以尾上下文'ctx0'進行CPS轉換，因其結果將傳遞給此續體'k'。

              [(,op ,a ,b) ; 匹配帶二元運算子'op'和兩個運算元'a'、'b'的表達式。
               (cps1 a ; 遞迴轉換第一個運算元'a'。
                     (lambda (v1) ; 'a'的續體。接收結果'v1'。
                       (cps1 b ; 遞迴轉換第二個運算元'b'。
                             (lambda (v2) ; 'b'的續體。接收結果'v2'。
                                   (ctx `(,op ,v1 ,v2))))))] ; 對由運算子'op'與CPS化後的運算元結果'v1'、'v2'組成的表達式應用原始上下文'ctx'。

              [(,rator ,rand) ; 匹配帶有運算元（函數）和運算元（參數）的函數應用。
               (cps1 rator ; 遞迴轉換運算元。
                     (lambda (r) ; 運算元的續體。接收結果'r'（函數）。
                       (cps1 rand ; 遞迴轉換運算元。
                             (lambda (d) ; 運算元的續體。接收結果'd'（參數）。
                               (cond
                                [(trivial? r) (ctx `(,r ,d))] ; 若運算元'r'是簡單運算子（如zero?、add1、sub1），將當前上下文'ctx'應用於運算子對運算元的應用結果。
                                [(eq? ctx ctx0) `(,r ,d k)]  ; 尾呼叫。若當前上下文是尾上下文'ctx0'，表示此函數應用處於尾位置。CPS化後的函數'r'以CPS化後的參數'd'和當前續體'k'呼叫。
                                [else ; 若函數應用不處於尾位置。
                                 (let ([u (fv)]) ; 產生新鮮變數名稱'u'存放結果。
                                   `(,r ,d (lambda (,u) ,(ctx u))))])))))]))]) ; CPS化後的函數'r'以CPS化後的參數'd'和新續體呼叫，該續體接收結果'u'並對其應用原始上下文'ctx'。

      (cps1 exp id))));; 以輸入表達式'exp'和初始恆等續體'id'呼叫'cps1'，啟動CPS轉換。

;;; 測試
;; 變數
(cps 'x) ; 轉換變數'x'。結果將是'(k x)'，因為初始上下文是'id'，而'id'應用於'x'。

(cps '(lambda (x) x)) ; 轉換簡單的恆等lambda函數。結果將是'(lambda (x k) (k x))'。

(cps '(lambda (x) (x 1))) ; 轉換將參數應用於1的lambda函數。結果將是'(lambda (x k) (x 1 k))'。

;; 無lambda（將產生恆等函數返回頂層）
(cps '(if (f x) a b)) ; 轉換測試部分為函數呼叫的if表達式。

(cps '(if x (f a) b)) ; 轉換測試部分為變數的if表達式。

;; 獨立if（尾位置）
(cps '(if x (f a) b)) ; 此處'if'位於頂層，故處於尾上下文。

;; 位於if測試內的if（非尾位置）
(cps '(lambda (x) (if (f x) a b))) ; 'if'位於lambda內，其結果由lambda使用（隱式返回），故不處於尾位置。

(cps '(lambda (x) (if (if x (f a) b) c d))) ; 嵌套if表達式。內層'if'位於外層'if'的測試中。

;; 兩個分支皆為簡單表達式，應進行更多優化
(cps '(lambda (x) (if (if x (zero? a) b) c d)))

;; 位於if分支內的if（尾位置）
(cps '(lambda (x) (if t (if x (f a) b) c))) ; 內層'if'位於外層'if'的結果分支中。若外層'if'處於尾上下文，內層亦同。

;; 位於if分支內，但再次位於另一if測試中（非尾位置）
(cps '(lambda (x) (if (if t (if x (f a) b) c) e w)))

;; 作為運算元的if（非尾位置）
(cps '(lambda (x) (h (if x (f a) b)))) ; 'if'表達式的結果作為參數傳給'h'。

;; 作為運算元的if（非尾位置）
(cps '(lambda (x) ((if x (f g) h) c))) ; 'if'表達式的結果作為要呼叫的函數。

;; 為何需要超過兩個名稱
(cps '(((f a) (g b)) ((f c) (g d)))) ; 此範例可能展示轉換複雜嵌套表達式時，需要新鮮變數名稱產生器（'fv'）來避免命名衝突。

;; 階乘
(define fact-cps
  (cps
   '(lambda (n)
      ((lambda (fact)
         ((fact fact) n))
       (lambda (fact)
         (lambda (n)
           (if (zero? n)
               1
               (* n ((fact fact) (sub1 n))))))))));; 輸出CPS化後的函數

(pretty-print fact-cps);; =>
;; '(lambda (n k)
;;    ((lambda (fact k) (fact fact (lambda (v0) (v0 n k))))
;;     (lambda (fact k)
;;       (k
;;        (lambda (n k)
;;          (if (zero? n)
;;            (k 1)
;;            (fact
;;             fact
;;             (lambda (v1) (v1 (sub1 n) (lambda (v2) (k (* n v2))))))))));
;;     k))

((eval fact-cps) 5 (lambda (v) v));; => 120
```

**CPS轉換器說明：**

此Scheme程式碼實現了針對Scheme簡單子集的續體傳遞風格（CPS）轉換。以下是關鍵概念的解析與程式碼運作原理：

**1. 續體傳遞風格（CPS）：**

* 在CPS中，函數不直接返回值，而是接受一個稱為**續體**的額外參數。
* 續體是代表當前函數結果後續計算步驟的函數。
* 當CPS函數完成計算時，會以結果呼叫續體。

**為何使用CPS？**

* **明確控制流：** CPS讓控制流變得明確。函數呼叫與返回被替換為對續體的呼叫。
* **尾呼叫優化：** CPS便於實現正確的尾呼叫優化。在轉換後的程式碼中，尾位置的函數呼叫成為最後操作，允許高效執行而不增加堆疊深度。
* **實現進階控制結構：** CPS可作為編譯器的中介表示，用於實現異常、協程和回溯等功能。

**2. `cps`函數：**

* 轉換的主要入口點。接受表達式`exp`作為輸入。
* 使用`letrec`定義數個相互遞迴的輔助函數。
* 透過以輸入表達式和恆等函數`id`作為初始續體呼叫`cps1`來初始化轉換。這意味著轉換後表達式的最終結果將直接返回。

**3. 輔助函數：**

* **`trivial?`：** 識別原始運算子如`zero?`、`add1`和`sub1`。這些在轉換中會特殊處理。
* **`id`：** 恆等函數`(lambda (v) v)`。作為初始續體，意即「直接返回值」。
* **`ctx0`：** 建立「尾上下文」。給定值`v`，返回`(k v)`，其中`k`是當前續體。表示當前計算處於尾位置，結果應直接傳遞給等待的續體。
* **`fv`：** 產生新鮮變數名稱（如`v0`、`v1`、`v2`...）。引入新續體時，避免變數捕捉至關重要。

**4. `cps1`函數（核心轉換）：**

* 此函數遞迴遍歷輸入表達式並將其轉換為CPS形式。
* 接受兩個參數：要轉換的表達式`exp`和當前續體`ctx`。
* 使用`pmatch`函式庫進行模式匹配來處理不同類型的表達式：

    * **字面值與變數：** 若表達式非序對（字面值或變數），它已是值。將當前續體`ctx`應用於此值：`(ctx x)`。

    * **`if`表達式：** 這是處理尾呼叫和避免上下文重複的轉換器關鍵部分。
        * 首先以接收測試結果（`t`）的續體轉換`test`表達式。
        * 若當前上下文`ctx`是尾上下文（`ctx0`）或初始恆等上下文（`id`），表示`if`表達式本身處於尾位置。此情況下保留`if`結構，並以相同上下文`ctx`對`conseq`和`alt`分支進行CPS轉換。
        * 若當前上下文非尾上下文，表示`if`表達式的結果後續會被使用。建立新續體`k`來接收`if`的結果並對其應用原始上下文`ctx`。接著以尾上下文`ctx0`對`conseq`和`alt`分支進行CPS轉換，並將整個`if`表達式包裹在引入`k`的`let`中。

    * **`lambda`表達式：** `lambda`表達式`(lambda (x) body)`轉換為接受額外參數`k`（續體）的新`lambda`表達式：`(lambda (x k) (cps1 body ctx0))`。原始lambda的主體以尾上下文`ctx0`進行CPS轉換。

    * **二元運算（`op a b`）：** 依序對運算元`a`和`b`進行CPS轉換。`a`的續體接收其結果`v1`，然後以接收其結果`v2`的續體對`b`進行CPS轉換。最後將原始上下文`ctx`應用於由運算子`op`和CPS化後的結果`v1`、`v2`組成的表達式。

    * **函數應用（`rator rand`）：** 依序對運算元（函數）和運算元（參數）進行CPS轉換。
        * 若運算元是`trivial?`運算子，直接將當前上下文`ctx`應用於運算子對運算元的應用結果。
        * 若當前上下文是尾上下文（`ctx0`），以CPS化後的參數`d`和當前續體`k`呼叫CPS化後的函數`r`。這確保了正確的尾呼叫。
        * 否則（非尾呼叫），建立新續體來接收函數呼叫的結果並對其應用原始上下文`ctx`。以CPS化後的參數`d`和此新續體呼叫CPS化後的函數`r`。

**5. 測試：**

* 程式碼包含多個測試案例，展示不同類型表達式的轉換，包括變數、lambda函數、各種上下文中的`if`表達式及函數應用。

**6. 階乘範例：**

* `fact-cps`定義展示CPS轉換器如何應用於遞迴階乘函數。
* `pretty-print`輸出顯示階乘函數的CPS化版本，現接受額外續體參數`k`。
* 最後一行以輸入`5`和頂層續體`(lambda (v) v)`（僅返回最終值）評估CPS化後的階乘函數。

**總結而言，此程式碼實現的CPS轉換旨在：**

* 將表達式轉換為續體傳遞風格。
* 透過明確傳遞當前續體來確保正確的尾呼叫優化。
* 當`if`本身處於尾位置時，透過保留`if`結構並以相同上下文對分支進行CPS轉換，有效處理`if`表達式而不重複周圍上下文。當`if`不處於尾位置時，引入新續體來處理結果。
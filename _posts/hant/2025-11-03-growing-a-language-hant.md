---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 培育一門語言
translated: true
type: note
---

### 概述
「語言成長」這場演講由 Guy L. Steele Jr. 於 1998 年 10 月 19 日在加拿大溫哥華舉行的 OOPSLA '98（物件導向程式設計、系統、語言與應用會議）上發表。這是一場長達 45 分鐘、關於語言設計與演進的開創性演講，使用 Scheme（Lisp 的一種方言）進行現場編碼示範。作為 Java 和 Scheme 的共同設計者，Steele 闡述了如何從零開始逐步構建程式語言，強調簡潔性、表達力與可擴展性。核心思想是：語言應從最精簡的原始元素出發，透過層層疊加功能來「有機成長」，而非一次性完成所有設計。

演講影片可在 YouTube 上觀看（由 ACM SIGPLAN 存檔），其思想對現代語言設計討論產生了深遠影響，包括函數式語言與嵌入式領域特定語言（DSL）的發展。

### 核心主題與結構
Steele 將演講結構設計為實作教學，透過現場編寫 Scheme 程式碼，將簡單的運算式求值器「培育」成完整的語言。他運用「園藝」（培育功能）與「建築」（僵化藍圖）的比喻，闡述演化式設計的優勢。以下是主要段落解析：

1. **引言：為何要培育語言？（0:00–5:00）**  
   Steele 透過批判「大爆炸」式語言設計（例如一次性規範所有功能導致冗餘）引出主題。他提出改為「培育」：從簡小起步、頻繁測試、根據實際需求擴展。借鑒 Lisp 的發展史，說明語言如何從求值器程式碼中成長。目標是建構一個可演化成圖靈完備的簡易算術運算式語言。

2. **種子：基礎求值器（5:00–10:00）**  
   從最核心開始：能處理基本數字（如 `3` → 3）的函數。  
   - 程式碼片段（Scheme）：  
     ```scheme
     (define (eval exp) exp)  ; 原子元素的恆等轉換
     ```  
   現場示範 `(eval 3)` 回傳 3。這就是「種子」——純粹無語法糖。

3. **萌芽：添加運算功能（10:00–20:00）**  
   透過對列表的模式匹配（如 `(+ 2 3)`）引入二元運算子。  
   - 擴充求值器：  
     ```scheme
     (define (eval exp)
       (if (pair? exp)
           (let ((op (car exp))
                 (args (cdr exp)))
             (apply op (map eval args)))
           exp))
     ```  
   示範求值過程：`(+ (* 2 3) 4)` → 10。強調程式碼潔淨——保持簡潔，避免過早優化。

4. **分枝：條件語句與變數（20:00–30:00）**  
   加入 `if` 條件判斷與 `let` 變數綁定，展示作用域如何自然形成。  
   - 擴充範例：  
     ```scheme
     (define (eval exp env)
       (if (pair? exp)
           (case (car exp)
             ((quote) (cadr exp))
             ((if) (if (eval (cadr exp) env)
                       (eval (caddr exp) env)
                       (eval (cadddr exp) env)))
             ((let) (eval (cadddr exp) (extend-env env (caadr exp) (eval (cadadr exp) env))))
             (else ...))  ; 預設為函數應用
           (lookup exp env)))  ; 變數查詢
     ```  
   現場演示：透過遞迴 `let` 綁定計算階乘，凸顯遞迴如何從迭代中「成長」。

5. **綻放：巨集與抽象化（30:00–40:00）**  
   引入衛生巨集以添加領域特定語法（如 `while` 迴圈），展示巨集如何讓使用者自行「擴展」語言。  
   - 關鍵洞見：語言應保持「開放」擴展性，如同 Lisp 的巨集系統，無需分叉核心即可實現 DSL。

6. **結論：給設計者的啟示（40:00–45:00）**  
   Steele 總結核心原則：  
   - **漸進主義**：一次只添加一項功能，立即測試。  
   - **一致性**：重複使用原始元素（例如萬物皆運算式）。  
   - **使用者賦能**：透過巨集等機制讓使用者擴展語言。  
   他聯繫實際語言（Java、Scheme）的發展，並警告「功能膨脹」的風險。問答環節涉及效能與實作挑戰的討論。

### 影響與啟示
本演講推廣了「語言工作台」理念，影響了 Racket（延伸自 Scheme）等工具，以及 Rust 巨集與 Swift 擴展等概念的發展。這是一堂將語言視為生命系統的經典課程——兼具實用性、哲學性與趣味性（Steele 的冷面幽默閃耀全場）。

完整體驗請觀看影片：[Growing a Language - OOPSLA '98](https://www.youtube.com/watch?v=_ahvzDzKdB0)。雖然文字紀錄與摘要較少，但程式碼可從投影片重建（透過 ACM Digital Library 取得）。若對程式語言設計感興趣，可搭配閱讀 Steele 後續的「Growing a Pattern Language」（OOPSLA '05）。
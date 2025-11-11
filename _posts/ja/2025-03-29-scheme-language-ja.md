---
audio: false
generated: true
lang: ja
layout: post
title: Schemeプログラミングチュートリアル
translated: true
type: note
---

Schemeは、そのシンプルさとエレガントさで知られるLispのミニマリストな方言です。このチュートリアルでは、基本を学んでいきます。

## 1. 基本構文と概念

### Schemeの実行
- Schemeインタプリタ（Racket、Guile、Chez Schemeなど）が必要です
- コードは通常、`.scm`ファイルに書くか、REPL（Read-Eval-Print Loop）で入力します

### 式と括弧
- Schemeではすべてが値を返す式です
- 括弧は関数呼び出しとグループ化に使用されます
- 形式: `(関数 引数1 引数2 ...)`

## 2. 基本データ型

```scheme
; 数値
42          ; 整数
3.14        ; 浮動小数点数
1/2         ; 有理数

; ブール値
#t          ; 真
#f         ; 偽

; 文字列
"hello"     ; 文字列リテラル

; シンボル
'hello      ; シンボル（'でクォート）
```

## 3. 基本操作

```scheme
; 算術演算
(+ 2 3)        ; 5
(- 10 4)       ; 6
(* 3 4)        ; 12
(/ 15 3)       ; 5

; 比較
(= 5 5)        ; #t
(< 3 7)        ; #t
(> 10 5)       ; #t
```

## 4. 変数の定義

```scheme
; グローバル変数の定義
(define x 10)

; 変数の使用
(+ x 5)        ; 15
```

## 5. 関数

### 関数の定義
```scheme
; 基本的な関数定義
(define square
  (lambda (x)    ; lambdaは無名関数を作成
    (* x x)))

(square 4)     ; 16
```

### 複数のパラメータ
```scheme
(define add
  (lambda (x y)
    (+ x y)))

(add 3 5)      ; 8
```

### 短縮形の定義
```scheme
; 代替構文（糖衣構文）
(define (multiply x y)
  (* x y))

(multiply 2 3) ; 6
```

## 6. 条件分岐

### If文
```scheme
(define (is-positive? n)
  (if (> n 0)
      #t
      #f))

(is-positive? 5)   ; #t
(is-positive? -2)  ; #f
```

### Cond（複数条件）
```scheme
(define (number-type n)
  (cond
    ((> n 0) "positive")
    ((< n 0) "negative")
    (else "zero")))

(number-type 5)    ; "positive"
(number-type 0)    ; "zero"
```

## 7. リスト

### リストの作成
```scheme
; quoteを使用
'(1 2 3)          ; 数値のリスト

; list関数を使用
(list 1 2 3)      ; 同上

; cons（構築）を使用
(cons 1 '(2 3))   ; 同上
```

### リスト操作
```scheme
(car '(1 2 3))    ; 1（最初の要素）
(cdr '(1 2 3))    ; (2 3)（残りのリスト）
(null? '())       ; #t（空かチェック）
(length '(1 2 3)) ; 3
```

## 8. 再帰

### 単純な再帰
```scheme
(define (factorial n)
  (if (= n 0)
      1
      (* n (factorial (- n 1)))))

(factorial 5)     ; 120 (5 * 4 * 3 * 2 * 1)
```

### リストの再帰
```scheme
(define (sum-list lst)
  (if (null? lst)
      0
      (+ (car lst) (sum-list (cdr lst)))))

(sum-list '(1 2 3 4))  ; 10
```

## 9. 高階関数

### マッピング
```scheme
(map square '(1 2 3 4))    ; (1 4 9 16)
(map + '(1 2 3) '(4 5 6))  ; (5 7 9)
```

### フィルタリング
```scheme
(define (even? n) (= (remainder n 2) 0))
(filter even? '(1 2 3 4 5 6))  ; (2 4 6)
```

## 10. Letバインディング

```scheme
; ローカル変数のバインディング
(define (circle-area r)
  (let ((pi 3.14159))
    (* pi (square r))))

(circle-area 2)    ; 12.56636
```

## 11. 入力/出力

```scheme
; 出力の表示
(display "Hello, Scheme!")
(newline)

; 入力の読み取り（実装によって異なる場合があります）
(define name (read))
(display "Hello, ")
(display name)
```

## 12. サンプルプログラム

いくつかの概念を組み合わせた完全なプログラムです：

```scheme
; 数値リストの平均を計算するプログラム
(define (average lst)
  (define (sum lst)
    (if (null? lst)
        0
        (+ (car lst) (sum (cdr lst)))))
  (define len (length lst))
  (if (= len 0)
      0
      (/ (sum lst) len)))

; プログラムのテスト
(display (average '(1 2 3 4 5)))  ; 3
(newline)
(display (average '()))           ; 0
```

## Schemeの主な特徴

1. **ミニマリスト**: 強力な機能を持つ小さなコア言語
2. **関数型**: 純粋関数と不変性を重視
3. **前置記法**: すべての操作で前置構文を使用
4. **第一級関数**: 関数を引数として渡せる
5. **末尾再帰最適化**: 効率的な再帰

## 学習のヒント

1. REPLで練習して即座に結果を確認する
2. 単純な関数から始めて複雑さを増していく
3. リスト処理では再帰的に考える
4. 適切なインデントで括弧を管理する
5. 高階関数を試してみる

このチュートリアルはSchemeの核心概念をカバーしています。理解を深めるには、以下を試してみてください：
- より複雑な再帰関数を書く
- マクロシステムを探求する（上級トピック）
- 電卓やリストプロセッサなどの小さなプロジェクトを構築する
- Schemeの標準ライブラリを学ぶ（実装によって異なります）

特定のセクションについて詳しく説明してほしい、またはさらに例が必要な場合はお知らせください。
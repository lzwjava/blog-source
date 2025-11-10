---
audio: false
generated: true
image: false
lang: ja
layout: post
title: 継続渡しスタイル変換コードの詳細解説
translated: true
type: note
---

以下はスクリーンショットから抽出したコードを、明確さのために再フォーマットしたものです：

```scheme
(define cps
  (lambda (exp)
    (letrec
        ([trivial? (lambda (x) (memq x '(zero? add1 sub1)))]
         [id (lambda (v) v)]
         [ctx0 (lambda (v) `(k ,v))]   ; 末尾コンテキスト
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
                               (ctx `(,op ,v1 ,v2)))))))]
              [(,rator ,rand)
               (cps1 rator
                     (lambda (r)
                       (cps1 rand
                             (lambda (d)
                               (cond
                                 [(trivial? r) (ctx `(,r ,d))]
                                 [(eq? ctx ctx0) `(,r ,d ,k)] ; 末尾呼び出し
                                 [else
                                  (let ([u (fv)])
                                    `(,r ,d (lambda (,u) ,(ctx u))))]))))))]))]
      (cps1 exp id))))
```

---

## このコードの役割

これは、小さなSchemeライクな言語のための**継続渡しスタイル (CPS) 変換器**の実装です。CPSは、*継続関数*を渡し回すことで制御フローを明示的にするようにプログラムを書き換える方法です。

### 主要コンポーネント

1. **自明な操作**

   ```scheme
   (trivial? (lambda (x) (memq x '(zero? add1 sub1))))
   ```

   いくつかのプリミティブ演算子を自明（CPSラッピングが不要）とマークします。

2. **継続コンテキスト**

   ```scheme
   [id (lambda (v) v)]      ; 恒等コンテキスト
   [ctx0 (lambda (v) `(k ,v))] ; デフォルトの末尾継続
   ```

   `id` は単に引数を返し、`ctx0` は「値を継続 `k` に返す」ことを意味します。

3. **新規変数**

   ```scheme
   [fv ...] ; シンボル v0, v1, v2, ... を生成
   ```

   新しいバインディングが必要な場合に使用されます。

4. **メイン変換器**

   ```scheme
   cps1
   ```

   これは式をCPS形式にケースバイケースで再帰的に変換します。

   * **変数と定数**
     `x` がペアでない（原子的な）場合、単に継続コンテキストを適用します。

   * **条件式**

     ```scheme
     (if test conseq alt)
     ```

     テストが最初にCPS変換されます。
     コンテキストが単純な場合（`ctx0` または `id`）、直接の `if` を生成します。
     それ以外の場合は、新しい継続 `k` を生成し、両方の分岐を `ctx0` でCPS変換します。

   * **ラムダ式**

     ```scheme
     (lambda (x) body)
     ```

     `(lambda (x k) <bodyのCPS変換結果>)` に変換されます。つまり、ラムダ式は明示的に継続を受け取るようになります。

   * **二項演算**

     ```scheme
     (op a b)
     ```

     両オペランドがCPS変換され、その後結合されます。

   * **関数適用**

     ```scheme
     (rator rand)
     ```

     演算子と被演算子がCPS変換されます。その後、自明性に応じて処理します：

     * 演算子がプリミティブの場合、直接適用します。
     * 末尾位置にある場合 (`ctx = ctx0`)、単に `(r d k)` を呼び出します。
     * それ以外の場合は、新しい継続でラップします。

5. **エントリポイント**

   ```scheme
   (cps exp)
   ```

   初期コンテキストとして `id` を指定して `cps1` を呼び出します。

---

## 例による直観

次の式をCPS変換するとします：

```scheme
((lambda (x) (add1 x)) 5)
```

CPS変換は、これを次のようなものに変換します：

```scheme
((lambda (x k)
   (k (add1 x)))
 5
 k)
```

ここで `k` は結果のための継続です。関数は値を返す代わりに、`k` をその値で呼び出します。

---

## レビュー

* **長所**

  * すべてのコアCPS変換ルール（変数、条件式、ラムダ式、適用）を実装しています。
  * 自明な演算子と高階呼び出しを正しく区別します。
  * 末尾呼び出しを特別に扱います（Schemeのセマンティクスにとって重要）。
  * 衛生的な新規変数生成 (`fv`) を使用しています。

* **潜在的な問題点**

  * プリミティブが限られている (`zero?`, `add1`, `sub1`) — より豊富な言語には `trivial?` を拡張する必要があります。
  * `pmatch` (パターンマッチャ) を使用しています — サポートするマクロライブラリが必要です。
  * 新規変数ジェネレータ (`fv`) はグローバルな `n` を変更します — 小さな実験には問題ありませんが、並行またはモジュール化された使用では安全ではありません。
  * 多引数ラムダ式を扱えません（単項のみ）。
  * let束縛や関数適用を超えるシーケンシングのサポートがありません。

---

✅ 総評：これはおもちゃのSchemeのためのCPS変換の、教育的な実装として見事なものです。継続渡しのメカニズム（`k` 引数の追加、分岐のラッピング、制御の明示化）を明確に示しています。

---

**具体的な作業例を段階的に見たい** ですか（例：`(if (zero? x) (add1 y) (sub1 y))` のCPS変換をステップバイステップで示す）？そうすれば、このコードがそれをどのように書き換えるか正確に確認できます。
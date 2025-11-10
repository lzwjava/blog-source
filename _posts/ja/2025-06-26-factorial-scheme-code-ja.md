---
audio: false
generated: true
lang: ja
layout: post
title: Chez Scheme階乗プログラム
translated: true
type: note
---

数値の階乗を計算するシンプルなChez Schemeプログラムです。`factorial.scm`として保存してください：

```scheme
(define (factorial n)
  (if (<= n 1)
      1
      (* n (factorial (- n 1)))))

(display "Factorial of 5 is: ")
(display (factorial 5))
(newline)
```

実行方法：
1. コードを`factorial.scm`というファイル名で保存します
2. ターミナルでファイルがあるディレクトリに移動します
3. `scheme --script factorial.scm`を実行します

出力結果：
```
Factorial of 5 is: 120
```

このプログラムは再帰的な`factorial`関数を定義し、5の階乗を計算します。`--script`オプション（`scheme --help`の出力に示されている通り）を使用すると、ファイルを直接実行できます。
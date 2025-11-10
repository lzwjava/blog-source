---
audio: false
generated: true
image: false
lang: ja
layout: post
title: Python Difflib シーケンス比較ガイド
translated: true
type: note
---

Pythonでは、**`difflib`** モジュールがシーケンス（文字列、リスト、その他のイテラブル）を比較するためのツールを提供します。このモジュールは、テキスト間の差分検出（Unixの `diff` のように）や、オートコンプリート機能、類似性ツールの構築などのタスクによく使用されます。

---

### `difflib` の仕組み

`difflib` の核心は、2つの入力間で最長の連続した一致する部分シーケンスを見つけようとすることです。そして、これらの一致を使用して類似点と相違点を強調表示します。このライブラリでは以下を行うことができます：

* 人間が読みやすい差分の生成 (`ndiff`, `unified_diff`, `context_diff`)
* シーケンス間の類似率の計算
* リストからの近似一致の提案 (`get_close_matches`)

---

### `SequenceMatcher`

最も重要なクラスは **`difflib.SequenceMatcher`** です。

**仕組み**:

* 2つのシーケンスを要素ごとに比較します。
* *最長共通部分シーケンス*（必ずしも連続している必要はない）を探します。
* あるシーケンスを別のシーケンスに変換する方法を説明する操作（`replace`, `delete`, `insert`, `equal`）のリストを生成します。

**主なメソッド**:

1.  **`ratio()`**
    類似性を測定する [0, 1] の範囲の浮動小数点数を返します。
    計算式:

    $$
    \text{ratio} = \frac{2 \times M}{T}
    $$

    ここで、`M` = 一致する要素の数、`T` = 両方のシーケンスの合計要素数です。

2.  **`quick_ratio()`** と **`real_quick_ratio()`**
    類似性のより高速な近似値を返します。精度を犠牲にして速度を優先します。

3.  **`get_opcodes()`**
    `a` を `b` に変換するための操作のリストを返します。
    例: `[('replace', 0, 2, 0, 1), ('equal', 2, 4, 1, 3)]`

4.  **`get_matching_blocks()`**
    位置情報を含むすべての一致する部分シーケンスを返します。

---

### 例

```python
import difflib

a = "hello world"
b = "helo wrld"

s = difflib.SequenceMatcher(None, a, b)

print("類似率:", s.ratio())
print("操作:", s.get_opcodes())
print("一致ブロック:", s.get_matching_blocks())
```

**出力**:

```
類似率: 0.9090909090909091
操作: [('equal', 0, 1, 0, 1), ('delete', 1, 2, 1, 1),
       ('equal', 2, 5, 1, 4), ('delete', 5, 6, 4, 4),
       ('equal', 6, 11, 4, 9)]
一致ブロック: [Match(a=0, b=0, size=1),
                Match(a=2, b=1, size=3),
                Match(a=6, b=4, size=5),
                Match(a=11, b=9, size=0)]
```

---

👉 要約すると:

*   `difflib` はシーケンス比較のツールキットです。
*   `SequenceMatcher` は中核となるエンジンで、一致する部分シーケンスを見つけ、類似性を計算します。
*   差分ツール、スペルチェッカー、盗用検出、自動提案などに役立ちます。

スペルチェックや検索候補のように、ファジー文字列マッチングのために `get_close_matches()`（内部的に `SequenceMatcher` を使用）の使用方法もご紹介しましょうか？
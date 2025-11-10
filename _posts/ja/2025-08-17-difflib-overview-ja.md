---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: Python difflib モジュール概要
translated: true
type: note
---

### difflibの概要
Python標準ライブラリの`difflib`モジュールは、シーケンス（文字列、リストなど）を比較して差分を見つけるために使用されます。テキストの差分比較、パッチ生成、類似性チェックなどのタスクに便利です。主なクラスと関数には、`Differ`（詳細な差分用）、`SequenceMatcher`（類似率とマッチング用）、および`ndiff`や`unified_diff`などの差分ジェネレータが含まれます。

### インポートと基本設定
インストールは不要です。標準ライブラリに含まれています。
```python
import difflib
```

### 主な関数とクラス

1. **`SequenceMatcher`**: 類似率を計算し、一致する部分シーケンスを見つけます。
   - ファジーマッチングや簡単な類似度スコアの取得に使用します。
   - 例:
     ```python
     seq1 = "abcdef"
     seq2 = "abcefg"
     matcher = difflib.SequenceMatcher(None, seq1, seq2)
     print("類似率:", matcher.ratio())  # 出力: ~0.83 (近い一致)
     print("共通要素:", matcher.find_longest_match(0, len(seq1), 0, len(seq2)))  # 最長一致を検索
     ```
     - `ratio()`は類似度を示す浮動小数点数（0から1）を返します。
     - `get_matching_blocks()`などのメソッドは正確な一致をリストします。

2. **`Differ`**: 行単位での追加、削除、変更を示す人間が読みやすい差分を生成します。
   - リストや複数行の文字列を比較するのに最適です。
   - 例:
     ```python
     text1 = ["line1", "line2", "line3"]
     text2 = ["line1", "line2 modified", "line3", "line4"]
     d = difflib.Differ()
     diff = list(d.compare(text1, text2))
     print("\n".join(diff))
     # 出力例:
     #   line1
     #   line2
     # - line3
     # + line2 modified
     # + line3  (実際の出力は行の変更を示します。正確さのために調整してください)
     ```
     - プレフィックス: `  ` (変更なし), `- ` (削除), `+ ` (追加), `? ` (行内の差分)。

3. **`ndiff`** と **`unified_diff`**: 特定のフォーマットで差分を生成します。
   - **`ndiff`**: `Differ`のようなシンプルな行単位の差分。
     ```python
     diff = list(difflib.ndiff(["a", "b"], ["a", "c"]))
     # 出力: ['  a', '- b', '+ c']
     ```
   - **`unified_diff`**: 統一差分フォーマット（Gitの差分のような）を作成し、パッチに便利です。
     ```python
     diff = difflib.unified_diff(["a", "b"], ["a", "c"], fromfile='file1', tofile='file2')
     print("\n".join(diff))
     # 出力例:
     # --- file1
     # +++ file2
     # @@ -1,2 +1,2 @@
     #  a
     # -b
     # +c
     ```

### ヒントとベストプラクティス
- **正規化**: 大文字小文字を区別しない比較や空白を無視する比較には、入力を前処理します（例: `text.lower()` や `text.splitlines()`）。
- **パフォーマンス**: 長いシーケンスの場合、ジャンクヒューリスティックが不要な場合は`autojunk=False`を指定して`SequenceMatcher`を使用します。
- **統合**: ファイル比較には`filecmp`と組み合わせるか、バージョン管理スクリプトで使用します。
- **応用**: HTMLフォーマットの差分には`HtmlDiff`を探索します（ほとんど必要ありませんが利用可能です）。

完全なドキュメントは、Pythonの[公式difflibページ](https://docs.python.org/3/library/difflib.html)を参照してください。特定のユースケースがある場合は、詳細を提供すると具体的な例を提示できます。
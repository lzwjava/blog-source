---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: Pythonグロブモジュールファイルマッチングガイド
translated: true
type: note
---

### globのインポート
Pythonでglobを使用するには、標準ライブラリからモジュールをインポートします：
```python
import glob
```

### 基本機能
`glob.glob()`関数はパターン文字列を受け取り、一致するファイルまたはディレクトリパスのリストを返します。Unixシェルスタイルのワイルドカードを使用します：

- `*`：任意の文字シーケンスに一致します（パス区切り文字を除く）。
- `?`：任意の1文字に一致します。
- `[seq]`：seq内の任意の文字に一致します（例：`[0-9]`は数字に一致）。
- `**`：ディレクトリを再帰的に検索します（`recursive=True`が必要）。

パターンは絶対パスが指定されない限り、現在のディレクトリを基準にします。

### 使用例

#### 1. 現在のディレクトリ内のすべての.txtファイルを検索
```python
import glob

files = glob.glob("*.txt")
print(files)  # 出力: ['file1.txt', 'file2.txt', ...]
```

#### 2. サブディレクトリ内の特定の拡張子を持つファイルを検索
```python
files = glob.glob("documents/*.pdf")
print(files)  # 出力: ['documents/doc1.pdf', ...]
```

#### 3. 特定のパターンに一致するファイル（例：'log'で始まり数字で終わるファイル）
```python
files = glob.glob("log[0-9].txt")
print(files)  # 出力: ['log1.txt', 'log2.txt', ...]（該当ファイルが存在する場合）
```

#### 4. サブディレクトリでの再帰的検索
`**`を`recursive=True`と共に使用して、ディレクトリとサブディレクトリを検索：
```python
files = glob.glob("**/*.py", recursive=True)
print(files)  # 出力: ['script1.py', 'subdir/script2.py', ...]
```

### 重要な注意点
- 結果はデフォルトでソートされていません；順序が必要な場合は`sorted()`を使用：`sorted(glob.glob("*.txt"))`。
- 大文字小文字を区別するファイルシステムで大文字小文字を区別しないマッチングを行うには、`fnmatch`との組み合わせやコード内での処理を検討してください（globは大文字小文字を区別します）。
- globはシンボリックリンクを追跡しません（明示的に処理されない限り）；より複雑な走査には`os.walk()`を使用してください。
- 一度に1つの一致を処理するには、`glob.iglob()`を使用します（大きな結果セットでメモリを節約するためのイテレータを返します）：`for file in glob.iglob("*.txt"): print(file)`。

これで基本は網羅しています；詳細は[Pythonドキュメント](https://docs.python.org/3/library/glob.html)を参照してください。
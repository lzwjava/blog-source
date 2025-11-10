---
audio: false
generated: true
image: false
lang: ja
layout: post
title: Git Diff-Treeガイド
translated: true
type: note
---

以下は、`git diff-tree`の実践的でエンドツーエンドのガイドです。これが何であるか、いつ使うか、実際の作業で役立つオプションを説明します。大きな表は避け、コピー＆ペースト可能な例を用いた焦点を絞った解説に徹します。

# `git diff-tree`の実際の動作

* **ツリーオブジェクト**を比較します。日常的な使用では、通常「**コミット**とその親コミットとの間で何が変更されたかを表示する」ことを意味します。
* `git show`/`git log`が porcelain (人間向け) であるのに対し、これは **plumbing** (スクリプト向け) です。
* ワーキングディレクトリを参照することはなく、リポジトリに保存されたツリー (コミット、コミットを指すタグ、または生のツリーID) のみを比較します。

# 使用する基本的な形式

1. コミットをその親と比較する

```bash
git diff-tree -p <commit>
```

`<commit>` に親が1つある場合、通常のパッチが表示されます。マージコミットの場合、マージを要求しない限り何も表示されません (後述)。

2. 2つのツリー/コミットを明示的に比較する

```bash
git diff-tree -p <old-tree-or-commit> <new-tree-or-commit>
```

「コミット vs 親」だけでなく、任意の2点を比較したい場合に便利です。

3. ファイル名のみを表示する (パッチなし)

```bash
git diff-tree --name-only -r <commit>
```

`-r` を追加してサブディレクトリに再帰的に入り、フラットなリストを取得します。

4. 変更タイプ付きで名前を表示する

```bash
git diff-tree --name-status -r <commit>
# 以下のような行を出力:
# A path/to/newfile
# M path/to/modified
# D path/to/deleted
```

5. パッチ (完全な差分) を表示する

```bash
git diff-tree -p <commit>            # `git show`のような unified diff
git diff-tree -U1 -p <commit>        # コンテキストを少なく (1行)
```

# 知っておくべきオプション (理由とタイミング)

* `-r` — サブツリーに再帰的に入り、すべてのネストされたパスを表示します。これがないと、変更されたディレクトリが単一行で表示される可能性があります。
* `--no-commit-id` — コミット単位の出力をスクリプト処理する際に、「commit <sha>」ヘッダーを抑制します。
* `--root` — コミットに**親がない**場合 (初期コミット) でも、空のツリーとの差分を表示します。
* `-m` — マージコミットに対して、**各親に対する差分**を表示します (複数の差分を生成)。
* `-c` / `--cc` — 結合されたマージ差分。`--cc` は洗練されたビューです (`git show` がマージに使用するもの)。
* `--name-only` / `--name-status` / `--stat` / `--numstat` — さまざまな要約スタイル。`--numstat` はスクリプト処理に適しています (追加/削除された行数)。
* `--diff-filter=<set>` — 変更タイプでフィルタリングします。例: `--diff-filter=AM` (追加または変更のみ)。一般的な文字: `A`dd (追加), `M`odified (変更), `D`eleted (削除), `R`enamed (名前変更), `C`opied (コピー), `T`ype changed (タイプ変更)。
* `-M` / `-C` — 名前変更とコピーを検出します。オプションの類似度しきい値を追加できます。例: `-M90%`。
* `--relative[=<path>]` — 出力をサブディレクトリに制限します。引数なしの場合、現在の作業ディレクトリを使用します。
* `-z` — パスを **NUL で終端**し、明確なマシンパーシングを実現します (ファイル名の改行やタブを処理)。
* `--stdin` — 標準入力からコミット (またはペア) のリストを読み取ります。これは高速なバッチ操作の秘訣です。

# 標準的なスクリプトパターン

### 1) 単一コミットで変更されたファイルをリストする

```bash
git diff-tree --no-commit-id --name-status -r <commit>
```

### 2) 多数のコミットをバッチ処理 (高速!)

```bash
git rev-list main --since="2025-08-01" |
  git diff-tree --stdin -r --no-commit-id --name-status
```

`--stdin` はコミットごとに `git` を起動するのを避け、広い範囲に対してはるかに高速です。

### 3) ディレクトリ内の追加と変更のみ

```bash
git diff-tree -r --no-commit-id --name-status \
  --diff-filter=AM <commit> -- src/backend/
```

### 4) ファイルごとに追加/削除された行数をカウント (スクリプト向け)

```bash
git diff-tree -r --no-commit-id --numstat <commit>
# 出力: "<追加行数>\t<削除行数>\t<パス>"
```

### 5) コミット内の名前変更を検出して表示

```bash
git diff-tree -r --no-commit-id -M --name-status <commit>
# "R100 old/name.txt\tnew/name.txt" のような行
```

### 6) マージコミットのパッチ

```bash
git diff-tree -m -p <merge-commit>     # 親ごとのパッチ
git diff-tree --cc <merge-commit>      # 結合ビュー (単一パッチ)
```

### 7) 初期コミット (親なし)

```bash
git diff-tree --root -p <initial-commit>
```

# 生のレコード形式の理解 (手動で解析する場合)

`--raw` (いくつかのモードで暗黙的に使用される) を使用して、最小限で安定したレコードを取得します:

```
:100644 100644 <oldsha> <newsha> M<TAB>path
```

* 数字はファイルモード: `100644` 通常ファイル, `100755` 実行可能ファイル, `120000` シンボリックリンク, `160000` gitlink (サブモジュール)。
* ステータスは単一の文字 (`A`, `M`, `D` など)、場合によってはスコア付き (例: `R100`)。
* 名前変更/コピーの場合、2つのパスが表示されます。`-z` がある場合、フィールドは NUL 区切りです。`-z` がない場合、タブ区切りです。

**ヒント:** 信頼性の高いツールを構築する場合は、常に `-z` を渡し、NUL で分割してください。改行を含むファイル名が存在します。

# 関連コマンドとの比較 (適切なものを選ぶために)

* `git diff`: **インデックス/ワーキングツリー**と HEAD、または任意の2つのコミット/ツリーを比較します。対話的な開発向け。
* `git show <commit>`: 「親との差分 + メタデータ」の便利なラッパーです。人間向けに優れています。
* `git log -p`: 履歴とパッチです。範囲指定の場合、手動で `diff-tree` をループするよりも便利なことが多いです。
* `git diff-tree`: **正確でスクリプト可能なコミット単位の差分**のための plumbing で、`--stdin` でバッチ処理可能。

# 実世界の例

### 「この PR マージコミットで何が変更された？」

```bash
git diff-tree --cc <merge-commit> | less
```

親ごとの詳細が必要な場合:

```bash
git diff-tree -m -p <merge-commit> | less
```

### 「最新のコミットで変更されたファイルのクリーンなリストを CI ステップに渡す」

```bash
git diff-tree --no-commit-id --name-only -r HEAD > changed.txt
```

### 「過去 20 コミットで追加または変更された Java ファイルのみ」

```bash
git rev-list -n 20 HEAD |
  git diff-tree --stdin -r --no-commit-id --name-only --diff-filter=AM |
  grep -E '\.java$'
```

### 「リリースタグ間の変更行数の要約」

```bash
git diff-tree -r --no-commit-id --numstat v1.2.0..v1.3.0
```

### 「変なファイル名を安全に処理する」

```bash
git diff-tree -z -r --no-commit-id --name-status <commit> |
  awk -v RS='\0' 'NR%2{status=$0; next}{printf "%s %s\n", status, $0}'
```

# パフォーマンスに関する注意

* 広い範囲に対しては、プロセス生成のオーバーヘッドを避けるため、`git rev-list` と `--stdin` を優先してください。
* 行変更が不要な場合は、パッチ (`--name-only`/`--name-status`) をスキップしてください。
* 正確性よりも速度を重視する場合は、名前変更検出 (`-M`, `-C`) を避けてください。

# 注意点とエッジケース

* **マージではデフォルトで出力なし。** `-m` (親ごと) または `--cc`/`-c` (結合) を渡す必要があります。
* **初期コミットは「空のツリー vs ツリー」。** `--root` を使用して差分を強制表示します。
* **サブモジュール**はモード `160000` と SHA (gitlink) を表示します。サブモジュールリポジトリ内で差分を取らない限り、内部の差分は表示されません。
* **パススペックは `--` の後に置く。** パスでフィルタリングする場合、曖昧さを避けるために `--` の後に置いてください。
* **空白/改行を含むファイル名。** 解析する場合は常に `-z` を追加してください。

# 実際に再利用できるクイック「チートスニペット」

```bash
# 変更されたファイル (フラットリスト)
git diff-tree --no-commit-id --name-only -r <commit>
```
---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Git Check-Ignoreコマンドの概要
translated: true
type: note
---

### `git check-ignore`とは？

`git check-ignore` コマンドは、特定のファイルやパスがGitの無視メカニズム（`.gitignore`ファイル、`.git/info/exclude`、グローバル無視ファイル（`core.excludesFile`経由）など）によって無視されているかどうかを判定するためのGitツールです。ファイルがリポジトリに追跡されなかったり追加されなかったりする理由をデバッグする際に特に便利です。

パスが無視されている場合、コマンドはそのパス（およびオプションでマッチしたパターン）を出力します。無視されていない場合、何も出力されません（終了コード0）。この特性により、自動化スクリプトで使いやすくなっています。

### 基本的な使用方法

チェックしたい1つ以上のパスを指定して実行します：

```
git check-ignore <パス名>...
```

- **例**: 単一ファイルが無視されているかチェック：
  ```
  git check-ignore path/to/myfile.txt
  ```
  - 出力：無視されている場合は `path/to/myfile.txt` を表示。無視されていない場合は何も表示しない。

- **例**: 複数ファイルをチェック：
  ```
  git check-ignore file1.txt file2.txt dir/file3.txt
  ```
  - 無視されているパスのみを1行ずつ出力。

### 主なオプション

| オプション | 説明 | 使用例 |
|--------|-------------|---------|
| `-v`, `--verbose` | マッチした無視パターン（例：`.gitignore`の該当行）を表示。 | `git check-ignore -v path/to/myfile.txt`<br>出力例: `path/to/myfile.txt: .gitignore:1:*.txt` (パス + ファイル名:行番号:パターン) |
| `-q`, `--quiet` | 出力を抑制するが、終了コードは使用する（無視されない場合は0、無視される場合は1）。スクリプトで便利。 | `git check-ignore -q path/to/myfile.txt`<br>（出力なし；終了コード `$?` を確認） |
| `--stdin` | コマンドライン引数ではなく標準入力からパスを読み取る。 | `echo "file1.txt\nfile2.txt" \| git check-ignore --stdin` |
| `--non-matching` | 出力を反転：無視され*ない*パスを表示。 | `git check-ignore --non-matching -v file1.txt file2.txt` |

### 一般的な使用例

1. **`.gitignore` ルールのデバッグ**:
   - `git status` で想定していたファイルが表示されない場合、`git check-ignore -v <ファイル>` を実行して、どのルールがそれを無視しているかを正確に確認できます。
   - 出力例: `src/logs/app.log: .gitignore:5:logs/*` (`.gitignore`の5行目がマッチしたことを示す)。

2. **スクリプト内での使用**:
   - ファイルを追加すべきかチェック：
     ```
     if git check-ignore -q myfile.txt; then
         echo "ファイルは無視されるため、スキップ..."
     else
         git add myfile.txt
     fi
     ```

3. **一括チェック**:
   - ディレクトリ内のすべての無視ファイルをリスト表示：
     ```
     find . -type f -print0 | xargs -0 git check-ignore
     ```

### ヒント
- Gitの無視スタック（ローカル`.gitignore`、グローバルexcludesなど）を尊重します。
- 未追跡ファイルやリポジトリ内に既にあるファイルの両方で動作します（ただし、無視ルールに対してチェックします）。
- 詳細については、公式ドキュメントを参照してください。

[Git check-ignore ドキュメント](https://git-scm.com/docs/git-check-ignore)  
[Stack Overflow: .gitignore によって無視されている特定のファイルを表示するGitコマンド](https://stackoverflow.com/questions/466764/git-command-to-show-which-specific-files-are-ignored-by-gitignore)  
[git check-ignore を使用して .gitignore をデバッグする](https://alexwlchan.net/til/2020/using-git-check-ignore-to-debug-your-gitignore/)
---
audio: false
generated: true
image: false
lang: ja
layout: post
title: VS Codeで無視されたファイルを除外
translated: true
type: note
---

`.gitignore` にあるファイルを「Go to File」（クイックオープン、Ctrl + P）に含めるには、`settings.json` で以下の3つの設定を調整できます：

1. **検索に `.gitignore` ルールを無視させる**

   ```jsonc
   "search.useIgnoreFiles": false,      // .gitignore を尊重しない
   "search.useGlobalIgnoreFiles": false // グローバル gitignore を尊重しない
   ```
2. **除外 glob パターンがそれらのファイルを隠さないようにする**
   デフォルトでは、VS Code は `files.exclude` からのすべてのパターンを `search.exclude` に継承します。もし `.gitignore` で指定されたディレクトリを手動で除外している場合は、それらを再度有効にしてください：

   ```jsonc
   "search.exclude": {
     "**/.git": false,          // .git をインデックスする（必要であれば）
     "**/.gitignore": false     // .gitignore ファイル自体を確実に隠さない
     // …上書きしたい他のパターン
   }
   ```
3. **ウィンドウをリロードする**
   ユーザーまたはワークスペース設定を保存した後、**Developer: Reload Window**（⇧ ⌘ P → 「Reload Window」）を実行して、ファイルインデクサが変更を認識するようにします。

これで Ctrl + P を押すと、無視されているかどうかに関係なく、*すべての*ファイルが名前で表示されるようになります。（[stackoverflow.com][1]）

[1]: https://stackoverflow.com/questions/62855190/how-do-you-include-git-ignored-files-in-vscode-quick-search?utm_source=chatgpt.com "How do you include git ignored files in VSCode quick search"
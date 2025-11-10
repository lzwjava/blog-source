---
audio: false
generated: true
image: false
lang: ja
layout: post
title: GitHubコード検索のヒントJSON
translated: true
type: note
---

以下のようにGitHubコード検索クエリを記述できます:

```
"deepseek/deepseek-chat-v3.1" language:JSON
```

### 注意点:

* 引用符はGitHubが正確な文字列`deepseek/deepseek-chat-v3.1`を検索することを保証します
* `language:JSON`（または`lang:json`、どちらも有効）は結果をJSONファイルに制限します
* `.json`ファイル以外のJSON形式の設定ファイル（`.ipynb`や`.eslintrc`など）を含めたい場合は、`lang:`フィルターを外せます

例:

* JSONファイルのみを検索:

  ```
  "deepseek/deepseek-chat-v3.1" lang:json
  ```

* すべてのファイルタイプを検索し、JSON結果を強調表示:

  ```
  "deepseek/deepseek-chat-v3.1"
  ```

さらに詳細な検索方法（リポジトリ内、issue、コード内のみの検索など）についても説明しましょうか？
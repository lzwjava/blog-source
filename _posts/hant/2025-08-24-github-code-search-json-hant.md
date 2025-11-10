---
audio: false
generated: true
image: false
lang: hant
layout: post
title: GitHub 代碼搜尋技巧 JSON
translated: true
type: note
---

你可以這樣撰寫 GitHub 程式碼搜尋查詢：

```
"deepseek/deepseek-chat-v3.1" language:JSON
```

### 注意事項：

* 引號確保 GitHub 搜尋確切的字串 `deepseek/deepseek-chat-v3.1`
* `language:JSON`（或 `lang:json`，兩者皆可使用）將結果限制在 JSON 檔案
* 若想包含非 `.json` 檔案中的 JSON 格式設定（例如 `.ipynb` 或 `.eslintrc`），可以移除 `lang:` 篩選器

範例：

* 僅搜尋 JSON 檔案：

  ```
  "deepseek/deepseek-chat-v3.1" lang:json
  ```

* 搜尋所有檔案類型但仍突出顯示 JSON 結果：

  ```
  "deepseek/deepseek-chat-v3.1"
  ```

需要我進一步示範如何精煉搜尋條件嗎？例如僅在儲存庫、問題或程式碼中進行搜尋？
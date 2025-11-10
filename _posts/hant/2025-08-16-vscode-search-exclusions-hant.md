---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 在 VS Code 中自訂搜尋排除項目
translated: true
type: note
---

在 VS Code 中，全域檔案搜尋功能會遵循您設定的**搜尋排除規則**。您可以設定讓搜尋結果忽略特定檔案或資料夾。

以下是主要方法：

---

### 1. 在 **settings.json** 中使用 `search.exclude`

開啟設定（`⌘,` / `Ctrl+,` → 右上角「開啟設定 (JSON)」）並新增：

```json
"search.exclude": {
  "**/node_modules": true,
  "**/dist": true,
  "**/*.log": true
}
```

* 鍵名使用 [glob 模式](https://code.visualstudio.com/docs/editor/codebasics#_advanced-search-options)
* `true` 表示「從搜尋中排除」
* 範例：

  * `**/node_modules` → 所有 node_modules 資料夾
  * `**/*.log` → 所有位置的 `.log` 檔案
  * `**/build/**` → build 資料夾內的所有內容

---

### 2. 使用 `.gitignore`

如果您的專案有 `.gitignore` 檔案，可以設定 VS Code 在搜尋時遵循該檔案：

```json
"search.useIgnoreFiles": true
```

這樣被 Git 忽略的內容就不會出現在搜尋結果中。

---

### 3. 使用 `.ignore`

您也可以在專案根目錄建立 `.ignore` 檔案（格式與 `.gitignore` 相同），專門用於編輯器工具。當 `search.useIgnoreFiles` 啟用時，VS Code 會遵循此檔案。

---

### 4. 在搜尋介面中快速排除

進行搜尋時，將滑鼠懸停在結果中的檔案/資料夾上，點擊**「排除」**。這會暫時將該路徑新增至設定中的 `search.exclude`。

---

👉 最常見的設定方式是：

* 在 `.gitignore` 中新增專案全域性的忽略規則
* 在 `search.exclude` 中新增編輯器專用的忽略規則（例如 `dist`, `.vscode`）

---

需要我示範如何**僅在搜尋時排除**檔案，但仍讓這些檔案顯示在檔案總管中？或是也要將它們從側邊欄的檔案總管中隱藏？
---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 在 IntelliJ IDEA 中排除檔案
translated: true
type: note
---

在 IntelliJ IDEA 中，您可以排除檔案或目錄，使其不會出現在搜尋、索引、程式碼自動完成或建置中。根據您的需求，有以下幾種方法可以實現：

---

### 1. 將目錄標記為 *已排除*

* 在 **專案視圖** 中，右鍵點擊要排除的資料夾。
* 選擇 **Mark Directory as → Excluded**。
* IDEA 將停止對其進行索引，因此它不會出現在搜尋、導航或程式碼分析中。

這通常用於建置輸出資料夾（如 `target/`、`out/`、`dist/` 等）。

---

### 2. 從版本控制中排除（VCS 忽略）

如果您不想讓 IDEA（和 Git）追蹤某些檔案：

* 在專案中建立或編輯 `.gitignore` 檔案。
* 在該檔案中加入目錄或檔案名稱模式。
* IDEA 會識別 `.gitignore` 並在 VCS 操作中隱藏它們。

---

### 3. 從程式碼分析／檢查中排除檔案

* 前往 **Settings → Editor → Inspections**。
* 在那裡您可以配置 **Scopes**，並將檢查僅分配給特定的檔案集，同時排除其他檔案。

---

### 4. 從建置中排除（Gradle/Maven）

如果您使用 Gradle 或 Maven，可以配置 `build.gradle` 或 `pom.xml` 以排除某些目錄（如生成的程式碼或資源）。IDEA 會遵循這些建置工具的配置。

---

### 5. 排除特定檔案類型

* 前往 **Settings → Editor → File Types**。
* 將模式（如 `*.log`、`*.tmp`）加入到 "Ignore files and folders" 清單中。

---

👉 快速提示：如果您的目標只是讓 IDEA 停止浪費資源索引大型資料夾（如 `node_modules/`），那麼 **Mark Directory as Excluded** 選項是最快且最有效的方法。

您是否還想了解如何在 IDEA 中將測試目錄（如 `src/test/java`）從 **程式碼覆蓋率** 運行中排除？
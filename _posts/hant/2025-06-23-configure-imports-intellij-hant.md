---
audio: false
generated: true
lang: hant
layout: post
title: 在 IntelliJ IDEA 中配置單類導入
translated: true
type: note
---

IntelliJ IDEA 提供了控制導入處理方式的設定，包括防止使用萬用字元。以下是設定始終使用單類別導入的方法：

1.  **開啟設定/偏好設定：**
    * **Windows/Linux：** `Ctrl + Alt + S`
    * **macOS：** `Cmd + ,` (逗號)

2.  **導航至 Java 程式碼風格設定：**
    * 在設定對話框的左側面板中，導航至：
        `Editor` -> `Code Style` -> `Java`

3.  **切換至「Imports」分頁：**
    * 在右側選擇 `Imports` 分頁。

4.  **設定導入選項：**
    您會看到幾個重要設定：

    * **`Use single class import`**：**勾選此核取方塊**。這是主要設定，會指示 IntelliJ 優先使用個別類別導入而非萬用字元導入。

    * **`Class count to use import with '*'`**：此設定決定當單一套件中有多少類別需要導入時，IntelliJ 會自動切換為萬用字元導入（例如 `java.util.*`）。為有效停用萬用字元導入，**請將此數值設為極高數字**，例如 `999` 或 `9999`。這能確保幾乎不會觸發萬用字元導入的閾值。

    * **`Names count to use static import with '*'`**：此設定與上述類似，但針對靜態導入。同樣請設定為高數值（例如 `999` 或 `9999`）以防止萬用字元靜態導入。

    * **`Packages to Use Imports with '*'`**：此表格列出 IntelliJ 會*始終*使用萬用字元導入的套件，無視其他設定。若想完全避免萬用字元導入，**請確保此表格為空白**。若看到如 `java.util.*` 或 `java.awt.*` 等條目，請將其移除。

5.  **套用變更：**
    * 點擊 `Apply` 然後 `OK` 儲存設定。

**完成這些設定後：**

* 當您使用「自動導入」功能時（例如透過 `Alt + Enter` 處理未解析的類別），IntelliJ 現在會插入個別類別導入而非萬用字元。
* 若現有檔案已包含萬用字元導入，您可使用「Optimize Imports」操作（Windows/Linux 按 `Ctrl + Alt + O`，macOS 按 `Cmd + Option + O`）將其根據新設定轉換為單類別導入。

透過以上步驟，您可有效防止 IntelliJ IDEA 在 Java 檔案中使用萬用字元導入。
---
audio: false
generated: true
lang: hant
layout: post
title: 修復 Jekyll YAML 與檔案錯誤
translated: true
type: note
---

您提供的輸出顯示了兩類錯誤：

1.  **YAML 異常：** 這表示您的 Markdown 檔案的前置資料（頂部的 YAML 區塊）存在問題：
      * `/Users/lzwjava/projects/lzwjava.github.io/notes/2025-06-25-company-valuation-comparison-en.md`
      * `/Users/lzwjava/projects/lzwjava.github.io/notes/2025-06-25-top-companies-evolve-en.md`
        錯誤訊息 "did not find expected key while parsing a block mapping at line 2 column 1" 表明這些檔案中的 YAML 語法不正確，很可能是在前置資料中缺少了某個鍵或存在縮排問題。

2.  **`Errno::ENOENT: No such file or directory @ rb_sysopen - /Users/lzwjava/projects/lzwjava.github.io/wandb/debug-internal.log`**：此錯誤表示 Jekyll 試圖存取一個不存在的檔案或目錄，具體是 `/wandb/debug-internal.log`。這可能是 Jekyll 嘗試處理的暫存檔案或來自其他工具（例如 Weights & Biases - `wandb`）的相依項目。

關於如何讓 Jekyll 忽略某些目錄，您可以在 `_config.yml` 檔案中使用 `exclude` 選項。

具體操作如下：

1.  **開啟您的 `_config.yml` 檔案**（位於 Jekyll 專案的根目錄）。

2.  **新增或修改 `exclude` 指令。** 此指令接受一個路徑（檔案或目錄）陣列，Jekyll 在建置過程中應忽略這些路徑。

    例如，要忽略 `wandb` 目錄以及任何其他您想排除的目錄，請將以下內容新增到您的 `_config.yml` 中：

    ```yaml
    exclude:
      - wandb/
      - some_other_directory/
      - another_file_to_ignore.md
    ```

    **重要注意事項：**

      * 請確保為目錄包含尾部斜線 (`/`)，以確保其內所有內容都被忽略。
      * 路徑是相對於您的 Jekyll 專案根目錄。

**針對您的特定錯誤使用 `exclude`：**

  * **對於 `wandb` 目錄錯誤：** 在 `_config.yml` 的 `exclude` 清單中加入 `wandb/` 應能防止 Jekyll 嘗試讀取其中的檔案，從而解決 `wandb/debug-internal.log` 的 `No such file or directory` 錯誤。

  * **對於 YAML 異常：** `exclude` 指令無法修正您 Markdown 檔案中的 YAML 錯誤。您需要**手動更正** `notes/2025-06-25-company-valuation-comparison-en.md` 和 `notes/2025-06-25-top-companies-evolve-en.md` 中的前置資料。

    **典型的 Jekyll 前置資料結構：**

    ```yaml
    ---
    layout: post
    title: "我的精彩文章"
    date: 2025-07-02 10:00:00 +0800
    categories: [notes, tech]
    tags: [jekyll, markdown]
    ---

    您的內容放在這裡。
    ```

    請仔細檢查 YAML 異常中提到的檔案，確保它們遵循此結構，特別是縮排和正確的鍵值對。錯誤 "did not find expected key while parsing a block mapping at line 2 column 1" 表明在您前置資料的開頭就有問題，可能是缺少鍵或在應該有鍵的地方多了一個空格。

在對 `_config.yml` 進行這些更改並修正您的 Markdown 檔案後，請再次嘗試執行您的 Jekyll 建置或服務命令。
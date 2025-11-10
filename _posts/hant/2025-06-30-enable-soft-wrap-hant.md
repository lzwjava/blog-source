---
audio: false
generated: true
lang: hant
layout: post
title: 在 Zed 中啟用軟換行
translated: true
type: note
---

Zed 與許多現代文字編輯器一樣，採用「軟換行」的概念來處理行尾換行。這意味著行內容會在編輯器內顯示為換行，但檔案中並不會實際插入換行字元。

以下是在 Zed 中啟用換行功能的方法：

1.  **開啟 Zed 設定：**

      * 按下 `Command + Shift + P`（macOS）或 `Ctrl + Shift + P`（Windows/Linux）開啟指令選擇區。
      * 輸入「local」並選擇「zed: Open Local Settings」。這將開啟你的 `settings.json` 檔案。

2.  **新增 `soft_wrap` 設定：**

      * 在你的 `settings.json` 檔案中，新增或修改 `"soft_wrap"` 設定。你有幾個選項：

          * **`"editor_width"`：** 這是最常用且通常建議的選項。它會根據當前編輯器視窗的寬度進行換行。
            ```json
            {
              "soft_wrap": "editor_width"
            }
            ```
          * **`"preferred_line_length"`：** 這會根據指定的 `preferred_line_length`（例如 80 個字元）進行換行。你還需要定義 `preferred_line_length`。
            ```json
            {
              "soft_wrap": "preferred_line_length",
              "preferred_line_length": 80
            }
            ```
          * **`"bounded"`：** 此選項提供更進階的換行行為，但對大多數使用者而言，`editor_width` 或 `preferred_line_length` 通常已足夠。
          * **`"none"`：** 此選項會停用換行功能。

3.  **儲存檔案：**

      * 按下 `Command + S`（macOS）或 `Ctrl + S`（Windows/Linux）儲存 `settings.json` 檔案。

現在 Zed 應該會根據你選擇的設定進行換行。

**重要注意事項：**

  * **專案層級設定：** 你也可以在專案層級啟用換行功能，方法是在你的專案目錄中建立一個 `.zed` 資料夾，並在其中放置一個帶有所需 `soft_wrap` 設定的 `settings.json` 檔案。這將針對該特定專案覆寫你的全域設定。
  * **語言特定設定：** 你甚至可以針對特定語言設定 `soft_wrap`。例如，要為 Markdown 檔案設定軟換行：
    ```json
    {
      "languages": {
        "Markdown": {
          "soft_wrap": "editor_width"
        }
      }
    }
    ```
  * **「重新換行」指令：** 如果你尋找的是「硬換行」文字（實際插入換行字元）而非僅視覺換行的指令，Zed 也提供「Rewrap」指令（通常綁定於 `Alt-Q` 或 `Alt-W`）。這對於格式化註解或長段落文字非常有用。
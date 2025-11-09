---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: CodeIgniter 表情符號輔助設定
translated: true
type: note
---

### 概述
這是一個來自 CodeIgniter 網頁框架的 PHP 設定檔，專門用於其**表情符號/笑臉輔助工具**。CodeIgniter 是一個用於構建網頁應用程式的 PHP MVC 框架。此檔案定義了一組笑臉/表情符號的映射關係，框架的 `smiley_helper` 會使用這些映射來自動將文字型表情符號（例如 `:-)`）替換為顯示對應 GIF 圖片的 HTML `<img>` 標籤。

該檔案透過 `defined('BASEPATH') OR exit('No direct script access allowed');` 來阻止直接存取，這是 CodeIgniter 中的一項安全措施，旨在防止未經授權的直接指令碼執行。

### 主要組成部分
- **目的**：將使用者生成內容（例如論壇貼文或評論）中的純文字表情符號轉換為視覺化圖片，以提供更好的使用者體驗。
- **資料結構**：`$smileys` 是一個 PHP 關聯陣列，其正式結構如下：
  ```
  $smileys = array(
      'smiley_code' => array('image_file', 'width', 'height', 'alt_text'),
      // ...
  );
  ```
  - **smiley_code**：要匹配的文字模式（例如 `:-)`、`:lol:`、`>:(`）。
  - **image_file**：笑臉目錄中 GIF 圖片的名稱（在 CodeIgniter 中預設為 `application/views/smileys/`）。
  - **width/height**：用於 `<img>` 標籤的尺寸（以像素為單位）（此處均為 `'19'`，表示 19x19px 的 GIF 圖片）。
  - **alt_text**：用於無障礙功能/螢幕閱讀器的替代文字，描述情感。

- **在 CodeIgniter 中的用法**：使用 `$this->load->helper('smiley');` 載入輔助工具，然後對包含表情符號代碼的字串呼叫像 `parse_smileys($text)` 這樣的函數。這會將代碼替換為 `<img>` 標籤，例如：
  - 輸入：`I'm happy :)`
    輸出：`I'm happy <img src="http://example.com/smileys/smile.gif" width="19" height="19" alt="smile">`

### 條目細分
該陣列包含 40 多個映射，按情感類型分組。大多數圖片是 19x19px 的 GIF。以下是摘要視圖（含範例）：

| 表情符號代碼 | 圖片 | 替代文字 | 備註 |
|---------------|-------|----------|-------|
| `:-)`, `:)` | grin.gif, smile.gif | grin, smile | 正面的露齒笑和微笑。 |
| `:lol:`, `:cheese:` | lol.gif, cheese.gif | LOL, cheese | 大笑/豎起大拇指，咧嘴笑。 |
| `;-)`, `;)` | wink.gif | wink | 眨眼。 |
| `:smirk:`, `:roll:` | smirk.gif, rolleyes.gif | smirk, rolleyes | 諷刺/智者點頭。 |
| `:-S`, `:wow:`, `:bug:` | confused.gif, surprise.gif, bigsurprise.gif | confused, surprised, big surprise | 困惑/驚訝。 |
| `:-P`, `%-P`, `;-P`, `:P` | tongue_laugh.gif, 等 | tongue laugh, 等 | 吐舌頭變體（大笑、眨眼、咂舌聲）。 |
| `:blank:`, `:long:`, `:ohh:`, `:grrr:`, `:gulp:`, `8-/` | 各種 | blank stare, long face, ohh, grrr, gulp, oh oh | 中性或惱怒的表情。 |
| `:down:`, `:red:`, `:sick:`, `:shut:` | 各種 | downer, red face, sick, shut eye | 悲傷、尷尬、生病。 |
| `:-/`, `>:(` (`:mad:`), `>:-(` (`:angry:`) | hmm.gif, mad.gif, angry.gif | hmmm, mad, angry | 困惑、生氣、憤怒。 |
| `:zip:`, `:kiss:` | zip.gif, kiss.gif | zipper, kiss | 拉上嘴巴拉鍊、親吻。 |
| `:ahhh:`, `:coolsmile:`, `-:coolsmirk:`, `:coolgrin:`, `:coolhmm:`, `:coolmad:`, `:coolcheese:` | shock.gif, shade_smile.gif, 等 | shock, cool smile, cool smirk, cool grin, cool hmm, cool mad, cool cheese | 震驚或「酷」/戴太陽鏡的變體。 |
| `:vampire:`, `:snake:` | vampire.gif, snake.gif | vampire, snake | 主題表情符號。 |
| `:exclaim:`, `:question:` | exclaim.gif, question.gif | exclaim, question | 標點符號等效項（!, ?）。 |

### 擴展與自訂
- **新增笑臉**：附加新條目，例如 `':fire:' => array('fire.gif', '19', '19', 'fire');`。
- **變更圖片**：如果將 GIF 替換為 PNG/JPG，請更新檔案名稱（並相應調整寬度/高度）。
- **目錄**：確保圖片存在於 CodeIgniter 的笑臉路徑中。
- **限制**：這裡的所有圖片尺寸都相同；實際實現可能有所不同。此陣列僅定義映射——替換邏輯在輔助工具本身中。

如果您有關於在 CodeIgniter 中自訂或使用此功能的具體問題，請提供更多詳細資訊！
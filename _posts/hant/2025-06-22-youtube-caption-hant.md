---
audio: false
generated: true
lang: hant
layout: post
title: YouTube 影片字幕擷取方法
translated: true
type: note
---

要取得 YouTube 影片的所有字幕，請根據你的需求以及是否想使用手動或自動化方法，遵循以下步驟。請注意，影片必須提供字幕（可以是自動生成或由創作者上傳）。

### 手動方法（使用 YouTube 內建文字記錄功能）
1. **開啟影片**：在網頁瀏覽器中前往 YouTube 並導航至目標影片。
2. **檢查字幕**：點擊影片暫停播放。查看播放器右下角是否有「CC」（隱藏式字幕）圖示。如果可見，表示字幕可用。
3. **存取文字記錄**：
   - 向下滾動至影片描述，點擊「顯示更多」。
   - 找到並點擊「顯示文字記錄」（如果可用）。這會在影片右側開啟帶有時間戳記和文字的文字記錄面板。
4. **切換時間戳記**：點擊文字記錄面板右上角的三個垂直點，選擇「切換時間戳記」以根據你的偏好顯示或隱藏時間戳記。
5. **複製文字記錄**：
   - 滾動至文字記錄底部，在最後一個字後點擊並按住，然後拖曳至頂部以反白所有文字。
   - 按 `Ctrl + C`（Windows）或 `Command + C`（Mac）進行複製。
6. **貼上並儲存**：開啟文字編輯器（例如 Notepad、TextEdit 或 Word），使用 `Ctrl + V` 或 `Command + V` 貼上文字，並儲存為 `.txt` 檔案或你偏好的格式。

**注意**：此方法僅適用於 YouTube 網站，不適用於行動應用程式。[](https://www.wikihow.com/Download-YouTube-Video-Subtitles)

### 適用於內容創作者（從你自己的影片下載字幕）
如果你擁有影片，可以直接從 YouTube Studio 下載字幕：
1. **登入 YouTube Studio**：前往 [studio.youtube.com](https://studio.youtube.com)。
2. **選擇影片**：點擊左側選單中的「內容」，然後選擇影片。
3. **存取字幕**：點擊左側選單中的「字幕」，然後選擇語言。
4. **下載字幕**：點擊字幕軌旁的三點選單，選擇「下載」。選擇格式如 `.srt`、`.vtt` 或 `.sbv`。
5. **編輯或使用**：在文字編輯器或字幕編輯器（例如 Aegisub）中開啟下載的檔案以供進一步使用。

**注意**：你只能下載你管理頻道中影片的字幕檔案。[](https://ito-engineering.screenstepslive.com/s/ito_fase/a/1639680-how-do-i-download-a-caption-file-from-youtube)

### 自動化方法（使用第三方工具）
如果你需要特定格式（例如 `.srt`）的字幕，或適用於非你擁有的影片，請使用信譽良好的第三方工具：
1. **選擇工具**：熱門選項包括：
   - **DownSub**：免費線上字幕下載工具。
   - **Notta**：提供高準確度的轉錄和字幕下載。[](https://www.notta.ai/en/blog/download-subtitles-from-youtube)
   - **4K Download**：用於字幕提取的桌面應用程式。[](https://verbit.ai/captioning/a-guide-to-downloading-subtitles-and-captions-from-youtube-enhancing-accessibility-and-user-experience/)
2. **複製影片 URL**：開啟 YouTube 影片，點擊影片下方的「分享」，並複製 URL。
3. **使用工具**：
   - 將 URL 貼上至工具的輸入欄位。
   - 選擇所需的語言和格式（例如 `.srt`、`.txt`）。
   - 點擊「下載」或「提取」並儲存檔案。
4. **驗證**：開啟檔案以確保準確性，因為自動生成的字幕可能包含錯誤。

**注意**：使用可信工具以避免安全風險。部分工具可能包含廣告或需要付費才能使用進階功能。[](https://gotranscript.com/blog/how-to-download-subtitles-from-youtube)

### 使用 YouTube API（適用於開發者）
如需批量提取字幕或應用程式整合，請使用 YouTube Data API：
1. **設定 API 存取**：在 [Google Cloud Console](https://console.cloud.google.com) 中建立專案，啟用 YouTube Data API v3，並取得 API 金鑰。
2. **列出字幕軌**：使用 `captions.list` 端點檢索影片的可用字幕軌。範例：
   ```
   GET https://www.googleapis.com/youtube/v3/captions?part=snippet&videoId=VIDEO_ID&key=API_KEY
   ```
3. **下載字幕**：使用 `captions.download` 端點取得特定字幕軌。範例：
   ```
   GET https://www.googleapis.com/youtube/v3/captions/CAPTION_ID?tfmt=srt&key=API_KEY
   ```
4. **限制**：
   - 你只能下載自己影片的字幕，除非影片擁有者已將其公開。
   - API 使用有配額限制（每次字幕下載約 200 單位）。[](https://developers.google.com/youtube/v3/docs/captions)[](https://stackoverflow.com/questions/73863672/how-can-i-get-captions-of-a-youtube-video-and-display-it-separately)
5. **替代方案**：部分開發者從影片頁面原始碼中爬取定時文字 URL（例如 `https://www.youtube.com/api/timedtext?...`），但這種方法不可靠，可能違反 YouTube 服務條款，並有 IP 被封鎖的風險。[](https://stackoverflow.com/questions/73863672/how-can-i-get-captions-of-a-youtube-video-and-display-it-separately)

### 額外提示
- **語言選擇**：如果字幕提供多種語言，請從「字幕/CC」設定或文字記錄的下拉選單中選擇你偏好的語言。[](https://riverside.fm/blog/youtube-transcription)
- **自動生成字幕**：由於口音、背景噪音或複雜音訊，這些字幕可能包含錯誤。如果準確性至關重要，請審核並編輯。[](https://support.google.com/youtube/answer/6373554?hl=en)
- **無障礙存取**：字幕為聽障或聽力受損的觀眾增強了無障礙存取，並透過使內容可搜尋來改善 SEO。[](https://www.descript.com/blog/article/transcript-of-youtube-videos)
- **沒有可用字幕？**：如果影片缺乏字幕，考慮使用轉錄服務如 Rev 或 Notta 從音訊生成文字記錄。[](https://www.rev.com/resources/how-to-download-youtube-subtitles-as-text-files)[](https://www.notta.ai/en/blog/download-subtitles-from-youtube)

### 限制
- 並非所有影片都有字幕，特別是當創作者停用它們或 YouTube 的自動字幕生成不支援該語言或音訊品質時。[](https://support.google.com/youtube/answer/6373554?hl=en)
- YouTube 行動應用程式不支援檢視文字記錄，但你可以透過「CC」按鈕啟用字幕。[](https://riverside.fm/blog/youtube-transcription)
- 部分第三方工具或 API 方法可能不適用於自動生成的字幕或受限制的影片。[](https://stackoverflow.com/questions/9611397/how-to-extract-closed-caption-transcript-from-youtube-video)

如果你需要特定影片的字幕或特定格式，請告訴我，我可以進一步指導你！
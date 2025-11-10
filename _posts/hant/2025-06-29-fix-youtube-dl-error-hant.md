---
audio: false
generated: true
lang: hant
layout: post
title: 修復 YouTube-dl 機器人驗證錯誤
translated: true
type: note
---

youtube-dl 出現的「請登入以確認您不是自動程式」錯誤，通常是由於 YouTube 封鎖請求所致，原因可能包括 IP 限制、VPN 使用或缺乏身份驗證。以下是解決步驟，從最簡單的方案開始：

1. **更新 youtube-dl**：
   - 此錯誤可能源自 youtube-dl 版本過舊，因為 YouTube 經常更新其系統。請執行以下指令更新至最新版本：
     ```bash
     sudo youtube-dl -U
     ```
     若透過 pip 安裝，則使用：
     ```bash
     pip install --upgrade youtube-dl
     ```
   - 更新後，請重新執行指令：
     ```bash
     youtube-dl https://www.youtube.com/watch?v=st3mUEub99E
     ```

2. **改用 yt-dlp（推薦替代方案）**：
   - youtube-dl 已停止活躍維護，而其分支 yt-dlp 對 YouTube 近期變更的相容性更佳。安裝 yt-dlp：
     ```bash
     sudo pip install yt-dlp
     ```
     接著使用：
     ```bash
     yt-dlp https://www.youtube.com/watch?v=st3mUEub99E
     ```
   - yt-dlp 能更有效處理身份驗證與 IP 限制。[](https://stackoverflow.com/questions/79049216/yt-dlp-error-sign-in-required-when-downloading-youtube-video)

3. **停用 VPN 或更換伺服器**：
   - 若您使用 VPN，YouTube 可能將您的 IP 標記為可疑。嘗試停用 VPN 或切換至其他伺服器：
     ```bash
     yt-dlp https://www.youtube.com/watch?v=st3mUEub99E
     ```
   - 據用戶回報，斷開 VPN 或更換伺服器後問題即獲解決。[](https://www.reddit.com/r/youtubedl/comments/1e6bzu4/ytdlp_error_sign_in_to_confirm_youre_not_a_bot/)[](https://www.reddit.com/r/youtubedl/comments/1i48cey/you_tube_ytdlp_sign_in_to_confirm_youre_not_a_bot/?tl=en)

4. **使用 Cookies 進行身份驗證**：
   - YouTube 可能要求驗證以跳過程式檢查。請從已登入 YouTube 的瀏覽器匯出 cookies：
     - 安裝瀏覽器擴充功能（如 Firefox 或 Chrome 的「Export Cookies」）。
     - 登入 YouTube 後，將 cookies 匯出為 `cookies.txt` 檔案，並透過以下指令使用：
       ```bash
       youtube-dl --cookies ~/path/to/cookies.txt https://www.youtube.com/watch?v=st3mUEub99E
       ```
       或使用 yt-dlp：
       ```bash
       yt-dlp --cookies ~/path/to/cookies.txt https://www.youtube.com/watch?v=st3mUEub99E
       ```
     - 亦可使用 `--cookies-from-browser firefox`（或將 `firefox` 替換為 `chrome`、`edge` 等）自動擷取 cookies：
       ```bash
       yt-dlp --cookies-from-browser firefox https://www.youtube.com/watch?v=st3mUEub99E
       ```
     - 注意：為避免帳號遭標記，請盡量避免使用主要 Google 帳號，可改用一次性帳號。[](https://stackoverflow.com/questions/79049216/yt-dlp-error-sign-in-required-when-downloading-youtube-video)[](https://www.reddit.com/r/youtubedl/comments/1e6bzu4/ytdlp_error_sign_in_to_confirm_youre_not_a_bot/)[](https://www.reddit.com/r/youtubedl/comments/1i48cey/you_tube_ytdlp_sign_in_to_confirm_youre_not_a_bot/?tl=en)

5. **使用代理伺服器**：
   - 若問題持續，您的 IP 可能遭封鎖（例如使用資料中心 IP）。可嘗試透過住宅代理伺服器隱藏 IP：
     ```bash
     youtube-dl --proxy "http://proxy_address:port" https://www.youtube.com/watch?v=st3mUEub99E
     ```
     或使用 yt-dlp：
     ```bash
     yt-dlp --proxy "http://proxy_address:port" https://www.youtube.com/watch?v=st3mUEub99E
     ```
   - 住宅代理伺服器被標記的機率低於資料中心代理。[](https://apify.com/epctex/youtube-video-downloader/issues/sign-in-to-confirm-y-1hjZd7SOtg8iLxyvN)

6. **清除快取或嘗試不同網路**：
   - 若您近期清理過日誌或暫存檔，請確認 youtube-dl/yt-dlp 未依賴損毀的快取。清除快取：
     ```bash
     rm -rf ~/.cache/youtube-dl
     rm -rf ~/.cache/yt-dlp
     ```
   - 切換至其他網路（如行動熱點）測試是否為 IP 相關問題。[](https://forum.dvdfab.cn/forum/streamfab-support/streamfab/455389-sign-in-to-confirm-you-re-not-a-bot-help-please-with-yt-downloader)

7. **透過詳細輸出進行除錯**：
   - 若以上步驟皆無效，請執行含詳細輸出的指令以進一步診斷：
     ```bash
     youtube-dl -v https://www.youtube.com/watch?v=st3mUEub99E
     ```
     或使用 yt-dlp：
     ```bash
     yt-dlp -v https://www.youtube.com/watch?v=st3mUEub99E
     ```
   - 可將輸出內容分享至相關論壇（如 yt-dlp 的 GitHub issues）尋求社群協助。[](https://github.com/yt-dlp/yt-dlp/issues/10128)

**注意事項**：
- YouTube 的程式偵測機制日趨嚴格，常針對資料中心 IP 或未驗證請求。[](https://github.com/jagrosh/MusicBot/issues/1588)
- 使用 cookies 有少量帳號標記風險，建議使用次要帳號。[](https://stackoverflow.com/questions/79049216/yt-dlp-error-sign-in-required-when-downloading-youtube-video)
- 若影片為私人或受限內容，使用 cookies 前請確認帳號具存取權限。[](https://askubuntu.com/questions/776122/how-to-resolve-sign-in-error-when-using-youtube-dl-for-downloading-my-personal)
- 若所有方法均無效，可考慮使用替代前端如 Invidious 或 NewPipe，但這些工具可能有限制。[](https://www.reddit.com/r/youtubedl/comments/1ihxrjm/getting_error_sign_in_to_confirm_youre_not_a_bot/)

請依序嘗試上述步驟，建議優先從更新或切換至 yt-dlp 開始，這是最可能解決問題的方法。若問題仍然存在，請提供詳細輸出或具體細節（如 VPN 使用情況、作業系統）。
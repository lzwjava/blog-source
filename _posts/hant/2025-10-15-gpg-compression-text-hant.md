---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: GPG 壓縮縮小文字檔案
translated: true
type: note
---

### 為什麼加密的 SRT 檔案體積會減半
像 `.srt` 這樣的字幕檔案是純文字格式（例如時間軸和對白行），內容存在大量重複和冗餘——非常適合壓縮。GPG 的預設設定會在加密*之前*使用 zlib（類似 ZIP 的演算法）壓縮資料，從而消除冗餘。你原本 136K 的檔案縮減至 54K（約減少 60%），這對於文字密集的 SRT 檔案來說十分典型。

- **原始檔案**：136 KB（未壓縮文字）。
- **加密後**：54 KB（壓縮後加密）。
- **壓縮比**：約原始大小的 40%——與影片相比節省了大量空間，因為影片壓縮效果有限。

這與你的 MP4 經驗相反：影片本身已預先壓縮（H.264），因此 GPG 難以進一步縮減體積。但文字檔案？壓縮效果立竿見影。

若想進一步縮小體積（或驗證效果），可將其解密回原狀：
```
gpg --decrypt 'The Shawshank Redemption 1994.720p.BRRip.x264.YIFY.srt.gpg' > test.srt
ls -lh test.srt  # 應與原始大小相符
```
隨後刪除測試檔案。GPG 的壓縮等級固定為 6（在速度與體積間取得平衡），若需極致壓縮，需先使用自訂工具如 `gzip -9` 進行處理。

[GPG 對文字檔案的壓縮機制](https://www.gnupg.org/documentation/manuals/gnupg/Encrypting-and-Decrypting.html#compress-options)  
[SRT 檔案壓縮效果優異的原因](https://superuser.com/questions/123456/why-do-text-files-compress-better-than-binary)
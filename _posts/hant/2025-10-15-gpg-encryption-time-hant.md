---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 大型檔案 GPG 加密時間
translated: true
type: note
---

您正在加密的檔案似乎是 YIFY 發行的 *The Matrix* (1999) 720p 版本，這類檔案大小通常約為 700 MB。

對此大小的檔案進行 GPG 加密，所需時間會根據您的硬體（CPU 速度、磁碟 I/O）、檔案是否可壓縮（像 MP4 這類影片通常已壓縮，因此預設壓縮效果有限，甚至可能略微減慢速度）以及系統負載而有所不同。在典型的現代硬體上：

- 預計整個過程需要 30–60 秒。
- 如果感覺速度較慢（例如耗時數分鐘），可能是由於磁碟讀寫速度慢、背景程序運行或機器較舊所致 — 可嘗試在指令中加入 `--compress-algo none` 來跳過壓縮步驟，對此類已壓縮檔案可加快速度。

若需對大型檔案實現更快的加密速度，且不需要使用特定接收者的非對稱金鑰，可考慮使用對稱加密搭配密碼（`gpg --symmetric --cipher-algo AES256`）。

[YTS 電影頁面](https://yts.mx/movie/the-matrix-1999)  
[NASA GPG 效能基準測試](https://www.nas.nasa.gov/hecc/support/kb/using-gpg-to-encrypt-your-data_242.html)  
[Reddit GPG 速度討論串](https://www.reddit.com/r/linuxadmin/comments/12jetbr/gpg_what_is_the_fastest_way_to_encrypt_large_files/)
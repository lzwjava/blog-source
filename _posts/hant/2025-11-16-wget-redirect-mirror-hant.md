---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 從 Mirror.accum.se 的正常 Wget 重新導向
translated: true
type: note
---

您的 `wget` 指令正在存取 `https://mirror.accum.se/mirror/wikimedia.org/dumps/...` 並收到 **302 重新導向** 至 `https://laotzu.ftp.acc.umu.se/...`。這對於 **accum.se** 鏡像站來說是完全正常且預期的行為 —— 以下是原因說明：

### 重新導向發生的原因
`mirror.accum.se` 只是一個由瑞典于默奧大學學術電腦俱樂部 (ACC) 運行的 **重新導向器 / 負載平衡器**。  
它本身 **並不** 儲存檔案，而是：

- 根據您 IP 的地理位置（或有時根據負載）
- 自動將您重新導向至其鏡像伺服器群組中最快/最近的實際儲存伺服器
- 在您的情況中，它選擇了 `laotzu.ftp.acc.umu.se`（這是擁有資料的真實 FTP/HTTP 伺服器）

這是他們多年來使用的相同系統。您可能會被重新導向至的其他常見主機名稱包括：

- `issac.ftp.acc.umu.se`
- `laotzu.ftp.acc.umu.se`（您遇到的那個）
- `morpork.ftp.acc.umu.se`
- 等等

因此，即使您在腳本中寫入 `mirror.accum.se`，您幾乎總是會從其中一個 `*.ftp.acc.umu.se` 後端伺服器下載。

### 為何第一個檔案顯示「206 Partial Content」
因為您（或某人/某個腳本）之前已經開始下載該相同檔案，`wget -c` 檢測到本地的部分檔案並發送了 `Range` 請求。伺服器正確地恢復了下載 → 206 Partial Content。這是好事！

### 有問題嗎？
沒有。一切運作正常。

- 重新導向是正常且無害的
- 最終的伺服器 (`laotzu.ftp.acc.umu.se`) 仍然是官方的 ACC/Wikimedia 鏡像站
- 無論您被重新導向至哪個後端伺服器，校驗碼都會相同

### 如果您想避免重新導向（可選）
您可以完全跳過重新導向器，直接指向其中一個真實主機，例如：

```bash
# 這三個主機在 mirror.accum.se 背後本來就是輪流使用的
wget -c https://laotzu.ftp.acc.umu.se/mirror/wikimedia.org/dumps/enwiki/20251101/...
# 或
wget -c https://issac.ftp.acc.umu.se/mirror/wikimedia.org/dumps/enwiki/20251101/...
```

但大多數人仍然使用 `mirror.accum.se`，因為重新導向器會自動為您選擇最佳選項。

### 簡而言之
您的腳本沒問題。從 `mirror.accum.se` → `laotzu.ftp.acc.umu.se` 的 302 重新導向是該鏡像站的正常、預期行為。沒有任何問題，您下載的仍然是正版的 Wikimedia 資料庫備份。請繼續使用 `mirror.accum.se` —— 它是全球最快、最可靠的鏡像站之一。
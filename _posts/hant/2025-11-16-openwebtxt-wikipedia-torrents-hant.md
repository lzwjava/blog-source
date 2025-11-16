---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: OpenWebText 及維基百科數據集種子
translated: true
type: note
---

### OpenWebText 數據集種子檔案

OpenWebText 是 OpenAI WebText 數據集的開源複製版本，包含從高評分 Reddit 連結中提取的約 38GB 清理文本（主要經過質量篩選的網頁抓取內容）。這是用於訓練語言模型的熱門大規模文本語料庫。雖然完整抓取文本並非總是以單一種子檔案形式提供，以下是可靠選項：

- **網址清單（已篩選，約 480MB）**：用於抓取 OpenWebText 的預篩選網址清單，包含約 2600 萬個網址。您可使用此清單自行下載和處理文本。
  - 種子檔案：[OpenWebText-urls-26M-filtered.xz](https://academictorrents.com/details/f5161721b322bca66ed74da32b963c1066e64312)
  - 來源：Academic Torrents（由社群做種）。

- **網址清單（完整版，約 1.75GB）**：來自 Reddit 提交內容的完整去重網址清單。
  - 種子檔案：[WebText dataset urls.txt.tar.gz](https://academictorrents.com/details/15f3494b2991e75194d3af72bf7afa5025a7abc3)
  - 來源：Academic Torrents（由社群做種）。

- **分詞處理版本（約 16GB）**：來自抓取語料庫的 GPT-2 分詞文本檔案（395 個檔案，可直接用於模型訓練）。
  - 種子檔案：[OpenWebText (Gokaslan's distribution, 2019), GPT-2 Tokenized](https://academictorrents.com/details/36c39b25657ce1639ccec0a91cf242b42e1f01db)
  - 來源：Academic Torrents（由 OSUOSL 和社群做種）。

如需完整原始文本語料庫，請查閱官方網站以獲取直接下載連結（非種子方式），或使用上述網址配合 [OpenWebText GitHub 存儲庫](https://github.com/eukaryote31/openwebtext)中的抓取腳本。增強版本 OpenWebText2（約數 TB 規模）可透過 [EleutherAI 的存儲庫](https://github.com/EleutherAI/openwebtext2)獲取，但採用串流方式而非種子傳輸。

### 維基百科備份種子檔案

維基百科備份是每月匯出的完整數據庫 XML 檔案（包含文章、修訂記錄、元數據）。英文版本體積龐大（摘要壓縮檔約 20-25GB，完整歷史記錄可達 100+GB）。種子檔案由社群維護（非官方但經官方校驗碼驗證），並透過維基媒體伺服器進行網路做種以確保可靠性。請務必根據 [dumps.wikimedia.org](https://dumps.wikimedia.org/enwiki/latest/) 的哈希值驗證下載內容。

種子檔案的主要集散地是 [Meta-Wiki 數據備份種子頁面](https://meta.wikimedia.org/wiki/Data_dump_torrents#enwiki)，其中列出最新的英文維基百科備份（例如 enwiki-20251101）。以下是近期備份摘要：

| 備份日期 | 檔案類型 | 壓縮後大小 | 種子連結 | 備註 |
|-----------|-----------|-----------------|--------------|-------|
| 2025-11-01 | 頁面-文章（XML，僅摘要） | ~22GB | [enwiki-20251101-pages-articles-multistream.xml.bz2](https://meta.wikimedia.org/wiki/Data_dump_torrents#enwiki) | 多流格式；最便於文本提取 |
| 2025-11-01 | 頁面-文章-歷史（XML，完整修訂記錄） | ~120GB | [enwiki-20251101-pages-meta-history*.xml.bz2](https://meta.wikimedia.org/wiki/Data_dump_torrents#enwiki) | 包含所有編輯記錄；分拆成多個流以便處理 |
| 2025-10-01 | 頁面-文章（XML，僅摘要） | ~21GB | [enwiki-20251001-pages-articles-multistream.xml.bz2](https://meta.wikimedia.org/wiki/Data_dump_torrents#enwiki) | 前月備份；適合用於歷史比較 |

- **完整收藏集**：可在 [Academic Torrents 維基百科收藏集](https://academictorrents.com/collection/wikipedia) 瀏覽所有歷史英文維基百科種子檔案（包含最早可追溯至 2010 年的舊備份）。
- **Kiwix ZIM 格式**：若需要可離線瀏覽的維基百科（HTML 格式，約 100GB），可嘗試 [wikipedia_en_all_maxi_2024-01.zim.torrent](https://download.kiwix.org/zim/wikipedia/wikipedia_en_all_maxi_2024-01.zim.torrent) – 由社群做種，但請查閱 [Kiwix 下載頁面](https://download.kiwix.org/zim/wikipedia/) 以獲取 2025 年更新版本。

要將這些檔案處理成純文本，請使用 Python 的 `wikiextractor` 等工具。種子傳輸能減輕伺服器負載並支援斷點續傳 – 建議使用 qBittorrent 等用戶端軟體。如需其他語言或子集的備份，Meta-Wiki 頁面提供篩選功能。
---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 英文維基百科下載指南
translated: true
type: note
---

這是來自官方維基媒體下載鏡像站（通常是 https://dumps.wikimedia.org/enwiki/latest/）的目錄列表。  
當中包含了截至2025年11月初，你可以下載當前英文維基百科文章的所有不同方式。

### 主要格式及其實際內容

| 檔案名稱模式 | 內容說明 | 近似大小（未壓縮） | 最適合訓練LLM？ | 備註 |
| --- | --- | --- | --- | --- |
| `enwiki-latest-pages-articles.xml.bz2` | 單一巨型檔案，包含**所有**文章 + 討論頁、模板、重新導向頁等 | ~85–90 GB 未壓縮 | 是，非常常用 | 若你有足夠空間和頻寬，這是最簡單的選擇 |
| `enwiki-latest-pages-articles1.xml-p1p41242.bz2`  … 直至 … `enwiki-latest-pages-articles27.xml-…` | 相同數據，但分割成27個較小區塊（多重串流） | 每個壓縮檔約200–600 MB → 未壓縮總量仍為~85–90 GB | 是，最受歡迎的選擇 | 可並行下載且易於續傳 |
| `enwiki-latest-pages-articles-multistreamX.xml.bz2`（例如 multistream27） | 屬於上述分割版本的實際大型壓縮數據檔案 | 每個壓縮檔300–600 MB | 這些才是你需要的真實數據檔案 | 你需要這些 + 索引檔案 |
| `enwiki-latest-pages-articles-multistreamX.xml.bz2.md5` / `.meta` | 校驗和及小型元數據檔案 | < 1 KB | 文字處理不需要 | 僅用於驗證下載 |
| `enwiki-latest-pages-articles-multistream-indexX.xml.bz2` | 索引檔案，標明每篇文章在大型多重串流檔案中的位元組偏移量 | 每個壓縮檔~30–60 MB | 若使用多重串流則必需 | 快速隨機存取所需；大多數處理腳本都需要它們 |

### 推薦：2025年訓練模型時幾乎所有人使用的方式

事實上的標準方式（被LLaMA、Mistral、Qwen、DeepSeek、Gemma、Phi等使用）是：

下載**27個多重串流檔案 + 它們的27個索引檔案**  
（即所有以 `enwiki-latest-pages-articlesXX.xml-p…p….bz2` 開頭及對應的 `…-indexXX…bz2` 檔案）

或者更簡單：若你的連線和硬碟能夠處理，直接下載**單一巨型檔案**：

```
enwiki-latest-pages-articles.xml.bz2    ← 壓縮後24.6 GB，未壓縮~85–90 GB
```

兩者包含完全相同的原始XML數據（所有主命名空間文章 + 大量額外頁面）。

### 為何不選用小型檔案（multistream3.xml-p…、multistream4.xml-p… 等）？
那些是2010–2015年間的舊分割檔，僅包含維基百科的極小部分（當時剛好落在該頁面ID範圍內的文章）。它們僅因歷史原因保留，現今基本上已無用處。

### 快速開始指令（2025年傾印檔）

並行下載推薦的27+27個檔案（最快）：

```bash
# 取得檔案列表
wget -q https://dumps.wikimedia.org/enwiki/latest/ -O - | \
  grep -E 'enwiki-latest-pages-articles[0-9]+[02468]\.xml-p[0-9]+p[0-9]+\.bz2"' | \
  sed -e 's/.*href="//' -e 's/".*//' | \
  xargs -n1 -P10 wget https://dumps.wikimedia.org/enwiki/latest/

# 同時下載對應的索引檔案
wget -q https://dumps.wikimedia.org/enwiki/latest/ -O - | \
  grep -E 'enwiki-latest-pages-articles-multistream-index' | \
  sed -e 's/.*href="//' -e 's/".*//' | \
  xargs -n1 -P10 wget https://dumps.wikimedia.org/enwiki/latest/
```

或僅下載單一檔案（最簡單）：

```bash
wget https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2
```

之後你通常會使用以下工具進行處理：
- wikiextractor (Python) → 清理文字
- Hugging Face `datasets` 的維基百科加載器（已為你完成所有步驟）
- DeepSeek 或 EleutherAI 的處理腳本等

簡而言之：  
下載單一的24 GB檔案 `enwiki-latest-pages-articles.xml.bz2` 或27個分割檔案 + 索引。列表中的其他內容若非校驗和、舊有廢棄資料，就是你訓練時不需要的元數據。
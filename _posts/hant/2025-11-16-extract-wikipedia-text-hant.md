---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 從維基百科數據庫提取文本
translated: true
type: note
---

以下是從維基百科 `.bz2` 備份檔案（例如你的 `enwiki-latest-pages-articles1.xml-p1p41242.bz2`）中提取純文字最常見且有效的方法。

### 推薦工具與方法（從最簡單到最高效）

#### 1. 使用 wikiextractor（適合大多數人 – 快速且乾淨）
這是 NLP/ML 領域幾乎人人使用的標準工具，用於處理維基百科備份檔案。

```bash
# 安裝（只需一次）
pip install wikiextractor

# 提取文字（移除模板、表格等，提供每篇文章的乾淨文字）
wikiextractor enwiki-latest-pages-articles1.xml-p1p41242.bz2 --output wiki_text
```

- 輸出：建立一個 `wiki_text/` 資料夾，內含子資料夾 AA、AB 等，包含乾淨 JSON/文字的 `.bz2` 檔案。
- 若要取得純文字（每篇文章一行）：
```bash
wikiextractor enwiki-latest-pages-articles1.xml-p1p41242.bz2 --processes 8 -o wiki_text --json
# 然後如有需要，將 JSON 轉換為純文字
find wiki_text -name '*' -exec cat {} \; | grep '"text":' | sed 's/.*"text": "//;s/"$//' > all_text.txt
```

#### 2. 使用 gensim 的 WikiCorpus（如果你在 Python 中進行 NLP 處理，這工具很棒）

```python
from gensim.corpora import WikiCorpus

# 這會自動處理 .bz2 並提取文字 + 分詞
wiki = WikiCorpus("enwiki-latest-pages-articles1.xml-p1p41242.bz2", dictionary=False)

# 遍歷文章
with open("output.txt", "w", encoding="utf-8") as f:
    for i, text in enumerate(wiki.get_texts()):
        f.write(" ".join(text) + "\n")
        if i % 10000 == 0:
            print(f"Processed {i} articles")
```

#### 3. 簡單的 bzip2 + grep/awk（快速但粗糙，不進行清理）

```bash
# 僅解壓縮並查看原始 XML
bzip2 -dc enwiki-latest-pages-articles1.xml-p1p41242.bz2 | less

# 僅提取 <text> 內容（非常粗略，保留 wiki 標記）
bzip2 -dc enwiki-latest-pages-articles1.xml-p1p41242.bz2 | \
  sed -n '/<text /,/<\/text>/p' | \
  sed 's/<text[^>]*>//g;s/<\/text>//g' > raw_text_with_markup.txt
```

#### 4. 如果你有完整備份檔案且希望快速處理（並行處理）
你的檔案只是第一個區塊 (p1p41242)，但如果你之後有所有約 30+ 個區塊：

```bash
# 並行提取所有檔案
ls *.bz2 | xargs -P 8 -I {} wikiextractor {} --output wiki_extracted
```

### 總結 – 我目前給你的建議：

```bash
pip install wikiextractor
wikiextractor enwiki-latest-pages-articles1.xml-p1p41242.bz2 -o extracted_wiki --bytes 1M --json
```

這將在幾分鐘內為你提供乾淨、可讀的文章（你的檔案僅約 2-3 GB 壓縮，因此非常易於處理）。

如果你需要以下任何一項，請告訴我：
- 僅主要命名空間（真實文章，非討論頁面）
- 純文字而非 JSON
- 分詞輸出
- 改為中文維基百科 (zhwiki) – 處理過程完全相同

祝你提取順利！🚀
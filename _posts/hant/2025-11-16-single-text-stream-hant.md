---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 單一拼接文本流的訓練
translated: true
type: note
---

在 nanoGPT（以及基本上任何 GPT 風格的訓練中，包括原始的 GPT-2/GPT-3 訓練）中，**你必須在一個單一的巨型串聯文字流上進行訓練**，而不是逐篇輸入獨立文章/文件作為單獨序列。

以下是原因以及在 FineWeb（以及 Andrej 的 nanoGPT 代碼中）實際執行的方式：

### 你應該做的（正確方式）
1. 將**所有**獨立文章串聯成**一個巨大的 .txt 文件**（或多個大型分片文件），僅用特殊的文本結束標記 `<|endoftext|>`（或你選擇的任何分隔符）分隔。
2. 在訓練期間，nanoGPT 將會：
   - 將整個串聯文字載入到一個巨大的 token 陣列中。
   - 將其分割成固定長度的區塊（例如，block_size = 1024 tokens）。
   - 這些區塊經常跨越文件邊界 — 這不僅可以接受，而且是理想的。

這正是 OpenAI 訓練 GPT-2 和 GPT-3 的方式，也是 Andrej 在 Shakespeare、OpenWebText、FineWeb-Edu 等數據集上使用的方法。

### extract_fineweb.py 腳本正在做什麼
你運行的那個腳本已經在做正確的事情：

```bash
$ python ./scripts/train/extract_fineweb.py
```

它讀取所有 parquet 文件，提取每行（即每個網頁/文章）的 `text` 欄位，將原始文字一個接一個地寫入 `fineweb_extracted.txt`，並且（在最新版本中）自動在文件之間插入 `<|endoftext|>` 分隔符。

因此，生成的文件看起來像：

```
<文章 1 文字> <|endoftext|> <文章 2 文字> <|endoftext|> <文章 3 文字> <|endoftext|> ...
```

這很完美。你應該在那個單一巨型文件上進行訓練（或者使用 `train.py` 從中創建的分片 bin 文件）。

### 你不應該做的
- **不要**將每篇文章作為單獨的示例/序列提供給模型，並為每篇文章重新開始注意力機制。
- **不要**將每篇文章截斷或填充至確切的 block_size，並僅在文件內進行訓練。
- **不要**使用文件級別批次處理，其中批次中的每個序列是一個完整的文件。

這會破壞模型學習跨越多個文件的長距離依賴關係的能力，並會嚴重損害性能。

### 總結
是的 → 在**一個單一的大型串聯文字文件**上訓練（正是 `extract_fineweb.py` 生成的內容）。  
不 → **不要**逐篇作為單獨序列進行訓練。

這就是 GPT 一直以來的訓練方式，也是 nanoGPT 的 `train.py` 僅將數據視為一個長 token 流的原因。

所以，只需繼續正常的 nanoGPT 工作流程：

```bash
python scripts/train/extract_fineweb.py   # 你已經完成了這一步
python train.py --dataset=your_extracted_file_or_fineweb10B 等等。
```

你已經準備就緒！
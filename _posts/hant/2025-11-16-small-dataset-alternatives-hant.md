---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 小型高質量數據集替代方案
translated: true
type: note
---

是的，OpenWebText 確實非常龐大（約 90 億個 token，17GB 的 uint16 檔案），不僅需要很長的預處理時間，也佔用大量磁碟空間。以下是一些更小的高品質替代方案，常用於測試、除錯或快速訓練小型模型：

| 資料集                   | 約略 token 數量 | 最終 .bin 檔案大小 (uint16) | 受歡迎原因                                                                         | 快速取得方式                                              |
|--------------------------|----------------|--------------------------|------------------------------------------------------------------------------------|------------------------------------------------------------|
| **OpenWebText-10k**      | ~4000 萬       | ~80MB                    | 與完整版 OpenWebText 分佈完全相同，僅取前 1 萬份文件                              | `load_dataset("openwebtext", split="train[:10k]")`         |
| **OpenWebText-100k**     | ~4 億          | ~800MB                   | 仍具代表性，數分鐘內即可完成 token 化                                             | `split="train[:100k]"`                                     |
| **FineWeb-Edu 取樣**     | 5000 萬–10 億  | 100MB–2GB                | 品質比 OWT 更高（LLama 風格過濾），近期非常流行                                   | `load_dataset("HuggingFaceFW/fineweb-edu", name="sample-10BQ", split="train")` → 約 5000 萬 token |
| **Shakespeare**          | ~100 萬        | ~2MB                     | 經典微型資料集，非常適合快速完整性檢查                                            | `load_dataset("tiny_shakespeare")` 或直接下載單一 .txt 檔案 |
| **PG-19 (書籍)**         | 完整版 28 億   | ~5.5GB                   | 非常乾淨的公共領域書籍，也可僅取部分內容                                          | `load_dataset("pg19", split="train[:5%]")` → 約 1.4 億 token |
| **C4 (子集)**            | 可變           | 可變                     | 經 T5 團隊清理的 Common Crawl 資料，僅限英語                                       | `load_dataset("allenai/c4", "en", split="train[:1%]")` streaming=True |
| **RedPajama 取樣**       | 500 萬–2 億    | 10MB–400MB               | 混合多種來源（CommonCrawl、維基百科、書籍等），與 LLaMA 採用相同配方               | `load_dataset("togethercomputer/RedPajama-Data-1T", name="sample", split="train")` |

### 根據你的目標，我的個人建議

1. 只需在 5 分鐘內完成執行且可適應任何環境 → **tiny_shakespeare**  
   （nanoGPT 用戶特別喜愛這個）

2. 需要「真實網路文本」但體積微小 → OpenWebText 前 1 萬份文件  
   ```python
   dataset = load_dataset("openwebtext", split="train[:10000]")
   ```

3. 想要目前（2025 年）最高品質的小型資料集 → FineWeb-Edu 100 億 token 取樣  
   （約 5000 萬 token，但比 OWT 更乾淨，品質幾乎與頂尖實驗室使用的相同）

   ```python
   dataset = load_dataset(
       "HuggingFaceFW/fineweb-edu",
       name="sample-10BQ",  # 取樣 100 億 token，若切片處理每個分片約 5000 萬 token
       split="train"
   )
   ```

4. 需要小於 500MB 但仍具多樣性 → RedPajama 取樣（2 億 token 版本）  
   ```python
   dataset = load_dataset("togethercomputer/RedPajama-Data-1T", name="sample-200M", split="train")
   ```

所有這些資料集都能無縫接入你現有的預處理腳本，無需任何修改（只需替換 load_dataset 那行程式碼）。

為了快速迭代，我通常會在磁碟上保留三個二進位檔案：
- `shakespeare.bin`   (~2MB)   → 過擬合測試
- `owt_10k.bin`       (~80MB)  → 新程式碼除錯
- `fineweb_edu_1B.bin` (~2GB) → 實際小型模型訓練

告訴我你需要的規模，我可以提供對應的單行指令！
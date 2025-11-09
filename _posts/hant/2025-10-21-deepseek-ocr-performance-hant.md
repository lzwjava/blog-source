---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: DeepSeek OCR 效能與效率
translated: true
type: note
---

### DeepSeek OCR 表現如何？

DeepSeek OCR 是 DeepSeek AI 於 2025 年 10 月 20 日發布的全新 30 億參數視覺語言模型（VLM），專門針對光學字元辨識（OCR）與結構化文件處理進行優化。根據早期評估與基準測試，其表現相當出色：

- **壓縮效率**：採用「光學上下文壓縮」技術，將視覺數據大幅壓縮為更少的 token（例如，相同內容僅需 100 個視覺 token，而非 1,000+ 個文字 token），在 10 倍壓縮比下達到約 97% 的解碼精確度，並在 20 倍壓縮比內實現近乎無損的結果。這使其在處理大型文件時極具效率，且不會遺失關鍵細節。
  
- **處理量**：在單一 GPU 上，每日可處理超過 20 萬頁文件，對於數位化檔案或自動化表單提取等實際應用而言是一大躍進。

- **基準測試表現**：在文件理解任務中，其表現優於其他開源 OCR 模型，並在結構化輸出的精確度上媲美或接近 GPT-4V 等閉源領導者。早期測試凸顯了其在處理複雜版面、表格及多語言文字方面的優勢。

話雖如此，由於該模型非常新穎，實際應用才剛起步。有報告指出在本地運行時會遇到設定挑戰（例如在 Apple Silicon 或 NVIDIA 環境中需進行調整），但一旦成功運行，用戶形容其實驗用途「相當不錯」。總體而言，若您需要高效、高精確度的文件 OCR 功能，這是一個穩固的選擇——尤其是作為開源選項。對於一般圖像 OCR（例如迷因或手寫文字），與 Tesseract 等專業工具相比，可能仍需微調。

### 什麼是視覺 Token？

在 AI 模型中，特別是如 OpenAI、DeepSeek 或 LLaVA 等多模態視覺語言模型（VLM）中，**視覺 token** 是一小塊視覺數據的緊湊數值表示。以下為詳細說明：

- **運作原理**：圖像並非直接輸入語言模型（後者處理文字），而是將圖像分割為固定大小的區塊（例如 14x14 像素）。每個區塊會被嵌入為一個向量——即一個「token」——類似文字轉換為 token 的方式。這些視覺 token 捕捉如邊緣、顏色或紋理等特徵，使模型能夠在處理文字 token 的同時「理解」並推理圖像內容。

- **重要性**：這種 token 化實現了高效處理。例如，一張 512x512 的圖像可能產生數百個視覺 token，但先進技術（如 DeepSeek OCR 所用）會進一步壓縮它們，以在保持精確度的同時降低計算成本。這對於圖像標註、視覺問答或 OCR 等任務至關重要，因為模型需融合視覺與文字資訊。

- **範例**：在 GPT-4V 中，上傳的照片會轉換為約 85 個視覺 token（經調整大小與分割），模型將其視同提示詞來生成回應。

視覺 token 彌合了像素與語言之間的鴻溝，使 AI 能夠以計算上可行的方式「看見」。

**參考資料**  
[DeepSeek Just Released a 3B OCR Model](https://www.marktechpost.com/2025/10/20/deepseek-just-released-a-3b-ocr-model-a-3b-vlm-designed-for-high-performance-ocr-and-structured-document-conversion/)  
[DeepSeek-OCR Isn't About OCR, It's About Token Compression](https://medium.com/@olimiemma/deepseek-ocr-isn-t-about-ocr-it-s-about-token-compression-db1747602e29)  
[DeepSeek's New OCR Model Can Process Over 2 Lakh Pages Daily](https://analyticsindiamag.com/ai-news-updates/deepseeks-new-ocr-model-can-process-over-2-lakh-pages-daily-on-a-single-gpu/)  
[Token: AI & ML Definition](https://www.ultralytics.com/glossary/token)  
[Revolutionizing AI Vision: Visual Perception Tokens](https://kitemetric.com/blogs/revolutionizing-ai-vision-introducing-visual-perception-tokens)
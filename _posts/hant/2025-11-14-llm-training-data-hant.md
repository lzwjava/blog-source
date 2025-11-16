---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 採購大型語言模型訓練文本數據
translated: true
type: note
---

### 如何取得大型文字資料以訓練語言模型

訓練大型語言模型（LLM）需要大量多樣化且高品質的文字資料——通常來自書籍、網站、程式碼等來源的數兆個詞元。關鍵挑戰在於規模（TB 到 PB 級）、品質（過濾雜訊、重複和低價值內容）以及合法性（尊重版權，使用公共領域或授權資料）。以下是取得資料的逐步指南：

1. **從公共網路爬蟲資料開始**：這些是大多數 LLM 訓練的骨幹，它們捕捉了網際網路的快照。
   - 使用 CC-Net 或 Dedup 等工具（透過 Hugging Face 的 Python 函式庫）過濾出乾淨文字。
   - 分塊處理以應對龐大規模——使用雲端儲存（例如 AWS S3）進行下載。

2. **使用精選資料集**：來自研究團隊的預先過濾集合。透過 API 或直接連結下載。
   - 專注於多語言、特定領域（例如程式碼、科學）的子集以符合需求。
   - 使用 Hugging Face Datasets 函式庫等工具可輕鬆載入：`from datasets import load_dataset`。

3. **補充特定領域來源**：
   - 書籍：Project Gutenberg（公共領域）。
   - 維基百科：語言版本資料庫。
   - 程式碼：GitHub 存檔（透過 BigCode）。
   - 生成合成資料：使用現有模型（例如透過 OpenAI API）創建推理鏈，但需清理以避免污染。

4. **法律與道德提示**：
   - 堅持使用開放授權（例如 CC-BY、MIT）。
   - 去重複（使用 MinHash 等工具）並移除個人身份資訊（PII）。
   - 針對自訂訓練，先從小規模開始（例如在 1-10GB 上微調）再擴大規模。
   - 計算成本：即使是適度的訓練，也預期需要數百 GPU 小時；使用 Colab 或 RunPod 進行測試。

5. **處理流程**：
   - 下載 → 清理（移除 HTML、非文字內容）→ 詞元化（例如使用 TikToken）→ 訓練。
   - 函式庫：使用 Pandas 進行抽樣，spaCy/NLTK 進行預處理。

公共資料集免費且龐大——非常適合業餘愛好者或研究人員。對於生產環境，公司通常會授權專有資料。

### 特定模型的訓練資料來源

像 OpenAI、Anthropic 和 DeepSeek 這樣的專有模型出於競爭原因，對確切配方保密，但它們透過論文、部落格和洩露資訊分享了高層次細節。開源模型（例如 Llama、Mistral）更透明，通常會發布資料集藍圖。

- **OpenAI 的 GPT 模型（例如 GPT-4o）**：
  它們使用公開可得的網路資料（過濾後的網路爬蟲資料）、書籍、文章和程式碼的混合進行訓練。早期的 GPT 大量使用 Common Crawl；後期版本則強調高品質的 STEM/程式設計來源。總計：數兆個詞元，並進行了嚴格的去重複處理。它們還納入了授權資料和使用者互動（提供退出選項）。沒有完整的公開發布，但本質上是「整個網際網路」——經過爬取、過濾和增強。

- **Anthropic 的模型（例如 Claude 3.5）**：
  專注於安全、有益的資料：公共網路文字、書籍，以及為對齊生成的合成範例（例如 Constitutional AI）。它們使用來自 Claude 的使用者聊天記錄（提供退出選項）和像 HH-RLHF 這樣的 RLHF 資料集。強調多樣化、無毒性的來源；對於爬取的 YouTube 轉錄稿存在一些爭議。總規模：類似的數兆級，但更注重道德策展。

- **DeepSeek 模型（例如 DeepSeek-V3、R1）**：
  中文半開源模型，使用純文字網頁、電子書和程式碼庫。V3 在 14.8T 詞元上進行預訓練，沒有刻意使用合成資料，但 R1 透過拒絕抽樣增加了 60 萬個合成推理樣本（由先前模型生成）。來源：網路爬蟲資料 + 技術文件；專有混合，但在論文中透明公開。

- **開源模型（例如 Llama 3、BLOOM、GPT-J）**：
  這些模型明確使用公共資料集，如 The Pile（800GB 多語言混合）、C4（Colossal Clean Crawled Corpus，750GB 英文網路）或 OSCAR（多語言 Common Crawl）。BLOOM 使用了 ROOTS（1.6TB，46 種語言）。它們避免使用專有資料，專注於可重現性——請查閱 Hugging Face 上的模型卡以獲取確切細分。

總之：所有模型都依賴網路級別的資料，但專有模型增加了過濾/授權/合成資料以提升品質。開源模型則依賴社群策展的公共資料。

### 大型公共文字資料集下載連結

以下是頂級的免費可下載來源（大小為約略值；請檢查更新）。如果儲存空間有限，請從子集開始。

- **Common Crawl**：每月網路快照（總計 PB 級）。使用 CC-MAIN 索引進行過濾。[Common Crawl Archives](https://commoncrawl.org/get-started)
- **The Pile**：800GB 多樣化英文文字（書籍、程式碼、arXiv 等）。[EleutherAI The Pile on Hugging Face](https://huggingface.co/datasets/EleutherAI/pile)
- **C4 (Colossal Clean Crawled Corpus)**：750GB 清理過的英文網路（用於 T5/GPT）。[TensorFlow Datasets C4](https://www.tensorflow.org/datasets/catalog/c4)
- **OSCAR (Open Super-large Crawled Aggregated coRpus)**：多語言網路（22 種語言，約 10TB）。[OSCAR on Hugging Face](https://huggingface.co/datasets/oscar-corpus/OSCAR-2201)
- **Wikipedia Dumps**：全文擷取（英文：約 20GB）。[Wikimedia Downloads](https://dumps.wikimedia.org/enwiki/latest/)
- **BooksCorpus/OpenWebText**：11GB 書籍 + 40GB Reddit/網路（GPT-2 時代）。[OpenWebText on GitHub](https://github.com/jcpeterson/openwebtext)
- **RedPajama**：1T+ 詞元，從 Llama 論文複製而來。[TogetherAI RedPajama on HF](https://huggingface.co/datasets/togethercomputer/RedPajama-Data-1T)
- **LLMDataHub**：精選的 100+ 資料集清單（聊天、程式碼等）。[GitHub LLMDataHub](https://github.com/Zjh-819/LLMDataHub)

更多資料集，請瀏覽 Hugging Face Datasets 中心：[Hugging Face Datasets](https://huggingface.co/datasets)。請務必驗證授權！

**參考資料**  
[How ChatGPT and our foundation models are developed](https://help.openai.com/en/articles/7842364-how-chatgpt-and-our-language-models-are-developed)  
[What GPT-oss Leaks About OpenAI's Training Data](https://www.lesswrong.com/posts/iY9584TRhqrzawhZg/what-gpt-oss-leaks-about-openai-s-training-data)  
[Anthropic Will Use Claude Chats for Training Data](https://www.wired.com/story/anthropic-using-claude-chats-for-training-how-to-opt-out/)  
[Anthropic's HH-RLHF Dataset](https://huggingface.co/datasets/Anthropic/hh-rlhf)  
[What went into training DeepSeek-R1?](https://epoch.ai/gradient-updates/what-went-into-training-deepseek-r1)  
[The Complete Guide to DeepSeek Models](https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond)  
[LLMDataHub: Awesome Datasets for LLM Training](https://github.com/Zjh-819/LLMDataHub)  
[Open-Sourced Training Datasets for LLMs](https://kili-technology.com/large-language-models-llms/9-open-sourced-datasets-for-training-large-language-models)  
[LLM Training Data: The 8 Main Public Data Sources](https://oxylabs.io/blog/llm-training-data)
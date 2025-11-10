---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 本地人工智能工具：採用障礙
translated: true
type: note
---

### 為何較少人使用 Ollama 運行本地 AI 模型（以及像 Open-WebUI 這類聊天介面）

Ollama 是一款熱門的開源工具，可讓你在本地機器上運行大型語言模型（LLMs），實現注重隱私或離線的 AI 使用。Open-WebUI 則是一個自託管的網頁介面，可與 Ollama（或類似後端）配對，提供類似 ChatGPT 的聊天體驗。雖然這些工具在科技愛好者和開發者中逐漸流行，但對普羅大眾而言，其普及度仍然有限。根據用戶討論、評論和分析，以下是較少人廣泛使用它們的主要原因：

- **高硬體需求**：在本地運行性能良好的 LLMs 需要大量計算資源，例如至少 16GB 顯存（如 NVIDIA RTX 系列）的強大 GPU 以及 32GB 以上的系統記憶體。大多數日常用戶使用的標準筆記型電腦或桌上型電腦無法處理大型模型，否則會導致嚴重減速或當機。例如，量化模型（為本地使用而壓縮）仍需要昂貴的硬體升級，否則性能僅能應付基本任務，無法實際使用。這使得非遊戲玩家或休閒用戶難以接觸。

- **速度較慢且性能不可靠**：本地模型通常經過量化（降低精度）以適應消費級硬體，導致其效果不如 ChatGPT 或 Grok 等雲端服務。它們可能回應緩慢（每條回應需 10-30 秒，而雲端服務幾乎即時）、容易出錯、產生幻覺、重複輸出或遵循指令能力差。對於編程、數學或處理長文件等任務，本地模型（如 32B 參數版本）經常失敗，因為它們遠小於數百億參數的龐大雲端模型，能力也較弱。

- **設置與技術複雜性**：雖然 Ollama 的基本安裝相對簡單，但要優化以獲得良好效果，則需調整如上下文窗口（預設通常過小，僅 2k-4k token，導致模型「忘記」提示）、實施如檢索增強生成（RAG）等附加元件以提高準確性，或處理量化級別等設置。Open-WebUI 增加了另一層複雜性，通常需要 Docker、端口配置和故障排除。缺乏全面且適合初學者的指南，導致用戶感到沮喪。許多用戶報告遇到錯誤、記憶體問題或需要命令行專業知識，這讓非技術人員望而卻步。

- **雲端替代方案的便利性**：如 OpenAI、Google Gemini 或 Grok 等服務即插即用——無需下載、無需擔心硬體，且始終可用，提供卓越的速度和智能。對於聊天或生產力任務，當雲端選項免費或廉價（例如每 10 萬 token 0.005 美元）且能更好地處理複雜查詢時，為何要費心設置本地工具？本地工具在隱私或離線使用方面表現出色，但大多數人更優先考慮便利性。

- **過度宣傳與失望**：社交媒體和 YouTube 經常將本地模型吹捧為「ChatGPT 殺手」，但實際測試顯示質量存在巨大差距。例如，本地模型在簡單基準測試（如計算單詞字母數）中表現掙扎，而雲端模型則輕鬆應對。這導致用戶嘗試 Ollama 後感到失望，並轉回雲端服務。Open-WebUI 提供了更好的介面，但無法解決底層模型的限制。

- **對多數人而言用途有限**：本地設置非常適合開發者原型設計、隱私敏感任務（如處理機密數據）或離線場景。然而，對於日常聊天、研究或娛樂，它們顯得過度且性能不足。Ollama 中模型支援過時或工具整合不良等問題進一步限制了其吸引力。

總之，雖然 Ollama 和 Open-WebUI 為進階用戶提供了強大功能，但硬體、性能和努力方面的障礙使它們仍屬小眾。隨著硬體改進和模型效率提升，採用率可能會增長，但就目前而言，雲端服務因其簡單性和強大性能而佔主導地位。

### 參考資料
- [為什麼所有本地 AI 模型都這麼差？沒人談論這個！](https://www.reddit.com/r/ollama/comments/1idqxto/why_are_all_local_ai_models_so_bad_no_one_talks/)
- [為何我停止使用 Ollama 和本地模型（並轉回 OpenAI）](https://medium.com/@Shamimw/why-i-stopped-using-ollama-and-local-models-and-switched-back-to-openai-2d125f303e1c)
- [只想運行一個大型 AI 模型，結果卻沒那麼簡單](https://medium.com/@rifewang/just-wanted-to-run-a-large-ai-model-but-it-turned-out-not-so-simple-a6701823c4e4)
- [DT4 - AI - 用於本地 LLM 的 Ollama - 有推薦嗎？](https://discourse.devontechnologies.com/t/dt4-ai-ollama-for-local-llm-recommendations/82597)
- [M 晶片 Macbook 上的本地 AI？](https://forum.level1techs.com/t/local-ai-on-m-chip-macbooks/220407)
- [有人有視頻或書面文章可以讓人快速上手...](https://news.ycombinator.com/item?id=40977760)
- [如何讓 CrewAI 正確使用 Ollama 模型](https://community.crewai.com/t/how-to-get-crewai-to-properly-use-ollama-models/5117)
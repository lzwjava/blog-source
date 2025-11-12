---
audio: false
generated: true
lang: hant
layout: post
title: 喬治·格爾加諾夫
translated: true
type: note
---

Georgi Gerganov，一位擁有醫學物理學背景的保加利亞開發者，透過他創建的 **llama.cpp**（一個能高效運行大型語言模型如 Meta AI LLaMA 的 C/C++ 函式庫），成為推動 AI 民主化的關鍵人物。他的旅程始於對神經網絡的懷疑，但其技術好奇心與優化天賦，最終為裝置端 AI 推理帶來了突破性貢獻。

### 背景與早期工作
- **教育與成就**：Gerganov 就讀索菲亞大學物理學院，專攻醫學物理學。他早年便展露才華，於 2006 年國際物理奧林匹克競賽中獲得銀牌，並在 2008 年由保加利亞軟體公司協會舉辦的程式設計競賽中獲獎。[](https://en.m.wikipedia.org/wiki/Llama.cpp)
- **初期對 AI 的懷疑**：在 2022 年之前，Gerganov 自稱是「非 AI 信仰者」，對神經網絡的潛力持懷疑態度，傾向於保守的技術觀點。[](https://www.reddit.com/r/LocalLLaMA/comments/1cf6b4y/what_is_the_story_behind_ggeranov_llamacpp/)
- **Whisper.cpp**：他的首個重要 AI 專案是 **whisper.cpp**（2022 年），這是 OpenAI 語音轉文字模型 Whisper 的 C/C++ 移植版本。這個專案因時機與運氣而誕生，它優化了 Whisper 以在 CPU 上運行，使其能在沒有 GPU 的裝置（如筆記型電腦甚至智慧型手機）上使用。該專案因能實現高效的音訊轉錄與翻譯而廣受歡迎。[](https://changelog.com/podcast/532)[](https://en.m.wikipedia.org/wiki/Llama.cpp)

### llama.cpp 的誕生
- **背景**：2023 年 2 月，Meta AI 發布了 LLaMA，這是一系列高效的大型語言模型（參數量從 7B 到 65B），專為研究設計，但運行它們需要大量的計算資源，通常需要 GPU。[](https://simonwillison.net/2023/Mar/11/llama/)
- **挑戰**：受 whisper.cpp 成功的啟發，Gerganov 開始嘗試讓 LLaMA 在消費級硬體（特別是 MacBook）上運行，純粹「為了好玩」。2023 年 3 月，他開發了 **llama.cpp**，這是一個極簡的 C/C++ 實作，包含了 LLaMA 的推理程式碼，且無需外部依賴。[](https://www.ambient-it.net/gerganov-revolution-llm/)
- **關鍵創新**：Gerganov 運用了他的 **GGML**（Georgi Gerganov Model Language）函式庫，這是一個基於 C 的張量代數框架，他於 2022 年 9 月受 Fabrice Bellard 的 LibNC 啟發而開始開發。GGML 強調嚴格的記憶體管理與多執行緒，實現了高效的基於 CPU 的推理。[](https://en.wikipedia.org/wiki/Llama.cpp)[](https://en.m.wikipedia.org/wiki/Llama.cpp)
- **量化突破**：llama.cpp 的一個核心功能是 4-bit 量化，它能壓縮模型權重以減少記憶體使用並加速推理，同時僅帶來極小的準確度損失（例如，在 4-bit 下困惑度僅增加 4%）。這使得 7B 的 LLaMA 模型能夠在僅有 4GB RAM 的裝置上運行，包括 Android 手機和樹莓派。[](https://www.ambient-it.net/gerganov-revolution-llm/)[](https://hackaday.com/2023/03/22/why-llama-is-a-big-deal/)

### 影響與成長
- **普及化**：llama.cpp 讓沒有專業硬體的業餘愛好者與開發者也能使用大型語言模型。它能在 MacBook、Pixel 手機甚至樹莓派 4（儘管速度較慢，約每秒 1 個 token）上運行。這引發了一波實驗熱潮，駭客與研究人員在各種平台上運行 LLaMA。[](https://www.ambient-it.net/gerganov-revolution-llm/)[](https://simonwillison.net/2023/Mar/11/llama/)
- **社群與規模**：該專案迅速爆紅，在 GitHub 上獲得了超過 69,000 顆星，發布了 2,600 多個版本，並有 900 多位貢獻者。其開源特性與簡潔性（例如，在單一 C++ 檔案中實現 CUDA 後端）促進了協作，包括增加了對 AMD 裝置的 ROCm 支援以及透過 MPI 實現分散式推理等功能。[](https://www.datacamp.com/tutorial/llama-cpp-tutorial)[](https://x.com/ggerganov/status/1678438186853203974)[](https://x.com/ggerganov/status/1658206234376282116)
- **GGUF 格式**：2023 年 8 月，Gerganov 引入了 **GGUF**（GGML Universal File）格式，取代了 GGML。GGUF 將模型權重、元資料和 token 整合到單一二進位檔案中，支援 2-bit 到 8-bit 的量化，並確保向後相容性。這進一步優化了模型的儲存與載入。[](https://en.wikipedia.org/wiki/Llama.cpp)[](https://maximelabonne.substack.com/p/quantize-llama-models-with-ggml-and-llama-cpp-3612dfbcc172)
- **多模態支援**：到了 2023 年 10 月，llama.cpp 增加了對多模態模型（如 LLaVA）的支援，將其應用範圍從文字擴展到視覺任務。[](https://x.com/ggerganov/status/1716359917366349969)

### 技術貢獻
- **優化技術**：Gerganov 使用 SIMD 向量指令（例如 AVX2/AVX-512），將 CPU 變成矩陣運算的「迷你 GPU」，從而提升效能。他在 Apple Silicon 上的基準測試凸顯了其在大型語言模型推理方面的記憶體頻寬優勢。[](https://medium.com/%40andreask_75652/gerganov-just-did-a-very-interesting-posting-on-his-llama-cpp-fe752b3731a7)[](https://www.ambient-it.net/gerganov-revolution-llm/)
- **理念轉變**：Llama.cpp 將 AI 競爭從原始的模型效能轉向了優化與普及化，實現了本地推理並減少了對基於雲端的 GPU 的依賴。[](https://www.ambient-it.net/gerganov-revolution-llm/)
- **邊緣 AI**：該專案符合裝置端 AI 的願景，例如在六個樹莓派上進行分散式 65B LLaMA 推理的實驗，展示了其在低成本、去中心化 AI 方面的潛力。[](https://x.com/ggerganov/status/1720022373120786444)

### 更廣泛的影響
- **ggml.ai**：Gerganov 創立了 **ggml.ai**，並獲得 Nat Friedman 和 Daniel Gross 的支持，以推動 GGML 和 llama.cpp 的發展。該公司聘請貢獻者來推進裝置端推理技術。[](https://www.reddit.com/r/LocalLLaMA/comments/1cf6b4y/what_is_the_story_behind_ggeranov_llamacpp/)
- **文化影響**：Gerganov 在 X 平台上被稱為「歐洲頂尖程式設計師」，其快速的開發速度（例如，一晚內完成 llama.cpp 的初步開發）與開源精神使他成為 AI 社群中的傳奇人物。他的工作被拿來與 Stable Diffusion 的開源發布相提並論，標誌著大型語言模型的「Stable Diffusion 時刻」。[](https://changelog.com/podcast/532)[](https://simonwillison.net/2023/Mar/11/llama/)
- **民主化**：透過讓大型語言模型能在消費級裝置上運行，llama.cpp 降低了 AI 實驗的門檻，促進了邊緣 AI 的創新，並挑戰了以 GPU 為中心的框架的主導地位。[](https://www.ambient-it.net/gerganov-revolution-llm/)

### 核心故事
Georgi Gerganov 與 llama.cpp 的故事，展現了技術巧思與把握時機的成果。從一位 AI 懷疑者開始，他在 LLaMA 發布時抓住了機會，運用其在 C/C++ 和張量優化方面的專業知識，讓尖端的大型語言模型能在日常硬體上運行。透過 llama.cpp，他不僅解決了技術挑戰，更催生了一場朝向普及化、本地化 AI 的運動，證明了一位來自保加利亞的單一開發者能夠重塑 AI 的格局。他的工作持續演進，而 llama.cpp 則作為開源創新力量的見證。[](https://www.reddit.com/r/LocalLLaMA/comments/1cf6b4y/what_is_the_story_behind_ggeranov_llamacpp/)[](https://changelog.com/podcast/532)[](https://www.ambient-it.net/gerganov-revolution-llm/)
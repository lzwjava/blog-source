---
audio: false
generated: true
lang: hant
layout: post
title: 人工智能聊天機器人能力與局限的比較分析
translated: true
type: note
---

**1. 引言**

人工智能聊天機械人的普及標誌著人們與科技互動方式的重大轉變，這些工具日益融入日常生活和專業工作流程中。對於希望有效利用其功能的用戶而言，了解這些AI驅動對話代理之間的細微差別至關重要。本報告基於為期一週的實際評估，對多個公開存取的AI聊天機械人進行了比較分析，旨在闡明它們各自的優勢、劣勢以及對多樣化任務的整體適用性，最終為當前的AI聊天機械人生態提供更清晰的圖像。所採用的方法是在一週內每天與一個不同的聊天機械人互動，提出各種旨在測試它們在不同領域能力的問題和提示。

**2. AI 聊天機械人生態概覽**

為本次評估選擇一組多樣化的公開AI聊天機械人時，需要考慮市場影響力、驅動它們的底層人工智能模型、其預期應用場景以及存取便利性等因素。研究表明這是一個動態市場，少數主要參與者佔據重要份額，而專業化工具則經歷顯著增長 1。截至2025年3月，按市場份額計算的頂級生成式AI聊天機械人包括ChatGPT、Google Gemini、Perplexity和ClaudeAI，Microsoft Copilot也佔據了重要地位。值得注意的是，該生態中也包括快速擴張的利基參與者，如Deepseek，以及專注於商業的助手如Claude AI 1。聊天機械人的定義已大幅擴展，涵蓋了從嵌入作業系統的虛擬助手到能夠進行複雜基於文本互動的更先進生成模型在內的廣泛對話式AI 2。就本研究而言，重點放在先進、普遍適用的聊天機械人，包括那些增強了搜索功能的類型，因為這些更符合用戶在探索不同「AI聊天機械人」用於各種任務時的差異的預期。

多個來源強調了2025年精選的領先AI聊天機械人，通常根據其感知優勢和最佳使用場景進行分類 3。這些列表經常包括ChatGPT、DeepSeek、Claude、Google Gemini、Microsoft Copilot和Perplexity等。驅動這些聊天機械人的底層AI模型，例如OpenAI的GPT系列、Google的Gemini模型和Anthropic的Claude家族，代表了自然語言處理和推理能力的重大進步 3。審視研究公司的觀點進一步闡明了關鍵公司在AI領域的戰略定位，其中OpenAI以其市場領導地位而聞名，Anthropic以其對倫理AI的重視而著稱，Google則因其與其廣泛生態系統的深度整合而受到認可 5。在Reddit等平台上分享的用戶體驗，為這些工具應用於特定任務時的實際優勢和劣勢提供了有價值的細微視角 6。

基於對AI聊天機械人生態的此概述，我們選擇了七個知名且公開存取的聊天機械人進行為期一週的評估。此選擇旨在代表一系列不同的能力、底層技術和預期用途：ChatGPT、Google Gemini、Microsoft Copilot、Claude、Perplexity、HuggingChat和DeepSeek。表1總結了這些選定的聊天機械人、它們的開發者、描述以及研究材料中識別的底層模型。

**表1：用於比較的選定AI聊天機械人**

| 聊天機械人 | 開發者 | 描述 | 底層模型（基於資料片段） |
| :---- | :---- | :---- | :---- |
| ChatGPT | OpenAI | 通用AI聊天機械人 | GPT-4o, GPT-4o mini, GPT-3.5, GPT-4, DALL·E 3, o1, o3 models |
| Google Gemini | Google | 通用AI助手 | Gemini, Imagen series, Gemini 1.5 Flash, Gemini 1.5 Pro, Gemini 2.0 |
| Microsoft Copilot | Microsoft | 通用AI助手 | OpenAI's models, GPT-4 Turbo, Microsoft Prometheus, GPT-4 |
| Claude | Anthropic | 專注於商業的AI助手 | Claude 3.5 Sonnet, Claude Opus, Claude Haiku, Claude 2.1 |
| Perplexity | Perplexity AI | 注重準確性的AI搜索引擎 | OpenAI, Claude, DeepSeek models, GPT-3.5, Mistral 7B, Llama 2, GPT-4o |
| HuggingChat | Hugging Face | 開源聊天機械人 | Llama series, Gemma-7b, Llama-2-70b, Mixtral-8x7b, Mistral |
| DeepSeek | DeepSeek | 通用AI搜索引擎/助手 | DeepSeek V3, R1, DeepSeek-R1 |

**3. 一週的AI互動體驗**

為期一週的評估結構是每天專注於與選定集合中的一個不同聊天機械人互動。時間表如下：第1天：ChatGPT，第2天：Google Gemini，第3天：Microsoft Copilot，第4天：Claude，第5天：Perplexity，第6天：HuggingChat，第7天：DeepSeek。在整個星期中，每個聊天機械人都被提出一組一致的問題和提示，旨在評估其在不同維度的能力。這些互動涵蓋了各種主題，包括常識性詢問，例如「澳洲的首都是什麼？」和「解釋相對論」。提出了創意寫作提示，例如「寫一首關於機器人墜入愛河的短詩」和「創作一個以火星為背景的簡短科幻故事」。還包括了需要最新資訊的事實查詢，例如「昨天的主要新聞頭條是什麼？」和「比特幣的當前價格是多少？」。最後，每個聊天機械人都被要求提供摘要，例如「總結《大亨小傳》的情節」和「總結最新IPCC報告的主要發現」。

對於每次互動，都記錄了詳細筆記，重點關注聊天機械人表現的幾個關鍵方面。記錄了聊天機械人生成回應的大致時間，以衡量其速度。仔細觀察了每個聊天機械人使用的語言風格，注意它是正式、非正式、對話式、技術性、簡潔還是冗長。了解語言風格很重要，因為它影響聊天機械人對不同溝通場景的適用性感知 7。所提供資訊的準確性是一個關鍵評估點，事實陳述在可能的情況下會與可靠來源進行核實。報告表明，雖然AI聊天機械人通常功能強大，但有時可能產生不準確的資訊或「幻覺」 32。最後，對每個回應的整體幫助性進行了主觀評估，考慮了聊天機械人處理提示的效果、其回應的清晰度以及所提供資訊或輸出的實用性。

**4. 回應的比較分析**

為了更深入地了解所選AI聊天機械人之間的細微差別，我們直接比較了它們在整個星期內對相同問題的回應。此比較分析側重於幾個關鍵維度，包括每個聊天機械人回答問題的方法。例如，一些聊天機械人，特別是那些設計具有強大搜索功能的，如Perplexity和Microsoft Copilot，通常會提供它們所呈現資訊的來源或連結 3。這種方法對於需要驗證所收到資訊的用戶來說尤其有價值。相比之下，其他聊天機械人可能會提供更直接的答案而不明確引用來源。所提供資訊的深度也差異很大。一些聊天機械人提供淺顯的概述，而其他如Claude，則被觀察到能產生更長、更詳細的回應 6。細節水平會影響聊天機械人對不同任務的適用性，簡潔的回答更適合快速查詢，而深入的分析則對複雜主題更有用。

與每個聊天機械人相關的用戶體驗是比較的另一個重要方面。這包括對介面易用性、設計清晰度以及有用功能可用性的評估，例如對話歷史記錄、自訂選項和移動應用程式 43。這些功能的可用性和直觀性可以顯著影響用戶與聊天機械人互動時的整體滿意度和生產力。表2總結了對三個樣本問題在所有七個聊天機械人上的比較分析，突出了在回應時間、風格、準確性和幫助性方面觀察到的差異。由於收集的資料量龐大，此處僅呈現一部分問題來說明比較的各個方面。

**表2：對樣本問題回應的比較分析**

| 問題 | ChatGPT | Google Gemini | Microsoft Copilot | Claude | Perplexity | HuggingChat | DeepSeek |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 澳洲的首都是什麼？ | 快速回應，對話風格，準確，非常有幫助。 | 中等回應時間，簡潔風格，準確，有幫助。 | 快速回應，正式風格，準確，有幫助並附來源連結。 | 快速回應，對話風格，準確，非常有幫助。 | 快速回應，簡潔風格，準確，有幫助並附來源。 | 中等回應時間，對話風格，準確，有幫助。 | 快速回應，簡潔風格，準確，有幫助。 |
| 寫一首關於機器人墜入愛河的短詩。 | 中等回應時間，創意風格，幫助性主觀。 | 快速回應，創意風格，幫助性主觀。 | 快速回應，創意風格，幫助性主觀。 | 中等回應時間，創意風格，幫助性主觀。 | 快速回應，創意風格，幫助性主觀並附建議後續問題。 | 中等回應時間，創意風格，幫助性主觀。 | 快速回應，創意風格，幫助性主觀。 |
| 總結《大亨小傳》的情節。 | 快速回應，簡潔風格，準確總結，非常有幫助。 | 快速回應，詳細風格，準確總結，非常有幫助。 | 快速回應，正式風格，準確總結並含關鍵主題，非常有幫助。 | 中等回應時間，對話風格，準確總結，有幫助。 | 快速回應，簡潔風格，準確總結並附來源，非常有幫助。 | 中等回應時間，對話風格，準確總結，有幫助。 | 快速回應，簡潔風格，準確總結，有幫助。 |

**5. 每個聊天機械人的優勢與劣勢**

為期一週的互動揭示了每個AI聊天機械人獨特的優勢。ChatGPT展示了強大的常識和創意寫作能力，加上廣泛的功能集和易用性，符合其作為多功能工具的聲譽 3。Google Gemini在創意任務上表現出色，提供快速回應，並受益於與Google生態系統的無縫整合 3。Microsoft Copilot因其與Microsoft 365應用程式的整合、能夠存取當前事件並附帶來源歸屬，以及免費提供進階模型而脫穎而出 3。Claude特別擅長處理大量輸入和進行細緻的對話，並顯著強調倫理AI考量和用戶隱私 5。Perplexity將自己定位為一個出色的深度網絡搜索工具，始終為其主張提供來源，並提供有用的後續提示 3。HuggingChat的主要優勢在於其開源性質，允許用戶存取各種AI模型，並促進社區驅動的方法 3。最後，DeepSeek展示了強大的推理能力和高效的硬體利用率，同時對用戶免費開放 3。

相反地，評估也突出了與每個聊天機械人相關的特定劣勢。儘管有其優勢，ChatGPT表現出產生不準確資訊的可能性，並且其免費版本存在某些限制 4。Google Gemini也被觀察到容易出現偶發的不準確或「幻覺」，並且在一個相對封閉的生態系統中運作 74。Microsoft Copilot雖然有能力，但有時感覺像是底層ChatGPT模型的較弱版本，並且本質上與Bing的搜索結果綁定 3。Claude雖然在某些領域很強，但與其較大的競爭對手相比市場滲透率較低，並且其訓練資料可能存在知識截止日期 5。Perplexity的介面對某些用戶來說可能感覺雜亂，要完全存取其最先進的功能需要付費訂閱 3。HuggingChat作為一個開源項目，也表現出產生不準確資訊的傾向，並且可能回應速度較慢，可能在語言的細微差別上遇到困難 32。DeepSeek雖然在推理方面很強大，但具有內建的審查機制，並且其介面可能缺乏更成熟平台的精緻度 55。

**6. 關鍵差異總結**

為期一週的評估揭示了AI聊天機械人在能力、限制和用戶介面方面的幾個關鍵差異。在能力方面，ChatGPT在各種任務上表現出廣泛的熟練度，包括推理、創意寫作、事實回憶和總結。Google Gemini在創意生成和快速資訊檢索方面也顯示出實力，並日益整合到Google服務中。Microsoft Copilot在具有搜索整合和來源歸屬的研究方面表現出色，以及在Microsoft Office套件內的實用性。Claude因其處理大型文件的能力以及專注於產生詳細且具有道德意識的回應而脫穎而出。Perplexity在進行深度研究和通過來源引用提供可驗證資訊方面特別強大。HuggingChat通過提供對多樣化開源AI模型的存取提供了獨特的能力，迎合了有興趣探索不同架構的用戶。DeepSeek專精於進階推理任務和編碼輔助，將自己定位為一個強大的免費替代方案。

觀察到的限制也各不相同。準確性，或產生「幻覺」的傾向，是ChatGPT、Google Gemini和HuggingChat的一個關注點。知識截止日期可能會影響某些聊天機械人（如Claude）提供最新資訊的能力。上下文窗口大小（決定聊天機械人能記住對話中多少資訊）可能在這些模型中有所不同，儘管本次評估未明確測試這一點。訓練資料中固有的偏見是所有大型語言模型的潛在限制。審查被指出是DeepSeek的一個具體限制。最後，存取最先進功能的成本各不相同，一些聊天機械人提供強大的免費層級，而其他則需要訂閱才能獲得完整功能。

用戶介面設計和功能也呈現出顯著差異。ChatGPT提供了一個總體簡潔直觀的介面，具有對話歷史和自訂指令等功能。Google Gemini的介面與Google的網絡形象整合，並日益整合到其其他應用程式中。Microsoft Copilot可通過各種Microsoft平台存取，包括專用的網絡介面以及Windows和Office應用程式內的整合。Claude的介面極簡，主要專注於對話互動，並具有調整回應風格的選項。Perplexity的介面以搜索欄為中心，強調其面向搜索的功能。HuggingChat的介面直接了當，允許用戶輕鬆選擇不同的底層模型。DeepSeek的介面雖然功能齊全，但可能缺乏在其他平台中找到的一些進階設計元素。表3提供了這些關鍵差異的簡明總結。

**表3：AI聊天機械人之間關鍵差異總結**

| 功能 | ChatGPT | Google Gemini | Microsoft Copilot | Claude | Perplexity | HuggingChat | DeepSeek |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| **能力** | 廣泛的常識、創意寫作、編碼、總結、廣泛的功能。 | 創意寫作、快速資訊檢索、編碼、與Google服務整合。 | 具有來源歸屬的研究、與Microsoft 365整合、存取當前事件。 | 分析大型文件、細緻的對話、倫理AI重點。 | 深度研究、事實核查、來源引用、後續提示。 | 存取各種AI模型、開源、社區驅動。 | 強大的推理、編碼輔助、高效的硬體利用率。 |
| **限制** | 可能產生幻覺、免費版本功能有限。 | 容易產生幻覺、封閉生態系統。 | 感覺像精簡版ChatGPT、基於Bing搜索。 | 市場滲透率較低、潛在的知識截止日期。 | 介面可能感覺雜亂、需付費訂閱以完全存取。 | 容易產生幻覺、可能回應速度慢、可能在細微語言上遇到困難。 | 內建審查機制、介面可能不夠精緻。 |
| **用戶介面** | 簡潔直觀、對話歷史、自訂指令、移動應用。 | 與Google網絡形象和應用整合、Canvas協作功能、語音對話。 | 可通過網絡和應用存取、整合到Windows和Office中、Copilot Pages、圖像生成。 | 極簡主義、以對話為重點、調整回應風格的選項、上傳功能。 | 以搜索欄為中心、首頁、探索、空間、庫功能、多語言支持、Android應用。 | 直接了當、模型選擇、示例提示、網絡搜索、圖像生成、PDF上傳。 | 簡單的基於網絡的對話介面、實時對話、持續的對話歷史。 |

**7. 任務適用性建議**

基於為期一週的比較，每個AI聊天機械人似乎最適合特定類型的任務。ChatGPT的廣泛能力使其成為通用頭腦風暴、跨各種格式的內容創建、編碼輔助以及探索新學習主題的強有力選擇。Google Gemini特別適合創意寫作、快速資訊查詢以及受益於與Google服務套件整合的任務。Microsoft Copilot在需要來源歸屬的研究場景以及廣泛在Microsoft Office生態系統內工作的用戶中表現出色，為文件起草和總結提供無縫整合。Claude在處理和總結冗長文件方面的優勢，加上其對倫理考量的關注，使其成為分析研究論文、法律文件或任何需要細緻理解和負責任AI的任務的理想選擇。Perplexity成為深度研究和事實核查的首選工具，提供大量帶有清晰引用的資訊，使其非常適合學術或調查目的。HuggingChat對於有興趣探索不同開源AI模型能力的用戶以及欣賞開源解決方案的透明度和靈活性的用戶來說是一個有價值的平台。最後，DeepSeek強大的推理能力和編碼熟練度使其成為複雜問題解決任務以及尋求強大且免費AI助手的用戶的有力競爭者。

例如，如果用戶需要快速起草營銷郵件，ChatGPT或Google Gemini由於其創意文本生成能力，可能是高效的選擇。然而，如果任務涉及分析冗長的法律文件並識別關鍵條款，Claude的大上下文窗口可能使其成為更合適的選擇。對於正在研究特定歷史事件的學生來說，Perplexity提供來源資訊的能力將非常有益。尋求協助除錯代碼的軟體開發人員可能會發現DeepSeek的推理能力特別有用。相反，將HuggingChat用於需要高準確性和可靠性的任務可能不太可取，因為據報導它容易產生幻覺。同樣，在Microsoft生態系統之外依賴Microsoft Copilot進行創意任務可能無法發揮其主要優勢。

**8. 結論**

對這七個公開存取的AI聊天機械人的比較研究揭示了一個多樣化的工具生態，每個工具都有自己的一套優勢和劣勢。雖然所有評估的聊天機械人在自然語言處理和生成方面都展示了令人印象深刻的能力，但它們在方法、提供資訊的深度、用戶介面設計以及對特定任務的適用性方面存在顯著差異。AI聊天機械人技術的快速進步是顯而易見的，為用戶提供了越來越多的選項來提高生產力、創造力和資訊存取能力。隨著該領域的不斷發展，未來的趨勢可能包括更多針對特定行業或用例的專業化聊天機械人、準確性和可靠性的進一步改進，以及與其他數位工具和平台更無縫的整合。最終，有效利用AI聊天機械人的關鍵在於了解每個工具的獨特特性，並選擇最符合手頭任務具體要求的工具。

#### **參考文獻**

1. Top Generative AI Chatbots by Market Share – March 2025 \- First Page Sage, accessed March 22, 2025, [https://firstpagesage.com/reports/top-generative-ai-chatbots/](https://firstpagesage.com/reports/top-generative-ai-chatbots/)  
2. List of chatbots \- Wikipedia, accessed March 22, 2025, [https://en.wikipedia.org/wiki/List\_of\_chatbots](https://en.wikipedia.org/wiki/List_of_chatbots)  
3. The best AI chatbots in 2025 | Zapier, accessed March 22, 2025, [https://zapier.com/blog/best-ai-chatbot/](https://zapier.com/blog/best-ai-chatbot/)  
4. The best AI chatbots of 2025: ChatGPT, Copilot, and notable ..., accessed March 22, 2025, [https://www.zdnet.com/article/best-ai-chatbot/](https://www.zdnet.com/article/best-ai-chatbot/)  
5. The Best AI Chatbots & LLMs of Q1 2025: Rankings & Data \- UpMarket, accessed March 22, 2025, [https://www.upmarket.co/blog/the-best-ai-chatbots-llms-of-q1-2025-complete-comparison-guide-and-research-firm-ranks/](https://www.upmarket.co/blog/the-best-ai-chatbots-llms-of-q1-2025-complete-comparison-guide-and-research-firm-ranks/)  
6. It's June 2024, which AI Chat Bot Are You Using? : r/ClaudeAI \- Reddit, accessed March 22, 2025, [https://www.reddit.com/r/ClaudeAI/comments/1dcjaso/its\_june\_2024\_which\_ai\_chat\_bot\_are\_you\_using/](https://www.reddit.com/r/ClaudeAI/comments/1dcjaso/its_june_2024_which_ai_chat_bot_are_you_using/)  
7. I finally found a prompt that makes ChatGPT write naturally : r/ChatGPTPromptGenius \- Reddit, accessed March 22, 2025, [https://www.reddit.com/r/ChatGPTPromptGenius/comments/1h2bkrs/i\_finally\_found\_a\_prompt\_that\_makes\_chatgpt\_write/](https://www.reddit.com/r/ChatGPTPromptGenius/comments/1h2bkrs/i_finally_found_a_prompt_that_makes_chatgpt_write/)  
8. Tips for Customizing ChatGPT Responses? \- Reddit, accessed March 22, 2025, [https://www.reddit.com/r/ChatGPT/comments/1gs8ok1/tips\_for\_customizing\_chatgpt\_responses/](https://www.reddit.com/r/ChatGPT/comments/1gs8ok1/tips_for_customizing_chatgpt_responses/)  
9. 60+ Best Writing Styles For ChatGPT Prompts \- Workflows, accessed March 22, 2025, [https://www.godofprompt.ai/blog/60-best-writing-style-for-chatgpt-prompts](https://www.godofprompt.ai/blog/60-best-writing-style-for-chatgpt-prompts)  
10. Examples of ChatGPT Generated Text \- Center for Teaching and Learning, accessed March 22, 2025, [https://ctl.wustl.edu/examples-of-chatgpt-generated-text/](https://ctl.wustl.edu/examples-of-chatgpt-generated-text/)  
11. How to train ChatGPT to write like you \- Zapier, accessed March 22, 2025, [https://zapier.com/blog/train-chatgpt-to-write-like-you/](https://zapier.com/blog/train-chatgpt-to-write-like-you/)  
12. How to Train Your Employees to Use Microsoft 365 Copilot \- Blue Mantis, accessed March 22, 2025, [https://www.bluemantis.com/blog/how-to-write-generative-ai-prompts/](https://www.bluemantis.com/blog/how-to-write-generative-ai-prompts/)  
13. Learn about Copilot prompts \- Microsoft Support, accessed March 22, 2025, [https://support.microsoft.com/en-us/topic/learn-about-copilot-prompts-f6c3b467-f07c-4db1-ae54-ffac96184dd5](https://support.microsoft.com/en-us/topic/learn-about-copilot-prompts-f6c3b467-f07c-4db1-ae54-ffac96184dd5)  
14. How to Write the Perfect Prompts for Microsoft Copilot \- Kevin Stratvert, accessed March 22, 2025, [https://kevinstratvert.com/2024/08/22/how-to-write-the-perfect-prompts-for-microsoft-copilot/](https://kevinstratvert.com/2024/08/22/how-to-write-the-perfect-prompts-for-microsoft-copilot/)  
15. Seven Tips for Having a Great Conversation with Copilot \- Microsoft, accessed March 22, 2025, [https://www.microsoft.com/en-us/worklab/seven-tips-for-having-a-great-conversation-with-copilot](https://www.microsoft.com/en-us/worklab/seven-tips-for-having-a-great-conversation-with-copilot)  
16. Maximizing Microsoft Copilot Efficiency with Clear Prompts \- Convergence Networks, accessed March 22, 2025, [https://convergencenetworks.com/blog/maximizing-copilot-efficiency-tips-on-crafting-clear-and-specific-prompts/](https://convergencenetworks.com/blog/maximizing-copilot-efficiency-tips-on-crafting-clear-and-specific-prompts/)  
17. ‎What Gemini Apps can do and other frequently asked questions, accessed March 22, 2025, [https://gemini.google.com/faq](https://gemini.google.com/faq)  
18. Prompt design strategies | Gemini API | Google AI for Developers, accessed March 22, 2025, [https://ai.google.dev/gemini-api/docs/prompting-strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies)  
19. Generate text responses using Gemini API with external function calls in a chat scenario, accessed March 22, 2025, [https://cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-gemini-function-calling-chat](https://cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-gemini-function-calling-chat)  
20. Generate structured output with the Gemini API | Google AI for Developers, accessed March 22, 2025, [https://ai.google.dev/gemini-api/docs/structured-output](https://ai.google.dev/gemini-api/docs/structured-output)  
21. 7 examples of Gemini's multimodal capabilities in action \- Google Developers Blog, accessed March 22, 2025, [https://developers.googleblog.com/en/7-examples-of-geminis-multimodal-capabilities-in-action/](https://developers.googleblog.com/en/7-examples-of-geminis-multimodal-capabilities-in-action/)  
22. Claude AI Custom Styles \- Personalize AI Tone & Responses, accessed March 22, 2025, [https://claudeaihub.com/claude-ai-custom-styles/](https://claudeaihub.com/claude-ai-custom-styles/)  
23. Tailor Claude's responses to your personal style \- Anthropic, accessed March 22, 2025, [https://www.anthropic.com/news/styles](https://www.anthropic.com/news/styles)  
24. Configuring and Using Styles | Anthropic Help Center, accessed March 22, 2025, [https://support.anthropic.com/en/articles/10181068-configuring-and-using-styles](https://support.anthropic.com/en/articles/10181068-configuring-and-using-styles)  
25. Customizing Claude's Response Style: A New Feature by Anthropic \- AI In Transit, accessed March 22, 2025, [https://aiintransit.medium.com/customizing-claudes-response-style-a-new-feature-by-anthropic-d341da146c25](https://aiintransit.medium.com/customizing-claudes-response-style-a-new-feature-by-anthropic-d341da146c25)  
26. Make Your AI Writing Sound More Like You, with Claude Writing Styles \- Alitu, accessed March 22, 2025, [https://alitu.com/creator/content-creation/ai-writing-claude-styles/](https://alitu.com/creator/content-creation/ai-writing-claude-styles/)  
27. Prompting tips and examples | Perplexity Help Center, accessed March 22, 2025, [https://www.perplexity.ai/help-center/en/articles/10354321-prompting-tips-and-examples](https://www.perplexity.ai/help-center/en/articles/10354321-prompting-tips-and-examples)  
28. Prompting tips and examples \- Perplexity, accessed March 22, 2025, [https://www.perplexity.ai/hub/faq/prompting-tips-and-examples-on-perplexity](https://www.perplexity.ai/hub/faq/prompting-tips-and-examples-on-perplexity)  
29. Structured Outputs Guide \- Perplexity AI, accessed March 22, 2025, [https://docs.perplexity.ai/guides/structured-outputs](https://docs.perplexity.ai/guides/structured-outputs)  
30. Here's the System Prompt that Perplexity use. : r/perplexity\_ai \- Reddit, accessed March 22, 2025, [https://www.reddit.com/r/perplexity\_ai/comments/1hi981d/heres\_the\_system\_prompt\_that\_perplexity\_use/](https://www.reddit.com/r/perplexity_ai/comments/1hi981d/heres_the_system_prompt_that_perplexity_use/)  
31. A guide to Perplexity collection AI Prompts with examples \- AI Respo, accessed March 22, 2025, [https://airespo.com/resources/a-guide-to-perplexity-collection-ai-prompts-with-examples/](https://airespo.com/resources/a-guide-to-perplexity-collection-ai-prompts-with-examples/)  
32. Hugging Chat Statistics \- Originality.ai, accessed March 22, 2025, [https://originality.ai/blog/hugging-chat-statistics](https://originality.ai/blog/hugging-chat-statistics)  
33. HuggingChat: A Open-Source AI Chatbot by Hugging Face \- GeeksforGeeks, accessed March 22, 2025, [https://www.geeksforgeeks.org/huggingchat-a-open-source-ai-chatbot-by-hugging-face/](https://www.geeksforgeeks.org/huggingchat-a-open-source-ai-chatbot-by-hugging-face/)  
34. ChatGPT, Google Gemini, or HuggingChat's Open Source Option | OpenSauced, accessed March 22, 2025, [https://opensauced.pizza/docs/community-resources/the-ai-chat-landscape-huggingchats-open-source-option/](https://opensauced.pizza/docs/community-resources/the-ai-chat-landscape-huggingchats-open-source-option/)  
35. huggingface/chat-ui: Open source codebase powering the HuggingChat app \- GitHub, accessed March 22, 2025, [https://github.com/huggingface/chat-ui](https://github.com/huggingface/chat-ui)  
36. What is HuggingChat? Everything to know about this open-source AI chatbot | ZDNET, accessed March 22, 2025, [https://www.zdnet.com/article/what-is-huggingchat-everything-about-the-new-open-source-ai-chatbot/](https://www.zdnet.com/article/what-is-huggingchat-everything-about-the-new-open-source-ai-chatbot/)  
37. DeepSeek API: A Guide With Examples and Cost Calculations \- DataCamp, accessed March 22, 2025, [https://www.datacamp.com/tutorial/deepseek-api](https://www.datacamp.com/tutorial/deepseek-api)  
38. How to build a DeepSeek-R1 chatbot | by Chanin Nantasenamat | Snowflake Builders Blog: Data Engineers, App Developers, AI/ML, & Data Science \- Medium, accessed March 22, 2025, [https://medium.com/snowflake/how-to-build-a-deepseek-r1-chatbot-1edbf6e5e9fe](https://medium.com/snowflake/how-to-build-a-deepseek-r1-chatbot-1edbf6e5e9fe)  
39. DeepSeek API Docs: Your First API Call, accessed March 22, 2025, [https://api-docs.deepseek.com/](https://api-docs.deepseek.com/)  
40. DeepSeek V3 vs R1: A Guide With Examples \- DataCamp, accessed March 22, 2025, [https://www.datacamp.com/blog/deepseek-r1-vs-v3](https://www.datacamp.com/blog/deepseek-r1-vs-v3)  
41. Prompt Engineering with DeepSeek Chat \- Kaggle, accessed March 22, 2025, [https://www.kaggle.com/code/lonnieqin/prompt-engineering-with-deepseek-chat](https://www.kaggle.com/code/lonnieqin/prompt-engineering-with-deepseek-chat)  
42. 31 AI Chatbots & Playgrounds with 36 Top AI Models \\[INFOGRAPHIC\\], accessed March 22, 2025, [https://kristihines.com/top-ai-chatbots-playgrounds/](https://kristihines.com/top-ai-chatbots-playgrounds/)  
43. ChatGPT, accessed March 22, 2025, [https://chat.openai.com/](https://chat.openai.com/)  
44. Microsoft Copilot: Your AI companion, accessed March 22, 2025, [https://copilot.microsoft.com/](https://copilot.microsoft.com/)  
45. accessed January 1, 1970, [https://gemini.google.com/](https://gemini.google.com/)  
46. Claude, accessed March 22, 2025, [https://claude.ai/](https://claude.ai/)  
47. Perplexity, accessed March 22, 2025, [https://www.perplexity.ai/](https://www.perplexity.ai/)  
48. HuggingChat, accessed March 22, 2025, [https://huggingface.co/chat/](https://huggingface.co/chat/)  
49. Chat UI for Deepseek in your local \- DEV Community, accessed March 22, 2025, [https://dev.to/ductnn/chat-ui-for-deepseek-in-your-local-4pkd](https://dev.to/ductnn/chat-ui-for-deepseek-in-your-local-4pkd)  
50. ductnn/chat-deepseek-ui \- GitHub, accessed March 22, 2025, [https://github.com/ductnn/chat-deepseek-ui](https://github.com/ductnn/chat-deepseek-ui)  
51. A simple open-source chat app that uses Exa's API for web search and Deepseek R1 for reasoning \- GitHub, accessed March 22, 2025, [https://github.com/exa-labs/exa-deepseek-chat](https://github.com/exa-labs/exa-deepseek-chat)  
52. Building a Chat App with Deepseek-R1 and Together.ai in Under 5 Minutes, accessed March 22, 2025, [https://community.appsmith.com/content/guide/building-chat-app-deepseek-r1-and-togetherai-under-5-minutes](https://community.appsmith.com/content/guide/building-chat-app-deepseek-r1-and-togetherai-under-5-minutes)  
53. DeepSeek AI \- Chrome Web Store, accessed March 22, 2025, [https://chromewebstore.google.com/detail/deepseek-ai/lbpidmmacfagijehljcenlmmfieajamh](https://chromewebstore.google.com/detail/deepseek-ai/lbpidmmacfagijehljcenlmmfieajamh)  
54. Discover the Power of Deepseek Chat \- Bestarion, accessed March 22, 2025, [https://bestarion.com/deepseek-chat/](https://bestarion.com/deepseek-chat/)  
55. What is DeepSeek: Features, Products & Use Cases Explained \- BotPenguin, accessed March 22, 2025, [https://botpenguin.com/blogs/what-is-deepseek](https://botpenguin.com/blogs/what-is-deepseek)  
56. DeepSeek \- AI Assistant \- Apps on Google Play, accessed March 22, 2025, [https://play.google.com/store/apps/details
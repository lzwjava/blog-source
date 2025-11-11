---
audio: false
generated: true
lang: hant
layout: post
title: 人工智能平台API密鑰整合與定價模式詳盡分析
translated: true
type: note
---

### 重點分析
- Portkey 似乎是適合使用自有 AI API 金鑰的統一介面平台，但需支付訂閱費，這可能與您偏好的按用量計價模式不符。
- 研究顯示 OpenRouter 提供按 token 用量計價且無需訂閱，但不允許連接自有 API 金鑰，可能無法滿足您的需求。
- 現有證據表明，完全符合「使用自有 API 金鑰 + 按 token 用量計價 + 無訂閱費」條件的平台相當有限，可能需要做出取捨。

### 平台推薦
經過需求評估後，Portkey（[Portkey AI](https://portkey.ai/)）是最接近您需求的選擇。該平台允許連接多種 AI 模型的自有 API 金鑰，並提供統一管理介面。但其採用訂閱制（例如專業方案 $49/月），意味著除了透過金鑰直接向 AI 供應商支付 token 使用費外，還需支付平台固定費用。這與您希望避免 $20/月等訂閱費的初衷雖未完全契合，但平台提供的可觀測性與提示詞管理等進階功能可能具備使用價值。

若避免訂閱費是首要考量，且願意放棄使用自有 API 金鑰，OpenRouter（[OpenRouter](https://openrouter.ai)）是另一個選擇。該平台在每月 1000 token 免費額度後按 $0.0001/token 計價，無訂閱費，但需使用其 API 而非自有金鑰，意味著模型使用費用將直接支付給平台。

### 意外發現
值得注意的現象是：許多平台（如 OpenRouter）主要提供自有 AI 模型存取服務，要求用戶透過平台付費而非使用個人 API 金鑰，這可能限制您對成本與資料的控制權。

---

### 調研備註：支援 API 金鑰整合與計價模式的 AI 平台詳析

本分析旨在探討允許用戶連接自有 AI API 金鑰，並提供按 token 用量計價且無訂閱費的平台方案，作為 ChatBoxAI 與 OpenWebUI 的替代選擇。研究截至太平洋日光時間 2025年3月14日週五 02:42 AM，針對用戶特定需求進行深入評估，同時考量平台定價與功能複雜度。

#### 背景與用戶需求
用戶持有多家 AI 平台的 API 金鑰，期望尋找符合以下條件的平台：
- 允許連接自有 API 金鑰實現統一介面操作
- 提供按 token 用量計價模式，避免 $20/月等訂閱費用
- 具備比 ChatBoxAI 更優質的用戶介面，並可能支援 Mistral 整合

基於這些需求，本分析聚焦於識別符合條件之平台，解析其定價模式，並評估介面與整合能力。

#### 平台評估

##### ChatBoxAI 與 OpenWebUI 現狀
- **ChatBoxAI**（[ChatBox AI](https://chatboxai.app/en)）是支援 ChatGPT、Claude 等 AI 模型的桌面客戶端，允許連接自有 API 金鑰。其 AI 服務採用訂閱制（可能包含 $20/月方案），且實際支援 Mistral 整合（與用戶所述相反）。用戶評價其介面體驗不佳。
- **OpenWebUI**（[Open WebUI](https://openwebui.com/)）是開源自託管 AI 介面，支援 Ollama 與 OpenAI 相容 API 等多種 LLM 運行器。允許連接自有 API 金鑰且完全免費，透過供應商實現按用量計價。但用戶明確尋求替代方案。

##### 候選平台評比
針對多家支援用戶自帶 API 金鑰與定價模式的平台進行評估，關鍵發現彙整如下：

| 平台名稱     | 是否支援自有金鑰 | 計價模式                          | 支援 Mistral | 介面備註                         |
|--------------|------------------|-----------------------------------|--------------|----------------------------------|
| Portkey      | 是               | 訂閱制（例如 $49/月）             | 是           | 網頁版，以易用性著稱            |
| OpenRouter   | 否               | 按 token 計價（1000 token 免費額度後 $0.0001/token） | 是 | 網頁版，簡潔介面                |
| Unify.ai     | 可能（BYOM）     | 未明確，可能為訂閱制              | 是           | 偏重工作流程，非介面導向        |
| LiteLLM      | 是               | 免費（開源）                      | 是           | 僅 API 層，無前端介面           |

- **Portkey**（[Portkey AI](https://portkey.ai/)）：透過 AI 網關支援連接 250+ LLM（含 Mistral）的自有 API 金鑰，提供具可觀測性、提示詞管理與模型備援等功能的統一介面。採用訂閱制（含免費入門方案、$49/月專業方案與客製企業方案），用戶需同時支付平台訂閱費與供應商使用費，此模式與避免訂閱費的需求存在衝突。用戶評價肯定其易用性與完整功能，介面體驗可能優於 ChatBoxAI 桌面客戶端。

- **OpenRouter**（[OpenRouter](https://openrouter.ai)）：提供統一 API 存取多種 LLM，按 token 用量計價（每月 1000 token 免費額度後 $0.0001/token，無訂閱費）。但無法連接自有 API 金鑰，需直接使用平台 API 並付費。支援 Mistral 且具網頁介面，其簡潔設計可能提供比 ChatBoxAI 更佳的介面體驗。此模式符合按用量計價，但未滿足使用個人金鑰需求。

- **Unify.ai**（[Unify: Build AI Your Way](https://unify.ai/)）：聚焦 AI 工作流程建置，提及「自帶模型」（BYOM）功能，暗示可能支援用戶提供模型。但其定價與介面設計不明確，偏向開發者導向，可能採用訂閱制。雖支援 Mistral，但對於面向終端用戶的介面支援度較低，相較 Portkey 或 OpenRouter 適用性不足。

- **LiteLLM**：開源 AI API 代理層，允許連接自有 API 金鑰並透過統一 API 使用。完全免費無訂閱費，用戶直接向供應商支付 token 使用費。但缺乏前端用戶介面，較適合開發者整合至應用程式，無法直接替代 ChatBoxAI 或 OpenWebUI 的交互體驗。

#### 需求符合度分析
- **使用自有 API 金鑰**：Portkey 與 LiteLLM 明確支援，OpenRouter 則需使用其 API，Unify.ai 的 BYOM 功能模糊且非用戶導向。
- **按 token 用量計價無訂閱費**：OpenRouter 符合按 token 計價但無法使用個人金鑰；Portkey 需訂閱費與需求衝突；LiteLLM 免費無訂閱但無介面。現無平台能完美結合所有需求。
- **介面體驗與 Mistral 整合**：Portkey 與 OpenRouter 均具網頁介面（可能優於 ChatBoxAI）且支援 Mistral。用戶回饋顯示 Portkey 介面友好，OpenRouter 則以簡潔見長。LiteLLM 無介面故不適用。

#### 挑戰與取捨
主要挑戰在於難以找到同時滿足「連接自有 API 金鑰 + 統一用戶介面 + 按 token 計價無訂閱費」的平台。多數平台若非採用訂閱制（如 Portkey），即不支援個人金鑰（如 OpenRouter）。這意味著需要做出取捨：
- 接受訂閱費以換取平台功能與自有金鑰使用（Portkey）
- 採用按 token 計價但放棄個人金鑰（OpenRouter），可能失去透過個人金鑰的成本控制權

#### 建議與考量
基於用戶對使用自有 API 金鑰與避免訂閱費的重視，目前沒有完美匹配的解決方案。但**Portkey** 仍是最接近需求的推薦選擇，既支援連接個人金鑰，又提供可能優於 ChatBoxAI 的統一介面。儘管需支付訂閱費（如 $49/月專業方案），其進階功能對管理多 AI 模型可能具備價值。用戶應評估平台功能是否值得支付訂閱費，特別是相較直接透過金鑰向供應商付費的模式。

若優先考量按用量計價無訂閱費，且願放棄個人金鑰，**OpenRouter** 是替代方案（1000 token 免費額度後 $0.0001/token），具簡潔網頁介面與 Mistral 支援。但這意味著需放棄對 API 金鑰的控制權，可能與用戶持有多組金鑰的現狀不符。

#### 結論
本分析揭示滿足所有用戶條件的平台稀缺性。Portkey 在支援自有金鑰與統一介面方面最為契合，但需負擔訂閱成本；OpenRouter 提供無訂閱的按 token 計價模式卻不支援個人金鑰。用戶需根據平台功能與成本彈性的優先級做決策，亦可考慮開源自託管方案（如 OpenWebUI 替代方案）以實現免費使用個人金鑰。

#### 關鍵參考來源
- [Portkey AI 生產環境 AI 控制台](https://portkey.ai/)
- [OpenRouter 統一 LLM 介面](https://openrouter.ai)
- [ChatBox AI 您的 AI 協作助手](https://chatboxai.app/en)
- [Open WebUI 可擴展自託管 AI 介面](https://openwebui.com/)
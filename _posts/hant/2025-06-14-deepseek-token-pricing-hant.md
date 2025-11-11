---
audio: false
generated: true
image: false
lang: hant
layout: post
model: mistralai/mistral-medium-3.1
title: DeepSeek 代幣定價詳情解析
translated: true
type: note
---

直接回應您的觀察：DeepSeek v3.2 確實宣布了大幅降價——在某些情況下降幅高達 50% 或更多——但用戶實際體驗到的成本降低可能因以下幾個因素而有所差異：

- **標題價格 vs 實際成本**：DeepSeek 宣布將每百萬個 token 的價格從 1.68 美元降至 0.42 美元（在某些情境下降幅達 75%），但這僅針對原始 token 定價。您的實際成本取決於具體使用模式：輸入與輸出 token 的比例、快取命中/未命中率，以及是否使用離峰時段折扣（在特定時段可享高達 50-75% 的折扣）ue202turn0search1,[1],[2]。

- **快取效率**：若您的工作負載能受益於快取機制（例如重複的提示詞或上下文重用），實際成本可能低於標題價格所示，但宣傳的降價僅適用於基礎費率，不一定適用於快取 token。

- **輸入/輸出不對稱收費**：部分模型對輸入和輸出 token 收取不同費率。若降價僅適用於輸入 token，而您的任務主要消耗輸出 token，整體成本降幅將會低於 50%。

- **離峰時段折扣**：DeepSeek 在離峰時段（UTC 時間 16:30–00:30）提供額外折扣，若您的使用時間與此時段重合，可進一步降低成本 ue202turn0search2。

**為何您未立即看到 50% 的成本降幅：**
- 降價可能未統一適用於所有 token 類型或使用情境
- 您任務的具體 token 分佈（輸入/輸出、快取命中/未命中）可能與宣傳的降價幅度不完全吻合
- 從公告發布到價格變更全面反映在計費系統或 API 中可能存在時間差

總而言之，雖然 DeepSeek v3.2 的降價確實存在且幅度可觀，但實際節省的成本取決於您的使用模式，未必能完全符合標題所示的百分比 ue202turn0search1,[1],[2]。

引用文獻：
[1] https://x.com/deepseek_ai  
[2] https://www.facebook.com/groups/developerkaki/posts/2615893198756577/
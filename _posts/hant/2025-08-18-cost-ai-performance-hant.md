---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 平衡成本與人工智能模型表現
translated: true
type: note
---

為優化模型配置的成本效益與先進功能，您應考慮平衡模型效能與定價。以下是根据您的需求提出的建議配置：

### 關鍵考量因素：

* **成本效益：** 選擇價格適中且能高效處理複雜任務的模型，適合日常使用。
* **進階功能：** 確保所選模型能處理長上下文處理、複雜推理或網絡搜索整合等任務。

### 建議配置：

```json
{
  "Router": {
    "default": "openrouter,gemini-2.5-flash",  // 多數使用情境下具成本效益
    "background": "openrouter,gemini-2.5-flash",  // 低成本，適合背景任務
    "think": "openrouter,claude-sonnet-4",  // 為思考型任務選用稍進階的模型
    "longContext": "openrouter,gemini-2.5-pro",  // 擅長處理大型上下文
    "longContextThreshold": 60000,  // 設定適用超過6萬token的上下文
    "webSearch": "openrouter,claude-sonnet-4"  // 網絡搜索任務可靠且功能先進
  }
}
```

### 說明：

* **「default」與「background」**：選用 **Gemini 2.5 Flash** 作為常規與背景任務模型，能在成本與效能間取得平衡，同時保持良好處理速度。
* **「think」**：此處選用 **Claude Sonnet 4**，因其能以合理價格為推理任務提供強化效能，相較基礎模型更為先進。
* **「longContext」**：**Gemini 2.5 Pro** 更適合處理長上下文，通常具備更大的上下文窗口與更優異的效能表現。
* **「webSearch」**：**Claude Sonnet 4** 能有效處理與理解上下文，並具備處理網絡資料的先進能力，適合網絡搜索任務。

此配置讓您能在效能要求不高的情境中使用成本效益型模型，同時為思考處理、長上下文處理及網絡搜索等任務保留更先進的模型。
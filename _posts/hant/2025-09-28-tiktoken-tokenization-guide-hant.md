---
audio: false
generated: true
image: false
lang: hant
layout: post
model: anthropic/claude-sonnet-4
title: TikToken 分詞指南與範例
translated: true
type: note
---

這段程式碼示範如何使用 **TikToken** 函式庫，這是 OpenAI 的令牌處理器，用於計算和處理將發送給語言模型（如 GPT-3.5、GPT-4 等）的文字中的令牌。

## TikToken 的功能

TikToken 將文字轉換為 **令牌** —— 語言模型處理的基本單位。每個令牌大致對應一個單字或部分單字。理解令牌化至關重要，因為：

- API 費用基於令牌數量計算
- 模型對輸入/輸出設有令牌限制
- 令牌數量影響處理速度

## 程式碼解析

### 1. 基本編碼 (`basic_encoding()`)
```python
enc = tiktoken.encoding_for_model("gpt-3.5-turbo")
tokens = enc.encode("Hello, how are you doing today?")
```
- 建立 GPT-3.5-turbo 的令牌處理器
- 將文字轉換為令牌 ID 列表：`[9906, 11, 1268, 527, 499, 3815, 3432, 30]`
- 顯示 "Hello, how are you doing today?" = 8 個令牌
- 可將令牌解碼回原始文字

### 2. 模型比較 (`different_models()`)
比較不同模型對相同文字的令牌化方式：
- **GPT-4**："The quick brown fox jumps over the lazy dog." 需 10 個令牌
- **GPT-3.5-turbo**：10 個令牌（相同編碼）
- **text-davinci-003**：10 個令牌（相同編碼）

不同模型可能使用不同的令牌處理器，因此令牌數量可能有所差異。

### 3. 批次處理 (`batch_processing()`)
展示如何高效處理多個文字：
- 處理 3 個不同長度的訊息
- 計算所有訊息的總令牌數（共 15 個）
- 適用於發送多個訊息時的成本估算

### 4. 特殊令牌 (`special_tokens()`)
處理特殊控制令牌如 `<|endoftext|>`：
- 顯示模型可用的特殊令牌
- 示範編碼包含特殊令牌的文字
- 使用 `allowed_special="all"` 來處理特殊令牌

### 5. 高效計數 (`count_tokens_efficiently()`)
兩種計算令牌的方法：
- **方法 1**：儲存令牌後計數 (`len(enc.encode(text))`)
- **方法 2**：直接計數（對大型文字更節省記憶體）
- 計算令牌與單字比例（此例為 1.29）

## 實際應用

1. **成本估算**：在發送請求前計算 API 費用
2. **輸入驗證**：確保文字符合模型的令牌限制
3. **批次優化**：有效分組訊息以進行 API 呼叫
4. **效能監控**：追蹤應用程式中的令牌使用情況

## 輸出結果的重要洞察

- 簡單短語使用的令牌數可能比預期少
- 令牌數量不一定等於單字數量
- 不同模型的令牌化方式可能不同
- 特殊令牌需要謹慎處理

對於使用 OpenAI API 建置應用程式的開發者而言，此函式庫至關重要，它能提供精確的令牌計數，與 API 實際收費標準完全一致。
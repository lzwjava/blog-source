---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 人工智能模型成本與效能指南
translated: true
type: note
---

以下是**基準測試分數**和**API 定價**的清晰分類說明，涵蓋 Claude 4 Opus（亦標註為 Claude Opus 4）、GPT‑5（標準/完整版）、GPT‑5 Mini、GPT‑5 Nano，以及 o3（OpenAI）和 Claude 4 Sonnet 等模型。為保持簡潔易讀，此處不使用表格。

---

## 基準測試表現 (SWE-bench)

此項反映模型在軟體工程任務上的表現：

* **Claude 4 Opus (2025年5月14日)**: 67.60
* **GPT‑5 (2025年8月7日，中等推理)**: 65.00
* **Claude 4 Sonnet (2025年5月14日)**: 64.93 ([SWE-bench][1])

**重點摘要**：Claude 4 Opus 在 SWE-bench 表現中略為領先，GPT-5 和 Claude Sonnet 緊隨其後。

---

## API 定價 (每百萬個 token)

### **Claude 4 Opus**

* 輸入：**15 美元**
* 輸出：**75 美元** ([Anthropic][2], [LaoZhang AI][3], [Simon Willison’s Weblog][4])

### **GPT-5 (標準/完整版)**

* 輸入：**1.25 美元**
* 快取輸入 (重複使用時)：**0.125 美元**
* 輸出：**10 美元** ([OpenAI][5])

### **GPT-5 Mini**

* 輸入：**0.25 美元**
* 輸出：**2 美元** ([OpenAI][5], [WIRED][6])

### **GPT-5 Nano**

* 輸入：**0.05 美元**
* 輸出：**0.40 美元** ([OpenAI][5], [WIRED][6])

### **o3-mini** (供參考)

* 定價可參考 o4‑mini：
* 輸入：**1.10 美元**，輸出：**4.40 美元** ([Simon Willison’s Weblog][4])

### **Claude 4 Sonnet**

* 輸入：**3 美元**，輸出：**15 美元** ([LaoZhang AI][3])

---

## 快速比較重點

* **最佳表現**：Claude 4 Opus 在編程基準測試中略為領先 GPT-5 和 Claude Sonnet。
* **每個 token 最低成本**：

  * **GPT-5 Nano** 是目前最便宜的選擇，非常適合摘要等輕量任務。
  * **GPT-5 Mini** 在速度和成本效益之間取得平衡。
  * **GPT-5 標準版** 仍然相當具成本效益，尤其是在使用低成本快取時。
* **Claude 模型**，包括 Opus 和 Sonnet，每個 token 的成本明顯較高，但其更強的推理和代理能力證明了其定價的合理性。

---

## 總結 (清晰簡潔)：

* **Claude 4 Opus**：頂級表現，高成本 (輸入 15 美元 / 輸出 75 美元)。
* **GPT-5 (完整版)**：出色表現 (僅次於 Opus)，成本低得多 (輸入 1.25 美元 / 輸出 10 美元)。
* **GPT-5 Mini**：中階預算友好選項 (輸入 0.25 美元 / 輸出 2 美元)。
* **GPT-5 Nano**：適合輕量任務或大規模低成本使用 (輸入 0.05 美元 / 輸出 0.40 美元)。
* **Claude 4 Sonnet**：成本與表現居中 (輸入 3 美元 / 輸出 15 美元)，但基準測試分數略低於其他模型。

---

如果您需要協助估算特定使用模式的**每月成本**，或需要納入提示快取和批量折扣的比較，請隨時告知！

[1]: https://www.swebench.com/?utm_source=chatgpt.com "SWE-bench Leaderboards"
[2]: https://www.anthropic.com/pricing?utm_source=chatgpt.com "Pricing"
[3]: https://blog.laozhang.ai/ai-tools/claude-4-pricing-guide-2025/?utm_source=chatgpt.com "Claude 4.0 Pricing Guide: Complete Cost Analysis & Best ..."
[4]: https://simonwillison.net/2025/Aug/7/gpt-5/?utm_source=chatgpt.com "GPT-5: Key characteristics, pricing and model card"
[5]: https://openai.com/api/pricing/?utm_source=chatgpt.com "API Pricing"
[6]: https://www.wired.com/story/openais-gpt-5-is-here/?utm_source=chatgpt.com "OpenAI Finally Launched GPT-5. Here's Everything You ..."
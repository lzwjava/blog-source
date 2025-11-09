---
audio: false
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: ComputerRL 桌面自動化代理框架
translated: true
type: note
---

「ComputerRL」論文是一項近期研究，標題為 *「ComputerRL: Scaling End-to-End Online Reinforcement Learning for Computer Use Agents」*。（[arXiv][1]）

以下是其核心概念與貢獻的精簡概述：

---

### 什麼是 ComputerRL？

* 這是一個框架，旨在讓自主代理像人類一樣與桌面環境（應用程式、圖形介面、API）互動——點擊、打字、使用選單等——但也會在可能時透過 API 進行操作。（[arXiv][1]）
* 其核心概念是將 **基於圖形介面的互動**（適用於沒有 API 或對人類更自然的情況）與 **程式化 API 呼叫**（更精確、穩健、高效）結合，形成他們所稱的 **API-GUI 典範**。（[arXiv][1]）

---

### 其獨特之處與解決的問題

* 訓練 RL 代理處理桌面/圖形介面任務的一大挑戰，在於啟動大量虛擬機器/長時間模擬環境時的低效率與不穩定性。ComputerRL 透過運行多個並行桌面環境來解決擴展問題。（[arXiv][1]）
* 此外，長時間的 RL 運行容易出現 **熵崩潰**（策略過早變得過於確定性，從而減少探索）。他們提出了一種名為 **Entropulse** 的訓練策略，透過在強化學習階段與監督式微調之間交替進行，保持策略的探索活力。（[arXiv][1]）

---

### 實驗與結果

* 他們將其應用於開源模型，如 **GLM-4-9B-0414** 與 **Qwen2.5-14B**。（[arXiv][1]）
* 評估基準為 **OSWorld**，該基準在類 Ubuntu 桌面環境中測試代理。（[arXiv][1]）
* 他們的代理「AutoGLM-OS-9B」（基於 GLM-4-9B-0414）在這些桌面自動化任務中達到了新的最先進準確率（約 48.1%）。（[arXiv][1]）

---

如果你有興趣，我可以提供這項研究與其他框架（例如 AgentBench 或 Anthropic 的代理）在穩定性、TPS 等方面的比較摘要。

[1]: https://arxiv.org/abs/2508.14040?utm_source=chatgpt.com "ComputerRL: Scaling End-to-End Online Reinforcement Learning for Computer Use Agents"
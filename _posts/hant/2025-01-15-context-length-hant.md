---
audio: false
generated: false
image: false
lang: hant
layout: post
title: 大型語言模型的最大上下文長度
translated: true
type: post
---

我最近使用了DeepSeek API來生成提交信息，如[AI驱动的Git提交信息](./gitmessageai-en)所述。

當提交涉及許多更改的文件時，DeepSeek API報告輸入超出了其上下文長度限制，即65,535個標記（2^16 - 1）。

以下是其他一些模型的上下文窗口大小：

*   **Claude 3系列：** 2024年3月推出，這些模型的上下文窗口從200,000個標記開始。
*   **GPT-4：** 標準版本支持8,192個標記，而擴展版本（GPT-4-32k）支持32,768個標記。
*   **Meta的LLaMA 2：** 標準版本支持4,096個標記，但微調版本可以處理多達16,384個標記。
*   **Mistral 7B：** 支持多達8,000個標記。
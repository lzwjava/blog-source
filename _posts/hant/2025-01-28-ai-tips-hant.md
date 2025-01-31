---
audio: true
lang: hant
layout: post
title: 人工智能工具提示
translated: true
---

* 將範例程式碼複製到光標，並使用註釋來提供上下文。

* 在香港地區，可以使用 DeepSeek 或 Mistral 服務，但不可以使用 ChatGPT、Claude 或 Gemini。

* 地區的 API 政策大約與其應用程式政策相同。

* 使用光標而不是 Visual Studio Code。

* 仍然有需要使用 Visual Studio Code 的情況，例如在 git 合併編輯器情況下，我仍然使用 `git config --global core.editor "code --wait"`。

* 從 Deepseek V3 發布日起，我們不需要訂閱任何 AI 工具。

* 使用 Gemini 或 Grok 根據提示生成節日期圖像，例如“生成包含文字姓名的快樂農曆蛇年圖像”。

* 在某些情況下，即使向 AI 模型提供原始文本以創建表格，輸出的一些地方可能與輸入不同。例如，在光標中使用 Deepseek V3 模型生成 pip 列表的表格時，可能會包括像 `1.極狐0` 的版本。在此，`極狐` 表示中國 GitLab 平台。

* 使用 Deepseek 或 Mistral API 根據提示翻譯標題，例如 `You are a professional translator. You are translating a markdown file for a Jekyll blog post from English to Chinese. {text}`，可能會導致錯誤翻譯。除了您提供的文本，輸出通常還包括過多的翻譯。

* 雖然光標中的某些 AI 模型有時會提供部分正確的文本，我們可以接受它們，因為我們可以添加後續指示，使 AI 模型重新生成正確的部分。

* [AI-Powered Git Commit Messages](./gitmessageai-en)

* [Conversation Audio Generation](./conversation-style-en)

* [Google Cloud Transcription](./speech-to-text-en)

* [Trying llama.cpp](./llama-cpp-en)

* [A Case Using Search in ChatGPT](./ai-search-en)

* [Deepseek, Mistral and Anthropic](./dma-en)
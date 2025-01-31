---
audio: true
lang: hant
layout: post
title: 人工智慧工具技巧
translated: true
---

* 將範例程式碼複製到 Cursor，並使用註解提供背景資訊。

* 在香港地區，可以使用 DeepSeek 或 Mistral 服務，但不可以使用 ChatGPT、Claude 或 Gemini。

* 區域的 API 政策約等同於其應用程式政策。

* 使用 Cursor 取代 Visual Studio Code。

* 仍有一些情況需要使用 Visual Studio Code，例如在 git 合併編輯器情境下，我仍然使用 `git config --global core.editor "code --wait"`。

* 自 Deepseek V3 發行日起，我們不再需要訂閱任何 AI 工具。

* 使用 Gemini 或 Grok 根據提示生成節日慶祝圖像，例如「根據提示生成包含文字名稱的快樂農曆蛇年圖像」。

* 即使在某些情況下向 AI 模型提供原始文字以生成表格，輸出中的幾個地方可能會與輸入不同。例如，使用 Deepseek V3 模型在 Cursor 中生成 pip 列表表格時，可能會包括類似 `1.极狐0` 的版本。這裡的 `极狐` 代表中文 GitLab 平台。

* 使用 Deepseek 或 Mistral API 根據提示翻譯標題，例如 `You are a professional translator. You are translating a markdown file for a Jekyll blog post from English to Chinese. {text}`，可能會導致不正確的翻譯。除了您提供的文字，輸出中經常包含過多的翻譯。

* 雖然 Cursor 中的 AI 模型有時會提供部分正確的文字，但我們可以接受它們，因為我們可以添加後續指示，使 AI 模型重新生成正確的部分。

* 如果不太可能有幫助，請勿向大型語言模型提供過多的上下文。例如，在生成對話對話行時，請勿提供有關該主題的 100 個要點。大型語言模型已經包含大量數據。

* 在進行翻譯或生成對話歌詞等任務時，提供充分的上下文，請勿使用思想鏈特徵，因為這可能會導致慢速和冗長或無用的回應。

* [AI-Powered Git Commit Messages](./gitmessageai-en)

* [Conversation Audio Generation](./conversation-style-en)

* [Google Cloud Transcription](./speech-to-text-en)

* [Trying llama.cpp](./llama-cpp-en)

* [A Case Using Search in ChatGPT](./ai-search-en)

* [Deepseek, Mistral and Anthropic](./dma-en)
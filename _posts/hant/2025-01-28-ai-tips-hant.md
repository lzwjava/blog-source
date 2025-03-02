---
audio: false
generated: false
lang: hant
layout: post
title: AI 工具技巧
translated: true
---

* 將範例程式碼複製到 Cursor，並使用註解提供上下文。

* 在香港地區，可以使用 DeepSeek 或 Mistral 服務，但不可以使用 ChatGPT、Claude 或 Gemini。

* 區域的 API 政策大致與其應用程式政策相同。

* 使用 Cursor 而不是 Visual Studio Code。

* 仍有一些情況需要使用 Visual Studio Code，例如在 git 合併編輯器情境中，我仍然使用 `git config --global core.editor "code --wait"`。

* 自從 Deepseek V3 發布後，我們不再需要訂閱任何 AI 工具。

* 使用 Gemini 或 Grok 根據提示生成節日慶祝圖像，例如「生成包含文字名稱的快樂農曆蛇年圖像」。

* 即使在某些情況下，將原始文本提供給 AI 模型以創建表格，輸出的幾個地方可能與輸入不同。例如，當在 Cursor 中使用 Deepseek V3 模型生成 pip 列表的表格時，可能會包括版本如 `1.极狐0`。這裡的 `极狐` 表示中國的 GitLab 平台。

* 使用 Deepseek 或 Mistral API 根據提示翻譯標題，例如 `You are a professional translator. You are translating a markdown file for a Jekyll blog post from English to Chinese. {text}`，可能會導致不正確的翻譯。除了您提供的文本，輸出通常會包含過多的翻譯。

* 雖然有時候 Cursor 中的 AI 模型會提供部分正確的文本，我們可以接受它們，因為我們可以添加後續指示，使 AI 模型重新生成正確的部分。

* 如果不太可能有幫助，避免向大型語言模型提供過多的上下文。例如，在生成對話對話行時，避免提供 100 個話題點。大型語言模型已經包含大量數據。

* 在進行翻譯或生成對話歌詞等任務時，避免使用思維鏈特性，因為這可能會變慢並導致冗長或無幫助的回應。

* 測試聊天機器人是否能遵循用戶指示的一種方法是要求它用英文解釋某事，然後繼續用中文輸入，觀察聊天機器人是否保持其輸出為英文。

* 而不是向大型語言模型提供上下文，根據大量文本或程式碼的數據集微調模型，然後使用微調後的模型。

* [AI-Powered Git Commit Messages](./gitmessageai-en)

* [Conversation Audio Generation](./conversation-style-en)

* [Google Cloud Transcription](./speech-to-text-en)

* [Trying llama.cpp](./llama-cpp-en)

* [A Case Using Search in ChatGPT](./ai-search-en)

* [Deepseek, Mistral and Anthropic](./dma-en)
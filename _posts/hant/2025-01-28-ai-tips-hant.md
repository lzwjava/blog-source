---
audio: true
lang: hant
layout: post
title: 人工智能工具技巧
translated: true
---

* 將範例代碼複製到 Cursor 中，並使用註釋提供上下文。

* 在香港地區，可以使用 DeepSeek 或 Mistral 服務，但不能使用 ChatGPT、Claude 或 Gemini。

* 地區的 API 策略約與其應用程式策略相同。

* 使用 Cursor 而非 Visual Studio Code。

* 仍有一些情況需要使用 Visual Studio Code，例如在 git 合併編輯器情境下，我仍使用 `git config --global core.editor "code --wait"`。

* 自 Deepseek V3 發布之日起，我們不再需要訂閱任何 AI 工具。

* 使用 Gemini 或 Grok 以提示生成節日慶祝圖像，例如「生成包含文字姓名的快樂農曆蛇年圖像」。

* 即使在某些情況下，將原始文本提供給 AI 模型以創建表格，輸出的幾個地方可能會與輸入不同。例如，當使用 Deepseek V3 模型在 Cursor 中生成 pip 列表的表格時，可能會包括如 `1.极狐0` 的版本。這裡的 `极狐` 指的是中國的 GitLab 平台。

* 使用 Deepseek 或 Mistral API 以提示翻譯標題時，例如 `你是一名專業翻譯員。你正在將一個 Jekyll 部落格文章從英文翻譯成中文。{text}`，可能會導致錯誤的翻譯。除了你提供的文本，輸出中通常會有過多的翻譯。

* 雖然 Cursor 中的 AI 模型有時會提供部分正確的文本，但我們可以接受它們，因為我們可以添加後續指示來讓 AI 模型重新生成正確的部分。

* 如果不太可能有幫助，就避免向大型語言模型提供過多的上下文。例如，生成對話對話行時，避免提供 100 個話題點。大型語言模型已經包含了大量數據。

* [AI 助力 Git 提交訊息](./gitmessageai-en)

* [對話音频生成](./conversation-style-en)

* [Google Cloud 口述轉文](./speech-to-text-en)

* [嘗試 llama.cpp](./llama-cpp-en)

* [ChatGPT 中使用搜索的案例](./ai-search-en)

* [Deepseek、Mistral 和 Anthropic](./dma-en)
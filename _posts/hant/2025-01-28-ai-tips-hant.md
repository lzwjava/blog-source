---
audio: false
lang: hant
layout: post
title: AI 工具貼士
translated: true
---

* 將範例程式碼複製到 Cursor 中，並使用註釋提供上下文。

* 在香港地區，可以使用 DeepSeek 或 Mistral 服務，但不能使用 ChatGPT、Claude 或 Gemini。

* 一個地區的 API 政策與其應用程式政策大致相同。

* 使用 Cursor 代替 Visual Studio Code。

* 仍有一些情況需要使用 Visual Studio Code，例如 git merge editor 情境，我仍然使用 `git config --global core.editor "code --wait"`。

* 從 Deepseek V3 發佈日起，我們不需要訂閱任何 AI 工具。

* 使用 Gemini 或 Grok 根據提示生成節日慶祝圖片，例如「生成一個包含文字名稱的快樂農曆蛇年圖片」。

* 在某些情況下，即使向 AI 模型提供原文來創建表格，輸出中的某些地方也可能與輸入不同。例如，在 Cursor 中使用 Deepseek V3 模型生成 pip list 表格時，可能會包含例如 `1.極狐0` 的版本。這裡，「極狐」指的是中國的 GitLab 平台。

* 使用 DeepSeek 或 Mistral API 翻譯標題，例如提示 `You are a professional translator. You are translating a markdown file for a Jekyll blog post from English to Chinese. {text}`，可能會導致翻譯錯誤。除了您提供的文字外，輸出通常包含過多的翻譯。

* 儘管有時 Cursor 中的 AI 模型會給出部分正確的文字，但我們可以接受，因為我們可以添加後續說明，讓 AI 模型重新生成正確的部分。

* 如果不太可能有所幫助，請避免向大型語言模型提供過多的上下文。例如，在生成對話對白時，請避免提供關於某個主題的 100 個要點。大型語言模型已經包含大量的數據。

* 在提供充足上下文進行翻譯或生成對話歌詞等任務時，請避免使用 chain-of-thought 功能，因為它可能會很慢，並導致冗長或無用的回應。

* 測試聊天機器人是否能遵循用戶指令的一種方法是，要求它用英文解釋某事，然後用中文繼續輸入，觀察聊天機器人是否保持英文輸出。

* 我們在 AI 時代不使用 Postman 或 Figma 的一個原因是，它們的功能無法通過文字生成。它們也缺乏 command + K 快捷鍵來觸發組件替換。

* 在 AI 時代，用戶界面正成為一種障礙。為什麼要升級 Postman 以使其具備 AI 能力來測試應用程式，當我們可以直接使用 Python 的 requests 庫或其他程式語言來測試程式碼時，因為後者將由 AI 驅動？

* 為什麼要升級 Figma 以使其具備 AI 能力來創建用戶界面，當我們可以直接使用程式碼來生成用戶界面時，因為後者將由 AI 驅動？


* [AI 驅動的 Git 提交訊息](./gitmessageai-en)

* [對話音頻生成](./conversation-style-en)

* [Google Cloud 語音轉文字](./speech-to-text-en)

* [嘗試 llama.cpp](./llama-cpp-en)

* [在 ChatGPT 中使用搜尋的一個案例](./ai-search-en)

* [Deepseek、Mistral 和 Anthropic](./dma-en)

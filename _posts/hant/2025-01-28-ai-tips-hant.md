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

* 仍然有些情況需要使用 Visual Studio Code，例如 git merge editor 情境，我仍然使用 `git config --global core.editor "code --wait"`。

* 從 Deepseek V3 發佈之日起，我們不需要訂閱任何 AI 工具。

* 使用 Gemini 或 Grok 利用提示詞例如「生成一張包含姓名文字的喜慶農曆蛇年圖片」來生成節慶慶祝圖片。

* 有時即使提供原文本給 AI 模型生成表格，輸出結果在某些地方也可能與輸入有所不同。例如，在 Cursor 中使用 Deepseek V3 模型生成 pip list 表格時，可能會包含像 `1.極狐0` 這樣的版本號。此處，「極狐」指的是中國的 GitLab 平台。

* 使用 DeepSeek 或 Mistral API 翻譯標題，並使用提示詞例如「您是一位專業翻譯員。您正在將 Jekyll 網誌文章的 Markdown 檔案從英文翻譯成中文。{文字}」，可能會導致翻譯錯誤。除了您提供的文字外，輸出結果通常包含過多的翻譯內容。

* 儘管有時 Cursor 中的 AI 模型會給出部分正確的文字，我們也可以接受，因為我們可以添加後續指令讓 AI 模型重新生成正確的部分。

* 如果過多的上下文不太可能有幫助，請避免向大型語言模型提供過多的上下文。例如，在生成對話對白時，請避免提供 100 個關於某個主題的要點。大型語言模型已經包含大量的數據。

* 在提供足夠上下文執行翻譯或生成對話歌詞等任務時，避免使用 chain-of-thought 功能，因為它可能會很慢，並導致冗長或無用的回應。

* 測試聊天機器人是否能遵循使用者指令的一種方法是，要求它用英文解釋某事，然後用中文繼續輸入，觀察聊天機器人是否保持英文輸出。

* 我們在 AI 時代不使用 Postman 或 Figma 的其中一個原因是，它們的功能無法通過文字生成。它們也缺乏 command + K 快捷鍵來觸發組件替換。

* 在 AI 時代，使用者介面正成為一種障礙。為何要升級 Postman 以支援 AI 來測試應用程式，當我們可以直接使用 Python 的 requests 函式庫或其他程式語言來測試程式碼時，後者將由 AI 驅動？

* 為何要升級 Figma 以支援 AI 來建立使用者介面，當基於程式碼的使用者介面生成，透過 AI 加強，提供更直接且潛在更強大的方法時？

* LLM 將首先改變與文字相關的應用程式。


* [AI 驅動的 Git 提交訊息](./gitmessageai-en)

* [對話音訊生成](./conversation-style-en)

* [Google Cloud 語音轉文字](./speech-to-text-en)

* [嘗試 llama.cpp](./llama-cpp-en)

* [在 ChatGPT 中使用搜尋的案例](./ai-search-en)

* [Deepseek、Mistral 和 Anthropic](./dma-en)

---
audio: false
lang: hant
layout: post
title: AI工具小童谈
translated: true
---

* 將範例程式碼複製到Cursor中，並使用註解提供背景資訊。

* 在香港地區，使用DeepSeek或Mistral服務是可以接受的，而使用ChatGPT、Claude或Gemini則不可以。

* 某地區的API政策大約與其應用程式政策相同。

* 使用Cursor取代Visual Studio Code。

* 仍有需要使用Visual Studio Code的情況，例如在進行git merge editor的情境，我仍然使用`git config --global core.editor "code --wait"`。

* 從Deepseek V3發布之日起，我們不再需要訂閱任何AI工具。

* 使用Gemini或Grok生成節日慶祝圖片，提示如「生成一張包含名字文字的快樂農曆蛇年新年圖片」。

* 在某些情況下，即使提供原文給AI模型生成表格，輸出中的某些地方可能與輸入不同。例如，使用Cursor中的Deepseek V3模型生成pip list表格時，可能會包含版本如`1.极狐0`。這裡的`极狐`指的是中文的GitLab平台。

* 使用Deepseek或Mistral API翻譯標題時，當提示如`You are a professional translator. You are translating a markdown file for a Jekyll blog post from English to Chinese. {text}`時，可能會導致翻譯錯誤。除了您提供的文字外，輸出通常還包含過多的翻譯。
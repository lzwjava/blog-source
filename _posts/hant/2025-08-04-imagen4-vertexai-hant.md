---
audio: false
generated: true
image: false
lang: hant
layout: post
title: Vertex AI 的 Imagen 4 模型
translated: true
type: note
---

根據您提供的程式碼片段，您正在使用 `genai.Client` 與 Vertex AI 上的圖像生成模型進行互動。您指定的模型是 `"imagen-4.0-generate-preview-06-06"`。

以下是關於此模型的新功能及其代表的意義：

### Vertex AI 上最新的圖像生成模型

您使用的模型 `imagen-4.0-generate-preview-06-06` 屬於 Vertex AI 上最新的 **Imagen 4** 模型系列。此模型系列還包括：

* **`imagen-4.0-generate-preview-06-06`**：這是標準的 Imagen 4 模型，在速度和品質之間取得平衡。
* **`imagen-4.0-ultra-generate-preview-06-06`**：此「Ultra」版本專為更高品質而設計，但速度較慢且成本更高。
* **`imagen-4.0-fast-generate-preview-06-06`**：此「Fast」變體優先考慮速度和低延遲，而非最高品質。

這些 Imagen 4 模型是一次重大更新，建立在 Imagen 3 和 Imagen 2 等先前版本的基礎上。Imagen 4 的主要功能和更新包括：

* **改進的圖像品質**：新模型旨在生成比其前身更高品質的圖像。
* **更廣泛的長寬比支援**：Imagen 4 支援多種長寬比，包括 `1:1`、`3:4`、`4:3`、`9:16` 和 `16:9`，讓您能更好地控制輸出。
* **多語言提示**：雖然英語是主要語言，但這些模型也支援其他幾種語言的文字提示，包括中文（簡體和繁體）、印地語、日語、韓語、葡萄牙語和西班牙語（預覽版）。
* **安全功能**：模型包含用戶可配置的安全設定，並採用數位浮水印（SynthID）來識別 AI 生成的內容。

您程式碼片段中的 `person_generation` 和 `safety_filter_level` 參數仍然相關，允許您配置模型行為以實現負責任的 AI，正如您使用 `person_generation="ALLOW_ADULT"` 和 `safety_filter_level="BLOCK_LOW_AND_ABOVE"` 所做的那樣。

### 圖像生成之外

除了更新的 Imagen 模型，Google Cloud 最近還在 Vertex AI 上推出了其他新的生成式 AI 模型，包括：

* **Veo 3 和 Veo 3 Fast**：這些是最新的影片生成模型，允許您從文字或圖像提示建立高品質影片。Veo 3 適用於具有原生音訊和唇形同步等功能的高品質專業影片，而 Veo 3 Fast 則針對速度進行了優化。
* **Gemini 2.5 模型**：這些是 Gemini 模型系列的最新版本，包括 Gemini 2.5 Pro、Gemini 2.5 Flash 和 Gemini 2.5 Flash-Lite，為各種任務提供先進的推理能力、多模態性和改進的性能。
---
audio: false
generated: true
image: false
lang: hant
layout: post
title: Google Gen AI 圖像配置
translated: true
type: note
---

以下快速概覽：`image_size` 參數在 Google Gen AI (Gemini/Imagen) Python SDK 中並不支援。取而代之的是，您需選擇模型變體（每個變體都有預設的解析度）、控制**長寬比**，以及若需要更高像素數量時，應用**放大**功能。您還可以調整**壓縮**和**輸出格式**，以及常見的「圖片數量」、「負向提示」、「安全設定」和「人物生成」設定。

## 模型變體

您需選擇模型名稱——每個變體都有其預設解析度和效能特性：

* **imagen-3.0** 系列：

  * `imagen-3.0-generate-002`
  * `imagen-3.0-generate-001`
  * `imagen-3.0-fast-generate-001`
  * `imagen-3.0-capability-001`
* **imagen-4.0 (預覽)** 系列：

  * `imagen-4.0-generate-preview-06-06`
  * `imagen-4.0-fast-generate-preview-06-06`
  * `imagen-4.0-ultra-generate-preview-06-06`
* **舊版**：`imagegeneration@002`, `@005`, `@006` ([Google Cloud][1])

## 預設解析度

預設情況下，這些模型輸出的正方形（"1:1"）圖片為 **1024 × 1024 像素**。如果您需要較小的檔案，可以在本地進行降取樣；如果您需要更高解析度，請參閱下方的**放大**說明。([raymondcamden.com][2])

## 長寬比

與其指定絕對尺寸，不如在您的 `GenerateImagesConfig` 中使用 `aspect_ratio` 欄位。支援的值包括：

* `1:1` (正方形)
* `3:4` (較高，社交媒體肖像)
* `4:3` (經典攝影/電視)
* `16:9` (寬螢幕風景)
* `9:16` (高/肖像，例如手機背景) ([Google Cloud][1], [Google AI for Developers][3])

您可以在社群教學中找到相同的列表：

* DataCamp 指出 Imagen 3 完全使用這五種比例 ([DataCamp][4])
* CodeSignal 的指南也為 Gemini/Imagen 列舉了這些比例 ([CodeSignal][5])

## 放大

如果您需要真正的 "2K" 或 "4K" 輸出，請呼叫**放大**模式：

```python
from google.genai import types
config = types.GenerateImagesConfig(
    mode="upscale",
    upscale_config=types.UpscaleConfig(upscale_factor="x2"),
)
```

* `"x2"` 會使每個維度加倍（例如 1024 → 2048，約為 2K）
* `"x4"` 會使每個維度變為四倍（例如 1024 → 4096，約為 4K）([Google Cloud][1])

## 壓縮與格式

* **JPEG 品質**：使用 `compression_quality` (0–100，預設為 75) 來權衡檔案大小與細節 ([Google Cloud][1])
* **MIME 類型**：透過 `output_options.mime_type`，您可以選擇
  `image/jpeg`、`image/png`、`image/gif`、`image/webp`、`image/bmp`、`image/tiff` 或 `image/vnd.microsoft.icon` ([Google Cloud][6])

## 其他配置選項

其他所有設定都在 `GenerateImagesConfig` 中：

```python
config = types.GenerateImagesConfig(
    number_of_images=1,           # 要生成的圖片數量
    seed=1234,                    # 用於確定性輸出
    enhance_prompt=True,          # 基於 LLM 的提示詞改寫
    negative_prompt="排除狗",
    language="en",
    safety_filter_level="block_medium_and_above",  
    person_generation="allow_adult",
)
```

這些設定讓您可以控制隨機性、提示詞增強、安全閾值以及模型是否可以包含人物。([Google Cloud][1])

## 建議

移除您的 `image_size="2K"` 這行程式碼——沒有這樣的標誌。取而代之的是：

1. **選擇合適的模型**以平衡速度與品質。
2. 使用 **`aspect_ratio`** 來決定構圖。
3. 如果您確實需要更高的像素數量，請在基礎解析度下生成圖片，然後應用內建的**放大**功能（"x2" 或 "x4"）。
4. 調整 **compression_quality** 或在本地進行降取樣以獲得較小的檔案。

透過這些控制項，您可以實現正方形或電影比例的構圖、小尺寸或高解析度輸出，而無需使用不支援的 `image_size` 參數。

[1]: https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api "Generate images  |  Generative AI on Vertex AI  |  Google Cloud"
[2]: https://www.raymondcamden.com/2025/01/30/generative-ai-images-with-gemini-and-imagen-an-introduction?utm_source=chatgpt.com "Generative AI Images with Gemini and Imagen"
[3]: https://ai.google.dev/gemini-api/docs/imagen?utm_source=chatgpt.com "Generate images using Imagen | Gemini API | Google AI for ..."
[4]: https://www.datacamp.com/tutorial/imagen-3 "Imagen 3: A Guide With Examples in the Gemini API | DataCamp"
[5]: https://codesignal.com/learn/courses/creating-images-with-geminis-imagen-and-flask/lessons/generating-a-simple-image-with-geminis-imagen-and-flask?utm_source=chatgpt.com "Generating a Simple Image with Gemini's Imagen and Flask"
[6]: https://cloud.google.com/vertex-ai/generative-ai/docs/image/generate-images?utm_source=chatgpt.com "Generate images using text prompts"
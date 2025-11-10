---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 封鎖低階及以上
translated: true
type: note
---

你遇到的錯誤是：

```
Only block_low_and_above is supported for safetySetting.
```

當你在 **Imagen‑4** 模型中為 `GenerateImagesConfig` 設定 `safety_filter_level="BLOCK_MEDIUM_AND_ABOVE"`（或任何其他值）時會出現此錯誤——但在你發送請求時（2025年8月），**該 API 僅允許在這些模型上使用 `"BLOCK_LOW_AND_ABOVE"`** 進行圖片安全過濾（[Google Cloud][1]）。

---

### ✅ 如何修正你的程式碼

只需將 `safety_filter_level` 更新為支援的值：

```python
from google import genai
from google.genai.types import GenerateImagesConfig

client = genai.Client()

image = client.models.generate_images(
    model="imagen-4.0-generate-preview-06-06",
    prompt="A dog reading a newspaper",
    config=GenerateImagesConfig(
        image_size="2K",
        number_of_images=1,
        safety_filter_level="BLOCK_LOW_AND_ABOVE",
        person_generation="ALLOW_ADULT",
    ),
)

image.generated_images[0].image.save("output-image.png")
print(
    f"Created image using {len(image.generated_images[0].image.image_bytes)} bytes"
)
```

* `safety_filter_level="BLOCK_LOW_AND_ABOVE"`：這是 **Imagen 4** 唯一支援的值。其他閾值如 `"BLOCK_MEDIUM_AND_ABOVE"` 會導致 400 INVALID\_ARGUMENT 錯誤（[Medium][2], [Google AI for Developers][3]）。
* `number_of_images=1` 是明確設定的，以便清楚顯示你每次呼叫請求一張圖片。

---

### 🧾 其他可選參數：

* `person_generation="ALLOW_ADULT"` 是預設設定，但明確寫出來也沒問題（會阻擋兒童圖像；允許成人領域的圖片）（[Google Cloud][1]）。
* `image_size="2K"` 在你的程式碼中是有效的——只需確保你的 SDK 版本支援它。

---

### TL;DR — 快速檢查清單

| 步驟 | 要做什麼                                                   |
| ---- | ------------------------------------------------------------ |
| ✅ 1  | 將 safety\_filter\_level 改為 `"BLOCK_LOW_AND_ABOVE"`      |
| 🧾 2 | 保留 `person_generation="ALLOW_ADULT"`（或省略使用預設值） |
| 🚫 3 | 不要使用 `"BLOCK_MEDIUM_AND_ABOVE"` 或 `"BLOCK_ONLY_HIGH"`  |
| ⏱ 4  | 在 Google 增加更多級別之前，不要再更改安全設定      |

如果你遇到其他錯誤，請告訴我——很樂意幫忙！

[1]: https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api?utm_source=chatgpt.com "Generate images | Generative AI on Vertex AI"
[2]: https://medium.com/generative-ai/3-ways-to-try-googles-imagen-4-image-generator-if-you-re-outside-the-us-ee2a1895ca9b?utm_source=chatgpt.com "3 Ways to Try Google's Imagen 4 Image Generator if You're ..."
[3]: https://ai.google.dev/gemini-api/docs/migrate?utm_source=chatgpt.com "Migrate to the Google GenAI SDK - Gemini API"
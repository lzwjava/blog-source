---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 移除寬度和高度
translated: true
type: note
---

您遇到的錯誤：

```
Extra inputs are not permitted [type=extra_forbidden, input_value=1200, input_type=int]
```

是由於將 `width` 和 `height` 傳入 `GenerateImagesConfig` 所導致，該配置**不支援**這些欄位。根據錯誤訊息和 Gemini 的 API 設計，`image_size` 必須是**預定義的枚舉值**之一，且目前公開的 Gemini API **不支援** `CUSTOM` 尺寸（截至目前為止）。

---

### ✅ 修正方案

您應該**移除** `width` 和 `height` 參數，並使用有效的 `image_size` 枚舉值，例如 `"1024x1024"` 或 `"512x512"`。

以下是修正後的版本：

```python
from google import genai
from google.genai.types import GenerateImagesConfig
import os

# 設定 Vertex AI 客戶端
client = genai.Client(
    vertexai=True,
    project=os.getenv('GOOGLE_CLOUD_PROJECT'),
    location=os.getenv('GOOGLE_CLOUD_LOCATION')
)

image = client.models.generate_images(
    model="imagen-4.0-generate-preview-06-06",
    prompt="A dog reading a newspaper",
    config=GenerateImagesConfig(
        image_size="1024x1024",  # 使用允許的值代替 CUSTOM
        number_of_images=1,
        safety_filter_level="BLOCK_LOW_AND_ABOVE",
        person_generation="ALLOW_ADULT",
    ),
)

print(f"Created OG image using {len(image.generated_images[0].image.image_bytes)} bytes")
```

---

### 🔍 若要生成**自訂尺寸圖片**如 `1200x630`：

目前的 Gemini/Imagen 公開 API **不支援**任意圖片尺寸。如果您需要 1200×630 尺寸（例如用於 OG 圖片），您的選擇是：

1. **後處理生成後的圖片**，將其調整/裁剪至所需尺寸。
2. 使用**其他支援自訂尺寸的模型/API**（例如 Stability AI 的 SDXL、Midjourney 或私有端點）。
3. 如果您擁有內部存取權限（例如在 Google 內部使用），請查閱內部文件或聯繫您的 Vertex AI 客戶經理確認。

如果您需要協助在圖片生成後調整尺寸，請告訴我。
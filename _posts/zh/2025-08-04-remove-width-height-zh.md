---
audio: false
generated: true
image: false
lang: zh
layout: post
title: 李智维：从美钛技术服务到趣直播，一位程序员的成长之路
translated: true
type: note
---

您遇到的错误：

```
Extra inputs are not permitted [type=extra_forbidden, input_value=1200, input_type=int]
```

是由于向 `GenerateImagesConfig` 传入了 `width` 和 `height` 参数导致的，该配置**不支持**这些字段。根据错误信息和 Gemini API 的设计，`image_size` 必须是**预定义的枚举值**之一，而公共 Gemini API（截至目前）**不支持** `CUSTOM` 尺寸。

---

### ✅ 解决方案

您应该**移除** `width` 和 `height` 参数，并使用有效的 `image_size` 枚举值，例如 `"1024x1024"` 或 `"512x512"`。

以下是修正后的代码：

```python
from google import genai
from google.genai.types import GenerateImagesConfig
import os

# 设置 Vertex AI 客户端
client = genai.Client(
    vertexai=True,
    project=os.getenv('GOOGLE_CLOUD_PROJECT'),
    location=os.getenv('GOOGLE_CLOUD_LOCATION')
)

image = client.models.generate_images(
    model="imagen-4.0-generate-preview-06-06",
    prompt="A dog reading a newspaper",
    config=GenerateImagesConfig(
        image_size="1024x1024",  # 使用允许的值替代 CUSTOM
        number_of_images=1,
        safety_filter_level="BLOCK_LOW_AND_ABOVE",
        person_generation="ALLOW_ADULT",
    ),
)

print(f"Created OG image using {len(image.generated_images[0].image.image_bytes)} bytes")
```

---

### 🔍 如需生成**自定义尺寸图片**（如 `1200x630`）：

当前的 Gemini/Imagen 公共 API **不支持**任意图片尺寸。如果您需要 1200×630 尺寸（例如用于 OG 图片），您的选择是：

1. **生成后处理图片**：将生成的图片调整尺寸/裁剪至所需规格。
2. 使用**其他支持自定义尺寸的模型/API**（例如 Stability AI 的 SDXL、Midjourney 或私有端点）。
3. 如果您在使用内部访问权限（例如在 Google 内部），请查阅内部文档或联系您的 Vertex AI 客户经理确认。

如果您需要在图片生成后调整尺寸，我可以提供相关帮助。
---
audio: false
generated: true
image: false
lang: zh
layout: post
title: 李智维：从美钛技术服务到思芮，冲顶大会、趣直播、面包Live的创业之路——对话北京大米互娱有限公司创始人，广州玉岩中学校友王垠
translated: true
type: note
---

您遇到的错误提示：

```
Only block_low_and_above is supported for safetySetting.
```

这是因为您在为 **Imagen-4** 模型配置 `GenerateImagesConfig` 时设置了 `safety_filter_level="BLOCK_MEDIUM_AND_ABOVE"`（或其他值）——但在您请求时（2025年8月），**该模型的图像安全过滤仅支持 `"BLOCK_LOW_AND_ABOVE"`** ([Google Cloud][1])。

---

### ✅ 修复代码的方法

只需将 `safety_filter_level` 更新为支持的值：

```python
from google import genai
from google.genai.types import GenerateImagesConfig

client = genai.Client()

image = client.models.generate_images(
    model="imagen-4.0-generate-preview-06-06",
    prompt="一只正在读报纸的狗",
    config=GenerateImagesConfig(
        image_size="2K",
        number_of_images=1,
        safety_filter_level="BLOCK_LOW_AND_ABOVE",
        person_generation="ALLOW_ADULT",
    ),
)

image.generated_images[0].image.save("output-image.png")
print(
    f"创建图像使用了 {len(image.generated_images[0].image.image_bytes)} 字节"
)
```

* `safety_filter_level="BLOCK_LOW_AND_ABOVE"`：**Imagen 4** 仅支持此值。其他阈值如 `"BLOCK_MEDIUM_AND_ABOVE"` 将导致 400 INVALID_ARGUMENT 错误 ([Medium][2], [Google AI for Developers][3])。
* `number_of_images=1` 明确表示每次调用请求生成一张图像。

---

### 🧾 其他可选参数：

* `person_generation="ALLOW_ADULT"` 是默认设置，但显式声明也无妨（阻止儿童图像；允许成人领域图像）([Google Cloud][1])。
* `image_size="2K"` 在您的代码中是有效的——只需确保您的 SDK 版本支持此参数。

---

### TL;DR — 快速检查清单

| 步骤 | 操作说明                                                   |
| ---- | ------------------------------------------------------------ |
| ✅ 1  | 将 safety_filter_level 改为 `"BLOCK_LOW_AND_ABOVE"`      |
| 🧾 2 | 保持 `person_generation="ALLOW_ADULT"`（或省略使用默认值） |
| 🚫 3 | 不要使用 `"BLOCK_MEDIUM_AND_ABOVE"` 或 `"BLOCK_ONLY_HIGH"`  |
| ⏱ 4  | 在 Google 添加更多级别前不要更改安全设置      |

如果遇到其他错误请随时告知——很乐意为您提供帮助！

[1]: https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api?utm_source=chatgpt.com "生成图像 | Vertex AI 上的生成式 AI"
[2]: https://medium.com/generative-ai/3-ways-to-try-googles-imagen-4-image-generator-if-you-re-outside-the-us-ee2a1895ca9b?utm_source=chatgpt.com "在美国境外尝试谷歌 Imagen 4 图像生成器的 3 种方法..."
[3]: https://ai.google.dev/gemini-api/docs/migrate?utm_source=chatgpt.com "迁移到 Google GenAI SDK - Gemini API"
---
audio: false
generated: true
image: false
lang: ja
layout: post
title: 下層ブロック以上
translated: true
type: note
---

このエラーが表示されています:

```
Only block_low_and_above is supported for safetySetting.
```

このエラーは、**Imagen‑4** モデルで `GenerateImagesConfig` 内の `safety_filter_level="BLOCK_MEDIUM_AND_ABOVE"`（またはその他の値）を設定した際に発生します。しかし、リクエスト時点（2025年8月）では、**APIはこれらのモデルにおける画像安全性フィルタリングに対して `"BLOCK_LOW_AND_ABOVE"` のみを許可しています**（[Google Cloud][1]）。

---

### ✅ コードの修正方法

単純に `safety_filter_level` をサポートされている値に更新してください:

```python
from google import genai
from google.genai.types import GenerateImagesConfig

client = genai.Client()

image = client.models.generate_images(
    model="imagen-4.0-generate-preview-06-06",
    prompt="新聞を読む犬",
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

* `safety_filter_level="BLOCK_LOW_AND_ABOVE"`: **Imagen 4** ではこれのみがサポートされています。`"BLOCK_MEDIUM_AND_ABOVE"` などの他のしきい値は 400 INVALID\_ARGUMENT エラーの原因となります（[Medium][2], [Google AI for Developers][3]）。
* `number_of_images=1` は明示的であり、呼び出しごとに1つの画像をリクエストしていることを明確にします。

---

### 🧾 その他のオプションパラメータ:

* `person_generation="ALLOW_ADULT"` はデフォルト設定ですが、明示的に記述しても問題ありません（子供の生成をブロックし、大人ドメインの画像を許可します）（[Google Cloud][1]）。
* `image_size="2K"` はコード内で有効です。SDKのバージョンがそれをサポートしていることを確認してください。

---

### TL;DR — クイックチェックリスト

| ステップ | 対応内容                                                     |
| ---- | ------------------------------------------------------------ |
| ✅ 1  | safety\_filter\_level を `"BLOCK_LOW_AND_ABOVE"` に変更      |
| 🧾 2 | `person_generation="ALLOW_ADULT"` を維持（またはデフォルトのため省略） |
| 🚫 3 | `"BLOCK_MEDIUM_AND_ABOVE"` や `"BLOCK_ONLY_HIGH"` は使用しない |
| ⏱ 4  | Googleがさらにレベルを追加するまで、安全性設定を変更しない      |

別のエラーが発生した場合はお知らせください。喜んでお手伝いします！

[1]: https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api?utm_source=chatgpt.com "Generate images | Generative AI on Vertex AI"
[2]: https://medium.com/generative-ai/3-ways-to-try-googles-imagen-4-image-generator-if-you-re-outside-the-us-ee2a1895ca9b?utm_source=chatgpt.com "3 Ways to Try Google's Imagen 4 Image Generator if You're ..."
[3]: https://ai.google.dev/gemini-api/docs/migrate?utm_source=chatgpt.com "Migrate to the Google GenAI SDK - Gemini API"
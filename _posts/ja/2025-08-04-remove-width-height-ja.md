---
audio: false
generated: true
image: false
lang: ja
layout: post
title: 幅と高さを削除
translated: true
type: note
---

以下のエラーが表示されています：

```
Extra inputs are not permitted [type=extra_forbidden, input_value=1200, input_type=int]
```

このエラーは、`GenerateImagesConfig` に `width` と `height` を渡したことが原因です。この設定は**それらのフィールドをサポートしていません**。エラーメッセージとGeminiのAPI設計によると、`image_size` は**事前定義された列挙値**のいずれかでなければならず、パブリックなGemini APIでは（現時点では）`CUSTOM` は**サポートされていません**。

---

### ✅ 修正方法

`width` と `height` を**削除**し、`"1024x1024"` や `"512x512"` などの有効な `image_size` 列挙値を使用する必要があります。

修正後のコードは以下の通りです：

```python
from google import genai
from google.genai.types import GenerateImagesConfig
import os

# Vertex AIクライアントをセットアップ
client = genai.Client(
    vertexai=True,
    project=os.getenv('GOOGLE_CLOUD_PROJECT'),
    location=os.getenv('GOOGLE_CLOUD_LOCATION')
)

image = client.models.generate_images(
    model="imagen-4.0-generate-preview-06-06",
    prompt="A dog reading a newspaper",
    config=GenerateImagesConfig(
        image_size="1024x1024",  # CUSTOMの代わりに許可された値を使用
        number_of_images=1,
        safety_filter_level="BLOCK_LOW_AND_ABOVE",
        person_generation="ALLOW_ADULT",
    ),
)

print(f"Created OG image using {len(image.generated_images[0].image.image_bytes)} bytes")
```

---

### 🔍 **カスタムサイズの画像**（例: `1200x630`）を生成するには：

現在のGemini/ImagenのパブリックAPIは、任意の画像サイズを**サポートしていません**。1200×630（例：OG画像用）が必要な場合の選択肢は以下の通りです：

1. 生成後の画像を**後処理**して、希望のサイズにリサイズ/クロップする。
2. カスタムサイズをサポートする**別のモデル/API**を使用する（例：Stability AIのSDXL、Midjourney、またはプライベートエンドポイント）。
3. 内部アクセス（例：Google内）を使用している場合は、内部ドキュメントまたはVertex AIアカウントマネージャーに確認する。

生成後の画像リサイズについてヘルプが必要な場合はお知らせください。
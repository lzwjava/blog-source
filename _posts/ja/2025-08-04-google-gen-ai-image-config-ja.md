---
audio: false
generated: true
image: false
lang: ja
layout: post
title: Google Gen AI 画像設定
translated: true
type: note
---

以下に簡単な概要を示します：`image_size`パラメータはGoogle Gen AI（Gemini/Imagen）Python SDKではサポートされていません。代わりに、モデルバリアント（それぞれが暗黙的なデフォルト解像度を持っています）から選択し、**アスペクト比**を制御し、より高いピクセル数が必要な場合は**アップスケール**を適用します。また、**圧縮**と**出力形式**、さらに通常の「画像数」、「ネガティブプロンプト」、「安全性」、「人物」設定も調整できます。

## モデルバリアント

モデル名を選択します。各バリアントには独自のデフォルト解像度とパフォーマンスプロファイルがあります：

* **imagen-3.0** ファミリー：

  * `imagen-3.0-generate-002`
  * `imagen-3.0-generate-001`
  * `imagen-3.0-fast-generate-001`
  * `imagen-3.0-capability-001`
* **imagen-4.0 (プレビュー)** ファミリー：

  * `imagen-4.0-generate-preview-06-06`
  * `imagen-4.0-fast-generate-preview-06-06`
  * `imagen-4.0-ultra-generate-preview-06-06`
* **レガシー**: `imagegeneration@002`, `@005`, `@006` ([Google Cloud][1])

## デフォルト解像度

デフォルトでは、これらのモデルからの正方形（「1:1」）出力は**1024 × 1024ピクセル**です。より小さいファイルが必要な場合は、ローカルでダウンサンプリングできます。より高い解像度が必要な場合は、以下の**アップスケーリング**を参照してください。([raymondcamden.com][2])

## アスペクト比

絶対的な寸法を指定する代わりに、`GenerateImagesConfig`の`aspect_ratio`フィールドを使用します。サポートされている値：

* `1:1` (正方形)
* `3:4` (縦長、ソーシャルメディアのポートレート)
* `4:3` (クラシックな写真/TV)
* `16:9` (ワイドスクリーンの風景)
* `9:16` (縦長/ポートレート、例：電話の背景) ([Google Cloud][1], [Google AI for Developers][3])

コミュニティチュートリアルでも同じリストが確認できます：

* DataCampはImagen 3に対してこれら5つの比率を正確に指摘しています ([DataCamp][4])
* CodeSignalのガイドもGemini/Imagenに対してそれらを列挙しています ([CodeSignal][5])

## アップスケーリング

真の「2K」または「4K」出力が必要な場合は、**アップスケール**モードを呼び出します：

```python
from google.genai import types
config = types.GenerateImagesConfig(
    mode="upscale",
    upscale_config=types.UpscaleConfig(upscale_factor="x2"),
)
```

* `"x2"` は各次元を2倍にします（例：1024 → 2048、およそ2K）
* `"x4"` は4倍にします（例：1024 → 4096、およそ4K） ([Google Cloud][1])

## 圧縮と形式

* **JPEG品質**: `compression_quality` (0–100、デフォルト75)を使用して、ファイルサイズと詳細のトレードオフを調整します ([Google Cloud][1])
* **MIMEタイプ**: `output_options.mime_type`を通じて、`image/jpeg`、`image/png`、`image/gif`、`image/webp`、`image/bmp`、`image/tiff`、または`image/vnd.microsoft.icon`を選択できます ([Google Cloud][6])

## 追加の設定オプション

その他すべては`GenerateImagesConfig`に含まれます：

```python
config = types.GenerateImagesConfig(
    number_of_images=1,           # 生成する画像の数
    seed=1234,                    # 決定論的な出力のため
    enhance_prompt=True,          # LLMベースのプロンプト書き換え
    negative_prompt="犬を除外",
    language="en",
    safety_filter_level="block_medium_and_above",  
    person_generation="allow_adult",
)
```

これらにより、ランダム性、プロンプトの強化、安全性の閾値、モデルが人物を含むことができるかどうかを制御できます。([Google Cloud][1])

## 推奨事項

`image_size="2K"`の行を削除してください。そのようなフラグは存在しません。代わりに：

1. 速度と品質に応じて**適切なモデルを選択**します。
2. フレーミングには**`aspect_ratio`**を使用します。
3. 本当に高いピクセル数が必要な場合は、基本解像度で生成した後、組み込みの**アップスケール**（「x2」または「x4」）を適用します。
4. より小さいファイルが必要な場合は、**compression\_quality**を調整するか、ローカルでダウンサンプリングします。

これらの設定を使用することで、サポートされていない`image_size`パラメータなしで、正方形またはシネマティックなフレーミング、小さなまたは高解像度の出力を実現できます。

[1]: https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api "Generate images  |  Generative AI on Vertex AI  |  Google Cloud"
[2]: https://www.raymondcamden.com/2025/01/30/generative-ai-images-with-gemini-and-imagen-an-introduction?utm_source=chatgpt.com "Generative AI Images with Gemini and Imagen"
[3]: https://ai.google.dev/gemini-api/docs/imagen?utm_source=chatgpt.com "Generate images using Imagen | Gemini API | Google AI for ..."
[4]: https://www.datacamp.com/tutorial/imagen-3 "Imagen 3: A Guide With Examples in the Gemini API | DataCamp"
[5]: https://codesignal.com/learn/courses/creating-images-with-geminis-imagen-and-flask/lessons/generating-a-simple-image-with-geminis-imagen-and-flask?utm_source=chatgpt.com "Generating a Simple Image with Gemini's Imagen and Flask"
[6]: https://cloud.google.com/vertex-ai/generative-ai/docs/image/generate-images?utm_source=chatgpt.com "Generate images using text prompts"
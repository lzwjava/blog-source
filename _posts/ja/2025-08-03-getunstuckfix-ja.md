---
audio: false
generated: true
image: false
lang: ja
layout: post
title: 公式固定版Imagen Pythonスニペット
translated: true
type: note
---

基本的に正しいロジックは実装されていますが、**get‑unstuck** の手順が少し間違っています。以下は公式ドキュメントの例を元に整理したバージョンです：

```python
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

# ← APIキーを設定するか、環境変数 GOOGLE_API_KEY / GEMINI_API_KEY を使用
client = genai.Client(api_key="YOUR_API_KEY")

response = client.models.generate_images(
    model="imagen-4.0-generate-preview-06-06",
    prompt="A dog reading a newspaper",
    config=types.GenerateImagesConfig(
        number_of_images=1,
        # image_size="2K",  # 2K解像度の場合（オプション）；新しいfast-previewライブラリが必要
        aspect_ratio="1:1",
        safety_filter_level="BLOCK_MEDIUM_AND_ABOVE",
        person_generation="ALLOW_ADULT",
    )
)

for i, generated in enumerate(response.generated_images):
    raw = generated.image.image_bytes
    pil = Image.open(BytesIO(raw))  # 生のバイトデータをPIL画像に変換
    pil.save(f"output-image-{i+1}.png")
    print(f"Saved image {i+1}, {len(raw):,} bytes")
```

GoogleのPythonスニペットでも4‑previewモデルで `image_size="2K"` を使用していましたが、以下の点に注意してください：

* Imagen 4モデルで `image_size` をサポートするには `google-genai` v1.28以上が必要です
* それ以外の場合はこのフィールドを省略してください（デフォルトは1,024×1,024の固定正方形解像度です）（[GitHub][1]）

---

### 🚩 よくある落とし穴と修正方法

1. **PILのインストール不足**
   `google-genai` をインストールしても `Pillow` を追加していない場合、`.image.save()` の呼び出しが暗黙的に失敗する（または `AttributeError` が発生する）可能性があります。以下を確認してください：

   ```bash
   pip install pillow
   ```

2. **APIキーがない、または誤ったサービスが選択されている**
   クラウド資格情報なしでAPIキーも指定せずに `genai.Client()` を呼び出すと、呼び出し時に認証エラー（例：`"401 UNAUTHENTICATED"`）でクライアントが失敗します。Gemini Developer APIでは、`api_key="…"` を渡すか、シェルで `GOOGLE_API_KEY` を設定してください（[GitHub][1]）

3. **ライブラリのバージョン不一致**
   古いバージョンのライブラリやレガシーな `google.generativeai` モジュールは `generate_images()` を公開しておらず、*非推奨*のgenerative-aiインターフェースをデフォルトで使用する場合があります。常に以下を確認してください：

   ```bash
   pip install --upgrade google-genai
   ```

   古いリポジトリ（`deprecated-generative-ai-python`）での「出力画像を開けない」問題は、この不一致が原因で発生し、壊れたバイトを書き込んだ後に `UnidentifiedImageError` や `FileNotFoundError` がスローされることが一般的でした（[GitHub][1]）

4. **PILで開く際のUnidentifiedImageError**
   以下のエラーが表示される場合：

   ```
   PIL.UnidentifiedImageError: cannot identify image file <_io.BytesIO …>
   ```

   これは通常、レスポンスバッファが破損しているか不完全であることを意味します。以下を再確認してください：

   * プロンプトがフィルタリングされていないこと（例：RAIブロック）
   * バイトデータをbase64デコードしていないこと（SDKは既に生のPNG/JPEGデータを返します）
   * ファイルのダウンロードが途中で切断されていないこと

---

### ✅ この修正が機能する理由

* 2025‑08‑01時点のGoogle公式ドキュメントのスニペットでは、以下を正確に使用しています：

  ```python
  types.GenerateImagesConfig(image_size="2K")
  ```

  その後 `result.image.save(...)` で保存しています（[Google Cloud][2]）

* しかし、Imagen 3モデルを使用する他のガイドでは、`image_size` を指定せずに `number_of_images`、`aspect_ratio`、安全設定のみを指定しています。これはImagen 3がそれをサポートしていないためです（[GitHub][1]）

上記の流れに従うことで問題を解決できるはずです。特定のエラーメッセージ（HTTP 403、レスポンスにJSONキーがないなど）が表示される場合は、それを貼り付けてください。次のステップのトラブルシューティングをお手伝いします。

[1]: https://github.com/google-gemini/generative-ai-python/issues/674?utm_source=chatgpt.com "can not open the output images from imagen API · Issue #674 · google-gemini/deprecated-generative-ai-python · GitHub"
[2]: https://cloud.google.com/vertex-ai/generative-ai/docs/image/overview?utm_source=chatgpt.com "Imagen on Vertex AI | AI Image Generator"
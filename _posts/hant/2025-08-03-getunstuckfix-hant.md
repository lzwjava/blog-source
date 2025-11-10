---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 固定官方 Imagen Python 代碼片段
translated: true
type: note
---

你基本上已經實現了正確的邏輯，但 **get‑unstuck** 的說明略有偏差。以下是根據官方文件範例整理後的版本：

```python
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

# ← 設定你的 API 金鑰或使用環境變數 GOOGLE_API_KEY / GEMINI_API_KEY
client = genai.Client(api_key="YOUR_API_KEY")

response = client.models.generate_images(
    model="imagen-4.0-generate-preview-06-06",
    prompt="A dog reading a newspaper",
    config=types.GenerateImagesConfig(
        number_of_images=1,
        # image_size="2K",  # 可選用於 2K 解析度；需要較新的 fast-preview 函式庫
        aspect_ratio="1:1",
        safety_filter_level="BLOCK_MEDIUM_AND_ABOVE",
        person_generation="ALLOW_ADULT",
    )
)

for i, generated in enumerate(response.generated_images):
    raw = generated.image.image_bytes
    pil = Image.open(BytesIO(raw))  # 將原始位元組轉換為 PIL 影像
    pil.save(f"output-image-{i+1}.png")
    print(f"已儲存影像 {i+1}，大小 {len(raw):,} 位元組")
```

雖然 Google 的 Python 程式碼片段也在其 4‑preview 模型中使用了 `image_size="2K"`，但請注意：

* 你必須執行 `google-genai` v1.28 或更新版本，才能在 Imagen 4 模型上支援 `image_size`；
* 否則請省略該欄位（預設為 1,024×1,024 的固定正方形像素解析度）([GitHub][1])。

---

### 🚩 常見陷阱與修正方法

1. **缺少 PIL 安裝**
   如果你安裝了 `google-genai` 但未添加 `Pillow`，則 `.image.save()` 呼叫可能會無聲失敗（或引發 `AttributeError`）。請確保：

   ```bash
   pip install pillow
   ```

2. **沒有 API 金鑰或選擇了錯誤的服務**
   如果你在沒有 API 金鑰且沒有雲端憑證的情況下呼叫 `genai.Client()`，客戶端會在呼叫時因認證錯誤而失敗（例如 `"401 UNAUTHENTICATED"`）。請傳入 `api_key="…"` 或在 shell 中設定 `GOOGLE_API_KEY`，用於 Gemini Developer API ([GitHub][1])。

3. **函式庫版本不匹配**
   舊版本的函式庫或舊版 `google.generativeai` 模組可能不會公開 `generate_images()`，並且可能仍預設使用 *已棄用* 的 generative-ai 介面。請務必確保：

   ```bash
   pip install --upgrade google-genai
   ```

   在舊版儲存庫（`deprecated-generative-ai-python`）中出現的「無法開啟輸出影像」問題是由於版本不匹配所致，通常在寫入損壞的位元組後會拋出 `UnidentifiedImageError` 或 `FileNotFoundError` ([GitHub][1])。

4. **使用 PIL 開啟時出現 UnidentifiedImageError**
   如果你看到：

   ```
   PIL.UnidentifiedImageError: cannot identify image file <_io.BytesIO …>
   ```

   這通常表示回應緩衝區已損壞或不完整。請仔細檢查：

   * 你的提示詞未被過濾（例如被 RAI 阻擋）；
   * 你沒有對位元組進行 base64 解碼（SDK 已經回傳原始 PNG/JPEG 資料）；
   * 你的檔案下載沒有被中途截斷。

---

### ✅ 此修正為何有效

* Google 文件於 2025‑08‑01 的官方程式碼片段明確使用了：

  ```python
  types.GenerateImagesConfig(image_size="2K")
  ```

  然後透過 `result.image.save(...)` 儲存 ([Google Cloud][2])。

* 但其他使用 Imagen 3 模型的指南僅指定了 `number_of_images`、`aspect_ratio` 和安全設定——沒有 `image_size`——因為 Imagen 3 不支援該參數 ([GitHub][1])。

遵循上述流程應能解決你的問題。如果你遇到特定的錯誤訊息（例如 HTTP 403、回應中缺少 JSON 鍵等），請隨時貼回該訊息，我將協助你進行下一步的疑難排解。

[1]: https://github.com/google-gemini/generative-ai-python/issues/674?utm_source=chatgpt.com "can not open the output images from imagen API · Issue #674 · google-gemini/deprecated-generative-ai-python · GitHub"
[2]: https://cloud.google.com/vertex-ai/generative-ai/docs/image/overview?utm_source=chatgpt.com "Imagen on Vertex AI | AI Image Generator"
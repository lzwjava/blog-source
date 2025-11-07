---
audio: false
generated: true
image: false
lang: en
layout: post
title: Fixed Official Imagen Python Snippet
translated: false
---

You've basically implemented the correct logic, but the **get‑unstuck** instructions are slightly off. Here's a cleaned‑up version adapted from the official example in the docs:

```python
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

# ← Set your API key or use the environment variable GOOGLE_API_KEY / GEMINI_API_KEY
client = genai.Client(api_key="YOUR_API_KEY")

response = client.models.generate_images(
    model="imagen-4.0-generate-preview-06-06",
    prompt="A dog reading a newspaper",
    config=types.GenerateImagesConfig(
        number_of_images=1,
        # image_size="2K",  # optional for 2K resolution; requires newer fast-preview library
        aspect_ratio="1:1",
        safety_filter_level="BLOCK_MEDIUM_AND_ABOVE",
        person_generation="ALLOW_ADULT",
    )
)

for i, generated in enumerate(response.generated_images):
    raw = generated.image.image_bytes
    pil = Image.open(BytesIO(raw))  # Convert raw bytes into a PIL image
    pil.save(f"output-image-{i+1}.png")
    print(f"Saved image {i+1}, {len(raw):,} bytes")
```

While Google’s Python snippet also used `image_size="2K"` for its 4‑preview model, be aware that:

* You must be running `google-genai` v1.28 or newer to support `image_size` on Imagen 4 models;
* Otherwise omit that field (the default is 1,024×1,024 at a fixed square pixel resolution) ([GitHub][1]).

---

### 🚩 Common Pitfalls & Fixes

1. **Missing PIL installation**
   If you installed `google-genai` but didn’t add `Pillow`, `.image.save()` calls may fail silently (or raise `AttributeError`). Make sure:

   ```bash
   pip install pillow
   ```

2. **No API key or wrong service selected**
   If you call `genai.Client()` with no API key and without cloud credentials, the client fails at call-time with an authentication error (e.g., `"401 UNAUTHENTICATED"`). Either pass `api_key="…"` or set `GOOGLE_API_KEY` in your shell, for Gemini Developer API ([GitHub][1]).

3. **Library version mismatch**
   Older versions of the library or legacy `google.generativeai` module don’t expose `generate_images()` and may still default to the *deprecated* generative-ai interface. Always ensure:

   ```bash
   pip install --upgrade google-genai
   ```

   The issue “cannot open the output images” in older repos (`deprecated-generative-ai-python`) resulted from that mismatch, and usually threw `UnidentifiedImageError` or `FileNotFoundError` after writing broken bytes ([GitHub][1]).

4. **UnidentifiedImageError when opening with PIL**
   If you see:

   ```
   PIL.UnidentifiedImageError: cannot identify image file <_io.BytesIO …>
   ```

   that usually means the response buffer is corrupted or incomplete. Double-check that:

   * Your prompt wasn’t filtered (e.g. RAI blocking);
   * You aren’t base64‑decoding the bytes (the SDK already returns raw PNG/JPEG data);
   * Your file download isn’t cut short.

---

### ✅ Why This Fix Works

* The official snippet in Google’s docs on 2025‑08‑01 exactly uses:

  ```python
  types.GenerateImagesConfig(image_size="2K")
  ```

  before saving via `result.image.save(...)` ([Google Cloud][2]).

* But other guides using Imagen 3–models only specify `number_of_images`, `aspect_ratio`, and safety settings—without `image_size`—because Imagen 3 doesn’t support it ([GitHub][1]).

Following the flow above should get you unblocked. If you run into a specific error message (like HTTP 403, missing JSON key in response, etc.), feel free to paste that back and I’ll help you troubleshoot the next step.

[1]: https://github.com/google-gemini/generative-ai-python/issues/674?utm_source=chatgpt.com "can not open the output images from imagen API · Issue #674 · google-gemini/deprecated-generative-ai-python · GitHub"
[2]: https://cloud.google.com/vertex-ai/generative-ai/docs/image/overview?utm_source=chatgpt.com "Imagen on Vertex AI | AI Image Generator"
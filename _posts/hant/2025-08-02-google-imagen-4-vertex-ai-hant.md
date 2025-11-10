---
audio: false
generated: true
image: false
lang: hant
layout: post
title: Google Imagen 4 預覽指南
translated: true
type: note
---

要使用 Google Imagen 4 Preview 0606，您需要透過 Google 的 Vertex AI 平台存取，因為這是一項專為文字轉圖像生成設計的 Generative AI Preview 服務。以下是基於現有資訊的逐步指南：

### 如何使用 Google Imagen 4 Preview 0606

1. **存取 Vertex AI**：
   - **平台**：Imagen 4 Preview 0606 可在 Google Cloud 的 Vertex AI 上使用。您需要擁有 Google Cloud 帳戶才能開始使用。
   - **註冊**：若尚未擁有帳戶，請前往 [cloud.google.com](https://cloud.google.com) 註冊並設定專案。請確保已啟用計費功能，因為此為預覽服務可能產生費用（定價詳情請參閱 Vertex AI 定價頁面的 Imagen 部分）。[](https://cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-generate-preview-06-06)[](https://cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-fast-generate-preview-06-06)
   - **導航至 Vertex AI**：登入後，前往 Google Cloud Console 中的 Vertex AI 部分，並找到 Generative AI 工具。

2. **設定環境**：
   - **身份驗證**：使用 Google Cloud 憑證驗證您的帳戶。您可透過以下指令生成存取權杖：
     ```bash
     gcloud auth print-access-token
     ```
   - **專案與位置**：設定您的 Google Cloud 專案 ID 和位置（例如 `us-central1`）。範例：
     ```bash
     export GOOGLE_CLOUD_PROJECT=your-project-id
     export GOOGLE_CLOUD_LOCATION=us-central1
     ```

3. **使用 Imagen 4 模型**：
   - **API 存取**：Imagen 4 Preview 0606 可透過 Vertex AI API 存取。使用模型端點 `imagen-4.0-generate-preview-06-06`。您可透過 cURL 或 Google Gen AI SDK for Python 等工具以程式設計方式與其互動。
   - **cURL 請求範例**：
     ```bash
     curl -X POST \
     -H "Authorization: Bearer $(gcloud auth print-access-token)" \
     -H "Content-Type: application/json; charset=utf-8" \
     "https://${GOOGLE_CLOUD_LOCATION}-aiplatform.googleapis.com/v1/projects/${GOOGLE_CLOUD_PROJECT}/locations/${GOOGLE_CLOUD_LOCATION}/publishers/google/models/imagen-4.0-generate-preview-06-06:predict" \
     -d '{"instances": [{"prompt": "A cat reading a book"}], "parameters": {"sampleCount": 1}}'
     ```
     此指令將回傳 base64 編碼的圖像。[](https://cloud.google.com/vertex-ai/generative-ai/docs/image/overview)
   - **Python SDK 範例**：
     ```python
     from google import genai
     from google.genai.types import GenerateImagesConfig
     client = genai.Client()
     image = client.models.generate_images(
         model="imagen-4.0-generate-preview-06-06",
         prompt="A dog reading a newspaper",
         config=GenerateImagesConfig(image_size="2K")
     )
     image.generated_images[0].image.save("output-image.png")
     print(f"Created output image using {len(image.generated_images[0].image.image_bytes)} bytes")
     ```
     此程式碼將生成圖像並儲存為 PNG 檔案。[](https://cloud.google.com/vertex-ai/generative-ai/docs/image/overview)

4. **設計有效提示詞**：
   - **提示詞結構**：為獲得最佳效果，請使用詳細且具體的提示詞。包含主體、環境、藝術風格（如寫實風格、抽象風格）、氛圍及構圖元素（如拍攝角度）。範例：「一幅充滿活力的未來城市日落圖像，賽博龐克風格，帶有霓虹燈光與戲劇性的低角度視角。」
   - **技巧**：
     - 保持精確：模糊的提示詞可能導致不可預測的結果
     - 避免無意義輸入（如隨機表情符號），因其可能產生不一致的輸出
     - 如需文字可特別指定，Imagen 4 已改進文字渲染能力。[](https://deepmind.google/models/imagen/)[](https://replicate.com/blog/google-imagen-4)
   - **負向提示詞**：您可使用負向提示詞排除不需要的元素（例如若不需要圖像中的文字，可加入「no text」）。[](https://docs.aimlapi.com/api-references/image-models/google/imagen-4-preview)

5. **探索變體版本**：
   - Imagen 4 Preview 0606 提供多種變體，如 **Fast**（速度提升最高 10 倍，適合批量生成）與 **Ultra**（提示詞遵循度更高，適合專業用途）。請在您的 Vertex AI 介面中確認可用版本，並根據需求選擇（例如 Fast 用於快速原型製作，Ultra 用於高品質輸出）。[](https://fal.ai/models/fal-ai/imagen4/preview)[](https://cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-fast-generate-preview-06-06)

6. **檢視輸出與安全功能**：
   - **輸出格式**：圖像以標準格式生成（如 PNG 或 JPEG），最高支援 2K 解析度。[](https://fal.ai/models/fal-ai/imagen4/preview)
   - **SynthID 數位浮水印**：所有生成圖像均包含不可見的數位浮水印，用以標識為 AI 生成，確保透明度。[](https://deepmind.google/models/imagen/)[](https://developers.googleblog.com/en/imagen-4-now-available-in-the-gemini-api-and-google-ai-studio/)
   - **內容限制**：Imagen 4 使用過濾機制盡量減少有害內容，但可能仍難以處理複雜構圖、小臉部或居中圖像。請查閱 Google 的使用指南了解內容限制。[](https://deepmind.google/models/imagen/)[](https://cloud.google.com/vertex-ai/generative-ai/docs/image/overview)

7. **替代平台**：
   - Imagen 4 亦可在第三方平台使用，如 Replicate、fal.ai 或 AI/ML API，這些平台可能提供更簡潔的介面或測試用沙箱環境。例如：
     - **Replicate**：使用提示詞如「寧靜的山景日落，超寫實風格」運行 Imagen 4。請查閱 Replicate 文件了解 API 金鑰與使用方法。[](https://replicate.com/blog/google-imagen-4)[](https://replicate.com/google/imagen-4-fast)
     - **fal.ai**：使用其 API 發送請求：
       ```javascript
       const result = await fal.subscribe("fal-ai/imagen4/preview", {
           input: { prompt: "A serene mountain landscape at sunset, hyperrealistic style" }
       });
       console.log(result.images[0].url);
       ```
       定價各有不同（例如 Standard 每張 $0.05、Fast $0.04、Ultra $0.06）。[](https://fal.ai/models/fal-ai/imagen4/preview)
   - **Gemini App 或 Google Workspace**：Imagen 4 已整合至 Gemini 應用程式、Google Slides、Docs 與 Vids，可直接在工作流程中生成圖像。例如在 Google Docs 中可生成圖像來輔助文件說明。[](https://www.stablediffusion.blog/imagen4)

8. **測試與迭代**：
   - 在整合至生產環境前，可先於沙箱環境（如 Google AI Studio 提供有限免費測試）實驗提示詞效果。[](https://developers.googleblog.com/en/imagen-4-now-available-in-the-gemini-api-and-google-ai-studio/)
   - 由於預覽服務可能功能有限或持續變更，請透過平台儀表板監控 API 使用情況與成本。[](https://fal.ai/models/fal-ai/imagen4/preview)

### 補充說明
- **定價**：請查閱 Vertex AI 定價頁面了解 Imagen 4 成本（例如 Standard 每張 $0.04、Ultra $0.06）。[](https://developers.googleblog.com/en/imagen-4-now-available-in-the-gemini-api-and-google-ai-studio/)[](https://fal.ai/models/fal-ai/imagen4/preview)
- **限制**：Imagen 4 可能難以處理模糊提示詞、小臉部或完美居中構圖。請使用清晰有結構的提示詞以獲得最佳效果。[](https://deepmind.google/models/imagen/)
- **可用性**：作為預覽服務，功能與支援可能變更。請查閱 Google Cloud 的發布階段說明以獲取更新。[](https://cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-generate-preview-06-06)[](https://cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-fast-generate-preview-06-06)

詳細文件請參閱 [Vertex AI Imagen 頁面](https://cloud.google.com/vertex-ai/docs/generative-ai/image/overview) 或 [Google Developers Blog](https://developers.googleblog.com)。API 存取請參閱 [x.ai/api](https://x.ai/api) 了解通用 AI API 指南，但具體 Imagen 4 詳情請見 Google Cloud 文件。[](https://cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-generate-preview-06-06)[](https://developers.googleblog.com/en/imagen-4-now-available-in-the-gemini-api-and-google-ai-studio/)

若需要特定平台或使用案例的協助，請隨時告知！
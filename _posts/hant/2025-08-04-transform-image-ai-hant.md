---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 以AI提示轉換圖像
translated: true
type: note
---

截至2025年8月，OpenAI的DALL-E模型（特別是較新的「GPT圖像」模型，如`gpt-image-1`）已發展至支援更複雜的圖像處理功能，包括「圖像轉圖像」變換。雖然DALL-E 2曾設有專門處理此類需求的「variations」端點，但新版模型透過結合圖像輸入與詳細文字提示，將此功能整合為一體。

以下將說明如何運用OpenAI API執行「圖像轉圖像」任務（例如賦予吉卜力風格）：

### 核心概念：結合文字提示的圖像編輯

與單純的文字轉圖像提示不同，使用OpenAI API進行圖像轉圖像時，需同時提供原始圖像與描述預期效果的文字提示。關鍵在於指導模型如何以新風格「重新詮釋」圖像。

### 逐步API使用指南

此流程通常包含幾個關鍵步驟：

1.  **準備圖像**：欲轉換的圖像須符合支援格式（如PNG、JPEG）與尺寸要求（通常正方形比例最為理想）。您需要將此圖像提供給API調用。

2.  **構建強效提示**：這是最關鍵的環節。您不能僅簡單輸入「轉成吉卜力風格」，而需具體描述希望模型應用的吉卜力風格*元素*。優質提示將成為AI的指引方針，指導其如何重新演算圖像。

      * **不良提示**：「吉卜力風格」
      * **較佳提示**：「以吉卜力工作室風格呈現的魔法森林場景。使用柔和的水彩紋理、搭配金色時刻光線的鮮明但溫潤色調，並增添奇幻如夢的氛圍。」
      * **更進階提示**：「將此肖像轉化為吉卜力工作室角色，保留其基本特徵但融入標誌性美學：略為簡化的面部細節、富表現力的雙眼與柔和色調。採用手繪質感與懷舊氛圍。」

3.  **執行API調用**：您將使用OpenAI的圖像編輯API。此功能通常歸屬於圖像生成API的一部分，但需使用特定參數來接收圖像輸入。您需傳送圖像（通常以Base64編碼字串形式，或先上傳至OpenAI伺服器後取得檔案ID）與詳細提示文字。

      * **端點**：DALL-E 2可能使用`/v1/images/edits`端點，但對於GPT圖像等新型號，可能已整合至單一功能更強大的`/v1/chat/completions`端點，以處理多模態輸入（文字與圖像）。請查閱官方文件以確認正確端點與請求結構。

      * **參數說明**：

          * `model`：指定使用模型，如`dall-e-2`或新型號`gpt-image-1`。
          * `image`：已準備的圖像資料。
          * `prompt`：描述欲應用之吉卜力風格的文字說明。
          * `n`：生成圖像數量（新型號通常限生成1張）。
          * `size`：預期輸出尺寸（如「1024x1024」）。

4.  **處理回應**：API將回傳包含新生成圖像URL的JSON物件，您可據以下載保存該圖像。

### 範例程式碼（Python概念示範）

儘管具體程式碼可能隨API更新而變動，以下提供使用`openai` Python套件的概念性範例：

```python
import openai
import base64
from io import BytesIO
from PIL import Image

# 設定OpenAI API金鑰
# 應從環境變數讀取，避免硬編碼
openai.api_key = os.getenv("OPENAI_API_KEY")

# 將圖像編碼為base64的函式
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

# 欲轉換的圖像路徑
image_path = "your_photo.png"
base64_image = encode_image(image_path)

# 詳細的吉卜力風格提示文字
prompt_text = "將此圖像轉換為吉卜力工作室動畫風格。應用柔和的水彩紋理、搭配金色時刻光線的鮮明但溫潤色調，以及奇幻如夢的氛圍。請維持圖像原始構圖。"

try:
    response = openai.images.generate(
        model="gpt-image-1", # 若使用variations端點可改用"dall-e-2"
        prompt=prompt_text,
        image_base64=base64_image, # 此參數可能隨API版本而異
        size="1024x1024",
        n=1,
    )

    image_url = response.data[0].url
    print(f"已生成吉卜力風格圖像：{image_url}")

except Exception as e:
    print(f"發生錯誤：{e}")

```

**重要注意事項：**

  * **API更新**：OpenAI API持續演進，請務必查閱官方文件以獲取最新端點、參數與程式範例。
  * **模型選擇**：新型號`gpt-image-1`通常能更精準遵循複雜細膩的指令，並兼具圖像分析與生成能力，對圖像轉圖像任務極為強大。
  * **提示工程**：輸出品質高度依賴提示內容。請多方嘗試不同描述詞與風格元素，以精準捕捉您追求的吉卜力神韻。
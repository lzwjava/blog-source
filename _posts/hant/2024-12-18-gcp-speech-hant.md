---
audio: false
generated: false
image: false
lang: hant
layout: post
title: 開始使用Google文字轉語音API
translated: true
type: post
---

我計劃使用Google Text-to-Speech API將一些王垠的文章轉換為音頻。以下是逐步指南，並附上ChatGPT提供的一些有用教程。一切準備就緒後，我將在這裡上傳音頻供您收聽。

---

### 第一步：設置Google Cloud帳戶

1. 創建Google Cloud帳戶  
   如果還沒有帳戶，請在[Google Cloud控制台](https://console.cloud.google.com/)註冊。

2. 創建新項目  
   - 在Cloud控制台中，點擊項目下拉菜單（左上角）。
   - 選擇新建項目，命名並創建項目。

3. 啟用Text-to-Speech API  
   - 訪問[Google Cloud Text-to-Speech API頁面](https://cloud.google.com/text-to-speech)。
   - 點擊啟用以為您的項目激活API。

4. 創建API憑證  
   - 在Cloud控制台中導航到API與服務 > 憑證。
   - 點擊創建憑證，然後選擇服務帳戶。
   - 按照提示創建服務帳戶並下載JSON格式的私鑰文件。  
   - 請妥善保管此JSON文件，因為它用於驗證您的API請求。

---

### 第二步：安裝Google Cloud SDK和客戶端庫

1. 安裝Google Cloud SDK  
   如果尚未安裝，請按照[Google Cloud SDK安裝指南](https://cloud.google.com/sdk/docs/install)為您的操作系統安裝。

2. 安裝Python客戶端庫  
   如果您使用Python，請使用以下命令安裝`google-cloud-texttospeech`庫：

   ```bash
   pip install google-cloud-texttospeech
   ```

---

### 第三步：設置身份驗證

在使用API之前，您需要使用憑證進行身份驗證。將環境變量設置為憑證文件的路徑：

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-file.json"
```

將路徑替換為您下載的JSON文件的實際位置。

---

### 第四步：實現文本到語音轉換

以下是一個使用Google Cloud Text-to-Speech API將文本轉換為語音的Python示例：

```python
from google.cloud import texttospeech

def text_to_speech(text, output_filename):
    # 初始化Text-to-Speech客戶端
    client = texttospeech.TextToSpeechClient()

    # 設置合成輸入
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # 設置語音參數（使用'en-US-Journey-D'）
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",  # 英語（美國）
        name="en-US-Journey-D"  # 特定語音模型（Journey）
    )

    # 設置音頻配置
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,  # MP3格式
        effects_profile_id=["small-bluetooth-speaker-class-device"],  # 針對藍牙揚聲器優化
        pitch=0.0,  # 無音調修改
        speaking_rate=0.9,  # 調整語速（可根據需要修改）
        volume_gain_db=5.0  # 更大音量
    )

    # 執行文本到語音請求
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # 將音頻內容寫入文件
    with open(output_filename, "wb") as out:
        out.write(response.audio_content)

    print(f"音頻內容已寫入 {output_filename}")

# 示例使用
article_text = "電影，哦天哪，我簡直太愛它們了。它們就像時光機，帶你進入不同的世界和風景，我簡直無法自拔。"
output_file = "output_audio.mp3"  # 輸出為MP3格式

# 將文本轉換為語音
text_to_speech(article_text, output_file)
```

---

### 第五步：運行腳本

1. 將腳本保存為`text_to_speech.py`。
2. 使用以下命令運行腳本：

   ```bash
   python text_to_speech.py
   ```

這將從提供的文本生成一個音頻文件（`output_audio.mp3`）。

---

### 第六步：服務帳戶密鑰

您的服務帳戶的JSON密鑰應類似於以下內容：

```json
{
  "type": "service_account",
  "project_id": "your-project-id",
  "private_key_id": "your-private-key-id",
  "private_key": "your-private-key",
  "client_email": "your-service-account-email@your-project-id.iam.gserviceaccount.com",
  "client_id": "your-client-id",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "your-client-cert-url"
}
```

---

### 為什麼選擇Journey？

Google Cloud Text-to-Speech提供了多種語音，但Journey因其自然、人聲般的音質而脫穎而出。與其他聽起來常常機械化的模型不同，Journey在表達力和逼真度方面表現出色。它特別適合長篇內容，如播客、有聲書或任何需要更對話語調的應用。

Journey的主要特點：
- 自然語音：聽起來更接近人聲。
- 表達力：根據上下文調整語調和抑揚頓挫。
- 適合長篇內容：非常適合播客和敘述。

有關Google Cloud Text-to-Speech的更多好處，請查看[Google Cloud概述](https://cloud.google.com/text-to-speech#benefits)。

---

### 第七步：生成新的服務帳戶密鑰（如果需要）

如果您的服務帳戶密鑰與上述示例不匹配，您可以從Google Cloud控制台生成新的密鑰。

生成新密鑰的步驟：
1. 前往[Google Cloud控制台](https://console.cloud.google.com/)。
2. 導航到IAM與管理 > 服務帳戶。
3. 創建新的服務帳戶：
   - 點擊創建服務帳戶並分配適當的角色。
   - 點擊創建。
4. 生成密鑰：
   - 創建服務帳戶後，點擊它。
   - 轉到密鑰選項卡，點擊添加密鑰，選擇JSON，然後下載密鑰。

---

### 示例音頻輸出

一切設置完成後，您可以生成音頻文件，該文件將在此處提供：  
[下載音頻文件](assets/audios/output-audio.mp3)。

---

### 結論

Google Cloud Text-to-Speech API使將文本轉換為自然語音變得簡單。無論您是構建需要語音輸出的應用程序，還是僅僅在實驗文本到語音轉換，此API都提供了強大的功能和自定義選項。探索完整文檔以獲取更多語音選擇、語言和高級功能。
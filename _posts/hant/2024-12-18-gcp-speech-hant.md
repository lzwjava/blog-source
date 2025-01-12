---
audio: true
lang: hant
layout: post
title: Google文本转语音API入门指南
---

我计划使用Google文字转语音API将王垠的一些文章转换为音频。以下是一步步的指南，以及ChatGPT提供的一些有用教程。一切准备就绪后，我将把音频上传到这里供您聆听。

---

### 第一步：设置谷歌云账户

1. 创建谷歌云账户  
   如果您还没有账户，请前往[谷歌云控制台](https://console.cloud.google.com/)进行注册。

2. 创建新项目  
   - 在云端控制台中，点击项目下拉菜单（左上角）。  
   - 选择“新建项目”，为其命名并创建项目。

3. 启用文本转语音API  
   - 访问[Google Cloud文本转语音API页面](https://cloud.google.com/text-to-speech)。  
   - 点击“启用”按钮，为您的项目激活该API。

4. 创建API凭证  
   - 在云控制台中，导航至“API和服务”>“凭证”。  
   - 点击“创建凭证”，然后选择“服务账号”。  
   - 按照提示创建服务账号，并下载JSON格式的私钥文件。  
   - 妥善保管此JSON文件，因为它用于验证您的API请求。

---

### 第二步：安装Google Cloud SDK和客户端库

1. 安装Google Cloud SDK  
   如果您尚未安装，请按照适用于您操作系统的[Google Cloud SDK安装指南](https://cloud.google.com/sdk/docs/install)进行操作。

2. 安装 Python 客户端库  
   如果你使用的是 Python，可以通过以下命令安装 `google-cloud-texttospeech` 库：

```bash
pip install google-cloud-texttospeech
```

---

### 第三步：设置身份验证

在使用API之前，您需要使用您的凭据进行身份验证。请将环境变量设置为您的凭据文件路径：

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-file.json"
```

將路徑替換為您下載的JSON文件的實際位置。

---

### 第四步：实现文本到语音的转换

以下是一个使用Google Cloud文本转语音API将文本转换为语音的Python示例：

```python
from google.cloud import texttospeech
```

def text_to_speech(text, output_filename):
    # 初始化文本转语音客户端
    client = texttospeech.TextToSpeechClient()

    # 設置合成輸入
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # 設置語音參數（使用 'en-US-Journey-D'）
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",  # 英語（美國）
        name="en-US-Journey-D"  # 特定語音模型（Journey）
    )

    # 设置音频配置
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,  # MP3格式
        effects_profile_id=["small-bluetooth-speaker-class-device"],  # 针对蓝牙音箱优化
        pitch=0.0,  # 无音高调整
        speaking_rate=0.9,  # 调整后的语速（可按需修改）
        volume_gain_db=5.0  # 更大的音量
    )

    # 執行文字轉語音請求
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # 将音频内容写入文件
    with open(output_filename, "wb") as out:
        out.write(response.audio_content)

    print(f"音頻內容已寫入 {output_filename}")

# 示例用法
article_text = "電影，哦我的天哪，我簡直太愛它們了。它們就像時光機，帶你穿越到不同的世界和風景中，我對此簡直欲罷不能。"
output_file = "output_audio.mp3"  # 輸出為MP3格式

# 將文字轉換為語音
text_to_speech(article_text, output_file)
```

---

### 第五步：运行脚本

1. 將腳本保存為 `text_to_speech.py`。
2. 使用以下命令運行腳本：

```bash
python text_to_speech.py
```

这将从提供的文本生成一个音频文件（`output_audio.mp3`）。

---

### 步骤6：服务账户密钥

您的服务账户的JSON密钥应类似于以下内容：

```json
{
  "type": "service_account",
  "project_id": "你的項目ID",
  "private_key_id": "你的私鑰ID",
  "private_key": "你的私鑰",
  "client_email": "你的服務帳戶郵件@你的項目ID.iam.gserviceaccount.com",
  "client_id": "你的客戶端ID",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "你的客戶端證書URL"
}
```

---

### 为何选择Journey？

Google Cloud 的文本转语音服务提供了多种声音选项，其中 Journey 以其自然、拟人的音质脱颖而出。与常显机械化的其他模型不同，Journey 在表达力和逼真度上表现卓越。它特别适合用于长篇内容，如播客、有声书，或任何需要更对话式语调的应用场景。

Journey的主要特点：
- 自然语音：声音更接近人声。
- 表现力强：根据上下文调整语气和语调。
- 适合长篇内容：非常适合播客和叙述。

欲了解更多关于Google Cloud文本转语音服务优势的详细信息，请访问[Google Cloud概述](https://cloud.google.com/text-to-speech#benefits)。

---

### 步骤7：生成新的服务账户密钥（如有需要）

如果您的服务账号密钥与上述示例不符，您可以从Google云控制台生成一个新的密钥。

要生成新的密钥：
1. 前往 [Google Cloud 控制台](https://console.cloud.google.com/)。
2. 导航至 IAM 与管理 > 服务账号。
3. 创建新的服务账号：
   - 点击“创建服务账号”并分配适当的角色。
   - 点击“创建”。
4. 生成密钥：
   - 创建服务账号后，点击该账号。
   - 进入“密钥”标签页，点击“添加密钥”，选择 JSON 格式，然后下载密钥。

---

### 示例音频输出

一切设置完成后，您可以生成音频文件，该文件将在此处提供：
[下载音频文件](./assets/audios/output-audio.mp3)。

---

### 结论

综上所述，通过深入分析，我们得出了以下几点结论。首先，...（此处简要总结主要发现）。其次，...（进一步阐述相关发现或建议）。最后，...（提出未来研究方向或行动建议）。这些结论不仅为当前问题提供了解决方案，也为未来的研究奠定了基础。希望本报告能为相关领域的学者和实践者提供有价值的参考。

Google Cloud 文字转语音 API 使得将文本转换为自然流畅的语音变得轻而易举。无论您是在开发一个需要语音输出的应用程序，还是仅仅在尝试文字转语音技术，此 API 都提供了强大的功能和定制选项。查阅完整文档，以获取更多语音选择、语言支持及高级功能。
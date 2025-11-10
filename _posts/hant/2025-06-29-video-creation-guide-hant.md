---
audio: false
generated: true
lang: hant
layout: post
title: 使用 Python 製作教學影片
translated: true
type: note
---

要使用 DeepSeek API 和 Google Cloud Text-to-Speech API 創建帶有黑色背景和字幕同步的教育短視頻，您可以使用 Python 來協調整個流程。以下是一個逐步指南和一個實現此功能的 Python 腳本。該腳本將：
1. 使用 DeepSeek API 生成或優化腳本（假設您提供教育內容）。
2. 使用 Google Cloud Text-to-Speech API 將腳本轉換為音頻。
3. 使用像 `moviepy` 這樣的庫創建帶有黑色背景和字幕同步的視頻。

### 先決條件
- **DeepSeek API 密鑰**：在 [DeepSeek](https://api-docs.deepseek.com/) 註冊並獲取 API 密鑰。
- **Google Cloud Text-to-Speech API**：
  - 設置 Google Cloud 項目並啟用 Text-to-Speech API。
  - 創建服務帳戶並下載 JSON 憑證文件。
  - 安裝 Google Cloud Text-to-Speech 客戶端庫：`pip install google-cloud-texttospeech`。
- **Python 庫**：
  - 安裝所需庫：`pip install openai moviepy requests`。
- **FFmpeg**：確保安裝 FFmpeg 以便 `moviepy` 處理視頻渲染（從 [FFmpeg 網站](https://ffmpeg.org/) 下載或通過軟件包管理器安裝）。

### 步驟
1. **使用 DeepSeek API 生成或優化腳本**：使用 DeepSeek 創建或潤色教育腳本，確保其簡潔且適合 1 分鐘視頻。
2. **使用 Google Cloud Text-to-Speech 將文本轉換為音頻**：將腳本分成段落，為每個段落生成音頻，並保存為單獨的音頻文件。
3. **使用 MoviePy 創建視頻**：生成帶有黑色背景的視頻，顯示每個段落的字幕並與音頻同步，最後合併成一個 1 分鐘的最終視頻。

### Python 腳本
以下腳本假設您有一個包含教育內容（段落）的文本文件，並生成帶有黑色背景和字幕的視頻。

```python
import os
from openai import OpenAI
from google.cloud import texttospeech
from moviepy.editor import TextClip, CompositeVideoClip, ColorClip, concatenate_videoclips
import requests

# 設置環境變量
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/google-credentials.json"  # 更新為您的憑證文件路徑
DEEPSEEK_API_KEY = "your_deepseek_api_key"  # 更新為您的 DeepSeek API 密鑰

# 初始化 DeepSeek 客戶端
deepseek_client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")

# 使用 DeepSeek 優化腳本的函數
def refine_script_with_deepseek(script):
    prompt = f"""
    You are an expert scriptwriter for educational videos. Refine the following script to be concise, clear, and engaging for a 1-minute educational video. Ensure it is suitable for spoken narration and fits within 60 seconds when spoken at a natural pace. Split the script into 2-3 short paragraphs for caption display. Return the refined script as a list of paragraphs.

    Original script:
    {script}

    Output format:
    ["paragraph 1", "paragraph 2", "paragraph 3"]
    """
    response = deepseek_client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}],
        stream=False
    )
    refined_script = eval(response.choices[0].message.content)  # 將字符串轉換為列表
    return refined_script

# 使用 Google Cloud Text-to-Speech 為每個段落生成音頻的函數
def generate_audio(paragraphs, output_dir="audio"):
    client = texttospeech.TextToSpeechClient()
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    audio_files = []
    for i, paragraph in enumerate(paragraphs):
        synthesis_input = texttospeech.SynthesisInput(text=paragraph)
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US",
            name="en-US-Wavenet-D"  # 自然英語語音
        )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )
        response = client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )
        audio_file = os.path.join(output_dir, f"paragraph_{i+1}.mp3")
        with open(audio_file, "wb") as out:
            out.write(response.audio_content)
        audio_files.append(audio_file)
    return audio_files

# 創建帶有字幕和黑色背景的視頻的函數
def create_video(paragraphs, audio_files, output_file="educational_video.mp4"):
    clips = []
    for i, (paragraph, audio_file) in enumerate(zip(paragraphs, audio_files)):
        # 為字幕創建文本剪輯
        text_clip = TextClip(
            paragraph,
            fontsize=40,
            color="white",
            font="Arial",
            size=(1280, 720),  # 標準高清分辨率
            method="caption",
            align="center"
        )
        # 加載音頻並獲取其持續時間
        audio_clip = AudioFileClip(audio_file)
        duration = audio_clip.duration
        # 設置文本剪輯持續時間以匹配音頻
        text_clip = text_clip.set_duration(duration)
        # 創建黑色背景剪輯
        bg_clip = ColorClip(size=(1280, 720), color=(0, 0, 0), duration=duration)
        # 合併文本和背景
        video_clip = CompositeVideoClip([bg_clip, text_clip.set_position("center")])
        # 為視頻剪輯添加音頻
        video_clip = video_clip.set_audio(audio_clip)
        clips.append(video_clip)
    
    # 串聯所有剪輯
    final_clip = concatenate_videoclips(clips)
    # 寫入最終視頻
    final_clip.write_videofile(output_file, fps=24, codec="libx264", audio_codec="aac")
    final_clip.close()
    for clip in clips:
        clip.close()

# 主函數
def main():
    # 示例輸入腳本（替換為您的教育內容）
    input_script = """
    Machine learning is a field of artificial intelligence that allows computers to learn from data without being explicitly programmed. It involves algorithms that identify patterns and make predictions. Applications include image recognition, natural language processing, and more. This technology is transforming industries like healthcare and finance.
    """
    
    # 步驟 1：使用 DeepSeek 優化腳本
    refined_paragraphs = refine_script_with_deepseek(input_script)
    print("Refined Script:", refined_paragraphs)
    
    # 步驟 2：為每個段落生成音頻
    audio_files = generate_audio(refined_paragraphs)
    print("Audio files generated:", audio_files)
    
    # 步驟 3：創建帶有字幕和黑色背景的視頻
    create_video(refined_paragraphs, audio_files)
    print("Video created: educational_video.mp4")

if __name__ == "__main__":
    main()

```

### 使用方法
1. **設置憑證**：
   - 將 `"path/to/your/google-credentials.json"` 替換為您的 Google Cloud 服務帳戶 JSON 文件路徑。
   - 將 `"your_deepseek_api_key"` 替換為您的 DeepSeek API 密鑰。
2. **準備輸入腳本**：
   - 在 `main()` 函數中修改 `input_script` 變量為您的教育內容。腳本應為包含您要轉換為視頻的完整文本的單個字符串。
3. **運行腳本**：
   - 將腳本保存為 `create_educational_video.py` 並使用 `python create_educational_video.py` 運行。
   - 腳本將：
     - 使用 DeepSeek API 優化腳本，確保其簡潔並分成 2-3 個段落。
     - 使用 Google Cloud Text-to-Speech 為每個段落生成 MP3 音頻文件。
     - 創建一個帶有黑色背景的視頻，顯示每個段落作為字幕並與其對應的音頻同步。
4. **輸出**：
   - 最終視頻將保存為與腳本同一目錄下的 `educational_video.mp4`。
   - 每個段落的音頻文件將保存在 `audio` 目錄中。

### 注意事項
- **DeepSeek API**：腳本使用 `deepseek-chat` 模型來優化腳本。確保您的 API 密鑰有效且有足夠的餘額。DeepSeek API 在此用於為視頻旁白結構化腳本，因為它在文本生成和優化方面表現出色。[](https://www.datacamp.com/tutorial/deepseek-api)
- **Google Cloud Text-to-Speech**：腳本使用 `en-US-Wavenet-D` 語音進行自然英語旁白。您可以通過修改 `VoiceSelectionParams` 中的 `name` 參數來更改語音（請參閱 Google Cloud Text-to-Speech 文檔以獲取其他語音選項）。
- **MoviePy**：視頻以 1280x720 分辨率（高清）創建。您可以調整 `TextClip` 和 `ColorClip` 中的 `size` 參數以獲得不同的分辨率。
- **時間同步**：腳本通過將文本剪輯持續時間設置為匹配音頻持續時間來確保字幕與音頻同步。對於 1 分鐘的視頻，DeepSeek 提示強制使用簡潔的腳本。
- **依賴項**：確保 FFmpeg 已安裝並可在系統的 PATH 中訪問，以便 `moviepy` 正常工作。

### 示例輸出
如果您的輸入腳本是關於機器學習的，優化後的腳本可能如下所示：
```
["Machine learning, a branch of AI, enables computers to learn from data.", 
 "It uses algorithms to find patterns and predict outcomes.", 
 "Applications include image recognition and healthcare innovations."]
```
- 每個段落生成一個音頻文件（例如 `paragraph_1.mp3`、`paragraph_2.mp3` 等）。
- 最終視頻顯示黑色背景，白色字幕依次出現，與音頻旁白同步。

這種方法簡單、經濟高效，並能製作出適合 YouTube 或教育網站等平台的專業教育視頻。如果您需要進一步自定義（例如不同的字體、字幕樣式或附加效果），請告訴我！
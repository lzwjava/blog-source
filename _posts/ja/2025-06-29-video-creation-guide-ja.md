---
audio: false
generated: true
lang: ja
layout: post
title: Pythonで教育用動画を作成する
translated: true
type: note
---

DeepSeek APIとGoogle Cloud Text-to-Speech APIを使用して、テキストから生成された音声と同期した字幕を持つ黒背景の教育用ショートビデオを作成するには、Pythonを使用してプロセスを調整できます。以下に、これを実現するステップバイステップガイドとPythonスクリプトを示します。このスクリプトは以下のことを行います：
1. DeepSeek APIを使用してスクリプトを生成または改良します（教育コンテンツを提供することを想定）。
2. Google Cloud Text-to-Speech APIを使用してスクリプトを音声に変換します。
3. `moviepy`のようなライブラリを使用して、黒背景と音声に同期した字幕を持つビデオを作成します。

### 前提条件
- **DeepSeek APIキー**: [DeepSeek](https://api-docs.deepseek.com/)でサインアップしてAPIキーを取得してください。
- **Google Cloud Text-to-Speech API**:
  - Google Cloudプロジェクトをセットアップし、Text-to-Speech APIを有効にしてください。
  - サービスアカウントを作成し、JSON認証情報ファイルをダウンロードしてください。
  - Google Cloud Text-to-Speechクライアントライブラリをインストール: `pip install google-cloud-texttospeech`
- **Pythonライブラリ**:
  - 必要なライブラリをインストール: `pip install openai moviepy requests`
- **FFmpeg**: `moviepy`がビデオレンダリングを処理するためにFFmpegがインストールされていることを確認してください（[FFmpeg website](https://ffmpeg.org/)からダウンロードするか、パッケージマネージャー経由でインストール）。

### ステップ
1. **DeepSeek APIでスクリプトを生成または改良**: DeepSeekを使用して教育用スクリプトを作成または磨き上げ、1分間のビデオに適した簡潔なものにします。
2. **Google Cloud Text-to-Speechでテキストを音声に変換**: スクリプトを段落に分割し、それぞれの音声を生成して別々の音声ファイルとして保存します。
3. **MoviePyでビデオを作成**: 黒背景のビデオを生成し、各段落の字幕を音声に同期して表示し、最終的な1分間のビデオに結合します。

### Pythonスクリプト
以下のスクリプトは、教育コンテンツ（段落）を含むテキストファイルがあり、黒背景と字幕を持つビデオを生成することを想定しています。

```python
import os
from openai import OpenAI
from google.cloud import texttospeech
from moviepy.editor import TextClip, CompositeVideoClip, ColorClip, concatenate_videoclips
import requests

# 環境変数を設定
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/google-credentials.json"  # 認証情報ファイルのパスに更新
DEEPSEEK_API_KEY = "your_deepseek_api_key"  # DeepSeek APIキーに更新

# DeepSeekクライアントを初期化
deepseek_client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")

# DeepSeekでスクリプトを改良する関数
def refine_script_with_deepseek(script):
    prompt = f"""
    あなたは教育ビデオのための専門的なスクリプトライターです。以下のスクリプトを、1分間の教育ビデオ向けに簡潔で明確かつ魅力的に改良してください。自然なペースで話した場合に60秒以内に収まるようにし、字幕表示用に2-3の短い段落に分割してください。改良されたスクリプトを段落のリストとして返してください。

    元のスクリプト:
    {script}

    出力形式:
    ["段落1", "段落2", "段落3"]
    """
    response = deepseek_client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}],
        stream=False
    )
    refined_script = eval(response.choices[0].message.content)  # 文字列をリストに変換
    return refined_script

# Google Cloud Text-to-Speechを使用して各段落の音声を生成する関数
def generate_audio(paragraphs, output_dir="audio"):
    client = texttospeech.TextToSpeechClient()
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    audio_files = []
    for i, paragraph in enumerate(paragraphs):
        synthesis_input = texttospeech.SynthesisInput(text=paragraph)
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US",
            name="en-US-Wavenet-D"  # 自然な英語音声
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

# 字幕と黒背景でビデオを作成する関数
def create_video(paragraphs, audio_files, output_file="educational_video.mp4"):
    clips = []
    for i, (paragraph, audio_file) in enumerate(zip(paragraphs, audio_files)):
        # 字幕用のテキストクリップを作成
        text_clip = TextClip(
            paragraph,
            fontsize=40,
            color="white",
            font="Arial",
            size=(1280, 720),  # 標準HD解像度
            method="caption",
            align="center"
        )
        # 音声を読み込み、その長さを取得
        audio_clip = AudioFileClip(audio_file)
        duration = audio_clip.duration
        # テキストクリップの長さを音声に合わせて設定
        text_clip = text_clip.set_duration(duration)
        # 黒背景クリップを作成
        bg_clip = ColorClip(size=(1280, 720), color=(0, 0, 0), duration=duration)
        # テキストと背景を結合
        video_clip = CompositeVideoClip([bg_clip, text_clip.set_position("center")])
        # ビデオクリップに音声を追加
        video_clip = video_clip.set_audio(audio_clip)
        clips.append(video_clip)
    
    # すべてのクリップを連結
    final_clip = concatenate_videoclips(clips)
    # 最終ビデオを書き出し
    final_clip.write_videofile(output_file, fps=24, codec="libx264", audio_codec="aac")
    final_clip.close()
    for clip in clips:
        clip.close()

# メイン関数
def main():
    # 入力スクリプトの例（独自の教育コンテンツに置き換えてください）
    input_script = """
    Machine learning is a field of artificial intelligence that allows computers to learn from data without being explicitly programmed. It involves algorithms that identify patterns and make predictions. Applications include image recognition, natural language processing, and more. This technology is transforming industries like healthcare and finance.
    """
    
    # ステップ1: DeepSeekでスクリプトを改良
    refined_paragraphs = refine_script_with_deepseek(input_script)
    print("Refined Script:", refined_paragraphs)
    
    # ステップ2: 各段落の音声を生成
    audio_files = generate_audio(refined_paragraphs)
    print("Audio files generated:", audio_files)
    
    # ステップ3: 字幕と黒背景でビデオを作成
    create_video(refined_paragraphs, audio_files)
    print("Video created: educational_video.mp4")

if __name__ == "__main__":
    main()

```

### 使用方法
1. **認証情報の設定**:
   - `"path/to/your/google-credentials.json"`をGoogle CloudサービスアカウントのJSONファイルのパスに置き換えてください。
   - `"your_deepseek_api_key"`をDeepSeek APIキーに置き換えてください。
2. **入力スクリプトの準備**:
   - `main()`関数内の`input_script`変数を、ビデオに変換したい教育コンテンツで変更してください。スクリプトは、全文を含む単一の文字列である必要があります。
3. **スクリプトの実行**:
   - スクリプトを`create_educational_video.py`として保存し、`python create_educational_video.py`で実行してください。
   - スクリプトは以下を行います：
     - DeepSeek APIを使用してスクリプトを改良し、簡潔で2-3段落に分割されたものにします。
     - Google Cloud Text-to-Speechを使用して各段落のMP3音声ファイルを生成します。
     - 黒背景のビデオを作成し、各段落を対応する音声に同期した字幕として表示します。
4. **出力**:
   - 最終ビデオはスクリプトと同じディレクトリに`educational_video.mp4`として保存されます。
   - 各段落の音声ファイルは`audio`ディレクトリに保存されます。

### 注意点
- **DeepSeek API**: スクリプトはスクリプトをビデオナレーション用に構造化するために`deepseek-chat`モデルを使用します。APIキーが有効で十分なクレジットがあることを確認してください。DeepSeek APIは、テキスト生成と最適化に優れているため、ここではスクリプトの構造化に使用されています。
- **Google Cloud Text-to-Speech**: スクリプトは自然な英語ナレーションのために`en-US-Wavenet-D`音声を使用します。`VoiceSelectionParams`の`name`パラメータを変更することで音声を変更できます（他の音声オプションについてはGoogle Cloud Text-to-Speechのドキュメントを参照）。
- **MoviePy**: ビデオは1280x720解像度（HD）で作成されます。異なる解像度には`TextClip`と`ColorClip`の`size`パラメータを調整できます。
- **タイミング**: スクリプトは、テキストクリップの長さを音声の長さに合わせることで、字幕が音声と同期するようにしています。1分間のビデオの場合、DeepSeekのプロンプトは簡潔なスクリプトを強制します。
- **依存関係**: `moviepy`が正しく動作するために、FFmpegがシステムのPATHでアクセス可能であることを確認してください。

### 出力例
入力スクリプトが機械学習に関する場合、改良されたスクリプトは以下のようになるかもしれません：
```
["Machine learning, a branch of AI, enables computers to learn from data.", 
 "It uses algorithms to find patterns and predict outcomes.", 
 "Applications include image recognition and healthcare innovations."]
```
- 各段落は音声ファイル（例: `paragraph_1.mp3`, `paragraph_2.mp3`など）を生成します。
- 最終ビデオは黒背景に白い字幕が順番に表示され、音声ナレーションと同期します。

このアプローチはシンプルでコスト効率が良く、YouTubeや教育ウェブサイトのようなプラットフォームに適したプロフェッショナルな教育ビデオを生成します。さらなるカスタマイズ（異なるフォント、字幕スタイル、追加効果など）が必要な場合は、お知らせください！
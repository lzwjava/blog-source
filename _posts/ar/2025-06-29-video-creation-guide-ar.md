---
audio: false
generated: true
lang: ar
layout: post
title: إنشاء مقاطع فيديو تعليمية باستخدام بايثون
translated: true
type: note
---

لإنشاء مقاطع فيديو تعليمية قصيرة بخلفية سوداء وترجمات متزامنة مع الصوت المُنتج من نص باستخدام واجهة برمجة تطبيقات DeepSeek وواجهة برمجة تطبيقات Google Cloud Text-to-Speech، يمكنك استخدام Python لتنظيم العملية. فيما يلي دليل خطوة بخطة ونص برمجي بلغة Python يحقق ذلك. سيقوم النص البرمجي بما يلي:
1. استخدام واجهة برمجة تطبيقات DeepSeek لإنشاء نص أو تنقيحه (بافتراض أنك تقدم المحتوى التعليمي).
2. استخدام واجهة برمجة تطبيقات Google Cloud Text-to-Speech لتحويل النص إلى صوت.
3. استخدام مكتبة مثل `moviepy` لإنشاء فيديو بخلفية سوداء وترجمات متزامنة مع الصوت.

### المتطلبات الأساسية
- **مفتاح واجهة برمجة تطبيقات DeepSeek**: سجل في [DeepSeek](https://api-docs.deepseek.com/) واحصل على مفتاح API.
- **واجهة برمجة تطبيقات Google Cloud Text-to-Speech**:
  - أنشئ مشروع Google Cloud وقم بتمكين واجهة برمجة تطبيقات Text-to-Speech.
  - أنشئ حساب خدمة وقم بتنزيل ملف بيانات الاعتماد JSON.
  - ثبّت مكتبة عميل Google Cloud Text-to-Speech: `pip install google-cloud-texttospeech`.
- **مكتبات Python**:
  - ثبّت المكتبات المطلوبة: `pip install openai moviepy requests`.
- **FFmpeg**: تأكد من تثبيت FFmpeg حتى تتمكن `moviepy` من التعامل مع عرض الفيديو (قم بتنزيله من [موقع FFmpeg](https://ffmpeg.org/) أو ثبّته عبر مدير الحزم).

### الخطوات
1. **إنشاء أو تنقيح النص باستخدام واجهة برمجة تطبيقات DeepSeek**: استخدم DeepSeek لإنشاء أو تحسين النص التعليمي، مع التأكد من أنه موجز ومناسب لفيديو مدته دقيقة واحدة.
2. **تحويل النص إلى صوت باستخدام Google Cloud Text-to-Speech**: قسّم النص إلى فقرات، وقم بإنشاء صوت لكل منها، واحفظها كملفات صوتية منفصلة.
3. **إنشاء الفيديو باستخدام MoviePy**: أنشئ فيديو بخلفية سوداء، وعرض الترجمات لكل فقرة متزامنة مع الصوت، واجمعها في فيديو نهائي مدته دقيقة واحدة.

### النص البرمجي Python
يفترض النص البرمجي التالي أن لديك ملف نصي يحتوي على المحتوى التعليمي (فقرات) وينشئ فيديو بخلفية سوداء وترجمات.

```python
import os
from openai import OpenAI
from google.cloud import texttospeech
from moviepy.editor import TextClip, CompositeVideoClip, ColorClip, concatenate_videoclips
import requests

# إعداد متغيرات البيئة
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/google-credentials.json"  # حدّث بمسار ملف بيانات اعتمادك
DEEPSEEK_API_KEY = "your_deepseek_api_key"  # حدّث بمفتاح DeepSeek API الخاص بك

# تهيئة عميل DeepSeek
deepseek_client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")

# دالة لتنقيح النص باستخدام DeepSeek
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
    refined_script = eval(response.choices[0].message.content)  # Convert string to list
    return refined_script

# دالة لإنشاء الصوت لكل فقرة باستخدام Google Cloud Text-to-Speech
def generate_audio(paragraphs, output_dir="audio"):
    client = texttospeech.TextToSpeechClient()
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    audio_files = []
    for i, paragraph in enumerate(paragraphs):
        synthesis_input = texttospeech.SynthesisInput(text=paragraph)
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US",
            name="en-US-Wavenet-D"  # A natural-sounding English voice
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

# دالة لإنشاء الفيديو مع الترجمات والخلفية السوداء
def create_video(paragraphs, audio_files, output_file="educational_video.mp4"):
    clips = []
    for i, (paragraph, audio_file) in enumerate(zip(paragraphs, audio_files)):
        # إنشاء مقطع نصي للترجمات
        text_clip = TextClip(
            paragraph,
            fontsize=40,
            color="white",
            font="Arial",
            size=(1280, 720),  # Standard HD resolution
            method="caption",
            align="center"
        )
        # Load audio and get its duration
        audio_clip = AudioFileClip(audio_file)
        duration = audio_clip.duration
        # Set text clip duration to match audio
        text_clip = text_clip.set_duration(duration)
        # Create black background clip
        bg_clip = ColorClip(size=(1280, 720), color=(0, 0, 0), duration=duration)
        # Combine text and background
        video_clip = CompositeVideoClip([bg_clip, text_clip.set_position("center")])
        # Add audio to video clip
        video_clip = video_clip.set_audio(audio_clip)
        clips.append(video_clip)
    
    # Concatinate all clips
    final_clip = concatenate_videoclips(clips)
    # Write final video
    final_clip.write_videofile(output_file, fps=24, codec="libx264", audio_codec="aac")
    final_clip.close()
    for clip in clips:
        clip.close()

# الدالة الرئيسية
def main():
    # Example input script (replace with your educational content)
    input_script = """
    Machine learning is a field of artificial intelligence that allows computers to learn from data without being explicitly programmed. It involves algorithms that identify patterns and make predictions. Applications include image recognition, natural language processing, and more. This technology is transforming industries like healthcare and finance.
    """
    
    # Step 1: Refine script with DeepSeek
    refined_paragraphs = refine_script_with_deepseek(input_script)
    print("Refined Script:", refined_paragraphs)
    
    # Step 2: Generate audio for each paragraph
    audio_files = generate_audio(refined_paragraphs)
    print("Audio files generated:", audio_files)
    
    # Step 3: Create video with captions and black background
    create_video(refined_paragraphs, audio_files)
    print("Video created: educational_video.mp4")

if __name__ == "__main__":
    main()

```

### طريقة الاستخدام
1. **إعداد بيانات الاعتماد**:
   - استبدل `"path/to/your/google-credentials.json"` بالمسار إلى ملف JSON لحساب الخدمة الخاص بـ Google Cloud.
   - استبدل `"your_deepseek_api_key"` بمفتاح DeepSeek API الخاص بك.
2. **جهّز النص المدخل**:
   - عدّل المتغير `input_script` في الدالة `main()` بمحتواك التعليمي. يجب أن يكون النص سلسلة نصية واحدة تحتوي على النص الكامل الذي تريد تحويله إلى فيديو.
3. **شغّل النص البرمجي**:
   - احفظ النص البرمجي كـ `create_educational_video.py` وشغّله باستخدام `python create_educational_video.py`.
   - سيقوم النص البرمجي بما يلي:
     - تنقيح النص باستخدام واجهة برمجة تطبيقات DeepSeek لضمان إيجازه وتقسيمه إلى 2-3 فقرات.
     - إنشاء ملفات صوتية MP3 لكل فقرة باستخدام Google Cloud Text-to-Speech.
     - إنشاء فيديو بخلفية سوداء، مع عرض كل فقرة كترجمات متزامنة مع الصوت المقابل لها.
4. **المخرجات**:
   - سيتم حفظ الفيديو النهائي كـ `educational_video.mp4` في نفس دليل النص البرمجي.
   - سيتم حفظ الملفات الصوتية لكل فقرة في دليل `audio`.

### ملاحظات
- **واجهة برمجة تطبيقات DeepSeek**: يستخدم النص البرمجي نموذج `deepseek-chat` لتنقيح النص. تأكد من أن مفتاح API الخاص بك صالح وأن لديك رصيد كافٍ. تُستخدم واجهة برمجة تطبيقات DeepSeek هنا لتنظيم النص لرواية الفيديو، حيث أنها تتقن توليد النص وتحسينه.
- **Google Cloud Text-to-Speech**: يستخدم النص البرمجي صوت `en-US-Wavenet-D` للرواية الإنجليزية ذات النبرة الطبيعية. يمكنك تغيير الصوت عن طريق تعديل المعلمة `name` في `VoiceSelectionParams` (راجع وثائق Google Cloud Text-to-Speech لخيارات الأصوات الأخرى).
- **MoviePy**: يتم إنشاء الفيديو بدقة 1280x720 (HD). يمكنك ضبط المعلمة `size` في `TextClip` و `ColorClip` لدق مختلفة.
- **التوقيت**: يضمن النص البرمجي تزامن الترجمات مع الصوت عن طريق ضبط مدة المقطع النصي لتطابق مدة الصوت. لفيديو مدته دقيقة واحدة، يفرز مطالبة DeepSeek نصًا موجزًا.
- **التبعيات**: تأكد من تثبيت FFmpeg وأنه يمكن الوصول إليه في PATH الخاص بنظامك حتى تعمل `moviepy` بشكل صحيح.

### مثال على المخرجات
إذا كان نصك المدخل حول التعلم الآلي، فقد يبدو النص المنقح كما يلي:
```
["Machine learning, a branch of AI, enables computers to learn from data.", 
 "It uses algorithms to find patterns and predict outcomes.", 
 "Applications include image recognition and healthcare innovations."]
```
- كل فقرة تُنتج ملف صوتي (مثل `paragraph_1.mp3`, `paragraph_2.mp3`، إلخ).
- يعرض الفيديو النهائي خلفية سوداء مع ظهور ترجمات بيضاء بشكل تسلسلي، متزامنة مع رواية الصوت.

هذه الطريقة بسيطة وفعالة من حيث التكلفة وتنتج مقاطع فيديو تعليمية ذات مظهر احترافي مناسبة لمنصات مثل YouTube أو المواقع التعليمية. إذا كنت بحاجة إلى مزيد من التخصيص (مثل خطوط مختلفة، أو أنماط ترجمات، أو تأثيرات إضافية)، فأخبرني!
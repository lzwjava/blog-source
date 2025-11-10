---
audio: false
generated: true
lang: hi
layout: post
title: पायथन से शैक्षिक वीडियो बनाएँ
translated: true
type: note
---

शैक्षिक लघु वीडियो बनाने के लिए जिनमें काली पृष्ठभूमि और कैप्शन हों, और ऑडियो टेक्स्ट से DeepSeek API और Google Cloud Text-to-Speech API का उपयोग करके जनरेट किया गया हो, आप प्रक्रिया को व्यवस्थित करने के लिए Python का उपयोग कर सकते हैं। नीचे एक चरण-दर-चरण मार्गदर्शिका और एक Python स्क्रिप्ट दी गई है जो इसे पूरा करती है। यह स्क्रिप्ट:
1. स्क्रिप्ट जनरेट करने या परिष्कृत करने के लिए DeepSeek API का उपयोग करेगी (यह मानते हुए कि आप शैक्षिक सामग्री प्रदान करते हैं)।
2. स्क्रिप्ट को ऑडियो में बदलने के लिए Google Cloud Text-to-Speech API का उपयोग करेगी।
3. काली पृष्ठभूमि और ऑडियो के साथ सिंक्रनाइज़ कैप्शन वाला वीडियो बनाने के लिए `moviepy` जैसे लाइब्रेरी का उपयोग करेगी।

### पूर्वापेक्षाएँ
- **DeepSeek API Key**: [DeepSeek](https://api-docs.deepseek.com/) पर साइन अप करें और एक API कुंजी प्राप्त करें।
- **Google Cloud Text-to-Speech API**:
  - एक Google Cloud प्रोजेक्ट सेट अप करें और Text-to-Speech API सक्षम करें।
  - एक service account बनाएं और JSON क्रेडेंशियल फ़ाइल डाउनलोड करें।
  - Google Cloud Text-to-Speech क्लाइंट लाइब्रेरी इंस्टॉल करें: `pip install google-cloud-texttospeech`।
- **Python Libraries**:
  - आवश्यक लाइब्रेरी इंस्टॉल करें: `pip install openai moviepy requests`।
- **FFmpeg**: सुनिश्चित करें कि वीडियो रेंडरिंग के लिए `moviepy` द्वारा उपयोग हेतु FFmpeg इंस्टॉल है ([FFmpeg वेबसाइट](https://ffmpeg.org/) से डाउनलोड करें या package manager के माध्यम से इंस्टॉल करें)।

### चरण
1. **DeepSeek API के साथ स्क्रिप्ट जनरेट या परिष्कृत करें**: 1-मिनट के वीडियो के लिए स्क्रिप्ट को संक्षिप्त और उपयुक्त बनाने के लिए DeepSeek का उपयोग करें।
2. **Google Cloud Text-to-Speech के साथ टेक्स्ट को ऑडियो में बदलें**: स्क्रिप्ट को पैराग्राफ में विभाजित करें, प्रत्येक के लिए ऑडियो जनरेट करें, और अलग-अलग ऑडियो फ़ाइलों के रूप में सहेजें।
3. **MoviePy के साथ वीडियो बनाएँ**: एक काली पृष्ठभूमि वाला वीडियो जनरेट करें, प्रत्येक पैराग्राफ के लिए कैप्शन प्रदर्शित करें जो ऑडियो के साथ सिंक्रनाइज़ हों, और उन्हें अंतिम 1-मिनट के वीडियो में संयोजित करें।

### Python स्क्रिप्ट
निम्नलिखित स्क्रिप्ट मानती है कि आपके पास शैक्षिक सामग्री (पैराग्राफ) वाली एक टेक्स्ट फ़ाइल है और एक काली पृष्ठभूमि और कैप्शन वाला वीडियो जनरेट करती है।

```python
import os
from openai import OpenAI
from google.cloud import texttospeech
from moviepy.editor import TextClip, CompositeVideoClip, ColorClip, concatenate_videoclips
import requests

# Environment variables सेट करें
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/google-credentials.json"  # अपनी क्रेडेंशियल फ़ाइल पथ के साथ अपडेट करें
DEEPSEEK_API_KEY = "your_deepseek_api_key"  # अपनी DeepSeek API कुंजी के साथ अपडेट करें

# DeepSeek क्लाइंट को इनिशियलाइज़ करें
deepseek_client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")

# DeepSeek के साथ स्क्रिप्ट को परिष्कृत करने के लिए फ़ंक्शन
def refine_script_with_deepseek(script):
    prompt = f"""
    आप शैक्षिक वीडियो के लिए एक विशेषज्ञ स्क्रिप्टलेखक हैं। निम्नलिखित स्क्रिप्ट को 1-मिनट के शैक्षिक वीडियो के लिए संक्षिप्त, स्पष्ट और आकर्षक बनाने के लिए परिष्कृत करें। सुनिश्चित करें कि यह बोली जाने वाली आवाज के लिए उपयुक्त है और प्राकृतिक गति से बोले जाने पर 60 सेकंड में फिट हो जाती है। कैप्शन प्रदर्शन के लिए स्क्रिप्ट को 2-3 छोटे पैराग्राफ में विभाजित करें। परिष्कृत स्क्रिप्ट को पैराग्राफ की सूची के रूप में लौटाएं।

    मूल स्क्रिप्ट:
    {script}

    आउटपुट प्रारूप:
    ["पैराग्राफ 1", "पैराग्राफ 2", "पैराग्राफ 3"]
    """
    response = deepseek_client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}],
        stream=False
    )
    refined_script = eval(response.choices[0].message.content)  # स्ट्रिंग को लिस्ट में बदलें
    return refined_script

# Google Cloud Text-to-Speech का उपयोग करके प्रत्येक पैराग्राफ के लिए ऑडियो जनरेट करने का फ़ंक्शन
def generate_audio(paragraphs, output_dir="audio"):
    client = texttospeech.TextToSpeechClient()
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    audio_files = []
    for i, paragraph in enumerate(paragraphs):
        synthesis_input = texttospeech.SynthesisInput(text=paragraph)
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US",
            name="en-US-Wavenet-D"  # एक प्राकृतिक-सी लगने वाली अंग्रेजी आवाज
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

# कैप्शन और काली पृष्ठभूमि के साथ वीडियो बनाने का फ़ंक्शन
def create_video(paragraphs, audio_files, output_file="educational_video.mp4"):
    clips = []
    for i, (paragraph, audio_file) in enumerate(zip(paragraphs, audio_files)):
        # कैप्शन के लिए टेक्स्ट क्लिप बनाएं
        text_clip = TextClip(
            paragraph,
            fontsize=40,
            color="white",
            font="Arial",
            size=(1280, 720),  # मानक HD रिज़ॉल्यूशन
            method="caption",
            align="center"
        )
        # ऑडियो लोड करें और उसकी अवधि प्राप्त करें
        audio_clip = AudioFileClip(audio_file)
        duration = audio_clip.duration
        # टेक्स्ट क्लिप की अवधि को ऑडियो से मेल खाने के लिए सेट करें
        text_clip = text_clip.set_duration(duration)
        # काली पृष्ठभूमि क्लिप बनाएं
        bg_clip = ColorClip(size=(1280, 720), color=(0, 0, 0), duration=duration)
        # टेक्स्ट और पृष्ठभूमि को संयोजित करें
        video_clip = CompositeVideoClip([bg_clip, text_clip.set_position("center")])
        # वीडियो क्लिप में ऑडियो जोड़ें
        video_clip = video_clip.set_audio(audio_clip)
        clips.append(video_clip)
    
    # सभी क्लिप्स को जोड़ें
    final_clip = concatenate_videoclips(clips)
    # अंतिम वीडियो लिखें
    final_clip.write_videofile(output_file, fps=24, codec="libx264", audio_codec="aac")
    final_clip.close()
    for clip in clips:
        clip.close()

# मुख्य फ़ंक्शन
def main():
    # उदाहरण इनपुट स्क्रिप्ट (अपनी शैक्षिक सामग्री के साथ बदलें)
    input_script = """
    Machine learning is a field of artificial intelligence that allows computers to learn from data without being explicitly programmed. It involves algorithms that identify patterns and make predictions. Applications include image recognition, natural language processing, and more. This technology is transforming industries like healthcare and finance.
    """
    
    # चरण 1: DeepSeek के साथ स्क्रिप्ट को परिष्कृत करें
    refined_paragraphs = refine_script_with_deepseek(input_script)
    print("परिष्कृत स्क्रिप्ट:", refined_paragraphs)
    
    # चरण 2: प्रत्येक पैराग्राफ के लिए ऑडियो जनरेट करें
    audio_files = generate_audio(refined_paragraphs)
    print("ऑडियो फ़ाइलें जनरेट हुईं:", audio_files)
    
    # चरण 3: कैप्शन और काली पृष्ठभूमि के साथ वीडियो बनाएँ
    create_video(refined_paragraphs, audio_files)
    print("वीडियो बन गया: educational_video.mp4")

if __name__ == "__main__":
    main()

```

### उपयोग कैसे करें
1. **क्रेडेंशियल सेट अप करें**:
   - `"path/to/your/google-credentials.json"` को अपनी Google Cloud service account JSON फ़ाइल के पथ से बदलें।
   - `"your_deepseek_api_key"` को अपनी DeepSeek API कुंजी से बदलें।
2. **इनपुट स्क्रिप्ट तैयार करें**:
   - `main()` फ़ंक्शन में `input_script` वेरिएबल को उस टेक्स्ट के साथ संशोधित करें जिसे आप वीडियो में बदलना चाहते हैं। स्क्रिप्ट एक सिंगल स्ट्रिंग होनी चाहिए जिसमें पूरा टेक्स्ट हो।
3. **स्क्रिप्ट रन करें**:
   - स्क्रिप्ट को `create_educational_video.py` के रूप में सेव करें और इसे `python create_educational_video.py` के साथ रन करें।
   - स्क्रिप्ट:
     - स्क्रिप्ट को संक्षिप्त बनाने और 2-3 पैराग्राफ में विभाजित करने के लिए DeepSeek API का उपयोग करेगी।
     - Google Cloud Text-to-Speech का उपयोग करके प्रत्येक पैराग्राफ के लिए MP3 ऑडियो फ़ाइलें जनरेट करेगी।
     - एक काली पृष्ठभूमि वाला वीडियो बनाएगी, जिसमें प्रत्येक पैराग्राफ उसके संबंधित ऑडियो के साथ सिंक्रनाइज़ कैप्शन के रूप में दिखाई देगा।
4. **आउटपुट**:
   - अंतिम वीडियो स्क्रिप्ट के समान डायरेक्टरी में `educational_video.mp4` के रूप में सेव हो जाएगा।
   - प्रत्येक पैराग्राफ के लिए ऑडियो फ़ाइलें `audio` डायरेक्टरी में सेव होंगी।

### नोट्स
- **DeepSeek API**: स्क्रिप्ट स्क्रिप्ट को संरचित करने के लिए `deepseek-chat` मॉडल का उपयोग करती है। सुनिश्चित करें कि आपकी API कुंजी वैध है और आपके पास पर्याप्त क्रेडिट हैं। यहाँ DeepSeek API का उपयोग वीडियो आवाज के लिए स्क्रिप्ट को संरचित करने के लिए किया जाता है, क्योंकि यह टेक्स्ट जनरेशन और ऑप्टिमाइजेशन में माहिर है।[](https://www.datacamp.com/tutorial/deepseek-api)
- **Google Cloud Text-to-Speech**: स्क्रिप्ट प्राकृतिक-सी लगने वाली अंग्रेजी आवाज के लिए `en-US-Wavenet-D` वॉइस का उपयोग करती है। आप `VoiceSelectionParams` में `name` पैरामीटर को बदलकर वॉइस बदल सकते हैं (अन्य वॉइस विकल्पों के लिए Google Cloud Text-to-Speech डॉक्यूमेंटेशन देखें)।
- **MoviePy**: वीडियो 1280x720 रिज़ॉल्यूशन (HD) में बनाया गया है। आप विभिन्न रिज़ॉल्यूशन के लिए `TextClip` और `ColorClip` में `size` पैरामीटर समायोजित कर सकते हैं।
- **टाइमिंग**: स्क्रिप्ट यह सुनिश्चित करती है कि टेक्स्ट क्लिप की अवधि को ऑडियो अवधि से मेल खाने के लिए सेट करके कैप्शन ऑडियो के साथ सिंक्रनाइज़ हों। 1-मिनट के वीडियो के लिए, DeepSeek प्रॉम्प्ट एक संक्षिप्त स्क्रिप्ट लागू करता है।
- **निर्भरताएँ**: सुनिश्चित करें कि FFmpeg इंस्टॉल है और `moviepy` के सही काम करने के लिए आपके सिस्टम के PATH में एक्सेसिबल है।

### उदाहरण आउटपुट
यदि आपकी इनपुट स्क्रिप्ट मशीन लर्निंग के बारे में है, तो परिष्कृत स्क्रिप्ट कुछ इस तरह दिख सकती है:
```
["Machine learning, a branch of AI, enables computers to learn from data.", 
 "It uses algorithms to find patterns and predict outcomes.", 
 "Applications include image recognition and healthcare innovations."]
```
- प्रत्येक पैराग्राफ एक ऑडियो फ़ाइल जनरेट करता है (जैसे, `paragraph_1.mp3`, `paragraph_2.mp3`, आदि)।
- अंतिम वीडियो एक काली पृष्ठभूमि दिखाता है जिसमें सफेद कैप्शन क्रमिक रूप से दिखाई देते हैं, जो ऑडियो आवाज के साथ सिंक्रनाइज़ होते हैं।

यह दृष्टिकोण सरल, लागत-प्रभावी है और YouTube या शैक्षिक वेबसाइटों जैसे प्लेटफार्मों के लिए उपयुक्त पेशेवर दिखने वाले शैक्षिक वीडियो तैयार करता है। यदि आपको आगे अनुकूलन (जैसे, अलग-अलग फोंट, कैप्शन स्टाइल, या अतिरिक्त इफेक्ट) की आवश्यकता है, तो मुझे बताएं!
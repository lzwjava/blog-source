---
audio: true
lang: hi
layout: post
title: व्रैपर की जगह कच्चे HTTP अनुरोधों का उपयोग करना पसंद करें।
translated: true
---

python
import requests
import json
import time
def translate_text(text, target_language, special=False):
    if not text or not text.strip():
        return ""
    if target_language == 'en':
        print(f"  अंग्रेजी के लिए अनुवाद को छोड़ रहा हूँ: {text[:50]}...")
        return text
    print(f"  पाठ का अनुवाद कर रहा हूँ: {text[:50]}...")

    retries = 3
    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": create_translation_prompt(target_language, special)},
                    {"role": "user", "content": text}
                ],
                stream=False
            )
            if not response or not response.choices or not response.choices[0].message.content:
                print(f"  त्रुटि: अनुवाद प्रतिक्रिया खाली या अमान्य है: {response}")
            if response and response.choices:
                translated_text = response.choices[0].message.content
                return translated_text
            else:
                print(f"  अनुवाद {attempt + 1} प्रयास पर विफल रहा।")
                if attempt == retries - 1:
                    return None
        except Exception as e:
            print(f"  अनुवाद {attempt + 1} प्रयास पर त्रुटि के साथ विफल रहा: {e}")
            if attempt == retries - 1:
                return None
            time.sleep(1)  # पुनः प्रयास करने से पहले प्रतीक्षा करें
    return None


त्रुटि:

bash
 अनुवाद 1 प्रयास पर त्रुटि के साथ विफल रहा: लाइन 5 कॉलम 1 (चर 4) पर मूल्य की अपेक्षा की जा रही है


यह त्रुटि दर्शाती है कि DeepSeek API एक प्रतिक्रिया लौटा रहा है जो मान्य JSON नहीं है,  posibly HTML या किसी अन्य प्रारूप में हो सकता है। यह अप्रत्याशित है, क्योंकि API से JSON की अपेक्षा की जाती है। समस्या का कारण एक अस्थायी API समस्या, दर सीमा या prompt की समस्या हो सकती है। इसे सुंदर रूप से हैंडल करना जरूरी है त्रुटि को लॉग करके और संभवतः पुनः प्रयास करके।
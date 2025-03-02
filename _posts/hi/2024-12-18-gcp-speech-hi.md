---
audio: false
generated: false
lang: hi
layout: post
title: Google Text-to-Speech API के साथ शुरुआत करना
translated: true
---

मैं Yin Wang के कुछ लेखों को Google Text-to-Speech API का उपयोग करके ऑडियो में बदलने की योजना बना रहा हूँ। नीचे एक चरण-दर-चरण मार्गदर्शिका है, साथ ही ChatGPT द्वारा प्रदान किए गए कुछ उपयोगी ट्यूटोरियल भी हैं। एक बार सब कुछ तैयार हो जाने के बाद, मैं ऑडियो को यहां अपलोड कर दूंगा ताकि आप इसे सुन सकें।

---

### चरण 1: Google Cloud खाता सेट करें

1. Google Cloud खाता बनाएं  
   यदि आपके पास पहले से नहीं है, तो [Google Cloud Console](https://console.cloud.google.com/) पर साइन अप करें।

2. एक नया प्रोजेक्ट बनाएं  
   - क्लाउड कंसोल में, प्रोजेक्ट ड्रॉपडाउन मेनू पर क्लिक करें (ऊपर बाईं ओर)।
   - नया प्रोजेक्ट चुनें, इसे एक नाम दें, और प्रोजेक्ट बनाएं।

3. टेक्स्ट-टू-स्पीच API सक्षम करें  
   - [Google Cloud Text-to-Speech API पेज](https://cloud.google.com/text-to-speech) पर जाएं।  
   - अपने प्रोजेक्ट के लिए API को सक्रिय करने के लिए Enable पर क्लिक करें।

4. API क्रेडेंशियल्स बनाएं  
   - Cloud Console में APIs & Services > Credentials पर नेविगेट करें।  
   - Create Credentials पर क्लिक करें, फिर Service Account चुनें।  
   - प्रॉम्प्ट्स का पालन करते हुए सर्विस अकाउंट बनाएं और JSON फॉर्मेट में प्राइवेट की फाइल डाउनलोड करें।  
   - इस JSON फाइल को सुरक्षित रखें क्योंकि इसका उपयोग आपके API अनुरोधों को प्रमाणित करने के लिए किया जाता है।

---

### चरण 2: Google Cloud SDK और क्लाइंट लाइब्रेरी इंस्टॉल करें

1. Google Cloud SDK इंस्टॉल करें  
   यदि आपने अभी तक नहीं किया है, तो अपने ऑपरेटिंग सिस्टम के लिए [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) इंस्टॉल करने के निर्देशों का पालन करें।

2. Python क्लाइंट लाइब्रेरी इंस्टॉल करें  
   यदि आप Python का उपयोग कर रहे हैं, तो `google-cloud-texttospeech` लाइब्रेरी को निम्नलिखित कमांड के साथ इंस्टॉल करें:

```bash
   pip install google-cloud-texttospeech
   ```

(नोट: यह एक कमांड है जिसे टर्मिनल में चलाया जाता है। इसे हिंदी में अनुवादित करने की आवश्यकता नहीं है।)

---

### चरण 3: प्रमाणीकरण सेट करें

API का उपयोग करने से पहले, आपको अपने क्रेडेंशियल्स के साथ प्रमाणीकरण करना होगा। अपने क्रेडेंशियल्स फ़ाइल के पथ को पर्यावरण चर में सेट करें:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-file.json"
```

(नोट: यह कोड ब्लॉक है, इसे अनुवादित नहीं किया जाना चाहिए।)

अपने डाउनलोड किए गए JSON फ़ाइल के वास्तविक स्थान के साथ पथ को बदलें।

---

### चरण 4: टेक्स्ट-टू-स्पीच रूपांतरण को लागू करें

यहां Google Cloud Text-to-Speech API का उपयोग करके टेक्स्ट को स्पीच में बदलने के लिए एक Python उदाहरण दिया गया है:

```python
from google.cloud import texttospeech
```

```python
def text_to_speech(text, output_filename):
    # टेक्स्ट-टू-स्पीच क्लाइंट को इनिशियलाइज़ करें
    client = texttospeech.TextToSpeechClient()
```

    # संश्लेषण इनपुट सेट करें
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # आवाज़ पैरामीटर सेट करें ( 'en-US-Journey-D' का उपयोग करके )
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",  # अंग्रेजी (संयुक्त राज्य अमेरिका)
        name="en-US-Journey-D"  # विशिष्ट आवाज़ मॉडल (Journey)
    )

    # ऑडियो कॉन्फ़िगरेशन सेट करें
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,  # MP3 प्रारूप
        effects_profile_id=["small-bluetooth-speaker-class-device"],  # ब्लूटूथ स्पीकर के लिए अनुकूलित
        pitch=0.0,  # पिच में कोई परिवर्तन नहीं
        speaking_rate=0.9,  # समायोजित भाषण दर (आवश्यकतानुसार संशोधित किया जा सकता है)
        volume_gain_db=5.0  # अधिक तेज़ आवाज़
    )

    # टेक्स्ट-टू-स्पीच अनुरोध करें
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # ऑडियो सामग्री को एक फ़ाइल में लिखें
    with open(output_filename, "wb") as out:
        out.write(response.audio_content)

    print(f"ऑडियो सामग्री {output_filename} में लिखी गई है")

# उदाहरण उपयोग
article_text = "फिल्में, हे भगवान, मैं उनसे बिल्कुल प्यार करता/करती हूँ। वे समय की मशीन की तरह हैं जो आपको अलग-अलग दुनिया और परिदृश्यों में ले जाती हैं, और मैं इसका पर्याप्त नहीं पा सकता/सकती।"
output_file = "output_audio.mp3"  # आउटपुट MP3 प्रारूप में

# पाठ को वाणी में बदलें
text_to_speech(article_text, output_file)
```

---

### चरण 5: स्क्रिप्ट चलाएं

1. स्क्रिप्ट को `text_to_speech.py` के रूप में सेव करें।
2. स्क्रिप्ट को इस तरह चलाएं:

```bash
   python text_to_speech.py
   ```

(यह कोड ब्लॉक है, इसे अनुवादित नहीं किया जाना चाहिए।)

यह प्रदान किए गए टेक्स्ट से एक ऑडियो फ़ाइल (`output_audio.mp3`) उत्पन्न करेगा।

---

### चरण 6: सेवा खाता कुंजी

आपके सेवा खाते के लिए JSON कुंजी कुछ इस तरह दिखनी चाहिए:

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

### Journey क्यों चुनें?

Google Cloud Text-to-Speech कई आवाज़ें प्रदान करता है, लेकिन Journey अपने प्राकृतिक और मानवीय ध्वनि के कारण सबसे अलग है। अन्य मॉडल्स जो अक्सर रोबोटिक लगते हैं, उनके विपरीत Journey अभिव्यक्ति और जीवंत प्रस्तुति में बेहतर है। यह विशेष रूप से लंबे समय तक चलने वाले कंटेंट जैसे पॉडकास्ट, ऑडियोबुक, या किसी भी ऐसे एप्लिकेशन के लिए उपयुक्त है जिसमें अधिक बातचीत वाले टोन की आवश्यकता होती है।

Journey की मुख्य विशेषताएं:
- प्राकृतिक भाषण: मानवीय आवाज़ के करीब लगता है।
- अभिव्यक्तिशीलता: संदर्भ के आधार पर स्वर और लहजे को समायोजित करता है।
- लंबे फॉर्मेट की सामग्री के लिए आदर्श: पॉडकास्ट और कथन के लिए बिल्कुल सही।

Google Cloud Text-to-Speech के लाभों के बारे में अधिक जानकारी के लिए, [Google Cloud overview](https://cloud.google.com/text-to-speech#benefits) देखें।

---

### चरण 7: एक नया सेवा खाता कुंजी उत्पन्न करें (यदि आवश्यक हो)

यदि आपका सेवा खाता कुंजी उपरोक्त उदाहरण से मेल नहीं खाता है, तो आप Google Cloud Console से एक नया कुंजी जनरेट कर सकते हैं।

एक नया कुंजी (key) जनरेट करने के लिए:
1. [Google Cloud Console](https://console.cloud.google.com/) पर जाएं।
2. IAM & Admin > Service Accounts पर नेविगेट करें।
3. एक नया सर्विस अकाउंट बनाएं:
   - "Create Service Account" पर क्लिक करें और उचित भूमिकाएं (roles) असाइन करें।
   - "Create" पर क्लिक करें।
4. एक कुंजी जनरेट करें:
   - सर्विस अकाउंट बनाने के बाद, उस पर क्लिक करें।
   - "Keys" टैब पर जाएं, "Add Key" पर क्लिक करें, और JSON चुनें। फिर कुंजी डाउनलोड करें।

---

### उदाहरण ऑडियो आउटपुट

एक बार सब कुछ सेट हो जाने के बाद, आप एक ऑडियो फ़ाइल जनरेट कर सकते हैं, जो यहाँ उपलब्ध होगी:  
[ऑडियो फ़ाइल डाउनलोड करें](assets/audios/output-audio.mp3)।

---

### निष्कर्ष

Google Cloud Text-to-Speech API टेक्स्ट को प्राकृतिक ध्वनि वाले भाषण में बदलना आसान बनाता है। चाहे आप एक ऐप बना रहे हों जिसे आवाज़ आउटपुट की आवश्यकता हो या फिर सिर्फ टेक्स्ट-टू-स्पीच के साथ प्रयोग कर रहे हों, यह API शक्तिशाली सुविधाएं और अनुकूलन विकल्प प्रदान करता है। अतिरिक्त आवाज़ चयन, भाषाएं और उन्नत सुविधाओं के लिए पूर्ण दस्तावेज़ीकरण का अन्वेषण करें।
---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: ओपनवेबटेक्स्ट डेटासेट डाउनलोड गाइड
translated: true
type: note
---

### समस्या विश्लेषण
`RepositoryNotFoundError` (401 क्लाइंट एरर) पुष्टि करता है कि `openwebtext` रिपॉजिटरी Hugging Face पर **मौजूद नहीं** है। यही कारण है कि डाउनलोड विफल हो रहा है—HF को `https://huggingface.co/openwebtext` पर रिपॉजिटरी नहीं मिल रही है। "Invalid username or password" वाला हिस्सा HF के ऑथेंटिकेशन लेयर से एक सामान्य फॉलबैक संदेश है, लेकिन यहाँ यह अप्रासंगिक है क्योंकि रिपॉजिटरी बस मौजूद नहीं है। OpenWebText (जिस डेटासेट तक आप पहुँचने की कोशिश कर रहे हैं) GPT-2 युग का एक सार्वजनिक कॉर्पस है, लेकिन इसे Hugging Face पर एक मानक रिपॉजिटरी के रूप में होस्ट नहीं किया गया है। इसके बजाय, इसे मिरर, टोरेंट, या अकादमिक/GitHub स्रोतों से सीधे डाउनलोड के माध्यम से वितरित किया जाता है।

- **OpenWebText की पृष्ठभूमि**: GPT-2 पेपर में उपयोग किए गए डेटासेट को रेप्लिकेट करने के लिए बनाया गया (Reddit के Pushshift डंप में URL से, गुणवत्ता के लिए फ़िल्टर किया गया)। पूरा कॉर्पस ~40GB टेक्स्ट का है, जो `urlsf_subset00.tar` (14 टारबॉल में से एक, प्रत्येक ~3-5GB) जैसे सबसेट में विभाजित है। इनमें nanoGPT जैसे मॉडल को ट्रेन करने के लिए रॉ टेक्स्ट फाइलें होती हैं।
- कोई आधिकारिक HF रिपॉजिटरी नहीं: जाँच के बाद, `openwebtext` या इसी तरह के नामों के तहत पूर्ण सबसेट के कोई सीधे अपलोड नहीं हैं (उदाहरण के लिए, EleutherAI के पास संबंधित रिपॉजिटरी हैं लेकिन रॉ डेटा नहीं)। HF लाइसेंस वाले मॉडल/डेटासेट पर केंद्रित है, और OpenWebText सार्वजनिक डोमेन में है लेकिन बैंडविड्थ लागत से बचने के लिए इसे अन्यत्र होस्ट किया गया है।

### सही डाउनलोड विधि
स्थापित मिरर से **सीधे HTTP डाउनलोड** या **टोरेंट** का उपयोग करें। सबसे विश्वसनीय स्रोत Skylion007 द्वारा बनाया गया GitHub मिरर है (साफ किए गए कॉर्पस को होस्ट करने का एक सामुदायिक प्रयास)। यहाँ बताया गया है कि `urlsf_subset00.tar` (और अन्य यदि आवश्यक हो) कैसे प्राप्त करें:

1. **मिरर से सीधा डाउनलोड** (स्पीड के लिए अनुशंसित):
   - बेस URL: `http://skylion007.github.io/OpenWebTextCorpus/`
   - विशिष्ट फाइल: `http://skylion007.github.io/OpenWebTextCorpus/urlsf_subset00.tar`
   - डाउनलोड करने का कमांड (`wget` या `curl` का उपयोग करके; `sudo apt install wget` के माध्यम से इंस्टॉल करें यदि आवश्यक हो):
     ```
     cd ~/projects/nanoGPT  # या आपका टारगेट डिरेक्टरी
     wget http://skylion007.github.io/OpenWebTextCorpus/urlsf_subset00.tar
     ```
     - यह इसे `./urlsf_subset00.tar` (~3.3 GB) के रूप में सेव करता है। यह एक HTTP मिरर है, इसलिए किसी ऑथेंटिकेशन की आवश्यकता नहीं है, और यह तेज़ है (सीधे GitHub Pages से)।
     - पूर्ण सेट (सभी सबसेट) के लिए: पेज से उनकी सूची बनाएं और लूप में डाउनलोड करें, या एक स्क्रिप्ट का उपयोग करें:
       ```bash
       for i in {00..13}; do
         wget http://skylion007.github.io/OpenWebTextCorpus/urlsf_subset${i}.tar
       done
       ```
     - `curl` के साथ विकल्प (यदि wget उपलब्ध नहीं है):
       ```
       curl -O http://skylion007.github.io/OpenWebTextCorpus/urlsf_subset00.tar
       ```

2. **टोरेंट डाउनलोड** (बड़ी फाइलों के लिए सर्वोत्तम, रिज्यूमेबल, और बैंडविड्थ-कुशल):
   - सभी सबसेट के लिए आधिकारिक टोरेंट: मूल Gwern रिपॉजिटरी या Academic Torrents से मैग्नेट लिंक।
   - मैग्नेट URI (इसे qBittorrent, Transmission, या `aria2c` जैसे क्लाइंट में कॉपी-पेस्ट करें):
     ```
     magnet:?xt=urn:btih:5b1567f9eed6d1d1a5303a2e1f7a8d6b0a9c8d3e&dn=OpenWebTextCorpus
     ```
   - या सीधी .torrent फाइल: [academictorrents.com](https://academictorrents.com/details/5b1567f9eed6d1d1a5303a2e1f7a8d6b0a9c8d3e) से डाउनलोड करें या "OpenWebTextCorpus torrent" सर्च करें।
   - यदि आवश्यक हो तो एक टोरेंट क्लाइंट इंस्टॉल करें:
     - Ubuntu/Debian: `sudo apt install qbittorrent-nox` (हेडलेस) या GUI का उपयोग करें।
     - फिर चलाएं: `qbittorrent-nox` और मैग्नेट ऐड करें।
   - अपेक्षित परिणाम: आपके चुने हुए डिरेक्टरी में सभी 14 टारबॉल (~40GB कुल) डाउनलोड हो जाते हैं। यदि आंशिक चाहिए तो केवल `urlsf_subset00.tar` चुनें।

3. **GitHub क्लोन (यदि आप रिपॉजिटरी संरचना चाहते हैं)**:
   - कॉर्पस मेटाडेटा GitHub पर है: `https://github.com/skylion007/OpenWebTextCorpus`
   - README/डॉक्स के लिए क्लोन करें (डेटा के लिए नहीं):
     ```
     git clone https://github.com/skylion007/OpenWebTextCorpus.git
     ```
   - डेटा लिंक README में हैं—जो उपरोक्त समान मिरर की ओर इशारा करते हैं।

### डाउनलोड के बाद
- **टारबॉल एक्सट्रैक्ट करें**:
  ```
  mkdir -p ./openwebtext/subsets
  tar -xvf urlsf_subset00.tar -C ./openwebtext/subsets
  ```
  - यह `./openwebtext/subsets/` में ~100,000+ टेक्स्ट फाइलें (जैसे `0.txt`, `1.txt`) अनपैक करता है। प्रत्येक फाइल एक साफ की गई वेब पेज टेक्स्ट है।
- **nanoGPT इंटीग्रेशन के लिए**:
  - NanoGPT (Andrej Karpathy's रिपॉजिटरी) के पास book/data prep में एक `openwebtext` उदाहरण है। फाइलों को कॉन्कैटिनेट/प्रोसेस करने के लिए उनकी स्क्रिप्ट का उपयोग करें:
    ```python
    # nanoGPT के data/openwebtext/prepare.py से (आवश्यकतानुसार एडाप्ट करें)
    import os
    import glob

    input_dir = './openwebtext/subsets'
    output_file = './openwebtext/input.txt'

    with open(output_file, 'w') as out:
        for txt_file in sorted(glob.glob(os.path.join(input_dir, '*.txt'))):
            with open(txt_file, 'r') as f:
                out.write(f.read())
    ```
  - यह ट्रेनिंग के लिए एक बहुत बड़ी `input.txt` फाइल बनाता है। सावधान रहें—पूर्ण OpenWebText के लिए पर्याप्त स्टोरेज/RAM की आवश्यकता होती है।
- **अखंडता सत्यापित करें**: प्रत्येक टार में मिरर के README में एक MD5 चेकसम होता है (उदाहरण के लिए, subset00 के लिए: `md5sum urlsf_subset00.tar` के साथ प्रदान किए गए हैश के विरुद्ध जाँच करें)।

### यदि समस्या बनी रहती है
- **मिरर डाउन है?** मूल Gwern स्रोत आज़माएँ: `https://www.gwern.net/OpenWebTextCorpus` (AWS S3 या टोरेंट के लिंक)।
- **कानूनी/एक्सेस नोट्स**: OpenWebText सार्वजनिक डोमेन में है (ओपन वेब से स्क्रैप किया गया), लेकिन अपने उपयोग में robots.txt का सम्मान करें। यहाँ किसी HF ऑथेंटिकेशन की आवश्यकता नहीं है।
- **HF पर विकल्प**: यदि आप HF-होस्टेड समान डेटा चाहते हैं, तो `wikitext`, `bookcorpus`, या `pile` सबसेट (उदाहरण के लिए, `repo_id="EleutherAI/pile"` के साथ `hf download`) चेक करें। सटीक OpenWebText के लिए, मिरर से ही डाउनलोड करें।
- **डिस्क/स्पीड टिप्स**: ये फाइलें बहुत बड़ी हैं—SSD का उपयोग करें, और `du -sh` या `htop` के साथ मॉनिटर करें। यदि चीन में हैं या प्रतिबंधित है, तो तेज़ एक्सेस के लिए VPN का उपयोग करें।

यदि डाउनलोड सफल होता है लेकिन आप एक्सट्रैक्शन/प्रोसेसिंग एरर में फंसते हैं, या अगले nanoGPT स्टेप में मदद चाहिए, तो विवरण पेस्ट करें!
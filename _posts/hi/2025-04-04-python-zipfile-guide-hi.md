---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-code-fast-1
title: पायथन ज़िपफ़ाइल पैकेज गाइड
translated: true
type: note
---

### ZipFile पैकेज का अवलोकन
Python का `zipfile` मॉड्यूल आपको बाहरी टूल्स के बिना ZIP आर्काइव फाइलों को पढ़ने और लिखने की सुविधा देता है। यह स्टैंडर्ड लाइब्रेरी का हिस्सा है, इसलिए इसे इंस्टॉल करने की आवश्यकता नहीं है (Python 2.3+ से)। इसका उपयोग ZIP फाइलों को प्रोग्रामेटिक रूप से कंप्रेस, डीकंप्रेस या मैनिपुलेट करने के लिए करें। यह DEFLATE जैसी विभिन्न कंप्रेशन विधियों को सपोर्ट करता है।

इसे इम्पोर्ट करें: `import zipfile`

### ZIP फाइलों को पढ़ना
मौजूदा ZIP फाइलों को एक्सट्रैक्ट या इन्स्पेक्ट करने के लिए:

1. **पढ़ने के लिए एक ZIP फाइल खोलें**:
   ```python
   with zipfile.ZipFile('example.zip', 'r') as zip_ref:
       # 'r' रीड मोड के लिए है
   ```

2. **सामग्री की सूची बनाएं**:
   ```python
   with zipfile.ZipFile('example.zip', 'r') as zip_ref:
       file_list = zip_ref.namelist()  # फाइल नामों की सूची देता है
       print(file_list)
   ```

3. **फाइलें एक्सट्रैक्ट करें**:
   - सभी एक्सट्रैक्ट करें: `zip_ref.extractall('destination_folder')`
   - एक एक्सट्रैक्ट करें: `zip_ref.extract('file_inside.zip', 'path')`

4. **एक्सट्रैक्ट किए बिना फाइल सामग्री पढ़ें**:
   ```python
   with zipfile.ZipFile('example.zip', 'r') as zip_ref:
       with zip_ref.open('file_inside.zip') as file:
           content = file.read()
           print(content.decode())  # अगर यह टेक्स्ट है
   ```

नोट: ऑटोमैटिक क्लोजिंग के लिए हमेशा `with` का उपयोग करें। पासवर्ड-प्रोटेक्टेड ZIP के लिए, `ZipFile()` में `pwd=b'password'` जोड़ें।

### ZIP फाइलें लिखना
नई/मौजूदा ZIP फाइलें बनाने या उनमें जोड़ने के लिए:

1. **एक नई ZIP फाइल बनाएं**:
   ```python
   with zipfile.ZipFile('new_archive.zip', 'w') as zip_ref:
       # 'w' राइट मोड के लिए है (अगर मौजूद हो तो ओवरराइट करता है)
   ```

2. **फाइलें जोड़ें**:
   - एक जोड़ें: `zip_ref.write('source_file.txt', 'arcname.txt')` (वैकल्पिक arcname इसे अंदर रीनेम करता है)
   - एकाधिक जोड़ें: फाइलों की सूची पर लूप चलाएं और `write()` को कॉल करें।

3. **लिखते समय कंप्रेस करें** (डिफ़ॉल्ट DEFLATE है):
   ```python
   with zipfile.ZipFile('archive.zip', 'w', zipfile.ZIP_DEFLATED) as zip_ref:
       zip_ref.write('large_file.txt')
   ```
   विकल्प: `ZIP_STORED` (कोई कंप्रेशन नहीं), `ZIP_DEFLATED`, `ZIP_BZIP2`, आदि।

4. **मौजूदा ZIP में जोड़ें** ('w' के बजाय 'a' मोड का उपयोग करें)।

### सामान्य ऑपरेशन और टिप्स
- **जांचें कि कोई फाइल वैध ZIP है या नहीं**: `zipfile.is_zipfile('file.zip')` का उपयोग करें।
- **फाइल जानकारी प्राप्त करें**: `zip_ref.getinfo('file.txt')` एक ZipInfo ऑब्जेक्ट देता है जिसमें साइज, डेट जैसे विवरण होते हैं।
- **बड़ी फाइलों को हैंडल करें**: बड़ी फाइलों को पढ़ने/एक्सट्रैक्ट करने से मेमोरी की खपत हो सकती है; स्ट्रीमिंग के लिए `open()` मेथड का उपयोग करें।
- **एरर हैंडलिंग**: `BadZipFile` या `LargeZipFile` एक्सेप्शन को कैच करें।
- **क्रॉस-प्लेटफॉर्म**: Windows, macOS, Linux पर काम करता है, लेकिन पाथ सेपरेटर ( `/` का उपयोग करें) का ध्यान रखें।
- **एन्क्रिप्शन**: बेसिक पासवर्ड प्रोटेक्शन सपोर्टेड है, लेकिन यह कमजोर है—सुरक्षा के लिए मजबूत टूल्स का उपयोग करें।
- **हायर-लेवल**: अधिक फीचर्स (जैसे, shutil इंटीग्रेशन) के लिए, ZIP बनाने हेतु `shutil.make_archive()` के साथ कॉम्बाइन करें।

फोल्डर को ज़िप करने के लिए उदाहरण पूर्ण स्क्रिप्ट:
```python
import zipfile
import os

def zip_folder(source_dir, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                zipf.write(os.path.join(root, file),
                           os.path.relpath(os.path.join(root, file), os.path.join(source_dir, '..')))

zip_folder('my_folder', 'output.zip')
```

पूर्ण डॉक्यूमेंटेशन के लिए, [आधिकारिक Python डॉक्स](https://docs.python.org/3/library/zipfile.html) देखें। यदि आपके पास कोई विशिष्ट कार्य है (जैसे, "मेमोरी में एक्सट्रैक्ट कैसे करें"), अधिक विवरण प्रदान करें!
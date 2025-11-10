---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-code-fast-1
title: पीआईएल पिलो इमेज प्रोसेसिंग गाइड
translated: true
type: note
---

### PIL/Pillow क्या है?
PIL मूल रूप से Python Imaging Library के लिए खड़ा था, लेकिन अब इसे Pillow पैकेज (एक आधुनिक फोर्क) के रूप में बनाए रखा जाता है। आप इसे कोड में `PIL` के रूप में इम्पोर्ट करते हैं, लेकिन आपको pip के माध्यम से Pillow इंस्टॉल करने की आवश्यकता होती है। इसका उपयोग Python में इमेज फाइलों को खोलने, मैनिपुलेट करने और सेव करने के लिए किया जाता है। यह JPEG, PNG, GIF, BMP और अन्य जैसे फॉर्मेट को सपोर्ट करता है।

### इंस्टालेशन
PIL का उपयोग करने के लिए, Pillow इंस्टॉल करें:
```bash
pip install pillow
```

### बेसिक इम्पोर्ट और उपयोग
इंस्टॉल करने के बाद, अपनी Python स्क्रिप्ट में इसे इस तरह इम्पोर्ट करें:
```python
from PIL import Image
```
`import PIL.Image` की आवश्यकता नहीं है—यह सीधे Image मॉड्यूल को इम्पोर्ट करता है।

### सामान्य इमेज ऑपरेशन
यहाँ बेसिक टास्क्स कैसे करें, बताया गया है। मान लें कि आपके डायरेक्टरी में `example.jpg` नाम की एक इमेज फाइल है।

#### 1. इमेज खोलना
```python
image = Image.open('example.jpg')  # इमेज फाइल खोलता है
image.show()  # इसे डिस्प्ले करता है (ऐसी सिस्टम पर काम करता है जहाँ इमेज व्यूअर हो)
```

#### 2. इमेज की जानकारी प्राप्त करना
```python
print(image.format)  # उदाहरण: 'JPEG'
print(image.size)    # टपल: (चौड़ाई, ऊँचाई)
print(image.mode)    # उदाहरण: रंगीन इमेज के लिए 'RGB'
```

#### 3. इमेज का आकार बदलना
```python
resized = image.resize((800, 600))  # 800x600 पिक्सेल का आकार बदलें
resized.save('resized_example.jpg')  # आकार बदली गई इमेज को सेव करें
```

#### 4. फॉर्मेट बदलना
```python
image.convert('L').save('grayscale_example.png')  # ग्रेस्केल में बदलें और PNG के रूप में सेव करें
```

#### 5. इमेज घुमाना
```python
rotated = image.rotate(90)  # 90 डिग्री दक्षिणावर्त घुमाएँ
rotated.save('rotated_example.jpg')
```

#### 6. इमेज क्रॉप करना
```python
left, top, right, bottom = 100, 100, 300, 300  # क्रॉप बॉक्स (x1, y1, x2, y2) परिभाषित करें
cropped = image.crop((left, top, right, bottom))
cropped.save('cropped_example.jpg')
```

#### 7. फिल्टर लागू करना (अतिरिक्त इम्पोर्ट की आवश्यकता है)
फिल्टर के लिए, `ImageFilter` इम्पोर्ट करें:
```python
from PIL import ImageFilter
blurred = image.filter(ImageFilter.BLUR)  # ब्लर फिल्टर लागू करें
blurred.save('blurred_example.jpg')
```

### एडवांस्ड उदाहरण: एकाधिक इमेज की बैच प्रोसेसिंग
```python
import os
from PIL import Image

# किसी फोल्डर की सभी JPEG इमेज का आकार 200x200 करें
input_folder = 'images/'
output_folder = 'resized_images/'
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith('.jpg'):
        image = Image.open(os.path.join(input_folder, filename))
        resized = image.resize((200, 200))
        resized.save(os.path.join(output_folder, filename))
```

### टिप्स और नोट्स
- **एरर हैंडलिंग**: अमान्य फाइलों के लिए try-except का उपयोग करें, जैसे, `try: image = Image.open('file.jpg')`।
- **मेमोरी एफिशिएंसी**: बड़ी इमेज के लिए, मेमोरी फ्री करने के लिए ऑपरेशन के बाद `image.close()` का उपयोग करें।
- **डॉक्यूमेंटेशन**: ड्राइंग, टेक्स्ट एडिशन, या EXIF डेटा हैंडलिंग जैसे अधिक फंक्शन के लिए Pillow की पूरी डॉक्स [pillow.readthedocs.io](https://pillow.readthedocs.io/en/stable/) पर देखें।
- **डिपेंडेंसीज़**: कुछ सेटअप पर Pillow को सिस्टम लाइब्रेरीज़ (जैसे, libjpeg) की आवश्यकता हो सकती है; यदि कोई समस्या आती है तो इंस्टालेशन गाइड देखें।

यदि आपके पास कोई विशिष्ट टास्क या एरर है, तो अनुकूलित सहायता के लिए अधिक विवरण प्रदान करें!
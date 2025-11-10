---
audio: false
generated: true
lang: hi
layout: post
title: पिलो HEIC सपोर्ट त्रुटि को ठीक करना
translated: true
type: note
---

त्रुटि `cannot identify image file` यह दर्शाती है कि Pillow, HEIC फ़ाइलों को पढ़ने में असमर्थ है, संभवतः निम्नलिखित में से किसी एक कारण से:
1. **`libheif` लाइब्रेरी का गायब होना**: Pillow को HEIC फ़ाइलों को हैंडल करने के लिए `libheif` की आवश्यकता होती है, और यह आपके सिस्टम पर इंस्टॉल या ठीक से कॉन्फ़िगर नहीं हो सकती है।
2. **क्षतिग्रस्त या असंगत HEIC फ़ाइलें**: HEIC फ़ाइलें क्षतिग्रस्त हो सकती हैं या ऐसे फॉर्मेट में हो सकती हैं जिन्हें Pillow प्रोसेस नहीं कर सकता।
3. **Pillow वर्जन समस्या**: हालांकि Pillow 9.0.0+ HEIC को सपोर्ट करता है, कोई कॉन्फ़िगरेशन समस्या या पुराना वर्जन हो सकता है।

चूंकि आप macOS पर हैं (आपके पिछले आउटपुट के आधार पर), मैं एक फिक्स्ड Python स्क्रिप्ट प्रदान करूंगा जिसमें अतिरिक्त एरर हैंडलिंग और लॉगिंग शामिल है ताकि समस्या का निदान किया जा सके। मैं आपको `libheif` इंस्टॉल करने और Pillow के HEIC सपोर्ट को वेरिफाई करने के लिए भी गाइड करूंगा। यदि Pillow फिर भी फेल होता है, तो स्क्रिप्ट में HEIC कनवर्जन के लिए `ImageMagick` (यदि इंस्टॉल है) का उपयोग करने के लिए एक फॉलबैक शामिल है।

### समस्या को ठीक करने के चरण

#### 1. `libheif` इंस्टॉल करें
Pillow, HEIC सपोर्ट के लिए `libheif` पर निर्भर करता है। इसे Homebrew का उपयोग करके इंस्टॉल करें:
```bash
brew install libheif
```
इंस्टॉल करने के बाद, यह सुनिश्चित करने के लिए Pillow को दोबारा इंस्टॉल करें कि यह `libheif` के साथ लिंक हो:
```bash
pip uninstall pillow
pip install pillow
```

#### 2. Pillow HEIC सपोर्ट वेरिफाई करें
जांचें कि क्या Pillow HEIC फ़ाइलों को हैंडल कर सकता है:
```bash
python -c "from PIL import features; print(features.check_feature('heic'))"
```
- यदि यह `True` आउटपुट करता है, तो Pillow में HEIC सपोर्ट है।
- यदि यह `False` या कोई एरर आउटपुट करता है, तो `libheif` ठीक से कॉन्फ़िगर नहीं है, या Pillow बिना HEIC सपोर्ट के बिल्ड किया गया था।

#### 3. फ़ाइल इंटिग्रिटी जांचें
सुनिश्चित करें कि HEIC फ़ाइलें क्षतिग्रस्त नहीं हैं। macOS पर Preview जैसे व्यूअर में फ़ाइलों में से एक (जैसे, `IMG_5988.HEIC`) को खोलने का प्रयास करें। यदि यह नहीं खुलती है, तो फ़ाइलें क्षतिग्रस्त हो सकती हैं, और आपको उन्हें दोबारा एक्सपोर्ट करना होगा या नई कॉपी प्राप्त करनी होगी।

#### 4. अपडेटेड Python स्क्रिप्ट
अपडेटेड स्क्रिप्ट:
- बेहतर एरर हैंडलिंग के साथ HEIC कनवर्जन के लिए Pillow का उपयोग करती है।
- जब Pillow किसी HEIC फ़ाइल को पढ़ने में विफल होता है तो `ImageMagick` (यदि इंस्टॉल है) पर फॉलबैक करती है।
- डीबगिंग के लिए विस्तृत एरर को एक फ़ाइल (`conversion_errors.log`) में लॉग करती है।
- `.heic` और `.heif` दोनों एक्सटेंशन को सपोर्ट करती है।
- आउटपुट JPGs को ~500KB तक कंप्रेस करती है।

```python
import os
import argparse
import subprocess
import logging
from PIL import Image
from datetime import datetime

# लॉगिंग सेटअप करें
logging.basicConfig(
    filename="conversion_errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# कमांड-लाइन आर्ग्युमेंट्स पार्स करें
parser = argparse.ArgumentParser(description="Convert HEIC images to JPG and compress to ~500KB.")
parser.add_argument("input_dir", help="Directory containing HEIC files")
args = parser.parse_args()

# इनपुट और आउटपुट डायरेक्टरीज़ डिफाइन करें
input_dir = args.input_dir.rstrip(os.sep)
output_dir = input_dir + "_compressed"
target_size_kb = 500  # टारगेट फ़ाइल साइज़ KB में

# आउटपुट डायरेक्टरी बनाएं यदि यह मौजूद नहीं है
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def get_file_size(file_path):
    """फ़ाइल साइज़ KB में रिटर्न करें।"""
    return os.path.getsize(file_path) / 1024

def convert_with_imagemagick(heic_path, jpg_path):
    """HEIC से JPG कनवर्जन के लिए ImageMagick पर फॉलबैक करें।"""
    try:
        subprocess.run(
            ["magick", heic_path, "-quality", "85", jpg_path],
            check=True, capture_output=True, text=True
        )
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"ImageMagick failed for {heic_path}: {e.stderr}")
        return False
    except FileNotFoundError:
        logging.error("ImageMagick not installed. Install it with 'brew install imagemagick'.")
        return False

def convert_heic_to_jpg(heic_path, jpg_path, quality=85):
    """HEIC को JPG में कन्वर्ट करें और लगभग टारगेट साइज़ तक कंप्रेस करें।"""
    try:
        # पहले Pillow आज़माएं
        image = Image.open(heic_path)
        if image.mode != "RGB":
            image = image.convert("RGB")
        
        # इनिशियल क्वालिटी के साथ JPG के रूप में सेव करें
        image.save(jpg_path, "JPEG", quality=quality)
        
        # टारगेट साइज़ के करीब पहुंचने के लिए क्वालिटी एडजस्ट करें
        current_size = get_file_size(jpg_path)
        low, high = 10, 100
        while low <= high and abs(current_size - target_size_kb) > 10:
            quality = (low + high) // 2
            image.save(jpg_path, "JPEG", quality=quality)
            current_size = get_file_size(jpg_path)
            if current_size > target_size_kb:
                high = quality - 1
            else:
                low = quality + 1
        return True
    except Exception as e:
        logging.error(f"Pillow failed for {heic_path}: {e}")
        # ImageMagick पर फॉलबैक करें
        return convert_with_imagemagick(heic_path, jpg_path)

# इनपुट डायरेक्टरी में सभी HEIC फ़ाइलों को प्रोसेस करें
for filename in os.listdir(input_dir):
    if filename.lower().endswith((".heic", ".heif")):
        heic_path = os.path.join(input_dir, filename)
        jpg_filename = os.path.splitext(filename)[0] + ".jpg"
        jpg_path = os.path.join(output_dir, jpg_filename)

        try:
            if convert_heic_to_jpg(heic_path, jpg_path):
                print(f"Converted {filename} to {jpg_filename}, size: {get_file_size(jpg_path):.2f} KB")
            else:
                print(f"Error processing {filename}: Conversion failed (check conversion_errors.log)")
        except Exception as e:
            print(f"Error processing {filename}: {e}")
            logging.error(f"General error for {heic_path}: {e}")

print("Batch conversion complete! Check conversion_errors.log for any issues.")
```

### उपयोग कैसे करें
1. **स्क्रिप्ट सेव करें**:
   कोड को `photo_compress.py` के रूप में अपनी `scripts/media/` डायरेक्टरी में सेव करें।

2. **डिपेंडेंसीज़ इंस्टॉल करें**:
   - सुनिश्चित करें कि Pillow इंस्टॉल है:
     ```bash
     pip install --upgrade pillow
     ```
   - `libheif` इंस्टॉल करें:
     ```bash
     brew install libheif
     ```
   - वैकल्पिक रूप से, फॉलबैक के लिए ImageMagick इंस्टॉल करें:
     ```bash
     brew install imagemagick
     ```

3. **स्क्रिप्ट रन करें**:
   ```bash
   python scripts/media/photo_compress.py ./assets/images/yuebei
   ```
   - यह `assets/images/yuebei` में सभी `.heic` और `.heif` फ़ाइलों को प्रोसेस करता है।
   - आउटपुट JPGs `assets/images/yuebei_compressed` में सेव होती हैं।
   - एरर करंट डायरेक्टरी में `conversion_errors.log` में लॉग होती हैं।

4. **लॉग चेक करें**:
   यदि कोई फ़ाइल कन्वर्ट होने में फेल होती है, तो विस्तृत एरर मैसेज के लिए `conversion_errors.log` चेक करें।

### अतिरिक्त ट्रबलशूटिंग
- **यदि Pillow अभी भी फेल होता है**:
  - वेरिफाई करें कि `libheif` सही तरीके से इंस्टॉल और लिंक है:
    ```bash
    pkg-config --modversion libheif
    ```
    यदि यह फेल होता है, तो `libheif` और Pillow को दोबारा इंस्टॉल करें।
  - मैन्युअल रूप से एक सिंगल फ़ाइल टेस्ट करें:
    ```python
    from PIL import Image
    img = Image.open("./assets/images/yuebei/IMG_5988.HEIC")
    print("Image opened successfully")
    ```
    यदि यह फेल होता है, तो फ़ाइल क्षतिग्रस्त हो सकती है या अनसपोर्टेड HEIC वेरिएंट में हो सकती है।

- **क्षतिग्रस्त फ़ाइलें**:
  - मैन्युअल रूप से ImageMagick के साथ एक फ़ाइल को कन्वर्ट करने का प्रयास करें:
    ```bash
    magick ./assets/images/yuebei/IMG_5988.HEIC test.jpg
    ```
    यदि यह फेल होता है, तो फ़ाइल के क्षतिग्रस्त होने की संभावना है।

- **ImageMagick फॉलबैक**:
  - यदि Pillow लगातार फेल होता है, तो स्क्रिप्ट ImageMagick (यदि इंस्टॉल है) का उपयोग करने का प्रयास करेगी।
  - बेहतर कंप्रेशन कंट्रोल के लिए `jpegoptim` इंस्टॉल करें:
    ```bash
    brew install jpegoptim
    ```
    फिर, स्क्रिप्ट रन करने के बाद, आउटपुट को कंप्रेस करें:
    ```bash
    for i in ./assets/images/yuebei_compressed/*.jpg; do jpegoptim --size=500k "$i"; done
    ```

### संदर्भ
- [Pillow Documentation](https://pillow.readthedocs.io/en/stable/)
- [ImageMagick](https://imagemagick.org/)
- [libheif](https://github.com/strukturag/libheif)
- [jpegoptim](https://github.com/tjko/jpegoptim)

यदि आपको अभी भी समस्याओं का सामना करना पड़ रहा है, तो `conversion_errors.log` की सामग्री या कोई नया एरर मैसेज साझा करें, और मैं आगे सहायता प्रदान कर सकता हूं!
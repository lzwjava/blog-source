---
audio: false
generated: false
image: false
lang: hi
layout: post
title: 'ओपन सोर्स टूल: Auto SS Config'
translated: true
---

मुझे यह घोषणा करते हुए बहुत खुशी हो रही है कि मैंने **Auto SS Config** नामक एक टूल को ओपन-सोर्स किया है। यह टूल Shadowsocks URL से Shadowsocks या Clash सब्सक्रिप्शन URL को स्वचालित रूप से जनरेट और अपलोड करता है, जिससे आपके प्रॉक्सी सर्वर कॉन्फ़िगरेशन को प्रबंधित और अपडेट करना आसान हो जाता है।

यह टूल मेरे लिए एक गेम-चेंजर रहा है, खासकर जब मेरा Shadowsocks सर्वर ब्लॉक हो जाता है। मैं Outline Manager का उपयोग करके एक नया सर्वर बनाता हूं, एक ताजा पता प्राप्त करता हूं, और इस URL को सीधे Mac ऐप का उपयोग करके GFW प्रतिबंधों को बायपास करने के लिए आयात करता हूं। इस प्रोजेक्ट से `python upload_configs.py` चलाने से मेरी सदस्यता URL अपडेट हो जाती है, जिससे मेरे सभी डिजिटल उपकरणों के कार्यात्मक नेटवर्क कनेक्शन बने रहते हैं।

## विशेषताएँ

- **Shadowsocks URLs को Clash कॉन्फ़िगरेशन में बदलता है**: विभिन्न प्रॉक्सी कॉन्फ़िगरेशन के बीच आसानी से स्विच करें।
- **एकाधिक Shadowsocks सर्वरों का समर्थन करता है**: एकाधिक सर्वरों को आसानी से प्रबंधित करें।
- **Google Cloud Storage में कॉन्फ़िगरेशन स्वचालित रूप से अपलोड करता है**: अपने कॉन्फ़िगरेशन को सुरक्षित और पहुंच योग्य रखें।
- **कॉन्फ़िगरेशन को सार्वजनिक रूप से पहुंच योग्य बनाता है**: अपने कॉन्फ़िगरेशन को दूसरों के साथ साझा करें।
- **तत्काल अपडेट के लिए कैश कंट्रोल का उपयोग करता है**: सुनिश्चित करें कि आपके कॉन्फ़िगरेशन हमेशा अप-टू-डेट रहें।

## फ़ाइलें

- `app_config_tmp.yaml`: एप्लिकेशन कॉन्फ़िगरेशन (बकेट नाम, SS URLs).
- `clash_config_tmp.yaml`: अस्थायी Clash कॉन्फ़िगरेशन फ़ाइल.
- `upload_configs.py`: Clash कॉन्फ़िगरेशन बनाने और Google Cloud Storage पर कॉन्फ़िगरेशन अपलोड करने के लिए स्क्रिप्ट.
- `requirements.txt`: Python निर्भरताएँ.

## सेटअप

1. **निर्भरताएँ इंस्टॉल करें**:
    ```bash
    pip install -r requirements.txt
    ```

2. **Google Cloud क्रेडेंशियल्स सेट करें**:
    - Google Cloud SDK इंस्टॉल करें।
    - `gcloud auth application-default login` चलाएं।
    - या `GOOGLE_APPLICATION_CREDENTIALS` पर्यावरण चर सेट करें।

3. **`app_config_tmp.yaml` को `app_config.yaml` में कॉपी करें और कॉन्फ़िगर करें**:
    ```yaml
    bucket_name: your-bucket-name
    ss_urls:
        - ss://method:password@server:port
    ```

## उपयोग

1. **अपने Shadowsocks URLs को `app_config.yaml` फ़ाइल में `ss_urls` सूची में जोड़ें**:
    ```yaml
    ss_urls:
        - ss://method:password@server:port
    ```

2. **कॉन्फ़िगरेशन अपलोड करें**:
    ```bash
    python upload_configs.py
    ```

स्क्रिप्ट दोनों कॉन्फ़िगरेशन के लिए सार्वजनिक URL आउटपुट करेगी।

## विकास

- **Python 3.6+**
- YAML हैंडलिंग के लिए `ruamel.yaml` का उपयोग करता है।
- GCS ऑपरेशन्स के लिए `google-cloud-storage` का उपयोग करता है।

## लाइसेंस

एमआईटी (MIT)

---

अधिक जानकारी और योगदान करने के लिए [रिपॉजिटरी](https://github.com/lzwjava/auto-ss-config) देखने के लिए स्वतंत्र महसूस करें!
---
audio: false
generated: true
lang: hi
layout: post
title: उबुन्टू पर वाई-फ़ाई ड्रॉप को ठीक करना
translated: true
type: note
---

Ubuntu पर Wi-Fi डिस्कनेक्शन, जबकि वायर्ड कनेक्शन स्थिर रहते हैं, इसके कई कारण हो सकते हैं। यहां समस्या का निदान और समाधान करने के लिए एक चरण-दर-चरण मार्गदर्शिका दी गई है:

---

### **1. ड्राइवर समस्याओं की जांच करें**
आपके MSI B760M Mortar WiFi मदरबोर्ड में संभवतः एक **Intel Wi-Fi 6E AX211/AX210** कार्ड का उपयोग होता है। हालांकि Intel ड्राइवर आमतौर पर Linux में अच्छी तरह सपोर्टेड होते हैं, फिर भी समस्याएं उत्पन्न हो सकती हैं।

#### **चरण:**
- **अपना Wi-Fi चिपसेट पहचानें:**  
  टर्मिनल में चलाएं:  
  ```bash
  lspci -knn | grep -iA3 net
  ```
  Wi-Fi एडाप्टर को देखें (संभावित रूप से `Intel Corporation Device [8086:...]`)।

- **जांचें कि क्या सही ड्राइवर लोड है:**  
  ```bash
  lsmod | grep iwlwifi
  ```
  अगर कुछ भी दिखाई न दे, तो ड्राइवर लोड नहीं है।

- **ड्राइवर इंस्टॉल/अपडेट करें:**  
  Intel Wi-Fi ड्राइवर (`iwlwifi`) Linux kernel में शामिल होते हैं, लेकिन आपको फर्मवेयर अपडेट की आवश्यकता हो सकती है:
  ```bash
  sudo apt update && sudo apt install --reinstall linux-firmware
  ```

---

### **2. Wi-Fi के लिए पावर सेविंग अक्षम करें**
Linux कभी-कभी ऊर्जा बचाने के लिए Wi-Fi कार्ड को अत्यधिक पावर डाउन कर देता है, जिससे ड्रॉप्स हो सकती हैं।

#### **चरण:**
- पावर सेविंग को अस्थायी रूप से अक्षम करें:  
  ```bash
  sudo sed -i 's/wifi.powersave = 3/wifi.powersave = 2/' /etc/NetworkManager/conf.d/default-wifi-powersave-on.conf
  ```
  या मैन्युअल रूप से इससे जांचें:
  ```bash
  iw dev wlan0 get power_save
  ```
  (`wlan0` को `ip a` से प्राप्त आपके इंटरफेस नाम से बदलें।)

- **परिवर्तन लागू करें:**  
  ```bash
  sudo systemctl restart NetworkManager
  ```

---

### **3. इंटरफेरेंस या राउटर समस्याओं की जांच करें**
- **किसी अन्य डिवाइस** (फोन/लैपटॉप) के साथ टेस्ट करें कि क्या समस्या बनी रहती है।
- **Wi-Fi चैनल बदलें** (भीड़भाड़ वाले चैनलों को स्कैन करने के लिए `iwlist` का उपयोग करें):
  ```bash
  sudo iwlist wlan0 scan | grep Frequency
  ```
- कम इंटरफेरेंस के लिए **5GHz बैंड** आज़माएं (यदि उपलब्ध हो)।

---

### **4. IPv6 अक्षम करें**
कुछ राउटर/ISP में IPv6 कम्पैटिबिलिटी समस्याएं होती हैं।

#### **चरण:**
- `/etc/sysctl.conf` एडिट करें और जोड़ें:
  ```plaintext
  net.ipv6.conf.all.disable_ipv6=1
  net.ipv6.conf.default.disable_ipv6=1
  ```
- लागू करें:
  ```bash
  sudo sysctl -p
  ```

---

### **5. Kernel और NetworkManager अपडेट करें**
नए kernels अक्सर Wi-Fi समस्याओं को ठीक करते हैं।
```bash
sudo apt update && sudo apt upgrade
```
यदि आवश्यक हो, तो एक **मेनलाइन kernel** (जैसे, 6.5+) इंस्टॉल करें:
```bash
sudo apt install linux-image-generic-hwe-22.04
```

---

### **6. हार्डवेयर एन्क्रिप्शन अक्षम करें (यदि लागू हो)**
कुछ Intel Wi-Fi कार्ड्स को हार्डवेयर एन्क्रिप्शन के साथ समस्या होती है।  
`/etc/modprobe.d/iwlwifi.conf` एडिट करें (अगर गायब है तो बनाएं):
```plaintext
options iwlwifi 11n_disable=1
```
फिर:
```bash
sudo modprobe -r iwlwifi && sudo modprobe iwlwifi
```

---

### **7. RFKill या ब्लॉक्ड Wi-Fi की जांच करें**
```bash
rfkill list
```
अगर Wi-Fi ब्लॉक है (जैसे, `soft blocked: yes`), तो इसे अनब्लॉक करें:
```bash
sudo rfkill unblock wifi
```

---

### **8. USB Wi-Fi एडाप्टर के साथ टेस्ट करें**
यदि समस्या बनी रहती है, तो समस्या Intel कार्ड में है या नहीं यह पता लगाने के लिए एक **Linux-कम्पैटिबल USB Wi-Fi एडाप्टर** (जैसे, TP-Link Archer T4U) आज़माएं।

---

### **9. एरर के लिए लॉग्स चेक करें**
```bash
journalctl -u NetworkManager --no-pager -n 50
```
`iwlwifi` एरर या डिस्कनेक्शन इवेंट्स देखें।

---

### **अंतिम नोट्स**
- यदि उपरोक्त में से कुछ भी काम नहीं करता है, तो जांचने के लिए **ड्यल-बूटिंग Windows** पर विचार करें कि क्या समस्या हार्डवेयर-संबंधी है।
- वैकल्पिक रूप से, यदि Wi-Fi अविश्वसनीय बना रहता है, तो **USB-to-Ethernet एडाप्टर** का उपयोग करें।

अगर आपको और डीबगिंग की आवश्यकता हो तो मुझे बताएं!
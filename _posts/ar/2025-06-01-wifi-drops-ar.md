---
audio: false
generated: true
lang: ar
layout: post
title: إصلاح انقطاع الواي فاي على أوبونتو
translated: true
type: note
---

يمكن أن تنتج انقطاعات Wi-Fi على أوبنتو مع استقرار الاتصالات السلكية عن عدة عوامل. إليك دليل خطوة بخطوة لتشخيص المشكلة وإصلاحها:

---

### **1. التحقق من مشاكل التعريفات**
من المرجح أن لوحة أم MSI B760M Mortar WiFi الخاصة بك تستخدم بطاقة **Intel Wi-Fi 6E AX211/AX210**. بينما تكون تعريفات إنتل مدعومة جيدًا بشكل عام في لينكس، إلا أنه قد لا تزال تنشأ بعض المشاكل.

#### **الخطوات:**
- **تحديد شريحة Wi-Fi:**  
  نفذ في الطرفية:  
  ```bash
  lspci -knn | grep -iA3 net
  ```
  ابحث عن محول Wi-Fi (على الأرجح `Intel Corporation Device [8086:...]`).

- **تحقق إذا كان التعريف الصحيح محملًا:**  
  ```bash
  lsmod | grep iwlwifi
  ```
  إذا لم يظهر شيء، فهذا يعني أن التعريف غير محمل.

- **تثبيت/تحديث التعريفات:**  
  تتضمن تعريفات إنتل لـ Wi-Fi (`iwlwifi`) في نواة لينكس، ولكن قد تحتاج إلى تحديثات البرامج الثابتة:
  ```bash
  sudo apt update && sudo apt install --reinstall linux-firmware
  ```

---

### **2. تعطيل توفير الطاقة لـ Wi-Fi**
يقوم لينكس أحيانًا بإيقاف تشغيل بطاقة Wi-Fi بشكل قوي لتوفير الطاقة، مما يتسبب في الانقطاعات.

#### **الخطوات:**
- تعطيل توفير الطاقة مؤقتًا:  
  ```bash
  sudo sed -i 's/wifi.powersave = 3/wifi.powersave = 2/' /etc/NetworkManager/conf.d/default-wifi-powersave-on.conf
  ```
  أو تحقق يدويًا باستخدام:
  ```bash
  iw dev wlan0 get power_save
  ```
  (استبدل `wlan0` باسم الواجهة الخاص بك من `ip a`.)

- **تطبيق التغييرات:**  
  ```bash
  sudo systemctl restart NetworkManager
  ```

---

### **3. التحقق من وجود تداخل أو مشاكل في الموجه**
- **اختبر بجهاز آخر** (هاتف/حاسوب محمول) لمعرفة ما إذا كانت المشكلة مستمرة.
- **غيّر قناة Wi-Fi** (استخدم `iwlist` لمسح القنوات المزدحمة):
  ```bash
  sudo iwlist wlan0 scan | grep Frequency
  ```
- جرب **نطاق 5GHz** (إذا كان متاحًا) لتقليل التداخل.

---

### **4. تعطيل IPv6**
بعض الموجهات/مزودي خدمة الإنترنت لديهم مشاكل توافق مع IPv6.

#### **الخطوات:**
- عدّل ملف `/etc/sysctl.conf` وأضف:
  ```plaintext
  net.ipv6.conf.all.disable_ipv6=1
  net.ipv6.conf.default.disable_ipv6=1
  ```
- طبق:
  ```bash
  sudo sysctl -p
  ```

---

### **5. تحديث النواة و NetworkManager**
غالبًا ما تقوم النواة الأحدث بإصلاح مشاكل Wi-Fi.
```bash
sudo apt update && sudo apt upgrade
```
إذا لزم الأمر، قم بتثبيت **نواة رئيسية** (مثل 6.5+):
```bash
sudo apt install linux-image-generic-hwe-22.04
```

---

### **6. تعطيل التشفير المادي (إذا كان مطبقًا)**
بعض بطاقات إنتل لـ Wi-Fi لها مشاكل مع التشفير المادي.  
عدّل ملف `/etc/modprobe.d/iwlwifi.conf` (أنشئه إذا كان مفقودًا):
```plaintext
options iwlwifi 11n_disable=1
```
ثم:
```bash
sudo modprobe -r iwlwifi && sudo modprobe iwlwifi
```

---

### **7. التحقق من RFKill أو Wi-Fi المقيد**
```bash
rfkill list
```
إذا كان Wi-Fi مقيدًا (مثال: `soft blocked: yes`)، فقم بإلغاء تقييده:
```bash
sudo rfkill unblock wifi
```

---

### **8. الاختبار بمحول Wi-Fi USB**
إذا استمرت المشكلة، جرب **محول Wi-Fi USB متوافق مع لينكس** (مثل TP-Link Archer T4U) لعزل ما إذا كانت المشكلة في بطاقة إنتل.

---

### **9. التحقق من السجلات للبحث عن أخطاء**
```bash
journalctl -u NetworkManager --no-pager -n 50
 ```
ابحث عن أخطاء `iwlwifi` أو أحداث انقطاع.

---

### **ملاحظات نهائية**
- إذا لم تنجح أي من الحلول أعلاه، فكر في **التمهيد المزدوج مع ويندوز** للتحقق مما إذا كانت المشكلة متعلقة بالعتاد.
- بدلاً من ذلك، استخدم **محول USB-to-Ethernet** إذا ظل Wi-Fi غير مستقر.

أعلمني إذا كنت بحاجة إلى مزيد من التنقيح!
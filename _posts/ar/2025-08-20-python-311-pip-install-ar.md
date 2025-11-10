---
audio: false
generated: true
image: false
lang: ar
layout: post
title: تثبيت بايثون ٣٫١١ و بيب ٣٫١١
translated: true
type: note
---

يبدو أن لديك إصدارات متعددة من Python و pip مثبتة على نظام Ubuntu الخاص بك، وتريد تثبيت **Python 3.11** و **pip (pip3.11)** المقابل له. إليك الطريقة:

---

### **1. تثبيت Python 3.11**
أولاً، قم بتحديث قائمة الحزم وتثبيت Python 3.11:

```bash
sudo apt update
sudo apt install python3.11
```

تحقق من التثبيت:

```bash
python3.11 --version
```

---

### **2. تثبيت pip لـ Python 3.11**
قد لا تتضمن مستودعات Ubuntu الافتراضية `pip` لـ Python 3.11. يمكنك تثبيته باستخدام الخطوات التالية:

#### **الخيار أ: تثبيت pip عبر apt (إذا كان متاحًا)**
```bash
sudo apt install python3.11-venv python3.11-dev python3-pip
```
إذا قام `python3-pip` بتثبيت pip لإصدار مختلف، انتقل إلى **الخيار ب**.

#### **الخيار ب: تثبيت pip باستخدام ensurepip**
```bash
python3.11 -m ensurepip --upgrade
```
سيؤدي هذا إلى تثبيت pip خصيصًا لـ Python 3.11.

#### **الخيار ج: تثبيت pip باستخدام get-pip.py**
إذا لم تنجح الطرق أعلاه، استخدم سكريبت `get-pip.py` الرسمي:

```bash
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11
```

---

### **3. التحقق من تثبيت pip3.11**
تحقق مما إذا كان `pip3.11` متاحًا الآن:

```bash
pip3.11 --version
```
يجب أن ترى ناتجًا مشابهًا لما يلي:
```
pip 23.x.x from /usr/local/lib/python3.11/site-packages/pip (python 3.11)
```

---

### **4. (اختياري) إنشاء بيئة افتراضية**
لتجنب التعارض بين إصدارات Python، يمكنك إنشاء بيئة افتراضية:

```bash
python3.11 -m venv myenv
source myenv/bin/activate
```
الآن، سيستخدم `pip` داخل البيئة الافتراضية Python 3.11.

---

### **جدول الملخص**

| الأمر | الغرض |
|---------|---------|
| `sudo apt update` | تحديث قائمة الحزم |
| `sudo apt install python3.11` | تثبيت Python 3.11 |
| `python3.11 -m ensurepip --upgrade` | تثبيت pip لـ Python 3.11 |
| `pip3.11 --version` | التحقق من تثبيت pip |
| `python3.11 -m venv myenv` | إنشاء بيئة افتراضية |

---
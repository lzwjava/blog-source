---
audio: false
generated: true
image: false
lang: ar
layout: post
title: إصلاح مسار ملف تكوين ميكاب
translated: true
type: note
---

خطأك

```
RuntimeError: param.cpp(70) [ifs] no such file or directory: /usr/local/etc/mecabrc
```

يعني أن **MeCab لا يمكنه العثور على ملف التهيئة الخاص به** (`mecabrc`).
على نظام macOS، إذا قمت بتثبيت MeCab عبر Homebrew مؤخرًا، فمن المرجح أنه مثبت تحت المسار `/opt/homebrew/` بدلاً من `/usr/local/`، لكن ربط Python لا يزال يبحث عن المسار القديم `/usr/local/etc/mecabrc`.

إليك كيفية إصلاح ذلك:

---

### 1. ابحث عن مكان وجود `mecabrc` الفعلي

شغّل:

```bash
brew list mecab
```

أو:

```bash
find /opt/homebrew -name mecabrc
```

على الأرجح سترى شيئًا مثل:

```
/opt/homebrew/etc/mecabrc
```

---

### 2. وجّه MeCab إلى ملف mecabrc الصحيح

يمكنك تحديد المسار في كود Python الخاص بك:

```python
import MeCab

t = MeCab.Tagger(f"-r /opt/homebrew/etc/mecabrc -d /opt/homebrew/lib/mecab/dic/ipadic")
print(t.parse("すもももももももものうち"))
```

---

### 3. أو قم بتعيين متغير بيئة

```bash
export MECABRC=/opt/homebrew/etc/mecabrc
```

ثم شغّل السكريبت الخاص بك بشكل طبيعي:

```bash
python try_mecab.py
```

---

### 4. إذا كنت تريد جعل `/usr/local/etc/mecabrc` يعمل

يمكنك أيضًا إنشاء رابط رمزي:

```bash
sudo mkdir -p /usr/local/etc
sudo ln -s /opt/homebrew/etc/mecabrc /usr/local/etc/mecabrc
```

لكن نهج متغير البيئة أنظف.

---

إذا كنت تريد، يمكنني أيضًا إعطاؤك أمر **إعادة تثبيت Homebrew + إعداد ipadic** بحيث يعمل دون الحاجة إلى تحديد `-r` في كل مرة. بهذه الطريقة يبقى ملف `try_mecab.py` الخاص بك نظيفًا.
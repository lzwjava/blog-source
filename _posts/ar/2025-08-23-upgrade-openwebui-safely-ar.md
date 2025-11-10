---
audio: false
generated: true
image: false
lang: ar
layout: post
title: ترقية Open WebUI بأمان الآن
translated: true
type: note
---

فهمتك. إليك الطرق الآمنة والمباشرة لترقية Open WebUI.

## إذا قمت بالتثبيت باستخدام `pip` (كما في حالتك)

```bash
# 1) (مُوصى به) فعّل البيئة الافتراضية التي تستخدمها لـ Open WebUI
#    مثال على conda:
conda activate open-webui
#    أو venv:
# source ~/open-webui-venv/bin/activate

# 2) قم بالترقية إلى أحدث إصدار
python3.11 -m pip install -U open-webui

# 3) (اختياري) إذا تسبب ذاكرة التخزين المؤقت لـ pip في مشكلة
python3.11 -m pip cache purge
python3.11 -m pip install --no-cache-dir -U open-webui

# 4) تحقق من الإصدار المثبت
python3.11 -m pip show open-webui
```

الوثائق الرسمية تنص على أن تشغيل `pip install -U open-webui` فقط يقوم بالترقية إلى أحدث إصدار. ([Open WebUI][1])

### حافظ على استمرارية بياناتك/إعداداتك

عند تشغيل الخادم، يمكنك تثبيت دليل بيانات معين حتى لا تؤثر الترقيات عليه:

```bash
# نظام macOS/Linux
DATA_DIR="$HOME/.open-webui" open-webui serve
# نظام Windows (PowerShell)
$env:DATA_DIR="C:\open-webui\data"; open-webui serve
```

هذا يعكس توجيهات الوثائق لتعيين `DATA_DIR` (أو استخدام `uvx … @latest serve` مع نفس المتغير) بحيث تظل محادثاتك/إعداداتك خارج تثبيت الحزمة. ([Open WebUI][2])

> نصيحة: إذا كنت قد شغلت سابقًا بدون `DATA_DIR`، ابدأ في استخدامه الآن؛ سوف يستخدم Open WebUI هذا المجلد من الآن فصاعدًا.

## إذا استخدمت Docker (للاكتمال)

```bash
# أوقف وأزل الحاوية القديمة (البيانات موجودة في Volume المسمى)
docker rm -f open-webui

# احصل على أحدث صورة
docker pull ghcr.io/open-webui/open-webui:main

# ابدأ التشغيل مرة أخرى باستخدام Volume الحالي الخاص بك
docker run -d -p 3000:8080 \
  -v open-webui:/app/backend/data \
  --name open-webui \
  ghcr.io/open-webui/open-webui:main
```

هذا هو إجراء التحديث اليدوي الموصى به من قبل المشروع؛ تظل بياناتك محفوظة في Volume Docker المسمى `open-webui`. ([Open WebUI][3])

## تحقق من الإصدار "الأحدث"

يمكنك التأكد من أحدث إصدار (tag) من صفحة الإصدارات (Releases) على GitHub قبل/بعد الترقية. ([GitHub][4])

إذا واجهتك أي أخطاء (مثل عدم توافق إصدار Python)، تأكد من أنك تستخدم Python 3.11 لطريقة التثبيت بـ pip، وهو ما يوصى به المشروع صراحةً. ([GitHub][5])

هل تريد مني التحقق من بيئتك الحالية أو تفسير أي خطأ يظهر أثناء الترقية؟ الصقه هنا وسأقوم باستكشاف الأخطاء وإصلاحها.

[1]: https://docs.openwebui.com/getting-started/quick-start/?utm_source=chatgpt.com "️ Quick Start"
[2]: https://docs.openwebui.com/?utm_source=chatgpt.com "Open WebUI: Home"
[3]: https://docs.openwebui.com/getting-started/updating/?utm_source=chatgpt.com "Updating Open WebUI"
[4]: https://github.com/open-webui/open-webui/releases?utm_source=chatgpt.com "Releases · open-webui/open-webui"
[5]: https://github.com/open-webui/open-webui?utm_source=chatgpt.com "open-webui/open-webui: User-friendly AI Interface ..."
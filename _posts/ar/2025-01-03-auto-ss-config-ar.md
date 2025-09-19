---
audio: false
generated: false
image: false
lang: ar
layout: post
title: 'أداة مفتوحة المصدر: Auto SS Config'
translated: true
---

يسرني أن أعلن عن إتاحة أداة مفتوحة المصدر أسميتها **Auto SS Config**. هذه الأداة تقوم تلقائيًا بإنشاء وتحميل روابط الاشتراك الخاصة بـ Shadowsocks أو Clash من روابط Shadowsocks، مما يجعل إدارة وتحديث إعدادات خادم الوكيل أسهل.

هذه الأداة كانت بمثابة تغيير جذري بالنسبة لي، خاصة عندما يتم حظر خادم Shadowsocks الخاص بي. أستخدم Outline Manager لإنشاء خادم جديد، والحصول على عنوان جديد، واستيراد هذا الرابط مباشرة باستخدام تطبيق Mac لتجاوز قيود جدار الحماية العظيم. تشغيل الأمر `python upload_configs.py` من هذا المشروع يقوم بتحديث روابط الاشتراك الخاصة بي، مما يضمن أن جميع أجهزتي الرقمية تحافظ على اتصالات شبكية عاملة.

## الميزات

- **تحويل روابط Shadowsocks إلى تكوين Clash**: قم بالتبديل بسهولة بين تكوينات البروكسي المختلفة.
- **يدعم خوادم Shadowsocks متعددة**: إدارة عدة خوادم بسهولة.
- **تحميل التكوينات تلقائيًا إلى Google Cloud Storage**: حافظ على تكويناتك آمنة ويمكن الوصول إليها.
- **جعل التكوينات متاحة للعامة**: شارك تكويناتك مع الآخرين.
- **استخدام التحكم في الذاكرة المؤقتة للتحديثات الفورية**: تأكد من أن تكويناتك محدثة دائمًا.

## الملفات

- `app_config_tmp.yaml`: تكوين التطبيق (اسم الـ bucket، عناوين SS).
- `clash_config_tmp.yaml`: ملف تكوين Clash المؤقت.
- `upload_configs.py`: سكريبت لإنشاء تكوين Clash وتحميل التكوينات إلى Google Cloud Storage.
- `requirements.txt`: تبعيات Python.

## الإعداد

1. **تثبيت التبعيات**:
    ```bash
    pip install -r requirements.txt
    ```

2. **إعداد بيانات اعتماد Google Cloud**:
    - قم بتثبيت Google Cloud SDK.
    - نفّذ الأمر `gcloud auth application-default login`.
    - أو قم بتعيين متغير البيئة `GOOGLE_APPLICATION_CREDENTIALS`.

3. **انسخ `app_config_tmp.yaml` إلى `app_config.yaml` وقم بالتكوين**:
    ```yaml
    bucket_name: اسم-الدلو-الخاص-بك
    ss_urls:
        - ss://method:password@server:port
    ```

## الاستخدام

1. **أضف روابط Shadowsocks الخاصة بك إلى قائمة `ss_urls` في ملف `app_config.yaml`**:
    ```yaml
    ss_urls:
        - ss://method:password@server:port
    ```

2. **تحميل التكوينات**:
    ```bash
    python upload_configs.py
    ```

    سيقوم البرنامج النصي بإخراج عناوين URL العامة لكلا التكوينين.

## التطوير

- **Python 3.6+**
- يستخدم `ruamel.yaml` للتعامل مع ملفات YAML.
- يستخدم `google-cloud-storage` لإجراء العمليات على GCS.

## الرخصة

معهد ماساتشوستس للتكنولوجيا (MIT)

---

لا تتردد في الاطلاع على [المستودع](https://github.com/lzwjava/auto-ss-config) لمزيد من التفاصيل والمساهمة!
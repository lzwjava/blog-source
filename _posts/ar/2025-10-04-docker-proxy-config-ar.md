---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: تهيئة إعدادات الوكيل لبرنامج دوكر ديمون
translated: true
type: note
---

### تكوين Docker Daemon لإعدادات الوكيل

يمكن تكوين Docker daemon لاستخدام وكيل HTTP/HTTPS للعمليات مثل سحب الصور أو بناء الحاويات من خلف جدار حماية الشركة. يتم ذلك عن طريق تحرير (أو إنشاء) ملف `/etc/docker/daemon.json`. لاحظ أن هذا التكوين ينطبق على الـ daemon نفسه (مثل `docker pull` أو `docker build`)، وليس على الحاويات الفردية (والتي ستستخدم متغيرات البيئة أو Docker build args).

#### المتطلبات الأساسية
- تحتاج إلى صلاحيات root أو sudo على نظام Linux (هذا هو النظام الأساسي لتكوين Docker daemon؛ على Windows/Mac مع Docker Desktop، استخدم إعدادات واجهة المستخدم الرسومية بدلاً من ذلك).
- تثبيت Docker وجاري تشغيله.
- معرفة تفاصيل خادم الوكيل الخاص بك (مثل `http://proxy.company.com:8080` لوكيل HTTP/HTTPS، وأي استثناءات no-proxy).

#### التكوين خطوة بخطوة

1. **تحديد موقع أو إنشاء ملف تكوين Daemon**:
   - افتح طرفية وانتقل إلى `/etc/docker/` (أنشئ الدليل إذا لم يكن موجودًا: `sudo mkdir -p /etc/docker`).
   - حرر الملف `daemon.json` باستخدام محرر نصوص (مثل `sudo nano /etc/docker/daemon.json` أو `sudo vim /etc/docker/daemon.json`).
   - إذا كان الملف غير موجود، قم بإنشائه. ابدأ بكائن JSON فارغ `{}` إذا كان جديدًا.

2. **إضافة تكوين الوكيل**:
   - أضف قسم `"proxies"` إلى ملف JSON. إليك مثال أساسي:

     ```json
     {
       "proxies": {
         "http-proxy": "http://proxy.company.com:8080",
         "https-proxy": "http://proxy.company.com:8080",
         "no-proxy": "localhost,127.0.0.1,*.company.com,10.0.0.0/8"
       }
     }
     ```

     - **الشروحات**:
       - `"http-proxy"`: عنوان URL لوكيل HTTP (مطلوب لطلبات non-HTTPS).
       - `"https-proxy"`: عنوان URL لوكيل HTTPS (غالبًا ما يكون هو نفسه وكيل HTTP).
       - `"no-proxy"`: قائمة مفصولة بفواصل من المضيفين/النطاقات/نطاقات IP التي يجب أن تتجاوز الوكيل (مثل العناوين المحلية أو النطاقات الداخلية). هذا يمنع الحلقات اللانهائية.
       - إذا كانت المصادقة مطلوبة، استخدم التنسيق `http://username:password@proxy.company.com:8080`.
       - لوكيلات SOCKS، استخدم `"http-proxy": "socks5://proxy.company.com:1080"`.

     - إذا كان `daemon.json` يحتوي بالفعل على محتوى موجود (مثل إعدادات أخرى مثل `"log-driver": "json-file"`)، قم بدمج قسم `"proxies"` فيه دون تكرار المفاتيح. تأكد من صحة بناء جملة JSON (استخدم أداة مثل `jsonlint` للتحقق إذا لزم الأمر).

3. **حفظ وإعادة تشغيل Docker Daemon**:
   - احفظ الملف.
   - أعد تشغيل خدمة Docker لتطبيق التغييرات:
     ```
     sudo systemctl restart docker
     ```
     - على الأنظمة القديمة أو إعدادات non-systemd، استخدم `sudo service docker restart`.
   - تحقق من أن الـ daemon قيد التشغيل:
     ```
     sudo systemctl status docker
     ```
     - تحقق من السجلات إذا كانت هناك مشاكل: `sudo journalctl -u docker.service`.

4. **التحقق من التكوين**:
   - اختبر عن طريق سحب صورة (والتي يجب أن توجّه الآن عبر الوكيل الخاص بك):
     ```
     docker pull hello-world
     ```
   - تحقق مما إذا تم تطبيق إعدادات الوكيل عن طريق فحص تكوين الـ daemon:
     ```
     docker info | grep -i proxy
     ```
     - يجب أن ترى ناتجًا مشابهًا لما يلي:
       ```
       HTTP Proxy: http://proxy.company.com:8080
       HTTPS Proxy: http://proxy.company.com:8080
       No Proxy: localhost,127.0.0.1,*.company.com,10.0.0.0/8
       ```
   - إذا كنت تستخدم Docker في سياق بناء، اختبر باستخدام:
     ```
     docker build -t test-proxy .
     ```
     (بافتراض وجود Dockerfile بسيط يسحب صورة أساسية).

#### ملاحظات إضافية
- **الأمان**: تجنب ترميز بيانات الاعتماد في `daemon.json` على الأنظمة المشتركة. استخدم متغيرات البيئة إذا أمكن، أو أدوات مثل `docker config` للإعدادات الأكثر تقدمًا.
- **المشاكل الشائعة**:
  - **أخطاء بناء الجملة**: JSON غير الصالح سيمنع الـ daemon من البدء. راجع مرة أخرى باستخدام `cat /etc/docker/daemon.json` وأداة التحقق من صحة JSON.
  - **جدار الحماية/SELinux**: تأكد من إمكانية الوصول إلى الوكيل الخاص بك وأن وحدات الأمان لا تمنعه.
  - **إصدار Docker**: يعمل هذا على Docker 20.10+ (استخدمت الإصدارات السابقة متغيرات بيئة مختلفة مثل `HTTP_PROXY`). تحقق من إصدارك باستخدام `docker --version` وقم بالترقية إذا لزم الأمر.
  - **الوكيل الخاص بالسجل**: للسجلات الخاصة، قد تحتاج إلى تكوين إضافي تحت `"registry-mirrors"` أو السجلات غير الآمنة في `daemon.json`.
- **للحاويات**: إذا كنت بحاجة إلى إعدادات الوكيل *داخل* الحاويات قيد التشغيل (وليس الـ daemon)، فاضبط متغيرات البيئة في Dockerfile (مثل `ENV http_proxy=http://proxy.company.com:8080`) أو عبر `docker run -e http_proxy=...`.
- **Docker Desktop (Windows/Mac)**: انتقل إلى Settings > Resources > Proxies، وقم بتمكين/تكوين هناك — لا حاجة لتحرير JSON.

لمزيد من التفاصيل، راجع وثائق Docker الرسمية: [Configure the Docker daemon](https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-configuration-file). إذا واجهت أخطاء، شارك الناتج الدقيق لاستكشاف الأخطاء وإصلاحها!
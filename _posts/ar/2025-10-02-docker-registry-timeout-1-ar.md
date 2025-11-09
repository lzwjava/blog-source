---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast:free
title: استكشاف أخطاء انتهاء وقت اتصال سجل دوكر
translated: true
type: note
---

الخطأ الذي تواجهه، `Error response from daemon: Get "https://registry-1.docker.io/v2/": net/http: request canceled while waiting for connection (Client.Timeout exceeded while awaiting headers)`، يشير إلى فشل عميل Docker في الاتصال بسجل Docker Hub بسبب انتهاء مهلة الاتصال. قد يكون هذا ناتجًا عن مشاكل في الشبكة، أو مشاكل في المصادقة، أو أخطاء في التهيئة. نظرًا لأنك تحاول تسجيل دخول قائم على الويب، دعنا نتتبع المشكلة ونحلها خطوة بخطوة.

### خطوات لحل المشكلة

1. **التحقق من اتصال الشبكة**
   - تأكد من أن اتصالك بالإنترنت مستقر.
   - اختبر الاتصال بـ Docker Hub عن طريق تشغيل:
     ```bash:disable-run
     ping registry-1.docker.io
     ```
     أو
     ```bash
     curl -v https://registry-1.docker.io/v2/
     ```
     إذا فشلت هذه الأوامر، فقد تكون لديك مشكلة في الشبكة (مثل جدار الحماية، الوكيل، أو مشاكل DNS).

2. **التحقق من المصادقة القائمة على الويب**
   - تشير الرسالة إلى أنك تستخدم رمز تأكيد جهاز لمرة واحدة (`LVFK-KCQX`). تأكد من أنك:
     - ضغطت على `ENTER` لفتح المتصفح أو قمت بزيارة `https://login.docker.com/activate` يدويًا.
     - أدخلت الرمز بشكل صحيح في المتصفح.
     - أكملت عملية المصادقة في المتصفح خلال فترة المهلة.
   - إذا لم يفتح المتصفح تلقائيًا، قم بزيارة الرابط يدويًا وأدخل الرمز.
   - إذا فشلت المصادقة أو انتهت المهلة، حاول إعادة بدء العملية:
     ```bash
     docker login
     ```

3. **معالجة مشاكل انتهاء المهلة**
   - يشير خطأ انتهاء المهلة إلى أن عميل Docker لم يتمكن من الاتصال بالسجل. قم بزيادة المهلة عن طريق تعيين متغير البيئة `DOCKER_CLIENT_TIMEOUT`:
     ```bash
     export DOCKER_CLIENT_TIMEOUT=120
     export COMPOSE_HTTP_TIMEOUT=120
     docker login
     ```
     هذا يمدد المهلة إلى 120 ثانية.

4. **التحقق من مشاكل الوكيل أو جدار الحماية**
   - إذا كنت خلف وكيل، قم بتكوين Docker لاستخدامه. قم بتحرير أو إنشاء الملف `~/.docker/config.json` وأضف:
     ```json
     {
       "proxies": {
         "default": {
           "httpProxy": "http://<proxy-host>:<proxy-port>",
           "httpsProxy": "https://<proxy-host>:<proxy-port>",
           "noProxy": "localhost,127.0.0.1"
         }
       }
     }
     ```
     استبدل `<proxy-host>` و `<proxy-port>` بتفاصيل الوكيل الخاصة بك.
   - إذا كان جدار حماية يمنع الوصول، فتأكد من أن `registry-1.docker.io` و `login.docker.com` مسموح بهما.

5. **استخدام مساعد بيانات الاعتماد (اختياري ولكنه موصى به)**
   - يشير التحذير حول بيانات الاعتماد غير المشفرة في `~/.docker/config.json` إلى إعداد مساعد بيانات الاعتماد. قم بتثبيت مساعد بيانات اعتماد مثل `docker-credential-pass` أو `docker-credential-secretservice`:
     - لنظام Linux مع `pass`:
       ```bash
       sudo apt-get install pass
       curl -fsSL https://github.com/docker/docker-credential-helpers/releases/download/v0.7.0/docker-credential-pass-v0.7.0-amd64.tar.gz | tar -xz
       sudo mv docker-credential-pass /usr/local/bin/
       ```
       قم بتهيئة `pass`:
       ```bash
       gpg2 --gen-key
       pass init <your-gpg-key-id>
       ```
       قم بتحديث `~/.docker/config.json` لاستخدام المساعد:
       ```json
       {
         "credsStore": "pass"
       }
       ```
     - أعد محاولة تسجيل الدخول بعد تكوين مساعد بيانات الاعتماد.

6. **التراجع إلى تسجيل الدخول عبر سطر الأوامر**
   - إذا استمر فشل تسجيل الدخول القائم على الويب، جرب تسجيل الدخول عبر سطر الأوامر باستخدام اسم مستخدم Docker Hub وكلمة المرور:
     ```bash
     docker login -u <your-username>
     ```
     أدخل كلمة المرور أو رمز الوصول الشخصي (PAT) عندما يُطلب منك. يمكنك إنشاء PAT من إعدادات حساب Docker Hub الخاص بك.

7. **التحقق من حالة خادم Docker**
   - تأكد من أن خادم Docker قيد التشغيل:
     ```bash
     sudo systemctl status docker
     ```
     إذا لم يكن قيد التشغيل، ابدأه:
     ```bash
     sudo systemctl start docker
     ```

8. **مسح تهيئة Docker (حل أخير)**
   - إذا استمرت المشكلة، امسح ملف تهيئة Docker وأعد المحاولة:
     ```bash
     mv ~/.docker/config.json ~/.docker/config.json.bak
     docker login
     ```

### ملاحظات إضافية
- **حالة Docker Hub**: تحقق مما إذا كانت Docker Hub تواجه انقطاعات عن طريق زيارة `https://status.docker.com/`.
- **مشاكل DNS**: إذا لم يتم حل اسم `registry-1.docker.io`، فحاول استخدام DNS عام مثل Google (`8.8.8.8`) أو Cloudflare (`1.1.1.1`) في إعدادات الشبكة الخاصة بك.
- **إصدار Docker**: تأكد من أن عميل Docker محدث:
  ```bash
  docker --version
  ```
  قم بتحديث Docker إذا لزم الأمر، باتباع التعليمات الخاصة بنظام التشغيل الخاص بك.

### المراجع
- [Docker Credential Store Documentation](https://docs.docker.com/go/credential-store/)
- [Docker Login Documentation](https://docs.docker.com/engine/reference/commandline/login/)
- [Docker Hub Status](https://status.docker.com/)
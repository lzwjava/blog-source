---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast:free
title: تثبيت Docker Compose على أوبونتو
translated: true
type: note
---

بناءً على معلومات نظامك، أنت تستخدم **Ubuntu 24.04.2 LTS** على بنية **x86_64**. لتنزيل ثنائي **Docker Compose** المناسب لنظامك من إصدار GitHub المذكور (v2.39.4)، يجب عليك اختيار الثنائي المتوافق مع Linux على x86_64.

### التنزيل الموصى به
يجب أن تقوم بتنزيل ثنائي **docker-compose-linux-x86_64**، والذي لم يتم ذكره صراحةً في الملفات المرفقة المقدمة ولكنه مُفترض كملف ثنائي قياسي لأنظمة Linux x86_64 في إصدارات Docker Compose. ومع ذلك، من الملفات المرفقة المدرجة، أقرب مطابقة لنظامك هي:

- **docker-compose-linux-aarch64** **غير** مناسب لأنه مخصص لبنية ARM64 (aarch64)، بينما نظامك هو x86_64.
- الثنائيات الخاصة بـ **darwin** (مثل `docker-compose-darwin-x86_64`) مخصصة لنظام macOS، وليس Linux.
- خيارات كود المصدر (`Source code (zip)` أو `Source code (tar.gz)`) تتطلب تجميعًا يدويًا، وهو غير ضروري نظرًا لأن الملف الثنائي المترجم مسبقًا يكون متاحًا عادةً.

نظرًا لأن ثنائي **docker-compose-linux-x86_64** لم يُذكر صراحةً في الملفات المرفقة التي قدمتها ولكنه قياسي لإصدارات Docker Compose، فمن المحتمل أن تجده في القائمة الكاملة للملفات المرفقة على صفحة إصدار GitHub. إذا لم يكن متاحًا، يمكنك استخدام كود المصدر أو تثبيت Docker Compose عبر طريقة بديلة (مثل مدير الحزم أو pip).

### خطوات التنزيل والتثبيت
1.  **تأكيد الملف الثنائي**: قم بزيارة صفحة إصدار GitHub للإصدار v2.39.4 لتأكيد توفر `docker-compose-linux-x86_64`. عادةً ما تكون صفحة الإصدار موجودة على:
    [إصدار Docker Compore v2.39.4](https://github.com/docker/compose/releases/tag/v2.39.4)

2.  **تنزيل الملف الثنائي**:
    إذا كان `docker-compose-linux-x86_64` متاحًا، قم بتنزيله. على سبيل المثال:
    ```bash
    curl -L "https://github.com/docker/compose/releases/download/v2.39.4/docker-compose-linux-x86_64" -o docker-compose
    ```

3.  **التحقق من التنزيل**:
    استخدم checksum المقدم للتحقق من سلامة الملف الذي تم تنزيله. على سبيل المثال، إذا كان ملف `docker-compose-linux-x86_64.sha256` متاحًا:
    ```bash
    echo "<sha256> docker-compose" | sha256sum --check
    ```
    استبدل `<sha256>` بالـ hash المناسب من الملفات المرفقة للإصدار (على سبيل المثال، `df7ff3dd8080134b851e1e49265028697d27de71f9bdc187e3d833357b934f36` لملف `docker-compose-darwin-x86_64.sha256`، لكنك تحتاج إلى الـ hash المكافئ لنظام Linux).

4.  **تثبيت الملف الثنائي**:
    انقل الملف الثنائي إلى دليل ضمن PATH الخاص بك، مثل `/usr/local/bin`:
    ```bash
    chmod +x docker-compose
    sudo mv docker-compose /usr/local/bin/docker-compose
    ```

5.  **التحقق من التثبيت**:
    تحقق من الإصدار المثبت:
    ```bash
    docker-compose --version
    ```
    يجب أن يظهر الناتج `Docker Compose version v2.39.4`.

### طريقة تثبيت بديلة
إذا لم يكن ثنائي `docker-compose-linux-x86_64` متاحًا أو كنت تفضل طريقة أبسط، يمكنك تثبيت Docker Compose باستخدام مدير الحزم أو pip، نظرًا لأن نظامك يحتوي على Python 3.13.4 مثبتًا:

#### عبر مدير الحزم (موصى به لـ Ubuntu)
غالبًا ما يكون Docker Compose متاحًا في مستودعات Ubuntu أو المستودع الرسمي لـ Docker:
```bash
sudo apt update
sudo apt install docker-compose-plugin
```
يقوم هذا بتثبيت إضافة Docker Compose، وهي الطريقة الحديثة لاستخدام Docker Compose (كأمر `docker compose` بدلاً من `docker-compose`). لاحظ أن الإصدار الموجود في مستودع Ubuntu قد لا يكون بالضبط v2.39.4، لذا تحقق من خلال:
```bash
docker compose version
```

#### عبر pip (Python)
نظرًا لأن لديك Python 3.13.4، يمكنك تثبيت Docker Compose عبر pip:
```bash
pip3 install docker-compose==2.39.4
```
يقوم هذا بتثبيت الإصدار المحدد. تحقق من خلال:
```bash
docker-compose --version
```

### ملاحظات
- يمكن استخدام ملف `checksums.txt` (SHA256: `1a9c3370b88825ab2b229bb90eda6f703d84018ea1d56b5ba573f8893c9ab6b4`) للتحقق من سلامة الملفات التي تم تنزيلها.
- إذا اخترت التجميع من المصدر (`Source code (zip)` أو `Source code (tar.gz)`)، فستحتاج إلى Go (غير مذكور في معلومات نظامك) وإعدادات إضافية، وهو أكثر تعقيدًا ولا يُوصى به إلا إذا كان ضروريًا.
- يتضمن الإصدار تحسينات وإصلاحات (مثل دعم `develop.watch.initial_sync`، وأمر volume ls بدون project، و TLS لـ bake)، وهي ذات صلة إذا كنت تستخدم هذه الميزات.

إذا كنت بحاجة إلى مساعدة في العثور على ثنائي `docker-compose-linux-x86_64` المحدد أو واجهت مشاكل، فأعلمني، وسأرشدك أكثر!

[إصدار Docker Compose v2.39.4](https://github.com/docker/compose/releases/tag/v2.39.4)
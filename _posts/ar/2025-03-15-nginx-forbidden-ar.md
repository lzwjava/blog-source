---
audio: false
generated: true
lang: ar
layout: post
title: إصلاح خطأ نيجنكس 403 الممنوع
translated: true
type: note
---

لإصلاح خطأ "403 Forbidden" الذي تواجهه في تكوين Nginx الخاص بك، تحتاج إلى معالجة مشكلتين رئيسيتين: الاستخدام غير الصحيح لتوجيه `root` في كتلة `location` والمشاكل المحتملة في أذونات نظام الملفات. فيما يلي دليل خطوة بخطوة لحل المشكلة بناءً على التكوين الذي قدمته:

```nginx
server {
    listen 80;
    server_name localhost;
    location /movies {
        root /path/to/your/movie/folder;
        autoindex on; # Enables directory listing
    }
}
```

عند زيارة `http://localhost/movies`، تحصل على خطأ 403 Forbidden، مما يشير عادةً إلى أن Nginx لا يمكنه الوصول إلى الدليل المطلوب أو خدمته. إليك كيفية إصلاح ذلك:

---

### 1. تصحيح تكوين Nginx
كتلة `location /movies` الحالية تستخدم `root /path/to/your/movie/folder;`. في Nginx، يلحق توجيه `root` URI الطلب (مثل `/movies`) إلى المسار المحدد، مما يعني أن Nginx يحاول خدمة الملفات من `/path/to/your/movie/folder/movies`. إذا كان هذا الدليل غير موجود، فإن Nginx يُرجع خطأ 403.

لإصلاح هذا، يجب استخدام توجيه `alias` بدلاً من `root`. يقوم توجيه `alias` بتعيين URI `/movies/` مباشرة إلى `/path/to/your/movie/folder/` دون إلحاق URI، وهو على الأرجح السلوك الذي تقصده.

قم بتحديث التكوين الخاص بك على النحو التالي:

```nginx
server {
    listen 80;
    server_name localhost;
    location /movies/ {
        alias /path/to/your/movie/folder/;
        autoindex on; # Enables directory listing
    }
}
```

- **التغييرات الرئيسية:**
  - تغيير `root` إلى `alias`.
  - إضافة شرطة مائلة في النهاية إلى `location /movies/` و `alias /path/to/your/movie/folder/` لضمان التعامل الصحيح مع الدليل باستخدام `autoindex`.

- **تطبيق التغييرات:**
  بعد تحديث ملف التكوين (مثل `/etc/nginx/nginx.conf` أو ملف في `/etc/nginx/sites-enabled/`)، أعد تشغيل Nginx لتطبيق التغييرات:
  - على Linux: `sudo systemctl restart nginx`
  - على Windows: أوقف وأعد تشغيل خدمة Nginx يدويًا.

- **اختبار الرابط:**
  قم بزيارة `http://localhost/movies/` (لاحظ الشرطة المائلة في النهاية) لمعرفة ما إذا كانت قائمة الدليل تظهر.

---

### 2. التحقق من أذونات نظام الملفات
إذا كان تغيير التكوين وحده لا يحل خطأ 403، فقد تكون المشكلة متعلقة بأذونات نظام الملفات. يحتاج Nginx إلى صلاحية قراءة `/path/to/your/movie/folder/` ومحتوياته، ويعتمد هذا الوصول على المستخدم الذي يعمل تحته Nginx (شائعًا `nginx` أو `www-data`).

- **تحديد مستخدم Nginx:**
  تحقق من ملف تكوين Nginx الرئيسي (مثل `/etc/nginx/nginx.conf`) بحثًا عن توجيه `user`. قد يبدو كالتالي:
  ```nginx
  user nginx;
  ```
  إذا لم يتم تحديده، فقد يكون افتراضيًا إلى `www-data` أو مستخدم آخر اعتمادًا على نظامك.

- **التحقق من الأذونات:**
  قم بتشغيل الأمر التالي لفحص أذونات مجلد الأفلام الخاص بك:
  ```bash
  ls -l /path/to/your/movie/folder
  ```
  سيعرض هذا المالك، المجموعة، والأذونات (مثل `drwxr-xr-x`).

- **ضبط الأذونات إذا لزم الأمر:**
  تأكد من أن مستخدم Nginx لديه صلاحية قراءة (وصول تنفيذي للمجلدات). إليك خياران:
  - **الخيار 1: تغيير الملكية (موصى به):**
    عيّن مالك المجلد إلى مستخدم Nginx (مثل `nginx`):
    ```bash
    sudo chown -R nginx:nginx /path/to/your/movie/folder
    ```
    استبدل `nginx` بالمستخدم الفعلي إذا كان مختلفًا (مثل `www-data`).

  - **الخيار 2: جعله قابل للقراءة للجميع (أقل أمانًا):**
    إذا كنت لا تريد تغيير الملكية، اجعل المجلد قابل للقراءة من قبل الآخرين:
    ```bash
    sudo chmod -R o+r /path/to/your/movie/folder
    ```

- **تأكد من الوصول إلى الدليل:**
  يحتاج الدليل نفسه إلى أذونات تنفيذ (`x`) حتى يتمكن Nginx من الوصول إلى محتوياته:
  ```bash
  sudo chmod o+x /path/to/your/movie/folder
  ```

- **تحقق من المجلدات الأصل:**
  إذا كان `/path/to/your/movie/folder` داخل مجلد أصل مقيد (مثل `/home/user/`)، فتأكد من أن جميع المجلدات الأصل حتى الجذر تحتوي على أذونات تنفيذ لمستخدم Nginx:
  ```bash
  sudo chmod o+x /path /path/to /path/to/your /path/to/your/movie
  ```

---

### 3. التحقق من التكوين واستكشاف الأخطاء وإصلاحها
بعد إجراء هذه التغييرات، اختبر مرة أخرى بزيارة `http://localhost/movies/`. إذا استمر خطأ 403:

- **تحقق من سجل أخطاء Nginx:**
  راجع سجل الأخطاء للحصول على تفاصيل محددة (يوجد عادةً في `/var/log/nginx/error.log`):
  ```bash
  sudo tail -f /var/log/nginx/error.log
  ```
  ابحث عن رسائل مثل "permission denied" أو "directory index is forbidden" لتحديد المشكلة بدقة.

- **اعتبارات إضافية:**
  - **SELinux (إذا كان مطبقًا):** على أنظمة مثل CentOS مع تمكين SELinux، قد يمنع الوصول. عيّن وضع SELinux مؤقتًا إلى الوضع المسموح به للاختبار:
    ```bash
    sudo setenforce 0
    ```
    إذا كان هذا يحل المشكلة، فستحتاج إلى ضبط سياسات SELinux (مثل استخدام `chcon` أو `audit2allow`).
  - **جدار الحماية:** تأكد من أن المنفذ 80 مفتوح إذا كنت تصل من جهاز آخر (على الرغم من أنه من غير المحتمل إذا كنت تختبر محليًا عبر `localhost`).

---

### التكوين النهائي
إليك التكوين المصحح والكامل:

```nginx
server {
    listen 80;
    server_name localhost;
    location /movies/ {
        alias /path/to/your/movie/folder/;
        autoindex on; # Enables directory listing
    }
}
```

- استبدل `/path/to/your/movie/folder/` بالمسار المطلق الفعلي لمجلد الأفلام الخاص بك.
- أعد تشغيل Nginx: `sudo systemctl restart nginx`.
- قم بزيارة `http://localhost/movies/` لتأكيد عمل قائمة الدليل.

من خلال تصحيح توجيه `alias` وضمان أذونات الملفات المناسبة، يجب حل خطأ 403 Forbidden، مما يسمح لك بالوصول إلى مجلد الأفلام الخاص بك عبر Nginx بنجاح.

---

لإصلاح خطأ Nginx 403 Forbidden الخاص بك والتأكد من إمكانية الوصول إلى ملف `.mkv` الفردي الخاص بك، دعنا ننشئ الإعداد بناءً على حالتك. لديك ملف `.mkv` واحد، وتريد معرفة مكان حفظه حتى يتمكن مستخدم Nginx من الوصول إليه. أدناه، سأرشدك خلال العملية خطوة بخطوة، بما في ذلك اختيار دليل مناسب وتكوين Nginx.

### الخطوة 1: اختر دليلًا لملف `.mkv` الخاص بك
عند تحديد مكان تخزين ملف `.mkv` الخاص بك ليقوم Nginx بخدمته، ضع في اعتبارك هذه العوامل:
- **إمكانية الوصول**: يحتاج مستخدم Nginx (مثل `nginx` أو `www-data`) إلى صلاحية قراءة.
- **الاتفاقيات**: عادة ما تخدم خوادم الويب الملفات من أدلة قياسية مثل `/var/www/` أو `/srv/www/`.
- **الأمان**: تجنب وضع الملفات في مواقع مفرطة في الصلاحيات أو حساسة (مثل `/home/user/` ما لم يكن ضروريًا).

في حالتك، نظرًا لأنه ملف `.mkv` واحد فقط وأنك تختبر محليًا (`localhost`)، أوصي باستخدام `/var/www/html/movies/` كموقع بسيط وقياسي. إليك السبب:
- `/var/www/html/` هو جذر ويب افتراضي شائع لـ Nginx و Apache.
- عادة ما يكون مملوكًا لمستخدم أو مجموعة خادم الويب، مما يجعل إدارة الأذونات أسهل.
- إضافة مجلد فرعي `/movies/` يحافظ على تنظيم الأشياء.

إذا كان `/var/www/html/` غير موجود أو غير مناسب على نظامك، فإن البدائل تشمل:
- `/srv/www/movies/` (دليل ويب قياسي آخر).
- `/usr/share/nginx/html/movies/` (أحيانًا يكون جذر مستندات Nginx الافتراضي).

في هذا المثال، دعنا نستخدم `/var/www/html/movies/`.

### الخطوة 2: إعداد الدليل والملف
بافتراض أنك على نظام Linux، اتبع هذه الخطوات:

1. **إنشاء الدليل**:
   ```bash
   sudo mkdir -p /var/www/html/movies
   ```

2. **انقل ملف `.mkv` الخاص بك**:
   استبدل `yourfile.mkv` بالاسم الفعلي لملفك وانقله إلى الدليل:
   ```bash
   sudo mv /path/to/yourfile.mkv /var/www/html/movies/yourfile.mkv
   ```

3. **تعيين الأذونات**:
   يحتاج مستخدم Nginx (شائعًا `nginx` أو `www-data`) إلى صلاحية قراءة للملف وصلاحية تنفيذ للدليل. أولاً، حدد مستخدم Nginx عن طريق التحقق من `/etc/nginx/nginx.conf`:
   ```bash
   grep user /etc/nginx/nginx.conf
   ```
   ابحث عن سطر مثل `user nginx;` أو `user www-data;`. إذا لم يتم تحديده، فقد يكون افتراضيًا إلى `www-data` (Ubuntu/Debian) أو `nginx` (CentOS/RHEL).

   ثم، اضبط الملكية:
   ```bash
   sudo chown -R nginx:nginx /var/www/html/movies
   ```
   استبدل `nginx` بـ `www-data` أو المستخدم الفعلي إذا كان مختلفًا.

   تأكد من الأذونات المناسبة:
   ```bash
   sudo chmod -R 755 /var/www/html/movies
   ```
   - `755` تعني أن المالك (Nginx) لديه وصول كامل، والآخرون (بما في ذلك عملية خادم الويب) يمكنهم القراءة والتنفيذ (التنقل) في الدليل.

### الخطوة 3: تكوين Nginx
قم بتحديث تكوين Nginx لخدمة ملف `.mkv` من `/var/www/html/movies/`. إليك تكوينًا أدنى يعمل:

```nginx
server {
    listen 80;
    server_name localhost;

    location /movies/ {
        alias /var/www/html/movies/;
        autoindex on; # Enables directory listing if you want to browse files
    }
}
```

- **ملاحظات**:
  - استخدم `alias` بدلاً من `root` لتعيين `/movies/` مباشرة إلى `/var/www/html/movies/`.
  - `autoindex on;` اختياري. إذا قمت بتعطيله (`autoindex off;`)، فستحتاج إلى تحديد رابط الملف المحدد (مثل `http://localhost/movies/yourfile.mkv`) للوصول إليه.

احفظ هذا التكوين (مثل في `/etc/nginx/sites-enabled/default` أو ملف مخصص مثل `/etc/nginx/conf.d/movies.conf`)، ثم اختبر وأعد تشغيل Nginx:
```bash
sudo nginx -t  # Test config for syntax errors
sudo systemctl restart nginx  # Apply changes
```

### الخطوة 4: اختبار الوصول
- افتح متصفحك وقم بزيارة:
  - `http://localhost/movies/` (إذا كان `autoindex` قيد التشغيل، سترى قائمة دليل تحتوي على `yourfile.mkv`).
  - `http://localhost/movies/yourfile.mkv` (للوصول مباشرة إلى الملف).
- إذا عمل، فيجب إما أن يعرض الملف في المتصفح (إذا كان مدعومًا) أو يطلب التنزيل.

### الخطوة 5: استكشاف الأخطاء وإصلاحها إذا لزم الأمر
إذا كنت لا تزال تحصل على خطأ 403:
1. **تحقق من الأذونات**:
   ```bash
   ls -l /var/www/html/movies/
   ```
   تأكد من أن `yourfile.mkv` قابل للقراءة (مثل `-rwxr-xr-x` أو على الأقل `-rw-r--r--`).

2. **تحقق من سجلات Nginx**:
   ```bash
   sudo tail -f /var/log/nginx/error.log
   ```
   ابحث عن أدلة مثل "permission denied."

3. **SELinux (إذا كان مطبقًا)**:
   إذا كنت على نظام مع SELinux (مثل CentOS)، قم بتشغيل:
   ```bash
   sudo setenforce 0  # Temporarily disable
   ```
   اختبر مرة أخرى. إذا عمل، فستحتاج إلى ضبط سياقات SELinux:
   ```bash
   sudo chcon -R -t httpd_sys_content_t /var/www/html/movies/
   sudo setenforce 1  # Re-enable SELinux
   ```

### الأفكار النهائية
من خلال حفظ ملف `.mkv` الخاص بك في `/var/www/html/movies/`، وتعيين الأذونات الصحيحة، واستخدام توجيه `alias` في Nginx، يجب أن تحل خطأ 403. هذا الإعداد بسيط ويتبع اتفاقيات خادم الويب، مما يسهل على مستخدم Nginx الوصول إلى الملف. دعني أعرف إذا واجهت أي عقبات!

---

إذا حصلت على خطأ "invalid user" مع `sudo chown -R nginx:nginx /var/www/movies`، فهذا يعني أن مستخدم `nginx` غير موجود على نظامك. يحدث هذا لأن عملية Nginx قد تعمل تحت مستخدم مختلف، مثل `www-data` (شائع على Debian/Ubuntu) أو افتراضي آخر اعتمادًا على نظام التشغيل الخاص بك.

### الإصلاح: تحديد واستخدام المستخدم الصحيح
1. **تحقق من مستخدم Nginx**:
   ابحث في ملف تكوين Nginx الخاص بك (عادة `/etc/nginx/nginx.conf`):
   ```bash
   grep user /etc/nginx/nginx.conf
   ```
   - إذا قال `user www-data;`، فاستخدم `www-data`.
   - إذا قال `user nginx;`، فيجب أن يكون مستخدم `nginx` موجودًا (قد يشير إلى تكوين خاطئ).
   - إذا لم يتم العثور على توجيه `user`، فإن المستخدم الافتراضي يعتمد على نظامك:
     - Ubuntu/Debian: `www-data`
     - CentOS/RHEL: `nginx`
     - أخرى: يمكن أن يكون `http`، `apache`، أو ما شابه.

2. **بديل: التحقق من العملية قيد التشغيل**:
   إذا لم يكن التكوين واضحًا، فانظر ما هو المستخدم الذي يعمل تحته Nginx:
   ```bash
   ps aux | grep nginx
   ```
   ابحث في العمود الأول (مثل `www-data` أو `nginx`) لعمليات العامل.

3. **تطبيق المستخدم الصحيح**:
   بافتراض أنه `www-data` (شائع على Ubuntu/Debian)، قم بتحديث الأمر:
   ```bash
   sudo chown -R www-data:www-data /var/www/movies
   ```
   إذا كان مستخدمًا مختلفًا (مثل `http`)، فاستخدم:
   ```bash
   sudo chown -R http:http /var/www/movies
   ```

4. **تعيين الأذونات**:
   بعد إصلاح الملكية، تأكد من الأذونات المناسبة:
   ```bash
   sudo chmod -R 755 /var/www/movies
   ```

5. **أعد التشغيل واختبر**:
   ```bash
   sudo systemctl restart nginx
   ```
   قم بزيارة `http://localhost/movies/yourfile.mkv`.

### إذا كنت لا تزال عالقًا
إذا لم يعمل `nginx` ولا `www-data` ولم يساعد فحص العملية، فأخبرني بنظام التشغيل الخاص بك (مثل Ubuntu، CentOS) أو ناتج `ps aux | grep nginx`، وسأحدد لك المستخدم المحدد!

---

إذا كان `autoindex on;` مضبوطًا ولكن `http://localhost/movies/` لا يزال لا يعرض قائمة الملفات، دعنا نستكشف الأخطاء ونصلحها خطوة بخطوة. نظرًا لأنك لا ترى قائمة الدليل، فقد تكون مشكلة في التكوين، أو مشكلة في الأذونات، أو شيء آخر يحجبها. إليك كيفية حلها:

### 1. التحقق من التكوين الخاص بك
تأكد من أن تكوين Nginx الخاص بك صحيح ومطبق. يجب أن يبدو كالتالي:

```nginx
server {
    listen 80;
    server_name localhost;

    location /movies/ {
        alias /var/www/movies/;
        autoindex on;
    }
}
```

- **الأخطاء الشائعة**:
  - خطأ مطبعي في مسار `alias` (مثل `/var/www/movie/` بدلاً من `/var/www/movies/`).
  - `autoindex on;` في الكتلة الخطأ أو معلقة.
  - ملف التكوين غير محمل (مثل محفوظ في المكان الخطأ).

تحقق من مكان التكوين الخاص بك:
- إذا كان في `/etc/nginx/sites-enabled/`، فتأكد من أنه مرتبط بشكل صحيح (مثل `ls -l /etc/nginx/sites-enabled/`).
- إذا كان في `/etc/nginx/conf.d/`، فتأكد من أنه ينتهي بـ `.conf` (مثل `movies.conf`).

اختبر وأعد التحميل:
```bash
sudo nginx -t
sudo systemctl reload nginx  # Reload instead of restart to avoid downtime
```

### 2. تأكد من وجود الملفات
تحقق من أن `/var/www/movies/` يحتوي على ملف `.mkv` الخاص بك:
```bash
ls -l /var/www/movies/
```
- إذا كان فارغًا، انقل ملفك هناك:
  ```bash
  sudo mv /path/to/yourfile.mkv /var/www/movies/
  ```
- إذا لم يكن فارغًا، لاحظ أسماء الملفات للاختبار.

### 3. تحقق من الأذونات
يحتاج Nginx إلى صلاحية قراءة (`r`) وتنفيذ (`x`) للوصول إلى الدليل والملفات. تحقق:
```bash
ls -ld /var/www/movies/
ls -l /var/www/movies/
```
- يجب أن يبدو الناتج كالتالي:
  ```
  drwxr-xr-x 2 www-data www-data 4096 Mar 15 14:00 /var/www/movies/
  -rw-r--r-- 1 www-data www-data 123456 Mar 15 14:00 yourfile.mkv
  ```
- أصلح إذا لزم الأمر (استبدل `www-data` بمستخدم Nginx الخاص بك):
  ```bash
  sudo chown -R www-data:www-data /var/www/movies/
  sudo chmod -R 755 /var/www/movies/
  ```

### 4. تحقق من السجلات
ابحث في سجل أخطاء Nginx عن أدلة:
```bash
sudo tail -n 20 /var/log/nginx/error.log
```
- **"permission denied"**: يشير إلى مشكلة في الأذونات — راجع الخطوة 3 مرة أخرى.
- **"directory index forbidden"**: يشير إلى أن `autoindex` لا يعمل — راجع التكوين مرة أخرى.
- لا توجد أخطاء ذات صلة: قد يعني أن Nginx لا يصل إلى كتلة الموقع الصحيحة.

### 5. اختبار الوصول المباشر
جرب الوصول إلى ملف محدد:
- قم بزيارة `http://localhost/movies/yourfile.mkv`.
- إذا عمل ولكن `/movies/` لم يعمل، فإن `autoindex` أو إعداد الدليل هو المشكلة.

### 6. الإصلاحات الشائعة
- **الشرطة المائلة في النهاية**: تأكد من أن `alias` ينتهي بـ `/` (`/var/www/movies/`)، واختبر كلًا من `http://localhost/movies` و `http://localhost/movies/`.
- **SELinux (إذا كان على CentOS/RHEL)**:
  ```bash
  sudo setenforce 0  # Temporarily disable
  ```
  اختبر مرة أخرى. إذا عمل، طبق:
  ```bash
  sudo chcon -R -t httpd_sys_content_t /var/www/movies/
  sudo setenforce 1
  ```
- **كتل موقع متضاربة**: إذا كانت كتلة `location` أخرى (مثل `location /`) تتجاوز `/movies/`، فانقل هذه الكتلة أعلى في التكوين أو اجعلها أكثر تحديدًا.

### 7. تكوين اختبار أدنى
إذا كان لا يزال لا يعمل، فبسّط لعزل المشكلة. استبدل التكوين الخاص بك بـ:

```nginx
server {
    listen 80;
    server_name localhost;

    location /movies/ {
        alias /var/www/movies/;
        autoindex on;
    }
}
```

احفظ، اختبر، وأعد التحميل:
```bash
sudo nginx -t
sudo systemctl reload nginx
```

### ما الذي يحدث؟
أخبرني:
- ماذا ترى في `http://localhost/movies/` (مثل 403، 404، صفحة فارغة)؟
- أي أخطاء في `sudo tail -n 20 /var/log/nginx/error.log`؟
- ناتج `ls -l /var/www/movies/`؟

مع ذلك، يمكنني تحديد المشكلة بالضبط وجعل قائمة الدليل تعمل!
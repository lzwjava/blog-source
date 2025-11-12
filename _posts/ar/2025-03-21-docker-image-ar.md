---
audio: false
generated: true
lang: ar
layout: post
title: بناء ونشر صورة دوكر
translated: true
type: note
---

إليك دليلًا خطوة بخطوة لبناء تطبيق Spring Boot إلى صورة Docker ونشره على خادم:

### المتطلبات الأساسية
1. تثبيت **Java** (مثل JDK 17 أو إصدار متوافق) محليًا.
2. **Maven** أو **Gradle** (اعتمادًا على إعداد مشروع Spring Boot الخاص بك).
3. تثبيت **Docker** على جهازك المحلي وعلى الخادم.
4. **مشروع Spring Boot** جاهز للتعبئة في حاوية.
5. **وصول إلى الخادم** (عبر SSH مثلًا) مع تثبيت Docker عليه.

---

### الخطوة 1: جهز تطبيق Spring Boot الخاص بك
تأكد من أن تطبيق Spring Boot يعمل محليًا. اختبره باستخدام:
```bash
mvn spring-boot:run  # إذا كنت تستخدم Maven
# أو
gradle bootRun       # إذا كنت تستخدم Gradle
```

تأكد من أن التطبيق يبني بنجاح:
```bash
mvn clean package    # Maven
# أو
gradle build         # Gradle
```
هذا يولد ملف `.jar` (مثل `target/myapp-1.0.0.jar`).

---

### الخطوة 2: أنشئ Dockerfile
في الدليل الجذري لمشروعك (حيث يوجد ملف `.jar`)، أنشئ ملفًا باسم `Dockerfile` بالمحتوى التالي:

```dockerfile
# استخدم صورة OpenJDK رسمية كصورة أساسية
FROM openjdk:17-jdk-slim

# عيّن دليل العمل داخل الحاوية
WORKDIR /app

# انسخ ملف JAR الخاص بتطبيق Spring Boot إلى الحاوية
COPY target/myapp-1.0.0.jar app.jar

# عرّض المنفذ الذي يعمل عليه تطبيق Spring Boot (الافتراضي هو 8080)
EXPOSE 8080

# شغّل ملف JAR
ENTRYPOINT ["java", "-jar", "app.jar"]
```

**ملاحظات:**
- استبدل `myapp-1.0.0.jar` بالاسم الفعلي لملف JAR الخاص بك.
- اضبط إصدار Java (`openjdk:17-jdk-slim`) إذا كان تطبيقك يستخدم إصدارًا مختلفًا.

---

### الخطوة 3: ابنِ صورة Docker
من الدليل الذي يحتوي على `Dockerfile`، شغّل:
```bash
docker build -t myapp:latest .
```
- `-t myapp:latest` يوسم الصورة كـ `myapp` بالإصدار `latest`.
- النقطة `.` تخبر Docker باستخدام الدليل الحالي كسياق للبناء.

تحقق من إنشاء الصورة:
```bash
docker images
```

---

### الخطوة 4: اختبر صورة Docker محليًا
شغّل الحاوية محليًا للتأكد من عملها:
```bash
docker run -p 8080:8080 myapp:latest
```
- `-p 8080:8080` يعين المنفذ 8080 على جهازك إلى المنفذ 8080 داخل الحاوية.
- افتح متصفحًا أو استخدم `curl` للاختبار (مثل `curl http://localhost:8080`).

أوقف الحاوية بـ `Ctrl+C` أو ابحث عن معرفها باستخدام `docker ps` وأوقفها:
```bash
docker stop <container-id>
```

---

### الخطوة 5: ادفع الصورة إلى سجل Docker (اختياري)
لنشر التطبيق على خادم، ستحتاج إلى دفع الصورة إلى سجل مثل Docker Hub (أو سجل خاص). إذا تخطيت هذه الخطوة، ستنقل الصورة يدويًا.

1. سجّل الدخول إلى Docker Hub:
   ```bash
   docker login
   ```
2. وسم صورتك:
   ```bash
   docker tag myapp:latest yourusername/myapp:latest
   ```
3. ادفع الصورة:
   ```bash
   docker push yourusername/myapp:latest
   ```

---

### الخطوة 6: انشر على الخادم
#### الخيار 1: استخدام سجل
1. اتصل بالخادم عبر SSH:
   ```bash
   ssh user@server-ip
   ```
2. اسحب الصورة:
   ```bash
   docker pull yourusername/myapp:latest
   ```
3. شغّل الحاوية:
   ```bash
   docker run -d -p 8080:8080 yourusername/myapp:latest
   ```
   - `-d` يشغّل الحاوية في الوضع المنفصل (في الخلفية).

#### الخيار 2: النقل اليدوي
إذا لم تستخدم سجلًا:
1. احفظ الصورة محليًا كملف `.tar`:
   ```bash
   docker save -o myapp.tar myapp:latest
   ```
2. انقلها إلى الخادم (عبر SCP مثلًا):
   ```bash
   scp myapp.tar user@server-ip:/path/to/destination
   ```
3. اتصل بالخادم عبر SSH:
   ```bash
   ssh user@server-ip
   ```
4. حمّل الصورة:
   ```bash
   docker load -i myapp.tar
   ```
5. شغّل الحاوية:
   ```bash
   docker run -d -p 8080:8080 myapp:latest
   ```

---

### الخطوة 7: تحقق من النشر
تحقق مما إذا كانت الحاوية تعمل:
```bash
docker ps
```

اختبر التطبيق من الخادم أو خارجيًا:
- إذا كنت على الخادم: `curl http://localhost:8080`
- إذا كان خارجيًا: استخدم IP الخادم (مثل `http://server-ip:8080`)، مع التأكد من أن المنفذ مفتوح في جدار حماية الخادم.

---

### اختياري: تحسينات
- **متغيرات البيئة**: مرّر إعدادات التهيئة لتطبيقك:
  ```bash
  docker run -d -p 8080:8080 -e "SPRING_PROFILES_ACTIVE=prod" myapp:latest
  ```
- **Docker Compose**: للإعدادات متعددة الحاويات، استخدم ملف `docker-compose.yml`.
- **سياسة إعادة التشغيل**: أضف `--restart unless-stopped` لضمان إعادة تشغيل الحاوية عند إعادة تشغيل الخادم.

أعلمني إذا كنت بحاجة إلى مساعدة في أي جزء محدد!

---

من ناتج الخطأ الذي قدمته، هناك بعض المشكلات التي تمنع أمر `docker build` من النجاح. دعنا نحللها ونصلحها خطوة بخطوة.

---

### المشكلات التي تم تحديدها
1. **إضافة `docker-buildx` مفقودة**
   الخطأ: `fork/exec /Users/lzwjava/.docker/cli-plugins/docker-buildx: no such file or directory`
   هذا يشير إلى أن Docker يحاول استخدام إضافة `buildx` (أداة بناء حديثة)، لكنها غير مثبتة أو غير مهيئة بشكل صحيح.

2. **تحذير إهالة أداة البناء القديمة**
   تحذير: `DEPRECATED: The legacy builder is deprecated...`
   Docker يوصي بالتبديل إلى BuildKit (`buildx`)، لكنه يعود إلى أداة البناء القديمة، والتي تفشل.

3. **خادم Docker لا يعمل**
   الخطأ: `Cannot connect to the Docker daemon at unix:///Users/lzwjava/.docker/run/docker.sock. Is the docker daemon running?`
   خادم Docker (الخدمة الخلفية التي تدير الحاويات) لا يعمل على نظامك.

4. **أخطاء الوصول إلى الملفات**
   أخطاء: `Can't add file ... to tar: io: read/write on closed pipe` و `Can't close tar writer...`
   هذه مشكلات ثانوية ناتجة عن فشل عملية البناء بسبب عدم تشغيل الخادم.

5. **تم اكتشاف إعدادات الوكيل**
   نظامك يستخدم وكلاء (`HTTP_PROXY` و `HTTPS_PROXY`). قد يتداخل هذا مع Docker إذا لم يتم تكوينه بشكل صحيح.

---

### الإصلاح خطوة بخطوة

#### 1. تحقق من أن خادم Docker يعمل
المشكلة الأساسية هي أن خادم Docker لا يعمل. إليك كيفية إصلاح ذلك:

- **على macOS** (بافتراض أنك تستخدم Docker Desktop):
  1. افتح Docker Desktop من مجلد التطبيقات أو Spotlight.
  2. تأكد من أنه يعمل (سترى أيقونة حوت Docker في شريط القوائم تتحول إلى اللون الأخضر).
  3. إذا لم يبدأ:
     - أغلق Docker Desktop وأعِد تشغيله.
     - تحقق من وجود تحديثات: Docker Desktop > Check for Updates.
     - إذا استمر الفشل، أعد تثبيت Docker Desktop من [docker.com](https://www.docker.com/products/docker-desktop/).

- **التحقق عبر Terminal**:
  شغّل:
  ```bash
  docker info
  ```
  إذا كان الخادم يعمل، سترى معلومات النظام. إذا لم يكن، ستحصل على نفس خطأ "Cannot connect".

- **أعِد تشغيل الخادم يدويًا** (إذا لزم الأمر):
  ```bash
  sudo launchctl stop com.docker.docker
  sudo launchctl start com.docker.docker
  ```

بمجرد أن يعمل الخادم، انتقل إلى الخطوات التالية.

---

#### 2. ثبّت إضافة `buildx` (اختياري لكن موصى به)
بما أن أداة البناء القديمة مهملة، فلنقم بإعداد `buildx`:

1. **ثبّت `buildx`**:
   - نزّل الملف الثنائي يدويًا أو استخدم تعليمات Docker:
     ```bash
     mkdir -p ~/.docker/cli-plugins
     curl -SL https://github.com/docker/buildx/releases/download/v0.13.0/buildx-v0.13.0.darwin-amd64 -o ~/.docker/cli-plugins/docker-buildx
     chmod +x ~/.docker/cli-plugins/docker-buildx
     ```
     (تحقق من [أحدث إصدار](https://github.com/docker/buildx/releases) لنظامك/معماريتك، مثل `darwin-arm64` لأجهزة Mac ذات M1/M2.)

2. **تحقق من التثبيت**:
   ```bash
   docker buildx version
   ```

3. **عيّن BuildKit كافتراضي** (اختياري):
   أضف هذا إلى `~/.docker/config.json`:
   ```json
   {
     "features": { "buildkit": true }
   }
   ```

بدلاً من ذلك، يمكنك تخطي هذا واستخدام أداة البناء القديمة حاليًا (انظر الخطوة 4).

---

#### 3. تعامل مع إعدادات الوكيل
إعدادات الوكيل الخاصة بك (`http://127.0.0.1:7890`) قد تتعارض مع قدرة Docker على جلب الصور. صمم Docker لاستخدامها:

1. **عبر Docker Desktop**:
   - افتح Docker Desktop > Settings > Resources > Proxies.
   - فعّل "Manual proxy configuration" وأدخل:
     - HTTP Proxy: `http://127.0.0.1:7890`
     - HTTPS Proxy: `http://127.0.0.1:7890`
   - طبّق وأعِد التشغيل.

2. **عبر CLI** (إذا لم تكن تستخدم Desktop):
   أنشئ أو حرّر `~/.docker/config.json`:
   ```json
   {
     "proxies": {
       "default": {
         "httpProxy": "http://127.0.0.1:7890",
         "httpsProxy": "http://127.0.0.1:7890"
       }
     }
   }
   ```
   أعِد تشغيل Docker بعد التحرير.

---

#### 4. أعِد محاولة البناء
الآن بعد أن أصبح الخادم يعمل وتم تكوين الوكلاء، حاول البناء مرة أخرى:

```bash
docker build -t myapp:latest .
```

- إذا ثبّتت `buildx`، فسيستخدم BuildKit افتراضيًا.
- إذا تخطيت `buildx`، أضف `--progress=plain` لإجبار أداة البناء القديمة:
  ```bash
  docker build --progress=plain -t myapp:latest .
  ```

---

#### 5. استكشاف أخطاء خطأ `.git/hooks` وإصلاحها (إذا استمر)
يشير خطأ `.git/hooks/pre-rebase.sample` إلى أن Docker يحاول تضمين ملفات غير ضرورية في سياق البناء. استبعدها باستخدام ملف `.dockerignore`:

1. أنشئ `.dockerignore` في نفس دليل `Dockerfile` الخاص بك:
   ```
   .git
   .gitignore
   *.md
   target/*
   !target/*.jar
   ```
2. هذا يخبر Docker بتجاهل مجلد `.git` وكل شيء في `target/` باستثناء ملف JAR الخاص بك.

3. أعِد محاولة البناء:
   ```bash
   docker build -t myapp:latest .
   ```

---

### التحقق النهائي
- تحقق من الصورة:
  ```bash
  docker images
  ```
- شغّلها محليًا:
  ```bash
  docker run -p 8080:8080 myapp:latest
  ```
- اختبر باستخدام `curl http://localhost:8080`.

---

### الخطوات التالية
بمجرد بناء الصورة بنجاح، اتبع خطوات النشر من ردّي السابق (مثل دفعها إلى سجل أو نقلها إلى خادم). أعلمني إذا واجهت أي مشكلات أخرى!
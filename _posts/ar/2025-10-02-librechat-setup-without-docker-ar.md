---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast:free
title: إعداد LibreChat بدون Docker Compose
translated: true
type: note
---

نعم، يمكنك إعداد LibreChat بدون Docker Compose باستخدام أوامر `docker run` الفردية أو حتى بطريقة غير Docker (التثبيت اليدوي باستخدام Node.js و Yarn و MongoDB و MeiliSearch). هذا يتجنب تنزيل ثنائي `docker-compose` نفسه (وهو صغير، ~20-30 ميجابايت، لكنني أفترض أنك تشير إلى عمليات سحب الصور الإجمالية التي تصل إلى ~70 ميجابايت+ لخدمات LibreChat). ومع ذلك، فإن صور Docker الأساسية (مثل التطبيق، MongoDB، MeiliSearch) لا تزال حوالي 500 ميجابايت-1 جيجابايت إجمالاً عند سحبها — Docker Compose هو مجرد أداة تنسيق فوق Docker، وليس المستخدم الرئيسي لعرض النطاق الترددي. سحب الصور عبر شبكة 4G/5G البطيئة سيظل هو عنق الزجاجة، ولكن يمكنك التخفيف من ذلك.

سأوضح الخيارات أدناه، مع إعطاء الأولوية لنصائح توفير عرض النطاق الترددي أولاً. إذا كانت بيانات الجوال محدودة للغاية، ففكر في الربط بشبكة WiFi مؤقتًا أو استخدام إعداد تم تنزيله مسبقًا على جهاز آخر (على سبيل المثال، تصدير/استيراد الصور عبر `docker save`/`docker load`).

### نصائح لتوفير عرض النطاق الترددي لأي إعداد قائم على Docker
- **سحب الصور مسبقًا على اتصال أسرع**: على جهاز آخر بإنترنت أفضل، قم بتشغيل `docker pull node:20-alpine` (للتطبيق)، و `docker pull mongo:7` (قاعدة البيانات)، و `docker pull getmeili/meilisearch:v1.10` (البحث). ثم احفظها في ملفات:
  ```
  docker save -o librechat-app.tar node:20-alpine
  docker save -o mongo.tar mongo:7
  docker save -o meili.tar getmeili/meilisearch:v1.10
  ```
  انقل ملفات .tar عبر USB / محرك أقراص (إجمالي ~500-800 ميجابايت مضغوطة)، ثم على جهاز Ubuntu الخاص بك: `docker load -i librechat-app.tar` إلخ. لا حاجة للسحب عبر الإنترنت.
- **استخدام بدائل أخف**: للاختبار، تخطى MeiliSearch في البداية (إنه اختياري للبحث؛ عطله في الإعدادات). صورة MongoDB هي ~400 ميجابايت — استخدم تثبيت MongoDB محلي بدلاً من ذلك (انظر قسم غير Docker أدناه) لتوفير ~400 ميجابايت.
- **مراقبة الاستخدام**: استخدم `docker pull --quiet` أو أدوات مثل `watch docker images` للمتابعة.
- **الخادم الوكيل أو ذاكرة التخزين المؤقت**: إذا كان لديك مرآة أو خادم وكيل لـ Docker Hub، فقم بتكوينه في `/etc/docker/daemon.json` لتسريع عمليات السحب.

### الخيار 1: Docker الخالص (بدون Compose) – مكافئ لإعداد Compose
يمكنك تكرار سلوك `docker-compose.yml` باستخدام `docker run` و `docker network`. هذا يقوم بتنزيل نفس الصور ولكنه يسمح لك بالتحكم في كل خطوة. إجمالي التنزيل لا يزال ~700 ميجابايت+ (بناء التطبيق + قواعد البيانات).

1. **إنشاء شبكة Docker** (تعزل الخدمات):
   ```
   docker network create librechat-network
   ```

2. **تشغيل MongoDB** (استبدل `your_mongo_key` بكلمة مرور قوية):
   ```
   docker run -d --name mongodb --network librechat-network \
     -e MONGO_INITDB_ROOT_USERNAME=librechat \
     -e MONGO_INITDB_ROOT_PASSWORD=your_mongo_key \
     -v $(pwd)/data/mongodb:/data/db \
     mongo:7
   ```
   - ينشئ `./data/mongodb` للاستمرارية.

3. **تشغيل MeiliSearch** (استبدل `your_meili_key`):
   ```
   docker run -d --name meilisearch --network librechat-network \
     -e MEILI_MASTER_KEY=your_meili_key \
     -p 7700:7700 \
     -v $(pwd)/data/meili:/meili_data \
     getmeili/meilisearch:v1.10
   ```
   - تجاوز هذا إذا كان عرض النطاق الترددي ضيقًا؛ عطله في إعدادات التطبيق لاحقًا.

4. **استنساخ وبناء/تشغيل تطبيق LibreChat**:
   - استنسخ المستودع إذا لم يتم ذلك: `git clone https://github.com/danny-avila/LibreChat.git && cd LibreChat` (~50 ميجابايت تنزيل للمستودع).
   - بناء الصورة (هذا يسحب قاعدة Node.js ~200 ميجابايت ويبني طبقات التطبيق):
     ```
     docker build -t librechat-app .
     ```
   - تشغيله (يربط بقاعدة البيانات، يستخدم متغيرات البيئة — أنشئ ملف `.env` كما في ردّي السابق):
     ```
     docker run -d --name librechat --network librechat-network -p 3080:3080 \
       --env-file .env \
       -v $(pwd):/app \
       librechat-app
     ```
     - في `.env`، عيّن `MONGODB_URI=mongodb://librechat:your_mongo_key@mongodb:27017/LibreChat` و `MEILI_HOST=http://meilisearch:7700` إلخ.

5. **الوصول**: `http://localhost:3080`. السجلات: `docker logs -f librechat`.

- **إيقاف/التنظيف**: `docker stop mongodb meilisearch librechat && docker rm them`.
- **الإيجابيات/السلبيات**: نفس إعداد Compose، ولكنه يدوي أكثر. لا يزال ثقيلاً على البيانات لسحب/بناء الصور.

### الخيار 2: التثبيت بدون Docker (يدوي، بدون سحب للصور) – موصى به لعرض النطاق الترددي المنخفض
قم بتثبيت التبعيات بشكل أصلي على Ubuntu. هذا يتجنب كل النفقات العامة لـ Docker (~0 ميجابايت للحاويات؛ فقط تنزيلات الحزم عبر apt/yarn، بإجمالي ~200-300 ميجابايت). يستخدم إعدادات Python/Node الخاصة بالنظام بشكل غير مباشر.

#### المتطلبات الأساسية (ثبت مرة واحدة)
```
sudo apt update
sudo apt install nodejs npm mongodb-org redis meilisearch git curl build-essential python3-pip -y  # الحزمة الرسمية لـ MongoDB; ثنائي MeiliSearch ~50 ميجابايت
sudo systemctl start mongod redis meilisearch
sudo systemctl enable mongod redis meilisearch
```
- Node.js: إذا لم يكن الإصدار v20+، فقم بتثبيته عبر nvm: `curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash`، ثم `nvm install 20`.
- Yarn: `npm install -g yarn`.
- إعدادات MongoDB: قم بتحرير `/etc/mongod.conf` للربط بـ localhost، ثم أعد التشغيل.

#### خطوات التثبيت
1. **استنساخ المستودع**:
   ```
   cd ~/projects
   git clone https://github.com/danny-avila/LibreChat.git
   cd LibreChat
   ```

2. **تثبيت التبعيات**:
   ```
   yarn install  # ~100-200 ميجابايت تنزيل للحزم
   ```

3. **تكوين `.env`** (انسخ من `.env.example`):
   - `cp .env.example .env && nano .env`
   - التغييرات الرئيسية:
     - Mongo: `MONGODB_URI=mongodb://localhost:27017/LibreChat` (أنشئ مستخدم قاعدة بيانات إذا لزم الأمر عبر `mongo` shell).
     - Meili: `MEILI_HOST=http://localhost:7700` و `MEILI_MASTER_KEY=your_key`.
     - عطل البحث إذا كنت تتخطى Meili: `SEARCH=false`.
     - أضف مفاتيح AI حسب الحاجة.

4. **البناء والتشغيل**:
   - في طرفية واحدة: `yarn run backend` (يبدأ API على المنفذ 3090).
   - في أخرى: `yarn run frontend` (يبدأ واجهة المستخدم على المنفذ 3080).
   - أو استخدم PM2 للإنتاج: `yarn global add pm2 && pm2 start yarn --name backend -- run backend` إلخ.

5. **الوصول**: `http://localhost:3080`. أنشئ حسابًا وقم بالتكوين.

- **البيانات**: يقوم MongoDB بالتخزين في `/var/lib/mongodb`، و Meili في `/var/lib/meilisearch`.
- **استكشاف الأخطاء وإصلاحها**:
  - مصادقة Mongo: شغّل `mongo` وأنشئ مستخدمًا: `use LibreChat; db.createUser({user: 'librechat', pwd: 'yourpass', roles: ['readWrite']})`.
  - المنافذ/جدار الحماية: `sudo ufw allow 3080,3090,7700`.
  - التحديثات: `git pull && yarn install && restart services`.
- **الإيجابيات**: أخف على عرض النطاق الترددي (بدون حاويات)، يستخدم موارد النظام مباشرة. السلبيات: إعداد أكثر تعقيدًا، احتمالية تعارض التبعيات (مثلًا، مع Python 3.13 الخاص بك، لكن Node منفصل).

إذا كانت بيانات الجوال محدودة للغاية، فإن الطريقة بدون Docker هي الأفضل — قم بذلك على مراحل، مع المراقبة باستخدام `du -sh` على المجلدات. بالنسبة للأخطاء، شارك السجلات (مثلًا، من `yarn run backend`). الدليل الرسمي بدون Docker: https://docs.librechat.ai/install/installation/manual_install.html. إذا كنت تحتاج إلى تكامل Ollama للذكاء الاصطناعي المحلي (يوفر تكاليف API)، فقم بتثبيته بشكل منفصل عبر البرنامج النصي الخاص به (~100 ميجابايت). دعني أعرف لإجراء التعديلات!
---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast:free
title: تثبيت LibreChat على أوبونتو
translated: true
type: note
---

### تثبيت LibreChat على أوبونتو 24.04 LTS

LibreChat هي منصة دردشة ذكاء اصطناعي مفتوحة المصدر تدعم نماذج متعددة للذكاء الاصطناعي (مثل OpenAI، Gemini، Ollama) من خلال واجهة ويب. طريقة التثبيت الموصى بها هي استخدام Docker Compose، لأنها بسيطة، وتتعامل مع التبعيات مثل MongoDB وMeiliSearch تلقائيًا، وتعمل بموثوقية على أوبونتو. نظامك (أوبونتو 24.04.2 LTS مع Python 3.13.4) يستوفي المتطلبات، لكنك ستحتاج إلى تثبيت Docker وGit أولاً.

#### المتطلبات الأساسية
1. **تحديث النظام**:
   ```
   sudo apt update && sudo apt upgrade -y
   ```

2. **تثبيت Git** (إذا لم يكن مثبتًا مسبقًا):
   ```
   sudo apt install git -y
   ```

3. **تثبيت Docker و Docker Compose**:
   - تثبيت Docker:
     ```
     sudo apt install docker.io -y
     sudo systemctl start docker
     sudo systemctl enable docker
     sudo usermod -aG docker $USER
     ```
     سجل الخروج ثم ادخل مرة أخرى (أو نفذ الأمر `newgrp docker`) حتى تصبح تغييرات المجموعة فعالة.
   - تثبيت Docker Compone (أحدث إصدار):
     ```
     sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
     sudo chmod +x /usr/local/bin/docker-compose
     ```
     تحقق من التثبيت باستخدام `docker-compose --version`.

#### خطوات التثبيت
1. **استنساخ مستودع LibreChat**:
   ```
   cd ~/projects  # أو المجلد الذي تفضله
   git clone https://github.com/danny-avila/LibreChat.git
   cd LibreChat
   ```

2. **نسخ وتهيئة ملف البيئة (.env)**:
   - انسخ ملف المثال:
     ```
     cp .env.example .env
     ```
   - حرر ملف `.env` باستخدام محرر نصوص (مثل `nano .env`). الإعدادات الرئيسية التي يجب تحديثها:
     - عيّن مفتاح MongoDB الرئيسي: أنشئ كلمة مرور قوية وعيّن `MONGODB_URI=mongodb://mongodb:27017/LibreChat?authSource=admin` و `MONGODB_MASTER_KEY=your_generated_key_here`.
     - لـ MeiliSearch: عيّن `MEILI_MASTER_KEY=your_generated_key_here` (أنشئ مفتاحًا قويًا).
     - أضف مفاتيح واجهة برمجة تطبيقات (API) للذكاء الاصطناعي إذا لزم الأمر (مثل `OPENAI_API_KEY=your_openai_key`). للنماذج المحلية مثل Ollama، لا يلزم وجود مفتاح في البداية.
     - احفظ الملف واخرج منه. للحصول على خيارات التهيئة الكاملة، راجع الوثائق.

3. **تشغيل LibreChat باستخدام Docker Compose**:
   ```
   docker-compose up -d
   ```
   - هذا الأمر سيسحب الصور المطلوبة، ويشغل الخدمات (تطبيق LibreChat، MongoDB، MeiliSearch)، ويعمل في الوضع المنفصل (detached mode).
   - انتظر حتى يتم بدء التشغيل بالكامل (يمكنك التحقق باستخدام `docker-compose logs -f`).

4. **الوصول إلى LibreChat**:
   - افتح متصفحك واذهب إلى `http://localhost:3080`.
   - أنشئ حسابًا على صفحة تسجيل الدخول.
   - اختر نموذج الذكاء الاصطناعي المطلوب (قم بتهيئة نقاط النهاية في الإعدادات) وابدأ المحادثة.

#### نصائح ما بعد التثبيت
- **الإيقاف/التحديث**: نفّذ `docker-compose down` للإيقاف، ثم `git pull` ثم `docker-compose up -d --build` للتحديث.
- **استمرارية البيانات**: يتم إنشاء وحدات تخزين (Volumes) تلقائيًا لبيانات MongoDB (في `./data/mongodb`).
- **استكشاف الأخطاء وإصلاحها**:
  - في حالة تعارض المنافذ، قم بتحرير ملف `docker-compose.yml` لتغيير `3080:3080`.
  - للوصول إلى الخادم بدون واجهة رسومية (headless/server)، استخدم عنوان IP الخاص بخادمك (مثل `http://your-server-ip:3080`) وتأكد من أن الجدار الناري يسمح بالمنفذ 3080 (`sudo ufw allow 3080`).
  - إذا كنت تستخدم نماذج لغوية محلية (LLMs)، قم بتثبيت Ollama بشكل منفصل وأضفه كنقطة نهاية في ملف `.env`.
- **الطريقة البديلة: NPM** (بدون Docker): إذا كنت تفضل ذلك، يمكنك تثبيت Node.js 18+، Yarn، MongoDB، وMeiliSearch يدويًا، ثم تنفيذ `yarn install` و `yarn run frontend` + `yarn run backend`. لكن يوصى بشدة باستخدام Docker للبساطة.

هذا يجب أن يجعلك جاهزًا للعمل بسرعة. إذا واجهت أخطاء، شارك ناتج الأمر للحصول على مزيد من المساعدة!

[وثائق LibreChat الرسمية](https://docs.librechat.ai/install/installation/docker_compose.html)  
[دليل أوبونتو لـ Docker](https://docs.librechat.ai/install/installation/docker_ubuntu.html)  
[برنامج It's FOSS التعليمي](https://itsfoss.com/librechat-linux/)
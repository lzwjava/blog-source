---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: تحسين ذاكرة دوكر لـ LibreChat
translated: true
type: note
---

### فهم استخدام الذاكرة في Docker مع LibreChat

LibreChat هو تطبيق يستهلك موارد كثيرة لأنه يعمل بكامل مكوناته: واجهة LibreChat الرئيسية، MongoDB لتخزين البيانات، Meilisearch لفهرسة البحث، قاعدة بيانات متجهات (على الأرجح Pinecone أو مشابه عبر vectordb)، وواجهة برمجة تطبيقات RAG للتوليد المعزز بالاسترجاع. كل من هذه الخدمات معزولة في حاويات Docker، مما يضيف بعض النفقات العامة—خاصة على نظام macOS، حيث يعمل Docker Desktop على تشغيل كل شيء داخل آلة افتراضية خفيفة الوزن لنظام Linux. هذه الآلة الافتراضية وحدها يمكن أن تستهلك 1-2 جيجابايت في وضع الخمول، ومع قواعد البيانات مثل MongoDB (التي تستخدم افتراضيًا ما يصل إلى 50٪ من ذاكرة الوصول العشوائي للخادم) وMeilisearch (التي تفهرس البيانات في الذاكرة)، من السهل الوصول إلى إجمالي 3 جيجابايت.

Docker "سهل" لأنه يحزم التبعيات، ويعزل البيئات، ويبدأ بأمر واحد (مثل `docker compose up`)، متجنبًا متاعب الإعداد اليدوي. ولكن نعم، المقايضة هي استهلاك الموارد: الحاويات لا تشارك نواة النظام المضيف بكفاءة، وبدون تعديلات، فإنها تنتفخ.

#### طرق سريعة لتقليل استخدام الذاكرة
إليك خطوات عملية لتحسين إعدادك دون التخلي عن Docker تمامًا:

1. **تحديد الموارد لكل حاوية**:
   - قم بتحرير ملف `docker-compose.yml` الخاص بك (في مستودع LibreChat). أضف حدود الموارد تحت كل خدمة. على سبيل المثال:
     ```
     services:
       chat-mongodb:
         deploy:
           resources:
             limits:
               memory: 512M  # تحديد MongoDB بحد أقصى 512 ميجابايت
       chat-meilisearch:
         deploy:
           resources:
             limits:
               memory: 256M  # Meilisearch لا تحتاج إلى الكثير
       vectordb:  # بافتراض أنها Qdrant أو مشابه
         deploy:
           resources:
             limits:
               memory: 256M
       rag_api:
         deploy:
           resources:
             limits:
               memory: 128M
       LibreChat:
         deploy:
           resources:
             limits:
               memory: 512M
     ```
     - شغّل `docker compose down` ثم `docker compose up -d` للتطبيق. هذا لن يكسر الأشياء ولكن قد يبطئ الاستعلامات إذا وصلت إلى الحدود—راقب باستخدام `docker stats`.

2. **ضبط إعدادات Docker Desktop**:
   - افتح Docker Desktop > الإعدادات > الموارد. اضبط الذاكرة على 2-4 جيجابايت إجمالاً (بدلاً من غير المحدد). فعّل "Use Rosetta for x86/amd64 emulation on Apple Silicon" إذا كانت أي صور ليست أصلية لـARM (جهاز M2 Air يعتمد على ARM، لذا يجب أن تكون معظمها جاهزة).
   - نظف الأشياء غير المستخدمة: `docker system prune -a` لتحرير مساحة القرص/الانتفاخ في الآلة الافتراضية.

3. **تعطيل الخدمات غير الضرورية**:
   - إذا كنت لا تستخدم البحث المتجه/RAG، قم بتعليق `vectordb` و `rag_api` في ملف `docker-compose.yml`.
   - للدردشة الأساسية، قد يقلل استخدام MongoDB + LibreChat وحدها الاستهلاك إلى حوالي ~1.5 جيجابايت.

4. **استخدم الصور الم optimized لـARM**:
   - تأكد من أنك على أحدث إصدار من LibreChat (الإصدار v0.7+ يدعم M1/M2 أصليًا). اسحب التحديثات باستخدام `docker compose pull`.

#### التشغيل بدون Docker: نعم، يمكن أن يكون أسرع/أخف
بالتأكيد—تخطي Docker يزيل النفقات العامة للآلة الافتراضية (يوفر 0.5-1 جيجابايت) ويسمح للخدمات بالعمل أصليًا على نظام macOS. لدى LibreChat دليل تثبيت يدوي يستخدم Node.js وnpm وتثبيت الخدمات مباشرة. قد تشعر بأنه أسرع على جهاز M2 Air الخاص بك حيث أن كل شيء يستفيد من ذاكرة Apple الموحدة دون الافتراضية.

**إيجابيات التثبيت الأصلي**:
- ذاكرة وصول عشوائي أقل (توقع 1-2 جيجابايت إجمالاً).
- بدء تشغيل وإدخال/إخراج أسرع (بدون شبكات الحاويات).
- تصحيح أخطاء أسهل.

**السلبيات**:
- خطوات إعداد أكثر (تثبيت MongoDB/Meilisearch يدويًا عبر Homebrew).
- احتمالية وجود تعارضات في التبعيات.

**دليل الإعداد الأصلي السريع** (لـmacOS):
1. قم بتثبيت المتطلبات الأساسية:
   - Node.js (الإصدار v18+): استخدم Homebrew `brew install node`.
   - MongoDB: `brew tap mongodb/brew && brew install mongodb-community`. ابدأ بـ `brew services start mongodb/brew/mongodb-community`.
   - Meilisearch: `brew install meilisearch`. ابدأ بـ `meilisearch --master-key=your-master-key`.
   - Yarn: `npm install -g yarn`.

2. استنساخ وتثبيت LibreChat:
   ```
   git clone https://github.com/danny-avila/LibreChat.git
   cd LibreChat
   cp .env.example .env
   # تحرير .env: اضبط MONGO_URI=mongodb://localhost:27017/librechat, MEILI_MASTER_KEY=your-master-key، إلخ.
   yarn install
   yarn build
   yarn dev  # أو yarn start للإنتاج
   ```

3. الوصول عبر http://localhost:3080. عدّل ملف `.env` لتعطيل RAG إذا لم يكن مستخدمًا.

إذا واجهت مشاكل (مثل توافق ARM)، فإن الوثائق الرسمية تحتوي على استكشاف الأخطاء وإصلاحها. هذا يجب أن يجعلك بسهولة تحت 2 جيجابايت.

#### أدوات المراقبة
- **Activity Monitor** (مدمج): شاهد علامة تبويب "الذاكرة" لعمليات Docker.
- **docker stats**: استخدام الحاوية في الوقت الفعلي في الطرفية.
- إذا استمرت المشكلة، تحقق من مشاكل GitHub الخاصة بـLibreChat—الكثير من الأشخاص على أجهزة M1/M2 يبلغون عن شكاوى مماثلة.

إذا لم يصلح هذا الأمر أو إذا شاركت ملف `docker-compose.yml` الخاص بك، يمكنني تحسين النصيحة!

[الوثائق الرسمية لـLibreChat - تحسين Docker](https://docs.librechat.ai/install/providers/docker.html)  
[دليل التثبيت اليدوي لـLibreChat](https://docs.librechat.ai/install/installation/manual_install.html)  
[حدود موارد Docker Desktop على macOS](https://docs.docker.com/desktop/settings/mac/)
---
audio: false
generated: true
image: false
lang: ar
layout: post
model: openai/gpt-5
title: دليل استعادة حاوية Docker الخاصة بـ MongoDB
translated: true
type: note
---

شكرًا — إخراج `docker inspect` يؤكد أن الحاوية **متوقفة** وأن دليل بيانات MongoDB الخاص بك هو نقطة ربط مضيف:
`/Users/lzwjava/projects/LibreChat/data-node:/data/db:rw`.
هذه أخبار جيدة — *ملفات بيانات MongoDB الخاصة بك موجودة على مضيف macOS الخاص بك*، لذا يمكن نسخها احتياطيًا قبل أن نقوم بأي تنظيف مدمر على جانب Docker.

أدناه مساران آمنان. **المسار أ (موصى به)** يحافظ على بياناتك وهو أبسط: قم بنسخ دليل البيانات على المضيف احتياطيًا، ثم استخدم Troubleshoot → Clean / Purge في Docker Desktop. **المسار ب (متقدم / ملاذ أخير)** يذهب نحو حذف منخفض المستوى لحالة Docker VM. سأقدم أوامر دقيقة حتى تتمكن من النسخ/اللصق.

---

# المسار أ — موصى به (نسخ بيانات المضيف احتياطيًا، ثم استخدام إعادة تعيين Docker Desktop)

1. تأكد من وجود دليل البيانات على المضيف واعرض محتوياته:

```bash
ls -la /Users/lzwjava/projects/LibreChat/data-node
```

2. أنشئ نسخة احتياطية من نوع tar لهذا الدليل (هذا يحافظ على ملفات MongoDB الخاصة بك):

```bash
mkdir -p ~/docker-backups/librechat
tar -czvf ~/docker-backups/librechat/data-node-backup-$(date +%Y%m%dT%H%M%S).tgz -C /Users/lzwjava/projects/LibreChat data-node
# النتيجة: ~/docker-backups/librechat/data-node-backup-YYYYMMDDTHHMMSS.tgz
```

(يمكنك أيضًا نسخ المجلد بدلاً من استخدام tar إذا كنت تفضل `cp -a /Users/lzwjava/projects/LibreChat/data-node ~/docker-backups/librechat/data-node-copy`.)

3. أغلق Docker Desktop تمامًا:

```bash
osascript -e 'quit app "Docker"'
```

4. افتح Docker Desktop → Troubleshoot (أو Preferences → Troubleshoot) → انقر على **Clean / Purge data** (أو **Reset to factory defaults** إذا لم يكن Clean موجودًا).

   * **مهم**: هذا يزيل صور وحاويات وحجوم Docker التي تعيش داخل Docker VM، لكنه **لن** يزيل الملفات المرتبطة من مضيف macOS الخاص بك (نسختك الاحتياطية `/Users/.../data-node` تضمن أنك في أمان).

5. بعد إعادة تعيين Docker، شغّل Docker Desktop مرة أخرى، تحقق من أن Docker يعمل، ثم أعد تشغيل كومبوز stack الخاص بك:

```bash
open -a Docker
# انتظر حتى يصبح Docker في حالة صحية
docker compose up -d
```

6. تحقق من حاوية Mongo والبيانات:

```bash
docker ps -a
# docker logs <new-mongo-container-id>  (إذا لزم الأمر)
```

إذا بدا أن هناك خطأ ما في الخطوة 5/6، استرجع النسخة الاحتياطية: أوقف أي حاوية mongo قيد التشغيل، انقل أو أزل مجلد data-node المعاد إنشاؤه واستخرج النسخة الاحتياطية من الأرشيف إلى `/Users/lzwjava/projects/LibreChat/data-node`.

---

# المسار ب — متقدم / ملاذ أخير (حذف يدوي لملفات Docker Desktop VM)

استخدم هذا فقط إذا *لم تتمكن* من استخدام واجهة Clean/Purge في Docker Desktop أو إذا لم تحل المشكلة وأنت تقبل بخسارة الحالة الداخلية لـ Docker.

1. أغلق Docker Desktop:

```bash
osascript -e 'quit app "Docker"'
```

2. انسخ إعدادات مستخدم Docker Desktop احتياطيًا (اختياري):

```bash
cp -a ~/Library/Containers/com.docker.docker ~/Library/Containers/com.docker.docker.backup-$(date +%Y%m%dT%H%M%S)
```

3. أزل الحالة الداخلية لـ Docker Desktop (مدمر — يحذف الحاويات/الصور داخل Desktop VM):

```bash
rm -rf ~/Library/Containers/com.docker.docker
rm -rf ~/.docker
```

4. أعد تشغيل Docker Desktop:

```bash
open -a Docker
```

5. أعد إنشاء stack الخاص بك:

```bash
docker compose up -d
```

مرة أخرى — بيانات Mongo المرتبطة بالمضيف الخاصة بك ستبقى دون مساس لأنها موجودة في `/Users/...` ما لم تحذفها يدويًا.

---

# فحوصات إضافية / أوامر يمكنك لصقها هنا إذا أردت مني مراجعتها قبل إعادة التعيين

(هذه غير مدمرة.)

```bash
# أظهر أن البيانات موجودة على المضيف
ls -la /Users/lzwjava/projects/LibreChat/data-node

# أظهر الصور والحجوم حتى نتمكن من التخطيط للحفظ
docker images
docker volume ls

# معلومات docker و ps للتشخيص السريع
docker info
docker ps -a
```

إذا قمت بلصق إخراج `ls -la` لمجلد `data-node`، سأؤكد أن النسخة الاحتياطية تبدو سليمة. إذا كنت تفضل، تابع مع المسار أ: انسخ احتياطيًا (الخطوة 2) ثم شغّل Docker Desktop → Troubleshoot → Clean / Purge — هذا هو الإصلاح الأنظف وعادة ما يحل خطأ إزالة `overlay2` العالق مع الحفاظ على ملفات Mongo الخاصة بك في أمان.
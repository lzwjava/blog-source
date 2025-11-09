---
audio: false
generated: true
image: false
lang: ar
layout: post
model: openai/gpt-5
title: حل مشكلات إزالة حاويات Docker
translated: true
type: note
---

جيد — شكرًا، هذا الإخراج يؤكد أن الحاوية عالقة في حالة **Removal In Progress** وأن `docker rm -f` يفشل مع نفس الخطأ في overlay2. أدناه سأقدم خطة استرداد دقيقة ومرتبة خصيصًا لـ **macOS باستخدام Docker Desktop** (موجهك يُظهر رسائل الوكيل الخاصة بـ Docker Desktop). سأحدد الخطوات التدميرية بوضوح وسأقدم أوامر دقيقة يمكنك نسخها/لصقها. اتبعها بالترتيب حتى يتم حل المشكلة.

---

## 1) فحوصات سريعة غير تدميرية (أوامر من سطر واحد)

شغّل هذه أولاً — فهي آمنة وتساعد في جمع المعلومات.

```bash
# إصدارات Docker والمعلومات (مفيدة لتصحيح الأخطاء)
docker version
docker info

# فحص الحاوية العالقة (قد تُرجع أو لا تُرجع معلومات كاملة)
docker inspect ccd89a3f36a1528cb923c90de8755faeb36e229cab353c2285222948197b8d18 || true

# محاولة قراءة السجلات (قد تفشل إذا كانت حالة الحاوية تالفة)
docker logs ccd89a3f36a1528cb923c90de8755faeb36e229cab353c2285222948197b8d18 || true
```

إذا أنتج `docker inspect` أو `docker logs` مخرجات مفيدة، الصقها هنا وسأقوم بتحليلها. (إذا كانت تظهر خطأ مع رسائل overlay، يمكنك المتابعة.)

---

## 2) إعادة تشغيل Docker Desktop (آمن، وغالبًا ما يحل المشكلة)

أغلق Docker Desktop تمامًا، ثم ابدأ تشغيله مرة أخرى.

```bash
osascript -e 'quit app "Docker"'
open -a Docker
```

بعد إعادة تشغيل Docker، جرب:

```bash
docker rm -f ccd89a3f36a1528cb923c90de8755faeb36e229c
```

إذا استمر الفشل، تابع.

---

## 3) إذا لم تساعد إعادة التشغيل — أوقف عملية VM منخفضة المستوى ثم أعد تشغيل Docker (آمن نسبيًا)

في بعض الأحيان تكون VM المضمنة (hyperkit) معلقة. إنهاؤها يجبر على إعادة تشغيل نظيفة. هذا آمن عادةً ولكنه سيوقف جميع الحاويات قيد التشغيل.

```bash
# ابحث عن عملية hyperkit المستخدمة من قبل Docker Desktop
ps aux | grep -i hyperkit | grep -v grep

# أوقفها (استبدل PID بالرقم من الأمر السابق)
sudo kill -9 <PID>

# ثم ابدأ تشغيل Docker مرة أخرى
open -a Docker
```

جرب `docker rm -f <id>` مرة أخرى.

---

## 4) محاولات تنظيف غير تدميرية

إذا كانت الحاوية لا تزال لا تُزال، جرب تقليم كائنات Docker غير المستخدمة. هذه آمنة للعناصر غير المستخدمة:

```bash
docker system prune -f
docker volume prune -f
docker container prune -f
```

ثم أعد محاولة أمر `docker rm -f`.

---

## 5) قم بتصدير ما تحتاجه قبل إعادة التعيين التدميرية (مهم)

إذا لم يُصلح شيء الحاوية العالقة، فإن الخيار العملي التالي على Docker Desktop هو **Reset / Clean / Purge** عبر واجهة مستخدم Docker Desktop — ولكن هذا **يمكن أن يحذف الصور/وحدات التخزين/الحاويات**. إذا كان لديك صور أو وحدات تخزين تريد الاحتفاظ بها، احفظها الآن.

احفظ الصور:

```bash
# اذكر الصور التي تهتم بها
docker images

# احفظ صورة (مثال)
docker save -o ~/myimage.tar my-image:tag
```

صدّر وحدات التخزين (مثال — استبدل `myvolume` و `./backup` حسب الحاجة):

```bash
mkdir -p ~/docker-vol-backups
docker run --rm -v myvolume:/data -v ~/docker-vol-backups:/backup alpine \
  sh -c "cd /data && tar czf /backup/myvolume.tgz ."
```

إذا كانت الحاوية العالقة تمنع الوصول الطبيعي إلى وحدات التخزين عبر `docker run`، فقد لا تعمل النسخ الاحتياطية؛ في هذه الحالة تابع إلى خيار Reset أدناه.

---

## 6) استخدم واجهة Troubleshoot في Docker Desktop — الخطوة التالية الموصى بها

افتح Docker Desktop → انقر على أيقونة **Troubleshoot** (أو Preferences → Troubleshoot). جرب هذه بالترتيب:

1.  **Restart Docker** (إذا لم تقم بذلك بعد إنهاء hyperkit).
2.  **Clean / Purge data** — هذا يزيل الصور/الحاويات/وحدات التخزين. **تدميري**.
3.  **Reset to factory defaults** — **تدميري**، يعيد حالة Docker Desktop إلى الإعدادات الافتراضية.

إذا كنت تريد مني المساعدة في الاحتفاظ بالصور/وحدات التخزين المهمة قبل إعادة التعيين، أخبرني بمخرجات `docker images` و `docker volume ls` (من الخطوة 1) وسأعطي أوامر حفظ/تصدير دقيقة.

---

## 7) إزالة ملفات Docker VM قسريًا (متقدم / تدميري) — فقط إذا كنت تقبل فقدان البيانات

إذا كنت مرتاحًا لفقدان بيانات Docker المحلية ولم تنجح إعادة التعيين من واجهة المستخدم، يمكنك حذف ملفات VM الخاصة بـ Docker Desktop. هذا هو الملاذ الأخير.

**تحذير — هذا يحذف جميع حاويات وصور ووحدات تخزين Docker Desktop.**

1.  أغلق Docker Desktop.
2.  في Finder أو الطرفية، احذف مجلد بيانات Docker:

```bash
# أغلق docker أولاً
osascript -e 'quit app "Docker"'

# أزِل بيانات VM لـ Docker Desktop (تدميري)
rm -rf ~/Library/Containers/com.docker.docker
rm -rf ~/.docker
```

3.  ابدأ تشغيل Docker Desktop مرة أخرى (سيقوم بإعادة إنشاء الحالة). ثم شغّل `docker system prune -a --volumes` لتنظيف ما تبقى.

---

## 8) جمع التشخيصات للحصول على مساعدة أعمق

إذا كنت تريد مني البحث أكثر قبل الخطوات التدميرية، أنشئ تشخيصات Docker Desktop والصق معرف التشخيص هنا:

*   Docker Desktop → Troubleshoot → **Get Support** أو **Generate Diagnostics** — سيعطيك معرف تشخيص. شارك ذلك المعرف (أو أرشيف التشخيص الكامل) ويمكنني تفسير السجلات والتوصية بإصلاحات مستهدفة.

يمكنك أيضًا لصق مخرجات هذه الأوامر (غير تدميرية):

```bash
docker info
docker ps -a
docker inspect ccd89a3f36a1528cb923c90de8755faeb36e229cab353c2285222948197b8d18 || true
```

---

## المسار الموصى به المختصر (ملخص)

1.  أغلق وأعد تشغيل Docker Desktop. جرب `docker rm -f` مرة أخرى.
2.  إذا كانت لا تزال عالقة: أوقف hyperkit (sudo kill -9 PID)، أعد تشغيل Docker Desktop. أعد المحاولة.
3.  شغّل `docker system prune` / `volume prune`. أعد المحاولة.
4.  صدّر/احفظ أي صور/وحدات تخزين تحتاجها.
5.  استخدم Docker Desktop → Troubleshoot → **Clean / Purge data** (أو Reset) إذا كنت تستطيع تحمل خسارة البيانات.
6.  إذا كنت تريد مني المساعدة في تفسير السجلات قبل الخطوات التدميرية، الصق مخرجات `docker info` و `docker ps -a` أو معرف التشخيص.

---

أخبرني أي خطوة جربتها للتو والصق مخرجات:

```bash
docker info
docker ps -a
docker images
docker volume ls
```

— سأقوم بتحليلها وسأعطي الأمر التالي الدقيق المخصص لحالتك.
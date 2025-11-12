---
audio: false
generated: true
image: false
lang: ar
layout: post
model: openai/gpt-5
title: حل أخطاء إزالة Overlay2 في Docker
translated: true
type: note
---

هذا الخطأ يعني أن Docker فشل في إزالة نظام ملفات overlay2 للحاوية — حيث أرجعت النواة/الآلة الافتراضية خطأ منخفض المستوى في الإدخال/الإخراج (`readdirent merged: bad message`). على نظام macOS، يحدث هذا عادةً عندما تكون الآلة الافتراضية لـ Docker أو تخزين overlay في حالة غير سليمة. فيما يلي خطوات آمنة ومتسلسلة (من الأقل تدميراً إلى الأكثر قوة) يمكنك تجربتها للتعافي.

**مهم:** بعض الأوامر أدناه يمكنها إزالة البيانات (الصور/الحجوم). سأحدد الخطوات التدميرية وأعرض الأوامر الدقيقة حتى تتمكن من نسخها/لصقها إذا أردت.

---

# فحوصات سريعة (آمنة)

في الطرفية، نفّذ:

```bash
# عرض حالة الحاوية ومعرف الحاوية المشكلة
docker ps -a --no-trunc | grep ccd89a3f36a1528cb923c90de8755faeb36e229c || true

# محاولة إزالة الحاوية قسرياً
docker rm -f ccd89a3f36a1528cb923c90de8755faeb36e229c
```

إذا نجح `docker rm -f`، فقد انتهيت. إذا فشل بنفس خطأ overlay، فتابع.

---

# إعادة تشغيل Docker (Docker Desktop لنظام macOS) — الخطوة التالية الموصى بها (آمنة)

أغلق Docker Desktop تماماً (استخدم أيقونة الحوت → Quit) ثم ابدأ تشغيله مرة أخرى. أو من سطر الأوامر:

```bash
# نظام macOS — إعادة تشغيل Docker Desktop عبر AppleScript
osascript -e 'quit app "Docker"'
open -a Docker
```

بعد إعادة تشغيل Docker، حاول `docker compose down` أو `docker rm -f <id>` مرة أخرى.

---

# إعادة تشغيل المضيف (آمن جداً)

إذا كانت إعادة التشغيل ممكنة، فإن إعادة تشغيل macOS غالباً ما تزيل مشاكل نظام ملفات الآلة الافتراضية:

* أعد تشغيل جهاز Mac، ثم شغّل Docker Desktop وحاول مرة أخرى.

---

# إذا كان لا يزال فاشلاً — استخدم إجراءات Troubleshoot في Docker Desktop (آمن / متوسط)

افتح Docker Desktop → Troubleshoot:

* انقر على **Restart Docker** (إذا لم تفعل ذلك بالفعل).
* إذا فشل ذلك، حاول **Clean / Purge data** أو **Reset to factory defaults** — **تحذير**: هذه الإجراءات تزيل الصور/الحاويات/الحجوم. استخدمها فقط إذا كان بإمكانك تحمل خسارة بيانات Docker المحلية.

---

# إذا كنت تستخدم Docker Engine (Linux) أو مرتاحاً للتنظيف اليدوي (تدميري)

**افعل هذا فقط إذا كنت تفهم مخاطر فقدان البيانات.** أوقف daemon Docker، أزل دليل overlay2 للمعرف المشكلة، ثم أعد تشغيل Docker.

```bash
# إيقاف daemon Docker (Linux)
sudo systemctl stop docker

# احفظ نسخة احتياطية من مجلد overlay2 أولاً (اختياري، إذا كان لديك مساحة)
sudo cp -a /var/lib/docker/overlay2/7acbf095f3537e4829397e10f2134499389c724d3378782a8882ff1299fc431f /root/overlay2-backup-7acbf095

# إذا تم عمل نسخة احتياطية / ليست ضرورية، أزل الدليل merged لذلك overlay:
sudo rm -rf /var/lib/docker/overlay2/7acbf095f3537e4829397e10f2134499389c724d3378782a8882ff1299fc431f

# (اختياريًا) إزالة metadata الحاوية إذا لزم الأمر
# تحذير: أزل فقط الملفات التي أنت متأكد من أنها تتوافق مع الحاوية التالفة
sudo rm -rf /var/lib/docker/containers/ccd89a3f36a1528cb923c90de8755faeb36e229cab353c2285222948197b8d18

# بدء تشغيل docker
sudo systemctl start docker

# ثم حاول تنظيف العناصر المعلقة
docker system prune -a --volumes
```

مرة أخرى: حذف الملفات تحت `/var/lib/docker` إجراء تدميري ويمكن أن يكسر حاويات أخرى إذا تم بشكل غير صحيح. استخدمه فقط إذا كنت تعرف ما الذي تحذفه.

---

# تنظيف أقل تدميراً غالباً ما يساعد

إذا لم تتمكن من حذف overlay مباشرة أو تفضل نهجاً أكثر لطفاً:

```bash
# حاول تقليم الكائنات غير المستخدمة
docker system prune -f
docker volume prune -f

# إزالة الصور/الحاويات غير المستخدمة (كن حذراً)
docker image prune -a -f
docker container prune -f
```

يمكن لهذا أن يحرر مساحة ويسمح أحياناً لـ Docker بإعادة تشغيل عمليات الإزالة بنجاح.

---

# إذا تكررت المشكلة وأنت تستخدم Docker Desktop for Mac

* فكر في زيادة حجم قرص الآلة الافتراضية لـ Docker (Settings → Resources → Disk image size).
* إذا كنت تعتمد على بيانات محلية مهمة، فقم بتصدير الحجوم/الحاويات أولاً (`docker export`, `docker save`) قبل استخدام Reset/Purge.

---

# تشخيصات لجمعها (إذا أردت مني المساعدة أكثر)

إذا لم ينجح أي مما سبق في إصلاحها، شارك مخرجات هذه الأوامر (غير التدميرية) وسأقترح خطوات تالية مستهدفة:

```bash
docker info
docker ps -a
docker compose version
docker version
# سرد أدلة overlay (Linux)
ls -lah /var/lib/docker/overlay2 | head -n 40
```

(إذا كنت تستخدم Docker Desktop على macOS، فإن `ls /var/lib/docker` لن يعرض محتويات الآلة الافتراضية — يفضل إعادة تشغيل Docker Desktop أو استخدام واجهة Troubleshoot.)

---

إذا أردت، أخبرني ما إذا كنت تشغّل **Docker Desktop على macOS** (على الأرجح) أم **Docker Engine على Linux** — سأعطيك تسلسلاً أقصر ومخصصاً. إذا فضلت، يمكنني أيضاً إنشاء قائمة تحقق من سطر واحد يمكنك تشغيلها بالترتيب.
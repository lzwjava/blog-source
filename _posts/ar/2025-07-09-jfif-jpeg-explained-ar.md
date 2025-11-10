---
audio: false
generated: true
image: false
lang: ar
layout: post
title: جيه بيه إي إف هو مجرد جيه بيه إي جي موضح
translated: true
type: note
---

يمثل اختصار JFIF **تنسيق تبادل ملفات JPEG** (JPEG File Interchange Format).

### ما هو JFIF

* إنه ليس تنسيق صورة مختلف عن JPEG، بل هو **طريقة موحدة لتضمين البيانات الوصفية والهيكل داخل ملف JPEG**.
* الملفات ذات الامتداد `.jfif` تظل **صور JPEG** — فهي ببساطة تعلن صراحة عن مواصفات JFIF في رؤوسها.
* العديد من الأدوات (خاصة القديمة مثل Windows Paint أو بعض الكاميرات/الماسحات الضوئية) استخدمت الامتداد `.jfif` كامتداد افتراضي بدلاً من `.jpg` أو `.jpeg`.

لذا، عندما ترى ملفًا بامتداد `.jfif`، يمكنك التعامل معه تمامًا مثل صورة `.jpg`.

---

### كيفية تحويل JFIF إلى تنسيقات الصور القياسية

1. **إعادة تسمية الامتداد**

   * في معظم الحالات، ما عليك سوى إعادة تسمية `image.jfif` → `image.jpg`.
   * نظرًا لأن التنسيق الأساسي هو JPEG، فإن معظم البرامج ستفتحه دون مشكلة.

2. **استخدام برامج تحرير الصور**

   * افتح ملف `.jfif` في Photoshop أو GIMP أو Paint أو Preview (macOS).
   * احفظ/صدّر الملف كـ `.jpg` أو `.png`.

3. **استخدام Python (Pillow)**

   ```python
   from PIL import Image

   img = Image.open("image.jfif")
   img.save("image.jpg")   # save as JPEG
   img.save("image.png")   # or convert to PNG
   ```

4. **استخدام سطر الأوامر (ImageMagick)**

   ```bash
   magick image.jfif image.jpg
   ```

   أو باستخدام FFmpeg (بما أنه يمكنه فك تشفير الصور أيضًا):

   ```bash
   ffmpeg -i image.jfif image.jpg
   ```

---

✅ باختصار: **JFIF هو مجرد JPEG**، لذا يمكنك فتحه مثل أي ملف `.jpg`. إذا كانت هناك مشكلة في التوافق، ما عليك سوى إعادة تسميته أو تحويله باستخدام Pillow/ImageMagick.

هل تريد مني أن أعطيك **برنامج نصي Python** سريعًا يمكنه تحويل جميع ملفات `.jfif` في مجلد دفعة واحدة إلى `.jpg`؟
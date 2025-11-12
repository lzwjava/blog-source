---
audio: false
generated: true
lang: ar
layout: post
title: تصور التبعيات
translated: true
type: note
---

لتصور رسم تبعيات Maven الذي يولده نص Python المقدم، يمكنك استخدام **Graphviz**، وهو أداة رسومية شائعة الاستخدام وبسيطة تعرض الرسوم الموضحة بلغة DOT. ينتج النص رسمًا للتبعيات بتنسيق DOT، يمثل التبعيات بين الوحدات داخل مشروع Maven كرسم موجه، حيث تمثل العقد بواسطة `artifactId` وتظهر الحواف علاقات التبعية. فيما يلي الخطوات لرسم وتصور هذا الرسم باستخدام Graphviz، مع ذكر أدوات بديلة مثل Polyglot أو غيرها إذا كنت تفضل خيارات مختلفة.

---

### استخدام Graphviz (الطريقة الموصى بها)

Graphviz مثالي هنا لأن النص يولد مخرجات بتنسيق DOT مباشرة، وهو التنسيق الذي يدعمه Graphviz بشكل أصلي. اتبع هذه الخطوات:

1. **تشغيل النص البرمجي**  
   نفذ نص Python، مع تقديم الدليل الجذري لمشروع Maven كوسيط. هذا يولد مخرجات DOT لرسم التبعيات.
   ```bash
   python script.py /path/to/maven/project
   ```

2. **حفظ مخرجات DOT في ملف**  
   إعادة توجيه مخرجات النص إلى ملف، على سبيل المثال، `dependencies.dot`. سيحتوي هذا الملف على وصف الرسم بتنسيق DOT.
   ```bash
   python script.py /path/to/maven/project > dependencies.dot
   ```

3. **تثبيت Graphviz (إذا لم يكن مثبتًا بالفعل)**  
   Graphviz متاح لأنظمة Windows وmacOS وLinux. قم بتثبيته باستخدام مدير الحزم الخاص بك:
   - **Ubuntu/Debian**:  
     ```bash
     sudo apt-get install graphviz
     ```
   - **macOS (باست
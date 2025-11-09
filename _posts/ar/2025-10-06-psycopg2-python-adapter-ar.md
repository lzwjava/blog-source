---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: محول Psycopg2 لـ PostgreSQL لـ Python
translated: true
type: note
---

**Psycopg2** هو محول قاعدة بيانات PostgreSQL مفتوح المصدر وشائع (يُعرف أيضًا باسم برنامج التشغيل) لغة برمجة Python. يسمح للتطبيقات المكتوبة بلغة Python بالاتصال بقواعد بيانات PostgreSQL، وتنفيذ استعلامات SQL، ومعالجة البيانات بكفاءة. تشمل الميزات الرئيسية:

- الامتثال الكامل لمواصفات Python DB API 2.0.
- دعم الإشعارات غير المتزامنة، والمؤشرات من جانب الخادم، وعمليات COPY.
- مكتوب بلغة C لأداء أفضل، مع دعم اختياري للبيانات الثنائية لنقل بيانات أسرع.
- يُستخدم على نطاق واسع في بيئات الإنتاج لمهام مثل تطوير الويب، وتحليل البيانات، وعمليات ETL.

إنه الجيل الثاني من مكتبة psycopg (ومن هنا جاء الرقم "2" في الاسم)، وبينما يُعد psycopg3 هو الإصدار الأحدث، يظل psycopg2 مستقرًا ويتم صيانته بنشاط لضمان التوافق مع التطبيقات القديمة.

للتثبيت، يمكنك استخدام الأمر `pip install psycopg2-binary` (إصدار binary أسهل للمبتدئين).

[الوثائق الرسمية لـ Psycopg](https://www.psycopg.org/docs/)  
[مقدمة من GeeksforGeeks](https://www.geeksforgeeks.org/python/introduction-to-psycopg2-module-in-python/)  
[صفحة الحزمة على PyPI](https://pypi.org/project/psycopg2/)
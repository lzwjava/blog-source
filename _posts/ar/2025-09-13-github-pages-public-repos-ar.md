---
audio: false
date: 2025-09-13
generated: true
image: false
lang: ar
layout: post
model: openai/gpt-5
title: GitHub Pages يتطلب مستودعات عامة
translated: true
type: note
---

حسنًا — إذا جعلت مستودع GitHub Pages خاصًا، فتفقد استضافة GitHub Pages المجانية.

تعمل GitHub Pages تلقائيًا فقط عندما يكون المستودع **عامًا**. إذا كان المستودع خاصًا، فلن يتم نشر موقع `github.io` إلا إذا كنت تستخدم **خطة GitHub Enterprise مع تمكين Pages للمستودعات الخاصة** (هذه ميزة مدفوعة، غير متضمنة في الحسابات الشخصية المجانية أو القياسية).

إذن بالنسبة لمدونتك الشخصية على `username.github.io`:

* **مستودع عام** → تقوم GitHub Pages ببنائه وتقديمه على `https://username.github.io/`.
* **مستودع خاص (حساب مجاني)** → يتم تعطيل GitHub Pages.
* **مستودع خاص (Enterprise)** → لا يزال يعمل، ولكن فقط إذا مكنت مؤسستك Pages للمستودعات الخاصة.

هل تريد مني أيضًا شرح طريقة بديلة (مثل الحفاظ على مستودعك الرئيسي خاصًا ولكن مزامنة ناتج `_site` فقط إلى مستودع عام منفصل للنشر)؟
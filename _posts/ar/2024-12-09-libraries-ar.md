---
audio: false
generated: false
image: false
lang: ar
layout: post
title: فكر في التحديثات عند استخدام المكتبات
translated: true
type: post
---

لقد استخدمت CodeIgniter في مشروعي الناشئ، [Fun Live](https://github.com/lzwjava/live-server). على الرغم من أن المشروع انتهى، إلا أنه بعد عدة سنوات، أردت إحياءه لتخليد ذكراه. ومع ذلك، في عام 2016، كنت أستخدم CodeIgniter 3، بينما الإصدار الأحدث الآن هو CodeIgniter 4.

لقد أثبت الترقية أنها مشكلة لأن الكود الخاص بي مرتبط بشكل وثيق بإطار عمل CodeIgniter. باتباع دليل الترقية الموجود على الرابط [https://codeigniter4.github.io/CodeIgniter4/installation/upgrade_4xx.html](https://codeigniter4.github.io/CodeIgniter4/installation/upgrade_4xx.html)، يتضح أن الأمر يتطلب جهدًا كبيرًا لتحديث قاعدة الكود.

هذه التجربة علمتني درسًا مهمًا: عند كتابة التعليمات البرمجية، يجب أن نفكر بعناية في كيفية التعامل مع التحديثات المستقبلية. من المهم أن نفكر في الأجزاء التي نتحكم فيها من الكود والأجزاء التي تتحكم فيها التبعيات الخارجية.
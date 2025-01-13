---
audio: true
lang: ar
layout: post
title: إعداد خادم الوكيل الخاص بك
translated: true
---

* لإعداد خادم، استخدم Outline Manager: [https://getoutline.org](https://getoutline.org).  
* تشمل مزودي الاستضافة الموصى بهم DigitalOcean، Google Cloud، Amazon Lightsail، Azure، Vultr، أو Linode. يُفضل استخدام المناطق في سنغافورة أو طوكيو. تجنب منطقة هونغ كونغ، حيث يتم حظر أدوات مثل ChatGPT وClaude هناك.  
* يمكن أن يتم حظر البروتوكولات مثل Shadowsocks وVMess وTrojan بسهولة.  
* استخدم Linode للهجرة السريعة للخادم.  
* قد تحتاج إلى نص برمجي لتجديد خادمك تلقائيًا كل يوم.  
* إذا تم حظر خادم الوكيل بواسطة جدار الحماية العظيم (GFW) أو واجهت مشاكل أخرى، يمكنك استخدام بطاقة SIM من China Telecom Macau لمشاركة بيانات الهاتف المحمول مع جهاز الكمبيوتر المحمول الخاص بك. وهذا يسمح لك بإعداد خادم جديد.  
* بالنسبة لخدمات السحابة مثل Google Cloud Platform، يتطلب تكوين خادم جديد وجود خادم وكيل موجود. ومع ذلك، يمكن إعداد مزودي مثل DigitalOcean أو Vultر مباشرة دون الحاجة إلى خادم وكيل.
* استخدم [Auto SS Config](https://github.com/lzwjava/auto-ss-config) لإنشاء وتحميل روابط الاشتراك في Shadowsocks أو Clash.
* استخدم وظيفة اللقطة (Snapshot) في Digital Ocean. إذا تم حظر عنوان IP للخادم، قم بإنشاء Droplet جديد من لقطة الخادم وقم بتشغيل `install.sh` مرة أخرى.
* استخدم وظيفة IP المحجوز في Digital Ocean. إذا تم حظر عنوان IP للخادم، قم بتعيين عنوان IP محجوز جديد.
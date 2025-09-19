---
audio: false
generated: false
image: true
lang: ar
layout: post
title: كيفية الوصول إلى جوجل
translated: true
---

نُشِر هذا المنشور أصلاً باللغة الصينية.

---

يغطي هذا الدرس ما يلي:

1. كيفية الوصول إلى الموقع الرسمي لخدمة VPN.
2. كيفية استخدام VPN على Windows.
3. مقدمة إلى برنامج Clash.
3. محاولة فتح Google و Twitter و YouTube و TikTok.

لنبدأ. إليك وصف مكتوب لكيفية تعليمي لـ Xiao Wang الوصول إلى Google.

سنستخدم منصة تُسمى "Summoner". الموقع الإلكتروني هو `https://zhshi.gitlab.io`.

<img src="/assets/images/google/zhs.png" alt="zhs" />

ومع ذلك، قد لا يكون الوصول إليه ممكنًا لأنه محظور بواسطة Great Firewall.

![zhs_user](/assets/images/google/zhs_user.png)

هذا ما يبدو عليه عند تسجيل الدخول.

هناك طريقتان بالفعل لتجاوز جدار الحماية. الأولى هي شراء خادم خاص بنا في الخارج. والثانية هي استخدام منصة VPN، والتي توفر العديد من عناوين الخوادم الخارجية.

"تجاوز جدار الحماية" يعني أولاً الوصول إلى خادم خارجي من داخل البلاد. يمكن لهذا الخادم الخارجي بعد ذلك الوصول إلى مواقع الويب المحظورة.

تُسمى هذه المنصة "Summoner". ولكن إذا كان الموقع الرسمي غير قابل للوصول، فكيف نحصل على عناوين الخوادم الخارجية التي توفرها؟ يستخدم Xiao Wang VPN لأول مرة، وأنا أعلمه عن بُعد. كيف يجب أن أعلمه؟

في هذه المرحلة، فكرت في تمكين جهاز كمبيوتر Xiao Wang الذي يعمل بنظام Windows من تجاوز جدار الحماية. سأقدم لـ Xiao Wang عنوانًا. ثم يمكن لـ Xiao Wang فتح موقع "Summoner" الإلكتروني، وتسجيل حساب، واستخدام عناوين الخوادم الخارجية ضمن حسابه الخاص.

![clash_win](/assets/images/google/clash_win.png)

![win_version](/assets/images/google/win_version.png)

بعد ذلك، تحقق مما إذا كان جهاز الكمبيوتر الخاص بك 64 بت أو 32 بت. إذا كان 64 بت، فقم بتنزيل `Clash.for.Windows.Setup.0.14.8.exe`. إذا كان 32 بت، فقم بتنزيل `Clash.for.Windows.Setup.0.14.8.ia32.exe`.

جهاز كمبيوتر Xiao Wang هو 64 بت. لكن التنزيل بطيء جدًا من جانبه. لذلك قمت بتنزيله على جهاز الكمبيوتر الخاص بي وأرسلته إليه عبر بريد QQ الإلكتروني.

قام بتنزيله من بريد QQ الإلكتروني، وقام بتثبيته، وفتحه.

![clash_win_exe](/assets/images/google/clash_win_exe.png)

أعطيتُه أولاً عنوان تكوين Summoner الخاص بي. سيقوم عنوان التكوين هذا بتنزيل ملف يحتوي على العديد من عناوين خادم VPN. ضمن `Profiles`، ألصق العنوان وانقر فوق `Download`.

![zhs_url](/assets/images/google/zhs_url.png)

انظر، لقد تم تنزيله. لاحظ التكوين الثاني أعلاه. هناك علامة اختيار خضراء أمامه، مما يشير إلى أننا نستخدم هذا التكوين.

![zhs_proxy](/assets/images/google/zhs_proxy.png)

بعد ذلك، افتح علامة التبويب `Proxies`. سترى بعض الأشياء هنا. هذه بعض من تكوينات `Clash`. ببساطة، هذا يعني أن مواقع الويب المحلية لن تستخدم VPN، بينما ستستخدم مواقع الويب الأجنبية ذلك.

لاحظ أن القيمة الحالية لـ `Proxy` هي `DIRECT`، وهذا يعني أنها اتصال مباشر. سنغيرها إلى عقدة.

![zhs_node](/assets/images/google/zhs_node.png)

لقد اخترنا عقدة `US Rose`.

![clash_system](/assets/images/google/clash_system.png)

بعد ذلك، قم بتبديل إعداد `System Proxy` لتمكينه. وهذا يعني تعيين برنامج `Clash` كطبقة بروكسي للنظام. بعد ذلك، سيتجه سير العمل للنظام أولاً إلى برنامج `Clash` ثم الوصول إلى الشبكة الخارجية.

<img src="/assets/images/google/google.png" alt="google" style="zoom:40%;" />

فتح Xiao Wang Google. بعد ذلك، حاول استخدام TikTok و YouTube و Twitter.

حسنًا، إذن Xiao Wang كان يستخدم حساب Summoner الخاص بي. كيف يسجل؟ يحتاج إلى فتح موقع Summoner الرسمي.

<img src="/assets/images/google/zhs_register.png" alt="zhs_register" style="zoom:50%;" />

بعد التسجيل، وجد أن إعادة الشحن لشراء الخدمات يتطلب بعض الخطوات. إليك لقطة شاشة لحسابي.

![zeng](/assets/images/google/zeng.png)

يقول إنه يحتاج إلى ربطه بـ Telegram.

<img src="/assets/images/google/zhs_telegram.png" alt="zhs_telegram" style="zoom:50%;" />

ذهب Xiao Wang إلى موقع Telegram الإلكتروني وقام بتنزيل إصدار سطح مكتب Telegram Windows.

![telegram](/assets/images/google/telegram.png)

بعد التنزيل والتثبيت، انتبه إلى النص أعلاه.

> بعد تثبيت Telegram والتسجيل، انقر للدردشة مع `小兔` أو `城主`، انسخ رمز الاستجابة السريعة أدناه وارسلها إليهم، أو `انقر هنا لنسخ الكود تلقائيًا وإرساله إلى Bot للربط`.

عندما تنقر على `小兔`، سيتم الانتقال تلقائيًا إلى برنامج `Telegram` وفتح نافذة دردشة مع `小兔`. ثم، أرسل لهم الكود.

![telegram_username](/assets/images/google/telegram_username.png)

ومع ذلك، فإن حساب `Telegram` الخاص بـ Xiao Wang مُسجل حديثًا وليس لديه `username`. إنه مثل استخدام WeChat بدون تعيين معرف WeChat.

ابحث عن قائمة Telegram وقم بتعيينه. ثم، أرسل الكود مرة أخرى للربط.

<img src="/assets/images/google/zhs_set.png" alt="zhs_set" style="zoom:50%;" />

بعد ذلك، يمكنك التبرع لدعمه. يمكنك البدء بإعادة شحن 30 يوان لمدة شهرين.

عد إلى الصفحة الرئيسية لـ Summoner. هنا، ابحث عن زر "انقر لنسخ"، واحصل على العنوان، ثم قم بتنزيل التكوين في برنامج `Clash`.

ثم يمكن لـ Xiao Wang حذف العنوان الذي أعطيته له. أصبح لدى Xiao Wang الآن حسابه الخاص على Summoner.

---
audio: false
generated: true
image: false
lang: ar
layout: post
model: openai/gpt-5
title: إزالة الشعب غير المرغوب فيها على جيت هاب
translated: true
type: note
---

فهمتك. النسخة المختصرة: لا يمكنك حذف فرع (fork) شخص آخر مباشرة. لكن يمكنك (أ) أن تطلب منه ذلك، (ب) تطهير المحتوى الحساس ومنع التسريبات المستقبلية، و (ج) استخدام الطرق الرسمية لـ GitHub (إشعار DMCA أو التواصل مع الدعم) عندما يكون ذلك مبررًا. إليك خطة واضحة بدون جداول تناسب المدونات الشخصية.

### 1) أولاً، راسل صاحب الفرع (أسرع طريقة)

افتح issue على الفرع الخاص بهم أو راسلهم عبر البريد الإلكتروني. إليك نموذج موجز يمكنك نسخه:

> مرحباً @tornadobaflocer — هذا الفرع يحتوي على ملاحظاتي الشخصية وسجل النشاطات. لقد نشرت المستودع فقط لاستخدام النطاق `lzwjava.github.io`، وليس لإعادة التوزيع. يرجى حذف هذا الفرع. أنا أجعل المصدر خاصًا وسأبقي فقط أصول الموقع المترجمة (compiled) عامة.
> شكرًا لتفهمك.

إذا قاموا بحذفه، فقد انتهيت. إذا لم يفعلوا، تابع.

### 2) افهم ما ستفعله GitHub وما لن تفعله

* حذف أو جعل مستودعك **العام** خاصًا **لا يزيل** الفروع العامة الموجودة. تبقى الفروع العامة عامة وتنفصل لتشكل "شبكة" خاصة بها. ([Stack Overflow][1])
* يمكنك فقط حذف فرع إذا كنت **مسؤولاً عن ذلك الفرع** (وهذا لا ينطبق عليك هنا). ([Stack Overflow][2])

### 3) إذا كان الفرع ينسخ محتواك المحمي بحقوق الطبع والنشر دون إذن

يمكنك تقديم إشعار إزالة DMCA إلى GitHub. إنه المسار الرسمي لإزالة المحتوى المنتهك للحقوق عبر الفروع. اقرأ السياسة ودليل "كية التقديم"؛ فهما يشرحان المعلومات التي يجب عليك تضمينها. ([GitHub Docs][3])

نصيحة: إذا لم يكن لمستودعك **أي ترخيص**، فإن حقوق الطبع والنشر الافتراضية تنطبق، مما يقوي طلب الإزالة (لم يكن للآخرين حقوق إعادة الاستخدام). يظل DMCA ساريًا حتى إذا كان لديك ترخيصًا متساهلًا، لكن الأمر يكون أكثر تعقيدًا.

### 4) امنع الفروع المستقبلية من كشف مصدرك

احتفظ **بالنطاق** عامًا، لكن احتفظ **بالمصدر** خاصًا من خلال تقسيم المستودعات:

* **مستودع المصدر الخاص** (مثل `blog-source`): محتوى Jekyll/Hugo الخاص بك، المسودات، الملاحظات، إعدادات التهيئة.
* **مستودع النشر العام** باسم **`lzwjava.github.io`**: يحتوي **فقط على الموقع المُنشأ** (HTML/CSS/JS). لا مسودات، لا تاريخ.

مواقع GitHub Pages تبقى عامة حتى عندما يكون المستودع خاصًا (باستثناء Enterprise Cloud مع Pages الخاص). لذا بالنسبة لمدونة شخصية، فإن إعداد "النشر فقط" باستخدام مستودعين هو النمط الآمن. ([GitHub Docs][4])

خيارات النشر التي يمكنك استخدامها اليوم:

* ادفع مخرجات `public/` أو `docs/` الخاصة بمولد المحتوى إلى `lzwjava.github.io`. ([Quarto][5])
* أو استخدم سير عمل GitHub Actions في `blog-source` يقوم ببناء المحتوى ودفعه بقوة (force-push) إلى الفرع الافتراضي لمستودع `lzwjava.github.io`. (الوثائق: اختر تدفق "النشر من فرع" أو "النشر باستخدام Actions"). ([GitHub Docs][6])

### 5) طهّر أي شيء حساس من السجل (سجلك وأي نسخ متبقية)

* غيّر أي رموز/مفاتيح token تم كشفها (افترض أنها معرضة للخطر).
* أعد كتابة السجل لإزالة الملفات/المسارات الحساسة باستخدام `git filter-repo` (توصي GitHub بهذا الآن) أو أداة BFG (أسرع للحالات الشائعة). ثم قم بالدفع القسري (force-push). ([GitHub Docs][7])

هذا لن يصلح فروع الآخرين بحد ذاته، لكنه ينظف مستودعك الأساسي ويدعم أي مطالبات بإزالة المحتوى من خلال إظهار أن المحتوى قد تمت إزالته.

### 6) تعزيز إضافي اختياري

* أضف ترخيصًا (LICENSE) واضحًا (إذا أردت تقييد إعادة الاستخدام صراحةً).
* أضف إخلاء مسؤولية في ملف README: "هذا المستودع موجود فقط لمخرجات الموقع المترجمة. لا تقم **بتفرعة** المصدر؛ فهو خاص."
* إذا استضفت محتوى في **منظمة** (organization)، يمكنك تعطيل تفرعة المستودعات الخاصة على مستوى المنظمة ولكل مستودع (لا يمنع استنساخ الكود العام، لكنه يساعد للمستودعات الخاصة). ([GitHub Docs][8])

---

## الخطوات التالية الملموسة (الترتيب العملي)

1. اطلب من @tornadobaflocer حذف الفرع (استخدم الرسالة أعلاه).
2. انقل مصدرك فورًا إلى مستودع **خاص** جديد (`blog-source`).
3. اجعل `lzwjava.github.io` مستودعًا **عامًا للنشر فقط** يحتوي فقط على الملفات المُنشأة. قم بتكوين Pages لينشر من فرعه/مجلده. ([GitHub Docs][6])
4. أعد كتابة سجل مستودعك العام القديم لإزالة الأجزاء الحساسة، ثم أرشفه أو احذفه. ([GitHub Docs][7])
5. إذا رفضوا وأردت إزالته، قدّم **إشعار إزالة DMCA** إلى GitHub. ([GitHub Docs][9])

إذا أردت، يمكنني صياغة إشعار DMCA بالتنسيق الدقيق الذي تطلبه GitHub، وسير عمل GitHub Actions بسيط يبني موقعك من `blog-source` ويدفع فقط الملفات المترجمة إلى `lzwjava.github.io`.

[1]: https://stackoverflow.com/questions/53052745/what-happens-to-the-forks-when-deleting-the-original-repository?utm_source=chatgpt.com "What happens to the forks when deleting the original repository?"
[2]: https://stackoverflow.com/questions/50280412/github-delete-a-fork-that-was-created-from-my-repo?utm_source=chatgpt.com "Github - Delete a fork that was created from my repo"
[3]: https://docs.github.com/articles/dmca-takedown-policy?utm_source=chatgpt.com "DMCA Takedown Policy"
[4]: https://docs.github.com/articles/creating-project-pages-manually?utm_source=chatgpt.com "Creating a GitHub Pages site"
[5]: https://quarto.org/docs/publishing/github-pages.html?utm_source=chatgpt.com "GitHub Pages"
[6]: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site?utm_source=chatgpt.com "Configuring a publishing source for your GitHub Pages site"
[7]: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository?utm_source=chatgpt.com "Removing sensitive data from a repository"
[8]: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-the-forking-policy-for-your-repository?utm_source=chatgpt.com "Managing the forking policy for your repository"
[9]: https://docs.github.com/en/site-policy/content-removal-policies/guide-to-submitting-a-dmca-takedown-notice?utm_source=chatgpt.com "Guide to Submitting a DMCA Takedown Notice"
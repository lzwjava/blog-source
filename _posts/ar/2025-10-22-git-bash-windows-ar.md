---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: جيت باش للويندوز موضَّح
translated: true
type: note
---

### كيف يعمل Git Bash

Git Bash (تحديدًا `git-bash.exe`) هو بيئة shell شبيهة بـ Unix خفيفة الوزن مُرفقة مع Git لنظام Windows. تم تصميمها لتوفير تجربة Bash مألوفة لمستخدمي Windows، مما يسمح لك بتشغيل أوامر Git وأدوات أخرى على نمط Unix في طرفية تحاكي shell متوافقة مع POSIX. إليك تفصيل لكيفية عملها:

1.  **المكونات الأساسية**:
    *   **محاكاة Bash**: في جوهرها، يشغل Git Bash نسخة محمولة من Bash (غلاف GNU Bourne-Again Shell). هذا ليس Bash أصليًا لنظام Windows بل طبقة محاكاة تترجم أوامر Unix إلى استدعاءات متوافقة مع Windows.
    *   **وقت تشغيل MSYS2**: تم بناء Git Bash على أساس MSYS2 (النسخة 2 من النظام الأدنى)، وهو منصة توزيع وبناء برمجيات لنظام Windows. يوفر MSYS2 مجموعة من أدوات ومكتبات GNU، مما يخلق بيئة خفيفة الوزن تشبه Linux دون الحاجة إلى آلة افتراضية كاملة أو WSL (نظام التشغيل الفرعي لنظام Windows لـ Linux).
    *   **ترجمة المسار**: يستخدم رابطًا ديناميكيًا ووقت تشغيل (من MSYS2) للتعامل مع مسارات الملفات. على سبيل المثال، يقوم بتعيين مسارات Windows (مثل `C:\Users`) إلى مسارات على نمط Unix (مثل `/c/Users`) بشكل شفاف، بحيث تعمل أوامر مثل `ls` أو `cd` كما هو متوقع. يتم ذلك عبر طبقة محاكاة POSIX تعترض استدعاءات النظام.

2.  **تدفق التنفيذ**:
    *   عند تشغيل `git-bash.exe`، يبدأ وقت تشغيل MSYS2، الذي يقوم بتهيئة Bash.
    *   تقوم متغيرات البيئة مثل `MSYSTEM` (يتم ضبطها على `MINGW64` افتراضيًا) بتكوين الجلسة لأدوات MinGW 64-bit، مما يؤثر على موجه الأوامر (مثل عرض "MINGW64" في عنوان الطرفية أو موجه PS1).
    *   يقوم بتحميل التكوين من ملفات مثل `/etc/bash.bashrc` (والذي يكون في الواقع موجودًا في دليل تثبيت Git، مثل `C:\Program Files\Git\etc\bash.bashrc`).
    *   أوامر Git متاحة لأن Git نفسه مُجمّع لهذه البيئة، ولكن يمكنك أيضًا تثبيت حزم إضافية عبر `pacman` الخاص بـ MSYS2 إذا لزم الأمر (على الرغم من أن Git Bash هو إصدار "مبسط" بدون إدارة حزم كاملة).

3.  **القيود والسلوكيات**:
    *   إنه ليس توزيعة Linux كاملة — فقد لا تعمل أدوات مثل `chmod` بشكل كامل على ملفات Windows بسبب أذونات NTFS.
    *   يعمل في نافذة وحدة تحكم (أو يمكن دمجه مع طرفيات مثل Windows Terminal) ويدعم ميزات مثل الإكمال التلقائي بالتبويب، السجل، والأسماء المستعارة.
    *   للتطوير، إنه رائع لسير عمل Git ولكنه غالبًا ما يُقترن بـ IDEs؛ للاحتياجات الأثقل لنظام Unix، فكر في استخدام WSL أو MSYS2 كامل.

### هل هو MinGW-w64؟

نعم، Git Bash مبني على MinGW-w64. MinGW-w64 (جنو البسيط لنظام Windows، 64-bit) هو سلسلة الأدوات المستخدمة لتجميع Bash والأدوات الأخرى في بيئة MSYS2 التي تشغل Git Bash. يشير "MINGW64" الذي تراه في موجه الأوامر أو شريط العنوان إلى أنه يعمل في النظام الفرعي MinGW-w64 الخاص بـ MSYS2، والذي يوفر دعمًا 64-bit للتطبيقات القابلة للتنفيذ الأصلية لنظام Windows مع محاكاة واجهات برمجة تطبيقات Unix. وهذا يميزه عن إعدادات MinGW القديمة 32-bit.

باختصار، يستفيد Git Bash من MinGW-w64 عبر MSYS2 لسد الفجوة بين أغلفة Windows وUnix، مما يجعله خيارًا محمولًا لا يتطلب تثبيتًا إضافيًا لمستخدمي Git.

[Why is "MINGW64" appearing on my Git bash?](https://stackoverflow.com/questions/32356595/why-is-mingw64-appearing-on-my-git-bash)  
[How to understand what is Shell, Terminal, MinGW, Bash, Git Bash etc](https://superuser.com/questions/1481401/how-to-understand-what-is-shell-terminal-mingw-bash-git-bash-etc)  
[Git for Windows](https://gitforwindows.org/)
---
audio: false
generated: true
lang: ar
layout: post
title: مشاكل تحميل مركز البرمجيات
translated: true
type: note
---

### النقاط الرئيسية
- يبدو من المحتمل أن services.msc هو أداة لإدارة خدمات Windows، والتحقق من خدمة sms agent host هنا أمر بالغ الأهمية لإصلاح مشكلات التنزيل.
- تشير الأبحاث إلى أن adaptiveclient هو على الأرجح Adaptiva Client Service، وهو جزء من أداة إدارة النظام التي قد تتعارض مع Configuration Manager، مما قد يؤثر على التنزيلات.
- تميل الأدلة إلى أن wmi performance adapter هو خدمة Windows لبيانات الأداء، والتي يستخدمها Configuration Manager ويجب أن تكون قيد التشغيل لكي يعمل بشكل صحيح.
- من المحتمل أن sms agent host هو خدمة عميل Configuration Manager، وهو ضروري لعمليات software center، ويجب أن يكون قيد التشغيل لكي تتم عملية التنزيل.

---

### ما هي هذه الخدمات ودورها؟
**نظرة عامة على services.msc**  
services.msc هو وحدة التحكم في الإدارة من Microsoft للخدمات، مما يسمح لك بعرض وإدارة جميع الخدمات على جهاز Windows الخاص بك. لإصلاح مشكلة تنزيل software center، يجب استخدامه للتأكد من أن خدمة sms agent host قيد التشغيل. إذا لم تكن قيد التشغيل، فقد يؤدي تشغيلها إلى حل المشكلة.

**شرح adaptiveclient**  
يشير adaptiveclient على الأرجح إلى Adaptiva Client Service، وهو جزء من برنامج إدارة الأنظمة من Adaptiva الذي يتكامل مع Configuration Manager ([موقع Adaptiva الرسمي](https://adaptiva.com)). إذا كانت هذه الخدمة تسبب تعارضًا في الموارد أو تداخلًا في الشبكة، فقد تؤثر على قدرة عميل Configuration Manager على تنزيل البرامج. قد تحتاج إلى إدارة أو إيقاف هذه الخدمة مؤقتًا لمعرفة ما إذا كان ذلك يحل المشكلة.

**تفاصيل wmi performance adapter**  
wmi performance adapter هو خدمة Windows توفر بيانات الأداء من خلال أداة Windows Management Instrumentation (WMI) ([استكشاف مشكلات أداء WMI وإصلاحها](https://learn.microsoft.com/en-us/troubleshoot/windows-server/system-management-components/scenario-guide-troubleshoot-wmi-performance-issues)). يستخدم Configuration Manager أداة WMI لمهام إدارية متنوعة، لذا فإن التأكد من تشغيل هذه الخدمة ضروري لكي يعمل Configuration Manager بشكل صحيح.

**دور sms agent host**  
sms agent host هو الخدمة التي تشغل عميل Configuration Manager على الجهاز ([وثائق Microsoft حول إدارة عميل Configuration Manager](https://learn.microsoft.com/en-us/mem/configmgr/core/clients/manage/manage-clients)). إنه ضروري لـ software center والنشرات. إذا لم يكن قيد التشغيل، فلن يتم المضي قدمًا في التنزيل.

### كيف ترتبط بإصلاح مشكلة التنزيل
لإصلاح مشكلة تنزيل software center العالقة عند 0%، اتبع هذه الخطوات:
- افتح services.msc وتأكد من أن خدمة sms agent host قيد التشغيل. إذا لم تكن قيد التشغيل، فقم بتشغيلها.
- تحقق مما إذا كانت خدمة wmi performance adapter قيد التشغيل، لأنها قد تكون مطلوبة لبعض وظائف Configuration Manager.
- إذا كان adaptiveclient قيد التشغيل ومن المحتمل أن يتداخل، ففكر في إيقافه أو طلب المساعدة الإضافية من دعم Adaptiva.
- إذا استمرت المشكلة، فتحقق من سجلات Configuration Manager للبحث عن أخطاء تتعلق بالتنزيل وتأكد من عدم وجود مشكلات في اتصال الشبكة بنقطة التوزيع. تحقق من تكوينات الحدود ونقطة التوزيع، وفكر في مسح ذاكرة التخزين المؤقت CCM أو إجراء إصلاح للعميل.

---

### ملاحظة المسح: تحليل شامل للخدمات وتأثيرها على تنزيلات Software Center

يقدم هذا القسم فحصًا مفصلاً للخدمات المذكورة—services.msc وadaptiveclient وwmi performance adapter وsms agent host—ودورها المحتمل في حل مشكلات تنزيل software Center العالقة عند 0% في سياق Microsoft Configuration Manager (SCCM). يستند التحليل إلى بحث مكثف ويهدف إلى تقديم فهم شامل للمحترفين في تكنولوجيا المعلومات والمستخدمين العاديين على حد سواء، مع ضمان تضمين جميع التفاصيل ذات الصلة من التحقيق.

#### فهم كل خدمة

**services.msc: وحدة تحكم إدارة الخدمات**  
services.msc ليس خدمة في حد ذاته ولكنه ملحق وحدة التحكم في الإدارة من Microsoft لإدارة خدمات Windows. يوفر واجهة رسومية لعرض وتشغيل وإيقاف وتكوين الخدمات، وهي عمليات خلفية أساسية لوظائف النظام والتطبيقات. في سياق إصلاح مشكلات تنزيل software center، تعد services.msc هي الأداة التي سيستخدمها المستخدمون للتحقق من حالة الخدمات الحرجة مثل sms agent host وwmi performance adapter. يعد التأكد من تشغيل هذه الخدمات خطوة أساسية في استكشاف الأخطاء وإصلاحها، حيث أن أي فشل في الخدمة يمكن أن يوقف عمليات Configuration Manager، بما في ذلك نشر البرامج.

**adaptiveclient: على الأرجح Adaptiva Client Service**  
لا يتوافق مصطلح "adaptiveclient" مباشرة مع أي خدمة أصلية في Configuration Manager، مما يؤدي إلى الاستنتاج بأنه يشير على الأرجح إلى Adaptiva Client Service، وهو جزء من مجموعة إدارة الأنظمة من Adaptiva ([موقع Adaptiva الرسمي](https://adaptiva.com)). تم تصميم برنامج Adaptiva، مثل OneSite، لتعزيز توزيع المحتوى وإدارته في SCCM، خاصة لإدارة التحديثات وصحة نقاط النهاية. خدمة عميل Adaptiva (AdaptivaClientService.exe) مسؤولة عن تنفيذ مهام مثل فحوصات الصحة وتحسين تسليم المحتوى. نظرًا لدمجها مع SCCM، إذا كانت هذه الخدمة تستهلك موارد شبكة مفرطة أو تتعارض مع عمليات عميل SCCM، فيمكن أن تسبب مشكلات تنزيل بشكل غير مباشر. على سبيل المثال، تشير مناقشات المنتدى إلى احتمال وجود تنافس على الموارد، مثل استخدام مساحة القرص لذاكرة التخزين المؤقت، مما قد يؤثر على أداء SCCM ([r/SCCM على Reddit: Adaptiva - Anyone have an Experience?](https://www.reddit.com/r/SCCM/comments/pb7325/adaptiva_anyone_have_an_experience/)).

**wmi performance adapter: خدمة Windows لبيانات الأداء**  
wmi performance adapter، أو WMI Performance Adapter (wmiApSrv)، هو خدمة Windows توفر معلومات مكتبة الأداء من موفري الأداء العالي لـ WMI للعملاء على الشبكة ([WMI Performance Adapter | موسوعة أمان Windows](https://www.windows-security.org/windows-service/wmi-performance-adapter-0)). يعمل فقط عند تنشيط أداة Performance Data Helper (PDH) وهو ضروري لجعل عدادات أداء النظام متاحة عبر واجهات برمجة تطبيقات WMI أو PDH. يعتمد Configuration Manager بشكل كبير على WMI لمهام مثل جمع الجرد ومراقبة صحة العميل ([استكشاف مشكلات أداء WMI وإصلاحها](https://learn.microsoft.com/en-us/troubleshoot/windows-server/system-management-components/scenario-guide-troubleshoot-wmi-performance-issues)). إذا لم تكن هذه الخدمة قيد التشغيل، فقد تعطل قدرة SCCM على جمع البيانات اللازمة، مما قد يؤثر بشكل غير مباشر على تنزيلات software center، خاصة إذا كانت بيانات الأداء مطلوبة لقرارات النشر.

**sms agent host: خدمة عميل Configuration Manager**  
خدمة sms agent host، والمعروفة أيضًا باسم CcmExec.exe، هي الخدمة الأساسية لعميل Configuration Manager المثبت على الأجهزة المدارة ([وثائق Microsoft حول إدارة عميل Configuration Manager](https://learn.microsoft.com/en-us/mem/configmgr/core/clients/manage/manage-clients)). تتعامل مع الاتصال بخادم SCCM، وتدير نشر البرامج، وتجمع الجرد، وتسهل تفاعلات المستخدم من خلال software center. هذه الخدمة ضرورية لأي نشاط نشر، بما في ذلك تنزيل وتثبيت التطبيقات أو التحديثات. إذا لم تكن قيد التشغيل أو واجهت مشكلات، كما هو الحال في الحالات التي تتوقف فيها عن الاستجابة بسبب مشكلات توقيت ([تتوقف خدمة Systems Management Server (SMS) Agent Host (Ccmexec.exe) عن الاستجابة على كمبيوتر عميل System Center Configuration Manager 2007 SP2](https://support.microsoft.com/en-us/topic/the-systems-management-server-sms-agent-host-service-ccmexec-exe-stops-responding-on-a-system-center-configuration-manager-2007-sp2-client-computer-6bd93824-d9ac-611f-62fc-eabc1ba20d47))، فإنها تمنع مباشرة المضي قدمًا في التنزيلات، مما يؤدي إلى حالة التعلق عند 0%.

#### ربط هذه الخدمات بإصلاح مشكلات تنزيل Software Center عند 0%

تشير مشكلة تنزيل software center العالقة عند 0% إلى أن عملية التنزيل لم تبدأ أو أنها تفشل في البداية، وهي مشكلة شائعة في بيئات SCCM غالبًا ما ترتبط بمشكلات في العميل أو الشبكة أو جانب الخادم. إليك كيف ترتبط كل خدمة باستكشاف الأخطاء وإصلاحها وحلها بشكل محتمل:

- **دور services.msc**: باعتباره وحدة التحكم في الإدارة، تعد services.msc هي الأداة الأولى للتحقق من حالة sms agent host وwmi performance adapter. إذا توقف sms agent host، فإن إعادة تشغيله عبر services.msc هو إجراء مباشر لحل المشكلة بشكل محتمل. وبالمثل، فإن التأكد من تشغيل wmi performance adapter يدعم عمليات SCCM المعتمدة على WMI. هذه الخطوة حاسمة حيث غالبًا ما يوصي منشورات المنتدى وأدلة استكشاف الأخطاء وإصلاحها بالتحقق من حالة الخدمة ([تعلق تنزيل تطبيق SCCM عند 0% في Software Center](https://www.prajwaldesai.com/sccm-application-download-stuck/)).

- **التأثير المحتمل لـ adaptiveclient**: نظرًا لدمج Adaptiva مع SCCM، يمكن أن تكون خدمة adaptiveclient عاملاً إذا كانت تستهلك عرض النطاق الترددي للشبكة أو مساحة القرص، مما قد يتعارض مع عملية تنزيل محتوى SCCM. على سبيل المثال، قد يتداخل توزيع المحتوى من نظير إلى نظير من Adaptiva إذا لم يتم تكوينه بشكل صحيح، كما هو موضح في تجارب المستخدمين حيث يمكن أن تفشل عمليات نقل المحتوى عبر Adaptiva وتتطلب التنظيف ([r/SCCM على Reddit: Adaptiva - Anyone have an Experience?](https://www.reddit.com/r/SCCM/comments/pb7325/adaptiva_anyone_have_an_experience/)). إذا كانت التنزيلات عالقة، فقد يساعد إيقاف هذه الخدمة أو إدارتها مؤقتًا في عزل المشكلة، على الرغم من أنه يجب على المستخدمين الرجوع إلى وثائق Adaptiva لممارسات الإدارة الآمنة.

- **أهمية wmi performance adapter**: على الرغم من عدم ذكرها مباشرة في معظم أدلة استكشاف الأخطاء وإصلاحها الخاصة بالتعلق عند 0%، فإن دور wmi performance adapter في توفير بيانات الأداء حيوي لـ SCCM. إذا لم تكن قيد التشغيل، فقد تواجه SCCM صعوبات في مراقبة صحة العميل أو أدائه، مما قد يؤثر بشكل غير مباشر على عمليات النشر. يمكن أن يمنع التأكد من ضبطها على التشغيل التلقائي وتشغيلها تضخم السجلات وضغط النظام، كما هو موضح في تقارير دورات البدء/الإيقاف المتكررة التي تطلقها أدوات المراقبة مثل SCCM ([لماذا سجل أحداث النظام الخاص بي مليء برسائل WMI Performance Adapter؟](https://serverfault.com/questions/108829/why-is-my-system-event-log-full-of-wmi-performance-adapter-messages)).

- **الدور الحاسم لـ sms agent host**: هذه الخدمة هي قلب المشكلة. إذا لم تكن قيد التشغيل، فلا يمكن لـ software center بدء التنزيلات، مما يؤدي إلى حالة التعلق عند 0%. غالبًا ما تتضمن خطوات استكشاف الأخطاء وإصلاحها إعادة تشغيل هذه الخدمة، والتحقق من السجلات مثل CcmExec.log للبحث عن أخطاء، والتأكد من اتصال الشبكة بنقطة التوزيع ([كية إعادة تشغيل خدمة SMS Agent Host | إعادة تشغيل عميل SCCM](https://www.prajwaldesai.com/restart-sms-agent-host-service-sccm-client/)). يمكن أن تساهم مشكلات مثل ارتفاع استخدام وحدة المعالجة المركزية أو الفشل في البدء بسبب مشكلات WMI أيضًا، مما يتطلب مزيدًا من التحقيق في إعدادات العميل والسجلات.

#### خطوات استكشاف الأخطاء وإصلاحها التفصيلية

لمعالجة مشكلة التنزيل العالقة عند 0% بشكل منهجي، ضع في اعتبارك الخطوات التالية، مع دمج الخدمات المذكورة:

1.  **التحقق من حالة الخدمة عبر services.msc**:
    *   افتح services.msc وتحقق مما إذا كان sms agent host (CcmExec.exe) قيد التشغيل. إذا كان متوقفًا، فقم بتشغيله وراقب ما إذا كانت التنزيلات تستمر.
    *   تأكد من أن wmi performance adapter قيد التشغيل أو مضبوط على البدء التلقائي لتجنب انقطاعات عمليات SCCM المعتمدة على WMI.

2.  **إدارة adaptiveclient إذا كان مشتبهًا به**:
    *   إذا كان adaptiveclient قيد التشغيل، فتحقق من استخدام الموارد (وحدة المعالجة المركزية، الذاكرة، الشبكة) عبر Task Manager. إذا كان مرتفعًا، ففكر في إيقافه مؤقتًا واختبار التنزيلات مرة أخرى. راجع وثائق Adaptiva للإجراءات الآمنة ([Adaptiva | الأسئلة الشائعة](https://adaptiva.com/faq)).

3.  **التحقق من سجلات Configuration Manager**:
    *   راجع السجلات مثل DataTransferService.log وContentTransferManager.log وLocationServices.log للبحث عن أخطاء تشير إلى سبب عدم بدء التنزيل. ابحث عن مشكلات مثل فشل اتصالات DP أو سوء تكوين الحدود ([تعلق تثبيت التطبيق عند التنزيل 0% في Software Center](https://learn.microsoft.com/en-us/answers/questions/264523/application-installation-stuck-at-downloading-0-in)).

4.  **ضمان اتصال الشبكة ونقطة التوزيع**:
    *   تحقق من أن العميل داخل الحدود الصحيحة ويمكنه الوصول إلى نقطة التوزيع. تحقق من إعدادات جدار الحماية وسياسات الشبكة، خاصة إذا كان adaptiveclient يؤثر على استخدام الشبكة.

5.  **إجراء صيانة العميل**:
    *   امسح ذاكرة التخزين المؤقت CCM (C:\Windows\CCMCache) وأعد تشغيل خدمة sms agent host. فكر في إصلاح العميل أو إعادة تثبيته إذا استمرت المشكلات، كما هو مقترح في مناقشات المنتدى ([r/SCCM على Reddit: Software Center Apps Downloading Stuck At 0% Complete](https://www.reddit.com/r/SCCM/comments/14z25vp/software_center_apps_downloading_stuck_at_0/)).

#### جداول للتوضيح

فيما يلي جدول يلخص الخدمات وتأثيرها المحتمل على مشكلة التنزيل:

| الخدمة                  | الوصف                                                                 | التأثير المحتمل على مشكلة التنزيل                     | الإجراء المتخذ                                     |
|-------------------------|---------------------------------------------------------------------|------------------------------------------------------|----------------------------------------------------|
| services.msc           | وحدة تحكم الإدارة لخدمات Windows                                    | تُستخدم للتحقق من الخدمات الحرجة مثل sms agent host وتشغيلها | افتح وتحقق من حالة sms agent host و wmi performance adapter |
| adaptiveclient         | على الأرجح Adaptiva Client Service، جزء من البرنامج المتكامل مع SCCM من Adaptiva | قد يسبب تعارضًا في الموارد أو الشبكة                  | تحقق من الاستخدام، فكر في الإيقاف المؤقت           |
| wmi performance adapter | يوفر بيانات الأداء عبر WMI، يستخدمها SCCM                          | قد يعطل عمليات SCCM إذا لم يكن قيد التشغيل            | تأكد من التشغيل، اضبط على تلقائي إذا لزم الأمر     |
| sms agent host         | خدمة عميل Configuration Manager، تتعامل مع النشرات                  | يجب أن تكون قيد التشغيل لكي تتم عملية التنزيل         | شغّلها إذا كانت متوقفة، تحقق من السجلات للبحث عن أخطاء |

جدول آخر لخطوات استكشاف الأخطاء وإصلاحها:

| رقم الخطوة | الإجراء                                     | الغرض                                                 |
|------------|---------------------------------------------|-------------------------------------------------------|
| 1          | التحقق من حالة sms agent host عبر services.msc | تأكد من أن خدمة عميل SCCM الأساسية قيد التشغيل        |
| 2          | التأكد من تشغيل wmi performance adapter    | دعم عمليات SCCM المعتمدة على WMI                      |
| 3          | إدارة adaptiveclient إذا كان استخدام الموارد مرتفعًا | عزل التعارضات المحتملة مع تنزيلات SCCM               |
| 4          | مراجعة سجلات Configuration Manager          | تحديد أخطاء محددة مثل مشكلات اتصال DP                |
| 5          | التحقق من الشبكة والحدود                     | تأكد من أن العميل يمكنه الوصول إلى نقطة التوزيع       |
| 6          | مسح ذاكرة التخزين المؤقت CCM، إعادة تشغيل العميل | حل مشكلات ذاكرة التخزين المؤقت أو تكوين العميل المحتملة|

#### تفصيل غير متوقع: دور Adaptiva

التفصيل غير المتوقع هو الدور المحتمل لبرنامج Adaptiva، والذي لا يتم مناقشته بشكل شائع في استكشاف أخطاء SCCM القياسية وإصلاحها ولكن يمكن أن يكون مهمًا إذا كان مثبتًا. قد يؤدي تكامله مع SCCM لتوزيع المحتوى وفحوصات الصحة إلى إدخال تعقيدات، خاصة في البيئات التي تحتوي على كلا النظامين، مما قد يؤدي إلى تنافس على الموارد أو مشكلات شبكة تؤثر على التنزيلات.

#### الخلاصة

يسلط هذا التحليل الشامل الضوء على أهمية التأكد من تشغيل خدمتي sms agent host وwmi performance adapter، باستخدام services.msc كأداة إدارة. قد يؤثر adaptiveclient، وهو على الأرجح خدمة Adaptiva، بشكل غير مباشر على التنزيلات من خلال التعارضات في الموارد أو الشبكة، مما يتطلب إدارة دقيقة. من خلال اتباع خطوات استكشاف الأخطاء وإصلاحها التفصيلية والاستفادة من الجداول المقدمة، يمكن للمستخدمين معالجة مشكلة تنزيل software center العالقة عند 0% بشكل منهجي، مما يضمن عملية حل شاملة.

---

### الاقتباسات الرئيسية
- [موقع Adaptiva الرسمي، حلول شاملة لإدارة نقاط النهاية](https://adaptiva.com)
- [وثائق Microsoft حول إدارة عميل Configuration Manager، إدارة العملاء في ConfigMgr](https://learn.microsoft.com/en-us/mem/configmgr/core/clients/manage/manage-clients)
- [استكشاف مشكلات أداء WMI وإصلاحها، دليل لحل مشكلات أداء WMI](https://learn.microsoft.com/en-us/troubleshoot/windows-server/system-management-components/scenario-guide-troubleshoot-wmi-performance-issues)
- [WMI Performance Adapter، مدخل موسوعة خدمة Windows](https://www.windows-security.org/windows-service/wmi-performance-adapter-0)
- [تعلق تنزيل تطبيق SCCM عند 0% في Software Center، دليل استكشاف الأخطاء وإصلاحها](https://www.prajwaldesai.com/sccm-application-download-stuck/)
- [r/SCCM على Reddit: Adaptiva - Anyone have an Experience?، تجارب المستخدمين مع Adaptiva](https://www.reddit.com/r/SCCM/comments/pb7325/adaptiva_anyone_have_an_experience/)
- [كيفية إعادة تشغيل خدمة SMS Agent Host | إعادة تشغيل عميل SCCM، دليل خطوة بخطوة](https://www.prajwaldesai.com/restart-sms-agent-host-service-sccm-client/)
- [تتوقف خدمة Systems Management Server (SMS) Agent Host (Ccmexec.exe) عن الاستجابة على كمبيوتر عميل System Center Configuration Manager 2007 SP2، مشكلة وحل معروف](https://support.microsoft.com/en-us/topic/the-systems-management-server-sms-agent-host-service-ccmexec-exe-stops-responding-on-a-system-center-configuration-manager-2007-sp2-client-computer-6bd93824-d9ac-611f-62fc-eabc1ba20d47)
- [لماذا سجل أحداث النظام الخاص بي مليء برسائل WMI Performance Adapter؟، مناقشة حول سلوك خدمة WMI](https://serverfault.com/questions/108829/why-is-my-system-event-log-full-of-wmi-performance-adapter-messages)
- [تعلق تثبيت التطبيق عند التنزيل 0% في Software Center، مناقشة منتدى Microsoft Q&A](https://learn.microsoft.com/en-us/answers/questions/264523/application-installation-stuck-at-downloading-0-in)
- [r/SCCM على Reddit: Software Center Apps Downloading Stuck At 0% Complete، نصائح استكشاف الأخطاء وإصلاحها من المجتمع](https://www.reddit.com/r/SCCM/comments/14z25vp/software_center_apps_downloading_stuck_at_0/)
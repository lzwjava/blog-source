---
audio: false
generated: false
lang: ar
layout: post
title: مركز البرمجيات مشاكل التحميل
translated: true
---

### نقاط رئيسية
- يبدو أن services.msc هو أداة لإدارة خدمات ويندوز، و التحقق من خدمة sms agent host هنا هو حاسم لتعديل مشاكل التنزيل.
- تشير الأبحاث إلى أن adaptiveclient هو محتمل أن يكون خدمة Adaptiva Client، جزء من أداة إدارة النظام التي قد تتعارض مع Configuration Manager، مما قد يؤثر على التنزيلات.
- يشير الدليل إلى أن wmi performance adapter هو خدمة ويندوز لتقديم بيانات الأداء، التي يستخدمها Configuration Manager ويجب أن تكون تعمل بشكل صحيح.
- sms agent host هو محتمل أن يكون خدمة Configuration Manager client، حاسمة لعملية مركز البرامج، ويجب أن تكون تعمل لتتمكن التنزيلات من الاستمرار.

---

### ما هذها الخدمات و دورها؟
**مقدمة services.msc**
services.msc هو وحدة تحكم إدارة Microsoft للخدمات، مما يسمح لك بملاحظة وإدارة جميع الخدمات على جهاز ويندوز الخاص بك. لتعديل مشكلة تنزيل مركز البرامج، يجب عليك استخدامه لضمان تشغيل خدمة sms agent host. إذا لم تكن تعمل، قد يساعدك تشغيلها على حل المشكلة.

**شرح adaptiveclient**
adaptiveclient يشير محتمل إلى خدمة Adaptiva Client، جزء من برنامج إدارة الأنظمة الخاص بAdaptiva الذي يتكامل مع Configuration Manager ([موقع Adaptiva الرسمي](https://adaptiva.com)). إذا كانت هذه الخدمة تسبب تعارض الموارد أو تعارض الشبكة، فقد تؤثر على قدرة Configuration Manager client على تنزيل البرامج. قد تحتاج إلى إدارة أو إيقاف هذه الخدمة مؤقتًا لمعرفة إذا كان ذلك يحل المشكلة.

**تفاصيل wmi performance adapter**
wmi performance adapter هو خدمة ويندوز تقدم بيانات الأداء من خلال Windows Management Instrumentation (WMI) ([إصلاح مشاكل أداء WMI](https://learn.microsoft.com/en-us/troubleshoot/windows-server/system-management-components/scenario-guide-troubleshoot-wmi-performance-issues)). Configuration Manager يستخدم WMI لمهام إدارة مختلفة، لذا يجب التأكد من تشغيل هذه الخدمة لضمان عمل Configuration Manager بشكل صحيح.

**دور sms agent host**
sms agent host هو الخدمة التي تعمل على Configuration Manager client على الجهاز ([توثيق Microsoft حول إدارة Configuration Manager Client](https://learn.microsoft.com/en-us/mem/configmgr/core/clients/manage/manage-clients)). هي حاسمة لعملية مركز البرامج والتوزيعات. إذا لم تكن تعمل، فلن تستمر التنزيلات.

### كيف تتصل هذه الخدمات بإصلاح مشكلة التنزيل
لتعديل مشكلة تنزيل مركز البرامج المتوقف عند 0٪، اتبع هذه الخطوات:
- افتح services.msc و تأكد من تشغيل خدمة sms agent host. إذا لم تكن تعمل، قم ببدءها.
- تحقق من تشغيل خدمة wmi performance adapter، فقد تكون مطلوبة لمهام Configuration Manager المختلفة.
- إذا كانت adaptiveclient تعمل و قد تكون تسبب تعارضًا، فاعتبر إيقافها أو طلب مساعدة إضافية من دعم Adaptiva.
- إذا استمرت المشكلة، تحقق من سجلات Configuration Manager بحثًا عن أخطاء تتعلق بالتنزيل و تأكد من عدم وجود مشاكل اتصال الشبكة إلى نقطة التوزيع. تحقق من حدود التوزيع و تكوين نقطة التوزيع، و اعتبر مسح CCM cache أو إجراء إصلاح للعميل.

---

### ملاحظة الاستطلاع: تحليل شامل للخدمات و تأثيرها على تنزيل مركز البرامج

يقدم هذا القسم فحصًا مفصلًا للخدمات المذكورة - services.msc، adaptiveclient، wmi performance adapter، و sms agent host - و أدوارها المحتملة في حل مشاكل تنزيل مركز البرامج المتوقف عند 0٪ في سياق Microsoft Configuration Manager (SCCM). يعتمد التحليل على بحث شامل ويهدف إلى تقديم فهم شامل للمهنيين في مجال تكنولوجيا المعلومات والمستخدمين العاديين، مما يضمن تضمين جميع التفاصيل ذات الصلة من التحقيق.

#### فهم كل خدمة

**services.msc: وحدة تحكم إدارة الخدمات**
services.msc ليست خدمة بنفسها، بل هي وحدة تحكم إدارة Microsoft للخدمات. توفر واجهة رسومية لمشاهدة، بدء، إيقاف، وتكوين الخدمات، والتي هي عمليات خلفية حاسمة للوظائف النظامية والتطبيقات. في سياق إصلاح مشاكل تنزيل مركز البرامج، services.msc هي الأداة التي يستخدمها المستخدمون للتحقق من حالة الخدمات الحاسمة مثل sms agent host و wmi performance adapter. التأكد من تشغيل هذه الخدمات هو خطوة أساسية في إصلاح الأخطاء، حيث يمكن أن يتوقف أي فشل في الخدمة عن تشغيل Configuration Manager، بما في ذلك توزيع البرامج.

**adaptiveclient: محتمل أن يكون خدمة Adaptiva Client**
لم يتم تحديد "adaptiveclient" مباشرة مع أي خدمة Configuration Manager الأصلية، مما يؤدي إلى الاستنتاج أنه محتمل أن يشير إلى خدمة Adaptiva Client، جزء من مجموعة إدارة الأنظمة الخاصة بAdaptiva ([موقع Adaptiva الرسمي](https://adaptiva.com)). برامج Adaptiva مثل OneSite مصممة لتحسين قدرات SCCM في توزيع المحتوى وإدارة المحتوى، خاصة في إدارة التحديثات و صحة النقطة النهائية. Adaptiva Client Service (AdaptivaClientService.exe) مسؤولة عن تنفيذ مهام مثل فحص الصحة و تحسين توزيع المحتوى. نظرًا لتكاملها مع SCCM، إذا كانت هذه الخدمة تستهلك موارد الشبكة أو تتعارض مع عمليات SCCM client، فقد تؤثر بشكل غير مباشر على تنزيل البرامج. على سبيل المثال، تشير مناقشات المنتديات إلى احتمال تعارض الموارد مثل استخدام مساحة القرص للمخزن المؤقت، مما يمكن أن يؤثر على أداء SCCM ([r/SCCM على Reddit: Adaptiva - هل لديك أي تجربة؟](https://www.reddit.com/r/SCCM/comments/pb7325/adaptiva_anyone_have_an_experience/)).

**wmi performance adapter: خدمة ويندوز لتقديم بيانات الأداء**
wmi performance adapter، أو WMI Performance Adapter (wmiApSrv)، هو خدمة ويندوز تقدم معلومات مكتبة الأداء من WMI high-performance providers إلى العملاء على الشبكة ([WMI Performance Adapter | موسوعة أمن ويندوز](https://www.windows-security.org/windows-service/wmi-performance-adapter-0)). يعمل فقط عندما يتم تفعيل Performance Data Helper (PDH) ويعد حاسماً لتقديم مؤشرات الأداء النظامية عبر WMI أو APIs PDH. Configuration Manager يعتمد بشكل كبير على WMI لمهام مثل جمع المخزون و مراقبة صحة العميل ([إصلاح مشاكل أداء WMI](https://learn.microsoft.com/en-us/troubleshoot/windows-server/system-management-components/scenario-guide-troubleshoot-wmi-performance-issues)). إذا لم تكن هذه الخدمة تعمل، فقد تتسبب في اضطراب SCCM في جمع البيانات اللازمة، مما قد يؤثر بشكل غير مباشر على تنزيل مركز البرامج، خاصة إذا كانت البيانات اللازمة للقرارات التوزيعية.

**sms agent host: خدمة Configuration Manager Client**
sms agent host service، المعروف أيضًا باسم CcmExec.exe، هو الخدمة الأساسية للعميل Configuration Manager المثبته على الأجهزة المدارة ([توثيق Microsoft حول إدارة Configuration Manager Client](https://learn.microsoft.com/en-us/mem/configmgr/core/clients/manage/manage-clients)). يدير التواصل مع SCCM server، يدير توزيع البرامج، يجمع المخزون، ويسهل التفاعل مع المستخدمين من خلال مركز البرامج. هذه الخدمة حاسمة لأي نشاط توزيع، بما في ذلك تنزيل وتثبيت التطبيقات أو التحديثات. إذا لم تكن تعمل أو واجهت مشاكل، كما في الحالات التي توقف فيها بسبب مشاكل زمنية ([The Systems Management Server (SMS) Agent Host service (Ccmexec.exe) stops responding on a System Center Configuration Manager 2007 SP2 client computer](https://support.microsoft.com/en-us/topic/the-systems-management-server-sms-agent-host-service-ccmexec-exe-stops-responding-on-a-system-center-configuration-manager-2007-sp2-client-computer-6bd93824-d9ac-611f-62fc-eabc1ba20d47)), فإنها تمنع التنزيلات من الاستمرار، مما يؤدي إلى حالة 0٪ المتوقف.

#### ربط هذه الخدمات بإصلاح مشاكل تنزيل مركز البرامج عند 0%

تؤكد مشكلة تنزيل مركز البرامج المتوقف عند 0٪ على أن عملية التنزيل لم تبدأ أو فشلت في البداية، مشكلة شائعة في بيئات SCCM غالبًا ما تكون مرتبطة بمشاكل العميل أو الشبكة أو الخادم. إليك كيف تتصل كل خدمة بإصلاح هذه المشكلة:

- **دور services.msc**: كواجهة إدارة، services.msc هي الأداة الأولى للتحقق من حالة sms agent host و wmi performance adapter. إذا كانت sms agent host متوقفة، يمكن أن يكون إعادة تشغيلها عبر services.msc خطوة مباشرة لتعديل المشكلة. كذلك، التأكد من تشغيل wmi performance adapter يدعم عمليات SCCM التي تعتمد على WMI. هذه الخطوة حاسمة حيث يوصي العديد من مناقشات المنتديات و دليلات إصلاح الأخطاء بالتحقق من حالة الخدمة ([SCCM Application Download Stuck at 0% in Software Center](https://www.prajwaldesai.com/sccm-application-download-stuck/)).

- **تأثير adaptiveclient المحتمل**: نظرًا لتكامل Adaptiva مع SCCM، قد تكون خدمة adaptiveclient عاملًا إذا كانت تستهلك عرض النطاق الترددي أو مساحة القرص، مما قد يسبب تعارضًا مع عملية تنزيل SCCM. على سبيل المثال، يمكن أن يسبب توزيع المحتوى من طرف إلى طرف في Adaptiva فشلًا إذا لم يتم تهيئته بشكل صحيح، كما هو موضح في تجارب المستخدمين حيث يمكن أن تفشل نقلات المحتوى عبر Adaptiva وتطلب تنظيف ([r/SCCM على Reddit: Adaptiva - هل لديك أي تجربة؟](https://www.reddit.com/r/SCCM/comments/pb7325/adaptiva_anyone_have_an_experience/)). إذا كانت التنزيلات متوقفة، يمكن أن يساعد إيقاف أو إدارة هذه الخدمة مؤقتًا في عزل المشكلة، ولكن يجب على المستخدمين الاستشارة الوثائق الرسمية Adaptiva للحصول على إجراءات إدارة آمنة.

- **أهمية wmi performance adapter**: على الرغم من عدم ذكرها في معظم دليلات إصلاح التنزيل المتوقف عند 0٪، فإن دور wmi performance adapter في تقديم بيانات الأداء حاسمة للSCCM. إذا لم تكن تعمل، قد يواجه SCCM صعوبة في مراقبة صحة العميل أو الأداء، مما قد يؤثر بشكل غير مباشر على عمليات التوزيع. التأكد من تشغيلها و تعيينها لتشغيل تلقائي يمكن أن يمنع زيادة السجلات و الضغط على النظام، كما هو موضح في تقارير دورات التشغيل المتكررة التي يتم تفعيلها بواسطة أدوات مراقبة مثل SCCM ([Why is my System event log full of WMI Performance Adapter messages?](https://serverfault.com/questions/108829/why-is-my-system-event-log-full-of-wmi-performance-adapter-messages)).

- **دور sms agent host الحاسم**: هذه الخدمة في قلب المشكلة. إذا لم تكن تعمل، فلن يتمكن مركز البرامج من بدء التنزيلات، مما يؤدي إلى حالة 0٪ المتوقف. تشمل خطوات إصلاح الأخطاء عادةً إعادة تشغيل هذه الخدمة، التحقق من سجلات مثل CcmExec.log بحثًا عن أخطاء، و التأكد من اتصال الشبكة إلى نقطة التوزيع ([How To Restart SMS Agent Host Service | Restart SCCM Client](https://www.prajwaldesai.com/restart-sms-agent-host-service-sccm-client/)). يمكن أن تسبب مشاكل مثل استخدام وحدة المعالجة المركزية العالي أو فشل في البدء بسبب مشاكل WMI أيضًا، مما يتطلب تحقيقًا إضافيًا في إعدادات العميل و السجلات.

#### خطوات إصلاح مفصلة

لتعالج النظامية مشكلة التنزيل المتوقف عند 0٪، اعتمد على الخطوات التالية، متضمنة الخدمات المذكورة:

1. **تحقق من حالة الخدمة عبر services.msc**:
   - افتح services.msc و تحقق من تشغيل sms agent host (CcmExec.exe). إذا كانت متوقفة، قم ببدءها و راقب إذا كانت التنزيلات تستمر.
   - تأكد من تشغيل wmi performance adapter أو تعيينها لتشغيل تلقائي لمنع انقطاع في عمليات SCCM التي تعتمد على WMI.

2. **إدارة adaptiveclient إذا كان مشتبهًا به**:
   - إذا كانت adaptiveclient تعمل، تحقق من استخدام الموارد (CPU، الذاكرة، الشبكة) عبر Task Manager. إذا كانت عالية، فاعتبر إيقافها مؤقتًا و اختبار التنزيلات مرة أخرى. استشير وثائق Adaptiva للحصول على إجراءات آمنة ([Adaptiva | FAQ](https://adaptiva.com/faq)).

3. **تحقق من سجلات Configuration Manager**:
   - مراجعة السجلات مثل DataTransferService.log، ContentTransferManager.log، و LocationServices.log بحثًا عن أخطاء تشير إلى سبب عدم بدء التنزيل. ابحث عن مشاكل مثل فشل اتصال DP أو خطأ في تكوين الحدود ([Application Installation stuck at Downloading 0% in Software Center](https://learn.microsoft.com/en-us/answers/questions/264523/application-installation-stuck-at-downloading-0-in)).

4. **تأكد من اتصال الشبكة و نقطة التوزيع**:
   - تأكد من أن العميل داخل حدود صحيحة و يمكن الوصول إلى نقطة التوزيع. تحقق من إعدادات الحائط الناري و سياسات الشبكة، خاصة إذا كانت adaptiveclient تؤثر على استخدام الشبكة.

5. **أداء صيانة العميل**:
   - مسح CCM cache (C:\Windows\CCMCache) و إعادة تشغيل خدمة sms agent host. اعتبر إصلاح العميل أو إعادة تثبيته إذا استمرت المشاكل، كما هو موضح في مناقشات المنتديات ([r/SCCM على Reddit: Software Center Apps Downloading Stuck At 0% Complete](https://www.reddit.com/r/SCCM/comments/14z25vp/software_center_apps_downloading_stuck_at_0/)).

#### الجداول للوضوح

جدول يوضح الخدمات و تأثيرها المحتمل على مشكلة التنزيل:

| الخدمة               | الوصف                                                                 | التأثير المحتمل على مشكلة التنزيل                     | الخطوة التي يجب اتخاذها                                      |
|-----------------------|-----------------------------------------------------------------------------|-------------------------------------------------------|----------------------------------------------------|
| services.msc          | وحدة تحكم إدارة الخدمات                                    | تستخدم للتحقق من حالة sms agent host و wmi performance adapter | افتح و تحقق من حالة sms agent host و wmi performance adapter |
| adaptiveclient        | محتمل أن يكون خدمة Adaptiva Client، جزء من برامج Adaptiva المتكاملة مع SCCM | قد يسبب تعارض الموارد أو الشبكة               | تحقق من الاستخدام، اعتبر إيقافها مؤقتًا         |
| wmi performance adapter | تقدم بيانات الأداء عبر WMI، يستخدمها SCCM                          | قد يسبب اضطراب SCCM إذا لم تكن تعمل          | تأكد من تشغيلها، اعتمد على تشغيل تلقائي إذا لزم الأمر         |
| sms agent host        | خدمة Configuration Manager client، يدير التوزيعات                  | يجب أن تكون تعمل لتتمكن التنزيلات من الاستمرار              | ابدأها إذا كانت متوقفة، تحقق من السجلات بحثًا عن أخطاء            |

جدول آخر للخطوات التعبيرية:

| رقم الخطوة | الخطوة                                      | الغرض                                              |
|-------------|---------------------------------------------|------------------------------------------------------|
| 1           | تحقق من حالة sms agent host عبر services.msc | تأكد من تشغيل خدمة SCCM client الأساسية       |
| 2           | تحقق من تشغيل wmi performance adapter   | دعم عمليات SCCM التي تعتمد على WMI                |
| 3           | إدارة adaptiveclient إذا كان استخدام الموارد مرتفع  | عزل المشاكل المحتملة مع تنزيل SCCM      |
| 4           | مراجعة سجلات Configuration Manager           | تحديد أخطاء محددة مثل مشاكل اتصال DP |
| 5           | تحقق من الشبكة و الحدود                | تأكد من إمكانية الوصول إلى نقطة التوزيع           |
| 6           | مسح CCM cache، إعادة تشغيل العميل             | حل مشاكل المخزن المؤقت أو إعدادات العميل المحتملة|

#### تفاصيل غير متوقعة: دور Adaptiva

تفصيل غير متوقع هو الدور المحتمل لبرامج Adaptiva، التي لا يتم ذكرها عادةً في دليلات إصلاح SCCM القياسية، ولكن قد تكون مهمة إذا كانت مثبتة. تكاملها مع SCCM في توزيع المحتوى و فحص الصحة قد يجلب تعقيدات، خاصة في بيئات تحتوي على كلا النظامين، مما قد يؤدي إلى تعارض الموارد أو مشاكل الشبكة تؤثر على التنزيلات.

#### الخاتمة

يوضح هذا التحليل الشامل أهمية التأكد من تشغيل خدمات sms agent host و wmi performance adapter، باستخدام services.msc كاداة إدارة. قد تؤثر adaptiveclient، محتمل أن تكون خدمة Adaptiva، بشكل غير مباشر على التنزيلات من خلال تعارض الموارد أو الشبكة، مما يتطلب إدارة حاسمة. من خلال اتباع الخطوات التعبيرية التفصيلية و الاستفادة من الجداول المقدمة، يمكن للمستخدمين معالجة مشكلة تنزيل مركز البرامج المتوقف عند 0٪ بشكل نظامي، مما يضمن عملية حل شاملة.
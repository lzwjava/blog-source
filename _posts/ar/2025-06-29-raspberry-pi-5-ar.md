---
audio: false
generated: true
lang: ar
layout: post
title: 'راسبيري باي 5: قوي ومتعدد الاستخدامات'
translated: true
type: note
---

يعتبر Raspberry Pi 5، الذي أصدرته مؤسسة Raspberry Pi في أكتوبر 2023، أحدث نسخة من سلسلة أجهزة الكمبيوتر أحادية اللوحة الشهيرة، والمصممة لتقديم أداء عالٍ وتنوعًا وبأسعار معقولة للهواة والمعلمين والمحترفين. مستندًا إلى نجاح الطرازات السابقة، يقدم Raspberry Pi 5 ترقيات كبيرة في قوة المعالجة والتوصيل والميزات، مما يجعله مناسبًا لمجموعة واسعة من التطبيقات، من المشاريع التعليمية إلى الأتمتة الصناعية ومهام الحوسبة المتقدمة. فيما يلي مقدمة شاملة عن Raspberry Pi 5، تغطي تاريخه ومواصفاته وميزاته وإعداده وتطبيقاته والمزيد.

---

### **نظرة عامة وتاريخ**
بدأت سلسلة Raspberry Pi في عام 2012 بمهمة توفير منصة ميسورة التكلفة ويمكن الوصول إليها لتعلم البرمجة والحوسبة. في البداية، استهدفت الطلاب والهواة، وسرعان ما اكتسبت Raspberry Pi شعبية بين المطورين والمهندسين لتصميمها المضغوط واستهلاكها المنخفض للطاقة وتنوعها. مع كل إصدار، تم تحسين الأداء وتوسيع القدرات، حيث يمثل Raspberry Pi 5 قفزة كبيرة مقارنة بـ Raspberry Pi 4 الذي صدر في عام 2019.

تم الإعلان عن Raspberry Pi 5 في 28 سبتمبر 2023 وأصبح متاحًا للطلب المسبق بعد ذلك بوقت قصير، وهو أول جهاز في السلسلة يتميز بتصميم سيليكون داخلي (وحدة تحكم الإدخال/الإخراج RP1) ويقدم ميزات متقدمة مثل دعم PCIe لخيارات تخزين أسرع. بسعر 60 دولارًا أمريكيًا للطراز بسعة 4 جيجابايت، و80 دولارًا أمريكيًا للطراز بسعة 8 جيجابايت، و50 دولارًا أمريكيًا للطراز بسعة 2 جيجابايت (الذي تم تقديمه في أغسطس 2024)، و120 دولارًا أمريكيًا للطراز بسعة 16 جيجابايت (الذي تم تقديمه في يناير 2025)، يظل حلاً حاسوبيًا قويًا وبأسعار معقولة.[](https://www.raspberrypi.com/products/raspberry-pi-5/)[](https://www.raspberrypi.com/news/introducing-raspberry-pi-5/)

---

### **المواصفات الرئيسية**
يتم تشغيل Raspberry Pi 5 بمجموعة قوية من المكونات المادية، مما يوفر زيادة في الأداء تتراوح بين 2-3 مرات مقارنة بـ Raspberry Pi 4. فيما يلي مواصفاته الأساسية:

- **المعالج**: Broadcom BCM2712، وهو معالج ARM Cortex-A76 رباعي النواة بتردد 2.4 جيجا هرتز وبتقنية 64 بت مع امتدادات التشفير، وذاكرة تخزين مؤقت L2 بسعة 512 كيلوبايت لكل نواة، وذاكرة تخزين مؤقت L3 مشتركة بسعة 2 ميجابايت. هذا المعالج أسرع بكثير من معالج Cortex-A72 الموجود في Raspberry Pi 4، مما يمكن من أداء أفضل للمهام المتطلبة مثل الحوسبة المكتبية والمحاكاة.[](https://www.raspberrypi.com/products/raspberry-pi-5/)[](https://www.zimaspace.com/blog/raspberry-pi-5-everything-you-need-to-know.html)
- **وحدة معالجة الرسومات**: VideoCore VII GPU، تدعم OpenGL ES 3.1 و Vulkan 1.2، وقادرة على تشغيل شاشتين مزدوجتين بدقة 4K بتردد 60 هرتز عبر منافذ micro HDMI.[](https://www.linkedin.com/pulse/introduction-raspberry-pi-5-specs-harshvardhan-mishra-wkbmf)
- **الذاكرة العشوائية**: متوفر بإصدارات 2 جيجابايت، و4 جيجابايت، و8 جيجابايت، و16 جيجابايت من نوع LPDDR4X-4267 SDRAM، مما يوفر نطاق ترددي للذاكرة أسرع من Raspberry Pi 4.[](https://wagnerstechtalk.com/rpi5/)[](https://www.raspberrypi.com/products/raspberry-pi-5/)
- **التخزين**:
  - فتحة بطاقة MicroSD مع دعم وضع SDR104 عالي السرعة (موصى به: 32 جيجابايت أو أعلى لنظام Raspberry Pi OS، و16 جيجابايت للإصدار Lite). السعات التي تزيد عن 2 تيرابايت غير مدعومة بسبب قيود MBR.
  - واجهة PCIe لأقراص M.2 NVMe SSD عبر لوحات HAT الاختيارية، مما يمكن من التمهيد السريع ونقل البيانات.[](https://www.raspberrypi.com/documentation/computers/getting-started.html)[](https://www.raspberrypi.com/products/raspberry-pi-5/)
- **التوصيل**:
  - Wi-Fi مزدوج النطاق 2.4 جيجا هرتز و5 جيجا هرتز من نوع 802.11ac.
  - Bluetooth 5.0 و Bluetooth Low Energy (BLE).
  - Ethernet جيجابت مع دعم Power over Ethernet (PoE) (يتطلب PoE+ HAT).
  - منفذا USB 3.0 (تشغيل متزامن بسرعة 5 جيجابت في الثانية) ومنفذا USB 2.0.
  - رأس 40-pin GPIO للتواصل مع أجهزة الاستشعار والشاشات والملحقات الأخرى.
  - منفذا micro HDMI لإخراج مزدوج بدقة 4K وتردد 60 هرتز.
  - جهازي إرسال واستقبال MIPي مزدوجي المسار للكاميرا/الشاشة (قابلان للتبادل لكاميرا واحدة وشاشة واحدة أو اثنين من نفس النوع).
  - موصل UART مخصص لتصحيح الأخطاء (921,600 بت في الثانية).[](https://www.linkedin.com/pulse/introduction-raspberry-pi-5-specs-harshvardhan-mishra-wkbmf)[](https://www.waveshare.com/wiki/Raspberry_Pi_5)
- **الطاقة**: يتطلب مصدر طاقة USB-C بقوة 5 فولت / 5 أمبير (مثل Raspberry Pi 27W USB-C Power Supply). قد تسبب مصادر الطاقة غير الكافية عدم استقرار.[](https://www.raspberrypi.com/products/raspberry-pi-5/)
- **ساعة الوقت الحقيقي (RTC)**: RTC مدمجة مع موصل بطارية احتياطية (J5)، مما يلغي الحاجة إلى وحدات ساعة خارجية عند إيقاف التشغيل.[](https://en.wikipedia.org/wiki/Raspberry_Pi)
- **ميزات أخرى**:
  - وحدة تحكم الإدخال/الإخراج RP1، وهي شريحة مخصصة صممتها Raspberry Pi لتحسين أداء الإدخال/الإخراج.
  - زر تشغيل/إيقاف، وهو أول زر من نوعه في السلسلة.
  - التوافق مع M.2 HAT+ لأقراص NVMe SSD وأجهزة PCIe الأخرى.[](https://www.tomshardware.com/reviews/raspberry-pi-5)[](https://www.raspberrypi.com/news/introducing-raspberry-pi-5/)

---

### **التصميم المادي**
يحتفظ Raspberry Pi 5 بحجم بطاقة الائتمان (85 مم × 56 مم) للطرازات الرئيسية السابقة، مما يضمن التوافق مع العديد من الإعدادات الحالية. ومع ذلك، فهو يتطلب علبة جديدة بسبب تغييرات التخطيط وزيادة متطلبات التبريد. تتضمن العلبة الرسمية لـ Raspberry Pi 5 (10 دولارات أمريكية) مروحة مدمجة للتبريد النشط، ويوصى بـ Active Cooler (5 دولارات أمريكية) لأحمال العمل الثقيلة لمنع الخنق الحراري. كما تتميز اللوحة بحواف أنظف بسبب عمليات التصنيع المحسنة مثل إعادة التدفق الدخيلة للموصلات والفصل الموجه للألواح.[](https://www.raspberrypi.com/products/raspberry-pi-5/)[](https://www.raspberrypi.com/news/introducing-raspberry-pi-5/)

---

### **نظام التشغيل والبرمجيات**
نظام التشغيل الموصى به هو **Raspberry Pi OS** (المبني على Debian Bookworm)، والمحسن لأجهزة Raspberry Pi 5. وهو متوفر في:
- **الإصدار الكامل**: يتضمن بيئة سطح مكتب وبرامج مثبتة مسبقًا للاستخدام العام.
- **الإصدار القياسي**: بيئة سطح مكتب مع الحد الأدنى من البرامج.
- **الإصدار المخفف**: واجهة سطر الأوامر فقط، مثالي للإعدادات بدون واجهة رسومية أو التطبيقات خفيفة الوزن.

تشمل أنظمة التشغيل المدعومة الأخرى:
- **Ubuntu**: توزيعة Linux قوية للاستخدام المكتبي والخوادم.
- **Arch Linux ARM**: بسيطة وقابلة للتخصيص بدرجة كبيرة.
- **LibreELEC**: نظام تشغيل خفيف الوزن لتشغيل مركز الوسائط Kodi.
- **Batocera/Recalbox**: لألعاب الريترو.
- **Windows 10/11**: دعم تجريبي للاستخدام المكتبي (غير موصى به رسميًا).[](https://www.jaycon.com/ultimate-guide-to-raspberry-pi/)[](https://wagnerstechtalk.com/rpi5/)

تعتبر أداة **Raspberry Pi Imager** هي الأداة الرسمية لنسخ أنظمة التشغيل على بطاقات microSD أو أقراص SSD. فهي تبسط عملية الإعداد من خلال السماح للمستخدمين بتحديد وتكوين نظام التشغيل، بما في ذلك التهيئة المسبقة لاسم المضhostname وحسابات المستخدمين و SSH للتشغيل بدون واجهة رسومية.[](https://wagnerstechtalk.com/rpi5/)[](https://www.scribd.com/document/693937166/Bash-A-Getting-started-with-Raspberry-Pi-5-A-beginners-Guide-2023)

---

### **عملية الإعداد**
إعداد Raspberry Pi 5 هو عملية مباشرة ولكنها تتطلب تحضيرًا محددًا للأجهزة والبرمجيات. إليك دليلًا خطوة بخطوة:

1. **اجمع الأجهزة**:
   - Raspberry Pi 5 (طراز 2 جيجابايت، أو 4 جيجابايت، أو 8 جيجابايت، أو 16 جيجابايت).
   - بطاقة MicroSD (يوصى بـ 32 جيجابايت أو أكثر، فئة 10 للأداء).
   - مصدر طاقة USB-C بقوة 5 فولت / 5 أمبير.
   - كابل Micro HDMI إلى HDMI للشاشة.
   - لوحة مفاتيح USB وفأرة (أو بدائل Bluetooth).
   - اختياري: شاشة، كابل Ethernet، قرص SSD من نوع M.2 مع لوحة HAT، علبة مع تبريد.[](https://robocraze.com/blogs/post/how-to-setup-your-raspberry-pi-5)

2. **جهز بطاقة MicroSD**:
   - قم بتنزيل Raspberry Pi Imager من موقع Raspberry Pi الرسمي.
   - قم بتنسيق بطاقة microSD باستخدام أداة مثل SDFormatter.
   - استخدم الأداة Imager لتحديد ونسخ نظام Raspberry Pi OS (Bookworm) على البطاقة.[](https://www.waveshare.com/wiki/Raspberry_Pi_5)

3. **قم بتوصيل الملحقات**:
   - أدخل بطاقة microSD في Raspberry Pi 5.
   - قم بتوصيل الشاشة بمنفذ HDMI0 (إذا كنت تستخدم شاشتين مزدوجتين، استخدم منفذي micro HDMI).
   - قم بتوصيل لوحة المفاتيح والفأرة و Ethernet (إذا لم تكن تستخدم Wi-Fi).
   - قم بتوصيل مصدر طاقة USB-C.[](https://www.raspberrypi.com/documentation/computers/getting-started.html)

4. **قم بالتمهيد والتكوين**:
   - شغل Raspberry Pi 5. يجب أن يظل مؤشر الطاقة الأحمر مضاءً، وسيومض مؤشر ACT الأخضر أثناء التمهيد.
   - اتبع المطالبات الظاهرة على الشاشة لتكوين نظام Raspberry Pi OS، بما في ذلك ضبط المنطقة الزمنية و Wi-Fi ومعلومات اعتماد المستخدم.
   - للإعدادات بدون واجهة رسومية، قم بتمكين SSH عبر الأداة Imager أو اتصل عبر UART لتصحيح الأخطاء.[](https://www.waveshare.com/wiki/Raspberry_Pi_5)

5. **الملحقات الاختيارية**:
   - قم بتثبيت قرص SSD من نوع M.2 باستخدام M.2 HAT+ لتخزين أسرع.
   - أضف بطارية إلى موصل RTC للحفاظ على الوقت عند إيقاف التشغيل.
   - استخدم علبة مع تبريد نشط للمهام المكثفة.[](https://www.theengineeringprojects.com/2023/10/introduction-to-raspberry-pi-5.html)[](https://www.raspberrypi.com/products/raspberry-pi-5/)

---

### **الميزات والتحسينات الرئيسية**
يقدم Raspberry Pi 5 عدة تطورات مقارنة بـ Raspberry Pi 4:
- **الأداء**: يوفر معالج Cortex-A76 ووحدة معالجة الرسومات VideoCore VII معالجة ورسومات أسرع بمقدار 2-3 مرات، مما يجعله مناسبًا لمهام مثل محاكاة PS2 والحوسبة المكتبية وأحمال عمل الذكاء الاصطناعي. يمكن رفع تردد تشغيل المعالج إلى 3 جيجا هرتز مع التبريد المناسب.[](https://wagnerstechtalk.com/rpi5/)[](https://www.tomshardware.com/reviews/raspberry-pi-5)
- **دعم PCIe**: تسمح إضافة واجهة PCIe لأقراص NVMe SSD والملحقات عالية السرعة الأخرى، مما يحسن بشكل كبير سرعة التمهيد ونقل البيانات.[](https://www.raspberrypi.com/news/introducing-raspberry-pi-5/)
- **وحدة تحكم الإدخال/الإخراج RP1**: تعزز هذه الشريحة المخصصة نطاق تردد USB 3.0 وتوصيل الكاميرا/الشاشة وأداء الإدخال/الإخراج بشكل عام.[](https://www.raspberrypi.com/products/raspberry-pi-5/)
- **دعم الشاشة المزدوجة بدقة 4K**: يمكن لمنفذي micro HDMI تمكين إخراج متزامن بدقة 4K وتردد 60 هرتز، مما يجعله مثاليًا لإعدادات الوسائط المتعددة والإنتاجية.[](https://www.linkedin.com/pulse/introduction-raspberry-pi-5-specs-harshvardhan-mishra-wkbmf)
- **ساعة الوقت الحقيقي المدمجة**: تضمن ساعة الوقت الحقيقي المدمجة مع النسخ الاحتياطي للبطارية حفظ الوقت بدقة بدون اتصال بالإنترنت.[](https://en.wikipedia.org/wiki/Raspberry_Pi)
- **زر الطاقة**: يبسط زر التشغيل/الإيقاف المخصص إدارة الطاقة.[](https://www.tomshardware.com/reviews/raspberry-pi-5)
- **تحسينات حرارية**: تحسن عملية التصنيع 40 نانومتر و Active Cooler الاختياري الكفاءة الحرارية، على الرغم من التوصية بالتبريد النشط للأداء العالي المستدام.[](https://robocraze.com/blogs/post/how-to-setup-your-raspberry-pi-5)

---

### **التطبيقات**
تجعل القدرات المحسنة لـ Raspberry Pi 5 منه مناسبًا لمجموعة واسعة من المشاريع:
- **التعليم**: تعلم البرمجة (Python، C++، Java) والإلكترونيات باستخدام رأس 40-pin GPIO لأجهزة الاستشعار ومصابيح LED والروبوتات.[](https://www.rs-online.com/designspark/introduction-to-raspberry-pi-5-specifications-and-features)
- **أتمتة المنزل**: تحكم في أجهزة المنزل الذكي مثل الأضواء والأقفال والكاميرات باستخدام أطر عمل إنترنت الأشياء.[](https://www.rs-online.com/designspark/introduction-to-raspberry-pi-5-specifications-and-features)
- **مراكز الوسائط**: شغل Kodi عبر LibreELEC للبث والتشغيل الإعلامي على شاشتين مزدوجتين بدقة 4K.[](https://www.jaycon.com/ultimate-guide-to-raspberry-pi/)
- **ألعاب الريترو**: استخدم Batocera أو Recalbox لمحاكاة أجهزة الألعاب حتى PS2.[](https://wagnerstechtalk.com/rpi5/)
- **الخوادم**: استضف خوادم ويب خفيفة الوزن، أو شبكات VPN خاصة، أو مراكز أتمتة منزلية (مثل HomeBridge).[](https://arstechnica.com/gadgets/2024/01/what-i-learned-from-using-a-raspberry-pi-5-as-my-main-computer-for-two-weeks/)
- **الأنظمة الصناعية والمضمنة**: وحدة Compute Module 5، المبنية على Raspberry Pi 5، مثالية للتطبيقات المضمنة المخصصة.
- **الذكاء الاصطناعي والتعلم الآلي**: استفد من تحسينات وحدة المعالجة المركزية/وحدة معالجة الرسومات لمشاريع الذكاء الاصطناعي على الحافة، مثل معالجة الصور أو التعرف على الصوت، مع لوحات AI HATs المتوافقة.[](https://www.jaycon.com/ultimate-guide-to-raspberry-pi/)[](https://www.raspberrypi.com/documentation/)
- **الحوسبة المكتبية**: استخدمه كحاسوب مكتبي منخفض التكلفة وموفر للطاقة للتصفح ومعالجة النصوص ومهام الإنتاجية الخفيفة.[](https://arstechnica.com/gadgets/2024/01/what-i-learned-from-using-a-raspberry-pi-5-as-my-main-computer-for-two-weeks/)

---

### **التوافق والتحديات**
بينما يقدم Raspberry Pi 5 ترقيات كبيرة، تظهر بعض مشكلات التوافق:
- **العلب**: لا يتناسب Raspberry Pi 5 مع علب Raspberry Pi 4 بسبب تغييرات التخطيط. استخدم العلبة الرسمية لـ Raspberry Pi 5 أو الخيارات المتوافقة من جهات خارجية.[](https://www.raspberrypi.com/products/raspberry-pi-5/)
- **لوحات HATs والإضافات**: قد تفتقر بعض لوحات HATs القديمة إلى الدعم البرمجي لـ Raspberry Pi 5، مما يتطلب تحديثات من المجتمع. قد تحتاج برمجة GPIO أيضًا إلى تعديلات.[](https://www.dfrobot.com/blog-13550.html)
- **مصدر الطاقة**: مطلوب مصدر طاقة USB-C بقوة 5 فولت / 5 أمبير لتجنب عدم الاستقرار، على عكس مصدر 5 فولت / 3 أمبير المستخدم في Raspberry Pi 4.[](https://www.waveshare.com/wiki/Raspberry_Pi_5)
- **نظام التشغيل**: فقط أحدث إصدار من نظام Raspberry Pi OS (Bookworm) محسن بالكامل. قد لا تدعم إصدارات نظام التشغيل القديمة ميزات جديدة مثل PCIe.[](https://www.waveshare.com/wiki/Raspberry_Pi_5)

يتعامل مجتمع Raspberry Pi بنشاط مع هذه التحديات، ويشارك الحلول وتحديثات البرامج الثابتة لتعزيز التوافق.[](https://www.dfrobot.com/blog-13550.html)

---

### **الملحقات والنظام البيئي**
يتم دعم Raspberry Pi 5 من خلال نظام بيئي غني بالملحقات:
- **الملحقات الرسمية**:
  - علبة Raspberry Pi 5 (10 دولارات أمريكية) مع مروحة مدمجة.
  - Active Cooler (5 دولارات أمريكية) لأحمال العمل الثقيلة.
  - مصدر طاقة USB-C بقوة 27 واط (12 دولارًا أمريكيًا).
  - M.2 HAT+ لأقراص NVMe SSD (10-20 دولارًا أمريكيًا).
  - أقراص NVMe SSD تحمل علامة Raspberry Pi التجارية (256 جيجابايت أو 512 جيجابايت).[](https://www.theengineeringprojects.com/2023/10/introduction-to-raspberry-pi-5.html)[](https://www.raspberrypi.com/products/raspberry-pi-5/)
- **الملحقات من جهات خارجية**: تقدم شركات مثل CanaKit و Pimoroni و Pineboards مجموعات ولوحات HATs وحلول تخزين مصممة خصيصًا لـ Raspberry Pi 5.[](https://wagnerstechtalk.com/rpi5/)[](https://www.tomshardware.com/reviews/raspberry-pi-5)
- **الوثائق والموارد**:
  - يغطي The Official Raspberry Pi Beginner’s Guide (الإصدار الخامس) بقلم Gareth Halfacree الإعداد والبرمجة والمشاريع. يتوفر ملف PDF مجاني عبر تطبيق Raspberry Pi Bookshelf.[](https://www.raspberrypi.com/news/available-now-the-official-raspberry-pi-beginners-guide-5th-edition/)
  - توفر موارد المجتمع مثل Wagner’s TechTalk ومجتمع Raspberry Pi على Reddit دروسًا تعليمية وأفكارًا للمشاريع.[](https://wagnerstechtalk.com/rpi5/)[](https://www.reddit.com/r/RASPBERRY_PI_PROJECTS/comments/16upxc0/total_beginner_with_raspberry_pi_where_do_i_start/)

---

### **الأداء وحالات الاستخدام**
يجعل أداء Raspberry Pi 5 منه بديلاً قابلاً للتطبيق لأجهزة الكمبيوتر الصغيرة منخفضة الطاقة القائمة على ARM. في الاختبارات، تم استخدامه بنجاح كحاسوب مكتبي عام للتصفح عبر الإنترنت وتحرير المستندات وتعدد المهام الخفيف، على الرغم من أنه قد يواجه صعوبة في أحمال عمل المتصفح الثقيلة (مثل علامات تبويب متعددة في Chrome). تجعل قدرته على تشغيل محاكاة PS2 والتعامل مع شاشتين مزدوجتين بدقة 4K منه خيارًا مفضلاً لألعاب الريترو ومراكز الوسائط. يعزز رفع تردد التشغيل إلى 3 جيجا هرتز ووحدة معالجة الرسومات إلى 1.1 جيجا هرتز الأداء بشكل أكبر، على الرغم من أن التبريد النشط ضروري.[](https://arstechnica.com/gadgets/2024/01/what-i-learned-from-using-a-raspberry-pi-5-as-my-main-computer-for-two-weeks/)[](https://www.tomshardware.com/reviews/raspberry-pi-5)

للتطبيقات الاحترافية، يدعم الطراز بسعة 16 جيجابايت المهام الأكثر تطلبًا مثل تطوير البرمجيات واستضافة الخوادم. تلبي وحدة Compute Module 5 و Raspberry Pi 500 (نسخة مدمجة مع لوحة مفاتيح) احتياجات الأنظمة المضمنة والحوسبة الشاملة.[](https://www.jaycon.com/ultimate-guide-to-raspberry-pi/)[](https://en.wikipedia.org/wiki/Raspberry_Pi)

---

### **المجتمع والدعم**
يمثل مجتمع Raspberry Pi قوة رئيسية، حيث تقدم المنتديات والمجتمعات على Reddit والمواقع الإلكترونية مثل raspberrypi.org دعماً واسعاً. توفر مؤسسة Raspberry Pi تحديثات منتظمة للبرامج الثابتة، مثل تلك التي تمكن من دعم محركي NVMe مزدوجين وتحسين رفع تردد التشغيل. تقدم مجلة The MagPi والوثائق الرسمية أفكارًا للمشاريع وتفاصيل تقنية.[](https://www.linkedin.com/pulse/introduction-raspberry-pi-5-specs-harshvardhan-mishra-wkbmf)[](https://www.raspberrypi.com/documentation/)

---

### **الخلاصة**
يعد Raspberry Pi 5 جهاز كمبيوتر أحادي اللوحة قويًا ومتعدد الاستخدامات وبأسعار معقولة، يبني على إرث الطرازات السابقة مع تقديم ميزات حديثة مثل دعم PCIe وشريحة RP1 المخصصة و RTC مدمجة. مع خيارات ذاكرة وصول عشوائي تصل إلى 16 جيجابايت، ودعم شاشة مزدوجة بدقة 4K، وزيادة في الأداء تتراوح بين 2-3 مرات، فهو مثالي للتعليم ومشاريع الهواة وأتمتة المنزل وألعاب الريترو والتطبيقات الصناعية. بينما توجد تحديات في التوافق، يضمن المجتمع النشط والتحديثات المنتظمة تجربة سلسة. سواء كنت مبتدئًا تتعلم Python أو مهندسًا تبني أنظمة إنترنت الأشياء، يقدم Raspberry Pi 5 إمكانيات لا حصر لها بسعر يجعل الحوسبة في متناول الجميع.[](https://www.zimaspace.com/blog/raspberry-pi-5-everything-you-need-to-know.html)[](https://www.rs-online.com/designspark/introduction-to-raspberry-pi-5-specifications-and-features)

لمزيد من التفاصيل، قم بزيارة موقع Raspberry Pi الرسمي (raspberrypi.com) أو استكشف موارد المجتمع مثل Wagner’s TechTalk ومجلة The MagPi.[](https://wagnerstechtalk.com/rpi5/)[](https://www.linkedin.com/pulse/introduction-raspberry-pi-5-specs-harshvardhan-mishra-wkbmf)
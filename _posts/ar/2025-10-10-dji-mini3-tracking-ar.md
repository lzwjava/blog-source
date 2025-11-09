---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: قيود وحلول التتبع في طائرة DJI Mini 3
translated: true
type: note
---

لا تحتوي طائرة DJI Mini 3 (الموديل الأساسي) على ميزات مدمجة مثل ActiveTrack (تتبع بصري للكائنات) أو وضع Follow Me (تتبع يعتمد على GPS) لمطاردة سيارة متحركة أو التحليق فوقها تلقائياً لالتقاط الصور أو الفيديو. هذا يمثل قيداً رئيسياً مقارنةً بالطائرات المسيرة الأكثر تطوراً من DJI.

مع ذلك، فإن طائرة DJI Mini 3 Pro تدعم ميزة ActiveTrack، التي تستخدم كاميرا الطائرة لتتبع الموضوعات بصرياً واتباعها مثل السيارات أو الأشخاص أو المركبات من الخلف، أو من الأعلى، أو من مواقع أخرى — مما يسمح لك بالتقاط لقطات ديناميكية بينما تحافظ الطائرة على مسافة وارتفاع محددين.

بخصوص واجهات برمجة التطبيقات (APIs) للتطوير المخصص:
- إن DJI Mobile SDK (لتطبيقات Android/iOS) يدعم بالفعل سلسلة Mini 3، بما في ذلك التحكم الأساسي في الطيران مثل أوامر Virtual Stick (على سبيل المثال، لضبط الموضع/السرعة يدوياً) ومهام Waypoint. يمكنك بناء تطبيق مخصص لجعل الطائرة تتبع مسار سيارة إذا قمت بدمج بيانات GPS في الوقت الفعلي من السيارة (عبر البلوتوث، أو تطبيق مرافق، أو جهاز إرسال خارجي). هذا لن يكون تتبعاً بصرياً جاهزاً للاستخدام (plug-and-play)، ولكن يمكنه محاكاة المطاردة من الأعلى أو الخلف عن طريق حساب الإزاحات (على سبيل المثال، 10-20 متراً للخلف و 50 متراً للأعلى).
- ومع ذلك، فإن واجهات برمجة التطبيقات (APIs) الخاصة بمهام ActiveTrack (للتتبع البصري الآلي) **غير مدعومة** على طائرة Mini 3 أو Mini 3 Pro — فهي محدودة بالموديلات الأقدم مثل Mavic Air 2 أو Air 2S.
- لالتقاط الصور أثناء الرحلة، يمكنك استخدام واجهات برمجة تطبيقات الكاميرا (Camera APIs) في الـ SDK لتفعيل التقاط الصور تلقائياً بناءً على المؤقتات، أو المسافة، أو منطقك المخصص.

إذا كنت لا تمانع في استخدام تطبيقات الطرف الثالث (التي تعتمد على الـ SDK في الخلفية):
- يمكن لتطبيقات مثل Dronelink أو Litchi تمكين وضع "Follow Me" أساسي على طائرة Mini 3 باستخدام GPS هاتفك (أو جهاز خارجي). لتتبع سيارة معينة، ستحتاج إلى إقرانها بجهار إرسال GPS (beacon) على المركبة (على سبيل المثال، عبر هاتف ذكي يعمل كنقطة اتصال، أو متعقب مخصص مثل بديل لـ Tile أو AirTag يغذي البيانات للتطبيق). هذا الإعداد نجح مع بعض المستخدمين لمطاردة السيارات على الطرق أو الممرات، مع بقاء الطائرة في موقع علوي أو متأخرة من الخلف لتصوير اللقطات.

ضع في اعتبارك الملاحظات القانونية/السلامة: يجب أن يلتزم تتبع الطائرات المسيرة للمركبات المتحركة باللوائح المحلية (على سبيل المثال، تتطلب قواعد FAA في الولايات المتحدة أن تكون within visual line-of-sight، وعدم التشغيل beyond visual range). اختبر في المناطق المفتوحة لتجنب العوائق، كما أن التصميم خفيف الوزن لطائرة Mini 3 يحد من مقاومتها للرياح أثناء المطاردة عالية السرعة.

### المراجع
- [DJI Mini 3 Active Track HACK DJI Mini 3 Follow Me](https://www.youtube.com/watch?v=UYzSdd3iJwA)
- [Does the mini 3 have ai tracking to follow objects like cars](https://www.facebook.com/groups/djimini3ukowners/posts/2726498670890510/)
- [Can someone explain follow me mode? And if it's on mini 3?](https://www.reddit.com/r/dji/comments/13pqbw7/can_someone_explain_follow_me_mode_and_if_its_on/)
- [DJI Mini 3 / Mini 3 Pro - Follow Me Mode With Dronelink](https://www.youtube.com/watch?v=Rhneo8QoXV0)
- [DJI Product SDK Compatibility](https://support.dji.com/help/content?customId=01700000763&spaceId=17&re=US&lang=en&documentType=&paperDocType=ARTICLE)
- [DJI has released MSDK 5.3.0 with support for Mini 3 Pro and Mini 3](https://forum.flylitchi.com/t/dji-has-released-msdk-5-3-0-with-support-for-mini-3-pro-and-mini-3/9512)
- [class ActiveTrackOperator - DJI Mobile SDK Documentation](https://developer.dji.com/api-reference/android-api/Components/Missions/DJIActiveTrackMissionOperator.html)
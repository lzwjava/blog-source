---
audio: false
generated: false
lang: ar
layout: post
title: يجب على الشركات توفير سياق الذكاء الاصطناعي أو الوكلاء لتسهيل التكامل
translated: true
---

لدي صديق يعمل في Greptime DB، وقد كنت أفكر في كيفية دمج منتجهم بسرعة في الأنظمة الحالية.

## السياق

أحد الأساليب المحتملة هو توفير المزيد من السياق للذكاء الاصطناعي. يمكن لـ Greptime DB تنظيم وثائقه بطريقة تتناسب مع أدوات الذكاء الاصطناعي مثل ChatGPT، مما يسهل عملية التكامل.

تقدم Greptime DB وثائقها على [https://greptime.com](https://greptime.com)، لكني أتساءل عما إذا كانت أدوات مثل ChatGPT أو DeepSeek يمكنها معالجة جميع الصفحات في وثائقهم بكفاءة. بالإضافة إلى ذلك، تنتشر ثروة من المعلومات عبر مستودعات GitHub، والقضايا، والوثائق الداخلية، والوثائق العامة، وغيرها من القطع المعرفية المخفية التي لم يتم توثيقها بشكل صريح.

لحل هذه المشكلة، قد يحتاج Greptime DB إلى إنشاء عدة نماذج GPT متخصصة. على سبيل المثال، يمكنهم إنشاء نصوص توجيهية مثل هذه:

```

### وثائق Greptime:  
الوثائق الرسمية متاحة على: [https://docs.greptime.com](https://docs.greptime.com)

* [دليل البدء السريع](https://docs.greptime.com/getting-started/quick-start)  
* [دليل المستخدم](https://docs.greptime.com/user-guide/overview)  
* [العروض التوضيحية](https://github.com/GreptimeTeam/demo-scene)  
* [الأسئلة الشائعة](https://docs.greptime.com/faq-and-others/faq)

### عناوين المستودعات:
فيما يلي الدلائل والملفات الرئيسية من جذر مستودع GreptimeDB:

1. [benches](https://github.com/GreptimeTeam/greptimedb/tree/main/benches)  
2. [docs](https://github.com/GreptimeTeam/greptimedb/tree/main/docs)  
3. [src](https://github.com/GreptimeTeam/greptimedb/tree/main/src)  
4. [test](https://github.com/GreptimeTeam/greptimedb/tree/main/test)  
5. [third_party](https://github.com/GreptimeTeam/greptimedb/tree/main/third_party)  
6. [tools](https://github.com/GreptimeTeam/greptimedb/tree/main/tools)  

تم ترجمة الروابط كما هي دون تغيير لأنها تشير إلى أسماء مجلدات ومشاريع تقنية.

ملفات رئيسية إضافية:

7. [Cargo.lock](https://github.com/GreptimeTeam/greptimedb/tree/main/Cargo.lock)  
8. [Cargo.toml](https://github.com/GreptimeTeam/greptimedb/tree/main/Cargo.toml)  
9. [LICENSE](https://github.com/GreptimeTeam/greptimedb/tree/main/LICENSE)  
10. [Makefile](https://github.com/GreptimeTeam/greptimedb/tree/main/Makefile)  
11. [README.md](https://github.com/GreptimeTeam/greptimedb/tree/main/README.md)  
12. [NOTICE](https://github.com/GreptimeTeam/greptimedb/tree/main/NOTICE)  

(ملاحظة: الأسماء مثل Cargo.lock و Cargo.toml و LICENSE و Makefile و README.md و NOTICE هي أسماء ملفات تقنية ولا يتم ترجمتها عادةً.)

يرجى البحث في هذه الموارد قبل الرد على أي استفسارات المستخدمين.

```

هذا سيسمح للمستخدمين بالتفاعل مع روبوت محادثة يعتمد على GPT ويجيب على الأسئلة بناءً على الوثائق، مما يضمن استجابات أكثر دقة.

لنقم بإنشاء هذا الـ GPT: [https://chatgpt.com/g/g-677e87121d448191b0813ca28425ce38-greptimedb-integration](https://chatgpt.com/g/g-677e87121d448191b0813ca28425ce38-greptimedb-integration)

لم أستطع الإجابة على هذا السؤال،

```
ما هو محتوى ملف `greptimedb/src/query/src/query_engine/context.rs`؟
```



## الوكيل

أتخيل أداة تسمى `greptimedb-agent` لتبسيط عملية التكامل.

تخيل تشغيل أمر بسيط مثل:

```bash
pip install greptimedb-agent
greptimedb-agent
```

ملاحظة: الكود أعلاه هو أمر لتنصيب وتشغيل `greptimedb-agent` باستخدام `pip`. لا يحتاج إلى ترجمة حيث أنه جزء من التعليمات البرمجية.

سيقوم `greptimedb-agent` بجمع المعلومات بشكل ذكي حول النظام الحالي، مثل تفاصيل الجهاز والكود الموجود، وذلك لفهم السياق واتخاذ القرار حول كيفية دمج Greptime DB بأفضل طريقة.

هذا الأمر سيحدث تلقائيًا كودك لدمج Greptime DB، ليحل محل قاعدة البيانات الحالية بسلاسة مع Greptime DB في بضع خطوات فقط.


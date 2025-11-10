---
audio: false
generated: true
lang: ar
layout: post
title: قواعد عناوين مواقع مشاريع GitHub Pages
translated: true
type: note
---

باستخدام GitHub Pages، يمكنك إنشاء **مواقع المشاريع** تحت حسابك الشخصي بالإضافة إلى موقع المستخدم الخاص بك (`username.github.io`). ومع ذلك، فإن تنسيق عنوان URL لمواقع المشاريع يقتصر على أنماط محددة، ولا يتم دعم جميع تكوينات النطاقات الفرعية أو المسارات الفرعية بشكل أصلي. دعنا نعالج سؤالك حول ما إذا كان يمكنك استخدام `username.github.io/project1` أو `project1.username.github.io` لمواقع المشاريع.

### النقاط الرئيسية
- **موقع المستخدم**: مستودع واحد باسم `username.github.io` يخدم المحتوى على `https://username.github.io`.
- **مواقع المشاريع**: يمكن تكوين أي مستودع آخر في حسابك الشخصي كموقع مشروع، يتم تقديمه على `https://username.github.io/repository-name` (مسار فرعي، وليس نطاقًا فرعيًا).
- **قيود النطاق الفرعي**: GitHub Pages لا تدعم النطاقات الفرعية مثل `project1.username.github.io` بشكل أصلي تحت نطاق `github.io`. يتم إدارة نطاق `github.io` بواسطة GitHub، ولا يتم دعم سوى `username.github.io` (للمستخدمين) أو `organization.github.io` (للمنظمات) كنطاقات فرعية من المستوى الأعلى. تتطلب النطاقات الفرعية المخصصة مثل `project1.username.github.io` نطاقًا مخصصًا وتكوين DNS.

### هل يمكنك استخدام `username.github.io/project1`؟
**نعم**، يمكنك استخدام `username.github.io/project1` لموقع مشروع. هذه هي الطريقة القياسية التي تتعامل بها GitHub Pages مع مواقع المشاريع:
- أنشئ مستودعًا في حسابك الشخصي (مثل `username/project1`).
- فعّل GitHub Pages لذلك المستودع:
  - انتقل إلى علامة تبويب **الإعدادات** الخاصة بالمستودع.
  - مرر لأسفل إلى قسم **الصفحات**.
  - ضمن **المصدر**، حدد الفرع الذي تريد نشره (مثل `main` أو `gh-pages`) واحفظ.
- بمجرد التكوين، سيكون الموقع متاحًا على `https://username.github.io/project1`.
- يمكنك إنشاء مواقع مشاريع متعددة (مثل `username.github.io/project2`, `username.github.io/project3`) من خلال تمكين GitHub Pages على مستودعات إضافية (`username/project2`, `username/project3`، إلخ).
- **المحتوى**: أضف `index.html` أو استخدم مولد مواقع ثابت مثل Jekyll في فرع النشر الخاص بكل مستودع.

### هل يمكنك استخدام `project1.username.github.io`؟
**لا**، GitHub Pages لا تدعم النطاقات الفرعية مثل `project1.username.github.io` بشكل أصلي تحت نطاق `github.io`. يسمح نطاق `github.io` فقط بـ:
- `username.github.io` لمواقع المستخدمين.
- `organization.github.io` لمواقع المنظمات.
- المسارات الفرعية مثل `username.github.io/repository-name` لمواقع المشاريع.

لتحقيق عنوان URL مثل `project1.username.github.io`، ستحتاج إلى:
1. **نطاق مخصص**: شراء نطاق (مثل `example.com`) من مسجل نطاقات مثل Namecheap أو GoDaddy.
2. **تكوين DNS**: إعداد سجل CNAME للإشارة من نطاق فرعي (مثل `project1.example.com`) إلى موقع GitHub Pages الخاص بك (مثل `username.github.io` أو `username.github.io/project1`).
3. **إعدادات GitHub Pages**:
   - في إعدادات **الصفحات** الخاصة بالمستودع، قم بتكوين النطاق المخصص (مثل `project1.example.com`).
   - اختياريًا، فعّل خيار "فرض HTTPS" للأمان.
4. **النتيجة**: يمكنك تعيين `project1.example.com` ليشير إلى محتوى مستودع `project1`، ولكن لا يمكن تعيين `project1.username.github.io`، لأن GitHub تتحكم في نطاق `github.io` ولا تسمح بالنطاقات الفرعية المخصصة تحته.

### مثال على الإعداد لـ `username.github.io/project1`
1. أنشئ مستودعًا باسم `project1` تحت حسابك (`username/project1`).
2. أضف محتوى (مثل `index.html`):
   ```bash
   git clone https://github.com/username/project1
   cd project1
   echo "Hello from Project 1" > index.html
   git add --all
   git commit -m "Initial commit"
   git push origin main
   ```
3. فعّل GitHub Pages:
   - انتقل إلى `username/project1` → **الإعدادات** → **الصفحات**.
   - عيّن المصدر إلى `main` (أو فرع آخر) واحفظ.
4. زر `https://username.github.io/project1` لرؤية الموقع مباشرة (قد يستغرق بضع دقائق حتى يصبح نشطًا).

### مثال للنطاق الفرعي المخصص مع نطاق مخصص
إذا كنت تريد `project1.example.com`:
1. امتلك نطاقًا (مثل `example.com`).
2. في إعدادات موفر DNS الخاص بك، أضف سجل CNAME:
   - الاسم: `project1`
   - القيمة: `username.github.io`
3. في إعدادات **الصفحات** الخاصة بمستودع `project1`، عيّن النطاق المخصص إلى `project1.example.com`.
4. ادفع المحتوى إلى مستودع `project1`، وسيتم تقديمه على `project1.example.com`.

### القيود
- **المسارات الفرعية فقط لـ `github.io`**: بدون نطاق مخصص، يتم دائمًا تقديم مواقع المشاريع كمسارات فرعية (`username.github.io/project1`)، وليس كنطاقات فرعية (`project1.username.github.io`).
- **موقع مستخدم واحد**: مستودع `username.github.io` الخاص بك محجوز لموقع المستخدم الخاص بك. تستخدم مواقع المشاريع مستودعات أخرى وتظهر كمسارات فرعية.
- **النطاقات الفرعية المخصصة تتطلب نطاقًا مخصصًا**: للحصول على `project1.something`، تحتاج إلى امتلاك `something` (مثل `example.com`) وتكوين DNS.
- **المستودعات الخاصة**: مواقع المشاريع في المستودعات الخاصة تتطلب GitHub Pro أو Team أو Enterprise. للحسابات المجانية، يجب أن تكون المستودعات عامة.

### الملخص
- **استخدم `username.github.io/project1`**: نعم، هذا مدعوم بشكل أصلي عن طريق إنشاء مستودع (`username/project1`) وتمكين GitHub Pages. يمكنك إنشاء مواقع مشاريع متعددة بهذه الطريقة (مثل `username.github.io/project2`، إلخ).
- **استخدم `project1.username.github.io`**: لا، هذا غير مدعوم تحت `github.io`. ستحتاج إلى نطاق مخصص (مثل `project1.example.com`) وإعداد DNS لتحقيق تأثير مماثل.
- **نطاقات فرعية متعددة**: للحصول على نطاقات فرعية متعددة `*.github.io`، أنشئ منظمات على GitHub (كما نوقش سابقًا) لـ `org1.github.io`، `org2.github.io`، إلخ، أو استخدم نطاقًا مخصصًا للنطاقات الفرعية مثل `project1.example.com`.

إذا كنت بحاجة إلى مساعدة في إعداد موقع مشروع معين، أو تكوين نطاق مخصص، أو إدارة مواقع متعددة، دعني أعلم!
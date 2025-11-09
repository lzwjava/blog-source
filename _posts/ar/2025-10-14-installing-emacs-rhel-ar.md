---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: تثبيت إيماكس على آر إتش إل
translated: true
type: note
---

### تثبيت Emacs على Red Hat Enterprise Linux

يستخدم Red Hat Enterprise Linux (RHEL) بشكل أساسي مدير الحزم DNF لتثبيت البرامج. يتوفر Emacs في المستودعات الافتراضية، لذا فإن عملية التثبيت مباشرة. فيما يلي الخطوات للإصدارات الحديثة (RHEL 8 والإصدارات الأحدث). للإصدارات الأقدم (مثل RHEL 7)، استبدل `dnf` بـ `yum`.

#### المتطلبات الأساسية
- تأكد من أن لديك صلاحيات المستخدم root (استخدم `sudo`).
- يجب أن يكون نظامك مسجلاً في Red Hat Subscription Management إذا كنت تستخدم المستودعات الرسمية لـ RHEL.

#### خطوات التثبيت
1.  **حدّث ذاكرة التخزين المؤقت للحزم** (يُوصى به لضمان الحصول على أحدث إصدار متاح):  
    ```
    sudo dnf update
    ```

2.  **ثبّت Emacs**:  
    ```
    sudo dnf install emacs
    ```  
    سيؤدي هذا إلى تثبيت أحدث إصدار مستقر متاح في المستودعات (مثل Emacs 28.x أو 29.x، اعتمادًا على إصدار RHEL الخاص بك).

3.  **تحقق من التثبيت**:  
    قم بتشغيل الأمر التالي للتحقق من الإصدار:  
    ```
    emacs --version
    ```  
    يجب أن ترى ناتجًا مشابهًا لـ `GNU Emacs 28.2` (أو ما يشابه ذلك).

#### ملاحظات
- إذا كنت تستخدم إصدارًا قديمًا من RHEL يستخدم YUM (مثل RHEL 7)، فالأمر هو `sudo yum install emacs`.
- للحصول على أحدث إصدار من Emacs (مثل 29+)، قد تحتاج إلى التجميع من المصدر أو استخدام مستودعات خارجية مثل EPEL، حيث أن المستودعات الأساسية قد تتأخر في التحديث.
- لبدء تشغيل Emacs، ما عليك سوى كتابة `emacs` في الطرفية.

[أسئلة شائعة حول GNU Emacs: تثبيت Emacs](https://www.gnu.org/software/emacs/manual/html_node/efaq/Installing-Emacs.html)  
[توثيق Red Hat: إدارة البرامج باستخدام DNF](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/managing_software_with_the_dnf_tool/index)
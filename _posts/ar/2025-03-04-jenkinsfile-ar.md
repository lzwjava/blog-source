---
audio: false
generated: true
lang: ar
layout: post
title: كتابة ملف جنكينز
translated: true
type: note
---

لكتابة Jenkinsfile يدمج مكتبة مشتركة، ومعامل نصي، وكتابة try-catch، وكتابة node، وبيان شرطي if، يمكنك اتباع النهج التالي. تُكتب ملفات Jenkins بلغة Groovy ويمكنها تعريف خط أنابيب لأتمتة عمليات البناء والاختبار والنشر. فيما يلي مثال كامل لـ Jenkinsfile نصي يستوفي هذه المتطلبات.

أولاً، لاستخدام مكتبة مشتركة، تحتاج إلى استيرادها باستخدام الشرحة `@Library`. تحتوي المكتبات المشتركة في Jenkins على كود قابل لإعادة الاستخدام يمكن استدعاؤه من خطوط أنابيب متعددة. على سبيل المثال، إذا كانت مكتبتك المشتركة تحمل اسم `my-shared-library`، فقم بتضمينها في أعلى ملف Jenkinsfile هكذا:

```groovy
@Library('my-shared-library') _
```

الشرطة السفلية (`_`) بعد الشرحة مطلوبة لاستيراد المكتبة بشكل صحيح.

بعد ذلك، لتعريف معامل نصي، استخدم خطوة `properties`. هذا يسمح للمستخدمين بتمرير قيمة نصية إلى خط الأنابيب عند تشغيله. إليك كيفية إضافة معامل نصي باسم `MY_STRING`:

```groovy
properties([
    parameters([
        string(name: 'MY_STRING', defaultValue: 'default', description: 'A string parameter')
    ])
])
```

تحدد كتلة `node` مكان تنفيذ خط الأنابيب، مثل أي وكيل متاح. داخل هذه الكتلة، يمكنك تضمين منطق خط الأنابيب الخاص بك:

```groovy
node {
    // Pipeline steps go here
}
```

لمعالجة الأخطاء المحتملة، قم بتغليف خطواتك في كتلة `try-catch`. يضمن ذلك أنه في حالة فشل شيء ما، يمكنك التقاط الاستثناء والتعامل معه بأمان. بالإضافة إلى ذلك، يمكن استخدام بيان `if` لاتخاذ القرارات بناءً على قيمة المعامل النصي (`params.MY_STRING`).

إليك ملف Jenkinsfile الكامل الذي يجمع كل هذه العناصر:

```groovy
@Library('my-shared-library') _

properties([
    parameters([
        string(name: 'MY_STRING', defaultValue: 'default', description: 'A string parameter')
    ])
])

node {
    try {
        // Call a function from the shared library (assuming it exists)
        myLibraryFunction()
        
        // Use an if statement based on the string parameter
        if (params.MY_STRING == 'test') {
            echo "Running test"
        } else {
            echo "Not running test"
        }
    } catch (Exception e) {
        echo "An error occurred: ${e.message}"
    }
}
```

### شرح المكونات

- **`@Library('my-shared-library') _`**: تستورد مكتبة مشتركة باسم `my-shared-library`. استبدل `my-shared-library` بالاسم الفعلي لمكتبتك. يُفترض أن الدالة `myLibraryFunction()` معرفة في هذه المكتبة.
- **`properties`**: تعرف معامل نصي `MY_STRING` بقيمة افتراضية `'default'` ووصف. يمكنك الوصول إلى هذا المعامل في خط الأنابيب باستخدام `params.MY_STRING`.
- **`node`**: تشغل خط الأنابيب على أي وكيل متاح. يمكنك تحديد وكيل معين (مثل `node('linux')`) إذا لزم الأمر.
- **`try-catch`**: تنفذ الخطوات داخل كتلة `try` وتلتقط أي استثناءات في كتلة `catch`، وتطبع رسالة خطأ إذا حدث خطأ ما.
- **`if`**: تتحقق مما إذا كانت `MY_STRING` تساوي `'test'` وتطبع رسالة وفقًا لذلك. يمكنك تعديل الشرط والإجراءات حسب الحاجة.

### ملاحظات
- يفترض هذا المثال خط أنابيب نصي، والذي يوفر مرونة أكبر مع بناء جملة Groovy. إذا كنت بحاجة إلى خط أنابيب تصريحي بدلاً من ذلك، فسيختلف الهيكل قليلاً (على سبيل المثال، استخدام كتل `pipeline` و `script` للكود المكتوب بـ Groovy).
- استدعاء `myLibraryFunction()` هو عنصر نائب. تأكد من أن مكتبتك المشتركة تعرف هذه الدالة، أو استبدلها بدالة فعلية من مكتبتك.
- يمكنك توسيع ملف Jenkinsfile هذا بإضافة مراحل (مثل `stage('Build')`) أو منطق أكثر تعقيدًا اعتمادًا على متطلباتك.

يوفر ملف Jenkinsfile هذا أساسًا متينًا يتضمن جميع العناصر التي طلبتها: مكتبة مشتركة، ومعامل نصي، وكتابة try-catch، وكتابة node، وبيان شرطي if. قم بتعديل التفاصيل (اسم المكتبة، استدعاءات الدوال، أو الشروط) لتناسب حالة استخدامك!
---
audio: false
generated: true
lang: ar
layout: post
title: كتابة ملف Jenkins
translated: true
---

لإعداد ملف Jenkinsfile يتضمن مكتبة مشتركة، معلمة نصية، كتلة try-catch، كتلة node، و بيان if، يمكنك استخدام النهج التالي. يتم كتابة ملفات Jenkinsfile باستخدام Groovy ويمكن أن تعرّف pipeline لتوثيق عمليات البناء، الاختبار، والتوزيع. أدناه مثال كامل لملف Jenkinsfile مكتوب باستخدام Groovy يفي بهذه المتطلبات.

أولاً، لاستخدام مكتبة مشتركة، يجب عليك استيرادها باستخدام تعليق `@Library`. تحتوي المكتبات المشتركة في Jenkins على كود قابل لإعادة الاستخدام يمكن استدعاؤه من عدة pipelines. على سبيل المثال، إذا كانت مكتبة مشتركة تحمل اسم `my-shared-library`، فستدرجها في أعلى ملف Jenkinsfile كما يلي:

```groovy
@Library('my-shared-library') _
```

الخط السفلي (`_`) بعد التعليق مطلوب لاستيراد المكتبة بشكل صحيح.

بعد ذلك، لتحديد معلمة نصية، استخدم خطوة `properties`. هذا يسمح للمستخدمين بعبور قيمة نصية إلى pipeline عند تشغيلها. إليك كيفية إضافة معلمة نصية تحمل اسم `MY_STRING`:

```groovy
properties([
    parameters([
        string(name: 'MY_STRING', defaultValue: 'default', description: 'A string parameter')
    ])
])
```

تحدد كتلة `node` مكان تنفيذ pipeline، مثل على أي وكيل متاح. داخل هذه الكتلة، يمكنك تضمين منطق pipeline:

```groovy
node {
    // Pipeline steps go here
}
```

للمحاولة في التعامل مع الأخطاء المحتملة، قم بتغليف خطواتك في كتلة `try-catch`. هذا يضمن أن إذا حدث خطأ ما، يمكنك القبض على الاستثناء وتعامل معه بشكل لائق. بالإضافة إلى ذلك، يمكن استخدام بيان `if` لتخاذ قرارات بناءً على قيمة المعلمة النصية (`params.MY_STRING`).

إليك ملف Jenkinsfile الكامل يجمع جميع هذه العناصر:

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

- **`@Library('my-shared-library') _`**: يستورد مكتبة مشتركة تحمل اسم `my-shared-library`. قم بإعادة تسمية `my-shared-library` باسم مكتبةك الفعلي. يتم افتراض أن الدالة `myLibraryFunction()` تم تعريفها في هذه المكتبة.
- **`properties`**: يحدد معلمة نصية `MY_STRING` مع قيمة افتراضية هي `'default'` و وصف. يمكنك الوصول إلى هذه المعلمة في pipeline باستخدام `params.MY_STRING`.
- **`node`**: ينفذ pipeline على أي وكيل متاح. يمكنك تحديد وكيل معين (مثل `node('linux')`) إذا كان ذلك ضرورياً.
- **`try-catch`**: ينفذ الخطوات داخل كتلة `try` ويقبض على أي استثناءات في كتلة `catch`، ويطبع رسالة خطأ إذا حدث خطأ ما.
- **`if`**: يحدد إذا كانت `MY_STRING` تساوي `'test'` ويطبع رسالة بشكل مناسب. يمكنك تعديل الشروط والأفعال حسب الحاجة.

### الملاحظات

- يرجح هذا المثال pipeline مكتوب باستخدام Groovy، والذي يوفر مرونة أكبر مع Groovy. إذا كنت تحتاج إلى pipeline تعرفي، فسيختلف الهيكل قليلاً (مثل استخدام `pipeline` و `script` للكود Groovy).
- `myLibraryFunction()` هو مكانة. تأكد من أن مكتبة مشتركة تعرّف هذه الدالة، أو قم بإعادة تسميةها بدالة فعليّة من مكتبةك.
- يمكنك توسيع هذا ملف Jenkinsfile بإضافة مراحل (مثل `stage('Build')`) أو منطق أكثر تعقيدًا حسب احتياجاتك.

يوفر هذا ملف Jenkinsfile أساسًا قويًا يتضمن جميع العناصر التي طلبتها: مكتبة مشتركة، معلمة نصية، كتلة try-catch، كتلة node، و بيان if. قم بتعديل التفاصيل (اسم المكتبة، استدعاءات الدوال، أو الشروط) لتناسب حالة الاستخدام الخاصة بك!
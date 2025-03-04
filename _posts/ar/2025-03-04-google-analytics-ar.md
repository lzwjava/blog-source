---
audio: false
generated: true
lang: ar
layout: post
title: استخدام Google Analytics
translated: true
---

لاستخدام Google Analytics، قم بتكامله في مشروعك الأمامي، وتحقق من البيانات باستخدام التطبيق والموقع، اتبع هذه الخطوات. يفترض هذا الدليل أن مشروعك الأمامي هو إما موقع ويب أو تطبيق موبايل ويستخدم **Google Analytics 4 (GA4)**، وهو المعيار الحالي اعتبارًا من عام 2023، حيث لا يتم دعم Universal Analytics anymore للجمع الجديد من البيانات.

---

### 1. إعداد Google Analytics
قبل تكامل Google Analytics في مشروعك، عليك إنشاء حساب وتكوينه:

- **إنشاء حساب**: اذهب إلى [analytics.google.com](https://analytics.google.com) و سجل الدخول باستخدام حساب Google الخاص بك إذا لم يكن لديك حساب بالفعل.
- **إنشاء خاصية GA4**:
  - انقر على "Admin" في الزاوية اليسرى السفلى.
  - تحت "Property," انقر على "Create Property," واملأ تفاصيل مشروعك، واختر **Google Analytics 4**.
- **إضافة تدفق البيانات**: حسب نوع مشروعك الأمامي:
  - **للموقع الإلكتروني**: اختر "Web," أدخل عنوان URL لموقعك الإلكتروني، واسم تدفق البيانات (مثلًا "My Website").
  - **للتطبيق الموبايل**: اختر "App," واختر iOS أو Android، وقدم تفاصيل التطبيق الخاص بك (مثلًا اسم الحزمة).

بعد إعداد تدفق البيانات، ستحصل على **معرف القياس** (مثلًا `G-XXXXXXXXXX`), الذي ستستخدمه للتكامل.

---

### 2. تكامل Google Analytics في مشروعك الأمامي
يتوقف عملية التكامل على ما إذا كان مشروعك الأمامي هو موقع ويب أو تطبيق موبايل.

#### لموقع ويب
- **إضافة العلامة**:
  - في خاصيتك GA4، اذهب إلى "Data Streams," اختر تدفق ويبك، واكتشف "Tagging Instructions."
  - انقر على **Google Tag** النص، الذي يبدو هكذا:
    ```html
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=YOUR_MEASUREMENT_ID"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'YOUR_MEASUREMENT_ID');
    </script>
    ```
  - ألصق هذا الكود في قسم `<head>` من HTML لموقعك الإلكتروني، استبدل `YOUR_MEASUREMENT_ID` بمعرف القياس الفعلي.
- **للتطبيقات ذات الصفحة الواحدة (SPAs)** (مثل React, Angular, Vue):
  - يتبع النص الافتراضي فقط تحميل الصفحة الأولي. لل SPAs، حيث لا يتم إعادة تحميل الصفحات عند تغييرات الطريق، استخدم مكتبة لتتبع التنقل. على سبيل المثال، في **React**:
    1. قم بتثبيت مكتبة `react-ga4`:
       ```bash
       npm install react-ga4
       ```
    2. قم بتشغيله في تطبيقك (مثلًا في `index.js` أو `App.js`):
       ```javascript
       import ReactGA from 'react-ga4';
       ReactGA.initialize('YOUR_MEASUREMENT_ID');
       ```
    3. تتبع مشاهدات الصفحة عند تغييرات الطريق (مثلًا باستخدام React Router):
       ```javascript
       ReactGA.send({ hitType: "pageview", page: window.location.pathname });
       ```
       استدع هذا كلما تغير الطريق، مثلًا في `useEffect` مرتبط بموقع الموجه.
  - توجد مكتبات مماثلة لأطر العمل الأخرى (مثل `ngx-analytics` لـ Angular، `vue-ga` لـ Vue—تحقق من توافق GA4).
- **اختياري**: استخدم **Google Tag Manager** (GTM) بدلاً من كتابة العلامة بشكل صريح لإدارة أسهل للScripts تتبع.

#### لتطبيق موبايل
- **استخدام Firebase (موصى به)**:
  - إذا كان تطبيقك يستخدم Firebase، قم بتفعيل **Google Analytics for Firebase**:
    1. قم بإنشاء مشروع Firebase في [console.firebase.google.com](https://console.firebase.google.com).
    2. أضف تطبيقك إلى المشروع (iOS أو Android).
    3. اتبع التعليمات لتنزيل ملف التكوين (مثلًا `GoogleService-Info.plist` لـ iOS، `google-services.json` لـ Android) واضفه إلى تطبيقك.
    4. قم بتثبيت SDK Firebase:
       - **iOS**: استخدم CocoaPods (`pod 'Firebase/Analytics'`) وابدأ في `AppDelegate`.
       - **Android**: أضف الاعتماديات في `build.gradle` وابدأ في تطبيقك.
    5. Firebase يربط تلقائيًا إلى خاصيتك GA4 ويبدأ في جمع البيانات.
- **بدون Firebase**:
  - استخدم **Google Analytics SDK** المستقلة لـ iOS أو Android (أقل شيوعًا الآن مع التكامل GA4 Firebase). راجع الوثائق الرسمية لتكوينه، حيث تختلف حسب المنصة.

---

### 3. التحقق من التكامل
- **لمواقع الويب**: بعد إضافة كود تتبع:
  - زور موقعك الإلكتروني وفتح تقرير **Real-time** في Google Analytics (تحت "Reports" > "Real-time").
  - إذا رأيت زيارتك مسجلة، فإن التكامل يعمل.
  - أو استخدم أداة متصفح مثل **GA Checker** أو Chrome DevTools console لتأكيد استدعاءات `gtag`.
- **للأجهزة**: تحقق من Firebase Console أو GA4 Real-time report بعد إطلاق تطبيقك مع SDK مثبت. قد يستغرق ذلك دقائق قليلة حتى تظهر البيانات.

---

### 4. التحقق من البيانات باستخدام التطبيق والموقع
بعد أن يبدأ Google Analytics في جمع البيانات، يمكنك مشاهدتها بطريقتين:
- **واجهة ويب Google Analytics**:
  - سجل الدخول إلى [analytics.google.com](https://analytics.google.com).
  - اختر خاصيتك GA4.
  - استكشف التقارير مثل:
    - **Real-time**: شاهد نشاط المستخدم الحي.
    - **Audience**: فهم ديموغرافيا المستخدم.
    - **Acquisition**: تتبع من أين يأتي المستخدمون.
    - **Behavior**: تحليل تفاعلات المستخدم (مثل مشاهدات الصفحة، الأحداث).
- **تطبيق Google Analytics الموبايل**:
  - قم بتنزيل **تطبيق Google Analytics الرسمي** من App Store (iOS) أو Google Play Store (Android).
  - سجل الدخول باستخدام حساب Google الخاص بك واختار خاصيتك.
  - مشاهدة مجموعة من التقارير (مثل Real-time, Audience) أثناء السفر.

---

### ملاحظات إضافية
- **إذا كان مشروعك يتضمن كلا من الموقع الإلكتروني والتطبيق**: يمكنك إضافة تدفقات بيانات متعددة (مثلًا واحدة للموقع الإلكتروني، واحدة للتطبيق) تحت نفس خاصية GA4. وهذا يسمح لك بمشاهدة تحليلات مشتركة أو منفصلة في نفس الواجهة.
- **تتبع الأحداث**: بالإضافة إلى مشاهدات الصفحة، تتبع الأحداث المخصصة (مثل النقرات على الأزرار) باستخدام `gtag('event', ...)` لمواقع الويب أو Firebase’s `logEvent` للأجهزة. مثال لموقع الويب:
  ```javascript
  gtag('event', 'click', {
    'event_category': 'Button',
    'event_label': 'Submit'
  });
  ```
- **GA4 مقابل Universal Analytics**: استخدم GA4 لمشاريع جديدة، حيث توقف Universal Analytics عن معالجة البيانات بعد 1 يوليو 2023.

بالتتبع لهذه الخطوات، ستنجح في تكامل Google Analytics في مشروعك الأمامي وستمكن من مراقبة بيانات المستخدم باستخدام كلا من موقع ويب Google Analytics والتطبيق الموبايل. إذا كان نوع مشروعك (موقع ويب أو تطبيق) يتطلب توضيحًا خاصًا، قم بتعديل خطوات التكامل وفقًا لذلك!
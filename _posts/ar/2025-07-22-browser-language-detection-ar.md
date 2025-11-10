---
audio: false
generated: true
lang: ar
layout: post
title: كشف تفضيلات لغة المستخدم
translated: true
type: note
---

### اكتشاف بلد المستخدم أو تفضيل اللغة

بما أن مدونة Jekyll الخاصة بك ثابتة (HTML/JS مُنشأة مسبقًا)، لا يمكنك بسهولة إجراء الاكتشاف من جانب الخادم دون التكامل مع منصة استضافة تدعم ذلك (مثل دوال Netlify أو GitHub Pages مع قيود). أفضل نهج هو اكتشاف JavaScript من جانب العميل عند تحميل الصفحة. لديك خياران رئيسيان:

1.  **تفضيل لغة المتصفح** (موصى به لحالة استخدامك): يكتشف هذا اللغة المفضلة للمستخدم من إعدادات المتصفح (عبر `navigator.language` أو `navigator.languages`). إنه سريع، لا يتطلب واجهات برمجة تطبيقات خارجية، يحترم خصوصية المستخدم (لا مشاركة عنوان IP)، ويرتبط مباشرة باللغة بدلاً من البلد. غالبًا ما تحتوي البلدان على لغات متعددة (مثل الهند التي تستخدم الإنجليزية على نطاق واسع إلى جانب الهندية)، لذا فهذا أكثر دقة للإعداد التلقائي للقائمة المنسدلة.

2.  **اكتشاف البلد بناءً على عنوان IP**: يستخدم هذا واجهة برمجة تطبيقات مجانية لتحديد الموقع الجغرافي للحصول على البلد من عنوان IP للمستخدم، ثم يعينه إلى لغة. إنه مفيد إذا كنت تحتاج تحديدًا إلى معلومات البلد (على سبيل المثال، للتحليلات)، لكنه يتطلب جلب بيانات خارجي، وقد يكون له آثار على الخصوصية، وليس دقيقًا دائمًا (شبكات VPN، الوكائل). إن تعيين البلد إلى اللغة هو أمر تقريبي.

يبدو أن هدفك هو التحديد التلقائي للغة في القائمة المنسدلة `<select id="sort-select">` (على سبيل المثال، 'date-desc|en' للإنجليزية). سأقدم كودًا لكلتا الطريقتين، يمكنك إضافته داخل علامة `<script>` الخاصة بك، مباشرة بعد `const sortSelect = document.getElementById('sort-select');`.

قم بإعطاء الأولية للتحقق من `localStorage` (كما يفعل الكود الخاص بك بالفعل)، ثم انتقل إلى الاكتشاف إذا لم تكن هناك تفضيلات محفوظة.

#### الخيار 1: استخدام لغة المتصفح (أبسط ومفضل)
أضف مقتطف الكود هذا. يتحقق من رمز اللغة الأساسي من `navigator.language` (على سبيل المثال، 'en-US' -> 'en', 'zh-CN' -> 'zh') ويعينه إلى قيم القائمة المنسدلة الخاصة بك. افتراضيًا، ينتقل إلى الإنجليزية إذا لم يتم العثور على تطابق.

```javascript
// Inside window.addEventListener('load', function () { ... });

// After const sortSelect = ...;

// Restore from localStorage if available
const savedSort = localStorage.getItem('sortOption');
if (savedSort) {
  sortSelect.value = savedSort;
} else {
  // Detect browser language if no saved preference
  let lang = navigator.language.toLowerCase().split('-')[0]; // e.g., 'en-US' -> 'en'
  
  // Special handling for Chinese variants (zh-Hant for traditional)
  if (lang === 'zh') {
    const fullLang = navigator.language.toLowerCase();
    if (fullLang.includes('tw') || fullLang.includes('hk') || fullLang.includes('hant')) {
      lang = 'hant';
    } else {
      lang = 'zh'; // Simplified Chinese
    }
  }

  // Map to your dropdown options (add more if needed)
  const langMap = {
    'en': 'date-desc|en',
    'zh': 'date-desc|zh',
    'ja': 'date-desc|ja',
    'es': 'date-desc|es',
    'hi': 'date-desc|hi',
    'fr': 'date-desc|fr',
    'de': 'date-desc|de',
    'ar': 'date-desc|ar',
    'hant': 'date-desc|hant'
  };

  sortSelect.value = langMap[lang] || 'date-desc|en'; // Default to English
}

updatePosts();
```

يعمل هذا بشكل متزامن عند التحميل، لذا لا يوجد تأخير. اختبره عن طريق تغيير إعدادات لغة المتصفح الخاص بك (على سبيل المثال، في Chrome: الإعدادات > اللغات).

#### الخيار 2: استخدام اكتشاف البلد بناءً على عنوان IP
هذا يتطلب جلب بيانات غير متزامن من واجهة برمجة تطبيقات مجانية. أوصي بـ `country.is` لأنها بسيطة وتُرجع فقط رمز البلد (على سبيل المثال، {country: 'US'}). إنها مجانية، لا تتطلب مفتاح واجهة برمجة تطبيقات، ومفتوحة المصدر.

أضف هذا الكود. ملاحظة: إنه غير متزامن، لذا نستخدم `await` ونلفه في دالة async لتجنب حجب واجهة المستخدم. إذا فشل الجلب (على سبيل المثال، بسبب أدوات حظر الإعلانات)، فإنه ينتقل افتراضيًا إلى الإنجليزية.

```javascript
// Inside window.addEventListener('load', async function () { ... });  // Make the load handler async

// After const sortSelect = ...;

// Restore from localStorage if available
const savedSort = localStorage.getItem('sortOption');
if (savedSort) {
  sortSelect.value = savedSort;
  updatePosts();
} else {
  try {
    // Fetch country code
    const response = await fetch('https://country.is/');
    const data = await response.json();
    const country = data.country.toUpperCase(); // e.g., 'US'

    // Map country codes to your languages (ISO 3166-1 alpha-2 codes)
    // This is approximate; expand as needed (e.g., multiple countries per language)
    const countryLangMap = {
      'US': 'date-desc|en',  // USA -> English
      'GB': 'date-desc|en',  // UK -> English
      'CN': 'date-desc|zh',  // China -> Simplified Chinese
      'TW': 'date-desc|hant', // Taiwan -> Traditional Chinese
      'HK': 'date-desc|hant', // Hong Kong -> Traditional Chinese
      'JP': 'date-desc|ja',  // Japan -> Japanese
      'ES': 'date-desc|es',  // Spain -> Spanish
      'MX': 'date-desc|es',  // Mexico -> Spanish (example for Latin America)
      'IN': 'date-desc|hi',  // India -> Hindi
      'FR': 'date-desc|fr',  // France -> French
      'DE': 'date-desc|de',  // Germany -> German
      'SA': 'date-desc|ar',  // Saudi Arabia -> Arabic
      'AE': 'date-desc|ar'   // UAE -> Arabic
    };

    sortSelect.value = countryLangMap[country] || 'date-desc|en'; // Default to English
  } catch (error) {
    console.warn('Country detection failed:', error);
    sortSelect.value = 'date-desc|en'; // Fallback
  }

  updatePosts();
}
```

-   **ملاحظات**:
    -   قم بتحديث `window.addEventListener` إلى `async function ()` كما هو موضح.
    -   للخصوصية: أبلغ المستخدمين إذا لزم الأمر (GDPR في الاتحاد الأوروبي). قد تمنع بعض المتصفحات/واجهات برمجة التطبيقات طلبات cross-origin؛ اختبر بدقة.
    -   إذا كنت تفضل واجهة برمجة تطبيقات مختلفة، تشمل البدائل `https://ip-api.com/json/` (تُرجع المزيد من البيانات مثل `{ "countryCode": "US" }`) أو `https://ipgeolocation.io/ip_location/` (سجل للحصول على الطبقة المجانية).
    -   حدود المعدل: هذه واجهات برمجة تطبيقات سخية للمدونات الشخصية، لكن راقب إذا زادت حركة المرور.

#### اعتبارات إضافية
-   **التراجع وتجاوز المستخدم**: يمكن للمستخدمين دائمًا تغيير القائمة المنسدلة، ويتم حفظها في localStorage. يمكنك إضافة زر "اكتشاف اللغة" إذا لم يكن الاكتشاف التلقائي مرغوبًا دائمًا.
-   **الاختبار**: استخدم شبكات VPN لمحاكاة بلدان مختلفة أو امتدادات المتصفح لانتحال اللغات.
-   **الخصوصية**: لغة المتصفح منخفضة المخاطر. لطرق IP، فكر في إضافة موافقة إذا كان جمهورك حساسًا.
-   **الجمع بين الاثنين**: استخدم لغة المتصفح أولاً، ثم IP إذا لم تتطابق مع اللغات المدعومة لديك (ولكن حافظ على البساطة).
-   **خاص بـ Jekyll**: لا حاجة لتغييرات في إعدادات Jekyll. إذا استضفت على Netlify/Vercel، يمكنك استخدام edge functions للاكتشاف من جانب الخادم، لكن هذا مبالغ فيه هنا.

إذا لم يعمل هذا أو يمكنك مشاركة الأخطاء، قدم المزيد من التفاصيل!

[Country.is API](https://country.is/)  
[IP-API Geolocation](https://ip-api.com/)  
[ipgeolocation.io](https://ipgeolocation.io/)
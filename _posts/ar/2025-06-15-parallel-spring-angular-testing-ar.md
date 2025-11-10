---
audio: false
generated: true
image: false
lang: ar
layout: post
title: اختبار المتصفح الزاوي للينابيع المتوازية
translated: true
type: note
---

فهمت — تريد طريقة عملية لاختبار موقع Spring (Java) + Angular الخاص بك في **Edge و Chrome بشكل متوازٍ**، بشكل أساسي **يدويًا** (مع القليل من الأتمتة الخفيفة حيثما تساعد). إليك سير عمل مجرب يمنع ظهور الجداول العريضة.

---

# 1) إعداد متصفحين نظيفين ومتشابهين

* **ثبّت أحدث إصدار مستقر** من Chrome و Edge. دوّن ملاحظة بالإصدارات.
* أنشئ **ملفات تعريف منفصلة ونظيفة** للاختبار في كل منهما:

  * Chrome: `chrome --user-data-dir=/tmp/chrome-qa --no-first-run`
  * Edge: `msedge --user-data-dir=/tmp/edge-qa --no-first-run`
* طابق **التكبير (100%)**، و **نسبة وحدات البكسل للجهاز (DPR)**، و **اللغة**، و **سمة نظام التشغيل**، و **حزم الخطوط**، وقم بإيقاف تشغيل الإضافات.
* ثبت كلا المتصفحين جنبًا إلى جنب (شاشتان إذا أمكن). استخدم نفس **منطقة العرض viewport** (مثلاً، 1440×900).

---

# 2) تحضير backend مستقر + بيانات واقعية

* شغّل backend الخاص بـ Spring في **وضع Staging** مع بيانات أولية حتمية.
* فضّل **حسابات اختبار غير قابلة للتغيير** و **مجموعة بيانات معروفة** (مثلاً، Testcontainers لصور قاعدة البيانات أو برامج إعداد Flyway/Liquibase).
* للتبعيات غير المستقرة، استخدم استعارات **WireMock** (HTTP) بحيث يكون سلوك واجهة المستخدم قابلاً للتكرار.

---

# 3) عكس التفاعلات عبر المتصفحين (يدوي، ولكن متزامن)

للاختبار اليدوي المتوازي الحقيقي، اعكس النقرات والتمرير والكتابة من متصفح إلى الآخر:

* استخدم **Browsersync** كخادم وكيل محلي **لمزامنة التفاعلات**:

  ```bash
  npm i -g browser-sync
  browser-sync start --proxy "http://localhost:4200" --files "dist/**/*" --open "external"
  ```

  افتح عنوان URL الذي يتم تمريره عبر الخادم الوكيل في **Chrome** و **Edge**؛ سيتم عكس التمرير والنقرات وإدخالات النماذج.
  (رائع لمقارنة التخطيطات، والتحقق من التمرير/التركيز Hover/Focus، والتدفقات السريعة.)

> إذا لم تتمكن من استخدام الخادم الوكيل (قيود المصادقة، شبكة الشركة)، شغّل نافذتين والتزم **بقائمة خطوات** مضغوطة (أدناه) بالإضافة إلى مسجل شاشة بعرض منقسم.

---

# 4) قائمة التحقق cross-browser (شغّل كليهما في وقت واحد)

اعمل على هذه **بشكل متوازٍ** — نفس الخطوة في كلا المتصفحين قبل الانتقال إلى التالية.

* **Bootstrap والخطوط:** Flash of unstyled content (FOUC)، خطوط الأيقونات، الخطوط الاحتياطية.
* **التخطيط Layout:** الفجوات في Flex/Grid، الرؤوس والتذييلات الثابتة، تجاوز النص / علامة الحذف، التفاف النص في RTL/L10n.
* **النماذج:** الإكمال التلقائي، العناصر النائبة Placeholders، رسائل التحقق، مدخلات الأرقام/التواريخ، إدخال النص الصيني IME، النسخ/اللصق.
* **التركيز/لوحة المفاتيح:** ترتيب Tab، رؤية حلقة التركيز Focus ring، `:focus-visible` مقابل `:focus`، سلوكيات Enter/Esc، الاختصارات.
* **التمرير/النشط Hover/active:** القوائم، التلميحات Tooltips، تأثيرات التموج Ripple effects، فئات حالة Angular Material.
* **الملفات والتنزيلات:** مرشحات قبول إدخال الملف File input accept filters، السحب والإفلات Drag-and-drop، مطالبات التنزيل.
* **المصادقة/الجلسة Auth/session:** ملفات تعريف الارتباط Cookies، SameSite، عزل التخزين عبر علامات التبويب، انتهاء مهلة الجلسة وتدفقات تحديث الرمز المميز Refresh token flows.
* **التوجيه Routing:** الروابط العميقة Deep links، التحديث القاسي Hard refresh على مسار متداخل، مسار ارتداد لخطأ 404.
* **التخزين المؤقت Caching:** دورة تحديث Service Worker، إبطال الأصول القديمة Stale assets busting، سلوك الصفحة في وضع عدم الاتصال.
* **الوسائط وواجهات برمجة التطبيقات APIs:** getUserMedia/clipboard، أذونات الإشعارات.
* **فحص سريع لإمكانية الوصول Accessibility:** المعالم والأدوار Landmarks/Roles، تباين الألوان (في أدوات المطور DevTools)، التنقل بلوحة المفاتيح فقط.
* **التحقق السريع من الأداء Performance:** أدوات المطور → الأداء Performance، تحقق من المهام الطويلة Long tasks، و Lighthouse في **كلا** المتصفحين.

نصيحة: أبقِ **أدوات المطور مفتوحة** (F12) في كلا المتصفحين، مثبتة في الأسفل، وقارن تحذيرات **وحدة التحكم Console** (إطار العمل + سياسة أمان المحتوى CSP + رسائل إهمال الاستخدام Deprecation messages).

---

# 5) خصوصيات Angular التي تختلف غالبًا

* **كشف التغيير Change detection والعمليات غير المتزامنة Async:** توقيت المهمة الدقيقة Microtask timing يمكن أن يكشف عن ظروف تنافسية Race conditions بشكل مختلف؛ راقب دوارات التحميل Spinners وأزرار "حفظ" لمشاكل النقر المزدوج.
* **أخطاء Zone.js:** رفض promise غير معالج في أحد المتصفحين وليس الآخر — تحقق من وحدة التحكم.
* **سمات Angular Material:** تحقق من وضع الظلام/الضوء Dark/Light tokens، وضع التباين العالي High-contrast mode، ومخططات التركيز Focus outlines (غالبًا ما يقوم Edge بعرض التركيز بشكل مختلف قليلاً).
* **أنابيب i18n وتنسيقات التاريخ:** الاختلافات المحلية مع `DatePipe` و `Intl` في أنواع Chromium.

---

# 6) مشاكل Spring backend الشائعة

* **CORS وإعادة التوجيه Redirects:** نفس القواعد ولكن **Edge يعرض أحيانًا مشاكل طلب CORS المبدئي Preflight issues** في وقت أبكر أثناء التطوير**؛ تحقق من استجابات `OPTIONS` والرؤوس Headers.
* **نوع المحتوى Content-Type والضغط Compression:** تحقق من `application/json;charset=UTF-8` مقابل `application/json`؛ تحقق من gzip/br — عدم التطابق قد يظهر كـ "فشل في التحميل Failed to load" في أحد المتصفحين أولاً.
* **رؤوس الأمان Security headers:** CSP، HSTS، X-Frame-Options — السياسات الأكثر صرامة يمكن أن تمنع البرامج النصية/الأنماط المضمنة Inline scripts/styles بشكل مختلف.

---

# 7) اجعل "اليدوي" قابلاً للتكرار بطبقة رقيقة من الأتمتة

حتى إذا كنت لا تريد اختبار E2E كامل، قم بإعداد **إطار اختبار متصفح قصير وسريع** بحيث يمكن لـ CI تشغيل كل من Chrome و Edge على كل طلب دمج Pull Request. ستكتشف التراجعات Regression في وقت أبكر وتخفف من عبء الاختبار اليدوي.

### الخيار أ: Playwright (خياري الأول لتطبيقات Angular)

* عدّاد اختبار واحد، يُطلق إصدارات **Chrome Stable** و **Microsoft Edge**، ويعمل **بشكل متوازٍ**.
* `npm i -D @playwright/test`
* `npx playwright install chromium`
* مثال `playwright.config.ts`:

  ```ts
  import { defineConfig, devices } from '@playwright/test';

  export default defineConfig({
    testDir: './e2e',
    workers: 4, // التوازي Parallelism
    use: {
      baseURL: 'http://localhost:4200',
      trace: 'retain-on-failure',
    },
    projects: [
      {
        name: 'Chrome Stable',
        use: { ...devices['Desktop Chrome'], channel: 'chrome' },
      },
      {
        name: 'Microsoft Edge',
        use: { ...devices['Desktop Edge'], channel: 'msedge' },
      },
    ],
  });
  ```

  مواصفات اختبار أساسية (`e2e/smoke.spec.ts`):

  ```ts
  import { test, expect } from '@playwright/test';

  test('home loads and login works', async ({ page }) => {
    await page.goto('/');
    await expect(page.getByRole('heading', { name: 'Welcome' })).toBeVisible();
    await page.getByLabel('Email').fill('user@example.com');
    await page.getByLabel('Password').fill('Password123!');
    await page.getByRole('button', { name: 'Sign in' }).click();
    await expect(page.getByText('Dashboard')).toBeVisible();
  });
  ```

  التشغيل: `npx playwright test`

### الخيار ب: Cypress (عائلة Chromium، يشغّل Chrome و Edge)

* التوازي عبر مصفوفة CI (أو لوحة تحكم Cypress Dashboard).
* في CI، شغّل:

  * `cypress run --browser chrome`
  * `cypress run --browser edge`
* حافِظ على المواصفات مضغوطة (للاختبار الأساسي Smoke فقط) للبقاء "يدويًا أولاً".

### الخيار ج: Selenium Grid (إذا كنت تستخدم Selenium بالفعل)

* Selenium Grid في حاوية Docker يُشغّل **عُقد chromium/edge** في وقت واحد.

  ```yaml
  # docker-compose.yml
  services:
    selenium-hub:
      image: selenium/hub:4
      ports: ["4444:4444"]
    chrome:
      image: selenium/node-chrome:4
      shm_size: 2gb
      depends_on: [selenium-hub]
      environment: [SE_EVENT_BUS_HOST=selenium-hub]
    edge:
      image: selenium/node-edge:4
      shm_size: 2gb
      depends_on: [selenium-hub]
      environment: [SE_EVENT_BUS_HOST=selenium-hub]
  ```

  وجّه اختبارات WebDriver الخاصة بك إلى `http://localhost:4444/wd/hub` وشغّل مجموعات الاختبار Test suites بشكل متوازٍ.

---

# 8) CI "متوازي بشكل افتراضي"

* استخدم مهمة **مصفوفة Matrix job** (Chrome/Edge) وشغّل اختبارك الأساسي Smoke في Playwright/Cypress بشكل متوازٍ.
* استخدم Fail-fast لتوفير الوقت؛ أرفق **آثار التنفيذ Traces/مقاطع الفيديو** للمتصفح الذي فشل.
* كل ليلة، شغّل مجموعة أوسع قليلاً و **فحص Lighthouse** على كلا المتصفحين.

---

# 9) التصنيف السريع عند الاختلاف

* احصل على **HAR** من كل متصفح، وقارن الاستجابات (الحالة Status، الرؤوس Headers، التخزين المؤقت Caching).
* قارن **الأنماط المحسوبة Computed styles** للعنصر المعطوب (أدوات المطور DevTools → الأنماط Styles → المحسوبة Computed).
* بدّل بين **تقليل الحركة Reduced motion** و **الألوان الإجبارية Forced colors** للكشف عن مشاكل CSS متعلقة بإمكانية الوصول Accessibility.
* امسح **بيانات الموقع Site data** (لوحة Application) وكرر الاختبار لاستبعاد تأثير Service Worker القديم / ذاكرة التخزين المؤقت Caches.

---

# 10) القطع الأثرية Minimal artifacts للمحافظة عليها

* **قائمة تحقق واحدة مشتركة** (بتنسيق markdown) لفحوصاتك cross-browser.
* **سجل إصدارات Version ledger**: commit التطبيق، إصدارات Chrome/Edge، نظام التشغيل، الأعلام المهمة.
* أرفق **لقطات الشاشة Screenshots** (بنفس منطقة العرض viewport) لأي فرق بصري تقبله كـ "لن يتم إصلاحه Won’t fix".

---

إذا أردت، يمكنني إنشاء **هيكل Playwright** جاهز للتشغيل لتطبيق Angular الخاص بك (مع `npm scripts`، ومصفوفة CI، ومواصفتين للاختبار الأساسي Smoke)، أو **برنامج نصي Browsersync** مخصص لإعداد خادم التطوير Development server الخاص بك.
---
audio: false
generated: true
image: false
lang: ar
layout: post
model: openai/gpt-5
title: تهيئة بلايورايت مع إصدار محدد من كروم
translated: true
type: note
---

فهمت. تريد تكوين **Playwright** على نظام Windows بحيث يُطلق **ملف Chrome التنفيذي المحدد** مع **خيارات إطلاق** معينة (مثل `headless: true`) مباشرة في ملف `playwright.config.js` الخاص بك.

إليك كيف يمكنك القيام بذلك:

---

### 1. استخدم `executablePath` في إعداد Playwright الخاص بك
بشكل افتراضي، يستخدم Playwright متصفح Chromium المرفق معه، ولكن إذا كنت تريد **Google Chrome** (التثبيت الخاص بك)، فيجب أن تخبر Playwright بموقع ملف `chrome.exe`.

مثال على `playwright.config.js`:

```js
// playwright.config.js
import { defineConfig, devices } from '@playwright/test';
import path from 'path';

export default defineConfig({
  projects: [
    {
      name: 'Google Chrome',
      use: {
        browserName: 'chromium',
        // على نظام Windows، قدم المسار الكامل لملف chrome.exe
        channel: undefined, // تأكد من إلغاء تعيين القناة، لأننا سنستخدم executablePath
        executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
        headless: true,  // التشغيل في الوضع headless
        args: [
          '--disable-gpu',
          '--no-sandbox',
          '--disable-dev-shm-usage',
        ],
      },
    },
  ],
});
```

---

### 2. ملاحظات
- على نظام **Windows**، يكون مسار Chrome المعتاد هو:
  - `C:\Program Files\Google\Chrome\Application\chrome.exe`
  - أو `C:\Program Files (x86)\Google\Chrome\Application\chrome.exe`
- تأكد من **تهريب الشرطات المائلة العكسية** (`\\`) في سلاسل JavaScript.
- استخدم `headless: true` لفرض الوضع headless.
- يمكنك أيضًا تمرير أي وسائط سطر أوامر خاصة بـ Chromium في `args`.

---

### 3. تشغيل الإعداد
يمكنك الآن تشغيل الاختبارات باستخدام:

```bash
npx playwright test --project="Google Chrome"
```

---

✅ هذا سوف يُطلق **ملف Chrome التنفيذي المحدد** الخاص بك في **الوضع headless** مع الوسائط المحددة.

---

هل تريد أيضًا أن أوضح لك كيفية **التبديل الشرطي** بين متصفح Playwright Chromium المرفق وملف `chrome.exe` المثبت لديك (على سبيل المثال، للاستخدام في CI مقابل التطوير المحلي)؟
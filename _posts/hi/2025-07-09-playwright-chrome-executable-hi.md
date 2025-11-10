---
audio: false
generated: true
image: false
lang: hi
layout: post
model: openai/gpt-5
title: विशिष्ट क्रोम एक्ज़ीक्यूटेबल के साथ प्लेराइट कॉन्फ़िगर करना
translated: true
type: note
---

ठीक है। आप **Playwright** को Windows पर इस तरह कॉन्फ़िगर करना चाहते हैं कि यह आपके `playwright.config.js` में सीधे कुछ **लॉन्च विकल्पों** (जैसे `headless: true`) के साथ एक **विशिष्ट Chrome executable** लॉन्च करे।

यहां बताया गया है कि आप इसे कैसे कर सकते हैं:

---

### 1. अपनी Playwright कॉन्फ़िग में `executablePath` का उपयोग करें
डिफ़ॉल्ट रूप से, Playwright अपने बंडल किए गए Chromium का उपयोग करता है, लेकिन यदि आप **Google Chrome** (आपकी अपनी इंस्टॉलेशन) चाहते हैं, तो आपको Playwright को बताना होगा कि `chrome.exe` फ़ाइल कहाँ स्थित है।

उदाहरण `playwright.config.js`:

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
        // Windows पर, chrome.exe का पूरा पथ प्रदान करें
        channel: undefined, // सुनिश्चित करें कि channel सेट नहीं है, क्योंकि हम executablePath का उपयोग करेंगे
        executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
        headless: true,  // headless मोड में चलाएं
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

### 2. नोट्स
- **Windows** पर, Chrome का सामान्य पथ है:
  - `C:\Program Files\Google\Chrome\Application\chrome.exe`
  - या `C:\Program Files (x86)\Google\Chrome\Application\chrome.exe`
- JS स्ट्रिंग्स में **बैकस्लैश को एस्केप** (`\\`) करना सुनिश्चित करें।
- हेडलेस मोड को लागू करने के लिए `headless: true` का उपयोग करें।
- आप `args` में कोई भी Chromium CLI flags भी पास कर सकते हैं।

---

### 3. कॉन्फ़िग चलाएं
अब आप इसके साथ टेस्ट चला सकते हैं:

```bash
npx playwright test --project="Google Chrome"
```

---

✅ यह दिए गए arguments के साथ आपके **विशिष्ट Chrome executable** को **हेडलेस मोड** में लॉन्च करेगा।

---

क्या आप मुझे यह भी दिखाना चाहेंगे कि बंडल किए गए Playwright Chromium और आपके इंस्टॉल किए गए `chrome.exe` के बीच **सशर्त रूप से कैसे स्विच करें** (उदाहरण के लिए CI बनाम लोकल डेव के लिए)?
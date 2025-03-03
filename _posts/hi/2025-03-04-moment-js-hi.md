---
audio: false
generated: true
lang: hi
layout: post
title: Moment.js का उपयोग JavaScript में
translated: true
---

मैं आपको JavaScript में `moment` और `moment-timezone` लाइब्रेरी का उपयोग करने का तरीका दिखाऊंगा। ये तारीख और समय को संभालने के लिए लोकप्रिय लाइब्रेरी हैं।

1. पहले, अगर आपने पहले से नहीं किया है, तो पैकेज इंस्टॉल करें:
```bash
npm install moment moment-timezone
```

2. बेसिक उपयोग उदाहरण:

```javascript
// लाइब्रेरी इम्पोर्ट करें
const moment = require('moment');
const momentTimezone = require('moment-timezone');

// बेसिक Moment.js उपयोग
// वर्तमान तारीख और समय
const now = moment();
console.log(now.format('YYYY-MM-DD HH:mm:ss')); // उदाहरण के लिए, "2025-03-03 14:30:45"

// एक विशेष तारीख को पर्स
const date = moment('2025-12-25');
console.log(date.format('MMMM Do YYYY')); // "December 25th 2025"

// तारीखों को मैनिपुलेट करें
const tomorrow = moment().add(1, 'days');
console.log(tomorrow.format('ddd, MMM D')); // उदाहरण के लिए, "Tue, Mar 4"

// Moment-Timezone का उपयोग करें
// एक विशेष टाइमजोन में समय प्राप्त करें
const nyTime = momentTimezone.tz('America/New_York');
console.log(nyTime.format('YYYY-MM-DD HH:mm:ss z')); // टाइमजोन संक्षिप्त नाम शामिल है

// टाइमजोन के बीच समय को परिवर्तित करें
const localTime = moment();
const tokyoTime = localTime.clone().tz('Asia/Tokyo');
console.log(`Local: ${localTime.format('HH:mm')}`);
console.log(`Tokyo: ${tokyoTime.format('HH:mm')}`);

// सभी उपलब्ध टाइमजोन सूचीबद्ध करें
const timezones = momentTimezone.tz.names();
console.log(timezones); // टाइमजोन नामों का एक एर्रे
```

सामान्य फॉर्मेटिंग विकल्प:
- `YYYY`: 4-अंकों का वर्ष (2025)
- `MM`: 2-अंकों का महीना (03)
- `DD`: 2-अंकों का दिन (03)
- `HH`: 24-घंटे (14)
- `hh`: 12-घंटे (02)
- `mm`: मिनट (30)
- `ss`: सेकंड (45)
- `z`: टाइमजोन संक्षिप्त नाम

उपयोगी विधियाँ:
```javascript
// तारीख मैनिपुलेशन
moment().add(7, 'days');     // समय जोड़ें
moment().subtract(2, 'hours'); // समय घटाएं
moment().startOf('month');   // अवधि की शुरुआत
moment().endOf('month');     // अवधि की समाप्ति

// तारीख तुलना
moment().isBefore(date);
moment().isAfter(date);
moment().isSame(date);

// टाइमजोन ऑपरेशन
momentTimezone.tz('2025-03-03', 'America/Los_Angeles');
momentTimezone.tz.guess(); // उपयोगकर्ता के टाइमजोन का अनुमान लगाएं
```

नोट:
1. ये संस्करण (^2.14.1 और ^0.5.7) काफी पुराने हैं (लगभग 2016 के आसपास के)। विशेष संगतता आवश्यकताओं के अलावा, नए संस्करण का उपयोग करने की सलाह दी जाती है।
2. अब Moment.js को एक पुराना प्रोजेक्ट माना जाता है जो रखरखाव मोड में है। नए प्रोजेक्टों के लिए, आप `date-fns` या `luxon` जैसे विकल्पों का विचार कर सकते हैं।
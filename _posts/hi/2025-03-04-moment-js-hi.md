---
audio: false
generated: true
lang: hi
layout: post
title: जावास्क्रिप्ट में मोमेंट.जेएस का उपयोग
translated: true
type: note
---

मैं आपको JavaScript में `moment` और `moment-timezone` लाइब्रेरीज़ के उपयोग का तरीका दिखाऊंगा। ये dates और times को हैंडल करने के लिए प्रसिद्ध लाइब्रेरीज़ हैं।

1. सबसे पहले, पैकेज इंस्टॉल करें (अगर पहले से नहीं किया है):
```bash
npm install moment moment-timezone
```

2. बेसिक उपयोग के उदाहरण:

```javascript
// लाइब्रेरीज़ इम्पोर्ट करें
const moment = require('moment');
const momentTimezone = require('moment-timezone');

// बेसिक Moment.js उपयोग
// वर्तमान तारीख और समय
const now = moment();
console.log(now.format('YYYY-MM-DD HH:mm:ss')); // उदा., "2025-03-03 14:30:45"

// एक विशिष्ट तारीख पार्स करें
const date = moment('2025-12-25');
console.log(date.format('MMMM Do YYYY')); // "December 25th 2025"

// तारीखों में हेरफेर करें
const tomorrow = moment().add(1, 'days');
console.log(tomorrow.format('ddd, MMM D')); // उदा., "Tue, Mar 4"

// Moment-Timezone का उपयोग
// किसी विशिष्ट टाइमज़ोन में समय प्राप्त करें
const nyTime = momentTimezone.tz('America/New_York');
console.log(nyTime.format('YYYY-MM-DD HH:mm:ss z')); // टाइमज़ोन संक्षिप्त नाम शामिल करता है

// टाइमज़ोन के बीच समय बदलें
const localTime = moment();
const tokyoTime = localTime.clone().tz('Asia/Tokyo');
console.log(`Local: ${localTime.format('HH:mm')}`);
console.log(`Tokyo: ${tokyoTime.format('HH:mm')}`);

// सभी उपलब्ध टाइमज़ोन की सूची दें
const timezones = momentTimezone.tz.names();
console.log(timezones); // टाइमज़ोन नामों की array
```

सामान्य फॉर्मेटिंग विकल्प:
- `YYYY`: 4-अंकीय वर्ष (2025)
- `MM`: 2-अंकीय महीना (03)
- `DD`: 2-अंकीय दिन (03)
- `HH`: 24-घंटा (14)
- `hh`: 12-घंटा (02)
- `mm`: मिनट (30)
- `ss`: सेकंड (45)
- `z`: टाइमज़ोन संक्षिप्त नाम

उपयोगी मेथड्स:
```javascript
// तारीख में हेरफेर
moment().add(7, 'days');     // समय जोड़ें
moment().subtract(2, 'hours'); // समय घटाएं
moment().startOf('month');   // अवधि की शुरुआत
moment().endOf('month');     // अवधि का अंत

// तारीख की तुलना
moment().isBefore(date);
moment().isAfter(date);
moment().isSame(date);

// टाइमज़ोन ऑपरेशन
momentTimezone.tz('2025-03-03', 'America/Los_Angeles');
momentTimezone.tz.guess(); // उपयोगकर्ता का टाइमज़ोन अनुमान लगाएं
```

नोट्स:
1. ये वर्ज़न (^2.14.1 और ^0.5.7) काफी पुराने हैं (लगभग 2016 के)। विशिष्ट कम्पैटिबिलिटी आवश्यकताओं के अलावा, नवीनतम वर्ज़न का उपयोग करने पर विचार करें।
2. Moment.js को अब एक लेगेसी प्रोजेक्ट माना जाता है जो मेंटेनेंस मोड में है। नए प्रोजेक्ट्स के लिए, आप `date-fns` या `luxon` जैसे विकल्पों पर विचार कर सकते हैं।
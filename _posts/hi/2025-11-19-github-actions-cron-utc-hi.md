---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: GitHub एक्शन्स क्रॉन UTC समय का उपयोग करती है
translated: true
type: note
---

**GitHub Actions की शेड्यूल्ड वर्कफ़्लोज़ (जो `on: schedule:` ट्रिगर और cron सिंटैक्स का उपयोग करती हैं) हमेशा cron समय को UTC (समन्वित सार्वभौमिक समय) में समझती हैं।**

वर्कफ़्लो YAML में सीधे कोई अलग टाइमज़ोन निर्दिष्ट करने के लिए कोई अंतर्निहित सपोर्ट मौजूद नहीं है। यदि आप चाहते हैं कि कोई जॉब एक विशिष्ट स्थानीय समय (जैसे, सुबह 9:00 बजे PST) पर चले, तो आपको उस समय को समतुल्य UTC समय में बदलना होगा और उसी के अनुसार cron एक्सप्रेशन लिखना होगा।

### आधिकारिक दस्तावेज़ीकरण से मुख्य बिंदु:
- शेड्यूल्ड वर्कफ़्लोज़ POSIX cron सिंटैक्स का उपयोग करती हैं और विशिष्ट **UTC समय** पर चलती हैं।
- उदाहरण: `cron: '0 5 * * *'` प्रतिदिन सुबह 5:00 बजे UTC पर चलती है (आपके स्थानीय समय पर नहीं)।

यह वर्षों से सुसंगत रहा है और 2025 के अंत तक भी यही स्थिति बनी हुई है — `schedule` इवेंट के लिए कोई मूल टाइमज़ोन पैरामीटर मौजूद नहीं है (कुछ अन्य GitHub फ़ीचर्स जैसे Dependabot के विपरीत)।

[ऐसी घटनाएँ जो वर्कफ़्लोज़ को ट्रिगर करती हैं - GitHub Docs](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#schedule)  
[GitHub Actions के लिए वर्कफ़्लो सिंटैक्स - GitHub Docs](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#on-schedule)
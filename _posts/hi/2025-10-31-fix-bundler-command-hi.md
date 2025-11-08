---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: बंडलर कमांड नहीं मिला ठीक करें
translated: true
type: note
---

### समस्या को समझना
आपका `gem install jekyll bundler` सफल रहा (इसने 30 gems इंस्टॉल कीं, जिनमें Bundler 2.7.2 भी शामिल है), लेकिन `bundle` कमांड नहीं मिल रही है। यह Ubuntu/Debian सिस्टम पर सिस्टम-वाइड `sudo gem install` के बाद एक आम PATH/एनवायरनमेंट समस्या है। Gems बाइनरीज़ को `/usr/local/bin` (या इसी तरह के पथ) में इंस्टॉल करती हैं, लेकिन आपके शेल के `$PATH` में यह शामिल नहीं हो सकता है, या बदलाव अभी तक प्रभावी नहीं हुआ है (जैसे, आपके प्रोफाइल को रीलोड करने की आवश्यकता हो सकती है)।

सिस्टम द्वारा सुझाया गया `apt install ruby-bundler` apt के माध्यम से एक पुराना वर्जन (2.4.20) इंस्टॉल करेगा, जो आपके gem द्वारा इंस्टॉल किए गए Bundler 2.7.2 के साथ टकराव पैदा कर सकता है—अभी के लिए इससे बचें। snap के लिए भी यही बात है; यह Ruby को ऐसे आइसोलेट कर सकता है जिससे gem पथ टूट जाते हैं।

### त्वरित समाधान: इंस्टॉल किए गए Bundler को सत्यापित करें और उपयोग करें
1. **जांचें कि `bundle` कहाँ इंस्टॉल है**:
   ```
   gem environment
   ```
   - "EXECUTABLE DIRECTORY" देखें (संभवतः `/usr/local/bin`)। इस पथ को नोट कर लें।

2. **`bundle` को सीधे ढूंढें और टेस्ट करें**:
   ```
   which bundle  # यदि कुछ नहीं मिलता, तो आज़माएँ: find /usr/local -name bundle 2>/dev/null
   /usr/local/bin/bundle --version  # इसका आउटपुट "Bundler version 2.7.2" होना चाहिए
   ```
   - यदि यह काम करता है, तो बढ़िया! अभी के लिए पूरा पथ उपयोग करें: `/usr/local/bin/bundle install`

3. **अपना Jekyll सेटअप पूरे पथ के साथ चलाएं**:
   - `~/projects/blog-source` में (यह मानते हुए कि इसमें एक `Gemfile` है):
     ```
     /usr/local/bin/bundle install
     /usr/local/bin/bundle exec jekyll serve
     ```
   - इससे Jekyll डिपेंडेंसीज़ इंस्टॉल होनी चाहिएँ और सर्वर शुरू हो जाना चाहिए (आमतौर पर http://127.0.0.1:4000 पर)।

### स्थायी समाधान: अपने PATH को अपडेट करें
यदि `/usr/local/bin` आपके `$PATH` में नहीं है, तो इसे जोड़ें:
1. `~/.bashrc` (या लॉगिन शेल्स के लिए `~/.profile`) एडिट करें:
   ```
   nano ~/.bashrc
   ```
   अंत में यह लाइन जोड़ें:
   ```
   export PATH="/usr/local/bin:$PATH"
   ```

2. अपने शेल को रीलोड करें:
   ```
   source ~/.bashrc
   ```

3. सत्यापित करें:
   ```
   echo $PATH  # अब इसमें /usr/local/bin शामिल होना चाहिए
   bundle --version  # बिना पूरा पथ दिए काम करना चाहिए
   ```

अब दोबारा कोशिश करें:
```
bundle install
bundle exec jekyll serve
```

### यदि यह काम नहीं करता है
- **पर्मिशन समस्या?** (दुर्लभ, लेकिन sudo इनका कारण बन सकता है।) बिना sudo के दोबारा इंस्टॉल करें (यूज़र-लोकल इंस्टॉल):
  ```
  gem install --user-install bundler jekyll
  ```
   फिर `~/.bashrc` में `export PATH="$HOME/.local/share/gem/ruby/*/bin:$PATH"` जोड़ें (`gem environment` से मिले पथ के अनुसार एडजस्ट करें)।

- **Ruby वर्जन मिसमैच?** `ruby --version` से जांचें। यदि यह सिस्टम Ruby है (जैसे, 2.7.x), तो Ruby वर्जन मैनेजर जैसे `rbenv` पर विचार करें (इसे `curl -fsSL https://github.com/rbenv/rbenv-installer/raw/HEAD/bin/rbenv-installer | bash` के माध्यम से इंस्टॉल करें, फिर सेटअप फॉलो करें)। यह लंबे समय में सिस्टम कॉन्फ्लिक्ट से बचाता है।

- **क्या प्रॉक्सी अभी भी सक्रिय है?** यदि आपके एनवायरनमेंट वेरिएबल (`http_proxy`, आदि) सेट हैं, तो Bundler को उन्हें इन्हेरिट कर लेना चाहिए—बस यह सुनिश्चित कर लें कि कमांड चलाने से पहले वे एक्सपोर्टेड हैं।

PATH में बदलाव के बाद आपका सेटअप सही से चलना चाहिए। यदि आपको कोई एरर आती है (जैसे, `gem environment` आउटपुट शेयर करें), तो अधिक टार्गेटेड सहायता के लिए उन्हें पेस्ट करें!
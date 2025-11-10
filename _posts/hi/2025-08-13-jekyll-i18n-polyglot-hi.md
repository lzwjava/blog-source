---
audio: false
generated: true
image: false
lang: hi
layout: post
title: 'जेकिल आई१८एन: बहुभाषी प्लगइन और फ़ोल्डर विधि'
translated: true
type: note
---

आपके Jekyll ब्लॉग में i18n (अंतर्राष्ट्रीयकरण) के लिए तीन अच्छे तरीके हैं, जो "बिल्ट-इन सुविधाओं वाले" से लेकर "बेसिक" तक के हैं। यहां प्रत्येक तरीका बताया गया है कि वह कैसे काम करता है और उसे कैसे सेट अप करें।

# 1) सबसे आसान: एक प्लगइन का उपयोग करें (jekyll-polyglot)

**सबसे अच्छा है अगर आप लोकल या CI के साथ बिल्ड कर सकते हैं।** GitHub Pages का बिल्ट-इन बिल्डर ज़्यादातर तीसरे पक्ष के प्लगइन्स की अनुमति नहीं देता, इसलिए या तो लोकल में बिल्ड करें (`jekyll build`) और जनरेट किया गया `_site/` फोल्डर पुश करें, या बिल्ड और पब्लिश करने के लिए GitHub Actions का उपयोग करें।

**इंस्टॉल करें**

```bash
gem install jekyll-polyglot
# या Gemfile में जोड़ें:
# gem 'jekyll-polyglot'
```

**\_config.yml**

```yml
plugins:
  - jekyll-polyglot

languages: ["en", "zh", "ja"]   # आपकी भाषाएं
default_lang: "en"
exclude_from_localization: ["assets", "images", "CNAME"]  # स्टैटिक पाथ शेयर रखें
parallel_localization: true
```

**कंटेंट स्ट्रक्चर**

```
_index.md               # वैकल्पिक लैंडिंग पेज
_posts/
  2024-05-01-hello.en.md
  2024-05-01-hello.zh.md
pages/
  about.en.md
  about.zh.md
```

Polyglot भाषा-विशिष्ट URL जैसे `/en/about/` और `/zh/about/` बनाता है। यह `site.active_lang` भी एक्सपोज़ करता है।

**भाषा स्विचर (अपने लेआउट में)**

```liquid
<nav class="lang-switch">
  {% for lang in site.languages %}
    {% if lang == site.active_lang %}
      <span>{{ lang }}</span>
    {% else %}
      <a href="{{ page.url | prepend:'/' | replace_first:'/' | prepend:'/' | absolute_url | replace: '/' | relative_url | prepend:'/' }}">
        {%- comment -%}
        हम प्रत्येक भाषा के लिए करंट URL को दोबारा बनाएंगे:
        {%- endcomment -%}
      </a>
    {% endif %}
  {% endfor %}
</nav>
```

Polyglot के साथ एक सरल तरीका है:

```liquid
<nav>
  {% for lang in site.languages %}
    <a href="{{ site.baseurl_root }}/{{ lang }}{{ page.permalink | default: page.url }}">{{ lang }}</a>
  {% endfor %}
</nav>
```

**UI स्ट्रिंग्स डेटा फाइलों के माध्यम से**
`_data/i18n.yml` बनाएं:

```yml
en:
  nav:
    home: "Home"
    posts: "Posts"
zh:
  nav:
    home: "主页"
    posts: "文章"
```

टेम्पलेट्स में उपयोग करें:

```liquid
{{ site.data.i18n[site.active_lang].nav.home }}
```

**SEO (hreflang)**
अपने लेआउट के `<head>` में:

```liquid
{% assign langs = site.languages %}
{% for l in langs %}
  <link rel="alternate" hreflang="{{ l }}" href="{{ site.url }}/{{ l }}{{ page.url }}" />
{% endfor %}
<link rel="alternate" hreflang="x-default" href="{{ site.url }}/{{ site.default_lang }}{{ page.url }}" />
```

# 2) बिना प्लगइन के: प्रति-भाषा फोल्डर्स + Liquid

**सबसे अच्छा है अगर आपको GitHub Pages के बिल्ट-इन बिल्डर का उपयोग करना है।**

**स्ट्रक्चर**

```
_en/
  index.md
  about.md
_zh/
  index.md
  about.md
_posts/
  en/
    2024-05-01-hello.md
  zh/
    2024-05-01-hello.md
```

**\_config.yml**

```yml
defaults:
  - scope: { path: "_posts/en" }
    values: { lang: "en", permalink: "/en/:categories/:year/:month/:day/:title/" }
  - scope: { path: "_posts/zh" }
    values: { lang: "zh", permalink: "/zh/:categories/:year/:month/:day/:title/" }
  - scope: { path: "_en" }
    values: { lang: "en", permalink: "/en/:path/" }
  - scope: { path: "_zh" }
    values: { lang: "zh", permalink: "/zh/:path/" }
```

**करंट भाषा सेट करें**
प्रत्येक पेज के फ्रंट मैटर में जोड़ें:

```yml
---
layout: default
lang: en
---
```

या पाथ से इनफर करें:

```liquid
{% assign current_lang = page.lang | default: page.path | split:'/' | first | remove:'_' %}
```

**अनुवादों के बीच क्रॉस-लिंक्स**
फ्रंट मैटर में एक शेयर्ड आइडेंटिफायर का उपयोग करें:

```yml
---
layout: post
lang: en
ref: hello-post
---
```

चीनी वर्जन में:

```yml
---
layout: post
lang: zh
ref: hello-post
---
```

फिर लेआउट में, सहोदर पेज ढूंढें:

```liquid
{% assign siblings = site.pages | concat: site.posts | where:"ref", page.ref %}
{% for s in siblings %}
  {% unless s.url == page.url %}
    <a href="{{ s.url }}">{{ s.lang }}</a>
  {% endunless %}
{% endfor %}
```

**बिना प्लगइन के UI स्ट्रिंग्स**
ऊपर बताए अनुसार `_data/i18n.yml` का उपयोग करें, और `current_lang` के माध्यम से भाषा चुनें।

**डिफ़ॉल्ट भाषा रीडायरेक्ट (वैकल्पिक)**
रूट पर `index.html` बनाएं:

```html
<!doctype html>
<meta charset="utf-8">
<script>
  const lang = (navigator.language || '').toLowerCase().startsWith('zh') ? 'zh' : 'en';
  location.replace('/' + lang + '/');
</script>
<noscript><a href="/en/">English</a> · <a href="/zh/">中文</a></noscript>
```

# 3) हाइब्रिड: पोस्ट्स का एक सेट, केवल UI का अनुवाद

**सबसे अच्छा है अगर आप आर्टिकल्स का अनुवाद नहीं करते, केवल नेविगेशन, फुटर आदि का करते हैं।**
`/posts/` का एक सिंगल सेट रखें, `_data/i18n.yml` जोड़ें, और लेबल्स को भाषा के अनुसार रेंडर करें। प्रति-भाषा इंडेक्स पेज प्रदान करें जो समान पोस्ट्स को लिस्ट करते हैं, लेकिन लोकलाइज़्ड डेट्स और UI के साथ।

**लोकलाइज़्ड डेट्स**

```liquid
{% assign locale = page.lang | default: site.default_lang %}
{{ page.date | date: "%B %-d, %Y" }}  {# या अगर हैं तो फिल्टर्स/प्लगइन्स का उपयोग करें #}
```

(Jekyll का बिल्ट-इन `date` पूरी तरह से लोकेल-अवेयर नहीं है; असली लोकेल फॉर्मेटिंग के लिए आपको प्लगइन या डेटा में प्रीफॉर्मेटेड स्ट्रिंग्स की आवश्यकता होगी।)

---

## प्रैक्टिकल टिप्स

* **स्लग्स:** अनुवादित समकक्षों के लिए समान `ref` रखें; टाइटल्स को भाषा के अनुसार अलग होने दें।
* **इमेजेस:** शेयर्ड इमेजेस को `/assets/` में रखें और लोकलाइज़ेशन से बाहर रखें ताकि URL स्थिर रहें।
* **साइटमैप्स और SEO:** प्रति-भाषा साइटमैप्स जनरेट करें या सुनिश्चित करें कि आपका साइटमैप सभी भाषा के URL लिस्ट करता है; प्रत्येक भाषा वर्जन के भीतर कैनोनिकल टैग जोड़ें।
* **फ़ीड्स:** कलेक्शन्स को स्कोप करके प्रति-भाषा फ़ीड्स बनाएं: अपने फ़ीड टेम्पलेट में `lang` द्वारा पोस्ट्स को फिल्टर करें।

---

## मिनिमल वर्किंग उदाहरण (बिना प्लगइन)

1. स्ट्रिंग्स के साथ `_data/i18n.yml`।
2. `lang` फ्रंट मैटर के साथ `_en/index.md` और `_zh/index.md`।
3. `lang` और शेयर्ड `ref` के साथ `_posts/en/` और `_posts/zh/` के अंतर्गत पोस्ट्स।
4. लेआउट `site.data.i18n[current_lang]` और ऊपर दिए गए सहोदर लुकअप स्निपेट का उपयोग करता है।

अगर आप मुझे अपनी करंट रेपो स्ट्रक्चर बताते हैं (और यह भी कि आप सीधे GitHub Pages पर बिल्ड कर रहे हैं या Actions के माध्यम से), तो मैं एक रेडी-टू-ड्रॉप कॉन्फ़िग और कुछ स्टार्टर लेआउट तैयार कर सकता हूं।
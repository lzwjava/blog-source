---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: पोस्ट और नोट्स को क्रमबद्ध करना
translated: true
type: note
---

### संशोधित `_includes/sort.html`

आपका मौजूदा `sort.html` पहले से ही 9 विकल्पों वाला भाषा चयनकर्ता है, जो एकदम सही है। यहाँ कोई बड़े बदलाव की ज़रूरत नहीं है, लेकिन मैंने `<span id="post-number">` में एक छोटा सा नोट जोड़ा है ताकि यह अधिक सामान्य हो (जैसे "posts" के बजाय "entries") क्योंकि अब हम नोट्स भी शामिल कर रहे हैं। अगर ज़रूरत हो तो आपका JS इसे डायनामिकली अपडेट कर सकता है। यह रही संशोधित वर्जन:

```html
<div class="sort-container">
  <span id="post-number" class="post-number">
    {{ site.posts.size | plus: site.notes.size }} entries
    ({{ site.posts.size | plus: site.notes.size | divided_by: 7 | times: 6 }} Translated by <a href="https://openrouter.ai">AI</a>)
  </span>
  <select id="sort-select">
    <option value="en" selected>English</option>
    <option value="zh">中文</option>
    <option value="ja">日本語</option>
    <option value="es">Español</option>
    <option value="hi">हिंदी</option>
    <option value="fr">Français</option>
    <option value="de">Deutsch</option>
    <option value="ar">العربية</option>
    <option value="hant">繁體中文</option>
  </select>
</div>
```

**मुख्य बदलाव**: गिनती को `site.notes.size` शामिल करने के लिए अपडेट किया गया है (हम इसे नीचे परिभाषित करेंगे)। फॉर्मूला वही रहता है लेकिन अब नोट्स को भी फैक्टर करता है। अगर आपका JS (`index.js`) पहले से ही इस स्पैन को दिखाई देने वाली आइटम्स के आधार पर डायनामिकली अपडेट करता है, तो यह भाषा-विशिष्ट गिनती को ऑटोमैटिकली हैंडल कर लेगा।

### स्टेप 1: Jekyll कलेक्शन के रूप में नोट्स कॉन्फ़िगर करें (`_config.yml` में)

`_notes` को `_posts` की तरह ट्रीट करने के लिए (ताकि Jekyll Markdown फाइल्स को प्रोसेस करे और उन्हें `site.notes` के ज़रिए एक्सपोज़ करे), इसे अपने `_config.yml` में एड करें। यह ज़रूरी है—इसके बिना, नोट्स में पोस्ट्स की तरह `url`, `title`, `date` आदि नहीं होंगे।

```yaml
collections:
  notes:
    output: true
    permalink: /notes/:path/
```

- `output: true` नोट्स के लिए पेज जेनरेट करता है (ऑप्शनल अगर आप सिर्फ डेटा चाहते हैं)।
- `permalink` यूआरएल जैसे `/notes/es/2025-11-07-tidb-vs-cockroachdb-es/` सुनिश्चित करता है (अगर ज़रूरत हो तो एडजस्ट करें)।
- इसे एड करने के बाद अपने Jekyll सर्वर को रीस्टार्ट करें।

अब `site.notes` भी `site.posts` की तरह काम करता है, यह मानते हुए कि आपकी नोट फाइल्स (जैसे `_notes/es/2025-11-07-tidb-vs-cockroachdb-es.md`) में समान फ्रंटमैटर है: `title:`, `date:`, `image:`, `top:`, `translated:`, `generated:`।

### स्टेप 2: संशोधित पेज लेआउट (जैसे `index.md` या जहाँ भी आपका `<ul class="post-list">` है)

आपका करंट लूप सिर्फ अंग्रेजी पोस्ट्स दिखाता है। नोट्स एड करने और सभी 9 भाषाओं को सपोर्ट करने के लिए:

- एक बार भाषाओं की लिस्ट डिफाइन करें।
- **सभी** भाषाओं पर लूप चलाएँ।
- प्रत्येक भाषा के लिए, मिलने वाली **पोस्ट्स** (`_posts/{lang}/` से) और **नोट्स** (`_notes/{lang}/` से) को `<li>` आइटम्स के रूप में एड करें।
- प्रत्येक `<li>` को `class="... lang-{lang}"` मिले ताकि आपका JS उन्हें फिल्टर कर सके (जैसे, `#sort-select` वैल्यू के आधार पर हाइड/शो)।
- यह पूरी लिस्ट को शुरू में ही पॉपुलेट कर देता है (JS द्वारा हाइड), फिर भाषाएँ डायनामिकली स्विच करता है।
- तारीख के हिसाब से सॉर्ट करें? अगर आप नए को पहले चाहते हैं तो लूप्स में `| sort: 'date' | reverse` एड करें (यह मानते हुए कि तारीखें तुलनीय हैं)।

यह रहा पूरा अपडेटेड लेआउट:

```html
---
layout: page
---
{% include sort.html %}

<ul class="post-list">
  {% if site.posts.size == 0 and site.notes.size == 0 %}
    <li class="list-group-item post-item">No entries available.</li>
  {% else %}
    {% assign langs = "en,zh,ja,es,hi,fr,de,ar,hant" | split: "," %}
    {% for lang in langs %}
      {% comment %} इस भाषा के लिए पोस्ट्स {% endcomment %}
      {% for post in site.posts | sort: 'date' | reverse %}
        {% if post.path contains "_posts/{{ lang }}/" %}
          {% assign translated = post.translated %}
          {% assign generated = post.generated %}
          {% if translated == nil %}{% assign translated = false %}{% endif %}
          {% if generated == nil %}{% assign generated = false %}{% endif %}
          <li class="list-group-item post-item lang-{{ lang }}" data-top="{{ post.top }}" data-translated="{{ translated }}" data-generated="{{ generated }}">
            <a href="{{ post.url }}">
              <span class="date">{{ post.date | date: "%Y.%m.%d" }}</span>
              <span class="type">{% if post.image %}image{% else %}text{% endif %}</span>
              <span class="title">{{ post.title }}</span>
            </a>
          </li>
        {% endif %}
      {% endfor %}

      {% comment %} इस भाषा के लिए नोट्स (बिल्कुल पोस्ट्स की तरह) {% endcomment %}
      {% for note in site.notes | sort: 'date' | reverse %}
        {% if note.path contains "_notes/{{ lang }}/" %}
          {% assign translated = note.translated %}
          {% assign generated = note.generated %}
          {% if translated == nil %}{% assign translated = false %}{% endif %}
          {% if generated == nil %}{% assign generated = false %}{% endif %}
          <li class="list-group-item post-item lang-{{ lang }}" data-top="{{ note.top }}" data-translated="{{ translated }}" data-generated="{{ generated }}">
            <a href="{{ note.url }}">
              <span class="date">{{ note.date | date: "%Y.%m.%d" }}</span>
              <span class="type">{% if note.image %}image{% else %}text{% endif %}</span>
              <span class="title">{{ note.title }}</span>
            </a>
          </li>
        {% endif %}
      {% endfor %}
    {% endfor %}
  {% endif %}
</ul>

{% include footer.html %}
<script src="/assets/js/index.js"></script>
```

**मुख्य बदलाव**:
- **भाषाएँ ऐरे**: `{% assign langs = "en,zh,ja,es,hi,fr,de,ar,hant" | split: "," %}`—आपके सेलेक्ट ऑप्शन्स से मेल खाता है। मेंटेन करना आसान।
- **पोस्ट्स लूप**: हार्ड-कोडेड `en` फिल्टर हटा दिया गया; अब प्रत्येक लैंग के लिए `post.path contains "_posts/{{ lang }}/"` चेक करता है।
- **नोट्स लूप**: समान रूप से एड किया गया, `note.path contains "_notes/{{ lang }}/"` चेक करता है। नोट्स को बिल्कुल पोस्ट्स की तरह ट्रीट करता है (समान क्लासेस, एट्रिब्यूट्स, स्ट्रक्चर)।
- **सॉर्टिंग**: कालानुक्रमिक क्रम (नए पहले) के लिए दोनों लूप्स में `| sort: 'date' | reverse` एड किया गया। अगर ज़रूरत न हो तो हटा दें।
- **खाली चेक**: `site.notes.size` को शामिल करने के लिए अपडेट किया गया।
- **परफॉर्मेंस**: यह बिल्ड टाइम पर सभी ~9 भाषाओं की सामग्री जेनरेट करता है। छोटी साइट्स के लिए ठीक है; अगर बहुत बड़ी हो तो पेजिनेशन या JS फेचिंग पर विचार करें।

### ऑप्शनल: एक टाइप स्विच एड करें (पोस्ट्स/नोट्स/दोनों)

आपने "add a select/switch , two options select or whatever" का ज़िक्र किया था। अगर आप **दूसरा ड्रॉपडाउन** चाहते हैं जो टाइप के हिसाब से फिल्टर करे (जैसे, सिर्फ पोस्ट्स, सिर्फ नोट्स, या दोनों), तो इसे `sort.html` में भाषा चयनकर्ता के बाद एड करें:

```html
<select id="type-select">
  <option value="both" selected>Posts & Notes</option>
  <option value="posts">Posts Only</option>
  <option value="notes">Notes Only</option>
</select>
```

फिर, प्रत्येक `<li>` में एक `data-type` एट्रिब्यूट एड करें:
- पोस्ट्स के लिए: `data-type="posts"`
- नोट्स के लिए: `data-type="notes"`

अपने `index.js` को अपडेट करें ताकि यह `#type-select` में बदलाव को हैंडल कर सके (जैसे, `.post-item[data-type="notes"]` को फिल्टर करके हाइड/शो करे)। यह Liquid को बदले बिना इसे सरल रखता है।

### अगले कदम
- टेस्ट करें: `_notes/es/2025-11-07-tidb-vs-cockroachdb-es.md` जैसा एक सैंपल नोट एड करें जिसमें फ्रंटमैटर (शीर्षक, तारीख, आदि) हो, रीबिल्ड करें, और ड्रॉपडाउन में "Español" पर स्विच करें—यह दिखाई देना चाहिए।
- JS ट्वीक्स: सुनिश्चित करें कि `index.js` `.lang-{value}` से फिल्टर करता है और `#post-number` को अपडेट करता है (जैसे, दिखाई देने वाले `<li>` की गिनती)। अगर यह अभी तक नोट्स को हैंडल नहीं करता है, तो ऊपर बताए अनुसार `data-type` एड करें।
- अगर पाथ अलग हैं (जैसे, डायरेक्टरीज़ में ट्रेलिंग `/` नहीं है), तो `contains` चेक्स को एडजस्ट करें।

यह आपके 9-भाषा सेटअप को बनाए रखते हुए नोट्स को सीमलेसली इंटीग्रेट करता है। अगर आपको JS स्निपेट्स या और ट्वीक्स की ज़रूरत हो तो बताएं!
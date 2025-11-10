---
audio: false
generated: true
image: false
lang: ar
layout: post
title: 'تهيئة جيكيل للغات المتعددة: إضافة بوليجلوت وطريقة المجلدات'
translated: true
type: note
---

لديك ثلاثة مسارات جيدة للتدويل (i18n) في مدونة جيكل، تتراوح من الحلول "الشاملة" إلى الحلول "الأساسية". إليك كيفية عمل كل منها وكيفية إعدادها.

# 1) الأسهل: استخدام إضافة (jekyll-polyglot)

**الأفضل إذا كان بإمكانك البناء محليًا أو باستخدام التكامل المستمر (CI).** أداة البناء المضمنة في GitHub Pages لا تسمح بمعظم إضافات الطرف الثالث، لذا إما أن تبني محليًا (`jekyll build`) وتقوم برفع مجلد `_site/` المُنشأ، أو تستخدم GitHub Actions للبناء والنشر.

**التثبيت**

```bash
gem install jekyll-polyglot
# أو أضف إلى Gemfile:
# gem 'jekyll-polyglot'
```

**\_config.yml**

```yml
plugins:
  - jekyll-polyglot

languages: ["en", "zh", "ja"]   # لغاتك
default_lang: "en"
exclude_from_localization: ["assets", "images", "CNAME"]  # احتفظ بالمسارات الثابتة مشتركة
parallel_localization: true
```

**هيكل المحتوى**

```
_index.md               # الصفحة المقصودة (اختياري)
_posts/
  2024-05-01-hello.en.md
  2024-05-01-hello.zh.md
pages/
  about.en.md
  about.zh.md
```

تقوم Polyglot ببناء عناوين URL محددة باللغة مثل `/en/about/` و `/zh/about/`. كما تعرض أيضًا `site.active_lang`.

**مبدل اللغة (في التخطيط الخاص بك)**

```liquid
<nav class="lang-switch">
  {% for lang in site.languages %}
    {% if lang == site.active_lang %}
      <span>{{ lang }}</span>
    {% else %}
      <a href="{{ page.url | prepend:'/' | replace_first:'/' | prepend:'/' | absolute_url | replace: '/' | relative_url | prepend:'/' }}">
        {%- comment -%}
        سنعيد بناء عنوان URL الحالي لكل لغة:
        {%- endcomment -%}
      </a>
    {% endif %}
  {% endfor %}
</nav>
```

نهج أبسط مع Polyglot هو:

```liquid
<nav>
  {% for lang in site.languages %}
    <a href="{{ site.baseurl_root }}/{{ lang }}{{ page.permalink | default: page.url }}">{{ lang }}</a>
  {% endfor %}
</nav>
```

**سلاسل واجهة المستخدم عبر ملفات البيانات**
أنشئ `_data/i18n.yml`:

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

استخدم في القوالب:

```liquid
{{ site.data.i18n[site.active_lang].nav.home }}
```

**تحسين محركات البحث (hreflang)**
في `<head>` للتخطيط الخاص بك:

```liquid
{% assign langs = site.languages %}
{% for l in langs %}
  <link rel="alternate" hreflang="{{ l }}" href="{{ site.url }}/{{ l }}{{ page.url }}" />
{% endfor %}
<link rel="alternate" hreflang="x-default" href="{{ site.url }}/{{ site.default_lang }}{{ page.url }}" />
```

# 2) بدون إضافة: مجلدات لكل لغة + Liquid

**الأفضل إذا كان يجب عليك استخدام أداة البناء المضمنة في GitHub Pages.**

**الهيكل**

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

**تعيين اللغة الحالية**
أضف في front matter لكل صفحة:

```yml
---
layout: default
lang: en
---
```

أو استنتج من المسار:

```liquid
{% assign current_lang = page.lang | default: page.path | split:'/' | first | remove:'_' %}
```

**الروابط المتبادلة بين الترجمات**
استخدم معرفًا مشتركًا في front matter:

```yml
---
layout: post
lang: en
ref: hello-post
---
```

في النسخة الصينية:

```yml
---
layout: post
lang: zh
ref: hello-post
---
```

ثم في التخطيط، ابحث عن الصفحات المقابلة (الأخوة):

```liquid
{% assign siblings = site.pages | concat: site.posts | where:"ref", page.ref %}
{% for s in siblings %}
  {% unless s.url == page.url %}
    <a href="{{ s.url }}">{{ s.lang }}</a>
  {% endunless %}
{% endfor %}
```

**سلاسل واجهة المستخدم بدون إضافات**
استخدم `_data/i18n.yml` كما هو مذكور أعلاه، واختر اللغة عبر `current_lang`.

**إعادة التوجيه للغة الافتراضية (اختياري)**
أنشئ `index.html` في الجذر:

```html
<!doctype html>
<meta charset="utf-8">
<script>
  const lang = (navigator.language || '').toLowerCase().startsWith('zh') ? 'zh' : 'en';
  location.replace('/' + lang + '/');
</script>
<noscript><a href="/en/">English</a> · <a href="/zh/">中文</a></noscript>
```

# 3) الهجين: مجموعة واحدة من المقالات، ترجمة واجهة المستخدم فقط

**الأفضل إذا كنت لا تترجم المقالات، بل تترجم فقط الإطار العام (التنقل، التذييلة).**
احتفظ بمجموعة واحدة من `/posts/`، أضف `_data/i18n.yml`، وعرض التسميات حسب اللغة. وفر صفحات رئيسية لكل لغة تعرض نفس المقالات، ولكن بتواريخ وواجهة مستخدم مترجمة.

**التواريخ المترجمة**

```liquid
{% assign locale = page.lang | default: site.default_lang %}
{{ page.date | date: "%B %-d, %Y" }}  {# أو استخدم المرشحات/الإضافات إذا كانت متوفرة لديك #}
```

(الوظيفة المضمنة `date` في جيكل ليست مدركة للغة بالكامل؛ من أجل تنسيق التواريخ حسب اللغة حقًا، ستحتاج إلى إضافة أو سلاسل مسبقة التنسيق في البيانات.)

---

## نصائح عملية

* **العناوين:** احتفظ بنفس `ref` للنسخ المترجمة المقابلة؛ دع العناوين تختلف حسب اللغة.
* **الصور:** ضع الصور المشتركة في `/assets/` واستثنها من الترجمة حتى تبقى عناوين URL ثابتة.
* **خرائط الموقع وتحسين محركات البحث:** أنشئ خرائط موقع لكل لغة أو تأكد من أن خريطة موقعك تسرد جميع عناوين URL للغات؛ أضف وسوم canonical داخل كل نسخة بلغة.
* **المصادر:** أنشئ مصادر لكل لغة عن طريق تحديد النطاق للمجموعات: رشّح المقالات حسب `lang` في قالب المصدر.

---

## مثال عملي بسيط (بدون إضافة)

1.  `_data/i18n.yml` مع السلاسل النصية.
2.  `_en/index.md` و `_zh/index.md` مع `lang` في front matter.
3.  المقالات تحت `_posts/en/` و `_posts/zh/` مع `lang` و `ref` مشترك.
4.  التخطيط يستخدم `site.data.i18n[current_lang]` ومقتطف البحث عن الصفحات المقابلة (الأخوة) المذكور أعلاه.

إذا أخبرتني بهيكل مستودعك الحالي (وما إذا كنت تقوم بالبناء مباشرة على GitHub Pages أو عبر Actions)، يمكنني تخصيص إعداد جاهز للتطبيق وبعض التخطيطات الأولية.
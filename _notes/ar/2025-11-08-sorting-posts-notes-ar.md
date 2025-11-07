---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: ترتيب المنشورات والملاحظات
translated: true
---

### `_includes/sort.html` المُعدَّل

`sort.html` الحالي لديك يحتوي بالفعل على اختيار اللغة مع 9 خيارات، وهذا مثالي. لا توجد حاجة لتغييرات كبيرة هنا، لكنني أضفت ملاحظة صغيرة في `<span id="post-number">` لجعلها أكثر عمومية (مثل "إدخالات" بدلاً من "منشورات") لأننا الآن نضمّن الملاحظات. يمكن تحديث هذا ديناميكيًا بواسطة JS الخاص بك إذا لزم الأمر. إليك النسخة المعدلة:

```html
<div class="sort-container">
  <span id="post-number" class="post-number">
    {{ site.posts.size | plus: site.notes.size }} إدخالات
    ({{ site.posts.size | plus: site.notes.size | divided_by: 7 | times: 6 }} تمت الترجمة بواسطة <a href="https://openrouter.ai">الذكاء الاصطناعي</a>)
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

**التغيير الرئيسي**: تم تحديث العدد ليشمل `site.notes.size` (سنعرف هذا أدناه). تبقى الصيغة كما هي لكنها الآن تأخذ في الاعتبار الملاحظات. إذا كان JS الخاص بك (`index.js`) يقوم بالفعل بتحديث هذا النطاق ديناميكيًا بناءً على العناصر المرئية، فسيتعامل مع الأعداد الخاصة باللغة تلقائيًا.

### الخطوة 1: تكوين الملاحظات كمجموعة Jekyll (في `_config.yml`)

لمعاملة `_notes` مثل `_posts` (حتى تقوم Jekyll بمعالجة ملفات Markdown وتعرضها عبر `site.notes`)، أضف هذا إلى `_config.yml` الخاص بك. هذا أساسي — بدونه، لن يكون للملاحظات `url`، `title`، `date`، إلخ، كما هو الحال في المنشورات.

```yaml
collections:
  notes:
    output: true
    permalink: /notes/:path/
```

- `output: true` يولد صفحات للملاحظات (اختياري إذا كنت تريد البيانات فقط).
- `permalink` يضمن عناوين URL مثل `/notes/es/2025-11-07-tidb-vs-cockroachdb-es/` (عدل إذا لزم الأمر).
- أعد تشغيل خادم Jekyll الخاص بك بعد إضافة هذا.

الآن `site.notes` يعمل تمامًا مثل `site.posts`، بافتراض أن ملفات الملاحظات الخاصة بك (مثل `_notes/es/2025-11-07-tidb-vs-cockroachdb-es.md`) تحتوي على frontmatter مشابه: `title:`، `date:`، `image:`، `top:`، `translated:`، `generated:`.

### الخطوة 2: تخطيط الصفحة المعدل (مثل `index.md` أو أي مكان يوجد فيه `<ul class="post-list">` الخاص بك)

الحلقة الحالية الخاصة بك تُظهر فقط المنشورات الإنجليزية. لإضافة الملاحظات ودعم جميع اللغات التسع:

- عرّف قائمة اللغات مرة واحدة.
- كرّر عبر **جميع** اللغات.
- لكل لغة، أضف **المنشورات** المطابقة (من `_posts/{lang}/`) و **الملاحظات** (من `_notes/{lang}/`) كعناصر `<li>`.
- كل `<li>` تحصل على `class="... lang-{lang}"` حتى يتمكن JS الخاص بك من تصفيتها (مثل إخفاء/إظهار بناءً على قيمة `#sort-select`).
- هذا يملأ القائمة بأكملها مقدمًا (مخفي بواسطة JS)، ثم يبدل اللغات ديناميكيًا.
- الفرز حسب التاريخ؟ أضف `| sort: 'date' | reverse` إلى الحلقات إذا كنت تريد الأحدث أولاً (بافتراض أن التواريخ قابلة للمقارنة).

إليك تخطيط النسخة المحدثة بالكامل:

```html
---
layout: page
---
{% include sort.html %}

<ul class="post-list">
  {% if site.posts.size == 0 and site.notes.size == 0 %}
    <li class="list-group-item post-item">لا توجد إدخالات متاحة.</li>
  {% else %}
    {% assign langs = "en,zh,ja,es,hi,fr,de,ar,hant" | split: "," %}
    {% for lang in langs %}
      {% comment %} المنشورات لهذه اللغة {% endcomment %}
      {% for post in site.posts | sort: 'date' | reverse %}
        {% if post.path contains "_posts/{{ lang }}/" %}
          {% assign translated = post.translated %}
          {% assign generated = post.generated %}
          {% if translated == nil %}{% assign translated = false %}{% endif %}
          {% if generated == nil %}{% assign generated = false %}{% endif %}
          <li class="list-group-item post-item lang-{{ lang }}" data-top="{{ post.top }}" data-translated="{{ translated }}" data-generated="{{ generated }}">
            <a href="{{ post.url }}">
              <span class="date">{{ post.date | date: "%Y.%m.%d" }}</span>
              <span class="type">{% if post.image %}صورة{% else %}نص{% endif %}</span>
              <span class="title">{{ post.title }}</span>
            </a>
          </li>
        {% endif %}
      {% endfor %}

      {% comment %} الملاحظات لهذه اللغة (مثل المنشورات تمامًا) {% endcomment %}
      {% for note in site.notes | sort: 'date' | reverse %}
        {% if note.path contains "_notes/{{ lang }}/" %}
          {% assign translated = note.translated %}
          {% assign generated = note.generated %}
          {% if translated == nil %}{% assign translated = false %}{% endif %}
          {% if generated == nil %}{% assign generated = false %}{% endif %}
          <li class="list-group-item post-item lang-{{ lang }}" data-top="{{ note.top }}" data-translated="{{ translated }}" data-generated="{{ generated }}">
            <a href="{{ note.url }}">
              <span class="date">{{ note.date | date: "%Y.%m.%d" }}</span>
              <span class="type">{% if note.image %}صورة{% else %}نص{% endif %}</span>
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

**التغييرات الرئيسية**:
- **مصفوفة اللغات**: `{% assign langs = "en,zh,ja,es,hi,fr,de,ar,hant" | split: "," %}` — تطابق خيارات الاختيار الخاصة بك. سهل الصيانة.
- **حلقة المنشورات**: تمت إزالة عامل التصفية الثابت `en`؛ الآن يتحقق من `post.path contains "_posts/{{ lang }}/"` لكل لغة.
- **حلقة الملاحظات**: أضيفت بشكل مماثل، للتحقق من `note.path contains "_notes/{{ lang }}/"`. تعامل الملاحظات تمامًا مثل المنشورات (نفس الفئات، السمات، الهيكل).
- **الفرز**: تمت إضافة `| sort: 'date' | reverse` إلى كلتا الحلقتين للترتيب الزمني (الأحدث أولاً). احذفها إذا لم تكن مطلوبة.
- **التحقق من الفراغ**: تم تحديثه ليشمل `site.notes.size`.
- **الأداء**: يولد هذا محتوى جميع اللغات ~9 في وقت البناء. جيد للمواقع الصغيرة؛ إذا كان الموقع ضخمًا، ففكر في التقسيم إلى صفحات أو جلب البيانات بواسطة JS.

### اختياري: إضافة مفتاح تبديل النوع (منشورات/ملاحظات/كليهما)

لقد ذكرت "إضافة اختيار/مفتاح تبديل، خيارين للاختيار أو أي شيء". إذا كنت تريد **قائمة منسدلة ثانية** للتصفية حسب النوع (مثل: المنشورات فقط، الملاحظات فقط، أو كليهما)، أضف هذا إلى `sort.html` بعد اختيار اللغة:

```html
<select id="type-select">
  <option value="both" selected>المنشورات والملاحظات</option>
  <option value="posts">المنشورات فقط</option>
  <option value="notes">الملاحظات فقط</option>
</select>
```

ثم، أضف سمة `data-type` إلى كل `<li>`:
- للمنشورات: `data-type="posts"`
- للملاحظات: `data-type="notes"`

قم بتحديث `index.js` الخاص بك للتعامل مع تغييرات `#type-select` (مثل تصفية `.post-item[data-type="notes"]` لإخفاء/إظهار). هذا يبقي الأمر بسيطًا دون تغيير Liquid.

### الخطوات التالية
- اختبر: أضف ملاحظة نموذجية مثل `_notes/es/2025-11-07-tidb-vs-cockroachdb-es.md` مع frontmatter (العنوان، التاريخ، إلخ)، أعد البناء، وبدّل إلى "Español" في القائمة المنسدلة — يجب أن تظهر.
- تعديلات JS: تأكد من أن `index.js` يقوم بالتصفية حسب `.lang-{value}` ويحدث `#post-number` (مثل عد عناصر `<li>` المرئية). إذا لم يكن يتعامل مع الملاحظات بعد، أضف `data-type` كما هو مذكور أعلاه.
- إذا كانت المسارات مختلفة (مثل عدم وجود `/` في نهاية الدلائل)، فقم بتعديل عمليات التحقق `contains`.

هذا يدمج الملاحظات بسلاسة مع الحفاظ على إعدادات لغاتك التسع. أعلمني إذا كنت بحاجة إلى مقاطع JS أو تعديلات إضافية!
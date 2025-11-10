---
audio: false
generated: true
image: false
lang: ar
layout: post
title: صفحات الفهرس المخصصة للغة المسبقة الترجمة
translated: true
type: note
---

نعم، يمكنك معايرة صفحات الفهرس المنفصلة مسبقًا للغات مختلفة (مثل `index-zh.html`، `index-en.html`) لتحسين الأداء وتجربة المستخدم، خاصة إذا كان موقعك يحتوي على عدد كبير من المنشورات أو إذا كنت ترغب في تقليل معالجة JavaScript على جانب العميل. هذا النهج يتضمن إنشاء ملفات HTML ثابتة لكل لغة أثناء عملية البناء، بدلاً من الاعتماد على JavaScript لتصفية وترتيب المنشورات ديناميكيًا على جانب العميل.

أدناه، سأوضح كيف يمكنك تحقيق هذا باستخدام Jekyll، مع التركيز على إنشاء صفحات فهرس منفصلة لكل لغة (`index-zh.html`، `index-en.html`، إلخ) مع الحفاظ على وظائف الإعداد الحالي الخاص بك. سيعتمد هذا على نظام بناء Jeklox لحساب قوائم المنشورات المصفاة مسبقًا لكل لغة، مما يقلل الحاجة إلى JavaScript معقد على جانب العميل.

---

### النهج لمعايرة `index-zh.html`، `index-en.html`، إلخ مسبقًا

لمعايرة صفحات الفهرس الخاصة باللغة مسبقًا، يمكنك إنشاء قوالب صفحات Jekyll منفصلة لكل لغة واستخدام Liquid لتصفية المنشورات حسب اللغة أثناء عملية البناء. بهذه الطريقة، ستحتوي كل صفحة (`index-en.html`، `index-zh.html`، إلخ) فقط على المنشورات ذات الصلة، وسيتم التعامل مع منطق الترتيب/التصفية في وقت البناء بدلاً من المتصفح.

إليك كيف يمكنك القيام بذلك:

---

#### 1. إنشاء قوالب صفحات خاصة باللغة

قم بإنشاء ملفات صفحات منفصلة في الدليل الجذري لمشروع Jekyll الخاص بك لكل لغة، مثل:

- `index-en.html`
- `index-zh.html`
- `index-ja.html`
- ... وهكذا للغات الأخرى (`es`، `hi`، `fr`، `de`، `ar`، `hant`، إلخ).

سيستخدم كل ملف هيكلاً مشابهًا للكود المقدم لديك ولكنه سيقوم بتصفية المنشورات للغة محددة باستخدام Liquid. إليك مثال لـ `index-en.html`:

```html
---
layout: page
lang: en
permalink: /en/
---

<div class="sort-container">
  <span id="post-number" class="post-number">
    {% assign en_posts = site.posts | where: "lang", "en" %}
    {{ en_posts.size }} posts
    ({{ en_posts | where: "translated", true | size }} by <a href="https://mistral.ai">AI</a>)
  </span>

  <select id="sort-select">
    <option value="author-picks|en">Picks</option>
    <option value="date-desc|all">All</option>
    <option value="date-desc|original">Original</option>
    <option value="date-desc|en" selected>English</option>
    <option value="date-desc|zh">中文</option>
    <option value="date-desc|ja">日本語</option>
    <option value="date-desc|es">Español</option>
    <option value="date-desc|hi">हिंदी</option>
    <option value="date-desc|fr">Français</option>
    <option value="date-desc|de">Deutsch</option>
    <option value="date-desc|ar">العربية</option>
    <option value="date-desc|hant">繁體中文</option>
  </select>
</div>

<ul class="post-list">
  {% if en_posts.size > 0 %}
    {% for post in en_posts %}
      <li class="list-group-item post-item lang-en" data-top="{{ post.top | default: 0 }}" data-translated="{{ post.translated | default: false }}" data-generated="{{ post.generated | default: false }}">
        <a href="{{ post.url }}">
          <span class="date">{{ post.date | date: "%Y.%m.%d" }}</span>
          <span class="type">{% if post.image %}image{% else %}text{% endif %}</span>
          <span class="title">{{ post.title }}</span>
        </a>
      </li>
    {% endfor %}
  {% else %}
    <li class="list-group-item post-item">No posts available.</li>
  {% endif %}
</ul>

<footer class="site-footer">
  <span class="site-footer-credits">
    Powered by <a href="https://jekyllrb.com/">Jekyll</a><br>
    Ignited by <a href="https://mistral.ai">Mistral</a><br>
    Updated at <a href="https://github.com/lzwjava/lzwjava.github.io/commit/{{ site.release }}">{{ site.release | slice: 0, 6 }}</a><br>
    Copyright©{{ site.starting_year }}–{{ site.time | date: "%Y" }}
  </span>
</footer>
```

لـ `index-zh.html`، ستستبدل عامل التصفية `lang` و `where`:

```html
---
layout: page
lang: zh
permalink: /zh/
---
<div class="sort-container">
  <span id="post-number" class="post-number">
    {% assign zh_posts = site.posts | where: "lang", "zh" %}
    {{ zh_posts.size }} posts
    ({{ zh_posts | where: "translated", true | size }} by <a href="https://mistral.ai">AI</a>)
  </span>
  <!-- نفس sort-select كما بالأعلى -->
</div>

<ul class="post-list">
  {% if zh_posts.size > 0 %}
    {% for post in zh_posts %}
      <li class="list-group-item post-item lang-zh" data-top="{{ post.top | default: 0 }}" data-translated="{{ post.translated | default: false }}" data-generated="{{ post.generated | default: false }}">
        <a href="{{ post.url }}">
          <span class="date">{{ post.date | date: "%Y.%m.%d" }}</span>
          <span class="type">{% if post.image %}image{% else %}text{% endif %}</span>
          <span class="title">{{ post.title }}</span>
        </a>
      </li>
    {% endfor %}
  {% else %}
    <li class="list-group-item post-item">No posts available.</li>
  {% endif %}
</ul>

<!-- نفس التذييل كما بالأعلى -->
```

كرر هذا لكل لغة (`ja`، `es`، `hi`، `fr`، `de`، `ar`، `hant`، إلخ)، مع تعديل front matter الخاص بـ `lang` وعامل التصفية `where` وفقًا لذلك.

---

#### 2. تحديث Front Matter للمنشورات

تأكد من أن كل منشور في دليل `_posts` الخاص بك يحتوي على متغير front matter باسم `lang` يتوافق مع لغته (مثل `en`، `zh`، `ja`، إلخ). على سبيل المثال:

```yaml
---
title: My English Post
lang: en
date: 2025-08-01
translated: true
generated: false
top: 1
---
```

هذا يسمح لعامل التصفية `where` بتحديد المنشورات حسب اللغة بشكل صحيح.

إذا كانت منشوراتك منظمة في أدلة فرعية مثل `_posts/en/`، `_posts/zh/`، إلخ، فيمكنك استنتاج اللغة من المسار بدلاً من استخدام متغير `lang`. على سبيل المثال، في `index-en.html`:

```liquid
{% assign en_posts = site.posts | where_exp: "post", "post.path contains '_posts/en/'" %}
```

---

#### 3. تبسيط JavaScript

نظرًا لأنه تم التعامل مع تصفية اللغة الآن في وقت البناء، يمكنك تبسيط JavaScript للتعامل فقط مع الترتيب (مثل حسب التاريخ أو مختارات المؤلف) والتنقل بين صفحات اللغة. إليك نسخة محدثة من JavaScript:

```javascript
window.addEventListener('load', function () {
  const sortSelect = document.getElementById('sort-select');
  const postNumber = document.getElementById('post-number');
  const postList = document.querySelector('.post-list');

  function updatePosts() {
    const selectedValue = sortSelect.value;
    const [sortOption, langFilter] = selectedValue.split('|');

    // إذا كانت اللغة المحددة لا تطابق الصفحة الحالية، قم بإعادة التوجيه
    const currentLang = '{{ page.lang }}';
    if (langFilter !== currentLang && langFilter !== 'all' && langFilter !== 'original' && sortOption !== 'author-picks') {
      window.location.href = `/${langFilter}/?sort=${selectedValue}`;
      return;
    }

    // احصل على جميع المنشورات
    const posts = document.querySelectorAll('.post-list li.post-item');
    let processedPosts = [];

    if (sortOption === 'author-picks') {
      // تصفية المنشورات ذات 'data-top' > 0
      processedPosts = Array.from(posts)
        .filter(post => parseInt(post.dataset.top || 0, 10) > 0)
        .map(post => ({ element: post }));
    } else if (sortOption === 'date-desc' && langFilter === 'original') {
      // تصفية المنشورات الأصلية (غير المترجمة، غير المُنشأة)
      processedPosts = Array.from(posts)
        .filter(post => post.dataset.translated === 'false' && post.dataset.generated === 'false')
        .map(post => {
          const dateElement = post.querySelector('.date');
          const dateStr = dateElement ? dateElement.textContent.trim().replace(/\./g, '-') : null;
          return { element: post, date: dateStr ? new Date(dateStr) : null };
        })
        .filter(item => item.date)
        .sort((a, b) => b.date - a.date);
    } else {
      // الترتيب تنازليًا حسب التاريخ
      processedPosts = Array.from(posts)
        .map(post => {
          const dateElement = post.querySelector('.date');
          const dateStr = dateElement ? dateElement.textContent.trim().replace(/\./g, '-') : null;
          const aElement = post.querySelector('a');
          const href = aElement ? aElement.getAttribute('href') : '';
          const fileName = href ? href.split('/').pop() : '';
          return { element: post, date: dateStr ? new Date(dateStr) : null, fileName };
        })
        .filter(item => item.date)
        .sort((a, b) => {
          const dateComparison = b.date - a.date;
          return dateComparison !== 0 ? dateComparison : a.fileName.localeCompare(b.fileName);
        });
    }

    // امسح القائمة الحالية
    postList.innerHTML = '';

    // أضف المنشورات المعالجة أو اعرض رسالة
    if (processedPosts.length > 0) {
      processedPosts.forEach(item => {
        if (item.element) {
          postList.appendChild(item.element);
        }
      });
    } else {
      const noPostsMessage = document.createElement('li');
      noPostsMessage.className = 'list-group-item post-item';
      noPostsMessage.textContent = 'No posts available. Please refresh the page.';
      postList.appendChild(noPostsMessage);
    }

    // تحديث عدد المنشورات
    const translatedCount = processedPosts.filter(item => item.element && item.element.dataset.translated === 'true').length;
    postNumber.innerHTML = `${processedPosts.length} posts (${translatedCount} by <a href="https://mistral.ai">AI</a>)`;

    // اعرض القائمة
    postList.style.display = 'block';
  }

  // استعادة من localStorage أو تعيين الافتراضي
  const savedSort = localStorage.getItem('sortOption');
  if (savedSort) {
    sortSelect.value = savedSort;
  } else {
    sortSelect.value = 'date-desc|{{ page.lang }}';
  }

  updatePosts();

  // مستمع الحدث لتغييرات القائمة المنسدلة
  sortSelect.addEventListener('change', function () {
    localStorage.setItem('sortOption', sortSelect.value);
    updatePosts();
  });
});
```

التغييرات الرئيسية:
- يتحقق البرنامج النصي مما إذا كانت اللغة المحددة تطابق لغة الصفحة الحالية (`{{ page.lang }}`). إذا لم تكن كذلك، فإنه يعيد التوجيه إلى صفحة اللغة المناسبة (مثل `/zh/` للصينية).
- لم تعد هناك حاجة لتصفية اللغة حيث تمت تصفية المنشورات مسبقًا بواسطة قالب Liquid.

---

#### 4. تكوين Permalinks والتنقل

تأكد من أن كل صفحة خاصة بلغة لها permalink فريد في front matter الخاص بها (مثل `permalink: /en/` لـ `index-en.html`). هذا يسمح للمستخدمين بالانتقال مباشرة إلى `/en/`، `/zh/`، إلخ.

قد ترغب أيضًا في تحديث تنقل موقعك لتضمين روابط إلى صفحات اللغة هذه. على سبيل المثال، في التخطيط أو الرأس الخاص بك:

```html
<nav>
  <a href="/en/">English</a>
  <a href="/zh/">中文</a>
  <a href="/ja/">日本語</a>
  <!-- أضف لغات أخرى -->
</nav>
```

---

#### 5. التعامل مع عوامل التصفية "All" و "Original"

لخيارات "All" و "Original" في القائمة المنسدلة:
- **All**: يمكنك إنشاء `index.html` يتضمن جميع المنشورات (مشابه للإعداد الأصلي الخاص بك) أو إعادة التوجيه إلى إحدى صفحات اللغة المحددة.
- **Original**: يمكنك إنشاء `index-original.html` الذي يقوم بتصفية المنشورات ذات `translated: false` و `generated: false`:

```html
---
layout: page
lang: original
permalink: /original/
---
<div class="sort-container">
  <span id="post-number" class="post-number">
    {% assign original_posts = site.posts | where: "translated", false | where: "generated", false %}
    {{ original_posts.size }} posts
    (0 by <a href="https://mistral.ai">AI</a>)
  </span>
  <!-- نفس sort-select -->
</div>

<ul class="post-list">
  {% if original_posts.size > 0 %}
    {% for post in original_posts %}
      <li class="list-group-item post-item lang-{{ post.lang }}" data-top="{{ post.top | default: 0 }}" data-translated="false" data-generated="false">
        <a href="{{ post.url }}">
          <span class="date">{{ post.date | date: "%Y.%m.%d" }}</span>
          <span class="type">{% if post.image %}image{% else %}text{% endif %}</span>
          <span class="title">{{ post.title }}</span>
        </a>
      </li>
    {% endfor %}
  {% else %}
    <li class="list-group-item post-item">No posts available.</li>
  {% endif %}
</ul>

<!-- نفس التذييل -->
```

---

#### 6. فوائد المعايرة المسبقة

- **الأداء**: تقوم تصفية المنشورات في وقت البناء بتقليل معالجة JavaScript على جانب العميل، مما يجعل الموقع أسرع، خاصة للمستخدمين الذين لديهم أجهزة أو اتصالات أبطأ.
- **تحسين محركات البحث (SEO)**: يمكن لمحركات البحث فهرسة صفحات اللغة المحددة (`/en/`، `/zh/`، إلخ) بشكل أفضل، مما يحسن إمكانية الاكتشاف.
- **JavaScript أبسط**: يحتاج JavaScript فقط للتعامل مع الترتيب والتنقل، وليس تصفية اللغة.
- **الموثوقية**: تتجنب الصفحات المترجمة مسبقًا الأخطاء على جانب العميل (على سبيل المثال، رسالة "Known bug pending fix" في الكود الأصلي الخاص بك).

---

#### 7. الاعتبارات

- **وقت البناء**: تزيد المعايرة المسبقة لصفحات الفهرس المتعددة من وقت البناء، خاصة إذا كان لديك العديد من المنشورات أو اللغات. ومع ذلك، فإن هذا يكون عادةً ضئيلاً ما لم يكن لديك آلاف المنشورات.
- **الصيانة**: ستحتاج إلى الحفاظ على ملفات فهرس متعددة (`index-en.html`، `index-zh.html`، إلخ). لتقليل التكرار، يمكنك استخدام includes أو تخطيطات Jekyll لمشاركة الكود المشترك.
- **الترتيب الديناميكي**: لا يزال JavaScript يتعامل مع الترتيب (مثل مختارات المؤلف، date-desc)، ولكن يمكنك حساب الإصدارات المرتبة مسبقًا من كل صفحة إذا كنت تريد إخراجًا ثابتًا بالكامل (على الرغم من أن هذا سيخلق المزيد من الملفات، على سبيل المثال، `index-en-picks.html`).

---

#### 8. مثال على هيكل الدليل

قد يبدو مشروع Jekyll الخاص بك هكذا:

```
├── _posts/
│   ├── en/
│   │   ├── 2025-08-01-post1.md
│   │   ├── 2025-08-02-post2.md
│   ├── zh/
│   │   ├── 2025-08-01-post1-zh.md
│   ├── ja/
│   └── ...
├── _layouts/
│   ├── page.html
├── index-en.html
├── index-zh.html
├── index-ja.html
├── index-original.html
├── _includes/
│   ├── header.html
│   ├── footer.html
├── assets/
│   ├── js/
│   │   ├── sort.js
```

---

#### 9. الاختبار والنشر

- اختبر محليًا باستخدام `jekyll serve` للتأكد من أن كل صفحة لغة (`/en/`، `/zh/`، إلخ) تعرض المنشورات الصحيحة.
- تحقق من أن التنقل عبر القائمة المنسدلة يعيد التوجيه بشكل صحيح بين صفحات اللغة.
- انشر على منصة الاستضافة الخاصة بك (مثل GitHub Pages) وتحقق من أن permalinks تعمل كما هو متوقع.

---

### المراجع
- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [Mistral AI](https://mistral.ai)

إذا كان لديك المزيد من الأسئلة أو تحتاج إلى مساعدة في أجزاء محددة من التنفيذ، فأخبرني!
---
audio: false
generated: true
image: false
lang: hi
layout: post
title: पूर्वसंकलित भाषा-विशिष्ट अनुक्रमणिका पृष्ठ
translated: true
type: note
---

हाँ, आप प्रदर्शन और user experience को बेहतर बनाने के लिए विभिन्न भाषाओं के लिए अलग-अलग index pages को precompile कर सकते हैं (जैसे, `index-zh.html`, `index-en.html`), खासकर यदि आपकी साइट में बड़ी संख्या में posts हैं या आप client-side JavaScript processing को कम करना चाहते हैं। इस approach में build process के दौरान प्रत्येक भाषा के लिए static HTML files generate करना शामिल होगा, न कि client side पर dynamically posts को filter और sort करने के लिए JavaScript पर निर्भर रहना।

नीचे, मैं बताऊंगा कि आप इसे Jekyll के साथ कैसे प्राप्त कर सकते हैं, जिसमें आपकी मौजूदा setup की functionality को बनाए रखते हुए प्रत्येक भाषा (`index-zh.html`, `index-en.html`, आदि) के लिए अलग-अलग index pages बनाना शामिल है। यह Jekyll की build system का लाभ उठाकर प्रत्येक भाषा के लिए filtered post lists को precompute करेगा, जिससे complex client-side JavaScript की आवश्यकता कम हो जाएगी।

---

### `index-zh.html`, `index-en.html`, आदि को Precompile करने का Approach

Language-specific index pages को precompile करने के लिए, आप प्रत्येक भाषा के लिए अलग-अलग Jekyll page templates बना सकते हैं और build process के दौरान Liquid का उपयोग posts को भाषा के आधार पर filter करने के लिए कर सकते हैं। इस तरह, प्रत्येक page (`index-en.html`, `index-zh.html`, आदि) में केवल relevant posts होंगी, और sorting/filtering logic build time पर handle होगी न कि browser में।

यहां बताया गया है कि आप इसे कैसे कर सकते हैं:

---

#### 1. Language-Specific Page Templates बनाएं

प्रत्येक भाषा के लिए अपने Jekyll project की root directory में अलग-अलग page files बनाएं, जैसे:

- `index-en.html`
- `index-zh.html`
- `index-ja.html`
- ...और अन्य भाषाओं (`es`, `hi`, `fr`, `de`, `ar`, `hant`, आदि) के लिए भी।

प्रत्येक file आपके दिए गए code के समान structure का उपयोग करेगी लेकिन Liquid का उपयोग करके एक specific भाषा के लिए posts को filter करेगी। यहां `index-en.html` के लिए एक उदाहरण दिया गया है:

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

`index-zh.html` के लिए, आप `lang` और `where` filter को replace करेंगे:

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
  <!-- Same sort-select as above -->
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

<!-- Same footer as above -->
```

प्रत्येक भाषा (`ja`, `es`, `hi`, `fr`, `de`, `ar`, `hant`, आदि) के लिए इसे दोहराएं, `lang` front matter और `where` filter को तदनुसार adjust करते हुए।

---

#### 2. Post Front Matter को Update करें

सुनिश्चित करें कि आपकी `_posts` directory में प्रत्येक post में एक `lang` front matter variable है जो उसकी भाषा से मेल खाती है (जैसे, `en`, `zh`, `ja`, आदि)। उदाहरण के लिए:

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

यह `where` filter को भाषा के आधार पर posts को सही ढंग से identify करने की अनुमति देता है।

यदि आपकी posts subdirectories जैसे `_posts/en/`, `_posts/zh/`, आदि में organized हैं, तो आप `lang` variable का उपयोग करने के बजाय path से भाषा का अनुमान लगा सकते हैं। उदाहरण के लिए, `index-en.html` में:

```liquid
{% assign en_posts = site.posts | where_exp: "post", "post.path contains '_posts/en/'" %}
```

---

#### 3. JavaScript को Simplify करें

चूंकि language filtering अब build time पर handle हो रही है, आप JavaScript को केवल sorting (जैसे, date या author picks द्वारा) और language pages के बीच navigation handle करने के लिए simplify कर सकते हैं। यहां JavaScript का एक updated version दिया गया है:

```javascript
window.addEventListener('load', function () {
  const sortSelect = document.getElementById('sort-select');
  const postNumber = document.getElementById('post-number');
  const postList = document.querySelector('.post-list');

  function updatePosts() {
    const selectedValue = sortSelect.value;
    const [sortOption, langFilter] = selectedValue.split('|');

    // If the selected language doesn't match the current page, redirect
    const currentLang = '{{ page.lang }}';
    if (langFilter !== currentLang && langFilter !== 'all' && langFilter !== 'original' && sortOption !== 'author-picks') {
      window.location.href = `/${langFilter}/?sort=${selectedValue}`;
      return;
    }

    // Grab all posts
    const posts = document.querySelectorAll('.post-list li.post-item');
    let processedPosts = [];

    if (sortOption === 'author-picks') {
      // Filter posts with 'data-top' > 0
      processedPosts = Array.from(posts)
        .filter(post => parseInt(post.dataset.top || 0, 10) > 0)
        .map(post => ({ element: post }));
    } else if (sortOption === 'date-desc' && langFilter === 'original') {
      // Filter original (non-translated, non-generated) posts
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
      // Sort by date descending
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

    // Clear existing list
    postList.innerHTML = '';

    // Append processed posts or show a message
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

    // Update the post count
    const translatedCount = processedPosts.filter(item => item.element && item.element.dataset.translated === 'true').length;
    postNumber.innerHTML = `${processedPosts.length} posts (${translatedCount} by <a href="https://mistral.ai">AI</a>)`;

    // Show the list
    postList.style.display = 'block';
  }

  // Restore from localStorage or set default
  const savedSort = localStorage.getItem('sortOption');
  if (savedSort) {
    sortSelect.value = savedSort;
  } else {
    sortSelect.value = 'date-desc|{{ page.lang }}';
  }

  updatePosts();

  // Event listener for dropdown changes
  sortSelect.addEventListener('change', function () {
    localStorage.setItem('sortOption', sortSelect.value);
    updatePosts();
  });
});
```

Key changes:
- Script जांचता है कि selected भाषा current page की भाषा (`{{ page.lang }}`) से मेल खाती है या नहीं। यदि नहीं, तो यह appropriate language page (जैसे, Chinese के लिए `/zh/`) पर redirect करता है।
- Language filtering अब आवश्यक नहीं है क्योंकि posts Liquid template द्वारा prefiltered हैं।

---

#### 4. Permalinks और Navigation को Configure करें

सुनिश्चित करें कि प्रत्येक language-specific page के front matter में एक unique permalink है (जैसे, `index-en.html` के लिए `permalink: /en/`)। यह users को सीधे `/en/`, `/zh/`, आदि पर navigate करने की अनुमति देता है।

आप अपनी site की navigation को इन language-specific pages के links शामिल करने के लिए भी update करना चाह सकते हैं। उदाहरण के लिए, अपने layout या header में:

```html
<nav>
  <a href="/en/">English</a>
  <a href="/zh/">中文</a>
  <a href="/ja/">日本語</a>
  <!-- Add other languages -->
</nav>
```

---

#### 5. "All" और "Original" Filters को Handle करें

Dropdown में "All" और "Original" options के लिए:
- **All**: आप एक `index.html` बना सकते हैं जिसमें सभी posts शामिल हों (आपकी original setup के समान) या किसी एक language-specific page पर redirect कर सकते हैं।
- **Original**: आप एक `index-original.html` बना सकते हैं जो `translated: false` और `generated: false` वाली posts को filter करे:

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
  <!-- Same sort-select -->
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

<!-- Same footer -->
```

---

#### 6. Precompiling के Benefits

- **Performance**: Build time पर posts को filter करने से client-side JavaScript processing कम होती है, जिससे site तेज होती है, खासकर slower devices या connections वाले users के लिए।
- **SEO**: Search engines language-specific pages (`/en/`, `/zh/`, आदि) को बेहतर ढंग से index कर सकते हैं, जिससे discoverability में सुधार होता है।
- **Simpler JavaScript**: JavaScript को केवल sorting और navigation handle करने की आवश्यकता होती है, language filtering की नहीं।
- **Reliability**: Precompiled pages client-side bugs (जैसे, आपके original code में "Known bug pending fix" message) से बचते हैं।

---

#### 7. Considerations

- **Build Time**: Multiple index pages को precompile करने से build time बढ़ती है, खासकर यदि आपके पास कई posts या भाषाएं हैं। हालांकि, यह आमतौर पर नगण्य होती है जब तक कि आपके पास हजारों posts न हों।
- **Maintenance**: आपको multiple index files (`index-en.html`, `index-zh.html`, आदि) को maintain करने की आवश्यकता होगी। Duplication को कम करने के लिए, आप common code share करने के लिए Jekyll includes या layouts का उपयोग कर सकते हैं।
- **Dynamic Sorting**: JavaScript अभी भी sorting (जैसे, author picks, date-desc) handle करता है, लेकिन यदि आप fully static output चाहते हैं तो आप प्रत्येक page के sorted versions को precompute कर सकते हैं (हालांकि इससे अधिक files बनेंगी, जैसे, `index-en-picks.html`)।

---

#### 8. Example Directory Structure

आपका Jekyll project कुछ इस तरह दिख सकता है:

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

#### 9. Testing और Deployment

- यह सुनिश्चित करने के लिए `jekyll serve` के साथ locally test करें कि प्रत्येक language page (`/en/`, `/zh/`, आदि) सही posts display करती है।
- Verify करें कि dropdown navigation language pages के बीच correctly redirect करता है।
- अपने hosting platform (जैसे, GitHub Pages) पर deploy करें और check करें कि permalinks expected रूप से work करते हैं।

---

### References
- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [Mistral AI](https://mistral.ai)

यदि आपके पास implementation के specific parts के बारे में और प्रश्न हैं या सहायता की आवश्यकता है, तो मुझे बताएं!
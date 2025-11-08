  const translations = {
    'en': 'Translated',
    'zh': '翻译',
    'ja': '翻訳済み',
    'es': 'Traducido',
    'hi': 'अनुवादित',
    'fr': 'Traduit',
    'de': 'Übersetzt',
    'ar': 'مترجم',
    'hant': '翻譯'
  };

window.addEventListener('load', function () {
    const typeSelect = document.getElementById('type-select');
    const sortSelect = document.getElementById('sort-select');
    const postNumber = document.getElementById('post-number');
    const postList = document.querySelector('.post-list');

    // Detect current page type and language from URL
    const currentPath = window.location.pathname;
    let currentType = 'posts'; // default
    let currentLang = 'en';   // default

    if (currentPath.includes('/notes')) {
      currentType = 'notes';
    }

    // Check for language in filename (e.g., /notes-zh.html or /index-zh.html)
    const langMatch = currentPath.match(/-(zh|ja|es|hi|fr|de|ar|hant)\.html$/);
    if (langMatch) {
      currentLang = langMatch[1];
    }

    // Count and display posts
    const posts = document.querySelectorAll('.post-list li.post-item');
    const translatedCount = Array.from(posts).filter(post => post.dataset.translated === 'true').length;
    const notesFiltered = Array.from(posts).filter(post => post.dataset.type === 'note').length;
    const displayLang = localStorage.getItem('selectedLanguage') || currentLang;
    const translatedText = translations[displayLang] || translations['en'];
    postNumber.innerHTML = `${posts.length} (${translatedCount} ${translatedText} by <a href="https://mistral.ai">AI</a>)`;

    // Restore from localStorage if available
    const savedLang = localStorage.getItem('selectedLanguage');
    const savedType = localStorage.getItem('selectedType');

    if (savedLang) {
      sortSelect.value = savedLang;
    } else {
      sortSelect.value = currentLang;
    }

    if (savedType) {
      typeSelect.value = savedType;
    } else {
      typeSelect.value = currentType;
    }

    // Event listener for type changes
    typeSelect.addEventListener('change', function () {
      const selectedType = typeSelect.value;
      const currentLang = sortSelect.value;

      // Save to localStorage
      localStorage.setItem('selectedType', selectedType);

      // Build redirect URL
      let url;
      if (selectedType === 'posts') {
        url = currentLang === 'en' ? '/' : `/index-${currentLang}.html`;
      } else {
        url = `/notes-${currentLang}.html`;
      }

      window.location.href = url;
    });

    // Event listener for language changes
    sortSelect.addEventListener('change', function () {
      const selectedLang = sortSelect.value;
      const currentType = typeSelect.value;

      // Save to localStorage
      localStorage.setItem('selectedLanguage', selectedLang);

      // Build redirect URL
      let url;
      if (currentType === 'posts') {
        url = selectedLang === 'en' ? '/' : `/index-${selectedLang}.html`;
      } else {
        url = `/notes-${selectedLang}.html`;
      }

      window.location.href = url;
    });

  });
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
    const sortSelect = document.getElementById('sort-select');
    const postNumber = document.getElementById('post-number');
    const postList = document.querySelector('.post-list');

    // Count and display posts
    const posts = document.querySelectorAll('.post-list li.post-item');
    const translatedCount = Array.from(posts).filter(post => post.dataset.translated === 'true').length;
    const currentLang = localStorage.getItem('selectedLanguage') || 'en';
    const translatedText = translations[currentLang] || translations['en'];
    postNumber.innerHTML = `${posts.length} (${translatedCount} ${translatedText} by <a href="https://mistral.ai">AI</a>)`;

    // Restore from localStorage if available
    const savedLang = localStorage.getItem('selectedLanguage');
    if (savedLang) {
      sortSelect.value = savedLang;
    }

    // Event listener for dropdown changes
    sortSelect.addEventListener('change', function () {
      const selectedLang = sortSelect.value;

      // Save to localStorage
      localStorage.setItem('selectedLanguage', selectedLang);

      // Redirect to appropriate page
      if (selectedLang === 'en') {
        window.location.href = '/';
      } else {
        window.location.href = `/index-${selectedLang}.html`;
      }
    });

  });
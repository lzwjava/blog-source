---
audio: false
generated: true
lang: hant
layout: post
title: 偵測用戶語言偏好
translated: true
type: note
---

### 偵測使用者的國家或語言偏好

由於你的 Jekyll 網誌是靜態的（生成的 HTML/JS），若沒有整合支援此功能的託管平台（例如 Netlify functions 或有限制的 GitHub Pages），就難以進行伺服器端偵測。最佳方法是在頁面載入時進行客戶端 JavaScript 偵測。你有兩個主要選擇：

1. **瀏覽器語言偏好**（推薦用於你的使用情境）：這會從使用者的瀏覽器設定（透過 `navigator.language` 或 `navigator.languages`）偵測其偏好的語言。這種方法速度快、無需外部 API、尊重使用者隱私（不分享 IP），且直接與語言而非國家綁定。國家通常使用多種語言（例如印度廣泛使用英語和印地語），因此對於自動設定下拉選單來說更為準確。

2. **基於 IP 的國家偵測**：這種方法使用免費的地理定位 API 從使用者的 IP 位址獲取國家，然後將其對應到語言。如果你特別需要國家資訊（例如用於分析），這會很有用，但它需要外部獲取資料、可能涉及隱私問題，且並非總是精確（VPN、代理伺服器）。將國家對應到語言是近似值。

你的目標似乎是自動選擇 `<select id="sort-select">` 下拉選單中的語言（例如英語對應 'date-desc|en'）。我將提供兩種方法的程式碼，你可以將其添加到 `<script>` 標籤內，緊接在 `const sortSelect = document.getElementById('sort-select');` 之後。

優先檢查 `localStorage`（如你的程式碼已實現），如果沒有儲存的偏好設定，則回退到偵測。

#### 選項 1：使用瀏覽器語言（更簡單且首選）
添加此程式碼片段。它檢查 `navigator.language` 的主要語言代碼（例如 'en-US' -> 'en', 'zh-CN' -> 'zh'）並將其對應到你的下拉選單值。如果沒有匹配項，則預設為英語。

```javascript
// Inside window.addEventListener('load', function () { ... });

// After const sortSelect = ...;

// Restore from localStorage if available
const savedSort = localStorage.getItem('sortOption');
if (savedSort) {
  sortSelect.value = savedSort;
} else {
  // Detect browser language if no saved preference
  let lang = navigator.language.toLowerCase().split('-')[0]; // e.g., 'en-US' -> 'en'
  
  // Special handling for Chinese variants (zh-Hant for traditional)
  if (lang === 'zh') {
    const fullLang = navigator.language.toLowerCase();
    if (fullLang.includes('tw') || fullLang.includes('hk') || fullLang.includes('hant')) {
      lang = 'hant';
    } else {
      lang = 'zh'; // Simplified Chinese
    }
  }

  // Map to your dropdown options (add more if needed)
  const langMap = {
    'en': 'date-desc|en',
    'zh': 'date-desc|zh',
    'ja': 'date-desc|ja',
    'es': 'date-desc|es',
    'hi': 'date-desc|hi',
    'fr': 'date-desc|fr',
    'de': 'date-desc|de',
    'ar': 'date-desc|ar',
    'hant': 'date-desc|hant'
  };

  sortSelect.value = langMap[lang] || 'date-desc|en'; // Default to English
}

updatePosts();
```

這會在載入時同步運行，因此沒有延遲。通過更改瀏覽器語言設定（例如在 Chrome 中：設定 > 語言）來測試它。

#### 選項 2：使用基於 IP 的國家偵測
這需要非同步獲取免費 API。我推薦 `country.is`，因為它簡單且僅返回國家代碼（例如 {country: 'US'}）。它是免費的，無需 API 金鑰，且是開源的。

添加此程式碼。注意：它是非同步的，因此我們使用 `await` 並將其包裝在非同步函數中以避免阻塞 UI。如果獲取失敗（例如被廣告攔截器阻擋），則預設為英語。

```javascript
// Inside window.addEventListener('load', async function () { ... });  // Make the load handler async

// After const sortSelect = ...;

// Restore from localStorage if available
const savedSort = localStorage.getItem('sortOption');
if (savedSort) {
  sortSelect.value = savedSort;
  updatePosts();
} else {
  try {
    // Fetch country code
    const response = await fetch('https://country.is/');
    const data = await response.json();
    const country = data.country.toUpperCase(); // e.g., 'US'

    // Map country codes to your languages (ISO 3166-1 alpha-2 codes)
    // This is approximate; expand as needed (e.g., multiple countries per language)
    const countryLangMap = {
      'US': 'date-desc|en',  // USA -> English
      'GB': 'date-desc|en',  // UK -> English
      'CN': 'date-desc|zh',  // China -> Simplified Chinese
      'TW': 'date-desc|hant', // Taiwan -> Traditional Chinese
      'HK': 'date-desc|hant', // Hong Kong -> Traditional Chinese
      'JP': 'date-desc|ja',  // Japan -> Japanese
      'ES': 'date-desc|es',  // Spain -> Spanish
      'MX': 'date-desc|es',  // Mexico -> Spanish (example for Latin America)
      'IN': 'date-desc|hi',  // India -> Hindi
      'FR': 'date-desc|fr',  // France -> French
      'DE': 'date-desc|de',  // Germany -> German
      'SA': 'date-desc|ar',  // Saudi Arabia -> Arabic
      'AE': 'date-desc|ar'   // UAE -> Arabic
    };

    sortSelect.value = countryLangMap[country] || 'date-desc|en'; // Default to English
  } catch (error) {
    console.warn('Country detection failed:', error);
    sortSelect.value = 'date-desc|en'; // Fallback
  }

  updatePosts();
}
```

- **注意事項**：
  - 如所示，將 `window.addEventListener` 更新為 `async function ()`。
  - 關於隱私：如有需要（例如歐盟的 GDPR），請告知使用者。某些瀏覽器/API 可能會阻擋跨來源請求；請徹底測試。
  - 如果你偏好不同的 API，替代方案包括 `https://ip-api.com/json/`（返回更多資料，如 `{ "countryCode": "US" }`）或 `https://ipgeolocation.io/ip_location/`（註冊免費層級）。
  - 速率限制：對於個人網誌來說這些限制很寬鬆，但如果流量增長請注意監控。

#### 其他考量
- **回退與使用者覆寫**：使用者始終可以更改下拉選單，並且它會儲存到 localStorage。如果自動偵測並非總是所需，你可以添加一個「偵測語言」按鈕。
- **測試**：使用 VPN 模擬不同國家，或使用瀏覽器擴充功能偽造語言。
- **隱私**：瀏覽器語言風險較低。對於 IP 方法，如果你的受眾對此敏感，請考慮添加同意提示。
- **結合兩者**：首先使用瀏覽器語言，如果它與你支援的語言不匹配，則使用 IP（但保持簡單）。
- **Jekyll 特定**：無需更改 Jekyll 配置。如果你在 Netlify/Vercel 上託管，可以使用 edge functions 進行伺服器端偵測，但這對於此處來說過於複雜。

如果這不起作用或者你可以分享錯誤資訊，請提供更多詳細資料！

[Country.is API](https://country.is/)  
[IP-API Geolocation](https://ip-api.com/)  
[ipgeolocation.io](https://ipgeolocation.io/)
---
audio: false
generated: true
lang: fr
layout: post
title: Détection de la Préférence Linguistique de l'Utilisateur
translated: true
type: note
---

### Détection de la langue ou du pays de l'utilisateur

Étant donné que votre blog Jekyll est statique (HTML/JS généré), vous ne pouvez pas facilement effectuer une détection côté serveur sans intégrer une plateforme d'hébergement qui la prend en charge (par exemple, les fonctions Netlify ou GitHub Pages avec des limitations). La meilleure approche est la détection côté client via JavaScript au chargement de la page. Vous avez deux options principales :

1.  **Préférence de langue du navigateur** (Recommandé pour votre cas d'usage) : Cette méthode détecte la langue préférée de l'utilisateur à partir des paramètres de son navigateur (via `navigator.language` ou `navigator.languages`). Elle est rapide, ne nécessite pas d'API externes, respecte la vie privée de l'utilisateur (aucun partage d'adresse IP) et est directement liée à la langue plutôt qu'au pays. Les pays ont souvent plusieurs langues (par exemple, l'Inde utilise largement l'anglais aux côtés du hindi), cette méthode est donc plus précise pour la sélection automatique dans le menu déroulant.

2.  **Détection du pays par IP** : Cette méthode utilise une API de géolocalisation gratuite pour obtenir le pays à partir de l'adresse IP de l'utilisateur, puis le mappe à une langue. Elle est utile si vous avez spécifiquement besoin d'informations sur le pays (par exemple, pour l'analyse), mais elle nécessite un appel externe, peut avoir des implications en matière de vie privée et n'est pas toujours précise (VPN, proxies). Le mappage du pays vers la langue est approximatif.

Votre objectif semble être la sélection automatique de la langue dans le menu déroulant `<select id="sort-select">` (par exemple, 'date-desc|en' pour l'anglais). Je vais fournir le code pour les deux méthodes, que vous pouvez ajouter à l'intérieur de votre balise `<script>`, juste après `const sortSelect = document.getElementById('sort-select');`.

Priorisez la vérification du `localStorage` (comme votre code le fait déjà), puis utilisez la détection comme solution de repli si aucune préférence enregistrée n'existe.

#### Option 1 : Utilisation de la langue du navigateur (Plus simple et préférée)
Ajoutez cet extrait de code. Il vérifie le code de langue principal à partir de `navigator.language` (par exemple, 'en-US' -> 'en', 'zh-CN' -> 'zh') et le mappe à vos valeurs de menu déroulant. L'anglais est utilisé par défaut si aucune correspondance n'est trouvée.

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

Ce code s'exécute de manière synchrone au chargement, donc aucun délai. Testez-le en modifiant les paramètres de langue de votre navigateur (par exemple, dans Chrome : Paramètres > Langues).

#### Option 2 : Utilisation de la détection du pays par IP
Cela nécessite un appel asynchrone (fetch) à une API gratuite. Je recommande `country.is` car elle est simple et ne renvoie que le code du pays (par exemple, {country: 'US'}). Elle est gratuite, ne nécessite pas de clé API et est open-source.

Ajoutez ce code. Note : Il est asynchrone, nous utilisons donc `await` et l'enveloppons dans une fonction asynchrone pour éviter de bloquer l'interface utilisateur. Si l'appel échoue (par exemple, à cause de bloqueurs de publicité), il revient par défaut à l'anglais.

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

-   **Notes** :
    -   Mettez à jour le `window.addEventListener` en `async function ()` comme indiqué.
    -   Pour la vie privée : Informez les utilisateurs si nécessaire (RGPD dans l'UE). Certains navigateurs/API peuvent bloquer les requêtes cross-origin ; testez soigneusement.
    -   Si vous préférez une autre API, les alternatives incluent `https://ip-api.com/json/` (renvoie plus de données comme `{ "countryCode": "US" }`) ou `https://ipgeolocation.io/ip_location/` (inscrivez-vous pour le niveau gratuit).
    -   Limites de débit : Elles sont généreuses pour les blogs personnels, mais surveillez si le trafic augmente.

#### Considérations supplémentaires

-   **Solution de repli et remplacement par l'utilisateur** : Les utilisateurs peuvent toujours modifier le menu déroulant, et la valeur est enregistrée dans le localStorage. Vous pourriez ajouter un bouton "Détecter la langue" si la détection automatique n'est pas toujours souhaitée.
-   **Tests** : Utilisez des VPN pour simuler différents pays ou des extensions de navigateur pour simuler des langues.
-   **Vie privée** : La langue du navigateur présente un faible risque. Pour les méthodes par IP, envisagez d'ajouter une demande de consentement si votre public est sensible.
-   **Combinaison des deux** : Utilisez d'abord la langue du navigateur, puis l'adresse IP si elle ne correspond pas à celles que vous prenez en charge (mais gardez cela simple).
-   **Spécifique à Jekyll** : Aucun changement de configuration Jekyll n'est nécessaire. Si vous hébergez sur Netlify/Vercel, vous pourriez utiliser les fonctions edge pour une détection côté serveur, mais c'est excessif ici.

Si cela ne fonctionne pas ou si vous pouvez partager des erreurs, fournissez plus de détails !

[API Country.is](https://country.is/)  
[Géolocalisation IP-API](https://ip-api.com/)  
[ipgeolocation.io](https://ipgeolocation.io/)
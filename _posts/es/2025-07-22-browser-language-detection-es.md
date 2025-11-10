---
audio: false
generated: true
lang: es
layout: post
title: Preferencia de Idioma del Usuario
translated: true
type: note
---

### Detectar el país o preferencia de idioma del usuario

Dado que tu blog de Jekyll es estático (HTML/JS generado), no puedes hacer una detección del lado del servidor fácilmente sin integrarte con una plataforma de hosting que lo admita (por ejemplo, funciones de Netlify o GitHub Pages con limitaciones). El mejor enfoque es la detección del lado del cliente con JavaScript al cargar la página. Tienes dos opciones principales:

1.  **Preferencia de idioma del navegador** (Recomendado para tu caso de uso): Esto detecta el idioma preferido del usuario desde la configuración de su navegador (a través de `navigator.language` o `navigator.languages`). Es rápido, no requiere APIs externas, respeta la privacidad del usuario (sin compartir IP) y se relaciona directamente con el idioma en lugar del país. Los países a menudo tienen múltiples idiomas (por ejemplo, India usa inglés ampliamente junto con hindi), por lo que esto es más preciso para configurar automáticamente el menú desplegable.

2.  **Detección de país basada en IP**: Esto utiliza una API de geolocalización gratuita para obtener el país desde la dirección IP del usuario, luego lo asigna a un idioma. Es útil si específicamente necesitas información del país (por ejemplo, para análisis), pero requiere una solicitud externa, puede tener implicaciones de privacidad y no siempre es precisa (VPNs, proxies). Mapear un país a un idioma es aproximado.

Tu objetivo parece ser seleccionar automáticamente el idioma en el menú desplegable `<select id="sort-select">` (por ejemplo, 'date-desc|en' para inglés). Proporcionaré código para ambos métodos, que puedes agregar dentro de tu etiqueta `<script>`, justo después de `const sortSelect = document.getElementById('sort-select');`.

Prioriza verificar `localStorage` (como tu código ya lo hace), luego recurre a la detección si no existe una preferencia guardada.

#### Opción 1: Usar el idioma del navegador (Más simple y preferida)
Agrega este fragmento de código. Verifica el código de idioma principal de `navigator.language` (por ejemplo, 'en-US' -> 'en', 'zh-CN' -> 'zh') y lo asigna a los valores de tu menú desplegable. Usa inglés como valor predeterminado si no hay coincidencia.

```javascript
// Dentro de window.addEventListener('load', function () { ... });

// Después de const sortSelect = ...;

// Restaurar desde localStorage si está disponible
const savedSort = localStorage.getItem('sortOption');
if (savedSort) {
  sortSelect.value = savedSort;
} else {
  // Detectar el idioma del navegador si no hay preferencia guardada
  let lang = navigator.language.toLowerCase().split('-')[0]; // ej., 'en-US' -> 'en'
  
  // Manejo especial para variantes del chino (zh-Hant para tradicional)
  if (lang === 'zh') {
    const fullLang = navigator.language.toLowerCase();
    if (fullLang.includes('tw') || fullLang.includes('hk') || fullLang.includes('hant')) {
      lang = 'hant';
    } else {
      lang = 'zh'; // Chino simplificado
    }
  }

  // Mapear a las opciones de tu menú desplegable (agrega más si es necesario)
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

  sortSelect.value = langMap[lang] || 'date-desc|en'; // Valor predeterminado: Inglés
}

updatePosts();
```

Esto se ejecuta de forma síncrona al cargar, por lo que no hay retrasos. Pruébalo cambiando la configuración de idioma de tu navegador (por ejemplo, en Chrome: Configuración > Idiomas).

#### Opción 2: Usar detección de país basada en IP
Esto requiere una solicitud asíncrona a una API gratuita. Recomiendo `country.is` porque es simple y devuelve solo el código del país (por ejemplo, {country: 'US'}). Es gratuito, no necesita clave API y es de código abierto.

Agrega este código. Nota: Es asíncrono, por lo que usamos `await` y lo envolvemos en una función asíncrona para evitar bloquear la interfaz de usuario. Si la solicitud falla (por ejemplo, bloqueadores de anuncios), usa inglés como valor predeterminado.

```javascript
// Dentro de window.addEventListener('load', async function () { ... });  // Hacer que el manejador de carga sea asíncrono

// Después de const sortSelect = ...;

// Restaurar desde localStorage si está disponible
const savedSort = localStorage.getItem('sortOption');
if (savedSort) {
  sortSelect.value = savedSort;
  updatePosts();
} else {
  try {
    // Obtener el código de país
    const response = await fetch('https://country.is/');
    const data = await response.json();
    const country = data.country.toUpperCase(); // ej., 'US'

    // Mapear códigos de país a tus idiomas (códigos ISO 3166-1 alpha-2)
    // Esto es aproximado; amplía según sea necesario (ej., múltiples países por idioma)
    const countryLangMap = {
      'US': 'date-desc|en',  // USA -> Inglés
      'GB': 'date-desc|en',  // UK -> Inglés
      'CN': 'date-desc|zh',  // China -> Chino simplificado
      'TW': 'date-desc|hant', // Taiwán -> Chino tradicional
      'HK': 'date-desc|hant', // Hong Kong -> Chino tradicional
      'JP': 'date-desc|ja',  // Japón -> Japonés
      'ES': 'date-desc|es',  // España -> Español
      'MX': 'date-desc|es',  // México -> Español (ejemplo para Latinoamérica)
      'IN': 'date-desc|hi',  // India -> Hindi
      'FR': 'date-desc|fr',  // Francia -> Francés
      'DE': 'date-desc|de',  // Alemania -> Alemán
      'SA': 'date-desc|ar',  // Arabia Saudita -> Árabe
      'AE': 'date-desc|ar'   // EAU -> Árabe
    };

    sortSelect.value = countryLangMap[country] || 'date-desc|en'; // Valor predeterminado: Inglés
  } catch (error) {
    console.warn('La detección de país falló:', error);
    sortSelect.value = 'date-desc|en'; // Respaldo
  }

  updatePosts();
}
```

-   **Notas**:
    - Actualiza el `window.addEventListener` a `async function ()` como se muestra.
    - Para la privacidad: Informa a los usuarios si es necesario (GDPR en la UE). Algunos navegadores/APIs pueden bloquear solicitudes de origen cruzado; prueba exhaustivamente.
    - Si prefieres una API diferente, las alternativas incluyen `https://ip-api.com/json/` (devuelve más datos como `{ "countryCode": "US" }`) o `https://ipgeolocation.io/ip_location/` (regístrate para el nivel gratuito).
    - Límites de tasa: Estos son generosos para blogs personales, pero monitorea si el tráfico crece.

#### Consideraciones adicionales

-   **Respaldo y anulación del usuario**: Los usuarios siempre pueden cambiar el menú desplegable, y se guarda en localStorage. Podrías agregar un botón "Detectar idioma" si la detección automática no siempre es deseada.
-   **Pruebas**: Usa VPNs para simular diferentes países o extensiones del navegador para suplantar idiomas.
-   **Privacidad**: El idioma del navegador es de bajo riesgo. Para los métodos de IP, considera agregar un aviso de consentimiento si tu audiencia es sensible.
-   **Combinar ambos**: Usa primero el idioma del navegador, luego la IP si no coincide con los que admites (pero manténlo simple).
-   **Específico de Jekyll**: No se necesitan cambios en la configuración de Jekyll. Si alojas en Netlify/Vercel, podrías usar funciones edge para la detección del lado del servidor, pero eso es excesivo aquí.

Si esto no funciona o puedes compartir errores, ¡proporciona más detalles!

[Country.is API](https://country.is/)  
[IP-API Geolocation](https://ip-api.com/)  
[ipgeolocation.io](https://ipgeolocation.io/)
---
audio: false
generated: true
lang: es
layout: post
title: Optimización del Rendimiento de gtag.js en Jekyll GitHub Pages
translated: true
type: note
---

El uso de `gtag.js` en un sitio de GitHub Pages construido con Jekyll presenta algunas limitaciones únicas, ya que GitHub Pages tiene un control limitado del lado del servidor y no hay acceso directo a las cabeceras de caché o a la secuencia de comandos del lado del servidor. Sin embargo, aún puedes optimizar la velocidad de carga de `https://www.googletagmanager.com/gtag/js?id=UA-66656236-1` utilizando técnicas del lado del cliente y configuraciones específicas de Jekyll. A continuación se presentan estrategias dirigidas para mejorar su rendimiento en este contexto:

---

### 1. **Cargar `gtag.js` de Forma Asíncrona**
Asegúrate de que el script `gtag.js` se cargue de forma asíncrona para evitar bloquear la representación de la página. En tu sitio de Jekyll:
- Añade el script a tu layout de Jekyll o al archivo include (por ejemplo, `_includes/analytics.html` o directamente en tu layout `default.html`).
- Usa el atributo `async`:
```html
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-66656236-1"></script>
```
- Coloca esto en el `<head>` o justo antes de `</body>` en tu plantilla de Jekyll (por ejemplo, `_layouts/default.html`):
```html
<head>
  <script async src="https://www.googletagmanager.com/gtag/js?id=UA-66656236-1"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'UA-66656236-1');
  </script>
</head>
```
- **Por qué ayuda**: `async` asegura que el script no bloquee el análisis del HTML, reduciendo el tiempo de carga percibido.

---

### 2. **Añadir Preconnect para el Dominio de Google**
Reduce la búsqueda de DNS y la latencia de conexión añadiendo una sugerencia `preconnect` para `googletagmanager.com`. En tu layout de Jekyll (`_layouts/default.html` o `_includes/head.html`):
```html
<link rel="preconnect" href="https://www.googletagmanager.com" crossorigin>
```
- Coloca esto en el `<head>` antes del script `gtag.js`.
- **Por qué ayuda**: Inicia la resolución DNS y la conexión TCP antes, acelerando la carga de `gtag.js`.

---

### 3. **Carga Diferida (Lazy-Load) de `gtag.js`**
Dado que GitHub Pages es estático, puedes cargar `gtag.js` de forma diferida para priorizar el contenido crítico. Añade el siguiente JavaScript a tu plantilla de Jekyll o a un archivo JS separado (por ejemplo, `assets/js/analytics.js`):
```javascript
window.addEventListener('load', () => {
  const script = document.createElement('script');
  script.src = 'https://www.googletagmanager.com/gtag/js?id=UA-66656236-1';
  script.async = true;
  document.head.appendChild(script);
  script.onload = () => {
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'UA-66656236-1');
  };
});
```
- Incluye este script en tu layout de Jekyll:
```html
<script src="{{ '/assets/js/analytics.js' | relative_url }}"></script>
```
- **Por qué ayuda**: Retrasa la carga de `gtag.js` hasta después de que se carguen los recursos críticos de la página (por ejemplo, HTML, CSS), mejorando la velocidad inicial de la página.

---

### 4. **Usar un Proxy CDN a través de Cloudflare**
GitHub Pages no permite cabeceras de caché personalizadas, pero puedes redirigir `gtag.js` a través de una CDN como Cloudflare para almacenarlo en caché más cerca de tus usuarios:
1. **Configurar Cloudflare**:
   - Añade tu sitio de GitHub Pages a Cloudflare (por ejemplo, `username.github.io`).
   - Habilita el DNS y el proxy de Cloudflare para tu dominio.
2. **Proxying de `gtag.js`**:
   - Crea una Page Rule en Cloudflare para almacenar en caché el script `gtag.js` o aloja una copia local en la carpeta `_site` de tu sitio Jekyll (por ejemplo, `assets/js/gtag.js`).
   - Actualiza tu etiqueta de script:
```html
<script async src="{{ '/assets/js/gtag.js' | relative_url }}"></script>
```
   - Sincroniza la copia local con el `gtag.js` de Google periódicamente para asegurarte de que esté actualizada (proceso manual o mediante un script de CI/CD).
3. **Configuración de Caché**:
   - En Cloudflare, establece una regla de caché para el script (por ejemplo, `Cache Everything` con un TTL de 1 hora).
- **Por qué ayuda**: Los servidores edge de Cloudflare reducen la latencia al servir el script desde una ubicación más cercana a tus usuarios.
- **Nota**: Ten cuidado con el proxying de los scripts de Google, ya que pueden actualizarse con frecuencia. Prueba exhaustivamente para asegurarte de que el seguimiento funciona.

---

### 5. **Optimizar la Construcción y Entrega de Jekyll**
Asegúrate de que tu sitio Jekyll esté optimizado para minimizar el tiempo total de carga de la página, lo que ayuda indirectamente al rendimiento de `gtag.js`:
- **Minificar Assets**:
  - Usa un plugin de Jekyll como `jekyll-compress` o `jekyll-minifier` para minificar HTML, CSS y JS.
  - Añade a tu `_config.yml`:
```yaml
plugins:
  - jekyll-compress
```
- **Habilitar Compresión Gzip**:
  - GitHub Pages habilita automáticamente Gzip para los archivos admitidos, pero confirma que tus archivos CSS/JS estén comprimidos revisando la cabecera `Content-Encoding` en las herramientas de desarrollo del navegador.
- **Reducir Recursos Bloqueantes**:
  - Minimiza el número de archivos CSS/JS que bloquean la representación cargados antes de `gtag.js`.
  - Usa `jekyll-assets` o similar para optimizar la entrega de assets:
```yaml
plugins:
  - jekyll-assets
```
- **CSS Crítico Inline**:
  - Incluye el CSS crítico en el `<head>` y difiere el CSS no crítico para reducir el tiempo de bloqueo de representación, lo que puede hacer que `gtag.js` parezca cargarse más rápido.
- **Optimización de Imágenes**:
  - Comprime imágenes usando `jekyll-picture-tag` o un plugin similar para reducir el peso total de la página, liberando ancho de banda para `gtag.js`.

---

### 6. **Cambiar a Analytics Minimalista**
Si `gtag.js` sigue siendo lento o si analytics no es crítico:
- Considera alternativas más ligeras como Plausible o Fathom, que usan scripts más pequeños (~1 KB frente a ~50 KB para `gtag.js`).
- Ejemplo para Plausible:
```html
<script defer data-domain="yourdomain.com" src="https://plausible.io/js/plausible.js"></script>
```
- Añade esto a tu `_includes/analytics.html` de Jekyll e inclúyelo en tu layout.
- **Por qué ayuda**: Los scripts más pequeños se cargan más rápido, especialmente en la infraestructura estática de GitHub Pages.

---

### 7. **Probar y Monitorizar el Rendimiento**
- **Medir el Tiempo de Carga**:
  - Usa Chrome DevTools (pestaña Network) para comprobar el tiempo de carga de `gtag.js`.
  - Prueba con herramientas como Lighthouse o WebPageTest para evaluar el rendimiento general de la página.
- **Simular Ubicaciones de Usuarios**:
  - Usa una herramienta como Pingdom para probar los tiempos de carga desde regiones donde se encuentra tu audiencia, ya que el rendimiento de GitHub Pages y la CDN de Google varían geográficamente.
- **Monitorizar Métricas de Usuario Real**:
  - Si usas Google Analytics, revisa el informe de Velocidad del Sitio para rastrear el impacto de `gtag.js`.
- **Depuración Específica de Jekyll**:
  - Ejecuta `jekyll build --profile` para identificar componentes de construcción lenta en tu sitio que podrían afectar indirectamente al rendimiento.

---

### 8. **Limitaciones con GitHub Pages**
- **Sin Control del Lado del Servidor**: GitHub Pages es un host estático, por lo que no puedes implementar etiquetado del lado del servidor o cabeceras de caché personalizadas para `gtag.js`.
- **Sin HTTP/3**: GitHub Pages usa HTTP/2, que es rápido pero no tan optimizado como HTTP/3. Una CDN como Cloudflare puede actualizar a HTTP/3.
- **Latencia Geográfica**: Los servidores de GitHub Pages están principalmente en EE. UU., por lo que los usuarios lejos de EE. UU. pueden experimentar cargas más lentas. Una CDN mitiga esto.

---

### Ejemplo de Configuración de Jekyll
Aquí hay un ejemplo de `_includes/analytics.html` para tu sitio Jekyll que combina `preconnect` y `async`:
```html
<link rel="preconnect" href="https://www.googletagmanager.com" crossorigin>
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-66656236-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'UA-66656236-1');
</script>
```
Inclúyelo en tu layout (`_layouts/default.html`):
```html
<head>
</head>
```

---

### Próximos Pasos
- **Probar el Rendimiento Actual**: Comparte el tiempo de carga actual para `gtag.js` (desde las herramientas de desarrollo del navegador) o la URL de tu sitio, y puedo analizarlo más a fondo.
- **Contexto Geográfico**: Déjame saber la ubicación principal de tu audiencia (por ejemplo, EE. UU., Europa, Asia) para adaptar las recomendaciones de CDN o proxy.
- **Configuración de Cloudflare**: Si estás abierto a usar Cloudflare, puedo proporcionar pasos detallados para redirigir `gtag.js`.
- **Analytics Alternativo**: Si estás abierto a cambiar de Google Analytics, puedo recomendar herramientas ligeras específicas y su integración con Jekyll.

¿Te gustaría que me centre en alguno de estos aspectos o que realice un análisis específico (por ejemplo, probar el rendimiento de tu sitio o proporcionar una guía de configuración de Cloudflare)?
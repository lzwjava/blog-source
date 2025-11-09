---
audio: false
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Prevención de la Invalidación de Caché CSS en Jekyll
translated: true
type: note
---

Lo que estás viendo es Jekyll (a través del tema o la pipeline de `jekyll-assets`/`jekyll-feed`/`minima`) añadiendo automáticamente una **huella digital (hash)** a la URL de tu hoja de estilo para cache-busting. Por eso el mismo archivo CSS termina con diferentes cadenas de consulta `?v=...` cuando se reconstruye.

Si no quieres que Jekyll cambie esa cadena de consulta en cada compilación, puedes deshabilitar o anular el comportamiento de "cache busting"/"digest":

### Opción 1. Usar un enlace fijo

En lugar de la etiqueta helper de Jekyll (ej. `{{ "/assets/css/style.css" | relative_url }}` o `{{ "/assets/css/style.css" | asset_path }}`), simplemente escribe manualmente:

```html
<link rel="stylesheet" href="/assets/css/style.css">
```

De esta manera, no se inyecta ninguna huella digital.

### Opción 2. Deshabilitar la generación de digest para assets

Si estás usando **jekyll-assets** o un tema que genera huellas digitales para los archivos, puedes deshabilitar la generación de digest en `_config.yml`:

```yml
assets:
  digest: false
```

### Opción 3. Usar `relative_url` sin digest

Si tu tema usa algo como:

```liquid
<link rel="stylesheet" href="{{ '/assets/css/style.css' | relative_url }}">
```

asegúrate de no pasarlo a través de `asset_path` o `absolute_url` con la generación de digest habilitada. Simplemente usa `relative_url`.

---

👉 En resumen:

* Si quieres que **nunca cambie**, escribe la ruta manualmente.
* Si quieres controlarlo mediante configuración, establece `assets.digest: false`.
* Si aún quieres versionado pero mantenerlo estable, necesitarías gestionar tu propia cadena `?v=...` manualmente.

¿Quieres que sea **completamente estático** (nunca cambie), o solo quieres evitar que Jekyll **genere nuevos hashes en cada compilación**?
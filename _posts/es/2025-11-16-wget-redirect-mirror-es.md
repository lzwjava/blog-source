---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Descarga normal de wget desde el espejo de mirror.accum.se
translated: true
type: note
---

Tu comando `wget` está accediendo a `https://mirror.accum.se/mirror/wikimedia.org/dumps/...` y recibiendo un **redireccionamiento 302** a `https://laotzu.ftp.acc.umu.se/...`. Este es un comportamiento completamente normal y esperado para el espejo **accum.se** — he aquí por qué sucede y qué significa:

### Por qué ocurre el redireccionamiento
`mirror.accum.se` es únicamente un **redireccionador / balanceador de carga** gestionado por el Academic Computer Club en la Universidad de Umeå (ACC) en Suecia.
**No** aloja los archivos por sí mismo. En su lugar:

- Consulta la geolocalización de tu IP (o a veces la carga)
- Te redirige automáticamente al servidor de almacenamiento real más rápido/cercano en su granja de espejos
- En tu caso, eligió `laotzu.ftp.acc.umu.se` (que es el servidor FTP/HTTP real que tiene los datos)

Este es el mismo sistema que han usado durante muchos años. Otros nombres de host comunes a los que podrías ser redirigido son:

- `issac.ftp.acc.umu.se`
- `laotzu.ftp.acc.umu.se` (el que te ha tocado)
- `morpork.ftp.acc.umu.se`
- etc.

Así que, aunque escribiste `mirror.accum.se` en tu script, casi siempre terminas descargando desde uno de los servidores back-end `*.ftp.acc.umu.se`.

### Por qué viste "206 Partial Content" en el primer archivo
Porque tú (o alguien/algun script) ya había comenzado a descargar ese mismo archivo anteriormente, `wget -c` detectó el archivo local parcial y envió una petición `Range`. El servidor reanudó correctamente la descarga → 206 Contenido Parcial. ¡Eso es bueno!

### ¿Hay algún problema?
No. Todo está funcionando según lo previsto.

- El redireccionamiento es normal e inofensivo
- El servidor final (`laotzu.ftp.acc.umu.se`) sigue siendo el espejo oficial de ACC/Wikimedia
- Las sumas de verificación serán idénticas sin importar a qué servidor back-end seas redirigido

### Si quieres evitar el redireccionamiento (opcional)
Puedes omitir completamente el redireccionador y apuntar directamente a uno de los hosts reales, por ejemplo:

```bash
# Estos tres tienen round-robin detrás de mirror.accum.se de todos modos
wget -c https://laotzu.ftp.acc.umu.se/mirror/wikimedia.org/dumps/enwiki/20251101/...
# o
wget -c https://issac.ftp.acc.umu.se/mirror/wikimedia.org/dumps/enwiki/20251101/...
```

Pero la mayoría de la gente sigue usando `mirror.accum.se` porque el redireccionador elige automáticamente el mejor para ti.

### TL;DR
Tu script está bien. El redireccionamiento 302 de `mirror.accum.se` → `laotzu.ftp.acc.umu.se` es el comportamiento normal y esperado de ese espejo. No hay ningún problema, y sigues descargando el volcado auténtico de Wikimedia. Sigue usando `mirror.accum.se` — es uno de los espejos más rápidos y confiables a nivel mundial.
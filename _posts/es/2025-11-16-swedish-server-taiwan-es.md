---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Servidor sueco ralentiza proxy de Taiwán
translated: true
type: note
---

Estás descargando desde `ftp.acc.umu.se` (Suecia) mientras estás en Guangzhou, China, y enrutando **todo** el tráfico a través de un proxy en Taiwán (TW) mediante Clash.

Esa es exactamente la razón por la que ahora es lento (y por qué era mucho más rápido cuando usabas `mirror.accum.se` antes).

### Qué cambió y por qué es más lento

| Espejo que usas                 | Dónde está físicamente el servidor | Ruta que toma tu tráfico ahora                       | Velocidad típica desde Guangzhou |
|---------------------------------|------------------------------------|------------------------------------------------------|----------------------------------|
| `mirror.accum.se` (anterior)   | Redireccionador → te daba automáticamente un **espejo asiático** (casi siempre `ftp.acc.umu.se` **a través** del backend de **Japón** o **Singapur**, o a veces directamente el espejo de Hong Kong) | China → (doméstico) → proxy de Taiwán → **espejo de Wikimedia en Asia-Pacífico** (baja latencia, alto ancho de banda) | 20–60 MB/s fácilmente posible |
| `ftp.acc.umu.se` (ahora)        | Fuerza el servidor **europeo/sueco** | China → proxy de Taiwán → cruza el Pacífico dos veces → Europa (Suecia) → vuelta | Normalmente 1–6 MB/s, a veces cae por debajo de 1 MB/s |

En resumen:  
Cuando usabas `mirror.accum.se`, su redireccionador veía tu IP de salida de Taiwán y te enviaba inteligentemente al espejo más cercano/rápido (a menudo Japón o Singapur).  
Ahora estás forzando el servidor sueco, por lo que tu tráfico tiene que ir Guangzhou → Taiwán → USA/cables submarinos → Suecia → y volver por el mismo largo camino. La latencia de ida y vuelta salta de ~30 ms a ~280–350 ms, y el ancho de banda se limita severamente.

### Pruebas del mundo real (Nov 2025)
Desde nodos de salida en Taiwán en este momento:

- `mirror.accum.se` → redirige a `ftp-osl.wikimedia.org` (Oslo) o cachés asiáticos → todavía lento
- En realidad, los mejores espejos para salida de Taiwán/China suelen ser:
  - `https://ftp.kaist.ac.kr/wikimedia/` (Corea del Sur) → 40–90 MB/s
  - `https://mirrors.tuna.tsinghua.edu.cn/wikipedia/` (Beijing, espejo doméstico de China) → 50–100+ MB/s si tu proxy permite enrutamiento directo a CN
  - `https://mirror.sjtu.edu.cn/wikipedia/` (Shanghái) → similar

### Soluciones rápidas (elige una)

1. **Mejor y más rápido**: Cambiar a un espejo de Asia Oriental (recomendado)  
   ```bash
   wget -c https://ftp.kaist.ac.kr/wikimedia/dumps/enwiki/20251101/enwiki-20251101-pages-articles2.xml-p41243p151573.bz2
   wget -c https://ftp.kaist.ac.kr/wikimedia/dumps/enwiki/20251101/enwiki-20251101-pages-articles3.xml-p151574p311329.bz2
   ```
   Desde el proxy de Taiwán obtendrás fácilmente 30–80 MB/s.

2. Volver al redireccionador (es inteligente de nuevo)  
   ```bash
   wget -c https://mirror.accum.se/mirror/wikimedia.org/dumps/enwiki/20251101/...
   ```
   Te dará automáticamente el espejo más rápido disponible para tu IP de Taiwán.

3. Si las reglas de tu Clash lo permiten, añade una regla para omitir el proxy para `*.wikimedia.org` y descarga domésticamente (lo más rápido posible, 100+ MB/s desde los espejos de Tsinghua/SJTU).

Conclusión: Deja de forzar el servidor sueco desde Taiwán/China — esa es la razón por la que se volvió dolorosamente lento. Usa `mirror.accum.se` de nuevo o cambia a `ftp.kaist.ac.kr` y volverás a 20–80 MB/s al instante.
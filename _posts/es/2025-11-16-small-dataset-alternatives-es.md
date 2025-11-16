---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Alternativas de Conjuntos de Datos Pequeños y de Alta Calidad
translated: true
type: note
---

Sí, OpenWebText es enorme (~9B tokens, archivo de 17GB en uint16) y requiere mucho tiempo para el preprocesamiento y mucho espacio en disco. Aquí hay alternativas mucho más pequeñas y de alta calidad que se usan comúnmente para pruebas, depuración o para entrenar modelos pequeños rápidamente:

| Dataset                  | Tokens aprox. | Tamaño final .bin (uint16) | Por qué gusta                                                                      | Cómo obtenerlo rápidamente                                |
|--------------------------|----------------|----------------------------|------------------------------------------------------------------------------------|------------------------------------------------------------|
| **OpenWebText-10k**      | ~40M           | ~80MB                      | Misma distribución exacta que OpenWebText completo, solo los primeros 10k documentos | `load_dataset("openwebtext", split="train[:10k]")`         |
| **OpenWebText-100k**     | ~400M          | ~800MB                     | Sigue siendo muy representativo, termina de tokenizar en pocos minutos            | `split="train[:100k]"`                                     |
| **Muestra FineWeb-Edu**  | 50M–1B         | 100MB–2GB                  | Mayor calidad que OWT (filtrado estilo LLama), muy popular últimamente            | `load_dataset("HuggingFaceFW/fineweb-edu", name="sample-10BQ", split="train")` → ~50M tokens |
| **Shakespeare**          | ~1M            | ~2MB                       | Dataset clásico y minúsculo, perfecto para comprobaciones rápidas                 | `load_dataset("tiny_shakespeare")` o simplemente descargar el archivo .txt |
| **PG-19 (libros)**       | Completo 2.8B  | ~5.5GB                     | Libros de dominio público muy limpios, pero puedes tomar solo una parte           | `load_dataset("pg19", split="train[:5%]")` → ~140M tokens  |
| **C4 (subconjunto)**     | variable       | variable                   | Common Crawl limpiado por el equipo de T5, solo en inglés                          | `load_dataset("allenai/c4", "en", split="train[:1%]")` streaming=True |
| **Muestra RedPajama**    | 5M–200M        | 10MB–400MB                 | Mezcla de fuentes (CommonCrawl, Wikipedia, libros, etc.), misma receta que LLaMA   | `load_dataset("togethercomputer/RedPajama-Data-1T", name="sample", split="train")` |

### Mis recomendaciones personales según tu objetivo

1. Si solo quieres algo que se ejecute en < 5 minutos y quepa en cualquier sitio → **tiny_shakespeare**  
   (a los usuarios de nanoGPT les encanta este)

2. Si quieres algo que siga siendo "texto real de internet" pero minúsculo → Los primeros 10k documentos de OpenWebText  
   ```python
   dataset = load_dataset("openwebtext", split="train[:10000]")
   ```

3. Si quieres el dataset pequeño de más alta calidad actualmente (2025) → Muestra de 10B tokens de FineWeb-Edu  
   (~50M tokens, pero mucho más limpio que OWT, calidad casi idéntica a la que usan los mejores laboratorios)

   ```python
   dataset = load_dataset(
       "HuggingFaceFW/fineweb-edu",
       name="sample-10BQ",  # 10 mil millones de tokens muestreados, ~50M por fragmento si se corta
       split="train"
   )
   ```

4. Si quieres algo < 500MB pero aún así diverso → Muestra RedPajama (versión de 200M tokens)  
   ```python
   dataset = load_dataset("togethercomputer/RedPajama-Data-1T", name="sample-200M", split="train")
   ```

Todos estos se integran en tu script de preprocesamiento exactamente igual sin cambios (solo reemplaza la línea load_dataset).

Para una iteración rápida, suelo mantener tres archivos binarios en disco:
- `shakespeare.bin`   (~2MB)   → pruebas de sobreajuste
- `owt_10k.bin`       (~80MB)  → depuración de código nuevo
- `fineweb_edu_1B.bin` (~2GB) → entrenamiento real de modelos pequeños

¡Dime qué tamaño necesitas y te puedo dar la línea de código exacta!
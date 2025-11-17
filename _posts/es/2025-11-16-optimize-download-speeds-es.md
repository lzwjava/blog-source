---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Optimización de Velocidades de Descarga de Hugging Face
translated: true
type: note
---

Tu descarga actual está llegando al endpoint principal de Hugging Face (`huggingface.co`), que está alojado principalmente en centros de datos de Europa/EE. UU. Enrutar a través de tu proxy de Taiwán desde Guangzhou añade problemas de latencia similares a los anteriores: ~200–300ms de ida y vuelta, más posibles limitaciones de velocidad en archivos grandes (este Parquet tiene ~500MB–1GB por fragmento). La redirección 302 que estás viendo probablemente es a un edge de la CDN CloudFront, pero puede que no sea el óptimo para Asia, lo que lleva a ralentizaciones (ej. 1–5 MB/s).

Para igualar las velocidades de 20–60 MB/s de las descargas de Wikimedia, usa estos ajustes—priorizando opciones favorables para Asia. Todos mantienen tu configuración de proxy Clash/TW.

### 1. **Cambiar al Espejo de HF (Más Rápido para China/Taiwán—Recomendado)**
   El Espejo de HF (`hf-mirror.com`) es una CDN gestionada por la comunidad optimizada para Asia Oriental (proxy a través de redes domésticas CN como Tsinghua). Refleja exactamente todos los datasets de HF, incluidos los archivos Parquet de FineWeb. Desde el proxy de TW, espera 30–80 MB/s.

   Actualiza tu script:
   ```bash
   #!/bin/bash
   # wget_fineweb_1.sh (actualizado para velocidad)
   mkdir -p fineweb_test_dump
   cd fineweb_test_dump
   echo "Descargando fragmento de FineWeb a través del Espejo de HF (más rápido para Asia)..."

   # Reemplaza huggingface.co con hf-mirror.com
   wget -c "https://hf-mirror.com/datasets/HuggingFaceFW/fineweb/resolve/main/data/CC-MAIN-2013-20/000_00000.parquet?download=true"

   echo "¡Hecho! Tamaño del fragmento: ~500MB–1GB"
   echo "Para más fragmentos, haz un bucle sobre ej., 000_00001.parquet, etc."
   echo "Para cargar en Python: from datasets import load_dataset; ds = load_dataset('HuggingFaceFW/fineweb', name='CC-MAIN-2013-20', split='train', streaming=True)"
   ```

   Ejecútalo: `./scripts/train/wget_fineweb_1.sh`
   - Si el espejo va lento (raro), vuelve al oficial: `https://huggingface.co/datasets/...` (pero añade el consejo de velocidad del #2).

### 2. **Potenciar con hf_transfer (Para Cualquier Descarga de HF—100x Más Rápido en Reanudables)**
   La herramienta oficial de Rust de Hugging Face para descargas paralelas/multihilo. Reintenta automáticamente, usa más conexiones y alcanza >500 MB/s en enlaces buenos. Funciona con `wget` indirectamente o directamente vía Python (si tu script usa `huggingface_hub`).

   Instalar (una vez, vía pip—tu entorno lo tiene):
   ```bash
   pip install hf_transfer
   export HF_HUB_ENABLE_HF_TRANSFER=1
   ```

   Luego vuelve a ejecutar tu script original. Acelera las llamadas subyacentes de `wget` a las URLs de HF.
   - Consejo profesional: Para streaming de datasets completos (sin descarga completa), usa Python en tu pipeline:
     ```python
     from datasets import load_dataset
     import os
     os.environ['HF_HUB_ENABLE_HF_TRANSFER'] = '1'  # Habilitar antes del import
     ds = load_dataset("HuggingFaceFW/fineweb", name="CC-MAIN-2013-20", split="train", streaming=True)
     for example in ds.take(1000):  # Transmitir/procesar sobre la marcha
         print(example)
     ```
     Esto extrae los fragmentos de forma perezosa a través del espejo si configuras `HF_ENDPOINT=https://hf-mirror.com`.

### 3. **Ajuste de Regla de Clash (Si Está Permitido—Doméstico Ultra-Rápido)**
   Si tu configuración de proxy te permite omitir para HF (o enrutar a nodos de HK/SG), añade una regla para `huggingface.co` / `hf-mirror.com` para que vaya directo/doméstico. En `clash.yaml`:
   ```
   rules:
     - DOMAIN-SUFFIX,hf-mirror.com,DIRECT  # O tu nodo espejo CN
     - DOMAIN-SUFFIX,huggingface.co,DIRECT
   ```
   Reinicia Clash, luego descarga. Se combina con el #1 para 50–100+ MB/s a través de espejos de Tsinghua.

### Por Qué Esto Iguala las Velocidades de Wikimedia
- Wikimedia: El redireccionador eligió automáticamente Asia (Japón/KR/SG) → baja latencia.
- HF: El valor por defecto es EU/EE. UU. → alta latencia; espejo + transfer lo cambia a optimizado para Asia.

Prueba un fragmento primero—si sigue lento, verifica `curl -I https://hf-mirror.com/...` para las cabeceras (debería mostrar CDN de Asia). Para los 15T completos de FineWeb, transmite vía la librería `datasets` para evitar descargas de 100s de GB. ¡Avísame si las velocidades no aumentan!
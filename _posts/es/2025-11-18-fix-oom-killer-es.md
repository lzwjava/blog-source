---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Corrección del Asesino OOM en el Script de FineWeb
translated: true
type: note
---

El mensaje "Killed" sin ningún traceback de Python significa que el asesino OOM (Out-of-Memory) de Linux terminó el proceso. Esto sucede en el script `data/fineweb/prepare.py` porque intenta cargar todo tu archivo de texto concatenado de ~15 GB (`train_fineweb.txt`) en la RAM de una vez con algo como `open(...).read()` antes de tokenizar.

Aunque FineWeb-Edu está diseñado para streaming (el descargador oficial usa Hugging Face `datasets` y procesa los fragmentos uno por uno en trozos de ~100M tokens sin cargar nunca todo en memoria), la carpeta nanoGPT fineweb tiene una ruta de archivo local personalizada que no es eficiente en memoria para archivos grandes.

### Soluciones Rápidas (elige una)

1. **La Mejor y Recomendada: Usa el descargador oficial de FineWeb-Edu con streaming en lugar de tus archivos locales**  
   No uses el `data/fineweb/prepare.py` de nanoGPT en absoluto.  
   Usa el script más nuevo de Karpathy hecho exactamente para FineWeb-Edu de 10B tokens (o más grande):

   ```bash
   # Desde la raíz de nanoGPT (o desde cualquier lugar)
   wget https://raw.githubusercontent.com/karpathy/build-nanogpt/master/fineweb.py
   python fineweb.py
   ```

   Esto descarga y tokeniza la muestra FineWeb-Edu sample-10BT (10 mil millones de tokens, ~15-20 GB en crudo) en modo streaming usando `datasets.load_dataset(..., streaming=True)` y multiprocesamiento. Nunca carga el dataset completo en la RAM y produce los mismos fragmentos `.bin` que nanoGPT espera en una carpeta como `edu_fineweb10B/`.  
   Funciona bien en máquinas con 32-64 GB de RAM (o incluso menos si reduces `num_proc_load_dataset` y `num_proc` en el script).

   Para las versiones completas de 100B o 1T, solo cambia `remote_name = "sample-10BT"` a `"100BT"` o lo que necesites.

2. **Si realmente quieres mantener tu archivo local de 10 parquet → txt**  
   Modifica `data/fineweb/prepare.py` para procesar el texto en trozos en lugar de cargarlo todo:

   Abre el script y reemplaza el gran bloque `with open(local_file, 'r', encoding='utf-8') as f: data = f.read()` con algo como esto:

   ```python
   from tqdm import tqdm
   import tiktoken
   enc = tiktoken.get_encoding("gpt2")

   chunk_size = 1_000_000  # caracteres por trozo, ajusta si es necesario
   tokens = []
   with open(local_file, "r", encoding="utf-8") as f:
       while True:
           chunk = f.read(chunk_size)
           if not chunk:
               break
           tokens.extend(enc.encode_ordinary(chunk))  # o enc.encode(chunk)
           print(f"Tokenized so far: {len(tokens)/1e6:.1f}M tokens")
   tokens = np.array(tokens, dtype=np.uint16)
   ```

   Esto mantiene el pico de RAM por debajo de ~10-15 GB incluso para tu archivo de 15 GB.

3. **Soluciones de hardware (temporales, no ideales)**  
   - Añade mucho espacio de intercambio (swap) (ej., un archivo de swap de 64-128 GB). Será extremadamente lento una vez que empiece a usar el swap, pero puede que termine.  
     ```bash
     sudo fallocate -l 64G /swapfile
     sudo chmod 600 /swapfile
     sudo mkswap /swapfile
     sudo swapon /swapfile
     ```
   - Ejecuta en una máquina/instancia con ≥64 GB de RAM (ej., AWS r6i.4xlarge o más grande).

### Resumen
Simplemente ejecuta el `fineweb.py` oficial de build-nanogpt — es la solución más limpia y la que todo el mundo usa ahora para FineWeb. Tu archivo txt concatenado de 15 GB es el problema, no FineWeb en sí mismo.

[Script descargador oficial de FineWeb-Edu](https://raw.githubusercontent.com/karpathy/build-nanogpt/master/fineweb.py)  
[Página del dataset FineWeb-Edu](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu)
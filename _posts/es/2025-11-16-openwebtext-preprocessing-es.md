---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Script de Preprocesamiento del Conjunto de Datos OpenWebText
translated: true
type: note
---

### Resumen
Este script de Python procesa un archivo de texto grande que contiene el conjunto de datos OpenWebText (un corpus de texto extraído de la web similar al utilizado para entrenar modelos como GPT-2). El objetivo es:
- Dividir el texto crudo en "documentos" (fragmentos de texto) manejables.
- Crear un objeto `Dataset` de Hugging Face para un manejo sencillo.
- Tokenizar el texto usando el tokenizador GPT-2 Byte Pair Encoding (BPE) de TikToken (ignorando tokens especiales y añadiendo un marcador de fin de texto).
- Dividir el conjunto de datos en conjuntos de entrenamiento (99.95%) y validación (0.05%).
- Guardar los datos tokenizados como archivos binarios compactos (`train.bin` y `val.bin`) utilizando arrays mapeados en memoria de NumPy. Estos archivos almacenan secuencias de IDs de tokens (como enteros de 16 bits) para una carga eficiente durante el entrenamiento de modelos de machine learning.

El script está diseñado para ser eficiente en sistemas multi-núcleo, utilizando multiprocesamiento para la tokenización. Está inspirado en un módulo de carga de datos del repositorio de Flash Attention (enlazado en el código), que maneja un preprocesamiento similar para el entrenamiento de modelos de lenguaje. Nota: OpenWebText es masivo (~40GB sin comprimir), pero este script asume un archivo local `openwebtext.txt` previamente descargado. Los archivos de salida son mucho más pequeños: `train.bin` ~17GB (9B tokens) y `val.bin` ~8.5MB (4M tokens).

El script imprime la configuración del proxy al inicio (probablemente para depurar problemas de red durante cualquier descarga implícita, aunque aquí no hay ninguna explícita). Utiliza 8 procesos workers para la tokenización por defecto.

### Desglose Paso a Paso

#### 1. Importaciones y Configuración Inicial
```python
import os
import tarfile
from tqdm import tqdm
import numpy as np
import tiktoken
from huggingface_hub import hf_hub_download
from datasets import load_dataset # huggingface datasets
import datasets

print("HTTP_PROXY:", os.getenv("HTTP_PROXY"))
print("HTTPS_PROXY:", os.getenv("HTTPS_PROXY"))

# number of workers in .map() call
# good number to use is ~order number of cpu cores // 2
num_proc = 8

# number of workers in load_dataset() call
# best number might be different from num_proc above as it also depends on NW speed.
# it is better than 1 usually though
num_proc_load_dataset = num_proc

enc = tiktoken.get_encoding("gpt2")

datasets.logging.set_verbosity_info()
```
- **Propósito**: Importa librerías para manejo de archivos (`os`, `tarfile`), barras de progreso (`tqdm`), operaciones numéricas (`numpy`), tokenización (`tiktoken`) y utilidades de Hugging Face (`huggingface_hub`, `datasets`).
- **Impresiones de proxy**: Registra las variables de entorno para proxies HTTP/HTTPS, útil si el script encuentra restricciones de red (por ejemplo, para descargar modelos del tokenizador, aunque TikToken maneja esto internamente).
- **Workers**: Establece `num_proc=8` para el procesamiento paralelo en la tokenización (aproximadamente la mitad de los núcleos de la CPU para equilibrar). `num_proc_load_dataset` coincide pero no se usa aquí (remanente del código de inspiración, que carga desde Hugging Face).
- **Codificador**: Carga el tokenizador GPT-2 BPE (`enc`). Esto convierte el texto en IDs de tokens enteros (rango 0–50,256).
- **Registro**: Establece el registro de Hugging Face datasets a nivel "info" para una salida detallada durante el procesamiento.

La guarda `if __name__ == '__main__':` asegura que la lógica principal se ejecute solo cuando el script se ejecuta directamente (no cuando se importa).

#### 2. Lectura y División del Archivo de Texto
```python
if __name__ == '__main__':
    # Read the local openwebtext.txt file
    txt_file = os.path.join(os.path.dirname(__file__), 'openwebtext.txt')
    print(f"Reading from local file: {txt_file}")

    # Read the text content
    texts = []
    with open(txt_file, 'r', encoding='utf-8', errors='ignore') as f:
        # Read the entire file
        full_text = f.read().strip()

        # Try to split into documents by double newlines first
        documents = full_text.split('\n\n')

        # If we only got one document, split by single newlines
        if len(documents) <= 1:
            documents = full_text.split('\n')

        # If we still only have one document, split by period followed by space
        if len(documents) <= 1:
            # Split on period followed by space, then join back sentences
            sentences = full_text.split('. ')
            # Group sentences into chunks of ~100 sentences per document
            chunk_size = 100
            for i in range(0, len(sentences), chunk_size):
                chunk = '. '.join(sentences[i:i+chunk_size])
                if chunk.strip():
                    texts.append(chunk.strip() + '.')
        else:
            # Process documents from double/single newline splits
            for doc in documents:
                doc = doc.strip()
                if doc:  # Only add non-empty documents
                    texts.append(doc)

        print(f"Created {len(texts)} documents from the text file")
```
- **Lectura del archivo**: Abre `openwebtext.txt` (se asume que está en el mismo directorio que el script) en modo UTF-8, ignorando errores de codificación. Lee todo el contenido en `full_text` y elimina espacios en blanco.
- **Lógica de división**: Intenta dividir el texto en "documentos" (fragmentos lógicos como párrafos o artículos):
  - **Primario**: Dividir por dobles saltos de línea (`\n\n`), común para separar documentos en corpus.
  - **Respaldo 1**: Si eso produce ≤1 fragmento (por ejemplo, no hay dobles saltos de línea), dividir por saltos de línea simples (`\n`) para texto basado en líneas.
  - **Respaldo 2**: Si todavía hay ≤1 fragmento (por ejemplo, un solo bloque de texto), dividir en oraciones por `. ` (punto + espacio), luego agrupar cada 100 oraciones en un "documento". Esto evita entradas únicas demasiado largas. Añade un punto al final de cada fragmento para completitud.
- **Salida**: Almacena documentos no vacíos, sin espacios, en la lista `texts`. Imprime el número total creado (por ejemplo, 10k ejemplos para un subconjunto).
- **¿Por qué de esta manera?** OpenWebText es una concatenación de páginas web, por lo que dividir crea ejemplos de entrenamiento que no son solo volcados crudos. Esto imita cómo se procesan conjuntos de datos como BookCorpus.

#### 3. Creación y División del Conjunto de Datos
```python
    # Create dataset from texts
    dataset = datasets.Dataset.from_dict({'text': texts})

    # create train/val split from the 10k examples
    split_dataset = dataset.train_test_split(test_size=0.0005, seed=2357, shuffle=True)
    split_dataset['val'] = split_dataset.pop('test') # rename the test split to val
```
- **Creación del dataset**: Envuelve la lista `texts` en un `Dataset` de Hugging Face con una sola columna `'text'`. Esto permite operaciones paralelas eficientes como mapear.
- **División**: Utiliza `train_test_split` para dividir en conjuntos de entrenamiento (99.95%) y prueba (0.05%). El tamaño pequeño de validación es intencional para conjuntos de datos enormes: suficiente para evaluación sin desperdiciar cómputo.
  - `test_size=0.0005`: 0.05% para val (por ejemplo, ~50 ejemplos de 100k).
  - `seed=2357`: Semilla aleatoria fija para reproducibilidad.
  - `shuffle=True`: Aleatoriza antes de dividir.
- **Renombrar**: Extrae `'test'` y lo renombra a `'val'`. Ahora `split_dataset` es un diccionario con claves `'train'` y `'val'`, cada una un objeto `Dataset`.

#### 4. Función de Tokenización
```python
    # we now want to tokenize the dataset. first define the encoding function (gpt2 bpe)
    def process(example):
        ids = enc.encode_ordinary(example['text']) # encode_ordinary ignores any special tokens
        ids.append(enc.eot_token) # add the end of text token, e.g. 50256 for gpt2 bpe
        # note: I think eot should be prepended not appended... hmm. it's called "eot" though...
        out = {'ids': ids, 'len': len(ids)}
        return out
```
- **Propósito**: Convierte texto a IDs de tokens para entrada del modelo.
- **`encode_ordinary`**: Tokeniza la cadena de texto en una lista de enteros (vocabulario GPT-2). Ignora cualquier token no estándar en el texto.
- **Añadir EOT**: Añade el token de fin de texto (ID 50256 para GPT-2) al final. Esto señala el límite de la secuencia durante el entrenamiento. (El comentario señala un debate potencial sobre anteponer vs. añadir, pero añadir es común en configuraciones de LM causal como GPT).
- **Salida**: Devuelve un diccionario con `'ids'` (lista de IDs de tokens) y `'len'` (longitud de la secuencia, para sumar más tarde).

#### 5. Aplicación de la Tokenización
```python
    # tokenize the dataset
    tokenized = split_dataset.map(
        process,
        remove_columns=['text'],
        desc="tokenizing the splits",
        num_proc=num_proc,
    )
```
- **Mapeo**: Aplica `process` a cada ejemplo en los conjuntos de datos de entrenamiento/validación usando workers paralelos (`num_proc=8`).
- **`remove_columns=['text']`**: Elimina el texto original para ahorrar memoria (solo necesitamos tokens ahora).
- **Progreso**: Muestra una barra de progreso mediante `desc`. Este paso puede llevar tiempo para conjuntos de datos grandes debido a la codificación.

#### 6. Guardado de Datos Tokenizados en Archivos Binarios
```python
    # concatenate all the ids in each dataset into one large file we can use for training
    for split, dset in tokenized.items():
        arr_len = np.sum(dset['len'], dtype=np.uint64)
        filename = os.path.join(os.path.dirname(__file__), f'{split}.bin')
        dtype = np.uint16 # (can do since enc.max_token_value == 50256 is < 2**16)
        arr = np.memmap(filename, dtype=dtype, mode='w+', shape=(arr_len,))

        # Use adaptive batch size based on dataset size
        total_batches = min(1024, len(dset))
        if total_batches < 1024:
            print(f"Using {total_batches} batches for {split} dataset (size: {len(dset)})")

        idx = 0
        for batch_idx in tqdm(range(total_batches), desc=f'writing {filename}'):
            # Only process if this batch index is valid for the dataset size
            if batch_idx < len(dset):
                # Batch together samples for faster write
                batch = dset.shard(num_shards=total_batches, index=batch_idx, contiguous=True).with_format('numpy')
                arr_batch = np.concatenate(batch['ids'])
                # Write into mmap
                arr[idx : idx + len(arr_batch)] = arr_batch
                idx += len(arr_batch)
        arr.flush()
```
- **Bucle por divisiones**: Para `'train'` y `'val'`, calcula el recuento total de tokens (`arr_len`) sumando los campos `'len'`.
- **Array mapeado en memoria**: Crea un archivo memmap de NumPy (`train.bin` o `val.bin`) como un array escribible de enteros uint16 (se ajusta al valor máximo de token de GPT-2 de 50,256; ahorra ~50% de espacio vs. int32). La forma es 1D: `(total_tokens,)`.
- **Procesamiento por lotes para eficiencia**: Divide el conjunto de datos en hasta 1024 fragmentos (`total_batches`) para evitar cargar todo en la RAM a la vez. Para conjuntos de datos pequeños (<1024 ejemplos), usa el número exacto.
  - **`shard`**: Divide el conjunto de datos en lotes contiguos (sin barajar aquí).
  - **`with_format('numpy')`**: Convierte el lote a arrays NumPy para una concatenación rápida.
- **Escritura**: Concatena los IDs de tokens de cada lote y los copia secuencialmente en el array memmap comenzando en `idx`. Rastrea el progreso con `tqdm`.
- **`flush()`**: Asegura que todos los datos se escriben en el disco.
- **¿Por qué binario/memmap?** Estos archivos son enormes pero se pueden transmitir. Durante el entrenamiento, puedes cargarlos con `np.memmap('train.bin', dtype=np.uint16, mode='r')` sin cargar todo en memoria.

#### 7. Comentarios sobre la Salida y el Uso
```python
    # train.bin is ~17GB, val.bin ~8.5MB
    # train has ~9B tokens (9,035,582,198)
    # val has ~4M tokens (4,434,897)

    # to read the bin files later, e.g. with numpy:
    # m = np.memmap('train.bin', dtype=np.uint16, mode='r')
```
- Estos son tamaños de ejemplo para el OpenWebText completo (su archivo local puede diferir).
- **Consejo de lectura**: Usa memmap para acceso de solo lectura. En los bucles de entrenamiento, puedes muestrear índices de inicio aleatorios y leer secuencias de longitud fija (por ejemplo, 1024 tokens) del array plano.

### Posibles Problemas y Notas
- **Uso de memoria**: Leer el `openwebtext.txt` completo en la RAM podría fallar para archivos muy grandes (40GB+). Considere lecturas en streaming si es necesario.
- **Colocación de EOT**: El comentario cuestiona añadir vs. anteponer EOT; en la práctica, añadir funciona para modelos autoregresivos (marca el final después del contenido).
- **Personalización**: Asume un archivo local; el código de inspiración descarga desde Hugging Face, pero esta versión lee localmente (más rápido, sin necesidad de autenticación).
- **Dependencias**: Requiere `tiktoken`, `datasets`, `numpy`, `tqdm`. Instalar via pip si faltan.
- **Escalabilidad**: Para el OpenWebText real, ejecutar en una máquina con 64GB+ de RAM y almacenamiento rápido (SSD). La división de 10k ejemplos sugiere que esto podría ser para un subconjunto.

Este script convierte texto crudo en un formato listo para el entrenamiento, optimizado para modelos de lenguaje como GPT. Si tienes preguntas sobre cómo modificarlo (por ejemplo, tokenizador diferente o tamaño de fragmento), ¡avísame
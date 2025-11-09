---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Entrenamiento de Conjuntos de Datos Personalizados con nanoGPT
translated: true
type: note
---

### Preparación y entrenamiento de un dataset de texto personalizado con nanoGPT

nanoGPT está diseñado para un entrenamiento sencillo con datos de texto, incluyendo datasets personalizados. El proceso implica preparar tu texto en archivos binarios de tokens, configurar los parámetros de entrenamiento y ejecutar el script de entrenamiento. A continuación, describiré los pasos basados en los ejemplos del repositorio (por ejemplo, Shakespeare u OpenWebText). Necesitarás Python 3.8+ y una GPU para un entrenamiento eficiente (la CPU funciona pero es más lenta).

#### 1. Instalar Dependencias
Primero, configura el entorno:
```
pip install torch numpy transformers datasets tiktoken wandb tqdm
```
- `torch`: Para PyTorch (instalar con CUDA si usas GPU: ej., `pip install torch --index-url https://download.pytorch.org/whl/cu118`).
- Los demás manejan tokenización, carga de datos y registro.

#### 2. Preparar tu Dataset Personalizado
nanoGPT espera tus datos como archivos binarios (`train.bin` y `val.bin`) que contengan enteros tokenizados. Necesitarás escribir un script de preparación simple para procesar tu texto en bruto.

- **Coloca tu Archivo de Texto**: Pon tu texto en bruto (ej., `input.txt`) en una nueva carpeta bajo `data/`, como `data/mi_dataset/`.
  
- **Crea un Script de Preparación**: Copia y adapta un ejemplo del repositorio (ej., `data/shakespeare_char/prepare.py` para nivel de carácter o `data/openwebtext/prepare.py` para nivel de token BPE de GPT-2).
  
  **Ejemplo para Tokenización a Nivel de Carácter** (simple para datasets pequeños; trata cada carácter como un token):
  ```python
  # Guardar como data/mi_dataset/prepare.py
  import os
  import requests
  import numpy as np
  from torch.utils.data import Dataset, random_split

  # Carga tu texto (reemplaza con la ruta de tu archivo)
  with open('data/mi_dataset/input.txt', 'r', encoding='utf-8') as f:
      text = f.read()

  # Codifica como caracteres
  chars = sorted(list(set(text)))
  vocab_size = len(chars)
  stoi = {ch: i for i, ch in enumerate(chars)}
  itos = {i: ch for i, ch in enumerate(chars)}
  def encode(s): return [stoi[c] for c in s]
  def decode(l): return ''.join([itos[i] for i in l])

  # Tokeniza todo el texto
  data = torch.tensor(encode(text), dtype=torch.long)

  # Divide en entrenamiento/validación (90/10)
  n = int(0.9 * len(data))
  train_data = data[:n]
  val_data = data[n:]

  # Guarda como archivos .bin
  train_data = train_data.numpy()
  val_data = val_data.numpy()
  train_data.tofile('data/mi_dataset/train.bin')
  val_data.tofile('data/mi_dataset/val.bin')

  # Imprime estadísticas
  print(f"Longitud del dataset en caracteres: {len(data)}")
  print(f"Tamaño del vocabulario: {vocab_size}")
  ```
  Ejecútalo:
  ```
  python data/mi_dataset/prepare.py
  ```
  Esto crea `train.bin` y `val.bin`.

- **Para Tokenización BPE de GPT-2** (mejor para datasets más grandes; usa subpalabras):
  Adapta `data/openwebtext/prepare.py`. Necesitarás instalar `tiktoken` (ya está en las dependencias) y manejar tu texto de manera similar, pero usando `tiktoken.get_encoding("gpt2").encode()` en lugar de la codificación de caracteres. Divide tu texto en fragmentos de entrenamiento/validación (ej., 90/10), luego guárdalos como arrays de NumPy en `.bin`.

- **Consejos**:
  - Mantén tu dataset limpio (ej., elimina caracteres especiales si es necesario).
  - Para archivos muy grandes, procésalos en fragmentos para evitar problemas de memoria.
  - Tamaño del vocabulario: ~65 para caracteres (Shakespeare); ~50k para BPE.

#### 3. Configurar el Entrenamiento
Crea un archivo de configuración copiando un ejemplo (ej., `config/train_shakespeare_char.py`) a `config/train_mi_dataset.py` y edítalo.

Parámetros clave a ajustar:
```python
# Ejemplo de fragmento de configuración
out_dir = 'out-mi_dataset'  # Carpeta de salida para checkpoints
dataset = 'mi_dataset'      # Coincide con el nombre de tu carpeta de datos
batch_size = 64             # Ajusta según la memoria de la GPU (ej., 12 para GPU pequeña)
block_size = 256            # Longitud de contexto (tokens por ejemplo)
n_layer = 6                 # Capas del Transformer
n_head = 6                  # Cabezas de atención
n_embd = 384                # Dimensión de embedding
max_iters = 5000            # Pasos de entrenamiento
lr = 6e-4                   # Tasa de aprendizaje
dropout = 0.2               # Tasa de dropout
init_from = 'scratch'       # 'scratch' para modelo nuevo; 'gpt2' para cargar uno preentrenado
```
- Para ajuste fino (empezar desde GPT-2 preentrenado): Establece `init_from = 'gpt2'` (o 'gpt2-medium').
- Para Apple Silicon: Añade `device = 'mps'`.
- Guarda checkpoints cada 500 iteraciones por defecto.

#### 4. Ejecutar el Entrenamiento
Entrena desde cero o haz ajuste fino:
```
python train.py config/train_mi_dataset.py
```
- Para multi-GPU (ej., 8 GPUs): `torchrun --standalone --nproc_per_node=8 train.py config/train_mi_dataset.py`.
- Monitoriza con WandB (registra pérdidas, muestras; habilita en la configuración con `wandb_log = True`).
- Tiempo de entrenamiento: Minutos para modelos pequeños en GPU; horas/días para modelos más grandes.

#### 5. Generar Muestras (Probar el Modelo)
Después del entrenamiento, genera texto de muestra:
```
python sample.py --out_dir=out-mi_dataset --start="Tu prompt aquí"
```
Esto carga el último checkpoint y genera.

#### Problemas Comunes
- **Errores de Memoria**: Reduce `batch_size` o `block_size`.
- **Sin GPU**: Añade `--device=cpu --compile=False` a los comandos.
- **Datasets Grandes**: Usa entrenamiento distribuido para escalar.

Para más detalles, consulta el README del repositorio y los ejemplos de datos/config.

[nanoGPT GitHub](https://github.com/karpathy/nanoGPT)
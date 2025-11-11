---
audio: false
generated: true
lang: es
layout: post
title: Corrección del Error de Carga de Modelos en llama.cpp
translated: true
type: note
---

Según el error `gguf_init_from_file_impl: failed to read key-value pairs`, tu archivo de modelo está **corrupto**, **incompleto** o es **incompatible** con tu versión de llama.cpp. Aquí te explicamos cómo solucionarlo:

### 1. **Verificar y volver a descargar el modelo**
   ```bash
   # Verificar el tamaño actual del archivo (la cuantización Q6_K debería ser ~6.1GB para el modelo de 8B):
   ls -lh /home/lzw/Projects/llama.cpp/models/DeepSeek-R1-0528-Qwen3-8B-UD-Q6_K_XL.gguf

   # Salida esperada:
   # -rw-r--r-- 1 lzw lzw 6.1G Jun  2 10:00 ...Q6_K_XL.gguf
   ```
   - Si el tamaño es < 6GB, **vuelve a descargar el modelo**:
     ```bash
     rm /home/lzw/Projects/llama.cpp/models/DeepSeek-R1-0528-Qwen3-8B-UD-Q6_K_XL.gguf
     # Vuelve a descargar desde la fuente original (por ejemplo, HuggingFace)
     ```

### 2. **Actualizar llama.cpp**
Tu compilación (commit `7675c555`) podría estar desactualizada:
```bash
cd ~/Projects/llama.cpp
git pull origin master          # Actualizar el código
rm -rf build && mkdir build     # Limpiar y crear directorio de compilación
cd build
cmake .. -DLLAMA_CUBLAS=ON      # Habilitar CUDA
make -j                         # Recompilar
```

### 3. **Validar la integridad del modelo**
Prueba el modelo con una inferencia simple:
```bash
~/Projects/llama.cpp/build/bin/main \
  -m /home/lzw/Projects/llama.cpp/models/DeepSeek-R1-0528-Qwen3-8B-UD-Q6_K_XL.gguf \
  -p "Hello" -n 10
```
- Si esto falla, el archivo del modelo está definitivamente corrupto.

### 4. **Probar con un modelo diferente (Prueba de sanidad)**
Prueba con un modelo que sepas que funciona (por ejemplo, [TinyLlama](https://huggingface.co/TheBloke/TinyLlama-1.1B-1T-OpenOrca-GGUF)):
```bash
~/Projects/llama.cpp/build/bin/llama-server \
  -m /path/to/tinyllama.Q8_0.gguf \
  --port 8000
```
- Si esto funciona, tu archivo de modelo original es el problema.

### 5. **Reconvertir el modelo (Avanzado)**
Si volver a descargar falla:
1. Obtén el modelo original de Hugging Face:
   ```bash
   huggingface-cli download deepseek-ai/DeepSeek-R1-0528-Qwen3-8B --local-dir ./deepseek-original
   ```
2. Reconvierte a GGUF:
   ```bash
   python3 ~/Projects/llama.cpp/convert-hf-to-gguf.py \
     ./deepseek-original \
     --outtype q6_k  # Coincide con tu cuantización
   ```

### Resumen de soluciones comunes:

| Problema | Solución |
|-------|----------|
| **Descarga corrupta** | Volver a descargar el modelo |
| **llama.cpp desactualizado** | `git pull` + recompilar |
| **GGUF incompatible** | Usar la última versión de `convert-hf-to-gguf.py` |
| **Permisos de archivo** | `chmod +r /path/to/model.gguf` |

> 💡 **Nota:** El modelo DeepSeek-R1 es nuevo (publicado el 28 de mayo de 2024). Asegúrate de que tu llama.cpp esté **actualizado en la última semana** para garantizar la compatibilidad.

Comienza por volver a descargar el modelo y actualizar llama.cpp: esto resuelve el 90% de estos problemas. ¡Avísame si necesitas más ayuda
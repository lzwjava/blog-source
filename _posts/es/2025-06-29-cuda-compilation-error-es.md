---
audio: false
generated: true
lang: es
layout: post
title: Corrección de Error de Compilación de CUDA con nvcc
translated: true
type: note
---

El error indica que el toolkit de CUDA no está instalado o configurado correctamente, ya que el compilador no puede encontrar `cuda.h`. Además, tu código es un archivo fuente de CUDA (`.cu`) pero estás intentando compilarlo con `gcc`, que no es adecuado para código CUDA. Necesitas usar `nvcc`, el compilador de NVIDIA CUDA. Aquí se explica cómo solucionar el problema:

### Pasos para Solucionarlo

1. **Instalar el CUDA Toolkit**:
   - Asegúrate de que el NVIDIA CUDA Toolkit esté instalado en tu sistema. Puedes descargarlo desde el [sitio web de NVIDIA CUDA Toolkit](https://developer.nvidia.com/cuda-downloads).
   - Sigue las instrucciones de instalación para tu sistema operativo (Linux en este caso, basado en el prompt).
   - Después de la instalación, verifícala ejecutando:
     ```bash
     nvcc --version
     ```
     Esto debería mostrar la versión de CUDA si está instalada correctamente.

2. **Usar `nvcc` para Compilar**:
   - Dado que tu archivo es un archivo fuente de CUDA (`.cu`), compílalo con `nvcc` en lugar de `gcc`. Reemplaza:
     ```bash
     gcc scripts/benchmark/cudamark.c
     ```
     con:
     ```bash
     nvcc scripts/benchmark/cudamark.cu
     ```
   - Nota: Asegúrate de que la extensión del archivo coincida con tu archivo real (`.cu` en el código que proporcionaste, no `.c` como en el error).

3. **Configurar el Entorno de CUDA**:
   - Asegúrate de que las rutas del toolkit de CUDA estén incluidas en tu entorno. Añade lo siguiente a tu archivo `~/.bashrc` o al archivo de configuración del shell equivalente:
     ```bash
     export PATH=/usr/local/cuda/bin:$PATH
     export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
     ```
     Luego, ejecuta `source` en el archivo:
     ```bash
     source ~/.bashrc
     ```

4. **Enlazar la Librería Thrust**:
   - Tu código usa Thrust, que es parte del toolkit de CUDA, por lo que no es necesario enlazar librerías adicionales explícitamente. Sin embargo, asegúrate de tener una versión compatible de CUDA (Thrust está incluido en CUDA 7.0 y versiones posteriores).

5. **Corregir Problemas en el Código**:
   - El código hace referencia a `thread_counts` pero no lo usa en la función `benchmark`. La función `parallel_sort_gpu` usa Thrust, que gestiona el paralelismo internamente, por lo que el bucle `thread_counts` en `main` es engañoso. Si tu intención era evaluar diferentes configuraciones de hilos, la función sort de Thrust no permite el control directo del número de hilos. Podrías aclarar esta lógica o eliminar el `thread_counts` no utilizado.
   - Para mayor claridad, podrías modificar el código para evaluar el mismo tamaño de lista múltiples veces y promediar las variaciones de tiempo:

     ```cuda
     #include <stdio.h>
     #include <stdlib.h>
     #include <cuda.h>
     #include <thrust/device_vector.h>
     #include <thrust/sort.h>
     #include <time.h>

     void parallel_sort_gpu(int *arr, int n) {
         thrust::device_vector<int> d_vec(arr, arr + n);
         thrust::sort(d_vec.begin(), d_vec.end());
         thrust::copy(d_vec.begin(), d_vec.end(), arr);
     }

     double benchmark(int list_size) {
         int *arr = (int*)malloc(list_size * sizeof(int));
         for (int i = 0; i < list_size; ++i) {
             arr[i] = rand() % 1000001;
         }

         clock_t start = clock();
         parallel_sort_gpu(arr, list_size);
         clock_t end = clock();

         free(arr);
         return (double)(end - start) / CLOCKS_PER_SEC;
     }

     int main() {
         int list_size = 50000000;
         int num_runs = 8; // Número de ejecuciones para promediar

         printf("Run,TimeTakenSeconds\n");
         for (int i = 0; i < num_runs; ++i) {
             double t = benchmark(list_size);
             printf("%d,%.6f\n", i + 1, t);
         }
         return 0;
     }
     ```

6. **Compilar el Código Actualizado**:
   - Guarda el código como `cudamark.cu` y compílalo:
     ```bash
     nvcc -o cudamark scripts/benchmark/cudamark.cu
     ```
   - Si encuentras errores del enlazador, asegúrate de que las librerías de CUDA sean accesibles (ver paso 3).

7. **Ejecutar el Programa**:
   - Ejecuta el binario compilado:
     ```bash
     ./cudamark
     ```

8. **Notas Adicionales**:
   - **Extensión del Archivo**: Asegúrate de que el archivo tenga la extensión `.cu`, ya que los archivos CUDA requieren esto para que `nvcc` los procese correctamente.
   - **Disponibilidad de la GPU**: Asegúrate de tener una GPU compatible con CUDA y los controladores correctos instalados. Verifica con:
     ```bash
     nvidia-smi
     ```
   - **Thrust y Versión de CUDA**: Verifica que tu versión de CUDA sea compatible con Thrust. Se recomienda CUDA 11.x o posterior para las características modernas de Thrust.
   - **Precisión de la Medición de Tiempo**: La función `clock()` mide el tiempo de CPU, no el tiempo de ejecución de la GPU. Para una medición más precisa del tiempo de la GPU, considera usar eventos de CUDA:
     ```cuda
     cudaEvent_t start, stop;
     cudaEventCreate(&start);
     cudaEventCreate(&stop);
     cudaEventRecord(start);
     parallel_sort_gpu(arr, list_size);
     cudaEventRecord(stop);
     cudaEventSynchronize(stop);
     float milliseconds = 0;
     cudaEventElapsedTime(&milliseconds, start, stop);
     return milliseconds / 1000.0; // Convertir a segundos
     ```

9. **Si los Errores Persisten**:
   - Si `cuda.h` aún no se encuentra, verifica la ruta de instalación del toolkit de CUDA (por ejemplo, `/usr/local/cuda/include`). Es posible que necesites especificar la ruta de inclusión explícitamente:
     ```bash
     nvcc -I/usr/local/cuda/include -o cudamark scripts/benchmark/cudamark.cu
     ```
   - Asegúrate de que la ruta del archivo `scripts/benchmark/cudamark.cu` sea correcta en relación con tu directorio actual.

### Comando de Compilación Actualizado
```bash
nvcc -o cudamark scripts/benchmark/cudamark.cu
```

### Salida Esperada
Después de solucionar los problemas, ejecutar `./cudamark` debería producir una salida similar a:
```
Run,TimeTakenSeconds
1,0.123456
2,0.124567
...
```

Si necesitas más ayuda o encuentras errores específicos, ¡por favor compártelos!
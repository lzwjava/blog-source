---
audio: false
generated: true
lang: es
layout: post
title: API del Controlador CUDA
translated: true
type: note
---

El encabezado `<cuda.h>` es parte de la **API de Controlador CUDA**, una API de nivel más bajo en comparación con la API de Runtime de CUDA de nivel superior (por ejemplo, `cudaMalloc`, `cudaMemcpy`). La API de Controlador proporciona un control más detallado sobre los recursos de la GPU (por ejemplo, contextos, módulos, streams) y se utiliza a menudo en escenarios avanzados como programación multi-GPU, carga dinámica de kernels u optimizaciones de bajo nivel.

### Funciones Comunes de la API de Controlador CUDA
Aquí hay algunas funciones clave y sus propósitos:

| Función                                      | Descripción                                                                                   |
|----------------------------------------------|-----------------------------------------------------------------------------------------------|
| **`cuInit(unsigned int flags)`**             | Inicializa el controlador CUDA. Debe llamarse antes que cualquier otra función de la API de Controlador. |
| **`cuDeviceGet(CUdevice *dev, int ordinal)`** | Obtiene un manejador para el dispositivo GPU con el ordinal especificado (por ejemplo, `0` para la primera GPU). |
| **`cuCtxCreate(CUcontext *ctx, unsigned int flags, CUdevice dev)`** | Crea un contexto CUDA en el dispositivo especificado.                                        |
| **`cuModuleLoad(CUmodule *mod, const char *fname)`** | Carga un archivo PTX o cubin en el contexto actual como un módulo.                           |
| **`cuModuleGetFunction(CUfunction *func, CUmodule mod, const char *name)`** | Recupera una función kernel de un módulo cargado.                                            |
| **`cuMemAlloc(CUdeviceptr *dptr, size_t bytesize)`** | Asigna memoria en la GPU.                                                                    |
| **`cuMemcpyHtoD(CUdeviceptr dst, const void *src, size_t bytes)`** | Copia datos desde el host (CPU) al dispositivo (GPU).                                        |
| **`cuMemcpyDtoH(void *dst, CUdeviceptr src, size_t bytes)`** | Copia datos desde el dispositivo (GPU) al host (CPU).                                        |
| **`cuLaunchKernel(CUfunction f, ...)`**      | Lanza una función kernel con las dimensiones de grid/block y los parámetros especificados.    |

---

### Flujo de Trabajo de Ejemplo
A continuación se muestra un ejemplo simplificado que utiliza la API de Controlador CUDA para:
1. Inicializar el controlador.
2. Asignar memoria en la GPU.
3. Copiar datos hacia/desde la GPU.
4. Cargar un kernel desde un archivo PTX y ejecutarlo.

```cpp
#include <cuda.h>
#include <stdio.h>

int main() {
    CUdevice dev;
    CUcontext ctx;
    CUmodule mod;
    CUfunction kernel;
    CUresult err;

    // 1. Inicializar el controlador CUDA
    cuInit(0);

    // 2. Obtener un manejador para el dispositivo 0 (primera GPU)
    cuDeviceGet(&dev, 0);

    // 3. Crear un contexto en el dispositivo
    cuCtxCreate(&ctx, 0, dev);

    // 4. Cargar un módulo PTX (por ejemplo, generado desde un archivo .cu)
    cuModuleLoad(&mod, "my_kernel.ptx");

    // 5. Obtener la función kernel del módulo
    cuModuleGetFunction(&kernel, mod, "my_kernel");

    // 6. Asignar memoria en la GPU
    size_t N = 1024;
    CUdeviceptr d_data;
    cuMemAlloc(&d_data, N * sizeof(float));

    // 7. Copiar datos del host al dispositivo
    float h_data[N] = {1.0f};
    cuMemcpyHtoD(d_data, h_data, N * sizeof(float));

    // 8. Configurar los parámetros del kernel
    void *args[] = { &d_data, &N };
    int blockSize = 256;
    int gridSize = (N + blockSize - 1) / blockSize;

    // 9. Lanzar el kernel
    cuLaunchKernel(
        kernel,
        gridSize, 1, 1,    // Dimensiones del grid
        blockSize, 1, 1,   // Dimensiones del bloque
        0, NULL,           // Memoria compartida y stream
        args, NULL         // Argumentos del kernel
    );

    // 10. Copiar los resultados de vuelta al host
    cuMemcpyDtoH(h_data, d_data, N * sizeof(float));

    // 11. Limpieza
    cuMemFree(d_data);
    cuModuleUnload(mod);
    cuCtxDestroy(ctx);

    return 0;
}
```

---

### Notas Clave
1. **Manejo de Errores**: Verifique siempre el valor de retorno (por ejemplo, `CUresult err = cuSomeFunction(...);`). Use `cuGetErrorString(err)` para decodificar los errores.
2. **Parámetros del Kernel**: Para `cuLaunchKernel`, los parámetros se pasan como un array de punteros a los argumentos. Asegúrese de que el orden coincida con los parámetros esperados por el kernel.
3. **Archivos PTX**: Los kernels deben compilarse a PTX (por ejemplo, `nvcc --ptx my_kernel.cu -o my_kernel.ptx`).
4. **Gestión de Contextos**: Los contextos son análogos a los procesos de la CPU—gestionan los recursos para una GPU. Use `cuCtxPushCurrent`/`cuCtxPopCurrent` para código multi-hilo.

---

### ¿Cuándo Usar la API de Controlador?
- **Carga Dinámica de Kernels**: Cargar PTX en tiempo de ejecución.
- **Control Multi-GPU**: Gestionar explícitamente múltiples GPUs.
- **Optimizaciones de Bajo Nivel**: Control detallado sobre contextos, streams o memoria.

Para la mayoría de las aplicaciones, la **API de Runtime** de nivel superior (por ejemplo, `cudaMalloc`, `cudaMemcpy`) es suficiente y más simple. Use la API de Controlador cuando necesite sus funciones avanzadas.
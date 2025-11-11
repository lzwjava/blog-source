---
audio: false
generated: true
lang: es
layout: post
title: Ejemplo Básico de CUDA
translated: true
type: note
---

Aquí tienes un ejemplo básico de CUDA que demuestra programación de GPU a bajo nivel usando CUDA C. Este ejemplo realiza una suma de vectores simple en la GPU usando las construcciones más fundamentales de CUDA:

```c
#include <stdio.h>
#include <cuda.h>

// Kernel de CUDA para suma de vectores
__global__ void vectorAdd(float *a, float *b, float *c, int n) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n) {
        c[i] = a[i] + b[i];
    }
}

int main() {
    int n = 1024;  // tamaño del vector
    size_t size = n * sizeof(float);
    
    // Asignación de memoria en el host
    float *h_a = (float*)malloc(size);
    float *h_b = (float*)malloc(size);
    float *h_c = (float*)malloc(size);

    // Inicializar arrays en el host
    for(int i = 0; i < n; i++) {
        h_a[i] = i;
        h_b[i] = i * 2;
    }

    // Punteros de memoria del dispositivo
    float *d_a, *d_b, *d_c;
    
    // Asignar memoria del dispositivo
    cudaMalloc((void**)&d_a, size);
    cudaMalloc((void**)&d_b, size);
    cudaMalloc((void**)&d_c, size);

    // Copiar datos del host al dispositivo
    cudaMemcpy(d_a, h_a, size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_b, h_b, size, cudaMemcpyHostToDevice);

    // Configurar parámetros de lanzamiento del kernel
    int threadsPerBlock = 256;
    int blocksPerGrid = (n + threadsPerBlock - 1) / threadsPerBlock;

    // Lanzar kernel
    vectorAdd<<<blocksPerGrid, threadsPerBlock>>>(d_a, d_b, d_c, n);

    // Esperar a que la GPU termine
    cudaDeviceSynchronize();

    // Copiar resultado de vuelta al host
    cudaMemcpy(h_c, d_c, size, cudaMemcpyDeviceToHost);

    // Verificar resultados
    for(int i = 0; i < 10; i++) {
        printf("%f + %f = %f\n", h_a[i], h_b[i], h_c[i]);
    }

    // Liberar memoria del dispositivo
    cudaFree(d_a);
    cudaFree(d_b);
    cudaFree(d_c);

    // Liberar memoria del host
    free(h_a);
    free(h_b);
    free(h_c);

    // Reiniciar dispositivo
    cudaDeviceReset();

    return 0;
}
```

Para compilar y ejecutar este código, necesitarás:
1. GPU NVIDIA con soporte CUDA
2. CUDA Toolkit instalado
3. Compilar con: `nvcc vector_add.cu -o vector_add`

Este ejemplo demuestra las operaciones más fundamentales de CUDA:
- Definición de kernel `__global__`
- Asignación manual de memoria con `cudaMalloc`
- Transferencias explícitas de memoria con `cudaMemcpy`
- Configuración de lanzamiento de kernel con `<<<bloques, hilos>>>`
- Sincronización del dispositivo
- Limpieza de memoria

Aspectos clave de bajo nivel:
1. Gestión directa de memoria sin usar ayudas del runtime de CUDA
2. Configuración manual de hilos/bloques
3. Sincronización explícita del dispositivo
4. Operaciones con punteros crudos
5. Sin abstracciones de alto nivel o librerías

El kernel usa la jerarquía básica de hilos de CUDA:
- `blockIdx.x`: Índice del bloque
- `blockDim.x`: Hilos por bloque
- `threadIdx.x`: Índice del hilo dentro del bloque

Esto calcula un ID único de hilo para cada elemento y realiza la suma solo si está dentro de los límites. El ejemplo lo mantiene simple pero muestra los conceptos centrales de programación CUDA a un nivel bajo.

La salida mostrará los primeros 10 resultados, como:
```
0.000000 + 0.000000 = 0.000000
1.000000 + 2.000000 = 3.000000
2.000000 + 4.000000 = 6.000000
...
```
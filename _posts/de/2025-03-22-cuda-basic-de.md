---
audio: false
generated: true
lang: de
layout: post
title: Grundlegendes CUDA-Beispiel
translated: true
type: note
---

Hier ist ein grundlegendes CUDA-Beispiel, das die Low-Level-GPU-Programmierung mit CUDA C demonstriert. Dieses Beispiel führt eine einfache Vektoraddition auf der GPU unter Verwendung der grundlegendsten CUDA-Konstrukte durch:

```c
#include <stdio.h>
#include <cuda.h>

// CUDA-Kernel für Vektoraddition
__global__ void vectorAdd(float *a, float *b, float *c, int n) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n) {
        c[i] = a[i] + b[i];
    }
}

int main() {
    int n = 1024;  // Vektorgröße
    size_t size = n * sizeof(float);
    
    // Host-Speicherzuweisung
    float *h_a = (float*)malloc(size);
    float *h_b = (float*)malloc(size);
    float *h_c = (float*)malloc(size);

    // Host-Arrays initialisieren
    for(int i = 0; i < n; i++) {
        h_a[i] = i;
        h_b[i] = i * 2;
    }

    // Device-Speicherzeiger
    float *d_a, *d_b, *d_c;
    
    // Device-Speicher zuweisen
    cudaMalloc((void**)&d_a, size);
    cudaMalloc((void**)&d_b, size);
    cudaMalloc((void**)&d_c, size);

    // Daten vom Host zum Device kopieren
    cudaMemcpy(d_a, h_a, size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_b, h_b, size, cudaMemcpyHostToDevice);

    // Kernel-Startparameter konfigurieren
    int threadsPerBlock = 256;
    int blocksPerGrid = (n + threadsPerBlock - 1) / threadsPerBlock;

    // Kernel starten
    vectorAdd<<<blocksPerGrid, threadsPerBlock>>>(d_a, d_b, d_c, n);

    // Auf GPU-Ende warten
    cudaDeviceSynchronize();

    // Ergebnis zurück zum Host kopieren
    cudaMemcpy(h_c, d_c, size, cudaMemcpyDeviceToHost);

    // Ergebnisse überprüfen
    for(int i = 0; i < 10; i++) {
        printf("%f + %f = %f\n", h_a[i], h_b[i], h_c[i]);
    }

    // Device-Speicher freigeben
    cudaFree(d_a);
    cudaFree(d_b);
    cudaFree(d_c);

    // Host-Speicher freigeben
    free(h_a);
    free(h_b);
    free(h_c);

    // Device zurücksetzen
    cudaDeviceReset();

    return 0;
}
```

Um diesen Code zu kompilieren und auszuführen, benötigen Sie:
1. NVIDIA-GPU mit CUDA-Unterstützung
2. Installiertes CUDA Toolkit
3. Kompilieren mit: `nvcc vector_add.cu -o vector_add`

Dieses Beispiel demonstriert die grundlegendsten CUDA-Operationen:
- `__global__` Kernel-Definition
- Manuelle Speicherzuweisung mit `cudaMalloc`
- Explizite Speicherübertragungen mit `cudaMemcpy`
- Kernel-Startkonfiguration mit `<<<Blöcke, Threads>>>`
- Device-Synchronisation
- Speicherbereinigung

Wichtige Low-Level-Aspekte:
1. Direkte Speicherverwaltung ohne CUDA Runtime-Helfer
2. Manuelle Thread/Block-Konfiguration
3. Explizite Device-Synchronisation
4. Rohe Pointer-Operationen
5. Keine High-Level-Abstraktionen oder Bibliotheken

Der Kernel verwendet die grundlegende CUDA-Thread-Hierarchie:
- `blockIdx.x`: Block-Index
- `blockDim.x`: Threads pro Block
- `threadIdx.x`: Thread-Index innerhalb des Blocks

Dies berechnet eine eindeutige Thread-ID für jedes Element und führt die Addition nur durch, wenn sie innerhalb der Grenzen liegt. Das Beispiel hält es einfach, zeigt aber die Kernkonzepte der CUDA-Programmierung auf niedrigem Niveau.

Die Ausgabe zeigt die ersten 10 Ergebnisse, wie:
```
0.000000 + 0.000000 = 0.000000
1.000000 + 2.000000 = 3.000000
2.000000 + 4.000000 = 6.000000
...
```
---
audio: false
generated: true
lang: de
layout: post
title: CUDA-Treiber-API
translated: true
type: note
---

Die `<cuda.h>`-Header-Datei ist Teil der **CUDA Driver API**, einer Low-Level-API im Vergleich zur höher angesiedelten CUDA Runtime API (z.B. `cudaMalloc`, `cudaMemcpy`). Die Driver API bietet eine feinere Kontrolle über GPU-Ressourcen (z.B. Kontexte, Module, Streams) und wird häufig in fortgeschrittenen Szenarien wie Multi-GPU-Programmierung, dynamischem Kernel-Laden oder Low-Level-Optimierungen verwendet.

### Häufige CUDA Driver API Funktionen
Hier sind einige wichtige Funktionen und ihre Zwecke:

| Funktion                         | Beschreibung                                                                                   |
|----------------------------------|------------------------------------------------------------------------------------------------|
| **`cuInit(unsigned int flags)`** | Initialisiert den CUDA-Treiber. Muss vor jeder anderen Driver API-Funktion aufgerufen werden.  |
| **`cuDeviceGet(CUdevice *dev, int ordinal)`** | Ruft einen Handle zur GPU mit dem angegebenen Index ab (z.B. `0` für die erste GPU).          |
| **`cuCtxCreate(CUcontext *ctx, unsigned int flags, CUdevice dev)`** | Erstellt einen CUDA-Kontext auf dem angegebenen Gerät.                                        |
| **`cuModuleLoad(CUmodule *mod, const char *fname)`** | Lädt eine PTX- oder Cubin-Datei in den aktuellen Kontext als Modul.                           |
| **`cuModuleGetFunction(CUfunction *func, CUmodule mod, const char *name)`** | Ruft eine Kernel-Funktion aus einem geladenen Modul ab.                                        |
| **`cuMemAlloc(CUdeviceptr *dptr, size_t bytesize)`** | Reserviert Speicher auf der GPU.                                                               |
| **`cuMemcpyHtoD(CUdeviceptr dst, const void *src, size_t bytes)`** | Kopiert Daten vom Host (CPU) zum Device (GPU).                                                 |
| **`cuMemcpyDtoH(void *dst, CUdeviceptr src, size_t bytes)`** | Kopiert Daten vom Device (GPU) zum Host (CPU).                                                 |
| **`cuLaunchKernel(CUfunction f, ...)`** | Startet eine Kernel-Funktion mit angegebenen Grid-/Block-Dimensionen und Parametern.           |

---

### Beispielhafter Ablauf
Unten ist ein vereinfachtes Beispiel, das die CUDA Driver API verwendet, um:
1. Den Treiber zu initialisieren.
2. GPU-Speicher zu reservieren.
3. Daten zur/von der GPU zu kopieren.
4. Einen Kernel aus einer PTX-Datei zu laden und auszuführen.

```cpp
#include <cuda.h>
#include <stdio.h>

int main() {
    CUdevice dev;
    CUcontext ctx;
    CUmodule mod;
    CUfunction kernel;
    CUresult err;

    // 1. Initialisiere den CUDA-Treiber
    cuInit(0);

    // 2. Hole Handle zu Gerät 0 (erste GPU)
    cuDeviceGet(&dev, 0);

    // 3. Erstelle einen Kontext auf dem Gerät
    cuCtxCreate(&ctx, 0, dev);

    // 4. Lade ein PTX-Modul (z.B. generiert aus einer .cu-Datei)
    cuModuleLoad(&mod, "my_kernel.ptx");

    // 5. Hole die Kernel-Funktion aus dem Modul
    cuModuleGetFunction(&kernel, mod, "my_kernel");

    // 6. Reserviere GPU-Speicher
    size_t N = 1024;
    CUdeviceptr d_data;
    cuMemAlloc(&d_data, N * sizeof(float));

    // 7. Kopiere Daten vom Host zum Device
    float h_data[N] = {1.0f};
    cuMemcpyHtoD(d_data, h_data, N * sizeof(float));

    // 8. Konfiguriere Kernel-Parameter
    void *args[] = { &d_data, &N };
    int blockSize = 256;
    int gridSize = (N + blockSize - 1) / blockSize;

    // 9. Starte den Kernel
    cuLaunchKernel(
        kernel,
        gridSize, 1, 1,    // Grid-Dimensionen
        blockSize, 1, 1,   // Block-Dimensionen
        0, NULL,           // Shared Memory und Stream
        args, NULL         // Kernel-Argumente
    );

    // 10. Kopiere Ergebnisse zurück zum Host
    cuMemcpyDtoH(h_data, d_data, N * sizeof(float));

    // 11. Aufräumen
    cuMemFree(d_data);
    cuModuleUnload(mod);
    cuCtxDestroy(ctx);

    return 0;
}
```

---

### Wichtige Hinweise
1.  **Fehlerbehandlung**: Überprüfe immer den Rückgabewert (z.B. `CUresult err = cuSomeFunction(...);`). Verwende `cuGetErrorString(err)`, um Fehler zu decodieren.
2.  **Kernel-Parameter**: Für `cuLaunchKernel` werden Parameter als ein Array von Zeigern auf die Argumente übergeben. Stelle sicher, dass die Reihenfolge den erwarteten Parametern des Kernels entspricht.
3.  **PTX-Dateien**: Kernel müssen zu PTX kompiliert werden (z.B. `nvcc --ptx my_kernel.cu -o my_kernel.ptx`).
4.  **Kontextverwaltung**: Kontexte sind analog zu CPU-Prozessen – sie verwalten Ressourcen für eine GPU. Verwende `cuCtxPushCurrent`/`cuCtxPopCurrent` für Multi-Threaded-Code.

---

### Wann sollte die Driver API verwendet werden?
-   **Dynamisches Kernel-Laden**: Laden von PTX zur Laufzeit.
-   **Multi-GPU-Steuerung**: Explizites Verwalten mehrerer GPUs.
-   **Low-Level-Optimierungen**: Feingranulare Kontrolle über Kontexte, Streams oder Speicher.

Für die meisten Anwendungen ist die höher angesiedelte **Runtime API** (z.B. `cudaMalloc`, `cudaMemcpy`) ausreichend und einfacher. Verwende die Driver API, wenn du ihre erweiterten Funktionen benötigst.
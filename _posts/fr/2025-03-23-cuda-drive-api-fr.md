---
audio: false
generated: true
lang: fr
layout: post
title: API de Pilote CUDA
translated: true
type: note
---

L'en-tête `<cuda.h>` fait partie de **l'API Driver CUDA**, une API de plus bas niveau comparée à l'API Runtime CUDA de plus haut niveau (par exemple, `cudaMalloc`, `cudaMemcpy`). L'API Driver offre un contrôle plus fin sur les ressources GPU (par exemple, les contextes, modules, streams) et est souvent utilisée dans des scénarios avancés comme la programmation multi-GPU, le chargement dynamique de kernels, ou les optimisations de bas niveau.

### Fonctions courantes de l'API Driver CUDA
Voici quelques fonctions clés et leurs objectifs :

| Fonction                                      | Description                                                                                    |
|-----------------------------------------------|------------------------------------------------------------------------------------------------|
| **`cuInit(unsigned int flags)`**              | Initialise le pilote CUDA. Doit être appelée avant toute autre fonction de l'API Driver.        |
| **`cuDeviceGet(CUdevice *dev, int ordinal)`** | Obtient un handle vers le périphérique GPU avec l'ordinal spécifié (par exemple, `0` pour le premier GPU). |
| **`cuCtxCreate(CUcontext *ctx, unsigned int flags, CUdevice dev)`** | Crée un contexte CUDA sur le périphérique spécifié.                                           |
| **`cuModuleLoad(CUmodule *mod, const char *fname)`** | Charge un fichier PTX ou cubin dans le contexte actuel en tant que module.                    |
| **`cuModuleGetFunction(CUfunction *func, CUmodule mod, const char *name)`** | Récupère une fonction kernel à partir d'un module chargé.                                     |
| **`cuMemAlloc(CUdeviceptr *dptr, size_t bytesize)`** | Alloue de la mémoire sur le GPU.                                                               |
| **`cuMemcpyHtoD(CUdeviceptr dst, const void *src, size_t bytes)`** | Copie les données de l'hôte (CPU) vers le device (GPU).                                        |
| **`cuMemcpyDtoH(void *dst, CUdeviceptr src, size_t bytes)`** | Copie les données du device (GPU) vers l'hôte (CPU).                                           |
| **`cuLaunchKernel(CUfunction f, ...)`**       | Lance une fonction kernel avec des dimensions de grille/bloc et des paramètres spécifiés.      |

---

### Flux de travail exemple
Voici un exemple simplifié utilisant l'API Driver CUDA pour :
1. Initialiser le pilote.
2. Allouer de la mémoire GPU.
3. Copier des données vers/depuis le GPU.
4. Charger un kernel à partir d'un fichier PTX et l'exécuter.

```cpp
#include <cuda.h>
#include <stdio.h>

int main() {
    CUdevice dev;
    CUcontext ctx;
    CUmodule mod;
    CUfunction kernel;
    CUresult err;

    // 1. Initialiser le pilote CUDA
    cuInit(0);

    // 2. Obtenir un handle vers le périphérique 0 (premier GPU)
    cuDeviceGet(&dev, 0);

    // 3. Créer un contexte sur le périphérique
    cuCtxCreate(&ctx, 0, dev);

    // 4. Charger un module PTX (par exemple, généré à partir d'un fichier .cu)
    cuModuleLoad(&mod, "my_kernel.ptx");

    // 5. Obtenir la fonction kernel à partir du module
    cuModuleGetFunction(&kernel, mod, "my_kernel");

    // 6. Allouer de la mémoire GPU
    size_t N = 1024;
    CUdeviceptr d_data;
    cuMemAlloc(&d_data, N * sizeof(float));

    // 7. Copier les données de l'hôte vers le device
    float h_data[N] = {1.0f};
    cuMemcpyHtoD(d_data, h_data, N * sizeof(float));

    // 8. Configurer les paramètres du kernel
    void *args[] = { &d_data, &N };
    int blockSize = 256;
    int gridSize = (N + blockSize - 1) / blockSize;

    // 9. Lancer le kernel
    cuLaunchKernel(
        kernel,
        gridSize, 1, 1,    // Dimensions de la grille
        blockSize, 1, 1,   // Dimensions du bloc
        0, NULL,           // Mémoire partagée et stream
        args, NULL         // Arguments du kernel
    );

    // 10. Copier les résultats vers l'hôte
    cuMemcpyDtoH(h_data, d_data, N * sizeof(float));

    // 11. Nettoyage
    cuMemFree(d_data);
    cuModuleUnload(mod);
    cuCtxDestroy(ctx);

    return 0;
}
```

---

### Notes importantes
1. **Gestion des erreurs** : Vérifiez toujours la valeur de retour (par exemple, `CUresult err = cuSomeFunction(...);`). Utilisez `cuGetErrorString(err)` pour décoder les erreurs.
2. **Paramètres du kernel** : Pour `cuLaunchKernel`, les paramètres sont passés sous forme de tableau de pointeurs vers les arguments. Assurez-vous que l'ordre correspond aux paramètres attendus par le kernel.
3. **Fichiers PTX** : Les kernels doivent être compilés en PTX (par exemple, `nvcc --ptx my_kernel.cu -o my_kernel.ptx`).
4. **Gestion du contexte** : Les contextes sont analogues aux processus CPU — ils gèrent les ressources pour un GPU. Utilisez `cuCtxPushCurrent`/`cuCtxPopCurrent` pour le code multi-threadé.

---

### Quand utiliser l'API Driver ?
- **Chargement dynamique de kernels** : Charger des PTX à l'exécution.
- **Contrôle multi-GPU** : Gérer explicitement plusieurs GPU.
- **Optimisations de bas niveau** : Contrôle fin des contextes, streams ou de la mémoire.

Pour la plupart des applications, l'API **Runtime** de plus haut niveau (par exemple, `cudaMalloc`, `cudaMemcpy`) est suffisante et plus simple. Utilisez l'API Driver lorsque vous avez besoin de ses fonctionnalités avancées.
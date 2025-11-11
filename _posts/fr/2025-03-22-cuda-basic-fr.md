---
audio: false
generated: true
lang: fr
layout: post
title: Exemple CUDA de Base
translated: true
type: note
---

Voici un exemple basique de CUDA qui démontre la programmation GPU de bas niveau en utilisant CUDA C. Cet exemple effectue une addition vectorielle simple sur le GPU en utilisant les constructions CUDA les plus fondamentales :

```c
#include <stdio.h>
#include <cuda.h>

// Noyau CUDA pour l'addition vectorielle
__global__ void vectorAdd(float *a, float *b, float *c, int n) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n) {
        c[i] = a[i] + b[i];
    }
}

int main() {
    int n = 1024;  // taille du vecteur
    size_t size = n * sizeof(float);
    
    // Allocation de mémoire hôte
    float *h_a = (float*)malloc(size);
    float *h_b = (float*)malloc(size);
    float *h_c = (float*)malloc(size);

    // Initialisation des tableaux hôte
    for(int i = 0; i < n; i++) {
        h_a[i] = i;
        h_b[i] = i * 2;
    }

    // Pointeurs de mémoire device
    float *d_a, *d_b, *d_c;
    
    // Allocation de mémoire device
    cudaMalloc((void**)&d_a, size);
    cudaMalloc((void**)&d_b, size);
    cudaMalloc((void**)&d_c, size);

    // Copie des données de l'hôte vers le device
    cudaMemcpy(d_a, h_a, size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_b, h_b, size, cudaMemcpyHostToDevice);

    // Configuration des paramètres de lancement du noyau
    int threadsPerBlock = 256;
    int blocksPerGrid = (n + threadsPerBlock - 1) / threadsPerBlock;

    // Lancement du noyau
    vectorAdd<<<blocksPerGrid, threadsPerBlock>>>(d_a, d_b, d_c, n);

    // Attente de la fin d'exécution du GPU
    cudaDeviceSynchronize();

    // Copie du résultat vers l'hôte
    cudaMemcpy(h_c, d_c, size, cudaMemcpyDeviceToHost);

    // Vérification des résultats
    for(int i = 0; i < 10; i++) {
        printf("%f + %f = %f\n", h_a[i], h_b[i], h_c[i]);
    }

    // Libération de la mémoire device
    cudaFree(d_a);
    cudaFree(d_b);
    cudaFree(d_c);

    // Libération de la mémoire hôte
    free(h_a);
    free(h_b);
    free(h_c);

    // Réinitialisation du device
    cudaDeviceReset();

    return 0;
}
```

Pour compiler et exécuter ce code, vous aurez besoin :
1. D'un GPU NVIDIA avec support CUDA
2. Du CUDA Toolkit installé
3. Compiler avec : `nvcc vector_add.cu -o vector_add`

Cet exemple démontre les opérations CUDA les plus fondamentales :
- Définition de noyau `__global__`
- Allocation manuelle de mémoire avec `cudaMalloc`
- Transferts de mémoire explicites avec `cudaMemcpy`
- Configuration de lancement de noyau avec `<<<blocks, threads>>>`
- Synchronisation de device
- Nettoyage de la mémoire

Aspects clés de bas niveau :
1. Gestion directe de la mémoire sans utiliser les aides d'exécution CUDA
2. Configuration manuelle des threads/blocs
3. Synchronisation explicite du device
4. Opérations sur pointeurs bruts
5. Aucune abstraction de haut niveau ou bibliothèques

Le noyau utilise la hiérarchie de threads CUDA de base :
- `blockIdx.x` : Index du bloc
- `blockDim.x` : Threads par bloc
- `threadIdx.x` : Index du thread dans le bloc

Ceci calcule un ID de thread unique pour chaque élément et effectue l'addition seulement si dans les limites. L'exemple reste simple mais montre les concepts fondamentaux de la programmation CUDA à un niveau bas.

La sortie affichera les 10 premiers résultats, comme :
```
0.000000 + 0.000000 = 0.000000
1.000000 + 2.000000 = 3.000000
2.000000 + 4.000000 = 6.000000
...
```
---
audio: false
generated: true
lang: fr
layout: post
title: Exemple d'addition vectorielle métallique
translated: true
type: note
---

Si vous utilisez macOS et souhaitez programmer le GPU en utilisant Metal (l'API bas niveau d'Apple pour le graphisme et le calcul), vous pouvez obtenir une fonctionnalité similaire à l'exemple CUDA que j'ai fourni précédemment. Metal est conçu pour vous donner un accès direct au GPU des appareils Apple, y compris les Mac, et il prend en charge à la fois les opérations de graphisme et de calcul. Voici un exemple Metal de base qui effectue une addition de vecteurs (similaire à l'exemple CUDA) en utilisant des constructions Metal de bas niveau en C++.

### Exemple d'Addition de Vecteurs avec Metal

Cet exemple utilise Metal pour additionner deux tableaux sur le GPU. Il évite les abstractions de haut niveau et s'en tient à l'API Metal de base pour une approche de bas niveau.

```cpp
#include <iostream>
#include <Metal/Metal.hpp>
#include <Foundation/Foundation.hpp>

int main() {
    // Initialiser le périphérique Metal
    NS::SharedPtr<MTL::Device> device = NS::TransferPtr(MTL::CreateSystemDefaultDevice());
    if (!device) {
        std::cerr << "Échec de la création du périphérique Metal" << std::endl;
        return 1;
    }

    // Taille des vecteurs
    const int n = 1024;
    const size_t bufferSize = n * sizeof(float);

    // Données hôte
    float* h_a = new float[n];
    float* h_b = new float[n];
    float* h_c = new float[n];

    // Initialiser les tableaux hôte
    for (int i = 0; i < n; i++) {
        h_a[i] = static_cast<float>(i);
        h_b[i] = static_cast<float>(i * 2);
    }

    // Créer les tampons Metal
    NS::SharedPtr<MTL::Buffer> d_a = NS::TransferPtr(device->newBuffer(h_a, bufferSize, MTL::ResourceStorageModeShared));
    NS::SharedPtr<MTL::Buffer> d_b = NS::TransferPtr(device->newBuffer(h_b, bufferSize, MTL::ResourceStorageModeShared));
    NS::SharedPtr<MTL::Buffer> d_c = NS::TransferPtr(device->newBuffer(bufferSize, MTL::ResourceStorageModeShared));

    // Créer la file de commandes
    NS::SharedPtr<MTL::CommandQueue> queue = NS::TransferPtr(device->newCommandQueue());

    // Charger le source du shader Metal (noyau d'addition de vecteurs)
    const char* kernelSource = R"(
        #include <metal_stdlib>
        using namespace metal;

        kernel void vectorAdd(device const float* a,
                             device const float* b,
                             device float* c,
                             uint id [[thread_position_in_grid]]) {
            c[id] = a[id] + b[id];
        }
    )";

    // Créer la bibliothèque et la fonction Metal
    NS::Error* error = nullptr;
    NS::SharedPtr<NS::String> source = NS::TransferPtr(NS::String::string(kernelSource, NS::UTF8StringEncoding));
    NS::SharedPtr<MTL::Library> library = NS::TransferPtr(device->newLibrary(source.get(), nullptr, &error));
    if (!library) {
        std::cerr << "Échec de la création de la bibliothèque : " << error->localizedDescription()->utf8String() << std::endl;
        return 1;
    }

    NS::SharedPtr<MTL::Function> function = NS::TransferPtr(library->newFunction(NS::String::string("vectorAdd", NS::UTF8StringEncoding)));
    if (!function) {
        std::cerr << "Échec de la création de la fonction" << std::endl;
        return 1;
    }

    // Créer l'état du pipeline de calcul
    NS::SharedPtr<MTL::ComputePipelineState> pipeline = NS::TransferPtr(device->newComputePipelineState(function.get(), &error));
    if (!pipeline) {
        std::cerr << "Échec de la création du pipeline : " << error->localizedDescription()->utf8String() << std::endl;
        return 1;
    }

    // Créer le tampon de commandes et l'encodeur
    NS::SharedPtr<MTL::CommandBuffer> commandBuffer = NS::TransferPtr(queue->commandBuffer());
    NS::SharedPtr<MTL::ComputeCommandEncoder> encoder = NS::TransferPtr(commandBuffer->computeCommandEncoder());

    // Définir le pipeline et les tampons
    encoder->setComputePipelineState(pipeline.get());
    encoder->setBuffer(d_a.get(), 0, 0);
    encoder->setBuffer(d_b.get(), 0, 1);
    encoder->setBuffer(d_c.get(), 0, 2);

    // Configurer les groupes de threads
    MTL::Size gridSize = MTL::Size(n, 1, 1);
    int threadsPerGroup = pipeline->maxTotalThreadsPerThreadgroup();
    if (threadsPerGroup > n) threadsPerGroup = n;
    MTL::Size threadgroupSize = MTL::Size(threadsPerGroup, 1, 1);

    // Dispatcher le noyau de calcul
    encoder->dispatchThreads(gridSize, threadgroupSize);
    encoder->endEncoding();

    // Exécuter et attendre
    commandBuffer->commit();
    commandBuffer->waitUntilCompleted();

    // Obtenir les résultats
    float* results = static_cast<float*>(d_c->contents());
    for (int i = 0; i < 10; i++) {
        std::cout << h_a[i] << " + " << h_b[i] << " = " << results[i] << std::endl;
    }

    // Nettoyage
    delete[] h_a;
    delete[] h_b;
    delete[] h_c;

    return 0;
}
```

### Prérequis
1. **macOS** : Ce code s'exécute sur macOS avec un GPU compatible (tout Mac moderne devrait fonctionner).
2. **Xcode** : Installez Xcode pour obtenir le framework Metal et les outils en ligne de commande.
3. **Compilation** : Utilisez `clang++` avec les frameworks Metal :
   ```bash
   clang++ -framework Metal -framework Foundation vector_add.mm -o vector_add
   ```
   Remarque : Enregistrez le fichier avec une extension `.mm` car il utilise Objective-C++ (Metal nécessite l'exécutif Objective-C).

### Aspects Clés de Bas Niveau
1. **Gestion Manuelle des Ressources** : Création explicite des tampons avec `newBuffer` et gestion de la mémoire sans wrappers de haut niveau.
2. **Définition Directe du Shader** : Le noyau en Metal Shading Language (MSL) est défini en ligne sous forme de chaîne, compilé à l'exécution.
3. **Configuration des Threads** : Calcul manuel des tailles de grille et de groupe de threads, similaire aux blocs et threads de CUDA.
4. **Contrôle du Tampon de Commandes** : Création et validation explicites des tampons de commandes pour l'exécution GPU.
5. **Aucune Abstraction** : Évite MetalKit ou autres frameworks de haut niveau, en restant sur les API Metal de base.

### Sortie
L'exécution produira quelque chose comme :
```
0 + 0 = 0
1 + 2 = 3
2 + 4 = 6
3 + 6 = 9
...
```

### Différences par Rapport à CUDA
- **Style d'API** : Metal utilise une API basée sur Objective-C++ avec des objets `NS::`, contrairement à l'API de style C de CUDA.
- **Modèle de Mémoire** : Le mode de stockage partagé de Metal (`MTL::ResourceStorageModeShared`) permet un accès CPU/GPU à la même mémoire, simplifiant les transferts par rapport au `cudaMemcpy` explicite de CUDA.
- **Modèle de Threads** : Metal utilise `dispatchThreads` avec des tailles de grille/groupe de threads, conceptuellement similaire au modèle grille/bloc de CUDA mais avec une terminologie et une configuration différentes.

### Conseils pour Metal sur macOS
- **Débogage** : Utilisez le débogueur Metal de Xcode pour inspecter l'exécution GPU.
- **Documentation** : Consultez la documentation Metal d'Apple pour plus de détails (disponible dans Xcode ou en ligne sur developer.apple.com).
- **Performance** : Pour des jeux de données plus importants, optimisez les tailles des groupes de threads en fonction de `maxTotalThreadsPerThreadgroup`.

Ceci est un point de départ pour la programmation Metal de bas niveau sur macOS. Vous pouvez l'étendre pour des tâches de calcul plus complexes ou du rendu graphique selon les besoins !
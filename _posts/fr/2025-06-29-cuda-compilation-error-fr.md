---
audio: false
generated: true
lang: fr
layout: post
title: Correction de l'Erreur de Compilation CUDA avec nvcc
translated: true
type: note
---

L'erreur indique que le toolkit CUDA n'est pas installé ou correctement configuré, car le compilateur ne trouve pas `cuda.h`. De plus, votre code est un fichier source CUDA (`.cu`) mais vous essayez de le compiler avec `gcc`, ce qui n'est pas adapté pour le code CUDA. Vous devez utiliser `nvcc`, le compilateur NVIDIA CUDA. Voici comment résoudre le problème :

### Étapes de Correction

1. **Installer le CUDA Toolkit** :
   - Assurez-vous que le NVIDIA CUDA Toolkit est installé sur votre système. Vous pouvez le télécharger depuis le [site web NVIDIA CUDA Toolkit](https://developer.nvidia.com/cuda-downloads).
   - Suivez les instructions d'installation pour votre système d'exploitation (Linux dans ce cas, d'après l'invite).
   - Après l'installation, vérifiez-la en exécutant :
     ```bash
     nvcc --version
     ```
     Cela devrait afficher la version de CUDA si l'installation est correcte.

2. **Utiliser `nvcc` pour Compiler** :
   - Puisque votre fichier est un fichier source CUDA (`.cu`), compilez-le avec `nvcc` au lieu de `gcc`. Remplacez :
     ```bash
     gcc scripts/benchmark/cudamark.c
     ```
     par :
     ```bash
     nvcc scripts/benchmark/cudamark.cu
     ```
   - Remarque : Assurez-vous que l'extension du fichier correspond à votre fichier actuel (`.cu` dans le code que vous avez fourni, et non `.c` comme dans l'erreur).

3. **Configurer l'Environnement CUDA** :
   - Assurez-vous que les chemins du toolkit CUDA sont inclus dans votre environnement. Ajoutez les lignes suivantes à votre fichier de configuration de shell `~/.bashrc` ou équivalent :
     ```bash
     export PATH=/usr/local/cuda/bin:$PATH
     export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
     ```
     Ensuite, rechargez le fichier :
     ```bash
     source ~/.bashrc
     ```

4. **Lier la Bibliothèque Thrust** :
   - Votre code utilise Thrust, qui fait partie du toolkit CUDA, donc aucune bibliothèque supplémentaire n'a besoin d'être liée explicitement. Cependant, assurez-vous d'avoir une version compatible de CUDA (Thrust est inclus dans CUDA 7.0 et versions ultérieures).

5. **Corriger les Problèmes de Code** :
   - Le code fait référence à `thread_counts` mais ne l'utilise pas dans la fonction `benchmark`. La fonction `parallel_sort_gpu` utilise Thrust, qui gère le parallélisme en interne, donc la boucle `thread_counts` dans `main` est trompeuse. Si vous aviez l'intention de comparer les performances de différentes configurations de threads, le tri de Thrust ne permet pas un contrôle direct du nombre de threads. Vous pourriez clarifier cette logique ou supprimer le `thread_counts` inutilisé.
   - Pour plus de clarté, vous pourriez modifier le code pour évaluer plusieurs fois la même taille de liste afin de moyenner les variations de temps :

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
         int num_runs = 8; // Nombre d'exécutions pour la moyenne

         printf("Run,TimeTakenSeconds\n");
         for (int i = 0; i < num_runs; ++i) {
             double t = benchmark(list_size);
             printf("%d,%.6f\n", i + 1, t);
         }
         return 0;
     }
     ```

6. **Compiler le Code Mis à Jour** :
   - Enregistrez le code sous `cudamark.cu` et compilez-le :
     ```bash
     nvcc -o cudamark scripts/benchmark/cudamark.cu
     ```
   - Si vous rencontrez des erreurs de l'éditeur de liens, assurez-vous que les bibliothèques CUDA sont accessibles (voir étape 3).

7. **Exécuter le Programme** :
   - Exécutez le binaire compilé :
     ```bash
     ./cudamark
     ```

8. **Notes Supplémentaires** :
   - **Extension de Fichier** : Assurez-vous que le fichier a une extension `.cu`, car les fichiers CUDA nécessitent cela pour que `nvcc` les traite correctement.
   - **Disponibilité du GPU** : Assurez-vous d'avoir un GPU compatible CUDA et les pilotes corrects installés. Vérifiez avec :
     ```bash
     nvidia-smi
     ```
   - **Thrust et Version CUDA** : Vérifiez que votre version de CUDA prend en charge Thrust. CUDA 11.x ou une version ultérieure est recommandée pour les fonctionnalités modernes de Thrust.
   - **Précision du Chronométrage** : La fonction `clock()` mesure le temps CPU, pas le temps d'exécution du GPU. Pour un chronométrage plus précis du GPU, envisagez d'utiliser les événements CUDA :
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
     return milliseconds / 1000.0; // Convertir en secondes
     ```

9. **Si les Erreurs Persistent** :
   - Si `cuda.h` n'est toujours pas trouvé, vérifiez le chemin d'installation du toolkit CUDA (par exemple, `/usr/local/cuda/include`). Vous devrez peut-être spécifier explicitement le chemin d'inclusion :
     ```bash
     nvcc -I/usr/local/cuda/include -o cudamark scripts/benchmark/cudamark.cu
     ```
   - Assurez-vous que le chemin du fichier `scripts/benchmark/cudamark.cu` est correct par rapport à votre répertoire actuel.

### Commande de Compilation Mise à Jour
```bash
nvcc -o cudamark scripts/benchmark/cudamark.cu
```

### Résultat Attendu
Après avoir résolu les problèmes, l'exécution de `./cudamark` devrait produire une sortie similaire à :
```
Run,TimeTakenSeconds
1,0.123456
2,0.124567
...
```

Si vous avez besoin d'une aide supplémentaire ou si vous rencontrez des erreurs spécifiques, veuillez les partager !
---
audio: false
generated: true
lang: de
layout: post
title: Beheben von CUDA-Kompilierungsfehlern mit nvcc
translated: true
type: note
---

Der Fehler zeigt an, dass das CUDA Toolkit nicht installiert oder nicht korrekt konfiguriert ist, da der Compiler `cuda.h` nicht finden kann. Zusätzlich ist Ihre Code-Datei eine CUDA-Quelldatei (`.cu`), Sie versuchen jedoch, sie mit `gcc` zu kompilieren, was für CUDA-Code nicht geeignet ist. Sie müssen `nvcc`, den NVIDIA CUDA Compiler, verwenden. So beheben Sie das Problem:

### Schritte zur Fehlerbehebung

1. **CUDA Toolkit installieren**:
   - Stellen Sie sicher, dass das NVIDIA CUDA Toolkit auf Ihrem System installiert ist. Sie können es von der [NVIDIA CUDA Toolkit Website](https://developer.nvidia.com/cuda-downloads) herunterladen.
   - Befolgen Sie die Installationsanweisungen für Ihr Betriebssystem (in diesem Fall Linux, basierend auf der Eingabeaufforderung).
   - Überprüfen Sie nach der Installation die Installation, indem Sie ausführen:
     ```bash
     nvcc --version
     ```
     Dies sollte die CUDA-Version anzeigen, wenn sie korrekt installiert ist.

2. **`nvcc` zum Kompilieren verwenden**:
   - Da Ihre Datei eine CUDA-Quelldatei (`.cu`) ist, kompilieren Sie sie mit `nvcc` anstelle von `gcc`. Ersetzen Sie:
     ```bash
     gcc scripts/benchmark/cudamark.c
     ```
     durch:
     ```bash
     nvcc scripts/benchmark/cudamark.cu
     ```
   - Hinweis: Stellen Sie sicher, dass die Dateierweiterung mit Ihrer tatsächlichen Datei übereinstimmt (`.cu` im bereitgestellten Code, nicht `.c` wie im Fehler).

3. **CUDA-Umgebung einrichten**:
   - Stellen Sie sicher, dass die CUDA Toolkit-Pfade in Ihrer Umgebung enthalten sind. Fügen Sie Folgendes zu Ihrer `~/.bashrc` oder einer entsprechenden Shell-Konfigurationsdatei hinzu:
     ```bash
     export PATH=/usr/local/cuda/bin:$PATH
     export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
     ```
     Führen Sie dann einen Sourcen-Befehl für die Datei aus:
     ```bash
     source ~/.bashrc
     ```

4. **Thrust-Bibliothek einbinden**:
   - Ihr Code verwendet Thrust, das Teil des CUDA Toolkits ist, daher müssen keine zusätzlichen Bibliotheken explizit eingebunden werden. Stellen Sie jedoch sicher, dass Sie eine kompatible CUDA-Version haben (Thrust ist in CUDA 7.0 und höher enthalten).

5. **Code-Probleme beheben**:
   - Der Code verweist auf `thread_counts`, verwendet es aber nicht in der `benchmark`-Funktion. Die `parallel_sort_gpu`-Funktion verwendet Thrust, das die Parallelität intern verwaltet, daher ist die `thread_counts`-Schleife in `main` irreführend. Wenn Sie verschiedene Thread-Konfigurationen benchmarken wollten, erlaubt Thrusts Sortierfunktion keine direkte Steuerung der Thread-Anzahl. Sie sollten diese Logik klären oder die ungenutzte `thread_counts` entfernen.
   - Zur Verdeutlichung könnten Sie den Code ändern, um dieselbe Listengröße mehrmals zu benchmarken, um Timing-Schwankungen zu mitteln:

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
         int num_runs = 8; // Anzahl der Durchläufe zum Mitteln

         printf("Run,TimeTakenSeconds\n");
         for (int i = 0; i < num_runs; ++i) {
             double t = benchmark(list_size);
             printf("%d,%.6f\n", i + 1, t);
         }
         return 0;
     }
     ```

6. **Aktualisierten Code kompilieren**:
   - Speichern Sie den Code als `cudamark.cu` und kompilieren Sie ihn:
     ```bash
     nvcc -o cudamark scripts/benchmark/cudamark.cu
     ```
   - Wenn Sie Linker-Fehler erhalten, stellen Sie sicher, dass die CUDA-Bibliotheken zugänglich sind (siehe Schritt 3).

7. **Das Programm ausführen**:
   - Führen Sie die kompilierte Binärdatei aus:
     ```bash
     ./cudamark
     ```

8. **Zusätzliche Hinweise**:
   - **Dateierweiterung**: Stellen Sie sicher, dass die Datei die Erweiterung `.cu` hat, da CUDA-Dateien diese benötigen, damit `nvcc` sie korrekt verarbeiten kann.
   - **GPU-Verfügbarkeit**: Stellen Sie sicher, dass Sie eine CUDA-fähige GPU und die korrekten Treiber installiert haben. Überprüfen Sie dies mit:
     ```bash
     nvidia-smi
     ```
   - **Thrust und CUDA-Version**: Verifizieren Sie, dass Ihre CUDA-Version Thrust unterstützt. CUDA 11.x oder höher wird für moderne Thrust-Funktionen empfohlen.
   - **Timing-Genauigkeit**: Die `clock()`-Funktion misst die CPU-Zeit, nicht die GPU-Ausführungszeit. Für eine genauere GPU-Zeitmessung sollten Sie CUDA-Events in Betracht ziehen:
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
     return milliseconds / 1000.0; // In Sekunden umwandeln
     ```

9. **Wenn Fehler weiterhin bestehen**:
   - Wenn `cuda.h` immer noch nicht gefunden wird, überprüfen Sie den Installationspfad des CUDA Toolkits (z.B. `/usr/local/cuda/include`). Möglicherweise müssen Sie den Include-Pfad explizit angeben:
     ```bash
     nvcc -I/usr/local/cuda/include -o cudamark scripts/benchmark/cudamark.cu
     ```
   - Stellen Sie sicher, dass der Dateipfad `scripts/benchmark/cudamark.cu` relativ zu Ihrem aktuellen Verzeichnis korrekt ist.

### Aktualisierter Kompilierungsbefehl
```bash
nvcc -o cudamark scripts/benchmark/cudamark.cu
```

### Erwartete Ausgabe
Nach der Behebung der Probleme sollte die Ausführung von `./cudamark` eine Ausgabe wie folgt produzieren:
```
Run,TimeTakenSeconds
1,0.123456
2,0.124567
...
```

Wenn Sie weitere Hilfe benötigen oder auf spezifische Fehler stoßen, teilen Sie diese bitte mit!
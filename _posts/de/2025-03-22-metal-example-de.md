---
audio: false
generated: true
lang: de
layout: post
title: Beispiel zur Vektoraddition von Metallen
translated: true
type: note
---

Wenn Sie macOS verwenden und die GPU mit Metal (Apples Low-Level-Grafik- und Compute-API) programmieren möchten, können Sie ähnliche Funktionalität wie im zuvor bereitgestellten CUDA-Beispiel erreichen. Metal wurde entwickelt, um Ihnen direkten Zugriff auf die GPU in Apple-Geräten, einschließlich Macs, zu geben, und es unterstützt sowohl Grafik- als auch Compute-Operationen. Nachfolgend finden Sie ein grundlegendes Metal-Beispiel, das eine Vektoraddition (ähnlich dem CUDA-Beispiel) unter Verwendung von Low-Level-Metal-Konstrukten in C++ durchführt.

### Metal-Vektoraddition-Beispiel

Dieses Beispiel verwendet Metal, um zwei Arrays auf der GPU zu addieren. Es vermeidet High-Level-Abstraktionen und bleibt bei der Kern-Metal-API für einen Low-Level-Ansatz.

```cpp
#include <iostream>
#include <Metal/Metal.hpp>
#include <Foundation/Foundation.hpp>

int main() {
    // Metal-Gerät initialisieren
    NS::SharedPtr<MTL::Device> device = NS::TransferPtr(MTL::CreateSystemDefaultDevice());
    if (!device) {
        std::cerr << "Fehler beim Erstellen des Metal-Geräts" << std::endl;
        return 1;
    }

    // Vektorgröße
    const int n = 1024;
    const size_t bufferSize = n * sizeof(float);

    // Host-Daten
    float* h_a = new float[n];
    float* h_b = new float[n];
    float* h_c = new float[n];

    // Host-Arrays initialisieren
    for (int i = 0; i < n; i++) {
        h_a[i] = static_cast<float>(i);
        h_b[i] = static_cast<float>(i * 2);
    }

    // Metal-Buffer erstellen
    NS::SharedPtr<MTL::Buffer> d_a = NS::TransferPtr(device->newBuffer(h_a, bufferSize, MTL::ResourceStorageModeShared));
    NS::SharedPtr<MTL::Buffer> d_b = NS::TransferPtr(device->newBuffer(h_b, bufferSize, MTL::ResourceStorageModeShared));
    NS::SharedPtr<MTL::Buffer> d_c = NS::TransferPtr(device->newBuffer(bufferSize, MTL::ResourceStorageModeShared));

    // Befehls-Warteschlange erstellen
    NS::SharedPtr<MTL::CommandQueue> queue = NS::TransferPtr(device->newCommandQueue());

    // Metal-Shader-Quellcode laden (Vektoraddition-Kernel)
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

    // Metal-Bibliothek und Funktion erstellen
    NS::Error* error = nullptr;
    NS::SharedPtr<NS::String> source = NS::TransferPtr(NS::String::string(kernelSource, NS::UTF8StringEncoding));
    NS::SharedPtr<MTL::Library> library = NS::TransferPtr(device->newLibrary(source.get(), nullptr, &error));
    if (!library) {
        std::cerr << "Fehler beim Erstellen der Bibliothek: " << error->localizedDescription()->utf8String() << std::endl;
        return 1;
    }

    NS::SharedPtr<MTL::Function> function = NS::TransferPtr(library->newFunction(NS::String::string("vectorAdd", NS::UTF8StringEncoding)));
    if (!function) {
        std::cerr << "Fehler beim Erstellen der Funktion" << std::endl;
        return 1;
    }

    // Compute-Pipeline-Status erstellen
    NS::SharedPtr<MTL::ComputePipelineState> pipeline = NS::TransferPtr(device->newComputePipelineState(function.get(), &error));
    if (!pipeline) {
        std::cerr << "Fehler beim Erstellen der Pipeline: " << error->localizedDescription()->utf8String() << std::endl;
        return 1;
    }

    // Befehls-Puffer und -Encoder erstellen
    NS::SharedPtr<MTL::CommandBuffer> commandBuffer = NS::TransferPtr(queue->commandBuffer());
    NS::SharedPtr<MTL::ComputeCommandEncoder> encoder = NS::TransferPtr(commandBuffer->computeCommandEncoder());

    // Pipeline und Buffer setzen
    encoder->setComputePipelineState(pipeline.get());
    encoder->setBuffer(d_a.get(), 0, 0);
    encoder->setBuffer(d_b.get(), 0, 1);
    encoder->setBuffer(d_c.get(), 0, 2);

    // Thread-Gruppen konfigurieren
    MTL::Size gridSize = MTL::Size(n, 1, 1);
    int threadsPerGroup = pipeline->maxTotalThreadsPerThreadgroup();
    if (threadsPerGroup > n) threadsPerGroup = n;
    MTL::Size threadgroupSize = MTL::Size(threadsPerGroup, 1, 1);

    // Compute-Kernel ausführen
    encoder->dispatchThreads(gridSize, threadgroupSize);
    encoder->endEncoding();

    // Ausführen und warten
    commandBuffer->commit();
    commandBuffer->waitUntilCompleted();

    // Ergebnisse abrufen
    float* results = static_cast<float*>(d_c->contents());
    for (int i = 0; i < 10; i++) {
        std::cout << h_a[i] << " + " << h_b[i] << " = " << results[i] << std::endl;
    }

    // Bereinigung
    delete[] h_a;
    delete[] h_b;
    delete[] h_c;

    return 0;
}
```

### Voraussetzungen
1. **macOS**: Dieser Code läuft auf macOS mit einer kompatiblen GPU (jeder moderne Mac sollte funktionieren).
2. **Xcode**: Installieren Sie Xcode, um das Metal-Framework und die Command-Line-Tools zu erhalten.
3. **Kompilieren**: Verwenden Sie `clang++` mit Metal-Frameworks:
   ```bash
   clang++ -framework Metal -framework Foundation vector_add.mm -o vector_add
   ```
   Hinweis: Speichern Sie die Datei mit der Erweiterung `.mm`, da sie Objective-C++ verwendet (Metal benötigt die Objective-C-Laufzeitumgebung).

### Wichtige Low-Level-Aspekte
1. **Manuelle Ressourcenverwaltung**: Explizites Erstellen von Buffern mit `newBuffer` und Verwalten des Speichers ohne High-Level-Wrapper.
2. **Direkte Shader-Definition**: Der Metal Shading Language (MSL)-Kernel wird inline als String definiert und zur Laufzeit kompiliert.
3. **Thread-Konfiguration**: Manuelles Berechnen der Grid- und Threadgroup-Größen, ähnlich wie CUDA-Blöcke und -Threads.
4. **Befehls-Puffer-Steuerung**: Explizites Erstellen und Committen von Befehls-Puffern für die GPU-Ausführung.
5. **Keine Abstraktionen**: Vermeidet MetalKit oder andere High-Level-Frameworks und bleibt bei den Kern-Metal-APIs.

### Ausgabe
Die Ausführung erzeugt in etwa:
```
0 + 0 = 0
1 + 2 = 3
2 + 4 = 6
3 + 6 = 9
...
```

### Unterschiede zu CUDA
- **API-Stil**: Metal verwendet eine Objective-C++-basierte API mit `NS::`-Objekten, anders als CUDAs C-style-API.
- **Speichermodell**: Metals Shared Storage Mode (`MTL::ResourceStorageModeShared`) erlaubt CPU/GPU-Zugriff auf denselben Speicher, was Transfers im Vergleich zu CUDAs explizitem `cudaMemcpy` vereinfacht.
- **Thread-Modell**: Metal verwendet `dispatchThreads` mit Grid-/Threadgroup-Größen, konzeptionell ähnlich zu CUDAs Grid-/Block-Modell, aber mit unterschiedlicher Terminologie und Konfiguration.

### Tipps für Metal auf macOS
- **Debugging**: Verwenden Sie Xcodes Metal-Debugger, um die GPU-Ausführung zu inspizieren.
- **Dokumentation**: Konsultieren Sie Apples Metal-Dokumentation für tiefergehende Details (verfügbar in Xcode oder online unter developer.apple.com).
- **Leistung**: Optimieren Sie für größere Datensätze die Threadgroup-Größen basierend auf `maxTotalThreadsPerThreadgroup`.

Dies ist ein Ausgangspunkt für Low-Level-Metal-Programmierung auf macOS. Sie können es für komplexere Compute-Aufgaben oder Grafik-Rendering nach Bedarf erweitern!
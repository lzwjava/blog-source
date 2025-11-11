---
audio: false
generated: true
lang: es
layout: post
title: Ejemplo de Adición de Vectores Metálicos
translated: true
type: note
---

Si estás usando macOS y quieres programar la GPU usando Metal (la API de bajo nivel de Apple para gráficos y computación), puedes lograr una funcionalidad similar al ejemplo de CUDA que proporcioné anteriormente. Metal está diseñado para darte acceso directo a la GPU en dispositivos Apple, incluyendo Macs, y soporta tanto operaciones de gráficos como de computación. A continuación se muestra un ejemplo básico de Metal que realiza una suma de vectores (similar al ejemplo de CUDA) usando construcciones de bajo nivel de Metal en C++.

### Ejemplo de Suma de Vectores con Metal

Este ejemplo usa Metal para sumar dos arreglos en la GPU. Evita abstracciones de alto nivel y se apega a la API central de Metal para un enfoque de bajo nivel.

```cpp
#include <iostream>
#include <Metal/Metal.hpp>
#include <Foundation/Foundation.hpp>

int main() {
    // Inicializar dispositivo Metal
    NS::SharedPtr<MTL::Device> device = NS::TransferPtr(MTL::CreateSystemDefaultDevice());
    if (!device) {
        std::cerr << "Error al crear el dispositivo Metal" << std::endl;
        return 1;
    }

    // Tamaño del vector
    const int n = 1024;
    const size_t bufferSize = n * sizeof(float);

    // Datos del host
    float* h_a = new float[n];
    float* h_b = new float[n];
    float* h_c = new float[n];

    // Inicializar arreglos del host
    for (int i = 0; i < n; i++) {
        h_a[i] = static_cast<float>(i);
        h_b[i] = static_cast<float>(i * 2);
    }

    // Crear buffers de Metal
    NS::SharedPtr<MTL::Buffer> d_a = NS::TransferPtr(device->newBuffer(h_a, bufferSize, MTL::ResourceStorageModeShared));
    NS::SharedPtr<MTL::Buffer> d_b = NS::TransferPtr(device->newBuffer(h_b, bufferSize, MTL::ResourceStorageModeShared));
    NS::SharedPtr<MTL::Buffer> d_c = NS::TransferPtr(device->newBuffer(bufferSize, MTL::ResourceStorageModeShared));

    // Crear cola de comandos
    NS::SharedPtr<MTL::CommandQueue> queue = NS::TransferPtr(device->newCommandQueue());

    // Cargar código fuente del shader Metal (kernel de suma de vectores)
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

    // Crear librería y función de Metal
    NS::Error* error = nullptr;
    NS::SharedPtr<NS::String> source = NS::TransferPtr(NS::String::string(kernelSource, NS::UTF8StringEncoding));
    NS::SharedPtr<MTL::Library> library = NS::TransferPtr(device->newLibrary(source.get(), nullptr, &error));
    if (!library) {
        std::cerr << "Error al crear la librería: " << error->localizedDescription()->utf8String() << std::endl;
        return 1;
    }

    NS::SharedPtr<MTL::Function> function = NS::TransferPtr(library->newFunction(NS::String::string("vectorAdd", NS::UTF8StringEncoding)));
    if (!function) {
        std::cerr << "Error al crear la función" << std::endl;
        return 1;
    }

    // Crear estado de la pipeline de computación
    NS::SharedPtr<MTL::ComputePipelineState> pipeline = NS::TransferPtr(device->newComputePipelineState(function.get(), &error));
    if (!pipeline) {
        std::cerr << "Error al crear la pipeline: " << error->localizedDescription()->utf8String() << std::endl;
        return 1;
    }

    // Crear buffer de comandos y codificador
    NS::SharedPtr<MTL::CommandBuffer> commandBuffer = NS::TransferPtr(queue->commandBuffer());
    NS::SharedPtr<MTL::ComputeCommandEncoder> encoder = NS::TransferPtr(commandBuffer->computeCommandEncoder());

    // Configurar pipeline y buffers
    encoder->setComputePipelineState(pipeline.get());
    encoder->setBuffer(d_a.get(), 0, 0);
    encoder->setBuffer(d_b.get(), 0, 1);
    encoder->setBuffer(d_c.get(), 0, 2);

    // Configurar grupos de hilos
    MTL::Size gridSize = MTL::Size(n, 1, 1);
    int threadsPerGroup = pipeline->maxTotalThreadsPerThreadgroup();
    if (threadsPerGroup > n) threadsPerGroup = n;
    MTL::Size threadgroupSize = MTL::Size(threadsPerGroup, 1, 1);

    // Despachar kernel de computación
    encoder->dispatchThreads(gridSize, threadgroupSize);
    encoder->endEncoding();

    // Ejecutar y esperar
    commandBuffer->commit();
    commandBuffer->waitUntilCompleted();

    // Obtener resultados
    float* results = static_cast<float*>(d_c->contents());
    for (int i = 0; i < 10; i++) {
        std::cout << h_a[i] << " + " << h_b[i] << " = " << results[i] << std::endl;
    }

    // Limpieza
    delete[] h_a;
    delete[] h_b;
    delete[] h_c;

    return 0;
}
```

### Prerrequisitos
1. **macOS**: Este código se ejecuta en macOS con una GPU compatible (cualquier Mac moderno debería funcionar).
2. **Xcode**: Instala Xcode para obtener el framework Metal y las herramientas de línea de comandos.
3. **Compilar**: Usa `clang++` con los frameworks Metal:
   ```bash
   clang++ -framework Metal -framework Foundation vector_add.mm -o vector_add
   ```
   Nota: Guarda el archivo con extensión `.mm` ya que usa Objective-C++ (Metal requiere el runtime de Objective-C).

### Aspectos Clave de Bajo Nivel
1. **Gestión Manual de Recursos**: Crear explícitamente buffers con `newBuffer` y gestionar la memoria sin wrappers de alto nivel.
2. **Definición Directa del Shader**: El kernel del Metal Shading Language (MSL) se define en línea como una cadena, compilado en tiempo de ejecución.
3. **Configuración de Hilos**: Calcular manualmente los tamaños de la cuadrícula y del grupo de hilos, similar a los bloques e hilos de CUDA.
4. **Control del Buffer de Comandos**: Crear y confirmar explícitamente los buffers de comandos para la ejecución en la GPU.
5. **Sin Abstracciones**: Evita MetalKit u otros frameworks de alto nivel, apegándose a las APIs centrales de Metal.

### Salida
Ejecutar esto producirá algo como:
```
0 + 0 = 0
1 + 2 = 3
2 + 4 = 6
3 + 6 = 9
...
```

### Diferencias con CUDA
- **Estilo de la API**: Metal usa una API basada en Objective-C++ con objetos `NS::`, a diferencia de la API estilo C de CUDA.
- **Modelo de Memoria**: El modo de almacenamiento compartido de Metal (`MTL::ResourceStorageModeShared`) permite el acceso de la CPU/GPU a la misma memoria, simplificando las transferencias comparado con `cudaMemcpy` explícito de CUDA.
- **Modelo de Hilos**: Metal usa `dispatchThreads` con tamaños de cuadrícula/grupo de hilos, conceptualmente similar al modelo de cuadrícula/bloque de CUDA pero con terminología y configuración diferentes.

### Consejos para Metal en macOS
- **Depuración**: Usa el depurador Metal de Xcode para inspeccionar la ejecución en la GPU.
- **Documentación**: Consulta la documentación de Metal de Apple para obtener detalles más profundos (disponible en Xcode o en línea en developer.apple.com).
- **Rendimiento**: Para conjuntos de datos más grandes, optimiza los tamaños de los grupos de hilos basándote en `maxTotalThreadsPerThreadgroup`.

¡Este es un punto de partida para la programación de bajo nivel con Metal en macOS. Puedes extenderlo para tareas de computación más complejas o renderizado de gráficos según sea necesario!
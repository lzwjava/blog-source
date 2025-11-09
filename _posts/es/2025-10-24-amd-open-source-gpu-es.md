---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: AMD Lidera en Soporte de GPU de Código Abierto
translated: true
type: note
---

### AMD vs. NVIDIA: Compromiso con el Código Abierto

Sí, generalmente se considera que AMD es más de código abierto que NVIDIA, particularmente en el contexto de controladores de GPU, pilas de software y soporte del ecosistema. Esto se debe al énfasis de larga data de AMD en soluciones completamente de código abierto, especialmente para Linux, donde sus controladores son maduros, están integrados en el kernel y son impulsados por la comunidad. NVIDIA, aunque ha hecho avances hacia la apertura en los últimos años, todavía depende en gran medida de componentes propietarios para obtener el máximo rendimiento y todas las funciones. A continuación, lo desglosaré por áreas clave.

#### Controladores de GPU
- **AMD**: El controlador AMDGPU es completamente de código abierto y ha sido el predeterminado para las GPU Radeon desde 2016. Está incluido directamente en el kernel de Linux (más de 5.9 millones de líneas de código a mediados de 2025), proporcionando soporte inmediato para renderizado, computación y Vulkan sin necesidad de blobs propietarios. Esto lo hace perfecto para usuarios y desarrolladores de Linux.
- **NVIDIA**: Los controladores tradicionales de NVIDIA son propietarios y requieren instalación manual para un rendimiento óptimo. Han abierto el código de los módulos del kernel desde 2022 (a través del proyecto `nvidia-open`), pero los componentes del espacio de usuario siguen siendo de código cerrado. Sus esfuerzos más recientes, como el controlador NOVA basado en Rust y las mejoras en Nouveau, todavía son experimentales y carecen de paridad completa de funciones (por ejemplo, sin soporte completo para DLSS o trazado de rayos avanzado en las variantes abiertas a finales de 2025).

**Ventaja**: AMD gana en confiabilidad e integración en entornos abiertos como Linux.

#### Pilas de Software para Computación e IA
- **AMD**: ROCm (Radeon Open Compute) es completamente de código abierto y admite frameworks de machine learning como PyTorch y TensorFlow en las GPU de AMD. Está diseñado para ser portable entre hardware y sistemas operativos, aunque históricamente ha estado por detrás en madurez del ecosistema en comparación con los competidores.
- **NVIDIA**: CUDA es el estándar de oro para la computación acelerada por GPU, pero es propietario y exclusivo de NVIDIA. Existen alternativas como OpenCL, pero están menos optimizadas. NVIDIA ha abierto el código de algunos componentes (por ejemplo, subconjuntos de cuDNN), pero la pila central sigue siendo cerrada, lo que limita la interoperabilidad.

**Ventaja**: AMD por su apertura, pero NVIDIA domina en herramientas pulidas y ricas en funciones, a menudo a costa del vendor lock-in.

#### Ecosistema y Comunidad en General
- AMD contribuye activamente a proyectos abiertos como Mesa (para gráficos) y tiene mejor soporte para Wayland de forma inmediata. Su enfoque fomenta las contribuciones de la comunidad, reduciendo los dolores de cabeza para los usuarios en distribuciones de código abierto.
- El progreso de NVIDIA incluye parches vGPU abiertos y una mejor confiabilidad de Nouveau en 2025, pero persisten problemas como los blobs de firmware y el soporte incompleto de Vulkan. Según los comentarios de la comunidad, son más "open-washing" que totalmente comprometidos.

En resumen, si "más código abierto" significa código accesible y modificable sin dependencias propietarias, AMD lleva la delantera, especialmente para gaming en Linux, desarrollo e inferencia de IA. NVIDIA sobresale en rendimiento bruto y funciones propietarias, pero se queda atrás en transparencia. Su elección depende de las prioridades: apertura (AMD) vs. dominio del ecosistema (NVIDIA).

#### Referencias
- [AMD vs Nvidia GPU: Which is better on Linux? (Reddit, 2023)](https://www.reddit.com/r/linux_gaming/comments/18nv50w/amd_vs_nvidia_gpu_which_is_better_on_linux_updated/)
- [NVIDIA vs AMD on Linux: Which GPU Should You Choose? (Linuxiac, 2025)](https://linuxiac.com/nvidia-vs-amd-gpus-on-linux/)
- [Open-Source NVIDIA Linux Driver Usage About To Become Much More Reliable (Phoronix, 2025)](https://www.phoronix.com/news/Nouveau-More-Reliable-Fix)
- [AMD Kernel Graphics Driver Exceeds 5.9 Million Lines In Linux 6.16 (Phoronix, 2025)](https://www.phoronix.com/news/Linux-6.16-AMDGPU-Driver-Size)
- [NVIDIA Posts Latest Linux Driver Patches For Open-Source vGPU Support (Phoronix, 2025)](https://www.phoronix.com/news/NVIDIA-vGPU-RFC-v2)
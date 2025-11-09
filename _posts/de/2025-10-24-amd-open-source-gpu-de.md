---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: AMD führt bei Open-Source-Grafikkartentreibern
translated: true
type: note
---

### AMD vs. NVIDIA: Open-Source-Engagement

Ja, AMD wird allgemein als quelloffener als NVIDIA angesehen, insbesondere im Kontext von GPU-Treibern, Software-Stacks und der Unterstützung des Ökosystems. Dies rührt von AMDs langjährigem Schwerpunkt auf vollständig quelloffenen Lösungen her, insbesondere für Linux, wo ihre Treiber ausgereift, kernelintegriert und community-gesteuert sind. NVIDIA, obwohl in den letzten Jahren Fortschritte in Richtung Offenheit gemacht, verlässt sich für volle Leistung und Funktionen nach wie vor stark auf proprietäre Komponenten. Im Folgenden werde ich dies nach Schlüsselbereichen aufschlüsseln.

#### GPU-Treiber
- **AMD**: Der AMDGPU-Treiber ist vollständig quelloffen und seit 2016 der Standard für Radeon-GPUs. Er ist direkt im Linux-Kernel enthalten (über 5,9 Millionen Codezeilen Mitte 2025) und bietet Out-of-the-Box-Unterstützung für Rendering, Compute und Vulkan, ohne proprietäre Blobs zu benötigen. Dies macht ihn nahtlos für Linux-Nutzer und Entwickler.
- **NVIDIA**: NVIDIAs traditionelle Treiber sind proprietär und erfordern für optimale Leistung eine manuelle Installation. Sie haben die Kernel-Module seit 2022 quelloffen gemacht (über das `nvidia-open`-Projekt), aber die Userspace-Komponenten bleiben closed-source. Ihre neueren Bemühungen, wie der Rust-basierte NOVA-Treiber und Nouveau-Verbesserungen, sind noch experimentell und erreichen keine volle Funktionsparität (z.B. keine vollständige DLSS- oder fortgeschrittene Raytracing-Unterstützung in quelloffenen Varianten bis Ende 2025).

**Vorteil**: AMD gewinnt aufgrund von Zuverlässigkeit und Integration in offenen Umgebungen wie Linux.

#### Compute- und AI-Software-Stacks
- **AMD**: ROCm (Radeon Open Compute) ist vollständig quelloffen und unterstützt Machine-Learning-Frameworks wie PyTorch und TensorFlow auf AMD-GPUs. Es ist für Portabilität über Hardware und Betriebssysteme hinweg konzipiert, hat aber historisch in der Ökosystemreife im Vergleich zu Mitbewerbern hinterhergehinkt.
- **NVIDIA**: CUDA ist der Goldstandard für GPU-beschleunigtes Rechnen, ist jedoch proprietär und exklusiv für NVIDIA. Alternativen wie OpenCL existieren, sind aber weniger optimiert. NVIDIA hat einige Komponenten quelloffen gemacht (z.B. cuDNN-Teilmengen), aber der Kern-Stack bleibt geschlossen, was die Interoperabilität einschränkt.

**Vorteil**: AMD gewinnt in puncto Offenheit, aber NVIDIA dominiert bei ausgereiften, funktionsreichen Tools – oft auf Kosten von Vendor-Lock-in.

#### Breiteres Ökosystem und Community
- AMD beteiligt sich aktiv an offenen Projekten wie Mesa (für Grafik) und hat eine bessere Wayland-Unterstützung out of the box. Ihr Ansatz fördert Community-Beiträge und verringert die Probleme für Nutzer in quelloffenen Distributionen.
- NVIDIAs Fortschritte beinhalten offene vGPU-Patches und eine bessere Nouveau-Zuverlässigkeit im Jahr 2025, aber Probleme wie Firmware-Blobs und unvollständige Vulkan-Unterstützung bestehen fort. Laut Community-Feedback betreiben sie eher "Open-Washing" als sich vollständig zu verpflichten.

Zusammenfassend lässt sich sagen: Wenn "quelloffener" zugänglicher, modifizierbarer Code ohne proprietäre Abhängigkeiten bedeutet, führt AMD – insbesondere für Linux-Gaming, Entwicklung und AI-Inferenz. NVIDIA glänzt mit roher Leistung und proprietären Funktionen, hinkt bei Transparenz aber hinterher. Ihre Wahl hängt von den Prioritäten ab: Offenheit (AMD) vs. Ökosystem-Dominanz (NVIDIA).

#### Referenzen
- [AMD vs Nvidia GPU: Which is better on Linux? (Reddit, 2023)](https://www.reddit.com/r/linux_gaming/comments/18nv50w/amd_vs_nvidia_gpu_which_is_better_on_linux_updated/)
- [NVIDIA vs AMD on Linux: Which GPU Should You Choose? (Linuxiac, 2025)](https://linuxiac.com/nvidia-vs-amd-gpus-on-linux/)
- [Open-Source NVIDIA Linux Driver Usage About To Become Much More Reliable (Phoronix, 2025)](https://www.phoronix.com/news/Nouveau-More-Reliable-Fix)
- [AMD Kernel Graphics Driver Exceeds 5.9 Million Lines In Linux 6.16 (Phoronix, 2025)](https://www.phoronix.com/news/Linux-6.16-AMDGPU-Driver-Size)
- [NVIDIA Posts Latest Linux Driver Patches For Open-Source vGPU Support (Phoronix, 2025)](https://www.phoronix.com/news/NVIDIA-vGPU-RFC-v2)
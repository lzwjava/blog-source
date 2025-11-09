---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Ghostty Emulador de Terminal Multiplataforma
translated: true
type: note
---

Sí, Ghostty está diseñado como un emulador de terminal multiplataforma, lo cual es de hecho uno de sus puntos fuertes—está construido para ejecutarse de manera consistente en múltiples sistemas operativos con alto rendimiento mediante aceleración por GPU e integración nativa de la interfaz de usuario. Sin embargo, a partir de octubre de 2025, su soporte completo está actualmente limitado a macOS y Linux, con Windows aún en etapas de planificación pero sin lanzar.

Respecto a la experiencia: No es *exactamente* idéntica en todas las plataformas porque Ghostty utiliza componentes nativos de la interfaz de usuario (por ejemplo, Cocoa en macOS, GTK en Linux) para sentirse idiomático e integrado en cada una—como una aplicación hecha a medida en lugar de un port genérico. Dicho esto, la funcionalidad central, las características (como pestañas, divisiones, búsqueda y protocolos de terminal avanzados), y el rendimiento están diseñados para ser muy similares y confiables en todos los lugares donde es compatible, minimizando las peculiaridades específicas de cada plataforma que podrías ver en emuladores menos pulidos.

Si Windows llega pronto (basado en las discusiones activas en GitHub), debería seguir el mismo enfoque nativo para una sensación fluida allí también.

[Características Oficiales de Ghostty](https://ghostty.org/docs/features)  
[Repositorio de Ghostty en GitHub](https://github.com/ghostty-org/ghostty)  
[Notas de Lanzamiento de Ghostty](https://ghostty.org/docs/install/release-notes)
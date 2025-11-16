---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: YourKit Profiler se integra a la perfección con IntelliJ
translated: true
type: note
---

Sí, YourKit Java Profiler se integra muy bien con IntelliJ IDEA (tanto en las ediciones Community como Ultimate), y es una de las experiencias de integración entre un profiler y un IDE más fluidas disponibles para Java.

Aquí están las características clave de integración sobre las que preguntaste:

- Lanzamiento directo desde IDEA  
  Una vez que instalas el plugin de YourKit (disponible en el JetBrains Marketplace o desde el propio plugin de YourKit), obtienes nuevas configuraciones de ejecución como "YourKit Snapshot", "YourKit Profiling (CPU)", "YourKit Profiling (Memory)", etc., justo al lado de tus botones normales de Run/Debug.

- Iniciar/detener la generación de perfiles directamente desde la barra de herramientas del IDE  
  Puedes iniciar la generación de perfiles con un clic, y detenerla + abrir automáticamente la instantánea capturada sin salir de IDEA.

- Clic en la interfaz de usuario del profiler → saltar instantáneamente al código fuente en IDEA  
  YourKit detecta que IDEA se está ejecutando y configura automáticamente la descompilación/navegación de código fuente. Cuando haces doble clic en cualquier método, stack frame, hotspot de asignación, etc., en la interfaz de usuario de YourKit, este abre la línea exacta en tu editor de IDEA (funciona incluso si solo tienes el bytecode, gracias al soporte integrado del descompilador).

- Instantánea de bienvenida al salir de la aplicación  
  Puedes configurar YourKit para que capture una instantánea automáticamente cuando tu aplicación termina, e IDEA la abrirá inmediatamente.

Estado actual (a partir de YourKit 2024.9, que es la última versión estable a finales de 2025):
- Soporte completo para IntelliJ IDEA 2023.3–2025.2+  
- Funciona perfectamente con Java 8–24 (incluyendo la generación de perfiles de virtual threads en Java 21+)  
- También soporta Kotlin, Scala, Groovy, etc., y salta al código fuente correcto.

Pasos de instalación (rápidos):
1. En IDEA → Settings → Plugins → Marketplace → busca "YourKit"
2. Instala/reinicia
3. El agente de YourKit viene incluido con el plugin, por lo que no se necesita una instalación separada de YourKit para el uso básico (aunque puedes instalar la aplicación completa independiente de YourKit si quieres la interfaz de usuario más completa fuera de IDEA).

La mayoría de los desarrolladores Java que usan YourKit a diario nunca salen de IDEA para la generación de perfiles una vez que este plugin está configurado.

Así que sí — exactamente el flujo de trabajo que describes funciona listo para usar y está muy pulido.
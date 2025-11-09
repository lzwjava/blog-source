---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: 'Ghostty: Emulador de Terminal Rápido y Multiplataforma'
translated: true
type: note
---

Ghostty es un emulador de terminal multiplataforma diseñado para velocidad, características e integración nativa en macOS y Linux (con soporte para Windows en desarrollo). Está construido principalmente en **Zig**, un lenguaje de programación de sistemas moderno centrado en la seguridad, el rendimiento y la simplicidad—no en Rust, como preguntaste.

### Detalles Claves de la Implementación
- **Arquitectura Central**: El núcleo compartido (que maneja la emulación de terminal, el renderizado y gran parte de la lógica) está escrito en Zig. Esto permite un control de bajo nivel y alto rendimiento, incluyendo aceleración por GPU mediante Metal (en macOS) o Vulkan/OpenGL (multiplataforma).
- **Capas Específicas por Plataforma**: Para lograr una sensación nativa, utiliza toolkits de plataforma para la GUI:
  - macOS: Swift/AppKit para la gestión de ventanas e interfaz de usuario.
  - Linux: GTK para la gestión de ventanas.
  - Una canalización de renderizado compartida en Zig lo une todo.
- **Características Notables de Su Diseño**:
  - Inicio y renderizado extremadamente rápidos (por ejemplo, maneja grandes salidas sin retraso).
  - Soporta ligaduras, emojis y tipografía avanzada.
  - Configurable mediante scripts Lua para extensibilidad.
  - Sin bloat—es minimalista pero incluye funciones esenciales como pestañas, búsqueda e integración del portapapeles OSC 52.
- **Filosofía de Desarrollo**: Creado por Mitchell Hashimoto (de HashiCorp), enfatiza la corrección y la eficiencia sobre los hacks de compatibilidad comunes en terminales antiguos como xterm. Es de código abierto bajo la licencia MIT.

Si estás interesado en construirlo o experimentar con él, consulta el repositorio de GitHub para el código base en Zig y las instrucciones de compilación (requiere Zig 0.13+).

### Referencias
- [Repositorio de Ghostty en GitHub](https://github.com/ghostty-org/ghostty)
- [Presentando Ghostty (Blog de Mitchell Hashimoto)](https://mitchellh.com/writing/ghostty-and-useful-zig-patterns)
- [Notas de la Versión Ghostty 1.0](https://dansasser.me/posts/ghostty-1-0-a-terminal-emulator-built-for-speed-features-and-native-integration/)
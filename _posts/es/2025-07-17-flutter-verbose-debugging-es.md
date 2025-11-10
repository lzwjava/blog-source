---
audio: false
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Guía de Depuración en Modo Verbose de Flutter
translated: true
type: note
---

Ah, entiendo 👍 — Sí, Flutter tiene un **modo verbose** que imprime *todo* lo que está haciendo internamente para que puedas ver dónde se queda colgado.

---

### ✅ Ejecutar comandos de `flutter` con registro verbose

Solo agrega la bandera `-v` (o `--verbose`):

- Para `flutter clean`:
  ```bash
  flutter clean -v
  ```

- Para obtener dependencias:
  ```bash
  flutter pub get -v
  ```

- Para ejecutar tu aplicación:
  ```bash
  flutter run -v
  ```

Esto volcará registros detallados (llamadas de red, eliminaciones de archivos, comandos de pod, etc.) a la terminal.

---

### 📌 Consejos para leer los registros verbose
- Mira las **últimas líneas** que se muestran antes de que deje de responder → eso te indica en qué paso se está colgando.
- Los bloqueos suelen ocurrir durante:
  - La resolución de **CocoaPods** (red lenta / repositorio desactualizado).
  - La sincronización de **Gradle** (en la compilación de Android).
  - Permisos (si Flutter no tiene acceso a algunos directorios).

---

👉 Si `flutter clean -v` aún parece estar atascado, pega aquí las últimas ~20 líneas que imprima ⬇️, y puedo ayudarte a analizar exactamente dónde se está colgando.

¿Quieres que te escriba un **script de limpieza rápido con verbosidad** para que puedas ejecutar `./super_clean.sh` en lugar de escribir cada comando?
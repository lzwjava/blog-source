---
audio: false
generated: true
lang: es
layout: post
title: Actualización de VSCode mediante Snap en Ubuntu
translated: true
type: note
---

Para actualizar Visual Studio Code (VSCode) instalado mediante Snap en Ubuntu, sigue estos pasos:

1. **Abre una terminal**: Puedes hacerlo presionando `Ctrl + Alt + T`.

2. **Verifica las actualizaciones**: Snap verifica automáticamente las actualizaciones en segundo plano, pero puedes activar una verificación manual ejecutando:
   ```bash
   sudo snap refresh
   ```

3. **Actualiza VSCode**: Si hay una versión más reciente de VSCode disponible, el comando `snap refresh` la descargará e instalará. Verás una salida que indica el progreso, como:
   ```
   code 1.85.2 from Visual Studio Code (code✓) refreshed
   ```
   Si no hay actualizaciones disponibles, dirá:
   ```
   All snaps up to date.
   ```

4. **Verifica la actualización**: Para confirmar la versión instalada de VSCode, ejecuta:
   ```bash
   code --version
   ```
   Esto mostrará la versión actual de VSCode.

### Notas:
- **Actualizaciones automáticas**: Los paquetes Snap, incluido VSCode, normalmente se actualizan automáticamente en segundo plano. Por lo general, no necesitas intervenir manualmente a menos que quieras forzar una actualización.
- **Privilegios de root**: El comando `sudo` es necesario para las operaciones de Snap a nivel del sistema.
- **Verifica el estado de Snap**: Si quieres ver qué paquetes Snap están instalados y sus versiones, usa:
   ```bash
   snap list
   ```
- **Solución de problemas**: Si la actualización falla, asegúrate de que tu conexión a internet sea estable y de que el daemon de Snap esté en ejecución (`sudo systemctl status snapd`). También puedes intentar actualizar los metadatos de Snap con:
   ```bash
   sudo snap refresh --list
   ```

Este proceso asegura que VSCode se mantenga actualizado con la última versión disponible en la Snap store.
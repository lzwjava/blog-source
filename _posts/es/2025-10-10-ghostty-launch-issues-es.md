---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Problemas de Instalación y Ejecución de Ghostty
translated: true
type: note
---

### Diagnóstico del problema

Según los registros que compartiste, la instalación de Ghostty 1.1.3 mediante el paquete `.deb` fue exitosa, pero su ejecución falla por dos razones principales:

1.  **Error en el Argumento de la CLI**: El comando `ghostty .` trata el `.` como un campo de configuración inválido (probablemente se intentó usar como un directorio, pero Ghostty no soporta esa sintaxis). Esto causa la salida inmediata con "invalid field".

2.  **Problema de Compatibilidad OpenGL/GTK**: Al ejecutar `ghostty` sin argumentos, se inicia pero se cierra inesperadamente debido a que "la versión de OpenGL es demasiado antigua. Ghostty requiere OpenGL 3.3" (tu sistema reporta 3.2 a Ghostty). Este es un problema conocido en Ubuntu 22.04, especialmente con controladores NVIDIA bajo X11. A pesar de que `glxinfo` a menudo muestra OpenGL 4.6+, el entorno de ejecución GTK 4.6 de Ghostty no puede acceder correctamente a versiones superiores con NVIDIA GL. La advertencia "GDK_DEBUG=vulkan-disable" es un intento de solución que no resuelve el problema central. El error final Gtk-CRITICAL es un síntoma de la falla en la realización de la superficie.

Esto afecta a muchos usuarios en Ubuntu 22.04 (y derivados como Pop!_OS) debido a la versión más antigua de GTK (4.6 vs. la más nueva 4.12+ necesaria para la compatibilidad completa con NVIDIA).

### Comprobaciones Rápidas
- Verifica tu soporte real de OpenGL (instala `mesa-utils` si es necesario: `sudo apt install mesa-utils`):
  ```
  glxinfo | grep "OpenGL version"
  ```
  Si reporta 3.3 o superior, el problema es específico de GTK/NVIDIA.
- Comprueba tu tipo de sesión: `echo $XDG_SESSION_TYPE`. Si es `x11`, es probable que esté contribuyendo al problema.

### Soluciones
Aquí tienes soluciones paso a paso, comenzando por la más simple:

1.  **Cambiar a Wayland (si tienes gráficos híbridos, ej. Intel + NVIDIA)**:
    - Cierra sesión y selecciona una sesión Wayland en el inicio de sesión (o añade `WaylandEnable=true` a `/etc/gdm3/custom.conf` y reinicia GDM).
    - Ejecuta Ghostty con los gráficos integrados: `prime-run --gpu intel ghostty` (instala `nvidia-prime` si es necesario).
    - Esto evita los problemas de NVIDIA X11 para algunos usuarios.

2.  **Instalar mediante Snap (Paquete Alternativo Más Sencillo)**:
    - El `.deb` no oficial que usaste puede heredar peculiaridades del sistema. Prueba el Snap oficial, que incluye las dependencias:
      ```
      sudo snap install ghostty --classic
      ```
    - Inícialo con `snap run ghostty`. Si OpenGL sigue fallando, procede con las actualizaciones.

3.  **Actualizar Ubuntu a 24.04 (Recomendado para una Solución a Largo Plazo)**:
    - Ubuntu 24.04 incluye GTK 4.14+, resolviendo la compatibilidad con NVIDIA.
    - Sigue la guía oficial de actualización: `sudo do-release-upgrade`.
    - Después de actualizar, reinstala Ghostty mediante el mismo `.deb` o Snap. Los usuarios reportan que funciona perfectamente después de la actualización.

4.  **Compilar desde el Código Fuente con Backend GLFW (Solución Temporal)**:
    - Esto utiliza un entorno de ejecución no-GTK para evitar el problema de OpenGL (nota: carece de pestañas, solo para pruebas).
      ```
      sudo apt install git zig libgtk-4-dev libadwaita-1-dev libharfbuzz-dev libpango1.0-dev libcairo2-dev libgdk-pixbuf-2.0-dev libglib2.0-dev libwayland-dev libxkbcommon-dev libinput-dev libudev-dev libseat-dev libpipewire-0.3-dev libsystemd-dev libx11-dev libxext-dev libxfixes-dev libxi-dev libxrandr-dev libxtst-dev libxdamage-dev libxcomposite-dev libxrender-dev libxcursor-dev libxinerama-dev libxss-dev libxv-dev libxxf86vm-dev libgl1-mesa-dev libegl1-mesa-dev libgles2-mesa-dev libgbm-dev libdrm-dev libvulkan-dev libclang-dev
      git clone https://github.com/ghostty-org/ghostty.git
      cd ghostty
      zig build -Doptimize=ReleaseFast -Dapp-runtime=glfw
      sudo cp zig-out/bin/ghostty /usr/local/bin/
      ```
    - Ejecuta `ghostty`. Para todas las funciones, vuelve a cambiar a GTK una vez que hayas actualizado el sistema.

### Consejos Adicionales
- Actualiza tus controladores NVIDIA: `sudo ubuntu-drivers autoinstall` (o usa la serie 550+ manualmente).
- Si estás usando solo AMD/Intel, asegúrate de que Mesa esté actualizado: `sudo apt update && sudo apt upgrade mesa-vulkan-drivers`.
- Para la advertencia de configuración en tu archivo de plantilla (`~/.config/ghostty/config`), edítalo para eliminar cualquier línea inválida (ej., un `.` suelto).

Si nada de esto funciona, comparte la salida de tu `glxinfo` o los detalles de tu GPU (`lspci | grep VGA`) para un consejo más específico.

[Discusión sobre OpenGL Demasiado Antiguo](https://github.com/ghostty-org/ghostty/discussions/3159)  
[Compilaciones de Ghostty para Ubuntu](https://github.com/mkasberg/ghostty-ubuntu)  
[Snap de Ghostty](https://snapcraft.io/ghostty)
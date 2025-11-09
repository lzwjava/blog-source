---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Resolución de Conflicto de Versión GLIBC en Ghostty
translated: true
type: note
---

El problema que estás experimentando no se trata solo de instalaciones conflictivas—es principalmente que tanto el Snap como el `.deb` que descargaste fueron compilados contra GLIBC 2.38 (de Ubuntu 24.04), pero tu sistema está en Ubuntu 22.04 (basado en la versión GLIBC 2.35 de tu paquete `libc-bin`). Esto provoca el error "version `GLIBC_2.38' not found" al intentar ejecutar el binario. Tener ambas instalaciones activas también puede generar conflictos de ruta (por ejemplo, qué binario `ghostty` se ejecuta), así que sí, primero deberías eliminarlas para limpiar el entorno.

### Paso 1: Eliminar las instalaciones existentes
Ejecuta estos comandos para desinstalar ambas:
```
sudo snap remove ghostty
sudo apt remove ghostty
```
- Esto eliminará la versión Snap y la versión `.deb` sin afectar tu sistema de otra manera.
- Verifica la eliminación con `which ghostty` (no debería devolver nada) y `snap list | grep ghostty` (debería estar vacío).

### Paso 2: Instalar una versión compatible
Ghostty no tiene paquetes `.deb` oficiales para Ubuntu 22.04 todavía, pero hay un repositorio no oficial confiable que compila archivos `.deb` compatibles para esta versión (y otras). Maneja la compatibilidad con GLIBC automáticamente.

La forma más fácil es usar su script de instalación automática, que detecta tu versión de Ubuntu y obtiene el paquete correcto:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/mkasberg/ghostty-ubuntu/HEAD/install.sh)"
```
- Esto descarga e instala el último `.deb` compatible (actualmente alrededor de la v1.2.x en lanzamientos recientes).
- Después de que termine, ejecuta `ghostty` para probar—debería iniciarse sin el error de GLIBC.
- Si ves algún mensaje sobre dependencias durante la instalación (por ejemplo, para `libonig5`), simplemente apruebalos con `Y`.

Si prefieres la instalación manual:
1. Ve a la [página de lanzamientos](https://github.com/mkasberg/ghostty-ubuntu/releases).
2. Descarga el archivo `.deb` etiquetado para Ubuntu 22.04 (por ejemplo, algo como `ghostty_1.2.1-0.ppa1_amd64_22.04.deb`—el nombre exacto varía según el lanzamiento).
3. Instálalo con `sudo dpkg -i ghostty_*.deb` (ejecuta desde la carpeta de descargas).
4. Si se queja de dependencias faltantes, corrígelo con `sudo apt install -f`.

### Notas adicionales
- **Por qué no es necesario compilar desde el código fuente aquí**: El repositorio no oficial hace el trabajo pesado por ti, pero si quieres compilar Ghostty tú mismo (por ejemplo, para una versión personalizada), sigue la [guía de compilación oficial desde el código fuente](https://ghostty.org/docs/install/build). Requiere Zig 0.13 y algunas dependencias como `libgtk-4-dev`, pero la ruta del `.deb` es más simple.
- **¿Actualizando Ubuntu?** Si estás abierto a la idea, pasar a 24.04 te permitiría usar el Snap oficial o el `.deb` para 24.04 que probaste antes, sin problemas.
- Después de la instalación, puedes configurar Ghostty mediante `~/.config/ghostty/config` (consulta la [documentación](https://ghostty.org/docs/config) para ver las opciones).

¡Si encuentras algún error durante estos pasas, pega la salida aquí para obtener más ayuda!
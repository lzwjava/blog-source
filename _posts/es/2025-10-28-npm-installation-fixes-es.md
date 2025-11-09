---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Soluciones para Errores de Instalación de npm
translated: true
type: note
---

### Comprender el Error

Se trata de un fallo de instalación de npm durante una actualización (o instalación) global del paquete `@anthropic-ai/claude-code`. El problema clave está en la fase "reify", donde npm intenta "retirar" (hacer una copia de seguridad) del directorio existente del paquete antes de instalar la nueva versión. Específicamente:

- npm está intentando renombrar `/usr/lib/node_modules/@anthropic-ai/claude-code` a una copia de seguridad temporal como `/usr/lib/node_modules/@anthropic-ai/.claude-code-ZjqcDZyQ`.
- Esto falla con `ENOTEMPTY: directory not empty` (errno -39), que típicamente ocurre cuando:
  - El directorio fuente contiene archivos/subdirectorios que están bloqueados, en uso o tienen problemas de permisos.
  - Hay enlaces simbólicos rotos, manejadores de archivos abiertos (por ejemplo, de un proceso `claude` en ejecución) o peculiaridades del sistema de archivos en Linux.
  - Raramente, la lógica interna de mover archivos de npm encuentra una condición de carrera.

Tu configuración:
- Node: v22.18.0
- npm: v11.6.1
- SO: Linux 6.14.0-29-generic (probablemente Ubuntu/Debian)
- Ejecutándose como root (basado en la ruta del log `/root/.npm/_logs/`), por lo que los permisos no son la causa principal.
- Directorio de trabajo: `/home/lzwjava/projects/blog-source` (pero esto es una instalación global, por lo que es irrelevante).

El paquete parece ser la herramienta Claude Code de Anthropic (CLI para asistencia de codificación con IA), y la línea 73 muestra una advertencia de desajuste de dependencia para `@img/sharp-libvips-linux-x64`, pero eso no está relacionado con el fallo.

### Soluciones Rápidas (Probar en Orden)

1. **Detener Cualquier Proceso en Ejecución**:
   - Termina cualquier proceso de la CLI `claude` o procesos relacionados: `pkill claude` (o `ps aux | grep claude` para encontrar los PIDs, luego `kill <PID>`).
   - Cierra terminales/IDEs que estén usando el paquete.

2. **Limpiar Manualmente el Directorio**:
   - Elimina el paquete y el binario existentes:
     ```
     sudo rm -rf /usr/lib/node_modules/@anthropic-ai/claude-code
     sudo rm -f /usr/bin/claude
     ```
   - Esto evita el paso de copia de seguridad de npm. Luego reintenta la instalación:
     ```
     sudo npm install -g @anthropic-ai/claude-code
     ```

3. **Limpiar la Caché de npm y Reintentar**:
   - Ejecuta:
     ```
     sudo npm cache clean --force
     sudo npm install -g @anthropic-ai/claude-code
     ```
   - Si persiste, añade `--no-optional` para omitir dependencias opcionales como la librería de imágenes Sharp.

4. **Alternativa: Usar npx o Evitar la Instalación Global**:
   - Si no lo necesitas globalmente, instálalo localmente en tu proyecto: `npm install @anthropic-ai/claude-code` (luego ejecuta vía `npx claude`).
   - O usa Yarn: `sudo yarn global add @anthropic-ai/claude-code` (Yarn a veces maneja los movimientos de forma diferente).

5. **Si el Problema Persiste**:
   - Comprueba si hay problemas del sistema de archivos: `ls -la /usr/lib/node_modules/@anthropic-ai/` (busca enlaces simbólicos extraños o bloqueos).
   - Haz un downgrade de npm temporalmente: `sudo npm install -g npm@10` (la v11 tiene erroes ocasionales de reify; revierte después).
   - Log completo: Revisa `/root/.npm/_logs/2025-10-27T16_10_10_534Z-debug-0.log` para más pistas.

Esto debería resolverlo—las instalaciones globales de npm en Linux pueden ser complicadas con los renombrados. Si compartes el comando exacto que ejecutaste o más contexto del log, puedo refinar esto.
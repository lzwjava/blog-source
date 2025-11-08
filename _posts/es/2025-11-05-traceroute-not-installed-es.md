---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Traceroute No Instalado Por Defecto
translated: true
type: note
---

Traceroute definitivamente está disponible en Linux—es una herramienta estándar de diagnóstico de red que rastrea la ruta que toman los paquetes hacia un destino. Sin embargo, **frecuentemente no viene instalado por defecto** en muchas distribuciones modernas (como Ubuntu, Fedora o instalaciones mínimas de Debian) para mantener los sistemas base livianos. Por eso no aparece en tu autocompletado de "trac".

### Solución Rápida
Instálalo mediante tu gestor de paquetes:
- **Debian/Ubuntu**: `sudo apt update && sudo apt install traceroute`
- **Fedora/RHEL/CentOS**: `sudo dnf install traceroute` (o `sudo yum install traceroute` en versiones antiguas)
- **Arch**: `sudo pacman -S traceroute`

Una vez instalado, escribir `trac` + Tab ahora debería incluir `traceroute` en la lista. Luego puedes ejecutarlo como `traceroute example.com` para probar.

Si estás en una configuración containerizada o súper mínima (por ejemplo, Alpine Linux), podría usar `tr` como un alias o requerir un paquete diferente—¡avísame tu distribución para más detalles específicos!
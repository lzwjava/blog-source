---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Editores de texto predeterminados en RHEL minimal
translated: true
type: note
---

En Red Hat Enterprise Linux (RHEL), particularmente en una instalación mínima (la predeterminada para servidores y configuraciones ligeras), el único editor de texto disponible inmediatamente es **vi**, proporcionado por el paquete `vim-minimal`. Esto te brinda una implementación básica y compatible del comando clásico `vi` para editar archivos en la terminal.

- **`vim` completo** (la versión mejorada con más características, resaltado de sintaxis, etc.) no se instala por defecto. Puedes agregarlo con `sudo dnf install vim-enhanced`.
- **Nano** y **Emacs** no están incluidos en la instalación mínima. Están disponibles en los repositorios pero requieren una instalación explícita:
  - Para Nano: `sudo dnf install nano`
  - Para Emacs: `sudo dnf install emacs`

Esto mantiene la instalación mínima ligera (alrededor de 200-300 paquetes en total) para priorizar la seguridad y el rendimiento. Si estás realizando una instalación de escritorio o servidor completa (no mínima), se podrían incluir más herramientas dependiendo del entorno seleccionado.

[Getting started with Nano (Red Hat)](https://www.redhat.com/en/blog/getting-started-nano)  
[Why RHEL has two vim installed by default?](https://unix.stackexchange.com/questions/699071/why-rhel-has-two-vim-installed-by-default)  
[RHEL 9 Package Manifest](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/package_manifest/index)
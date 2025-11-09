---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Guía de Configuración del Shell Ghostty
translated: true
type: note
---

### Ghostty y .bashrc en Ubuntu

Ghostty se comporta de manera similar a la Terminal GNOME predeterminada en Ubuntu (y otras distribuciones de Linux) en lo que respecta a cargar `.bashrc`. Por defecto, Ghostty inicia **shells interactivos no login** para bash, lo que significa que carga directamente `~/.bashrc`, al igual que la Terminal GNOME. Este es el comportamiento estándar para la mayoría de las terminales de Linux, donde `.bashrc` maneja la configuración del shell interactivo (por ejemplo, alias, prompts, variables de entorno para sesiones no login).

#### Cómo carga .bashrc
- Cuando abres una nueva ventana o pestaña de Ghostty, ejecuta `bash` (o tu shell predeterminado) como un shell no login.
- Bash verifica y carga `~/.bashrc` si el shell es interactivo (que lo es por defecto).
- Si tienes un `~/.bash_profile` (típicamente para shells login), no se cargará a menos que configures explícitamente Ghostty para iniciar un shell login (por ejemplo, añadiendo `initial-command = bash --login` a `~/.config/ghostty/config`).
- Problemas potenciales: Algunos usuarios reportan que `.bashrc` no se carga en el primer lanzamiento para usuarios nuevos o en configuraciones específicas (por ejemplo, sesiones SSH remotas en Ubuntu). Esto a menudo se puede solucionar asegurándose de que no exista un `~/.bash_profile` conflictivo, o cargándolo manualmente en tu configuración. Añadir una guarda en `.bashrc` como `[[ $- != *i* ]] && return` puede prevenir problemas en contextos no interactivos.

En resumen, sí: Ghostty es igual a la Terminal predeterminada en el uso de `.bashrc` en Ubuntu, con el mismo valor predeterminado de shell no login.

### Ghostty en macOS: ¿.zprofile o .bash_profile?

En macOS, Ghostty sigue la tradición de la plataforma (como Terminal.app) e inicia **shells login** por defecto, independientemente del shell. Esto afecta a qué perfil se carga:

- **Si usas zsh (predeterminado en macOS desde Catalina)**: Carga `~/.zprofile` (para configuración login) *y* `~/.zshrc` (para configuración interactiva) cada vez que se abre una nueva terminal.
- **Si usas bash**: Carga `~/.bash_profile` (shell login). Bash no cargará `~/.bashrc` directamente aquí; `~/.bashrc` es solo para shells interactivos no login. Para incluir el contenido de `.bashrc`, añade esto a tu `~/.bash_profile`:
  ```
  if [ -f ~/.bashrc ]; then . ~/.bashrc; fi
  ```

Por lo tanto, carga `~/.zprofile` para la configuración predeterminada de zsh, o `~/.bash_profile` si estás usando bash. Puedes cambiar de shell o ajustar la configuración de Ghostty si es necesario.

[Shell Integration - Ghostty](https://ghostty.org/docs/features/shell-integration)  
[macOS Login Shells - Ghostty](https://ghostty.org/docs/help/macos-login-shells)  
[Potential bug, .bashrc not read on startup - GitHub Discussion](https://github.com/ghostty-org/ghostty/discussions/3437)  
[Bash Startup Files - GNU Manual](https://www.gnu.org/software/bash/manual/bash.html#Bash-Startup-Files)
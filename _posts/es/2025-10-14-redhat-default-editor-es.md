---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Editor de Texto Predeterminado de Red Hat Enterprise Linux
translated: true
type: note
---

### Editor de texto predeterminado en Red Hat Enterprise Linux

En Red Hat Enterprise Linux (RHEL), el editor de texto predeterminado es **Vi** (frecuentemente configurado como un alias de **Vim**, que significa "Vi IMproved"). Vi es un editor de texto modal basado en línea de comandos que ha sido el estándar en sistemas tipo Unix desde la década de 1970. Es ligero, ubicuo y viene preinstalado en la mayoría de los sistemas RHEL a través del paquete `vim-minimal` o `vim-enhanced`.

#### ¿Por qué Vi/Vim?
- Es eficiente para entornos de servidor donde los editores con interfaz gráfica no son prácticos.
- Los comandos se basan en el teclado: modo de inserción para escribir (`i`) y modo de comando para editar (por ejemplo, `dd` para eliminar una línea, `:wq` para guardar y salir).
- Si eres nuevo en él, tiene una curva de aprendizaje, pero es muy potente una vez que se domina.

#### Cómo verificarlo y usarlo
- Ejecuta `vi nombre_de_archivo.txt` (o `vim nombre_de_archivo.txt`) para abrir un archivo.
- Para verificar tu editor predeterminado actual: `echo $EDITOR` (normalmente muestra `/usr/bin/vi`).
- Si prefieres otra opción (como Emacs, de tu consulta anterior), configúralo con `export EDITOR=emacs` en tu archivo `~/.bashrc`.

Para comenzar rápidamente, escribe `vimtutor` para iniciar un tutorial interactivo.

[Cómo empezar a usar el editor Vi - Red Hat](https://www.redhat.com/en/blog/get-started-vi-editor)  
[Habilidades en Linux: 9 tutoriales para sacarle más provecho a tu editor de texto - Red Hat](https://www.redhat.com/en/blog/text-editor-roundup-2022)
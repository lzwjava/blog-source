---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Instalación de Emacs en RHEL
translated: true
type: note
---

### Instalación de Emacs en Red Hat Enterprise Linux

Red Hat Enterprise Linux (RHEL) utiliza principalmente el gestor de paquetes DNF para instalar software. Emacs está disponible en los repositorios predeterminados, por lo que la instalación es sencilla. A continuación se detallan los pasos para versiones modernas (RHEL 8 y posteriores). Para versiones anteriores (por ejemplo, RHEL 7), reemplace `dnf` con `yum`.

#### Prerrequisitos
- Asegúrese de tener privilegios de root (use `sudo`).
- Su sistema debe estar registrado con Red Hat Subscription Management si utiliza los repositorios oficiales de RHEL.

#### Pasos de instalación
1.  **Actualice la caché de paquetes** (recomendado para asegurarse de obtener la última versión disponible):  
    ```
    sudo dnf update
    ```

2.  **Instale Emacs**:  
    ```
    sudo dnf install emacs
    ```  
    Esto instalará la última versión estable disponible en los repositorios (por ejemplo, Emacs 28.x o 29.x, dependiendo de su versión de RHEL).

3.  **Verifique la instalación**:  
    Ejecute lo siguiente para comprobar la versión:  
    ```
    emacs --version
    ```  
    Debería ver una salida similar a `GNU Emacs 28.2` (o similar).

#### Notas
- Si está en una versión anterior de RHEL que usa YUM (por ejemplo, RHEL 7), el comando es `sudo yum install emacs`.
- Para obtener la última versión absoluta de Emacs (por ejemplo, 29+), es posible que necesite compilar desde el código fuente o usar repositorios de terceros como EPEL, ya que los repositorios base pueden ir con retraso.
- Para iniciar Emacs, simplemente escriba `emacs` en la terminal.

[Preguntas frecuentes de GNU Emacs: Instalación de Emacs](https://www.gnu.org/software/emacs/manual/html_node/efaq/Installing-Emacs.html)  
[Documentación de Red Hat: Gestión de software con DNF](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/managing_software_with_the_dnf_tool/index)
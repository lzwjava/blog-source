---
audio: false
generated: true
lang: es
layout: post
title: Instalar Go mediante APT en Debian
translated: true
type: note
---

Para instalar Go usando `apt` en un sistemas Linux basados en Debian (por ejemplo, Ubuntu), sigue estos pasos. Ten en cuenta que `apt` puede instalar una versión anterior de Go (por ejemplo, 1.18 en Ubuntu 22.04), por lo que debes verificar si cumple con los requisitos de tu proyecto (comprueba el archivo `go.mod` en `~/Projects/clash-core` para ver la versión de Go requerida).

### Pasos para Instalar Go Usando APT

1.  **Actualizar el Índice de Paquetes**
    - Asegúrate de que tus listas de paquetes estén actualizadas:
      ```bash
      sudo apt update
      ```

2.  **Instalar Go**
    - Instala el paquete de Go:
      ```bash
      sudo apt install golang-go
      ```
    - Esto instala el compilador de Go, las herramientas y la librería estándar.

3.  **Verificar la Instalación**
    - Comprueba la versión de Go instalada:
      ```bash
      go version
      ```
    - Deberías ver una salida similar a:
      ```
      go version go1.18.1 linux/amd64
      ```
      (La versión depende del repositorio de paquetes de tu distribución).

4.  **Configurar GOPATH (Opcional)**
    - Las versiones modernas de Go (1.13+) usan módulos, por lo que `GOPATH` es opcional, pero configurarlo puede ser útil para algunos proyectos.
    - Edita el perfil de tu shell (por ejemplo, `~/.bashrc` o `~/.zshrc`):
      ```bash
      nano ~/.bashrc
      ```
    - Añade lo siguiente:
      ```bash
      export GOPATH=$HOME/go
      export PATH=$PATH:$GOPATH/bin
      ```
    - Guarda y recarga la configuración del shell:
      ```bash
      source ~/.bashrc
      ```

5.  **Reintentar la Compilación**
    - Navega a tu directorio de proyecto:
      ```bash
      cd ~/Projects/clash-core
      ```
    - Ejecuta el comando `make` nuevamente:
      ```bash
      make
      ```

### Notas
-   **Comprobación de Versión**: Si tu proyecto requiere una versión más nueva de Go (por ejemplo, 1.20 o superior), la versión de `apt` podría estar desactualizada. Comprueba la versión requerida en `go.mod` o en la documentación del proyecto. Si es necesario, instala una versión más nueva manualmente descargando el tarball desde [https://go.dev/dl/](https://go.dev/dl/) (como se describe en la respuesta anterior).
-   **Repositorios Alternativos**: Para una versión más nueva a través de `apt`, puedes añadir un PPA de terceros (por ejemplo, `ppa:longsleep/golang-backports` en Ubuntu). Ejecuta:
    ```bash
    sudo add-apt-repository ppa:longsleep/golang-backports
    sudo apt update
    sudo apt install golang-go
    ```
-   **Solución de Problemas**:
    - Si `go` no se encuentra, asegúrate de que `/usr/bin/go` exista (`ls /usr/bin/go`). Si no es así, reinstala con `sudo apt install --reinstall golang-go`.
    - Si obtienes errores de dependencias, ejecuta `sudo apt install -f` para corregirlos.
    - Para problemas de permisos, asegúrate de tener privilegios de `sudo`.

### Fuentes
-   Guía de instalación de Go en Ubuntu: [https://ubuntu.com/server/docs/programming-go](https://ubuntu.com/server/docs/programming-go)
-   Uso general de apt: [https://help.ubuntu.com/community/AptGet/Howto](https://help.ubuntu.com/community/AptGet/Howto)

Si la versión instalada es demasiado antigua o encuentras problemas, ¡avísame tu distribución de Linux (por ejemplo, Ubuntu 22.04) y la versión de Go requerida, y te guiaré más!
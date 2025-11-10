---
audio: false
generated: true
lang: es
layout: post
title: Instalar GitHub CLI
translated: true
type: note
---

Para instalar GitHub CLI (`gh`) en Ubuntu y usarlo para activar flujos de trabajo de GitHub Actions con el comando `gh workflow run`, sigue estos pasos:

### Pasos de instalación para GitHub CLI (`gh`) en Ubuntu

1.  **Añadir el repositorio de GitHub CLI y la clave GPG**:
    Ejecuta los siguientes comandos en tu terminal para configurar el repositorio oficial de paquetes de GitHub CLI:

    ```bash
    (type -p wget >/dev/null || (sudo apt update && sudo apt-get install wget -y)) \
    && sudo mkdir -p -m 755 /etc/apt/keyrings \
    && wget -qO- https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null \
    && sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
    ```

    Este script:
    - Instala `wget` si no está presente.
    - Crea un directorio para los anillos de claves de APT.
    - Descarga y añade la clave GPG de GitHub CLI.
    - Configura el repositorio de GitHub CLI para tu sistema.

2.  **Actualizar el índice de paquetes e instalar `gh`**:
    Actualiza tu lista de paquetes e instala la herramienta de línea de comandos `gh`:

    ```bash
    sudo apt update
    sudo apt install gh -y
    ```

3.  **Verificar la instalación**:
    Comprueba que `gh` se instaló correctamente ejecutando:

    ```bash
    gh --version
    ```

    Deberías ver una salida como `gh version X.Y.Z (YYYY-MM-DD)`, lo que confirma la instalación.

4.  **Autenticarse con GitHub**:
    Antes de usar `gh`, autentícate con tu cuenta de GitHub:

    ```bash
    gh auth login
    ```

    Sigue las indicaciones:
    - Elige `GitHub.com` (o tu servidor empresarial si es aplicable).
    - Selecciona tu protocolo preferido (`HTTPS` o `SSH`; `SSH` es recomendable si tienes una clave SSH configurada).
    - Elige el método de autenticación (el navegador es el más fácil; abre una página web para iniciar sesión).
    - Copia el código de un solo uso proporcionado, pégalo en el navegador y autoriza `gh`.
    - Confirma la configuración predeterminada o ajústala según sea necesario.

    Después de una autenticación exitosa, verás un mensaje de confirmación.

### Usar `gh workflow run` para GitHub Actions

El comando `gh workflow run` activa un flujo de trabajo de GitHub Actions. Así es cómo usarlo:

1.  **Navega a tu repositorio** (opcional):
    Si estás en un repositorio Git local vinculado a GitHub, `gh` lo detectará automáticamente. De lo contrario, especifica el repositorio con el flag `--repo`.

2.  **Listar flujos de trabajo disponibles** (opcional):
    Para encontrar el ID o el nombre del archivo del flujo de trabajo, ejecuta:

    ```bash
    gh workflow list
    ```

    Esto muestra todos los flujos de trabajo en el repositorio, mostrando sus nombres, IDs y estados (ej., `active`).

3.  **Ejecutar un flujo de trabajo**:
    Usa el comando `gh workflow run` con el nombre del archivo o el ID del flujo de trabajo. Por ejemplo:

    ```bash
    gh workflow run workflow.yml
    ```

    O, usando el ID del flujo de trabajo (ej., `123456`):

    ```bash
    gh workflow run 123456
    ```

    Si el flujo de trabajo acepta inputs, proporciónalos con el flag `--field`:

    ```bash
    gh workflow run workflow.yml --field key=value
    ```

    Para especificar una rama o ref, usa el flag `--ref`:

    ```bash
    gh workflow run workflow.yml --ref nombre-de-la-rama
    ```

4.  **Monitorizar el flujo de trabajo**:
    Después de activarlo, comprueba el estado de la ejecución:

    ```bash
    gh run list
    ```

    Para observar una ejecución específica en tiempo real, usa:

    ```bash
    gh run watch <run-id>
    ```

    Reemplaza `<run-id>` con el ID de ejecución de `gh run list`.

### Consejos para Solucionar Problemas

-   **Errores de firma GPG**: Si encuentras problemas relacionados con GPG durante `apt update`, consulta el rastreador de problemas de GitHub para buscar soluciones (ej., `cli/cli#9569`) o reintenta el paso de importación de la clave.[](https://github.com/cli/cli/blob/trunk/docs/install_linux.md)
-   **Problemas de firewall**: Si `keyserver.ubuntu.com` falla, intenta:

    ```bash
    sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-key C99B11DEB97541F0
    ```

    O instala `dirmngr` si es necesario:

    ```bash
    sudo apt-get install dirmngr
    ```

   [](https://gist.github.com/Manoj-Paramsetti/dc957bdd6a4430275d0fc28a0dc43ae9)
-   **Advertencia sobre la instalación Snap**: GitHub desaconseja usar el paquete Snap para `gh` debido a problemas en tiempo de ejecución. Usa el método APT descrito anteriormente.[](https://github.com/cli/cli/blob/trunk/docs/install_linux.md)
-   **Ámbitos de autenticación**: Si `gh workflow run` falla debido a permisos, asegúrate de que tu token tenga el ámbito `workflow`. Vuelve a autenticarte con:

    ```bash
    gh auth refresh -s workflow
    ```

### Notas Adicionales

-   **Manual de GitHub CLI**: Para más detalles sobre los comandos de `gh`, ejecuta `gh help` o visita el manual oficial en [cli.github.com](https://cli.github.com).[](https://cli.github.com/manual/)
-   **Requisitos del flujo de trabajo**: Asegúrate de que el archivo del flujo de trabajo (ej., `workflow.yml`) exista en el directorio `.github/workflows/` de tu repositorio y esté configurado para activadores manuales (ej., evento `workflow_dispatch`).
-   **Métodos de instalación alternativos**: También puedes instalar `gh` via Homebrew (`brew install gh`) o descargando binarios de la [página de lanzamientos](https://github.com/cli/cli/releases), pero el método APT es el recomendado para Ubuntu.[](https://github.com/cli/cli)

Esta configuración te permite gestionar eficientemente los flujos de trabajo de GitHub Actions desde la línea de comandos en Ubuntu. ¡Avísame si necesitas ayuda con comandos específicos de `gh` o configuraciones de flujos de trabajo!
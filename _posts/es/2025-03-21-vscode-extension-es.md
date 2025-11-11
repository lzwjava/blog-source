---
audio: false
generated: true
lang: es
layout: post
title: Solución de Problemas de Instalación de Extensiones de VSCode con Proxy
translated: true
type: note
---

Para verificar el registro de instalación de extensiones en Visual Studio Code (VSCode) o usar la línea de comandos para instalar una extensión con `code --install-extension` y ver el registro—especialmente si sospechas de un problema de proxy—aquí puedes proceder:

---

### Usar la Línea de Comandos con `code --install-extension`
Puedes instalar extensiones mediante la línea de comandos y obtener cierta visibilidad del proceso, lo que puede ayudar a diagnosticar problemas de proxy.

1.  **Instalar con Salida Detallada**
    Ejecuta el siguiente comando para instalar una extensión y ver una salida más detallada:
    ```bash
    code --install-extension <id-de-la-extensión> --verbose
    ```
    -   Reemplaza `<id-de-la-extensión>` con el ID de la extensión (por ejemplo, `vscodevim.vim`).
    -   La bandera `--verbose` aumenta el detalle de la salida, mostrando el progreso y posibles errores, como problemas de proxy o de red.

2.  **Manejar Problemas de Proxy**
    Si estás detrás de un proxy, podría interferir con la instalación. Prueba estos enfoques:
    -   **Establecer Variables de Entorno del Proxy**:
        Antes de ejecutar el comando, configura los ajustes del proxy:
        ```bash
        export HTTP_PROXY=http://tu-servidor-proxy:puerto
        export HTTPS_PROXY=http://tu-servidor-proxy:puerto
        code --install-extension <id-de-la-extensión>
        ```
        -   En Windows, usa `set` en lugar de `export`:
            ```cmd
            set HTTP_PROXY=http://tu-servidor-proxy:puerto
            set HTTPS_PROXY=http://tu-servidor-proxy:puerto
            code --install-extension <id-de-la-extensión>
            ```
    -   **Especificar el Proxy Directamente**:
        Usa la bandera `--proxy-server`:
        ```bash
        code --install-extension <id-de-la-extensión> --proxy-server=http://tu-servidor-proxy:puerto
        ```

3.  **Revisar la Salida**
    -   La salida de la consola de la bandera `--verbose` mostrará el progreso de la instalación y cualquier error (por ejemplo, tiempos de espera de conexión o fallos de autenticación del proxy).
    -   Nota: La interfaz de línea de comandos (`code`) tiene un soporte de proxy limitado en comparación con la GUI de VSCode, por lo que los registros podrían no ser tan detallados como se espera.

---

### Revisar los Registros en VSCode
Para registros más detallados—especialmente después de un intento de instalación—usa las funciones de registro integradas de VSCode:

1.  **Abrir la Carpeta de Registros**
    -   Abre VSCode y accede a la Paleta de Comandos:
        -   Presiona `Ctrl+Shift+P` (o `Cmd+Shift+P` en macOS).
        -   Escribe y selecciona **Developer: Open Logs Folder**.
    -   Esto abre una carpeta que contiene varios archivos de registro. Busca:
        -   **`exthost.log`**: Registros relacionados con los procesos del host de extensiones, incluidos los intentos de instalación.
        -   **`sharedprocess.log`**: Registros para procesos compartidos que podrían incluir eventos relacionados con extensiones.
    -   Abre estos archivos en un editor de texto y busca errores que mencionen el ID de la extensión, problemas de red o problemas de proxy.

2.  **Ver el Panel de Salida**
    -   En VSCode, ve a `View > Output` para abrir el panel **Output**.
    -   En el menú desplegable de la derecha, selecciona **Extensions**.
    -   Esto muestra registros en tiempo real para las actividades de las extensiones al instalar desde dentro de VSCode (no directamente mediante CLI). Si reintentas la instalación a través de la interfaz de usuario de VSCode, podrías ver errores relacionados con el proxy aquí.

---

### Pasos Adicionales para Solucionar Problemas de Proxy
Dado que sospechas de un problema de proxy, aquí hay consejos adicionales para asegurar una configuración adecuada:

-   **Configurar el Proxy en VSCode**
    -   Abre la configuración de VSCode (`File > Preferences > Settings` o `Ctrl+,`).
    -   Busca `proxy` y establece:
        ```json
        "http.proxy": "http://tu-servidor-proxy:puerto"
        ```
    -   Opcionalmente, ajusta `"http.proxyStrictSSL"` (establécelo en `false` si es necesario) o `"http.proxyAuthorization"` (para proxies con autenticación).
    -   Estos ajustes se aplican a las instalaciones dentro de VSCode, no necesariamente a la CLI.

-   **Probar el Acceso a la Red**
    -   Prueba manualmente si el proxy permite el acceso al Marketplace de VSCode:
        -   Encuentra la URL del archivo VSIX de la extensión (por ejemplo, desde el sitio web del Marketplace).
        -   Usa una herramienta como `curl`:
            ```bash
            curl -x http://tu-servidor-proxy:puerto <url-del-vsix>
            ```
        -   Si esto falla, tu proxy podría estar bloqueando la conexión.

---

### Enfoque Recomendado
-   **Para Instalación por CLI**: Usa `code --install-extension <id-de-la-extensión> --verbose` con variables de entorno del proxy o `--proxy-server` para ver la salida inmediata. Revisa si hay errores en la terminal.
-   **Para Registros Detallados**: Instala la extensión mediante la interfaz de usuario de VSCode (Marketplace) y revisa el panel **Output > Extensions** o la carpeta de registros (`exthost.log`).
-   **Verificación del Proxy**: Asegúrate de que los ajustes del proxy sean correctos tanto en tu sistema como en VSCode.

Esta combinación te permite monitorear el progreso y diagnosticar problemas de proxy de manera efectiva. Si la salida de la CLI no es suficiente, los registros de VSCode proporcionarán una visión más profunda de lo que está fallando.
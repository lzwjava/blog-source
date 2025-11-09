---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Corrección de Errores de Carga de Archivos EAR Grandes en WebSphere
translated: true
type: note
---

### Comprender el Problema
El "error de carga de archivos multiparte" (a menudo algo como `org.apache.commons.fileupload.FileUploadException: Processing of multipart/form-data request failed. File too large (errno:27)`) típicamente ocurre al actualizar un archivo EAR en IBM WebSphere Application Server (WAS) a través de la Consola Administrativa. Esto es común para archivos EAR grandes (ej. >20MB) debido a límites en las cargas de archivos, almacenamiento temporal, memoria heap o restricciones de recursos del SO. No es un problema con el EAR en sí, sino con cómo la consola maneja la carga HTTP multiparte.

### Soluciones Rápidas para Probar Primero
1.  **Copiar el EAR al Servidor y Desplegarlo Localmente**:
    - Usa FTP/SCP para transferir el nuevo archivo EAR a un directorio en el servidor WAS (ej. `/opt/IBM/WebSphere/AppServer/installableApps/`).
    - En la Consola Administrativa: Ve a **Aplicaciones > Tipos de aplicaciones > Aplicaciones empresariales de WebSphere**.
    - Selecciona tu aplicación existente > **Actualizar**.
    - Elige **Reemplazar o agregar un solo módulo** o **Reemplazar la aplicación completa**, luego selecciona **Sistema de archivos local** y apunta a la ruta del EAR copiado.
    - Esto evita la carga multiparte a través de HTTP.

2.  **Aumentar los Límites de Tamaño de Archivo del SO (Servidores UNIX/Linux)**:
    - El error `errno:27` a menudo significa que el archivo excede el ulimit del proceso.
    - Ejecuta `ulimit -f` como el usuario de WAS (ej. `webadmin`) para verificar el límite actual.
    - Establécelo a ilimitado: Añade `ulimit -f unlimited` al perfil de shell del usuario (ej. `~/.bash_profile`) o al script de inicio del servidor.
    - Reinicia el Deployment Manager (dmgr) e intenta la carga nuevamente.

### Cambios de Configuración en WAS
1.  **Aumentar el Tamaño del Heap para el Deployment Manager**:
    - Los EARs grandes pueden causar OutOfMemory durante el procesamiento.
    - En la Consola Administrativa: **Servidores > Tipos de servidor > Servidores administrativos > Deployment Manager**.
    - En **Administración de Java y procesos > Definición de proceso > Máquina virtual Java**:
      - Establece **Tamaño de pila inicial** en 1024 (o más, ej. 2048 para EARs muy grandes).
      - Establece **Tamaño de pila máximo** en 2048 (o más).
    - Guarda, reinicia el dmgr y vuelve a intentar.

2.  **Ajustar los Límites de Tamaño de Sesión HTTP o Post (Si Aplica)**:
    - Para límites del contenedor web: **Servidores > Tipos de servidor > Servidores de aplicaciones WebSphere > [Tu Servidor] > Contenedor Web > Transportes HTTP**.
    - Aumenta **Tamaño máximo de publicación** (en bytes) si está configurado bajo.
    - Nota: Esto afecta indirectamente a la aplicación web de la consola administrativa.

### Solución Recomendada a Largo Plazo: Usar wsadmin para Actualizaciones
Para actualizaciones grandes o frecuentes, evita la consola por completo—no es confiable para archivos grandes. Usa la herramienta de scripting wsadmin (Jython o JACL) para actualizar la aplicación.

#### Pasos:
1.  Copia el nuevo EAR a una ruta accesible por el servidor (ej. `/tmp/myapp.ear`).
2.  Inicia wsadmin:  
    ```
    /opt/IBM/WebSphere/AppServer/bin/wsadmin.sh -lang jython -user admin -password pass
    ```
3.  Ejecuta este script de Jython para actualizar:  
    ```python
    AdminApp.update('MyAppName', 'app', [-Map ModulesToApps, '[-MapWebModToVH [[default_host MyContext virtual_host]] ]'], [-Operation update], [-appname MyAppName], [-MapModulesToServers [[MyModule MyServer]]], [-nodefaultoptions], [-preCompileJSPs false], [-contextroot MyContext], [-noTxImport], [-connType SERVER], [ -contenturi /tmp/myapp.ear ])
    AdminConfig.save()
    ```
    - Reemplaza `MyAppName` con el nombre de tu aplicación, `MyContext` con el contexto raíz, `MyServer` con el servidor/clúster objetivo y `/tmp/myapp.ear` con la ruta del EAR.
4.  Sincroniza los nodos si estás en un entorno clusterizado: `AdminControl.invoke(AdminControl.completeServers(), 'sync')`.
5.  Reinicia la aplicación: **Aplicaciones > [App] > Reiniciar**.

Este método es más rápido, evita los límites de carga y es scriptable para automatización (ej. vía Jenkins).

### Consejos Adicionales
-   **Revisar los Logs**: Consulta `SystemOut.log` y `SystemErr.log` en el perfil del dmgr para más detalles (ej. `/opt/IBM/WebSphere/AppServer/profiles/Dmgr01/logs/dmgr/`).
-   **Probar con un EAR más Pequeño**: Verifica si el problema está relacionado con el tamaño comprimiendo una versión mínima.
-   **Versión de WAS**: Asegúrate de estar en una versión soportada (ej. 8.5, 9.0). Aplica los últimos fixes si es necesario.
-   Si el error persiste (ej. timeout), aumenta el timeout HTTP en **Entorno > Servidores de aplicaciones web > [Servidor] > Configuración de contenedor > Configuración de contenedor web > Contenedor web > Administración de sesiones > Configuración > Timeout**.

Si nada de esto lo resuelve, comparte el mensaje de error exacto y la versión de WAS para un consejo más específico.

### Referencias
-   [Error during deploy of war file on Websphere Application Server 7.0](https://coderanch.com/t/459530/application-servers/Error-deploy-war-file-Websphere)
-   [OutOfMemory errors while deploying applications in WebSphere Application Server](https://www.ibm.com/support/pages/outofmemory-errors-while-deploying-applications-websphere-application-server)
-   [Maximum size limit of an Ear that can be deployed in WAS](https://stackoverflow.com/questions/58748076/maximum-size-limit-of-an-ear-that-can-be-deployed-in-was)
-   [Deploying the enterprise archive (EAR) using the WebSphere Administrative Console](https://www.ibm.com/docs/en/configurepricequote/9.5.0?topic=cwaso-deploying-enterprise-archive-ear-using-websphere-admin-console)
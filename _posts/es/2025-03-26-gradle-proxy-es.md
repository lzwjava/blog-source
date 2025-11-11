---
audio: false
generated: true
lang: es
layout: post
title: Configurar Proxy para Gradle en VSCode
translated: true
type: note
---

Para configurar un proxy para Gradle en Visual Studio Code (VSCode) para que pueda descargar dependencias a través de un proxy, necesitas configurar los ajustes del proxy en la configuración de Gradle. Gradle utiliza un archivo de propiedades para gestionar dichos ajustes, y VSCode depende del sistema de construcción de Gradle para los proyectos de Gradle. Aquí te explicamos cómo hacerlo:

### Pasos para Configurar el Proxy para Gradle en VSCode

1.  **Localiza o Crea el Archivo de Propiedades de Gradle**
    - Gradle utiliza un archivo llamado `gradle.properties` para almacenar los ajustes de configuración global.
    - Este archivo se encuentra típicamente en el directorio de usuario de Gradle:
        - En Windows: `C:\Users\<TuNombreDeUsuario>\.gradle\gradle.properties`
        - En macOS/Linux: `~/.gradle/gradle.properties`
    - Si el archivo no existe, créalo en la ubicación anterior.

2.  **Añade los Ajustes del Proxy a `gradle.properties`**
    - Abre el archivo `gradle.properties` en un editor de texto.
    - Añade las siguientes líneas, reemplazando los marcadores de posición (`<proxyHost>`, `<proxyPort>`, `<username>`, `<password>`) con los detalles reales de tu proxy:
      ```
      systemProp.http.proxyHost=<proxyHost>
      systemProp.http.proxyPort=<proxyPort>
      systemProp.http.proxyUser=<username>
      systemProp.http.proxyPassword=<password>
      systemProp.https.proxyHost=<proxyHost>
      systemProp.https.proxyPort=<proxyPort>
      systemProp.https.proxyUser=<username>
      systemProp.https.proxyPassword=<password>
      ```
    - Ejemplo con valores reales:
      ```
      systemProp.http.proxyHost=proxy.ejemplo.com
      systemProp.http.proxyPort=8080
      systemProp.http.proxyUser=miusuario
      systemProp.http.proxyPassword=micontraseña
      systemProp.https.proxyHost=proxy.ejemplo.com
      systemProp.https.proxyPort=8080
      systemProp.https.proxyUser=miusuario
      systemProp.https.proxyPassword=micontraseña
      ```
    - Si tu proxy no requiere autenticación (usuario/contraseña), puedes omitir las líneas `proxyUser` y `proxyPassword`.

3.  **Opcional: Configurar el Proxy por Proyecto**
    - Si deseas que los ajustes del proxy se apliquen solo a un proyecto específico (en lugar de globalmente), puedes añadir el archivo `gradle.properties` al directorio raíz de tu proyecto (por ejemplo, `<raiz-del-proyecto>/gradle.properties`) con el mismo contenido mencionado arriba.

4.  **Verifica que Gradle Usa el Proxy**
    - Abre tu proyecto de Gradle en VSCode.
    - Ejecuta una tarea de construcción (por ejemplo, `gradle build`) a través de la terminal de VSCode o de la extensión de Gradle.
    - Gradle debería ahora enrutar sus descargas (como las dependencias del sitio oficial) a través del proxy especificado.

5.  **Notas Específicas para VSCode**
    - Asegúrate de que las extensiones **Java Extension Pack** y **Gradle for Java** estén instaladas en VSCode, ya que mejoran el soporte para proyectos Gradle.
    - Si VSCode todavía tiene problemas, verifica que tu runtime de Java (utilizado por Gradle) también respete el proxy. Es posible que necesites establecer argumentos de proxy para la JVM:
        - En VSCode, ve a `Archivo > Preferencias > Configuración`.
        - Busca `java.gradle.build.jvmArguments`.
        - Añade algo como:
          ```
          -Dhttp.proxyHost=<proxyHost> -Dhttp.proxyPort=<proxyPort> -Dhttps.proxyHost=<proxyHost> -Dhttps.proxyPort=<proxyPort>
          ```

6.  **Probar la Configuración**
    - Recarga tu proyecto en VSCode (por ejemplo, ciérralo y ábrelo de nuevo o usa el botón "Refresh" en la barra lateral de Gradle).
    - Ejecuta una tarea de Gradle (por ejemplo, `gradle build` o `gradle dependencies`) para confirmar que descarga archivos a través del proxy.

### Resolución de Problemas

-   **Verifica los Detalles del Proxy**: Asegúrate de que el host del proxy, el puerto y las credenciales sean correctos.
-   **Firewall o Red**: Si aún falla, es posible que tu proxy o red bloquee URLs específicas de Gradle (por ejemplo, `https://services.gradle.org`). Prueba con un comando como `curl` o consulta con tu administrador de red.
-   **Salida Detallada**: Ejecuta Gradle con `--debug` o `--info` (por ejemplo, `gradle build --debug`) en la terminal de VSCode para ver registros detallados sobre las peticiones de red.

Esta configuración debería permitir que Gradle en VSCode descargue dependencias a través de tu proxy exitosamente. ¡Avísame si encuentras algún problema!
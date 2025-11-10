---
audio: false
generated: true
lang: es
layout: post
title: Integración de YourKit Profiler con WebSphere Liberty en Windows
translated: true
type: note
---

Usar YourKit Java Profiler con WebSphere Liberty Server en Windows implica integrar el agente de YourKit en la JVM de WebSphere Liberty y configurarlo para el perfilado. A continuación, se detallan los pasos para configurar esto, basándose en la información disponible y las mejores prácticas para la integración de YourKit y WebSphere Liberty:

### Prerrequisitos
- **YourKit Java Profiler**: Instalado en tu máquina Windows. Descárgalo desde el [sitio oficial de YourKit](https://www.yourkit.com/) y asegúrate de tener una licencia válida o una clave de prueba.
- **WebSphere Liberty**: Instalado y ejecutándose en tu sistema Windows. Asegúrate de tener acceso administrativo a los archivos de configuración del servidor.
- **Java JDK**: WebSphere Liberty utiliza un entorno de ejecución Java (IBM JDK u OpenJDK). Confirma que la versión del JDK sea compatible con YourKit (YourKit es compatible con Java 5 y versiones posteriores, pero verifica la compatibilidad con tu versión específica).
- **Privilegios Administrativos**: Se requieren para modificar los archivos de configuración de WebSphere Liberty.

### Guía Paso a Paso

1. **Instalar YourKit Java Profiler**
   - Descarga e instala YourKit Java Profiler para Windows desde el [sitio web de YourKit](https://www.yourkit.com/download).
   - Toma nota del directorio de instalación, ya que necesitarás la ruta a la librería del agente de YourKit (`yjpagent.dll`).

2. **Localizar el Agente de YourKit**
   - El agente de YourKit para Windows se encuentra típicamente en:
     ```
     C:\Program Files\YourKit-Java-Profiler-<version>\bin\win64\yjpagent.dll
     ```
     (Usa `win32` en lugar de `win64` si ejecutas una JVM de 32 bits).
   - Asegúrate de que el agente coincida con la arquitectura de la JVM (32-bit o 64-bit) utilizada por WebSphere Liberty.

3. **Configurar WebSphere Liberty para Usar el Agente de YourKit**
   - **Localizar el Archivo `jvm.options`**:
     - Navega al directorio de configuración de tu servidor WebSphere Liberty, típicamente:
       ```
       <LIBERTY_INSTALL_DIR>\usr\servers\<server_name>\jvm.options
       ```
       Reemplaza `<LIBERTY_INSTALL_DIR>` con la ruta a tu instalación de WebSphere Liberty (ej., `C:\wlp`), y `<server_name>` con el nombre de tu servidor (ej., `defaultServer`).
     - Si el archivo `jvm.options` no existe, créalo en el directorio del servidor.
   - **Añadir la Ruta del Agente de YourKit**:
     - Abre `jvm.options` en un editor de texto con privilegios administrativos.
     - Añade la siguiente línea para incluir el agente de YourKit:
       ```
       -agentpath:C:\Program Files\YourKit-Java-Profiler-<version>\bin\win64\yjpagent.dll=disablestacktelemetry,disableexceptiontelemetry,delay=10000,probe_disable=*,sessionname=WebSphereLiberty
       ```
       - Reemplaza `<version>` con tu versión de YourKit (ej., `2023.9`).
       - Las opciones (`disablestacktelemetry`, `disableexceptiontelemetry`, `probe_disable=*`) reducen la sobrecarga al deshabilitar la telemetría innecesaria. El `delay=10000` asegura que el agente se inicie después de que el servidor se inicialice, y `sessionname=WebSphereLiberty` identifica la sesión de perfilado.
       - Ejemplo:
         ```
         -agentpath:C:\Program Files\YourKit-Java-Profiler-2023.9\bin\win64\yjpagent.dll=disablestacktelemetry,disableexceptiontelemetry,delay=10000,probe_disable=*,sessionname=WebSphereLiberty
         ```
   - **Guardar el Archivo**: Asegúrate de tener permisos de escritura para el archivo `jvm.options`.

4. **Verificar la Compatibilidad de la JVM**
   - WebSphere Liberty a menudo utiliza IBM JDK u OpenJDK. YourKit es compatible con ambos, pero si encuentras problemas (ej., `NoSuchMethodError` como se nota en algunos casos de IBM JDK), añade `probe_disable=*` a la ruta del agente para deshabilitar las sondas que pueden causar conflictos con IBM JDK.[](https://www.yourkit.com/forum/viewtopic.php?f=3&t=8042)
   - Verifica la versión de Java utilizada por Liberty:
     ```
     <LIBERTY_INSTALL_DIR>\java\bin\java -version
     ```
     Asegúrate de que sea compatible con YourKit (Java 5 o posterior para versiones antiguas; las versiones modernas son compatibles con Java 8+).

5. **Iniciar WebSphere Liberty**
   - Inicia tu servidor WebSphere Liberty como de costumbre:
     ```
     <LIBERTY_INSTALL_DIR>\bin\server start <server_name>
     ```
     Ejemplo:
     ```
     C:\wlp\bin\server start defaultServer
     ```
   - Revisa los registros del servidor (`<LIBERTY_INSTALL_DIR>\usr\servers\<server_name>\logs\console.log` o `messages.log`) en busca de errores relacionados con el agente de YourKit.
   - Busca el registro del agente de YourKit en:
     ```
     %USERPROFILE%\.yjp\log\<session_name>-<pid>.log
     ```
     Ejemplo:
     ```
     C:\Users\<TuNombreDeUsuario>\.yjp\log\WebSphereLiberty-<pid>.log
     ```
     El registro debería indicar que el agente está cargado y escuchando en un puerto (por defecto: 10001):
     ```
     Profiler agent is listening on port 10001
     ```

6. **Conectar la Interfaz de Usuario de YourKit Profiler**
   - Inicia la Interfaz de Usuario de YourKit Java Profiler en tu máquina Windows.
   - En la Interfaz de Usuario de YourKit, selecciona **Profile | Profile Local Java Server or Application** o **Profile | Profile Remote Java Server or Application**.
     - Para el perfilado local (dado que YourKit y Liberty están en la misma máquina), elige **Profile Local Java Server or Application**.
     - La Interfaz de Usuario debería detectar el proceso de WebSphere Liberty (identificado por `sessionname=WebSphereLiberty`).
   - Si no se detecta automáticamente, usa **Profile Remote Java Server or Application**, selecciona **Direct Connect**, e ingresa:
     - **Host**: `localhost`
     - **Port**: `10001` (o el puerto especificado en el registro del agente).
   - Conéctate al servidor. La Interfaz de Usuario mostrará la telemetría de CPU, memoria e hilos.

7. **Perfilar la Aplicación**
   - Usa la Interfaz de Usuario de YourKit para:
     - **Perfilado de CPU**: Habilita el muestreo o trazado de CPU para identificar cuellos de botella en el rendimiento. Evita habilitar "Profile J2EE" para sistemas de alta carga para minimizar la sobrecarga.[](https://www.jahia.com/blog/analyzing-system-performance-with-yourkit-java-profiler)
     - **Perfilado de Memoria**: Analiza el uso del heap y detecta fugas de memoria agrupando objetos por aplicación web (útil para aplicaciones alojadas en Liberty).[](https://www.yourkit.com/docs/java-profiler/latest/help/webapps.jsp)
     - **Análisis de Hilos**: Comprueba si hay interbloqueos o hilos congelados en la pestaña Threads.[](https://www.yourkit.com/changes/)
   - Toma instantáneas para análisis sin conexión si es necesario (File | Save Snapshot).
   - Monitoriza el uso de memoria, ya que el perfilado puede aumentar el consumo de memoria. Evita sesiones de perfilado largas sin monitorización.[](https://www.jahia.com/blog/analyzing-system-performance-with-yourkit-java-profiler)

8. **Solución de Problemas**
   - **El Servidor Falla al Iniciar o se Vuelve Inaccesible**:
     - Revisa los registros (`console.log`, `messages.log` y el registro del agente de YourKit) en busca de errores como `OutOfMemoryError` o `NoSuchMethodError`.[](https://www.yourkit.com/forum/viewtopic.php?t=328)[](https://www.yourkit.com/forum/viewtopic.php?t=16205)
     - Asegúrate de que `-agentpath` se añadió al archivo `jvm.options` correcto y coincide con el script utilizado para iniciar Liberty.[](https://www.yourkit.com/forum/viewtopic.php?t=16205)
     - Si usas IBM JDK, intenta añadir `probe_disable=*` a la ruta del agente para evitar conflictos.[](https://www.yourkit.com/forum/viewtopic.php?f=3&t=8042)
   - **ClassNotFoundException**:
     - Si ves errores como `java.lang.ClassNotFoundException` (ej., para `java.util.ServiceLoader`), asegúrate de que la versión del agente de YourKit sea compatible con tu JDK. Para IBM JDKs antiguos (ej., Java 5), usa YourKit 8.0 o anterior.[](https://www.yourkit.com/forum/viewtopic.php?f=3&t=7149)
   - **No Hay Datos de Perfilado**:
     - Verifica que las versiones del agente de YourKit y de la Interfaz de Usuario coincidan. Las versiones no coincidentes pueden causar problemas de conexión.[](https://www.yourkit.com/forum/viewtopic.php?t=328)
     - Asegúrate de que el servidor sea accesible a través del navegador (ej., `https://localhost:9443` si usas SSL). Si no lo es, verifica la configuración del firewall o la configuración SSL.[](https://www.yourkit.com/forum/viewtopic.php?t=16205)
   - **Problemas con el Archivo de Registro**:
     - Si no se crea ningún registro de YourKit en `~/.yjp/log/`, asegúrate de que el proceso tenga permisos de escritura en el directorio home del usuario.[](https://www.yourkit.com/forum/viewtopic.php?f=3&t=3219)
   - **Impacto en el Rendimiento**:
     - El perfilado puede afectar al rendimiento. Usa configuraciones mínimas (ej., deshabilita la telemetría de pila) para entornos similares a producción.[](https://www.jahia.com/blog/analyzing-system-performance-with-yourkit-java-profiler)

9. **Opcional: Usar el Asistente de Integración de YourKit**
   - YourKit proporciona un Asistente de Integración de Servidores Java para simplificar la configuración:
     - Inicia la Interfaz de Usuario de YourKit y selecciona **Profile | Profile Local Java Server or Application**.
     - Elige **WebSphere Liberty** de la lista de servidores soportados (o "Other Java application" si Liberty no está en la lista).
     - Sigue el asistente para generar la configuración `-agentpath` necesaria y actualizar `jvm.options`. Asegúrate de tener permisos de escritura para los archivos de configuración.[](https://www.yourkit.com/docs/java-profiler/latest/help/java-server-integration-wizard.jsp)
   - Esto es particularmente útil para asegurar rutas y configuraciones correctas.

10. **Detener el Perfilado**
    - Para deshabilitar el perfilado, elimina o comenta la línea `-agentpath` en `jvm.options` y reinicia el servidor.
    - Alternativamente, detén el servidor:
      ```
      <LIBERTY_INSTALL_DIR>\bin\server stop <server_name>
      ```

### Notas Adicionales
- **Licencia**: No se requiere clave de licencia para el agente de YourKit en el servidor; la licencia se aplica en la Interfaz de Usuario de YourKit. Para el perfilado remoto desde otra máquina Windows, asegúrate de que la Interfaz de Usuario tenga una licencia válida.[](https://www.yourkit.com/forum/viewtopic.php?f=3&t=11385)[](https://www.yourkit.com/forum/viewtopic.php?t=11385)
- **Perfilado Remoto**: Si realizas el perfilado desde una máquina diferente, asegura la conectividad de red al puerto del agente (por defecto: 10001) y usa la opción **Profile Remote Java Server or Application** con el nombre de host/IP del servidor.
- **Consideraciones de Rendimiento**: El perfilado puede aumentar el uso de memoria y CPU. Para sistemas de producción, comienza con opciones de perfilado mínimas (ej., muestreo de CPU) y monitoriza la salud del servidor.[](https://www.jahia.com/blog/analyzing-system-performance-with-yourkit-java-profiler)
- **Compatibilidad**: Si usas una versión antigua de WebSphere Liberty con IBM JDK 1.4.2 o 1.5, puede que necesites una versión antigua de YourKit (ej., 8.0 para Java 5).[](https://www.yourkit.com/forum/viewtopic.php?f=3&t=7149)[](https://stackoverflow.com/questions/61795/java-profiler-for-ibm-jvm-1-4-2-websphere-6-0-2)
- **Documentación**: Consulta la documentación oficial de YourKit para opciones de perfilado detalladas: [YourKit Java Profiler Help](https://www.yourkit.com/docs/java/help/).[](https://www.jahia.com/blog/analyzing-system-performance-with-yourkit-java-profiler)

### Ejemplo de Configuración
Aquí tienes un archivo `jvm.options` de ejemplo:
```
-Xmx4G
-Xms4G
-agentpath:C:\Program Files\YourKit-Java-Profiler-2023.9\bin\win64\yjpagent.dll=disablestacktelemetry,disableexceptiontelemetry,delay=10000,probe_disable=*,sessionname=WebSphereLiberty
```

### Probar la Configuración
- Después de iniciar el servidor, accede a tu aplicación (ej., `https://localhost:9443`) para asegurarte de que se está ejecutando.
- En la Interfaz de Usuario de YourKit, verifica que se muestren los datos de telemetría (CPU, memoria, hilos).
- Si surgen problemas, revisa el registro del agente de YourKit y los registros de Liberty en busca de errores.

¡Si encuentras errores específicos o necesitas ayuda con un paso en particular, házmelo saber y puedo proporcionar más asistencia!
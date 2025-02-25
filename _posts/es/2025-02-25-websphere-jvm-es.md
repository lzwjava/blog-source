---
audio: true
lang: es
layout: post
title: Opciones de JVM en WebSphere Liberty Server
translated: true
---

Para verificar las opciones de la JVM configuradas en el archivo `jvm.options` ubicado en el directorio del servidor de un servidor WebSphere Liberty Profile (WLP), puedes usar el comando `jinfo` proporcionado por el Kit de Desarrollo de Java (JDK). Este método te permite verificar las opciones aplicadas a un servidor en ejecución de manera eficiente. A continuación, se presenta una guía paso a paso para lograr esto:

### Pasos para verificar las opciones de la JVM

1. **Entender el contexto**
   El archivo `jvm.options` en el directorio del servidor (generalmente `<WLP_HOME>/usr/servers/<serverName>/jvm.options`) se utiliza para especificar argumentos de la JVM, como el tamaño del montículo (por ejemplo, `-Xmx`), configuraciones de recolección de basura (por ejemplo, `-XX:+UseG1GC`) o propiedades del sistema (por ejemplo, `-Dmy.property=value`), que se aplican cuando el servidor Liberty se inicia.

2. **Iniciar el servidor**
   Comienza iniciando tu servidor Liberty en segundo plano usando el siguiente comando:
   ```
   <WLP_HOME>/bin/server start <serverName>
   ```
   Reemplaza `<WLP_HOME>` con la ruta a tu instalación de WebSphere Liberty y `<serverName>` con el nombre de tu servidor. Este comando lanza el servidor como un proceso en segundo plano.

3. **Localizar el ID del proceso (PID)**
   Después de iniciar el servidor, necesitas el ID del proceso del proceso Java en ejecución. Liberty almacena convenientemente esto en un archivo `.pid` ubicado en:
   ```
   <WLP_HOME>/usr/servers/<serverName>/workarea/<serverName>.pid
   ```
   Abre este archivo (por ejemplo, usando `cat` en sistemas tipo Unix o un editor de texto) para obtener el PID, que es un valor numérico que representa el proceso del servidor.

4. **Verificar las banderas de la JVM**
   Usa el comando `jinfo` para inspeccionar las banderas de la JVM aplicadas al servidor en ejecución. Ejecuta:
   ```
   jinfo -flags <pid>
   ```
   Reemplaza `<pid>` con el ID del proceso obtenido del archivo `.pid`. Este comando muestra las banderas de la línea de comandos pasadas a la JVM, como `-Xmx1024m` o `-XX:+PrintGCDetails`. Revisa la salida para confirmar que las banderas que configuraste en `jvm.options` están presentes.

5. **Verificar las propiedades del sistema**
   Si tu archivo `jvm.options` incluye propiedades del sistema (por ejemplo, `-Dmy.property=value`), verifícalas por separado con:
   ```
   jinfo -sysprops <pid>
   ```
   Esto muestra todas las propiedades del sistema establecidas para la JVM. Busca en la salida las propiedades específicas que definiste para asegurarte de que se aplicaron correctamente.

### Requisitos previos
- **JDK instalado**: El comando `jinfo` es parte del JDK, no del JRE. Asegúrate de tener un JDK instalado y que el ejecutable `jinfo` esté en el PATH del sistema.
- **Permisos**: Ejecuta `jinfo` con el mismo usuario que inició el servidor o con suficientes privilegios para adjuntarse al proceso.

### Métodos alternativos
Si `jinfo` no está disponible o prefieres otro enfoque, aquí tienes dos opciones adicionales:

- **Usando `server dump`**:
  1. Inicia el servidor con `server start <serverName>`.
  2. Genera un volcado del servidor usando:
     ```
     <WLP_HOME>/bin/server dump <serverName>
     ```
  3. Localiza el archivo `.zip` generado en `<WLP_HOME>/usr/servers/<serverName>/`, extraelo y abre el archivo `javacore.<timestamp>.txt`.
  4. Busca la sección "CMDLINE" para ver la línea de comandos completa de Java, incluyendo las banderas de la JVM, y la sección "System Properties" para las propiedades del sistema.

- **Rastrear el script de inicio** (sistemas tipo Unix):
  1. Ejecuta el script del servidor con el rastreo habilitado:
     ```
     sh -x <WLP_HOME>/bin/server start <serverName>
     ```
  2. Revisa la salida para encontrar el comando de Java ejecutado por el script, que incluye todas las opciones de `jvm.options`.

### Notas
- **Servidor no en ejecución**: Si el servidor falla al iniciar debido a opciones no válidas, usa `server run <serverName>` para ejecutarlo en primer plano y revisa la salida de la consola para errores, o usa el método de rastreo del script para ver el comando.
- **Archivos de registro**: El archivo `console.log` en `<WLP_HOME>/usr/servers/<serverName>/logs/` puede contener alguna información de inicio, pero no lista todas las opciones de la JVM a menos que se habilite el registro detallado (por ejemplo, `-XX:+PrintFlagsFinal`).

### Conclusión
El método `jinfo` es la manera más directa de verificar las opciones de la JVM configuradas en `jvm.options` para un servidor Liberty en ejecución. Siguiendo los pasos anteriores, puedes confirmar que tanto las banderas de la JVM como las propiedades del sistema se aplican como se espera.
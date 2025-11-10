---
audio: false
generated: true
lang: es
layout: post
title: Descripción General de las Herramientas de OpenJDK 21
translated: true
type: note
---

El directorio `/usr/lib/jvm/java-21-openjdk-amd64/bin/` contiene herramientas proporcionadas por el OpenJDK 21 Java Development Kit (JDK). Estas herramientas se utilizan para diversas tareas relacionadas con el desarrollo, depuración, monitoreo y empaquetado de Java. A continuación se presenta una explicación concisa de cada herramienta y su uso común. Para un uso detallado, puede ejecutar `nombre_herramienta --help` o `man nombre_herramienta` en la terminal para la mayoría de estas herramientas.

---

### 1. **jar** - Crear y gestionar archivos Java ARchive (JAR)
- **Propósito**: Empaquetar clases y recursos de Java en un archivo JAR o extraer contenidos de un JAR.
- **Uso Común**:
  ```bash
  jar cf miapp.jar *.class  # Crear un archivo JAR
  jar xf miapp.jar          # Extraer contenidos de un JAR
  jar tf miapp.jar          # Listar contenidos de un JAR
  ```
- **Ejemplo**: `jar cvfm miapp.jar manifest.txt *.class` (crea un JAR con un archivo manifiesto).

---

### 2. **java** - Ejecutar una aplicación Java
- **Propósito**: Ejecutar un programa Java ejecutando un archivo de clase o JAR.
- **Uso Común**:
  ```bash
  java MiClase              # Ejecutar un archivo de clase
  java -jar miapp.jar       # Ejecutar un archivo JAR
  java -cp . MiClase        # Ejecutar con un classpath específico
  ```
- **Ejemplo**: `java -Xmx512m -jar miapp.jar` (ejecuta un JAR con 512MB de heap máximo).

---

### 3. **javadoc** - Generar documentación de API
- **Propósito**: Crear documentación HTML a partir de comentarios en el código fuente Java.
- **Uso Común**:
  ```bash
  javadoc -d docs MiClase.java  # Generar docs en la carpeta 'docs'
  ```
- **Ejemplo**: `javadoc -d docs -sourcepath src -subpackages com.example` (generar docs para un paquete).

---

### 4. **jcmd** - Enviar comandos de diagnóstico a una JVM en ejecución
- **Propósito**: Interactuar con un proceso Java en ejecución para diagnósticos (ej. volcados de hilos, información del heap).
- **Uso Común**:
  ```bash
  jcmd <pid> help           # Listar comandos disponibles para un proceso JVM
  jcmd <pid> Thread.print   # Imprimir volcado de hilos
  ```
- **Ejemplo**: `jcmd 1234 GC.run` (activar recolección de basura para el ID de proceso 1234).

---

### 5. **jdb** - Depurador de Java
- **Propósito**: Depurar aplicaciones Java de forma interactiva.
- **Uso Común**:
  ```bash
  jdb MiClase               # Iniciar depuración de una clase
  java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=*:5005 MiClase  # Ejecutar con agente de depuración
  jdb -attach localhost:5005  # Conectarse a una JVM en ejecución
  ```
- **Ejemplo**: `jdb -sourcepath src MiClase` (depurar con código fuente).

---

### 6. **jdeps** - Analizar dependencias de clases y JAR
- **Propósito**: Identificar dependencias de una aplicación o biblioteca Java.
- **Uso Común**:
  ```bash
  jdeps miapp.jar           # Analizar dependencias en un JAR
  jdeps -s MiClase.class    # Resumen de dependencias
  ```
- **Ejemplo**: `jdeps -v miapp.jar` (análisis de dependencias detallado).

---

### 7. **jhsdb** - Depurador Java HotSpot
- **Propósito**: Depuración y análisis avanzado de procesos JVM (ej. volcados de memoria).
- **Uso Común**:
  ```bash
  jhsdb jmap --heap --pid <pid>  # Analizar el heap de un proceso en ejecución
  jhsdb hsdb                     # Iniciar la GUI del depurador HotSpot
  ```
- **Ejemplo**: `jhsdb jmap --heap --pid 1234` (volcar información del heap para el proceso 1234).

---

### 8. **jinfo** - Ver o modificar la configuración de la JVM
- **Propósito**: Inspeccionar o cambiar opciones de la JVM para un proceso en ejecución.
- **Uso Común**:
  ```bash
  jinfo <pid>               # Ver banderas y propiedades de la JVM
  jinfo -flag +PrintGC <pid>  # Activar una bandera de la JVM
  ```
- **Ejemplo**: `jinfo -sysprops 1234` (mostrar propiedades del sistema para el proceso 1234).

---

### 9. **jmap** - Volcar información de memoria o heap de la JVM
- **Propósito**: Generar volcados de heap o estadísticas de memoria.
- **Uso Común**:
  ```bash
  jmap -heap <pid>          # Imprimir resumen del heap
  jmap -dump:file=dump.hprof <pid>  # Crear un volcado de heap
  ```
- **Ejemplo**: `jmap -dump:live,format=b,file=dump.hprof 1234` (volcar objetos activos).

---

### 10. **jpackage** - Empaquetar aplicaciones Java
- **Propósito**: Crear instaladores nativos o ejecutables para aplicaciones Java (ej. .deb, .rpm, .exe).
- **Uso Común**:
  ```bash
  jpackage --input target --name MiApp --main-jar miapp.jar --main-class MiClase
  ```
- **Ejemplo**: `jpackage --type deb --input target --name MiApp --main-jar miapp.jar` (crear un paquete Debian).

---

### 11. **jps** - Listar procesos JVM en ejecución
- **Propósito**: Mostrar procesos Java con sus IDs de proceso (PIDs).
- **Uso Común**:
  ```bash
  jps                       # Listar todos los procesos Java
  jps -l                    # Incluir nombres completos de clases
  ```
- **Ejemplo**: `jps -m` (mostrar clase principal y argumentos).

---

### 12. **jrunscript** - Ejecutar scripts en Java
- **Propósito**: Ejecutar scripts (ej. JavaScript) usando el motor de scripting de Java.
- **Uso Común**:
  ```bash
  jrunscript -e "print('Hola')"  # Ejecutar un comando de script único
  jrunscript script.js            # Ejecutar un archivo de script
  ```
- **Ejemplo**: `jrunscript -l js -e "print(2+2)"` (ejecutar código JavaScript).

---

### 13. **jshell** - REPL interactivo de Java
- **Propósito**: Ejecutar fragmentos de código Java de forma interactiva para pruebas o aprendizaje.
- **Uso Común**:
  ```bash
  jshell                    # Iniciar shell interactivo
  jshell script.jsh         # Ejecutar un script de JShell
  ```
- **Ejemplo**: `jshell -q` (iniciar JShell en modo silencioso).

---

### 14. **jstack** - Generar volcados de hilos
- **Propósito**: Capturar los rastreos de pila de los hilos en una JVM en ejecución.
- **Uso Común**:
  ```bash
  jstack <pid>              # Imprimir volcado de hilos
  jstack -l <pid>           # Incluir información de bloqueos
  ```
- **Ejemplo**: `jstack 1234 > hilos.txt` (guardar volcado de hilos en un archivo).

---

### 15. **jstat** - Monitorear estadísticas de la JVM
- **Propósito**: Mostrar estadísticas de rendimiento (ej. recolección de basura, uso de memoria).
- **Uso Común**:
  ```bash
  jstat -gc <pid>           # Mostrar estadísticas de recolección de basura
  jstat -class <pid> 1000   # Mostrar estadísticas de carga de clases cada 1 segundo
  ```
- **Ejemplo**: `jstat -gcutil 1234 1000 5` (mostrar estadísticas de GC 5 veces, cada 1 segundo).

---

### 16. **jstatd** - Demonio de monitoreo de JVM
- **Propósito**: Ejecutar un servidor de monitoreo remoto para permitir que herramientas como `jstat` se conecten remotamente.
- **Uso Común**:
  ```bash
  jstatd -J-Djava.security.policy=jstatd.policy
  ```
- **Ejemplo**: `jstatd -p 1099` (iniciar demonio en el puerto 1099).

---

### 17. **keytool** - Gestionar claves criptográficas y certificados
- **Propósito**: Crear y gestionar almacenes de claves para aplicaciones Java seguras.
- **Uso Común**:
  ```bash
  keytool -genkeypair -alias miclave -keystore almacenclaves.jks  # Generar un par de claves
  keytool -list -keystore almacenclaves.jks                     # Listar contenidos del almacén de claves
  ```
- **Ejemplo**: `keytool -importcert -file cert.pem -keystore almacenclaves.jks` (importar un certificado).

---

### 18. **rmiregistry** - Iniciar registro RMI
- **Propósito**: Ejecutar un registro para objetos Java Remote Method Invocation (RMI).
- **Uso Común**:
  ```bash
  rmiregistry               # Iniciar registro RMI en el puerto predeterminado (1099)
  rmiregistry 1234          # Iniciar en un puerto específico
  ```
- **Ejemplo**: `rmiregistry -J-Djava.rmi.server.codebase=file:./classes/` (iniciar con una codebase).

---

### 19. **serialver** - Generar serialVersionUID para clases
- **Propósito**: Calcular el `serialVersionUID` para clases Java que implementan `Serializable`.
- **Uso Común**:
  ```bash
  serialver MiClase         # Imprimir serialVersionUID para una clase
  ```
- **Ejemplo**: `serialver -classpath . com.example.MiClase` (calcular para una clase específica).

---

### 20. **javac** - Compilador de Java
- **Propósito**: Compilar archivos fuente Java en bytecode.
- **Uso Común**:
  ```bash
  javac MiClase.java        # Compilar un solo archivo
  javac -d bin *.java       # Compilar a un directorio específico
  ```
- **Ejemplo**: `javac -cp lib/* -sourcepath src -d bin src/MiClase.java` (compilar con dependencias).

---

### 21. **javap** - Desensamblar archivos de clase
- **Propósito**: Ver el bytecode o las firmas de métodos de una clase compilada.
- **Uso Común**:
  ```bash
  javap -c MiClase          # Desensamblar bytecode
  javap -s MiClase          # Mostrar firmas de métodos
  ```
- **Ejemplo**: `javap -c -private MiClase` (mostrar métodos privados y bytecode).

---

### 22. **jconsole** - Herramienta gráfica de monitoreo de JVM
- **Propósito**: Monitorear el rendimiento de la JVM (memoria, hilos, CPU) mediante una GUI.
- **Uso Común**:
  ```bash
  jconsole                  # Iniciar JConsole y conectarse a una JVM local
  jconsole <pid>            # Conectarse a un proceso específico
  ```
- **Ejemplo**: `jconsole localhost:1234` (conectarse a una JVM remota).

---

### 23. **jdeprscan** - Escanear APIs obsoletas
- **Propósito**: Identificar el uso de APIs obsoletas en un archivo JAR o de clase.
- **Uso Común**:
  ```bash
  jdeprscan miapp.jar       # Escanear un JAR en busca de APIs obsoletas
  ```
- **Ejemplo**: `jdeprscan --release 11 miapp.jar` (verificar contra APIs de Java 11).

---

### 24. **jfr** - Java Flight Recorder
- **Propósito**: Gestionar y analizar datos de perfilado de Java Flight Recorder.
- **Uso Común**:
  ```bash
  jfr print grabacion.jfr   # Imprimir contenidos de un archivo JFR
  jfr summary grabacion.jfr # Resumir un archivo JFR
  ```
- **Ejemplo**: `jfr print --events GC grabacion.jfr` (mostrar eventos de GC).

---

### 25. **jimage** - Inspeccionar o extraer archivos JIMAGE
- **Propósito**: Trabajar con archivos JIMAGE (utilizados en módulos JDK).
- **Uso Común**:
  ```bash
  jimage extract imagen.jimage  # Extraer contenidos de un archivo JIMAGE
  ```
- **Ejemplo**: `jimage list imagen.jimage` (listar contenidos de un JIMAGE).

---

### 26. **jlink** - Crear imágenes de tiempo de ejecución de Java personalizadas
- **Propósito**: Construir una JRE mínima con solo los módulos requeridos.
- **Uso Común**:
  ```bash
  jlink --module-path mods --add-modules java.base --output mijre
  ```
- **Ejemplo**: `jlink --add-modules java.base,java.sql --output jre-personalizado` (crear JRE con módulos específicos).

---

### 27. **jmod** - Gestionar archivos JMOD
- **Propósito**: Crear o gestionar archivos JMOD (utilizados para módulos JDK).
- **Uso Común**:
  ```bash
  jmod create --class-path classes mimod.jmod  # Crear un archivo JMOD
  jmod list mimod.jmod                        # Listar contenidos
  ```
- **Ejemplo**: `jmod extract mimod.jmod` (extraer contenidos JMOD).

---

### 28. **jwebserver** - Servidor HTTP simple
- **Propósito**: Ejecutar un servidor web básico para servir archivos estáticos.
- **Uso Común**:
  ```bash
  jwebserver -d /ruta/a/directorio  # Iniciar servidor para un directorio
  jwebserver -p 8080          # Iniciar en un puerto específico
  ```
- **Ejemplo**: `jwebserver -d ./html -p 8000` (servir archivos desde ./html en el puerto 8000).

---

### Consejos para Aprender Más
- **Documentación**: Ejecute `nombre_herramienta --help` o consulte la documentación de JDK de Oracle (ej. https://docs.oracle.com/en/java/javase/21/docs/specs/man/).
- **Páginas de Manual**: Use `man nombre_herramienta` para herramientas con páginas de manual.
- **Práctica**: Experimente en un proyecto de prueba para entender el comportamiento de las herramientas.
- **Herramientas de Monitoreo**: Para `jcmd`, `jmap`, `jstack`, etc., use `jps` para encontrar el PID de su proceso Java.
- **Depuración**: Combine `jdb`, `jhsdb` o `jconsole` para una depuración avanzada.

Si está trabajando en un proyecto de trading (como sugiere su directorio), herramientas como `javac`, `java`, `jar` y `jpackage` son probablemente las más relevantes para compilar, ejecutar y empaquetar su aplicación. Para ajustes de rendimiento, use `jstat`, `jmap` o `jfr`. ¡Avíseme si necesita una inmersión más profunda en alguna herramienta específica o ayuda con su proyecto de trading!
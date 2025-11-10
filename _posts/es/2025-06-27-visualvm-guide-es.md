---
audio: false
generated: true
lang: es
layout: post
title: 'Guía Completa de VisualVM: Perfilado y Monitoreo de Java'
translated: true
type: note
---

# Guía Completa de VisualVM

VisualVM es una herramienta de perfilado y monitoreo Java, potente y de código abierto, que proporciona una interfaz gráfica para analizar el rendimiento de aplicaciones Java. Está incluida en el Java Development Kit (JDK) y es particularmente útil para diagnosticar problemas de rendimiento, fugas de memoria y problemas relacionados con hilos. Esta guía cubre las características, configuración, uso y mejores prácticas de VisualVM para desarrolladores y administradores de sistemas.

## Tabla de Contenidos
1. [¿Qué es VisualVM?](#qué-es-visualvm)
2. [Características Clave de VisualVM](#características-clave-de-visualvm)
3. [Requisitos del Sistema](#requisitos-del-sistema)
4. [Instalando VisualVM](#instalando-visualvm)
5. [Iniciando VisualVM](#iniciando-visualvm)
6. [Conectando a Aplicaciones Java](#conectando-a-aplicaciones-java)
7. [Usando VisualVM para Monitoreo y Perfilado](#usando-visualvm-para-monitoreo-y-perfilado)
   - [Pestaña de Resumen](#pestaña-de-resumen)
   - [Pestaña de Monitor](#pestaña-de-monitor)
   - [Pestaña de Hilos](#pestaña-de-hilos)
   - [Sampler](#sampler)
   - [Profiler](#profiler)
   - [Análisis de Heap Dump](#análisis-de-heap-dump)
   - [Análisis de Thread Dump](#análisis-de-thread-dump)
   - [MBeans](#mbeans)
8. [Monitoreo Remoto](#monitoreo-remoto)
9. [Extendiendo VisualVM con Plugins](#extendiendo-visualvm-con-plugins)
10. [Mejores Prácticas](#mejores-prácticas)
11. [Solución de Problemas Comunes](#solución-de-problemas-comunes)
12. [Recursos Adicionales](#recursos-adicionales)

## ¿Qué es VisualVM?

VisualVM es una herramienta basada en Java que integra varias utilidades del JDK (como `jstack`, `jmap` y `jconsole`) en una única interfaz fácil de usar. Permite a los desarrolladores monitorear aplicaciones Java en tiempo real, perfilar el uso de CPU y memoria, analizar heap dumps y gestionar hilos. VisualVM es particularmente valiosa para identificar cuellos de botella en el rendimiento, fugas de memoria y problemas de hilos tanto en aplicaciones Java locales como remotas.

Desarrollada originalmente por Sun Microsystems, VisualVM es ahora parte del Oracle JDK y se mantiene activamente como un proyecto de código abierto. Es compatible con aplicaciones Java que se ejecutan en JDK 6 y versiones posteriores.

## Características Clave de VisualVM

- **Monitoreo en Tiempo Real**: Rastrea el uso de CPU, el consumo de memoria, la actividad de hilos y la recolección de basura.
- **Perfilado**: Ofrece perfilado de CPU y memoria para identificar cuellos de botella en el rendimiento y patrones de asignación de memoria.
- **Análisis de Heap Dump**: Permite inspeccionar el contenido de la memoria para diagnosticar fugas de memoria.
- **Análisis de Thread Dump**: Ayuda a analizar los estados de los hilos y detectar interbloqueos.
- **Gestión de MBeans**: Proporciona acceso a Java Management Extensions (JMX) para monitorear y gestionar aplicaciones.
- **Monitoreo Remoto**: Es compatible con el monitoreo de aplicaciones Java que se ejecutan en máquinas remotas.
- **Extensibilidad**: Es compatible con plugins para ampliar su funcionalidad, como la integración con frameworks específicos o herramientas de perfilado adicionales.
- **Ligero y Fácil de Usar**: Configuración mínima con una interfaz gráfica intuitiva.

## Requisitos del Sistema

Para usar VisualVM, asegúrese de lo siguiente:
- **Sistema Operativo**: Windows, macOS, Linux o cualquier SO compatible con una JVM.
- **Versión de Java**: JDK 6 o posterior (VisualVM se incluye con JDK 8 y versiones posteriores).
- **Memoria**: Al menos 512 MB de RAM libre para un monitoreo ligero; 1 GB o más para el análisis de heap dumps.
- **Espacio en Disco**: Aproximadamente 50 MB para la instalación de VisualVM.
- **Permisos**: Pueden requerirse privilegios de administrador para ciertas funciones (por ejemplo, acceder a procesos del sistema).

## Instalando VisualVM

VisualVM se incluye con Oracle JDK 8 y versiones posteriores, ubicado en el directorio `bin` de la instalación del JDK (ejecutable `jvisualvm`). Alternativamente, puede descargarlo como una aplicación independiente:

1. **Desde el JDK**:
   - Si tiene JDK 8 o posterior instalado, VisualVM ya está disponible en el directorio `JAVA_HOME/bin` como `jvisualvm`.
   - Ejecute el ejecutable `jvisualvm` para iniciar la herramienta.

2. **Descarga Independiente**:
   - Visite el [sitio web de VisualVM](https://visualvm.github.io/) para descargar la última versión independiente.
   - Extraiga el archivo ZIP a un directorio de su elección.
   - Ejecute el ejecutable `visualvm` (por ejemplo, `visualvm.exe` en Windows).

3. **Verificar la Instalación**:
   - Asegúrese de que la variable de entorno `JRE_HOME` o `JAVA_HOME` apunte a un JDK/JRE compatible.
   - Pruebe iniciando VisualVM.

## Iniciando VisualVM

Para iniciar VisualVM:
- **En Windows**: Haga doble clic en `jvisualvm.exe` en la carpeta `bin` del JDK o en el directorio de instalación independiente.
- **En macOS/Linux**: Ejecute `./jvisualvm` desde la terminal en el directorio `bin`.
- La interfaz de VisualVM se abrirá, mostrando una lista de aplicaciones Java locales en el panel izquierdo.

## Conectando a Aplicaciones Java

VisualVM puede monitorear aplicaciones Java tanto locales como remotas.

### Aplicaciones Locales
- Al iniciarse, VisualVM detecta automáticamente las aplicaciones Java en ejecución en la máquina local.
- Haga doble clic en una aplicación en el panel izquierdo para abrir su panel de monitoreo.
- Si una aplicación no aparece en la lista, asegúrese de que se esté ejecutando bajo una JVM compatible.

### Aplicaciones Remotas
Para monitorear una aplicación Java remota:
1. Habilite JMX en la aplicación remota agregando argumentos de la JVM (por ejemplo, `-Dcom.sun.management.jmxremote`).
2. En VisualVM, vaya a **Archivo > Agregar Conexión JMX**.
3. Ingrese la dirección IP del host remoto y el puerto (por ejemplo, `hostname:puerto`).
4. Proporcione las credenciales si la autenticación está habilitada.
5. Conéctese y monitoree la aplicación.

**Nota**: Para conexiones seguras, configure SSL y autenticación según sea necesario (consulte [Monitoreo Remoto](#monitoreo-remoto)).

## Usando VisualVM para Monitoreo y Perfilado

VisualVM proporciona varias pestañas y herramientas para analizar aplicaciones Java. A continuación, se presenta un desglose detallado de cada característica.

### Pestaña de Resumen
- Muestra información general sobre la aplicación, incluyendo:
  - Argumentos de la JVM
  - Propiedades del sistema
  - Classpath de la aplicación
  - PID (ID del Proceso)
- Útil para verificar la configuración de la aplicación.

### Pestaña de Monitor
- Proporciona gráficos en tiempo real para:
  - **Uso de CPU**: Rastrea el uso de CPU de la aplicación y del sistema.
  - **Memoria Heap**: Monitorea el uso del heap (Eden, Old Gen, PermGen/Metaspace) y la actividad de recolección de basura.
  - **Clases**: Muestra el número de clases cargadas.
  - **Hilos**: Muestra el número de hilos vivos y daemon.
- Permite activar manualmente la recolección de basura o los heap dumps.

### Pestaña de Hilos
- Visualiza los estados de los hilos (En Ejecución, Durmiendo, Esperando, etc.) a lo largo del tiempo.
- Proporciona funcionalidad de thread dump para capturar el estado actual de todos los hilos.
- Útil para identificar interbloqueos, hilos bloqueados o uso excesivo de hilos.

### Sampler
- Ofrece muestreo ligero de CPU y memoria para análisis de rendimiento.
- **Muestreo de CPU**:
  - Captura el tiempo de ejecución a nivel de método.
  - Identifica los métodos más activos que consumen la mayor parte del tiempo de CPU.
- **Muestreo de Memoria**:
  - Rastrea las asignaciones de objetos y el uso de memoria.
  - Ayuda a identificar objetos que consumen memoria en exceso.
- El muestreo tiene una sobrecarga menor que el perfilado pero proporciona datos menos detallados.

### Profiler
- Proporciona perfilado en profundidad de CPU y memoria.
- **Perfilado de CPU**:
  - Mide el tiempo de ejecución de los métodos.
  - Identifica cuellos de botella en el rendimiento a nivel de método.
- **Perfilado de Memoria**:
  - Rastrea las asignaciones y referencias de objetos.
  - Ayuda a detectar fugas de memoria identificando objetos que persisten inesperadamente.
- **Nota**: El perfilado tiene una sobrecarga mayor que el muestreo y puede ralentizar la aplicación.

### Análisis de Heap Dump
- Un heap dump es una instantánea de la memoria de la aplicación.
- Para generar un heap dump:
  1. Vaya a la pestaña **Monitor**.
  2. Haga clic en **Heap Dump**.
  3. Guarde el dump en un archivo `.hprof` o analícelo directamente en VisualVM.
- Características:
  - Ver instancias de clases, tamaños y referencias.
  - Identificar objetos con alto uso de memoria.
  - Detectar fugas de memoria analizando las rutas de retención de objetos.
- Use la consola **OQL (Object Query Language)** para consultas avanzadas del heap.

### Análisis de Thread Dump
- Captura el estado de todos los hilos en un momento específico.
- Para generar un thread dump:
  1. Vaya a la pestaña **Hilos**.
  2. Haga clic en **Thread Dump**.
  3. Analice el dump en VisualVM o expórtelo para herramientas externas.
- Útil para diagnosticar:
  - Interbloqueos
  - Hilos bloqueados
  - Problemas de contención de hilos

### MBeans
- Accede a JMX MBeans para gestionar y monitorear la aplicación.
- Características:
  - Ver y modificar atributos de MBeans.
  - Invocar operaciones de MBeans.
  - Monitorear notificaciones de MBeans.
- Útil para aplicaciones con instrumentación JMX personalizada.

## Monitoreo Remoto

Para monitorear aplicaciones Java remotas:
1. **Configurar la JVM Remota**:
   - Agregue los siguientes argumentos de la JVM a la aplicación remota:
     ```bash
     -Dcom.sun.management.jmxremote
     -Dcom.sun.management.jmxremote.port=<puerto>
     -Dcom.sun.management.jmxremote.ssl=false
     -Dcom.sun.management.jmxremote.authenticate=false
     ```
   - Para conexiones seguras, habilite SSL y autenticación:
     ```bash
     -Dcom.sun.management.jmxremote.ssl=true
     -Dcom.sun.management.jmxremote.authenticate=true
     -Dcom.sun.management.jmxremote.password.file=<archivo_contraseña>
     ```
2. **Configurar VisualVM**:
   - Agregue una conexión JMX en VisualVM usando la IP y el puerto del host remoto.
   - Proporcione las credenciales si se requieren.
3. **Configuración del Firewall**:
   - Asegúrese de que el puerto JMX esté abierto en el host remoto.
   - Use tunneling SSH para acceso remoto seguro si es necesario:
     ```bash
     ssh -L <puerto_local>:<host_remoto>:<puerto_remoto> usuario@host_remoto
     ```

## Extendiendo VisualVM con Plugins

VisualVM es compatible con plugins para mejorar su funcionalidad:
1. **Instalar Plugins**:
   - Vaya a **Herramientas > Plugins**.
   - Navegue por el Centro de Plugins para ver los plugins disponibles (por ejemplo, Visual GC, BTrace, plugins de JConsole).
   - Instálelos y reinicie VisualVM.
2. **Plugins Populares**:
   - **Visual GC**: Visualiza la actividad de recolección de basura.
   - **BTrace**: Proporciona trazado dinámico para aplicaciones Java.
   - **Plugins de JConsole**: Agrega funciones compatibles con JConsole.
3. **Plugins Personalizados**:
   - Descargue plugins del sitio web de VisualVM o de fuentes de terceros.
   - Coloque los archivos del plugin en el directorio `plugins` y reinicie VisualVM.

## Mejores Prácticas

- **Comience con el Muestreo**: Use el muestreo antes del perfilado para minimizar el impacto en el rendimiento.
- **Limite el Alcance del Perfilado**: Perfile paquetes o clases específicos para reducir la sobrecarga.
- **Heap Dumps Periódicos**: Programe heap dumps periódicos para aplicaciones de larga ejecución para rastrear tendencias de memoria.
- **Monitoree la Recolección de Basura**: Use el plugin Visual GC para analizar el rendimiento de la GC.
- **Conexiones Remotas Seguras**: Siempre use SSL y autenticación para el monitoreo remoto.
- **Guarde Instantáneas**: Guarde heap y thread dumps para análisis posteriores o colaboración.
- **Use OQL para Análisis Avanzado**: Aprenda OQL para consultas eficientes de heap dumps.
- **Monitoree el Uso de Recursos**: Asegúrese de que VisualVM tenga suficiente memoria para heap dumps grandes.

## Solución de Problemas Comunes

- **Aplicación No Detectada**:
  - Asegúrese de que la aplicación se esté ejecutando en una JVM compatible.
  - Verifique si la JVM está configurada para permitir conexiones JMX.
- **Alta Sobrecarga Durante el Perfilado**:
  - Cambie al muestreo para una sobrecarga menor.
  - Perfile clases o métodos específicos.
- **Problemas de Conexión para Monitoreo Remoto**:
  - Verifique la configuración del puerto JMX y del firewall.
  - Pruebe la conectividad usando `telnet <host> <puerto>`.
- **OutOfMemoryError en VisualVM**:
  - Aumente el tamaño del heap de VisualVM editando el archivo `visualvm.conf`:
    ```bash
    -J-Xmx<tamaño_memoria>m
    ```
- **El Análisis de Heap Dump es Lento**:
  - Use una máquina con más RAM.
  - Filtre clases para reducir el alcance del análisis.

## Recursos Adicionales

- **Sitio Web Oficial**: [visualvm.github.io](https://visualvm.github.io/)
- **Documentación**: [Documentación de VisualVM](https://visualvm.github.io/documentation.html)
- **Tutoriales**:
  - [Guía de VisualVM de Oracle](https://www.oracle.com/java/technologies/visualvm.html)
  - [Optimización del Rendimiento Java con VisualVM](https://www.baeldung.com/java-visualvm)
- **Comunidad**:
  - [Problemas de VisualVM en GitHub](https://github.com/visualvm/visualvm.github.io/issues)
  - [Etiqueta de VisualVM en Stack Overflow](https://stackoverflow.com/questions/tagged/visualvm)
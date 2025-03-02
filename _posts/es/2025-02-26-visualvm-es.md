---
audio: false
generated: true
lang: es
layout: post
title: Perfilado de aplicaciones Java con VisualVM
translated: true
---

Aquí tienes una guía clara y concisa sobre **cómo usar VisualVM** para monitorear y perfilar aplicaciones Java. VisualVM es una herramienta gratuita y poderosa incluida con el JDK que te ayuda a analizar el rendimiento, el uso de memoria y la actividad de hilos en tus aplicaciones Java.

---

### Paso 1: Instalar y Lanzar VisualVM
- **Verificar si VisualVM está instalado**: VisualVM generalmente viene con el JDK (versión 6 actualización 7 y posteriores). Búscalo en el directorio `bin` de tu instalación del JDK (por ejemplo, `jdk/bin/visualvm.exe` en Windows).
- **Descargar si es necesario**: Si no está incluido, descárgalo desde el [sitio web oficial de VisualVM](https://visualvm.github.io/).
- **Lanzar VisualVM**: Ejecuta el ejecutable `visualvm`. Al iniciar, verás una lista de procesos Java que actualmente se están ejecutando en tu máquina local.

---

### Paso 2: Conectar a tu Aplicación Java
- **Aplicaciones Locales**: VisualVM detecta automáticamente los procesos Java en ejecución en tu máquina. Haz doble clic en el proceso que deseas monitorear para conectarte a él.
- **Aplicaciones Remotas**: Para monitorear un proceso Java en otra máquina:
  1. Inicia la JVM remota con JMX habilitado (por ejemplo, agrega `-Dcom.sun.management.jmxremote` a los argumentos de la JVM).
  2. En VisualVM, haz clic derecho en **Remoto** en el panel izquierdo, selecciona **Agregar Host Remoto** e ingresa los detalles de la máquina remota.
  3. Una vez conectado, selecciona el proceso remoto para monitorear.

---

### Paso 3: Monitorear el Rendimiento de la Aplicación
Después de conectarte, la pestaña **Vista General** muestra detalles básicos como el ID del proceso y los argumentos de la JVM. Cambia a la pestaña **Monitorear** para obtener datos de rendimiento en tiempo real:
- **Uso de CPU**: Rastrear cuánto CPU está utilizando tu aplicación.
- **Uso de Memoria**: Muestra el consumo de heap y metaspace con el tiempo.
- **Hilos**: Muestra el número de hilos activos.
- **Recolección de Basura**: Monitorea la actividad de GC.

Estos gráficos te dan una visión general del estado de salud de tu aplicación.

---

### Paso 4: Perfilar el Uso de CPU y Memoria
Para un análisis más profundo, usa la pestaña **Perfilar**:
- **Perfilado de CPU**: Identifica los métodos que consumen más tiempo de CPU.
  1. Ve a la pestaña **Perfilar** y haz clic en **CPU**.
  2. Haz clic en **Iniciar** para comenzar el perfilado.
  3. Usa tu aplicación para generar la carga de trabajo que deseas analizar.
  4. Haz clic en **Detener** y revisa los resultados para ver cuáles métodos son más lentos.
- **Perfilado de Memoria**: Rastrear asignaciones de objetos y detectar fugas de memoria.
  1. En la pestaña **Perfilar**, haz clic en **Memoria**.
  2. Haz clic en **Iniciar**, usa tu aplicación, luego haz clic en **Detener**.
  3. Revisa los resultados para contar objetos y tamaños para detectar posibles problemas de memoria.

**Nota**: El perfilado añade sobrecarga, así que úsalo en entornos de desarrollo o pruebas, no en producción.

---

### Paso 5: Analizar Dumps de Heap y Hilos
- **Dumps de Heap**: Captura instantáneas de memoria para un análisis detallado.
  1. En la pestaña **Monitorear**, haz clic en **Dump de Heap**.
  2. Explora el dump en las vistas **Clases** o **Instancias** para ver las asignaciones de objetos.
  3. Busca patrones inusuales (por ejemplo, demasiados objetos) que puedan indicar fugas.
- **Dumps de Hilos**: Diagnostica problemas de hilos como bloqueos.
  1. En la pestaña **Hilos**, haz clic en **Dump de Hilos**.
  2. Revisa los estados de los hilos (por ejemplo, EJECUTANDO, ESPERANDO) para identificar problemas.

---

### Paso 6: Explorar Características Adicionales
- **Sampler**: Encontrado en la pestaña **Sampler**, proporciona un análisis ligero de CPU y memoria con menos sobrecarga que el perfilado completo.
- **Visual GC**: Instala el plugin Visual GC (a través de **Herramientas > Plugins**) para visualizar el comportamiento de la recolección de basura.
- **MBeans**: Usa la pestaña **MBeans** para ver y gestionar beans JMX para métricas personalizadas.

---

### Mejores Prácticas
- **Evitar Perfilado en Producción**: El perfilado ralentiza tu aplicación, así que quédate con configuraciones de desarrollo o pruebas.
- **Comenzar Simple**: Usa la pestaña **Monitorear** primero para obtener una línea de base antes de perfilar.
- **Enfocarse en Problemas Específicos**: Centra el perfilado en áreas problemáticas sospechosas para minimizar la sobrecarga.
- **Revisar Datos de GC**: Analiza las estadísticas de recolección de basura para optimizar el uso de memoria.

---

### Solución de Problemas
- **Aplicación No Mostrada**: Asegúrate de que esté ejecutándose con una JVM compatible y que VisualVM tenga acceso.
- **Problemas Remotos**: Confirma que la JVM remota esté configurada para JMX y que la configuración de red (por ejemplo, firewalls) permita la conexión.
- **Impacto en el Rendimiento**: Si el perfilado es demasiado lento, cambia al **Sampler** para una opción más ligera.

---

VisualVM es una excelente herramienta para entender y optimizar tus aplicaciones Java. Sigue estos pasos para monitorear el rendimiento, perfilar cuellos de botella y diagnosticar problemas de manera efectiva. Para más detalles, consulta la [documentación oficial de VisualVM](https://visualvm.github.io/documentation.html).
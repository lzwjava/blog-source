---
audio: false
generated: true
image: false
lang: es
layout: post
title: Guía del Puerto JMX Remoto 9001
translated: true
type: note
---

Un **agente remoto JMX** es parte de las Java Management Extensions (JMX). Te permite monitorizar y gestionar una aplicación Java en ejecución de forma remota. Cuando habilitas la gestión remota de JMX, la JVM inicia un agente que expone MBeans (Managed Beans) a través de un puerto TCP. Herramientas como **jconsole**, **VisualVM** o software de monitorización personalizado pueden conectarse a ese puerto para inspeccionar el uso de memoria, los estados de los hilos, la actividad del recolector de basura (GC) e incluso invocar operaciones.

Acerca del **puerto 9001**:

* El número de puerto real depende de cómo esté configurada la aplicación. Comúnmente verás 9001, 9090, 9091, etc.
* Si ves algo escuchando en `9001` y es un **agente remoto JMX**, significa que algún proceso Java se inició con propiedades del sistema como:

  ```bash
  -Dcom.sun.management.jmxremote
  -Dcom.sun.management.jmxremote.port=9001
  -Dcom.sun.management.jmxremote.authenticate=false
  -Dcom.sun.management.jmxremote.ssl=false
  ```

Esto abre JMX en el puerto `9001` sin autenticación/SSL (a menudo solo para uso interno o de desarrollo, ya que es inseguro si se expone públicamente).

---

### Cómo verificar qué programa usa el puerto JMX 9001 en Windows

1. Abre **Símbolo del sistema (como Administrador)**.
2. Ejecuta:

   ```cmd
   netstat -ano | findstr :9001
   ```

   Esto muestra el PID (Identificador de proceso) vinculado a ese puerto.
3. Para identificar el programa:

   ```cmd
   tasklist /FI "PID eq <PID>"
   ```

   Reemplaza `<PID>` con el número del paso 2.

---

### Cómo detenerlo / terminarlo

* Si confirmas que es un proceso Java que no deseas, termínalo con:

  ```cmd
   taskkill /PID <PID> /F
   ```
* Pero si es parte de tu servidor de aplicaciones (Tomcat, WebSphere, aplicación Spring Boot, etc.), es mejor detenerlo a través de su servicio/consola en lugar de terminar el proceso, para que se cierre de manera controlada.

---

👉 ¿Quieres que también te muestre cómo **deshabilitar el agente remoto JMX** en una aplicación Java para que no abra el puerto 9001 en absoluto?
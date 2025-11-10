---
audio: false
generated: true
image: false
lang: es
layout: post
title: Guía del Puerto del Agente Remoto JMX
translated: true
type: note
---

El **agente remoto JMX** es parte de la tecnología Java Management Extensions (JMX). Permite a los administradores o herramientas de monitoreo conectarse a una aplicación Java en ejecución desde fuera del proceso de la JVM, típicamente a través de TCP/IP. Esto se usa comúnmente para el monitoreo, diagnóstico y gestión de aplicaciones Java en producción.

Aquí hay un desglose:

### 1. Qué es el Agente Remoto JMX

* Expone los componentes internos de la JVM (uso de memoria, actividad de hilos, recolección de basura, carga de clases, etc.) como *Managed Beans (MBeans)*.
* Te permite conectarte de forma remota (por ejemplo, mediante **jconsole**, **VisualVM** o herramientas de monitoreo como los exportadores de Prometheus).
* Normalmente se habilita mediante flags de inicio de la JVM como:

  ```bash
  -Dcom.sun.management.jmxremote
  -Dcom.sun.management.jmxremote.port=9091
  -Dcom.sun.management.jmxremote.authenticate=false
  -Dcom.sun.management.jmxremote.ssl=false
  ```
* Una vez habilitado, la JVM ejecuta un servidor conector RMI (Remote Method Invocation) vinculado al puerto especificado.

### 2. Sobre el Puerto 9091

* El número **9091** en sí mismo no es especial; es simplemente un puerto TCP que configuras para las conexiones JMX.
* A menudo los administradores eligen el 9091 (o el 9010, 9999, etc.) por conveniencia y para evitar conflictos con los puertos estándar.
* Cuando escucha en `9091`, la JVM aceptará conexiones JMX remotas en ese puerto.
* Si se deja sin seguridad (`authenticate=false, ssl=false`), cualquier persona con acceso a la red puede controlar u observar tu JVM, lo que supone un riesgo de seguridad importante.

### 3. Uso Típico

* Monitoreo con **JConsole**:

  ```bash
  jconsole host:9091
  ```
* Integración con sistemas de monitoreo (por ejemplo, Prometheus JMX Exporter).
* Gestión remota durante la resolución de problemas (por ejemplo, verificar volcados de memoria, hilos, comportamiento del recolector de basura).

### 4. Consideraciones de Seguridad

* Siempre protege el puerto JMX con:

  * Firewalls de red (restringir el acceso).
  * Autenticación (archivos `password` y `access`).
  * SSL si es necesario.
* De lo contrario, exponerlo en el puerto 9091 sin seguridad es equivalente a dar control a nivel de shell remoto de tu JVM.

---

✅ En resumen: **agente remoto JMX en el puerto 9091** significa que tu JVM está exponiendo una interfaz de gestión y monitoreo a través del puerto TCP 9091, que puede ser utilizada por herramientas como JConsole o Prometheus, pero debe estar protegida.

¿Quieres que te muestre los **flags exactos de la JVM** para habilitarlo con autenticación por contraseña (en lugar del modo no seguro)?
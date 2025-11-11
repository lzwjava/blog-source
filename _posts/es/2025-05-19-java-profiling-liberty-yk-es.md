---
audio: false
generated: true
image: false
lang: es
layout: post
title: Perfilando Liberty con YourKit Java Profiler
translated: true
type: note
---

WebSphere Liberty puede integrarse con YourKit Java Profiler sin problemas, ya que Liberty es simplemente otro runtime basado en JVM. Así es como funciona típicamente:

---

### 1. Cómo funciona la integración

YourKit Java Profiler no necesita plugins específicos para Liberty; funciona adjuntándose al proceso de JVM en el que se ejecuta Liberty. Una vez adjuntado, intercepta llamadas a métodos, asignaciones de memoria, actividad de hilos y otros eventos del runtime.
Liberty se ejecuta en la JVM OpenJ9 (o HotSpot), por lo que puedes habilitar la generación de perfiles agregando el agente de YourKit al inicio de Liberty.

---

### 2. Adjuntar el agente de YourKit

Hay dos formas principales:

* **Adjuntado al inicio (preferido para servidores)**
  Agrega las opciones del agente de YourKit al archivo `jvm.options` de Liberty (en `<wlp_home>/usr/servers/<nombre_del_servidor>/`).
  Ejemplo:

  ```
  -agentpath:/ruta/hacia/yourkit/bin/linux-x86-64/libyjpagent.so=port=10001,listen=all
  ```

  Esto carga el agente del profiler tan pronto como se inicia el servidor.

* **Adjuntado bajo demanda (dinámico)**
  Si Liberty ya se está ejecutando, puedes adjuntar YourKit a través de la GUI. Este escanea las JVMs en ejecución y te permite conectarte sin reiniciar. Es útil para depuración en producción, pero requiere permisos (mismo usuario / tools.jar del JDK).

---

### 3. Generación de perfiles en contexto de Liberty

Cuando se ejecuta en Liberty, es posible que desees:

* **Filtrar por paquetes de aplicación** para no ahogarte en el código interno de Liberty.
* **Usar la vista de árbol de llamadas / puntos críticos** para analizar servlets lentos, endpoints JAX-RS o beans CDI.
* **Monitorear JDBC y grupos de hilos** ya que las aplicaciones Liberty a menudo dependen de recursos gestionados por el contenedor. YourKit puede rastrear llamadas JDBC y medir tiempos de espera.
* **Manejar múltiples aplicaciones** – si Liberty aloja varias aplicaciones, usa los filtros de hilos y clases de YourKit para limitar la generación de perfiles a la que te interesa.

---

### 4. Consideraciones de rendimiento

* La generación de perfiles siempre añade sobrecarga. Para desarrollo está bien usar la generación de perfiles completa de CPU/memoria; en producción usa el modo *muestreo* en lugar de la instrumentación.
* La carga de clases modular de Liberty a veces puede causar nombres de clase duplicados; YourKit generalmente maneja esto, pero tenlo en cuenta al filtrar.
* Si usas IBM JDK con Liberty, asegúrate de descargar el agente de YourKit construido para IBM J9/OpenJ9, no solo para HotSpot.

---

### 5. Flujo de trabajo típico

1. Instala YourKit en tu máquina de desarrollo.
2. Modifica el archivo `jvm.options` de Liberty con la ruta del agente.
3. Inicia Liberty.
4. Conéctate desde la GUI de YourKit a la JVM de Liberty (vía socket o attach).
5. Genera perfiles de tus endpoints, uso de memoria o bloqueos de hilos.
6. Guarda instantáneas para análisis posterior.

---

👉 ¿Quieres que te proporcione un **ejemplo de configuración paso a paso** para Liberty en **OpenJ9** (la JVM predeterminada de Liberty) con YourKit, incluyendo configuraciones de ejemplo en `jvm.options` para generación de perfiles de CPU vs memoria?
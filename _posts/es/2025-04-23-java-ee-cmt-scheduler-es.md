---
audio: false
generated: true
image: false
lang: es
layout: post
title: Programador de Tareas Gestionado por el Contenedor Java EE
translated: true
type: note
---

Un **ManagedScheduledExecutorService** es un recurso de Java EE (Jakarta EE) proporcionado por el servidor de aplicaciones (por ejemplo, WebSphere, WebLogic, WildFly) que te permite programar tareas para que se ejecuten en el futuro o periódicamente, similar a `ScheduledExecutorService` en Java SE estándar, pero con **beneficios gestionados por el contenedor**:

---

### Cómo Funciona

* **Integración con el contenedor**
  Está gestionado por el servidor de aplicaciones, lo que significa que las tareas se ejecutan con el contexto de seguridad, el cargador de clases y los límites de transacción de la aplicación. Esto evita problemas comunes de los hilos no gestionados en Java EE.

* **Capacidades de programación**
  Puedes programar tareas para:

  * Ejecutarse una vez después de un retraso.
  * Ejecutarse a una tasa fija (por ejemplo, cada 5 segundos).
  * Ejecutarse con un retraso fijo entre ejecuciones.

* **Gestión del ciclo de vida**
  El contenedor se encarga del ciclo de vida del grupo de hilos, la limpieza y la gestión de recursos. No necesitas apagarlo manualmente como un `ExecutorService` común.

---

### Tiempo de Espera (Timeout)

* No hay una única configuración de "tiempo de espera" para el grupo en sí, pero dos cosas son relevantes:

  * **Tiempo de espera de ejecución de la tarea**: Puedes envolver tareas con `ManagedTaskListener` y especificar propiedades como `ManagedTask.TIMEOUT` (dependiendo del soporte del proveedor). Algunos servidores te permiten configurar tiempos de espera predeterminados para las tareas, de modo que las tareas que se bloqueen sean canceladas por el contenedor.
  * **Tiempo de espera de `future.get()`**: Como con el `ScheduledExecutorService` regular, puedes usar `future.get(timeout, unit)` para limitar cuánto tiempo esperas por los resultados.

Por lo tanto, el "tiempo de espera" suele ser por tarea, no a nivel del grupo.

---

### Configuración del Tamaño del Grupo

* Cada servidor de aplicaciones tiene su propia configuración para el grupo de hilos subyacente.
  Ejemplos:

  * **WebSphere Liberty / Traditional**: configuras el grupo en `server.xml` bajo `<managedScheduledExecutorService>` con atributos como `corePoolSize` y `maximumPoolSize`.
  * **WebLogic**: lo configuras a través de la Consola de Administración o `weblogic-managed-executor`.
  * **WildFly / JBoss EAP**: configurado bajo el subsistema EE.

* Las configuraciones típicas del grupo incluyen:

  * **Tamaño del grupo central (Core pool size)**: número mínimo de hilos que se mantienen activos.
  * **Tamaño máximo del grupo (Maximum pool size)**: número máximo de hilos concurrentes.
  * **Tamaño de la cola / política de rechazo**: qué sucede cuando todos los hilos están ocupados.
  * **Tiempo de mantenimiento activo (Keep-alive time)**: cuánto tiempo se mantienen los hilos inactivos antes de ser liberados.

---

✅ **En resumen**:
`ManagedScheduledExecutorService` funciona como el programador de Java SE pero es consciente del contenedor, por lo que obtienes un uso seguro de hilos en aplicaciones Java EE. El tiempo de espera se aplica normalmente por tarea (ya sea a través de la API o la configuración del servidor), mientras que el tamaño del grupo (hilos centrales/máximos) se configura a nivel del contenedor, no en tu código de aplicación.

---

¿Quieres que te muestre un **ejemplo de fragmento de configuración para WebSphere Liberty** para el tamaño del grupo y el tiempo de espera?
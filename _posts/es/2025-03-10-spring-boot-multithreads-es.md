---
audio: false
generated: true
lang: es
layout: post
title: Spring Boot Multihilo
translated: true
type: note
---

En un proyecto de Spring Boot, los conceptos de "executors" e "hilos" (threads) típicamente se relacionan con cómo la aplicación maneja tareas concurrentes y gestiona su carga de trabajo, especialmente en escenarios que involucran procesamiento asíncrono, programación de tareas o manejo de múltiples solicitudes. Desglosemos esto paso a paso:

---

### **¿Qué son los Executors y los Threads en Spring Boot?**

1. **Threads (Hilos)**:
   - Un hilo es la unidad más pequeña de ejecución en un programa Java. En una aplicación Spring Boot, los hilos se utilizan para manejar tareas como procesar solicitudes HTTP, ejecutar trabajos en segundo plano o realizar operaciones de E/S.
   - Spring Boot, por defecto, se ejecuta dentro de un servidor web integrado (por ejemplo, Tomcat, Jetty o Undertow), que utiliza un grupo de hilos (thread pool) para gestionar las solicitudes entrantes. Cada solicitud normalmente se asigna a un hilo de este grupo.

2. **Executors**:
   - Un `Executor` en Java (y Spring Boot) es una abstracción sobre la gestión de hilos. Es parte del paquete `java.util.concurrent` y proporciona una forma de gestionar y ejecutar tareas de forma asíncrona sin crear y gestionar hilos manualmente.
   - En Spring Boot, los executors se usan a menudo para descargar tareas del hilo principal de la aplicación (por ejemplo, el hilo que maneja una solicitud HTTP) a un grupo de hilos separado. Esto es útil para tareas de larga duración, procesamiento en paralelo o trabajos programados.

3. **Contexto Específico de Spring**:
   - Spring Boot proporciona utilidades como `ThreadPoolTaskExecutor` (para ejecución general de tareas) y `ThreadPoolTaskScheduler` (para tareas programadas) para simplificar el trabajo con executors e hilos.
   - Estos se construyen sobre `ExecutorService` de Java y se usan comúnmente para:
     - Ejecución asíncrona de métodos (mediante `@Async`).
     - Programación de tareas (mediante `@Scheduled`).
     - Gestionar cargas de trabajo en escenarios de alta concurrencia.

---

### **¿Cómo funcionan en Spring Boot?**

#### **1. Gestión Predeterminada de Hilos en Spring Boot**
- Cuando inicias una aplicación web Spring Boot, el servidor integrado (por ejemplo, Tomcat) inicializa un grupo de hilos para manejar las solicitudes HTTP entrantes.
- Por ejemplo, la configuración predeterminada de Tomcat podría asignar 200 hilos (configurable mediante `server.tomcat.threads.max` en `application.properties`).
- A cada solicitud entrante se le asigna un hilo de este grupo. Si todos los hilos están ocupados y llega una nueva solicitud, esta puede ponerse en cola (dependiendo de la configuración del servidor) o ser rechazada.

#### **2. Executors en Spring Boot**
- Spring Boot proporciona la interfaz `TaskExecutor` (una extensión del `Executor` de Java) para gestionar grupos de hilos personalizados para tareas específicas.
- Una implementación común es `ThreadPoolTaskExecutor`, que te permite configurar:
  - **Core Pool Size**: El número de hilos que siempre se mantienen activos.
  - **Max Pool Size**: El número máximo de hilos permitidos en el grupo.
  - **Queue Capacity**: El número de tareas que pueden esperar en la cola antes de que se generen nuevos hilos (hasta el tamaño máximo del grupo).
  - **Thread Naming**: Para una depuración más fácil (por ejemplo, "my-executor-thread-1").

  Ejemplo de configuración en una aplicación Spring Boot:
  ```java
  import org.springframework.context.annotation.Bean;
  import org.springframework.context.annotation.Configuration;
  import org.springframework.scheduling.concurrent.ThreadPoolTaskExecutor;

  @Configuration
  public class ExecutorConfig {

      @Bean
      public ThreadPoolTaskExecutor taskExecutor() {
          ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
          executor.setCorePoolSize(5);      // Mínimo 5 hilos
          executor.setMaxPoolSize(10);      // Máximo 10 hilos
          executor.setQueueCapacity(100);   // Cola de hasta 100 tareas
          executor.setThreadNamePrefix("MyExecutor-");
          executor.initialize();
          return executor;
      }
  }
  ```

#### **3. Usando `@Async` con Executors**
- Spring Boot admite la ejecución asíncrona de métodos con la anotación `@Async`. Cuando anotas un método con `@Async`, este se ejecuta en un hilo separado gestionado por un executor.
- Por defecto, Spring utiliza un `SimpleAsyncTaskExecutor`, que crea un nuevo hilo para cada tarea (no es ideal para cargas altas). Para optimizar esto, puedes proporcionar tu propio `ThreadPoolTaskExecutor` (como se muestra arriba) y referenciarlo:
  ```java
  @Service
  public class MyService {

      @Async("taskExecutor") // Hace referencia al nombre del bean de la configuración
      public void doAsyncTask() {
          System.out.println("Running on thread: " + Thread.currentThread().getName());
      }
  }
  ```

#### **4. Programación de Tareas (Task Scheduling)**
- Para tareas programadas (por ejemplo, ejecutar un trabajo cada 5 minutos), Spring Boot utiliza `ThreadPoolTaskScheduler`. Es similar a `ThreadPoolTaskExecutor` pero adaptado para programación.
- Ejemplo:
  ```java
  @Scheduled(fixedRate = 5000) // Se ejecuta cada 5 segundos
  public void scheduledTask() {
      System.out.println("Scheduled task on: " + Thread.currentThread().getName());
  }
  ```

#### **5. Cómo interactúan los Hilos y los Executors**
- Cuando se envía una tarea a un executor (por ejemplo, mediante `@Async` o envío manual), el executor decide si:
  - Usar un hilo inactivo existente del grupo.
  - Crear un nuevo hilo (si se supera el tamaño del grupo central pero se está por debajo del tamaño máximo del grupo).
  - Poner la tarea en cola (si se alcanza el tamaño máximo del grupo y la cola no está llena).
  - Rechazar la tarea (si la cola está llena y no se pueden crear más hilos).
- Los hilos ejecutan las tareas y vuelven al grupo cuando terminan, listos para la siguiente tarea.

---

### **Ejemplo Práctico**
Imagina una aplicación Spring Boot que maneja registros de usuarios:
- **Hilo de Solicitud HTTP**: Un usuario envía un formulario de registro, manejado por un hilo del grupo de hilos de Tomcat.
- **Tarea Asíncrona**: El envío de un correo electrónico de confirmación se descarga a un `ThreadPoolTaskExecutor` mediante un método `@Async`, para que el hilo HTTP pueda responder inmediatamente sin esperar a que se envíe el correo.
- **Tarea Programada**: Un trabajo de limpieza se ejecuta cada hora para eliminar cuentas no verificadas, gestionado por un `ThreadPoolTaskScheduler`.

---

### **Puntos Clave**
- **Los Executors** abstraen la gestión de hilos, facilitando la escalabilidad y el ajuste de la concurrencia.
- **Los Threads** realizan el trabajo real, y su ciclo de vida es gestionado por los executors o el servidor web.
- Los valores predeterminados de Spring Boot son suficientes para aplicaciones pequeñas, pero para aplicaciones complejas o de alta carga, configurarás executors personalizados para optimizar el rendimiento.

Si tienes en mente un proyecto específico de Spring Boot y deseas ayuda para analizar su configuración de executor/hilos, ¡no dudes en compartir más detalles!
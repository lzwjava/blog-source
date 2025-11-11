---
audio: false
generated: true
lang: es
layout: post
title: FuturoCompletable en Java
translated: true
type: note
---

En un proyecto Java Spring Boot, no existe un equivalente directo al `Promise.all` de JavaScript, que espera a que se completen múltiples promesas y proporciona sus resultados. Sin embargo, puedes lograr una funcionalidad similar—ejecutar múltiples tareas concurrentemente en un bucle for y usar sus resultados después de que todos los hilos terminen—usando `CompletableFuture` del paquete `java.util.concurrent`, específicamente con el método `CompletableFuture.allOf`. Este enfoque es adecuado para un proyecto Spring Boot, especialmente cuando se combina con las características de programación asíncrona de Spring. A continuación, explicaré cómo hacer esto paso a paso, incluyendo un ejemplo completo.

### ¿Por qué `CompletableFuture`?
`CompletableFuture` (introducido en Java 8) te permite realizar operaciones asíncronas y gestionar su finalización. El método `allOf` toma múltiples instancias de `CompletableFuture` y retorna un nuevo `CompletableFuture` que se completa cuando todos los futuros dados han terminado, haciéndolo ideal para tu escenario donde quieres:
- Ejecutar tareas en paralelo dentro de un bucle for.
- Esperar a que todas las tareas finalicen.
- Usar los resultados posteriormente.

### Pasos para Implementar
Así es como puedes estructurar tu solución en un proyecto Spring Boot:

1.  **Definir las Tareas Asíncronas**
    Cada iteración de tu bucle for representa una tarea que puede ejecutarse de forma independiente. Estas tareas retornarán instancias de `CompletableFuture`, representando sus resultados eventuales.

2.  **Recolectar los Futures**
    Almacena todos los objetos `CompletableFuture` en una lista a medida que los creas en el bucle.

3.  **Esperar a que Todas las Tareas se Completen**
    Usa `CompletableFuture.allOf` para combinar los futuros en un único futuro que se completa cuando todas las tareas han terminado.

4.  **Recuperar y Usar los Resultados**
    Después de que todas las tareas estén completas, extrae los resultados de cada `CompletableFuture` y procésalos según sea necesario.

5.  **Manejar Excepciones**
    Ten en cuenta los posibles errores durante la ejecución de las tareas.

### Ejemplo de Implementación
Supongamos que tienes una lista de elementos para procesar concurrentemente (por ejemplo, llamar a un servicio o realizar algún cálculo). Aquí hay dos enfoques: uno usando la anotación `@Async` de Spring y otro usando `CompletableFuture.supplyAsync`.

#### Enfoque 1: Usando `@Async` con Spring
Spring Boot proporciona la anotación `@Async` para ejecutar métodos de forma asíncrona. Necesitarás habilitar el soporte asíncrono en tu aplicación.

**Paso 1: Habilitar Soporte Async**
Añade la anotación `@EnableAsync` a una clase de configuración o a tu clase principal de la aplicación:

```java
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableAsync;

@SpringBootApplication
@EnableAsync
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

**Paso 2: Definir un Servicio con un Método Async**
Crea un servicio con un método que procese cada elemento de forma asíncrona:

```java
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;
import java.util.concurrent.CompletableFuture;

@Service
public class MyService {

    @Async
    public CompletableFuture<String> processItem(String item) {
        // Simular algún trabajo (ej., E/S o cálculo)
        try {
            Thread.sleep(1000); // Retraso de 1 segundo
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            return CompletableFuture.completedFuture("Interrupted: " + item);
        }
        return CompletableFuture.completedFuture("Processed: " + item);
    }
}
```

**Paso 3: Procesar Elementos en un Controlador o Servicio**
En tu controlador u otro servicio, usa un bucle for para enviar tareas y esperar todos los resultados:

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.concurrent.CompletableFuture;

@Component
public class ItemProcessor {

    @Autowired
    private MyService myService;

    public List<String> processItems(List<String> items) {
        // Lista para contener todos los futures
        List<CompletableFuture<String>> futures = new ArrayList<>();

        // Enviar cada tarea en el bucle for
        for (String item : items) {
            CompletableFuture<String> future = myService.processItem(item);
            futures.add(future);
        }

        // Esperar a que todas las tareas se completen
        CompletableFuture<Void> allFutures = CompletableFuture.allOf(
            futures.toArray(new CompletableFuture[0])
        );

        // Bloquear hasta que todas las tareas estén hechas
        allFutures.join();

        // Recolectar resultados
        List<String> results = futures.stream()
            .map(CompletableFuture::join) // Obtener cada resultado
            .collect(Collectors.toList());

        return results;
    }
}
```

**Ejemplo de Uso:**
```java
List<String> items = Arrays.asList("Item1", "Item2", "Item3");
List<String> results = itemProcessor.processItems(items);
System.out.println(results); // Imprime: [Processed: Item1, Processed: Item2, Processed: Item3]
```

#### Enfoque 2: Usando `CompletableFuture.supplyAsync`
Si prefieres no usar `@Async`, puedes gestionar los hilos manualmente con un `Executor` y `CompletableFuture.supplyAsync`.

**Paso 1: Configurar un Thread Pool**
Define un bean `TaskExecutor` para controlar el grupo de hilos:

```java
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.concurrent.ThreadPoolTaskExecutor;
import org.springframework.core.task.TaskExecutor;

@Configuration
public class AsyncConfig {

    @Bean
    public TaskExecutor taskExecutor() {
        ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
        executor.setCorePoolSize(5);    // Número de hilos a mantener en el pool
        executor.setMaxPoolSize(10);    // Número máximo de hilos
        executor.setQueueCapacity(25);  // Capacidad de la cola para tareas pendientes
        executor.initialize();
        return executor;
    }
}
```

**Paso 2: Procesar Elementos con `supplyAsync`**
Usa el ejecutor para ejecutar tareas de forma asíncrona:

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import java.util.List;
import java.util.concurrent.CompletableFuture;
import java.util.stream.Collectors;
import org.springframework.core.task.TaskExecutor;

@Component
public class ItemProcessor {

    @Autowired
    private TaskExecutor taskExecutor;

    public List<String> processItems(List<String> items) {
        // Crear futures usando supplyAsync
        List<CompletableFuture<String>> futures = items.stream()
            .map(item -> CompletableFuture.supplyAsync(() -> processItem(item), taskExecutor))
            .collect(Collectors.toList());

        // Esperar a que todas las tareas se completen
        CompletableFuture.allOf(futures.toArray(new CompletableFuture[0])).join();

        // Recolectar resultados
        List<String> results = futures.stream()
            .map(CompletableFuture::join)
            .collect(Collectors.toList());

        return results;
    }

    private String processItem(String item) {
        // Simular algún trabajo
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            return "Interrupted: " + item;
        }
        return "Processed: " + item;
    }
}
```

### Puntos Clave
- **Esperar por la Finalización**: `CompletableFuture.allOf(...).join()` o `.get()` asegura que el hilo principal espere hasta que todas las tareas terminen. Usa `join()` para evitar manejar excepciones verificadas; lanza `CompletionException` si una tarea falla.
- **Manejo de Excepciones**: Envuelve la llamada a `.join()` o `.get()` en un bloque try-catch si necesitas manejar excepciones:

```java
try {
    allFutures.get();
} catch (InterruptedException e) {
    Thread.currentThread().interrupt();
    // Manejar interrupción
} catch (ExecutionException e) {
    // Manejar fallos de tareas
    e.printStackTrace();
}
```

- **Configuración del Thread Pool**: Ajusta el tamaño del grupo de hilos según tu carga de trabajo. Para tareas vinculadas a E/S (ej., llamadas a bases de datos, peticiones API), un grupo más grande (ej., 5–10 hilos) está bien. Para tareas vinculadas a CPU, coincide con el número de núcleos de CPU (ej., `Runtime.getRuntime().availableProcessors()`).
- **Orden de los Resultados**: Los resultados mantienen el orden de la lista de entrada ya que los futures se recogen en el mismo orden que el bucle.

### ¿Qué Enfoque Elegir?
- **Usa `@Async`** si tus tareas forman parte naturalmente de un servicio Spring y quieres que Spring gestione los hilos. Es más limpio y se integra bien con Spring Boot.
- **Usa `supplyAsync`** si necesitas más control sobre la ejecución de las tareas o no quieres depender del framework asíncrono de Spring.

### Respuesta Final
Para replicar `Promise.all` en un proyecto Java Spring Boot para un trabajo de bucle for donde quieres usar los resultados de los hilos después de la ejecución multihilo, usa `CompletableFuture.allOf` con una lista de instancias de `CompletableFuture`. El enfoque con `@Async` de Spring es recomendado por su simplicidad, pero `supplyAsync` con un ejecutor personalizado también funciona. El ejemplo anterior con `@Async` demuestra esto:

- Crea instancias de `CompletableFuture` en un bucle for usando un método `@Async`.
- Usa `CompletableFuture.allOf` para esperar todas las tareas.
- Recoge y usa los resultados después de la finalización.

Esto asegura que todas las tareas se ejecuten concurrentemente, y puedes procesar sus resultados una vez que todas hayan terminado, cumpliendo con tus requisitos de manera efectiva.
---
audio: false
generated: true
lang: es
layout: post
title: Comprensión de ExecutorService y ThreadPoolExecutor
translated: true
type: note
---

Configurar parámetros para un `ExecutorService` en Java implica configurar su grupo de subprocesos para optimizar el rendimiento según los recursos de su sistema (como una CPU de 8 núcleos) y la naturaleza de sus tareas (por ejemplo, vinculadas a CPU o vinculadas a E/S). A continuación, explicaré cómo configurar un `ExecutorService` para una CPU de 8 núcleos, centrándome en implementaciones comunes como `ThreadPoolExecutor`, y proporcionaré ejemplos prácticos adaptados a su caso de uso.

---

### Entendiendo ExecutorService y ThreadPoolExecutor

La interfaz `ExecutorService` es típicamente implementada por clases como `ThreadPoolExecutor`, que permite un control detallado sobre los parámetros del grupo de subprocesos. Al configurarlo para una CPU de 8 núcleos, debe considerar:
- **Tamaño del grupo central (Core Pool Size)**: El número de subprocesos que se mantienen activos incluso cuando están inactivos.
- **Tamaño máximo del grupo (Maximum Pool Size)**: El número máximo de subprocesos permitidos en el grupo.
- **Capacidad de la cola (Queue Capacity)**: El tamaño de la cola de tareas para retener tareas antes de que se ejecuten.
- **Estrategia de creación de subprocesos**: Cómo se crean y gestionan los subprocesos.
- **Tipo de tarea**: Si las tareas están vinculadas a la CPU (por ejemplo, cálculos) o vinculadas a E/S (por ejemplo, llamadas a bases de datos).

Para una CPU de 8 núcleos, la configuración óptima depende de si sus tareas son intensivas en CPU o intensivas en E/S (como el acceso a bases de datos en su escenario de validación).

---

### Parámetros clave para ThreadPoolExecutor

Así es como puede configurar un `ThreadPoolExecutor`:

```java
ThreadPoolExecutor executor = new ThreadPoolExecutor(
    corePoolSize,      // Número de subprocesos a mantener activos
    maximumPoolSize,   // Número máximo de subprocesos permitidos
    keepAliveTime,     // Tiempo que los subprocesos inactivos se mantienen activos (ej., 60L)
    TimeUnit.SECONDS,  // Unidad para keepAliveTime
    workQueue,         // Cola para retener tareas (ej., new LinkedBlockingQueue<>())
    threadFactory,     // Opcional: Nombrado personalizado de subprocesos o prioridad
    rejectionHandler   // Qué hacer cuando la cola está llena y se alcanza el máximo de subprocesos
);
```

#### Desglose de parámetros
1. **`corePoolSize`**:
   - Número mínimo de subprocesos que siempre se mantienen activos.
   - Para tareas vinculadas a CPU: Establezca esto al número de núcleos (ej., 8).
   - Para tareas vinculadas a E/S: Puede ser mayor (ej., 16 o más), ya que los subprocesos pueden pasar tiempo esperando.

2. **`maximumPoolSize`**:
   - Subprocesos máximos permitidos si la cola se llena.
   - Para tareas vinculadas a CPU: A menudo igual a `corePoolSize` (ej., 8).
   - Para tareas vinculadas a E/S: Mayor para manejar picos (ej., 20 o 50).

3. **`keepAliveTime`**:
   - Cuánto tiempo los subprocesos inactivos excedentes (más allá de `corePoolSize`) se mantienen activos antes de terminar.
   - Ejemplo: `60L` segundos es un valor predeterminado común.

4. **`workQueue`**:
   - Cola para tareas en espera de ser ejecutadas:
     - `LinkedBlockingQueue`: Cola sin límite (predeterminada en muchos casos).
     - `ArrayBlockingQueue`: Cola con límite (ej., `new ArrayBlockingQueue<>(100)`).
     - `SynchronousQueue`: Sin cola; las tareas se pasan directamente a los subprocesos (utilizada en `Executors.newCachedThreadPool()`).

5. **`threadFactory`** (Opcional):
   - Personaliza la creación de subprocesos (ej., nombrar subprocesos para depuración).
   - Predeterminado: `Executors.defaultThreadFactory()`.

6. **`rejectionHandler`** (Opcional):
   - Política cuando las tareas exceden `maximumPoolSize` y la capacidad de la cola:
     - `AbortPolicy` (predeterminado): Lanza `RejectedExecutionException`.
     - `CallerRunsPolicy`: Ejecuta la tarea en el subproceso que llama.
     - `DiscardPolicy`: Descarta la tarea silenciosamente.

---

### Configuración para una CPU de 8 Núcleos

#### Escenario 1: Tareas Vinculadas a CPU
Si sus tareas son intensivas en CPU (por ejemplo, cálculos pesados), desea igualar el número de subprocesos a los núcleos de la CPU para maximizar el rendimiento sin sobrecargar el sistema.

```java
import java.util.concurrent.*;

public class ExecutorConfig {
    public static ExecutorService createCpuBoundExecutor() {
        int corePoolSize = 8; // Coincide con 8 núcleos
        int maximumPoolSize = 8;
        long keepAliveTime = 60L; // 60 segundos

        return new ThreadPoolExecutor(
            corePoolSize,
            maximumPoolSize,
            keepAliveTime,
            TimeUnit.SECONDS,
            new LinkedBlockingQueue<>(), // Cola sin límite
            Executors.defaultThreadFactory(),
            new ThreadPoolExecutor.AbortPolicy()
        );
    }
}
```

- **Por qué**: 8 subprocesos utilizan completamente los 8 núcleos. Agregar más subprocesos causaría sobrecarga por cambio de contexto, reduciendo el rendimiento.

#### Escenario 2: Tareas Vinculadas a E/S (ej., Validación con Base de Datos)
Para su escenario de validación con acceso a base de datos, las tareas están vinculadas a E/S: los subprocesos pasan tiempo esperando respuestas de la base de datos. Puede usar más subprocesos que núcleos para mantener la CPU ocupada mientras algunos subprocesos esperan.

```java
import java.util.concurrent.*;

public class ExecutorConfig {
    public static ExecutorService createIoBoundExecutor() {
        int corePoolSize = 16; // 2x núcleos para tareas vinculadas a E/S
        int maximumPoolSize = 20; // Permitir cierta capacidad para picos
        long keepAliveTime = 60L;

        return new ThreadPoolExecutor(
            corePoolSize,
            maximumPoolSize,
            keepAliveTime,
            TimeUnit.SECONDS,
            new ArrayBlockingQueue<>(100), // Cola con límite para limitar memoria
            new ThreadFactoryBuilder().setNameFormat("validation-thread-%d").build(), // Nombrado personalizado
            new ThreadPoolExecutor.CallerRunsPolicy() // Recurrir al llamador si está sobrecargado
        );
    }
}
```

- **Por qué**:
  - `corePoolSize = 16`: Una heurística común para tareas vinculadas a E/S es `N * 2` (donde `N` son núcleos de CPU), pero puede ajustar esto según los límites de conexión de la base de datos y los tiempos de espera de las tareas.
  - `maximumPoolSize = 20`: Permite subprocesos adicionales para cargas máximas.
  - `ArrayBlockingQueue(100)`: Evita el crecimiento sin límite de las tareas en cola, evitando problemas de memoria.
  - `CallerRunsPolicy`: Asegura que el sistema se degrade gracefulmente bajo sobrecarga ejecutando tareas en el subproceso del llamador.

#### Integración con Spring Boot
En una aplicación Spring Boot, defina el `ExecutorService` como un bean:

```java
import com.google.common.util.concurrent.ThreadFactoryBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.util.concurrent.*;

@Configuration
public class AppConfig {
    @Bean
    public ExecutorService executorService() {
        int corePoolSize = 16; // Suposición de tarea vinculada a E/S para validación
        int maximumPoolSize = 20;
        long keepAliveTime = 60L;

        return new ThreadPoolExecutor(
            corePoolSize,
            maximumPoolSize,
            keepAliveTime,
            TimeUnit.SECONDS,
            new ArrayBlockingQueue<>(100),
            new ThreadFactoryBuilder().setNameFormat("validation-thread-%d").build(),
            new ThreadPoolExecutor.CallerRunsPolicy()
        );
    }
}
```

- **Nota**: Agregue Guava (`com.google.guava:guava`) a sus dependencias para `ThreadFactoryBuilder`, o use `Executors.defaultThreadFactory()` si no necesita un nombrado personalizado.

#### Uso en su Servicio de Validación
Inyéctelo y úselo como se muestra en sus ejemplos anteriores:

```java
@Service
public class ValidationService {
    private final ExecutorService executorService;
    private final RuleValidator ruleValidator;

    @Autowired
    public ValidationService(ExecutorService executorService, RuleValidator ruleValidator) {
        this.executorService = executorService;
        this.ruleValidator = ruleValidator;
    }

    // Usar en lógica CompletableFuture o ExecutorService como se mostró anteriormente
}
```

---

### Consejos de Ajuste para CPU de 8 Núcleos

1. **Mida el Rendimiento**:
   - Use herramientas de profiling (ej., VisualVM) para monitorear el uso de subprocesos y ajustar `corePoolSize` y `maximumPoolSize`.

2. **Límites de la Base de Datos**:
   - Si las reglas acceden a una base de datos, asegúrese de que el tamaño del grupo de subprocesos no exceda el tamaño de su grupo de conexiones (ej., `maximumPoolSize` de HikariCP). Coordine estas configuraciones.

3. **Cálculo Dinámico**:
   - Use `Runtime.getRuntime().availableProcessors()` para establecer dinámicamente el tamaño del grupo central:
     ```java
     int cores = Runtime.getRuntime().availableProcessors(); // Retorna 8 en una CPU de 8 núcleos
     int corePoolSize = cores * 2; // Para tareas vinculadas a E/S
     ```

4. **Subprocesos de Inicio Previo**:
   - Llame a `executor.prestartAllCoreThreads()` para inicializar todos los subprocesos centrales por adelantado, evitando la creación perezosa.

---

### Conclusión

Para una CPU de 8 núcleos ejecutando tareas vinculadas a E/S como sus reglas de validación con acceso a base de datos:
- Use un `ThreadPoolExecutor` con `corePoolSize = 16`, `maximumPoolSize = 20` y una cola con límite (ej., `ArrayBlockingQueue(100)`).
- Integre esto como un bean de Spring para la inyección de dependencias.
- Ajuste basándose en profiling y restricciones de la base de datos.

Esta configuración equilibra el paralelismo, el uso de recursos y la estabilidad del sistema, haciéndola adecuada para su caso de uso. ¡Avíseme si necesita ayuda para integrar esto en su proyecto específico!
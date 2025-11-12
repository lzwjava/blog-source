---
audio: false
generated: true
lang: es
layout: post
title: Implementación de Validación Multihilo con CompletableFuture
translated: true
type: note
---

Si utilizamos `CompletableFuture` en una aplicación Spring Boot para validación multi-hilo, proporciona una forma moderna y flexible de manejar tareas asíncronas. A continuación, explicaré cómo implementarlo, destacaré sus ventajas y desafíos, y proporcionaré una solución completa adaptada para validar múltiples reglas concurrentemente.

### Implementación de Validación Multi-hilo con CompletableFuture

`CompletableFuture` es parte de la API de concurrencia de Java y te permite ejecutar tareas de forma asíncrona, encadenar operaciones y manejar resultados o excepciones de manera elegante. Así es como podemos usarlo para validar múltiples reglas en paralelo, deteniéndose tan pronto como una falle.

#### Paso 1: Definir la Lógica de Validación

Primero, asumamos que tenemos un servicio que define reglas de validación individuales. Cada regla podría implicar acceso a la base de datos o lógica compleja, por lo que usaremos la anotación `@Transactional` de Spring para una gestión adecuada de las transacciones.

```java
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
public class RuleValidator {

    @Transactional(readOnly = true)
    public boolean validateRule(int ruleId) {
        // Simular lógica de validación (ej., consulta a base de datos)
        return performValidation(ruleId);
    }

    private boolean performValidation(int ruleId) {
        // Ejemplo: las reglas con ID par pasan, las impares fallan
        return ruleId % 2 == 0;
    }
}
```

#### Paso 2: Implementar el Servicio de Validación con CompletableFuture

Ahora, creemos un servicio que ejecute múltiples reglas de validación concurrentemente usando `CompletableFuture`. Usaremos un `ExecutorService` para gestionar los hilos y asegurar que si alguna regla falla, podamos detener el procesamiento de las demás.

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;

@Service
public class ValidationService {
    private static final Logger log = LoggerFactory.getLogger(ValidationService.class);
    private final ExecutorService executorService;
    private final RuleValidator ruleValidator;

    @Autowired
    public ValidationService(ExecutorService executorService, RuleValidator ruleValidator) {
        this.executorService = executorService;
        this.ruleValidator = ruleValidator;
    }

    public boolean validateAllRules() {
        // Crear una lista para contener todos los futures
        List<CompletableFuture<Boolean>> futures = new ArrayList<>();

        // Enviar 10 reglas de validación (por ejemplo)
        for (int i = 0; i < 10; i++) {
            final int ruleId = i;
            CompletableFuture<Boolean> future = CompletableFuture.supplyAsync(() -> {
                try {
                    return ruleValidator.validateRule(ruleId);
                } catch (Exception e) {
                    log.error("Validation failed for rule " + ruleId, e);
                    return false; // Tratar excepciones como fallos
                }
            }, executorService);
            futures.add(future);
        }

        // Crear un future para rastrear el resultado general
        CompletableFuture<Boolean> resultFuture = new CompletableFuture<>();

        // Monitorear cada future en busca de fallos
        for (CompletableFuture<Boolean> future : futures) {
            future.thenAccept(result -> {
                if (!result && !resultFuture.isDone()) {
                    // Primer fallo detectado
                    resultFuture.complete(false);
                    // Cancelar tareas restantes
                    futures.forEach(f -> {
                        if (!f.isDone()) {
                            f.cancel(true);
                        }
                    });
                }
            });
        }

        // Si todos los futures se completan con éxito, marcar como true
        CompletableFuture.allOf(futures.toArray(new CompletableFuture[0]))
                .thenRun(() -> {
                    if (!resultFuture.isDone()) {
                        resultFuture.complete(true);
                    }
                });

        try {
            return resultFuture.get(); // Bloquear hasta que el resultado esté disponible
        } catch (InterruptedException | ExecutionException e) {
            log.error("Error during validation", e);
            return false;
        }
    }
}
```

#### Cómo Funciona

1. **Envío de Tareas**:
   - Creamos un `CompletableFuture` para cada regla usando `supplyAsync()`, que ejecuta la lógica de validación de forma asíncrona.
   - El `executorService` (inyectado vía Spring) gestiona el grupo de hilos.

2. **Detección de Fallos**:
   - Cada future es monitoreado usando `thenAccept()`. Si cualquier regla retorna `false`, completamos el `resultFuture` con `false` y cancelamos los futures restantes.

3. **Caso de Éxito**:
   - `CompletableFuture.allOf()` espera a que todos los futures se completen. Si no ocurren fallos, completa `resultFuture` con `true`.

4. **Obtención del Resultado**:
   - Bloqueamos en `resultFuture.get()` para obtener el resultado final, manejando cualquier excepción que pueda ocurrir.

### Ventajas de Usar CompletableFuture

- **Flexibilidad**: Puedes encadenar operaciones (ej., `thenApply`, `thenCompose`) para procesar resultados más allá si es necesario.
- **Manejo de Excepciones**: Métodos incorporados como `exceptionally()` o `handle()` facilitan la gestión de errores.
- **Diseño No Bloqueante**: Soporta un estilo de programación reactiva, que puede extenderse para flujos de trabajo más complejos.

### Desafíos

- **Cancelación**: A diferencia de `ExecutorService` con `CompletionService` (donde puedes sondear fácilmente el primer resultado y cancelar los demás), `CompletableFuture` requiere la cancelación manual de otros futures cuando uno falla. Esto añade complejidad.
- **Complejidad**: El código puede volverse más difícil de leer y mantener en comparación con un enfoque más simple basado en bucles con `ExecutorService`.

### Ejemplo de Uso

Para usar esto en una aplicación Spring Boot, configurarías un bean `ExecutorService`:

```java
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

@Configuration
public class AppConfig {
    @Bean
    public ExecutorService executorService() {
        return Executors.newFixedThreadPool(10); // Ajustar el tamaño según sea necesario
    }
}
```

Luego, llama al servicio desde un controlador u otro componente:

```java
@RestController
public class ValidationController {
    private final ValidationService validationService;

    @Autowired
    public ValidationController(ValidationService validationService) {
        this.validationService = validationService;
    }

    @GetMapping("/validate")
    public ResponseEntity<String> validate() {
        boolean result = validationService.validateAllRules();
        return ResponseEntity.ok(result ? "All rules passed" : "Validation failed");
    }
}
```

### Conclusión

Usar `CompletableFuture` para la validación multi-hilo en Spring Boot es un enfoque viable, especialmente si valoras su naturaleza asíncrona y encadenable. Te permite ejecutar reglas de validación concurrentemente y manejar resultados de forma flexible. Sin embargo, si tu objetivo principal es la simplicidad—especialmente para detectar el primer fallo y cancelar las tareas restantes—el `ExecutorService` tradicional con `CompletionService` podría ser más fácil de implementar y mantener. Con `CompletableFuture`, ganas potencia y flexibilidad a costa de una lógica de cancelación ligeramente más compleja.
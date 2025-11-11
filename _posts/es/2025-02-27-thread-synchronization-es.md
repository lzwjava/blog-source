---
audio: false
generated: true
lang: es
layout: post
title: Sincronización de Hilos en Java
translated: true
type: note
---

¡Adentrémonos en la sincronización de hilos en Java! Cuando múltiples hilos acceden a recursos compartidos (como variables, colecciones o archivos), necesitas prevenir condiciones de carrera (race conditions), donde los hilos interfieren entre sí, llevando a resultados impredecibles. Java proporciona varias herramientas para esto: `synchronized`, `Lock` y `Semaphore`. Explicaré cada una, mostraré ejemplos y las compararé para que puedas elegir la correcta para tus necesidades.

---

### 1. La palabra clave `synchronized`
La palabra clave `synchronized` asegura que solo un hilo pueda ejecutar un bloque de código o método a la vez. Es la herramienta de sincronización más simple, incorporada en el núcleo de Java.

#### Cómo Funciona
- Bloquea el monitor de un objeto (cada objeto en Java tiene uno).
- Otros hilos esperan hasta que se libera el bloqueo.

#### Ejemplo: Contador con `synchronized`
```java
class Counter {
    private int count = 0;

    public synchronized void increment() {
        count++;
    }

    public int getCount() {
        return count;
    }
}

public class Main {
    public static void main(String[] args) throws InterruptedException {
        Counter counter = new Counter();
        Runnable task = () -> {
            for (int i = 0; i < 1000; i++) {
                counter.increment();
            }
        };

        Thread t1 = new Thread(task);
        Thread t2 = new Thread(task);
        t1.start();
        t2.start();
        t1.join();
        t2.join();

        System.out.println("Final count: " + counter.getCount()); // Siempre 2000
    }
}
```
- Sin `synchronized`, `count++` (leer-modificar-escribir) podría solaparse, dando un resultado menor a 2000.
- `synchronized` bloquea la instancia de `Counter`, asegurando actualizaciones atómicas.

#### Bloque Sincronizado
También puedes bloquear código específico en lugar de un método completo:
```java
public void increment() {
    synchronized (this) {
        count++;
    }
}
```
- Usa un objeto diferente como bloqueo si quieres un control más fino:
```java
private final Object lock = new Object();
public void increment() {
    synchronized (lock) {
        count++;
    }
}
```

#### Pros y Contras
- **Pros**: Simple, incorporado, bueno para uso básico.
- **Contras**: Sin flexibilidad (ej., no se puede interrumpir un hilo en espera), se bloquea hasta que se libera.

---

### 2. Interfaz `Lock` (java.util.concurrent.locks)
La interfaz `Lock` (ej., `ReentrantLock`) ofrece más control que `synchronized`. Es parte del paquete `java.util.concurrent` y se introdujo para abordar las limitaciones de `synchronized`.

#### Características Clave
- Llamadas explícitas `lock()` y `unlock()`.
- Soporta intento de bloqueo (try-locks), tiempos de espera y bloqueo interrumpible.
- Opción de equidad (fairness) (los hilos esperan en orden).

#### Ejemplo: Contador con `ReentrantLock`
```java
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

class Counter {
    private int count = 0;
    private final Lock lock = new ReentrantLock();

    public void increment() {
        lock.lock();
        try {
            count++;
        } finally {
            lock.unlock(); // Siempre desbloquear en finally
        }
    }

    public int getCount() {
        return count;
    }
}

public class Main {
    public static void main(String[] args) throws InterruptedException {
        Counter counter = new Counter();
        Runnable task = () -> {
            for (int i = 0; i < 1000; i++) {
                counter.increment();
            }
        };

        Thread t1 = new Thread(task);
        Thread t2 = new Thread(task);
        t1.start();
        t2.start();
        t1.join();
        t2.join();

        System.out.println("Final count: " + counter.getCount()); // Siempre 2000
    }
}
```
- `try-finally` asegura que el bloqueo se libere incluso si ocurre una excepción.

#### Características Avanzadas
- **Intento de Bloqueo (Try Lock)**: Intento no bloqueante de adquirir el bloqueo:
```java
if (lock.tryLock()) {
    try {
        count++;
    } finally {
        lock.unlock();
    }
} else {
    System.out.println("No se pudo adquirir el bloqueo");
}
```
- **Tiempo de Espera (Timeout)**: Esperar un tiempo limitado:
```java
if (lock.tryLock(1, TimeUnit.SECONDS)) { ... }
```
- **Interrumpible**: Permite que los hilos en espera sean interrumpidos:
```java
lock.lockInterruptibly();
```

#### Pros y Contras
- **Pros**: Flexible, soporta características avanzadas, control explícito.
- **Contras**: Más verboso, requiere desbloqueo manual (riesgo de olvidarse).

---

### 3. `Semaphore`
Un `Semaphore` controla el acceso a un recurso manteniendo un conjunto de permisos. Es ideal para limitar la concurrencia (ej., máximo 5 hilos pueden acceder a un recurso).

#### Cómo Funciona
- Los hilos adquieren permisos con `acquire()`.
- Liberan permisos con `release()`.
- Si no hay permisos disponibles, los hilos esperan.

#### Ejemplo: Limitando Conexiones a Base de Datos
```java
import java.util.concurrent.Semaphore;

class ConnectionPool {
    private final Semaphore semaphore = new Semaphore(3); // Máx 3 conexiones

    public void connect() {
        try {
            semaphore.acquire();
            System.out.println(Thread.currentThread().getName() + " conectado");
            Thread.sleep(1000); // Simular trabajo
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        } finally {
            semaphore.release();
            System.out.println(Thread.currentThread().getName() + " desconectado");
        }
    }
}

public class Main {
    public static void main(String[] args) {
        ConnectionPool pool = new ConnectionPool();
        Runnable task = () -> pool.connect();

        Thread[] threads = new Thread[10];
        for (int i = 0; i < 10; i++) {
            threads[i] = new Thread(task, "Thread-" + i);
            threads[i].start();
        }
    }
}
```
- Solo 3 hilos pueden "conectarse" a la vez; los demás esperan hasta que se libere un permiso.

#### Características Avanzadas
- **Equidad (Fairness)**: `new Semaphore(3, true)` asegura orden FIFO.
- **Intento de Adquirir (Try Acquire)**: `semaphore.tryAcquire()` verifica sin bloquear.

#### Pros y Contras
- **Pros**: Ideal para grupos de recursos (pools), sistema de permisos flexible.
- **Contras**: Más complejo que `synchronized` o `Lock`, no es para exclusión mutua simple.

---

### Combinando con `ExecutorService`
Así es como funcionan estas herramientas con un grupo de hilos (thread pool):
```java
import java.util.concurrent.*;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

class SharedResource {
    private int value = 0;
    private final Lock lock = new ReentrantLock();

    public void increment() {
        lock.lock();
        try {
            value++;
        } finally {
            lock.unlock();
        }
    }

    public int getValue() {
        return value;
    }
}

public class Main {
    public static void main(String[] args) throws InterruptedException {
        SharedResource resource = new SharedResource();
        ExecutorService executor = Executors.newFixedThreadPool(4);

        for (int i = 0; i < 10; i++) {
            executor.submit(() -> {
                for (int j = 0; j < 100; j++) {
                    resource.increment();
                }
            });
        }

        executor.shutdown();
        executor.awaitTermination(5, TimeUnit.SECONDS);
        System.out.println("Final value: " + resource.getValue()); // Siempre 1000
    }
}
```

---

### Comparación

| Característica     | `synchronized`       | `Lock` (ReentrantLock) | `Semaphore`         |
|--------------------|----------------------|------------------------|---------------------|
| Facilidad de Uso   | Alto                | Medio                 | Bajo               |
| Flexibilidad       | Baja                | Alto                  | Medio              |
| Granularidad       | Método/bloque       | Explícito             | Basado en permisos |
| Interrumpible      | No                  | Sí                    | Sí                 |
| Opción de Equidad  | No                  | Sí                    | Sí                 |
| Caso de Uso        | Exclusión mutua simple | Control avanzado   | Limitación de recursos |

---

### ¿Cuándo Usar Qué?
- **`synchronized`**: Exclusión mutua rápida y simple (ej., proteger una sola variable).
- **`Lock`**: Necesitas intentos de bloqueo (try-locks), tiempos de espera o interrupción (ej., flujos de trabajo complejos).
- **`Semaphore`**: Limitar el acceso concurrente a un recurso (ej., grupos de conexiones, limitación de tasa - rate limiting).
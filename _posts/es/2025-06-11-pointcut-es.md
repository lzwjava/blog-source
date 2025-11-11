---
audio: false
generated: true
lang: es
layout: post
title: Comprensión de las Expresiones Pointcut
translated: true
type: note
---

Estás solicitando una guía completa sobre las expresiones pointcut de AspectJ, específicamente enfocándote en `execution`, cómo usar comodines, coincidir nombres de clase (prefijo/sufijo) y también sobre otros tipos de advice como `@AfterReturning`. Vamos a desglosarlo.

### Entendiendo las Expresiones Pointcut en Spring AOP (Sintaxis AspectJ)

Spring AOP utiliza expresiones pointcut de AspectJ para determinar *dónde* se debe aplicar un advice (como `@Before`, `@AfterReturning`, etc.). El núcleo de tu pregunta gira en torno al designador pointcut `execution`, que es el más utilizado.

#### El Designador Pointcut `execution`

El designador pointcut `execution` coincide con ejecuciones de métodos. Su sintaxis general es:

`execution(modifiers-pattern? ret-type-pattern declaring-type-pattern?name-pattern(param-pattern) throws-pattern?)`

Desglosemos los componentes:

*   **`modifiers-pattern?`**: Opcional. Coincide con los modificadores de método (ej., `public`, `private`, `protected`).
*   **`ret-type-pattern`**: Requerido. Coincide con el tipo de retorno del método.
*   **`declaring-type-pattern?`**: Opcional. Coincide con el nombre de clase completo donde se declara el método.
*   **`name-pattern`**: Requerido. Coincide con el nombre del método.
*   **`param-pattern`**: Requerido. Coincide con los parámetros del método.
*   **`throws-pattern?`**: Opcional. Coincide con las excepciones lanzadas por el método.

#### Tu Ejemplo: `@Before("execution(* com.example.service.*.*(..))")`

Disectemos tu ejemplo dado:

*   `@Before`: Esta es una anotación de advice, lo que significa que el método anotado se ejecutará *antes* del join point coincidente.
*   `execution()`: El designador pointcut.
*   `*`: Coincide con cualquier tipo de retorno.
*   `com.example.service.*.*`:
    *   `com.example.service`: Coincide con el paquete `com.example.service`.
    *   `.*`: El primer `*` después de `service` coincide con cualquier clase dentro del paquete `com.example.service`.
    *   `.`: Separador entre paquete/clase y método.
    *   `*`: El segundo `*` coincide con cualquier nombre de método dentro de esas clases.
*   `(..)`: Coincide con cualquier número de parámetros (cero o más, de cualquier tipo).

**En español sencillo:** Este pointcut coincide con la ejecución de *cualquier método* en *cualquier clase* dentro del paquete `com.example.service` (y sus subpaquetes directos, si hay clases directamente en `com.example.service`).

---

### Comodines en Expresiones Pointcut

Los comodines son cruciales para crear expresiones pointcut flexibles.

*   **`*` (asterisco simple)**:
    *   Coincide con cualquier elemento único en un patrón de nombre (ej., cualquier tipo de retorno, cualquier nombre de clase, cualquier nombre de método).
    *   Coincide con cualquier segmento único en un nombre de paquete (ej., `com.example.*.service` coincidiría con `com.example.foo.service`).
*   **`..` (doble punto)**:
    *   **En patrones de paquete**: Coincide con cero o más segmentos en un nombre de paquete.
        *   `com.example..service`: Coincide con `com.example.service`, `com.example.foo.service`, `com.example.foo.bar.service`, etc.
    *   **En patrones de parámetros**: Coincide con cero o más argumentos de cualquier tipo.
        *   `(..)`: Coincide con cualquier número de argumentos.
        *   `(java.lang.String, ..)`: Coincide con métodos que tienen un `String` como primer argumento, seguido de cualquier número de otros argumentos.
        *   `(.., java.lang.Long)`: Coincide con métodos con cualquier número de argumentos iniciales, terminando con un `Long`.

---

### Coincidencia de Nombres de Clase

#### 1. Coincidir Nombre de Clase por Sufijo

Para coincidir clases que terminan con un sufijo específico, colocas el comodín antes del sufijo.

**Ejemplo: Coincidir todas las clases que terminan con `ServiceImpl`**

```java
@Before("execution(* com.example.service.*ServiceImpl.*(..))")
```

*   `*ServiceImpl`: Coincide con cualquier nombre de clase que termine con `ServiceImpl`.

**Ejemplo: Coincidir todas las clases que terminan con `Controller` en cualquier subpaquete de `com.example.web`**

```java
@Before("execution(* com.example.web..*Controller.*(..))")
```

*   `com.example.web..`: Coincide con `com.example.web` y cualquiera de sus subpaquetes.
*   `*Controller`: Coincide con cualquier nombre de clase que termine con `Controller`.

#### 2. Coincidir Nombre de Clase por Prefijo

Para coincidir clases que comienzan con un prefijo específico, colocas el comodín después del prefijo.

**Ejemplo: Coincidir todas las clases que comienzan con `User`**

```java
@Before("execution(* com.example.service.User*.*(..))")
```

*   `User*`: Coincide con cualquier nombre de clase que comience con `User`.

**Ejemplo: Coincidir todas las clases que comienzan con `Admin` en el paquete `com.example.admin`**

```java
@Before("execution(* com.example.admin.Admin*.*(..))")
```

#### 3. Coincidir Nombres de Clase Específicos (Coincidencia Exacta)

No se necesitan comodines para coincidencias exactas.

**Ejemplo: Coincidir métodos solo en `com.example.service.UserServiceImpl`**

```java
@Before("execution(* com.example.service.UserServiceImpl.*(..))")
```

---

### Diferentes Tipos de Designadores Pointcut

Si bien `execution` es el más común, AspectJ proporciona varios otros designadores pointcut para especificar join points. Puedes combinarlos usando operadores lógicos (`and`, `or`, `not` o `&&`, `||`, `!`).

Aquí están los más importantes:

1.  **`execution()`**: Como se discutió, coincide con ejecuciones de métodos.
    *   Ejemplo: `@Before("execution(* com.example.service.UserService.*(..))")`

2.  **`within()`**: Coincide con join points donde el código está dentro de un cierto tipo (clase). Esto se usa a menudo para restringir el alcance de otros pointcuts.
    *   Ejemplo: `@Before("within(com.example.service.*) && execution(* *(..))")`
        *   Esto combina `within` y `execution`. Significa "cualquier ejecución de método dentro de cualquier clase en el paquete `com.example.service`". La parte `execution` es entonces solo un comodín para cualquier método, ya que `within` maneja la coincidencia de clase.

3.  **`this()`**: Coincide con join points donde el proxy *en sí mismo* es una instancia del tipo dado. Esto es menos común para advice simples y más para introducciones o problemas de auto-invocación.
    *   Ejemplo: `@Around("this(com.example.service.UserService)")`
        *   Coincide si el proxy AOP implementa `UserService`.

4.  **`target()`**: Coincide con join points donde el *objeto objetivo* (el objeto real que se está asesorando, no el proxy) es una instancia del tipo dado. Esto a menudo es más intuitivo que `this()` cuando te importa la implementación subyacente.
    *   Ejemplo: `@Around("target(com.example.service.UserServiceImpl)")`
        *   Coincide si el objeto objetivo es una instancia de `UserServiceImpl`.

5.  **`args()`**: Coincide con join points donde los argumentos son de un cierto tipo o coinciden con un cierto patrón.
    *   Ejemplo: `@Before("execution(* com.example.service.*.*(String, ..))")`
        *   Coincide con métodos donde el primer argumento es un `String`.
    *   Ejemplo: `@Before("args(java.lang.String, int)")`
        *   Coincide con métodos que toman exactamente un `String` seguido de un `int`.
    *   Ejemplo: `@Before("args(name, age)")` donde `name` y `age` pueden luego vincularse a los parámetros del método de advice.

6.  **`bean()`**: (Específico de Spring) Coincide con métodos ejecutados en beans de Spring con nombres o patrones de nombres específicos.
    *   Ejemplo: `@Before("bean(userService) && execution(* *(..))")`
        *   Coincide con cualquier ejecución de método en el bean de Spring llamado "userService".
    *   Ejemplo: `@Before("bean(*Service) && execution(* *(..))")`
        *   Coincide con cualquier ejecución de método en beans de Spring cuyos nombres terminen con "Service".

7.  **`@annotation()`**: Coincide con join points donde el método objetivo (o la clase para `within`) está anotado con una anotación específica.
    *   Ejemplo: `@Before("@annotation(com.example.annotation.Loggable)")`
        *   Coincide con cualquier método que esté anotado con `@Loggable`.
    *   Ejemplo: `@Before("execution(* *(..)) && @annotation(org.springframework.transaction.annotation.Transactional)")`
        *   Coincide con cualquier ejecución de método que esté anotada con `@Transactional`.

8.  **`@within()`**: Coincide con join points donde el tipo declarativo (clase) está anotado con una anotación específica.
    *   Ejemplo: `@Before("@within(org.springframework.stereotype.Service) && execution(* *(..))")`
        *   Coincide con cualquier ejecución de método dentro de una clase que esté anotada con `@Service`.

9.  **`@target()`**: Coincide con join points donde la clase del objeto objetivo tiene la anotación dada.
    *   Ejemplo: `@Around("@target(com.example.annotation.Auditable)")`

10. **`@args()`**: Coincide con join points donde el tipo de tiempo de ejecución de los argumentos reales pasados al método tiene anotaciones del tipo(s) dado(s).
    *   Ejemplo: `@Before("@args(com.example.annotation.ValidInput)")`

---

### Tipos de Advice (Anotaciones)

Mencionaste `@AfterReturning` y "cualquier otro que podamos usar en anotaciones". Spring AOP proporciona varios tipos de advice, cada uno ejecutándose en un punto diferente del ciclo de vida del join point:

1.  **`@Before`**:
    *   Se ejecuta *antes* de la ejecución del método coincidente.
    *   Ejemplo: Registrar detalles de la solicitud antes de que se ejecute un método de servicio.
    *   No puede evitar que el método se ejecute ni alterar su valor de retorno.

2.  **`@AfterReturning`**:
    *   Se ejecuta *después* de que el método coincidente retorna *exitosamente* (sin lanzar una excepción).
    *   Puede acceder al valor de retorno del método.
    *   Sintaxis: `@AfterReturning(pointcut="yourPointcut()", returning="result")`
    *   Ejemplo:
        ```java
        @AfterReturning(pointcut="execution(* com.example.service.UserService.getUserById(..))", returning="user")
        public void logUserRetrieval(Object user) {
            System.out.println("Usuario recuperado: " + user);
        }
        ```
        *Nota: El nombre del atributo `returning` (`user` en este caso) debe coincidir con el nombre del parámetro en el método de advice.*

3.  **`@AfterThrowing`**:
    *   Se ejecuta *después* de que el método coincidente lanza una excepción.
    *   Puede acceder a la excepción lanzada.
    *   Sintaxis: `@AfterThrowing(pointcut="yourPointcut()", throwing="ex")`
    *   Ejemplo:
        ```java
        @AfterThrowing(pointcut="execution(* com.example.service.*.*(..))", throwing="ex")
        public void logException(Exception ex) {
            System.err.println("Ocurrió una excepción: " + ex.getMessage());
        }
        ```
        *Nota: El nombre del atributo `throwing` (`ex` en este caso) debe coincidir con el nombre del parámetro en el método de advice.*

4.  **`@After` (advice finally)**:
    *   Se ejecuta *después* de que el método coincidente se completa, independientemente de si retornó exitosamente o lanzó una excepción.
    *   Similar a un bloque `finally`.
    *   Ejemplo: Liberar recursos, independientemente del resultado del método.
    *   ```java
        @After("execution(* com.example.service.OrderService.placeOrder(..))")
        public void cleanupOrderProcess() {
            System.out.println("Proceso de orden completado (limpieza)");
        }
        ```

5.  **`@Around`**:
    *   El tipo de advice más potente y flexible.
    *   Se ejecuta *alrededor* de la ejecución del método coincidente.
    *   Eres responsable de invocar el método real usando `ProceedingJoinPoint.proceed()`.
    *   Puede inspeccionar, modificar o incluso suprimir los argumentos y el valor de retorno del método.
    *   Puede capturar y manejar excepciones lanzadas por el método asesorado.
    *   Ejemplo: Monitoreo de rendimiento, gestión de transacciones, caching.
    *   ```java
        import org.aspectj.lang.ProceedingJoinPoint;
        import org.aspectj.lang.annotation.Around;
        import org.aspectj.lang.annotation.Aspect;

        @Aspect
        public class PerformanceMonitorAspect {

            @Around("execution(* com.example.service.*.*(..))")
            public Object profile(ProceedingJoinPoint joinPoint) throws Throwable {
                long start = System.currentTimeMillis();
                Object result = joinPoint.proceed(); // Ejecuta el método original
                long end = System.currentTimeMillis();
                System.out.println(joinPoint.getSignature().getName() + " ejecutado en " + (end - start) + "ms");
                return result;
            }
        }
        ```

### Definiendo Pointcuts Reutilizables

Para una mejor legibilidad y reutilización, puedes definir pointcuts con nombre usando `@Pointcut`.

```java
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Pointcut;
import org.aspectj.lang.annotation.Before;
import org.aspectj.lang.annotation.AfterReturning;

@Aspect
public class MyServiceAspect {

    // Define un pointcut para todos los métodos en el paquete com.example.service
    @Pointcut("execution(* com.example.service.*.*(..))")
    public void serviceMethods() {}

    // Define un pointcut para métodos que retornan un objeto User
    @Pointcut("execution(com.example.model.User com.example.service.*.*(..))")
    public void returnsUser() {}

    // Usando el pointcut definido
    @Before("serviceMethods()")
    public void logBeforeServiceCall() {
        System.out.println("Antes de la ejecución del método de servicio.");
    }

    // Combinando pointcuts con AND lógico
    @AfterReturning(pointcut="serviceMethods() && returnsUser()", returning="user")
    public void logUserReturned(Object user) {
        System.out.println("El método de servicio retornó el usuario: " + user);
    }

    // También puedes definir pointcuts con argumentos
    @Pointcut("execution(* com.example.repository.*.save(..)) && args(entity)")
    public void repositorySave(Object entity) {}

    @Before("repositorySave(entity)")
    public void logEntityBeforeSave(Object entity) {
        System.out.println("Guardando entidad: " + entity);
    }
}
```

Esta guía completa cubre los conceptos esenciales de las expresiones pointcut, el uso de comodines, la coincidencia de nombres de clase y los diferentes tipos de advice en Spring AOP. Dominar estos conceptos te permitirá controlar con precisión dónde y cuándo se aplican tus preocupaciones transversales.
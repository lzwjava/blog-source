---
audio: false
generated: true
lang: es
layout: post
title: Excepción de reversión de transacción SQL en Spring
translated: true
type: note
---

Para abordar su consulta sobre capturar la `SqlTransactionRollbackException` que ocurre después de que `DataSourceUtils.java` obtiene una conexión JDBC de un `DataSource` y proporcionar un análisis detallado del bloqueo de base de datos asociado, desglosemos esto sistemáticamente.

### Capturando la SqlTransactionRollbackException

En una aplicación basada en Spring, `DataSourceUtils.java` es una clase de utilidad dentro del Spring Framework que facilita la obtención y gestión de conexiones JDBC desde un `DataSource`. Específicamente, el método `DataSourceUtils.getConnection(DataSource)` obtiene una conexión, ya sea obteniendo una nueva del pool de conexiones o reutilizando una conexión transaccional existente si ya está asociada con el contexto de transacción del hilo actual.

El escenario que ha descrito indica que después de que la conexión se obtiene exitosamente, se lanza una `SqlTransactionRollbackException`. Dado que `SqlTransactionRollbackException` no es una excepción estándar en la jerarquía de excepciones de Spring (Spring típicamente usa excepciones como `TransactionException`, `UnexpectedRollbackException` o `DeadlockLoserDataAccessException`), asumiré que es una excepción personalizada específica de la aplicación que se lanza cuando una transacción se revierte debido a un problema relacionado con la base de datos, como un conflicto de bloqueo.

Esta excepción probablemente ocurre no durante la obtención de la conexión en sí (lo que normalmente lanzaría una `CannotGetJdbcConnectionException` si fallara), sino durante operaciones posteriores de la base de datos dentro de una transacción—como ejecutar sentencias SQL—que encuentran un problema que requiere un rollback.

Para capturar esta excepción, necesita envolver el código que inicia la operación transaccional en un bloque `try-catch`. Así es como puede hacerlo:

#### Ejemplo con Gestión Transaccional Declarativa
Si está usando la anotación `@Transactional` de Spring para gestionar transacciones, la excepción se lanzaría desde el método donde se define la transacción. Por ejemplo:

```java
@Service
public class MyService {
    @Autowired
    private MyDao myDao;

    @Transactional
    public void performDatabaseOperation() {
        myDao.updateData(); // Asumir que esto causa un rollback debido a un problema de bloqueo
    }
}
```

Al llamar a este método de servicio, puede capturar la `SqlTransactionRollbackException`:

```java
@Autowired
private MyService myService;

public void executeOperation() {
    try {
        myService.performDatabaseOperation();
    } catch (SqlTransactionRollbackException e) {
        // Manejar la excepción
        System.err.println("Transacción revertida debido a: " + e.getMessage());
        // Opcionalmente reintentar la operación o notificar al usuario
    }
}
```

#### Ejemplo con Gestión Transaccional Programática
Si está gestionando transacciones programáticamente usando `TransactionTemplate` o `PlatformTransactionManager`, capturaría la excepción alrededor de la ejecución de la transacción:

```java
@Autowired
private TransactionTemplate transactionTemplate;

public void executeOperation() {
    try {
        transactionTemplate.execute(status -> {
            // Realizar operaciones de base de datos
            myDao.updateData();
            return null;
        });
    } catch (SqlTransactionRollbackException e) {
        // Manejar la excepción
        System.err.println("Transacción revertida debido a: " + e.getMessage());
    }
}
```

#### Consideraciones
- **Jerarquía de Excepciones**: Si `SqlTransactionRollbackException` es una excepción personalizada, verifique su superclase. Si extiende `DataAccessException` de Spring, podría capturar `DataAccessException` y verificar el tipo específico:
  ```java
  catch (DataAccessException e) {
      if (e instanceof SqlTransactionRollbackException) {
          // Manejar SqlTransactionRollbackException específicamente
      }
  }
  ```
- **Contexto de Transacción**: La excepción probablemente surge después de que se obtiene la conexión, cuando el gestor de transacciones o el controlador JDBC detectan un problema (por ejemplo, un estado de solo-rollback o un error de base de datos). Por lo tanto, capturarla a nivel de servicio o del llamador es apropiado.

### Análisis Detallado del Bloqueo de Base de Datos

La mención de "este tipo de bloqueo de base de datos" en su consulta, combinada con la excepción de rollback, sugiere fuertemente una conexión con un **deadlock**—un problema común de bloqueo de base de datos que puede llevar a reversiones de transacciones. Analicemos esto en detalle.

#### ¿Qué es un Deadlock?
Un deadlock ocurre en una base de datos cuando dos o más transacciones no pueden proceder porque cada una mantiene un bloqueo que la otra necesita, creando una dependencia cíclica. Por ejemplo:

- **Transacción T1**:
  1. Adquiere un bloqueo exclusivo en `TableA`.
  2. Intenta adquirir un bloqueo exclusivo en `TableB` (espera porque T2 lo mantiene).
- **Transacción T2**:
  1. Adquiere un bloqueo exclusivo en `TableB`.
  2. Intenta adquirir un bloqueo exclusivo en `TableA` (espera porque T1 lo mantiene).

Aquí, T1 espera a que T2 libere `TableB`, y T2 espera a que T1 libere `TableA`, resultando en un deadlock.

#### Cómo los Deadlocks Conducen a Rollbacks
La mayoría de las bases de datos relacionales (por ejemplo, MySQL, PostgreSQL, Oracle) tienen mecanismos de detección de deadlocks. Cuando se identifica un deadlock:
1. La base de datos selecciona una transacción "víctima" (a menudo la que ha realizado menos trabajo o basada en una política configurable).
2. La transacción víctima es revertida, liberando sus bloqueos.
3. La base de datos lanza una `SQLException` con un código de error específico (por ejemplo, error 1213 de MySQL, error 40P01 de PostgreSQL) a la aplicación.
4. En Spring, esta `SQLException` se traduce típicamente en una `DeadlockLoserDataAccessException`. Si su aplicación lanza `SqlTransactionRollbackException` en su lugar, podría ser un wrapper personalizado alrededor de tal evento.

En su escenario, después de que `DataSourceUtils` obtiene la conexión, una operación de base de datos dentro de la transacción encuentra un deadlock, conduciendo a un rollback y al lanzamiento de `SqlTransactionRollbackException`.

#### Tipos de Bloqueo Involucrados
- **Shared Locks**: Usados para operaciones de lectura; múltiples transacciones pueden mantener shared locks en el mismo recurso.
- **Exclusive Locks**: Usados para operaciones de escritura; solo una transacción puede mantener un exclusive lock, y entra en conflicto tanto con shared locks como con exclusive locks mantenidos por otros.
Los deadlocks típicamente involucran exclusive locks, ya que son más restrictivos.

#### Por Qué Ocurren los Deadlocks
Los deadlocks surgen debido a:
- **Orden Inconsistente de Bloqueo**: Transacciones que acceden a recursos (por ejemplo, tablas, filas) en secuencias diferentes.
- **Transacciones Largas**: Mantener bloqueos por períodos extendidos aumenta la posibilidad de conflictos.
- **Alta Concurrencia**: Múltiples transacciones operando en los mismos datos simultáneamente.

#### Escenario de Ejemplo
Suponga dos métodos en su aplicación que actualizan dos tablas:

```java
@Transactional
public void updateUserAndOrder1() {
    jdbcTemplate.update("UPDATE users SET name = ? WHERE id = ?", "Alice", 1); // Bloquea fila de users
    jdbcTemplate.update("UPDATE orders SET status = ? WHERE user_id = ?", "Shipped", 1); // Bloquea fila de orders
}

@Transactional
public void updateUserAndOrder2() {
    jdbcTemplate.update("UPDATE orders SET status = ? WHERE user_id = ?", "Processed", 1); // Bloquea fila de orders
    jdbcTemplate.update("UPDATE users SET name = ? WHERE id = ?", "Bob", 1); // Bloquea fila de users
}
```

Si estos métodos se ejecutan concurrentemente, `updateUserAndOrder1` podría bloquear `users` mientras espera por `orders`, y `updateUserAndOrder2` podría bloquear `orders` mientras espera por `users`, causando un deadlock.

#### Manejo y Prevención de Deadlocks
1. **Capturar la Excepción**:
   Como se mostró anteriormente, use un bloque `try-catch` para manejar `SqlTransactionRollbackException`. Usted podría:
   - Registrar el error para depuración.
   - Reintentar la operación (con precaución para evitar bucles infinitos):
     ```java
     int reintentos = 3;
     for (int i = 0; i < reintentos; i++) {
         try {
             myService.performDatabaseOperation();
             break;
         } catch (SqlTransactionRollbackException e) {
             if (i < reintentos - 1) {
                 Thread.sleep(1000 * (i + 1)); // Retroceso exponencial
                 continue;
             }
             throw e; // Relanzar después de reintentos máximos
         }
     }
     ```

2. **Asegurar un Orden de Bloqueo Consistente**:
   Modifique el código para acceder a las tablas en la misma secuencia (por ejemplo, siempre bloquear `users` antes que `orders`).

3. **Minimizar la Duración del Bloqueo**:
   Mantenga las transacciones cortas moviendo la lógica no transaccional fuera de los límites de `@Transactional`.

4. **Usar Niveles de Aislamiento Apropiados**:
   Ajuste el nivel de aislamiento de la transacción (por ejemplo, `READ_COMMITTED` en lugar de `SERIALIZABLE`) si los requisitos de la aplicación lo permiten, aunque esto no elimina los deadlocks por completo.

5. **Características Específicas de la Base de Datos**:
   - Habilite el registro de detección de deadlocks (por ejemplo, `innodb_print_all_deadlocks` en MySQL).
   - Use bloqueo a nivel de fila donde sea posible, aunque los deadlocks aún pueden ocurrir a nivel de fila.

#### Analizando Deadlocks
Para diagnosticar el deadlock específico:
- **Registros de la Base de Datos**: Revise los registros del servidor de base de datos para obtener detalles del deadlock (por ejemplo, transacciones involucradas, recursos bloqueados).
- **Depuración de Spring**: Habilite el registro de transacciones de Spring (`logging.level.org.springframework.transaction=DEBUG`) para rastrear eventos de transacciones.
- **Trazado de Aplicación**: Registre la secuencia de operaciones que conducen a la excepción.

### Conclusión
Para capturar la `SqlTransactionRollbackException`, coloque un bloque `try-catch` alrededor del código que invoca la operación transaccional, como un método de servicio marcado con `@Transactional`. Para el bloqueo de base de datos—probablemente un deadlock—asegúrese de que las transacciones accedan a los recursos en un orden consistente, mantenga las transacciones cortas y considere lógica de reintento para fallos transitorios. Los deadlocks ocurren debido a dependencias cíclicas de bloqueo, y aunque las bases de datos los resuelven revirtiendo una transacción víctima, un diseño proactivo puede minimizar su ocurrencia.

---

Al tratar con una `SqlTransactionRollbackException` en una aplicación Spring—particularmente en un escenario donde otra transacción mantiene un bloqueo, conduciendo a fallos en la obtención de conexiones y al lanzamiento de la excepción después de aproximadamente 20 intentos fallidos—hay varias estrategias que puede emplear para manejar y potencialmente mitigar este problema. Esta excepción típicamente surge durante el rollback de una transacción cuando bloqueos de base de datos o problemas de concurrencia impiden que la operación se complete exitosamente. A continuación, describo un enfoque integral para abordar este problema, enfocándose en la prevención, manejo y recuperación.

---

### Entendiendo el Problema
La `SqlTransactionRollbackException` (o más probablemente `TransactionRollbackException` en Spring, ya que la primera no es una excepción estándar de Spring) indica que una transacción no pudo ser revertida, posiblemente porque otra transacción mantiene un bloqueo en los recursos de base de datos requeridos. Esta contención de bloqueo hace que el gestor de transacciones falle al obtener una conexión, reintente múltiples veces (alrededor de 20 en su caso), y eventualmente lance la excepción cuando el rollback no puede completarse. Esto sugiere un problema de concurrencia, como contención de bloqueo o un deadlock, agravado por la gestión de transacciones de Spring reintentando internamente antes de darse por vencido.

---

### Estrategias para Manejar la Excepción

#### 1. Minimizar la Contención de Bloqueo con Transacciones Cortas
Las transacciones de larga duración aumentan la probabilidad de contención de bloqueo, ya que mantienen bloqueos de base de datos por períodos extendidos, bloqueando otras transacciones. Para reducir este riesgo:

- **Diseñar Transacciones de Corta Duración**: Asegúrese de que sus métodos `@Transactional` realizan sus operaciones de base de datos rápidamente y confirman o revierten prontamente. Evite incluir lógica de negocio que consuma mucho tiempo o llamadas externas dentro del alcance de la transacción.
- **Dividir Transacciones Grandes**: Si una sola transacción involucra múltiples operaciones, considere dividirla en transacciones más pequeñas e independientes donde sea posible. Esto reduce la duración durante la cual se mantienen los bloqueos.

#### 2. Optimizar Consultas de Base de Datos
Las consultas pobremente optimizadas pueden exacerbar la contención de bloqueo al mantener bloqueos por más tiempo del necesario. Para abordar esto:

- **Analizar y Optimizar Consultas**: Use herramientas de perfilado de base de datos para identificar consultas lentas. Agregue índices apropiados, evite escaneos de tabla innecesarios y minimice el alcance de las filas bloqueadas (por ejemplo, use cláusulas `WHERE` precisas).
- **Evitar Bloqueos Excesivamente Amplios**: Tenga cuidado con sentencias como `SELECT ... FOR UPDATE`, que bloquean filas explícitamente y pueden bloquear otras transacciones. Úselas solo cuando sea necesario y asegúrese de que afecten el menor número de filas posible.

#### 3. Ajustar Configuraciones de Transacción
La anotación `@Transactional` de Spring proporciona atributos para afinar el comportamiento de las transacciones. Si bien estos no resolverán directamente los fallos de rollback, pueden ayudar a gestionar la concurrencia:

- **Nivel de Aislamiento**: El nivel de aislamiento por defecto (`DEFAULT`) típicamente se asigna al valor por defecto de la base de datos (a menudo `READ_COMMITTED`). Aumentarlo a `REPEATABLE_READ` o `SERIALIZABLE` podría asegurar la consistencia de datos pero podría empeorar la contención de bloqueo. Por el contrario, mantener `READ_COMMITTED` o inferior (si se admite) podría reducir los problemas de bloqueo, dependiendo de su caso de uso. Pruebe cuidadosamente para encontrar el equilibrio correcto.
- **Comportamiento de Propagación**: El valor por defecto `REQUIRED` se une a una transacción existente o inicia una nueva. Usar `REQUIRES_NEW` suspende la transacción actual e inicia una nueva, potencialmente evitando conflictos con una transacción bloqueada. Sin embargo, esto puede no abordar problemas específicos de rollback.
- **Timeout**: Establezca un valor de `timeout` (en segundos) en `@Transactional(timeout = 10)` para que las transacciones fallen más rápido si están esperando por bloqueos. Esto evita reintentos prolongados pero no soluciona la causa raíz.

Ejemplo:
```java
@Transactional(timeout = 5, propagation = Propagation.REQUIRES_NEW)
public void performDatabaseOperation() {
    // Su código aquí
}
```

#### 4. Implementar Lógica de Reintento (Con Precaución)
Dado que la excepción ocurre después de múltiples reintentos internos (alrededor de 20), es probable que el gestor de transacciones de Spring ya esté intentando manejar el problema. Sin embargo, puede implementar lógica de reintento personalizada a un nivel superior:

- **Usando Spring Retry**:
  Anote un método de servicio con `@Retryable` para reintentar en `TransactionRollbackException`. Especifique el número de intentos y el retraso entre reintentos. Combínelo con un método `@Recover` para manejar el fallo después de que se agoten los reintentos.
  ```java
  import org.springframework.retry.annotation.Backoff;
  import org.springframework.retry.annotation.Retryable;
  import org.springframework.retry.annotation.Recover;
  import org.springframework.transaction.annotation.Transactional;

  @Service
  public class MyService {

      @Retryable(value = TransactionRollbackException.class, maxAttempts = 3, backoff = @Backoff(delay = 1000))
      public void executeOperation() {
          performTransactionalWork();
      }

      @Transactional
      private void performTransactionalWork() {
          // Operaciones de base de datos que podrían fallar
      }

      @Recover
      public void recover(TransactionRollbackException e) {
          // Registrar error, notificar administradores, o tomar acción correctiva
          System.err.println("Todos los reintentos fallaron: " + e.getMessage());
      }
  }
  ```
  **Nota**: Cada reintento inicia una nueva transacción, lo que podría no ser ideal si se requiere atomicidad a través de los reintentos. Aplique esto fuera del método `@Transactional` si es posible.

- **Reintento Manual con TransactionTemplate**:
  Para más control, use `TransactionTemplate` para envolver su código transaccional en un bucle de reintento:
  ```java
  import org.springframework.transaction.PlatformTransactionManager;
  import org.springframework.transaction.TransactionStatus;
  import org.springframework.transaction.support.TransactionCallbackWithoutResult;
  import org.springframework.transaction.support.TransactionTemplate;

  @Service
  public class MyService {
      private final TransactionTemplate transactionTemplate;
      private static final int MAX_REINTENTOS = 3;
      private static final long RETRASO_REINTENTO_MS = 1000;

      public MyService(PlatformTransactionManager transactionManager) {
          this.transactionTemplate = new TransactionTemplate(transactionManager);
      }

      public void executeWithRetry() {
          for (int i = 0; i < MAX_REINTENTOS; i++) {
              try {
                  transactionTemplate.execute(new TransactionCallbackWithoutResult() {
                      @Override
                      protected void doInTransactionWithoutResult(TransactionStatus status) {
                          // Código transaccional aquí
                      }
                  });
                  return; // Éxito, salir del bucle
              } catch (TransactionRollbackException e) {
                  if (i == MAX_REINTENTOS - 1) {
                      throw e; // Relanzar después de reintentos máximos
                  }
                  try {
                      Thread.sleep(RETRASO_REINTENTO_MS);
                  } catch (InterruptedException ie) {
                      Thread.currentThread().interrupt();
                  }
              }
          }
      }
  }
  ```
  **Precaución**: Reintentar puede no resolver el problema si el bloqueo persiste, y podría conducir a estados inconsistentes si se aplican cambios parciales antes de que falle el rollback. Asegúrese de que los reintentos sean idempotentes o seguros.

#### 5. Manejar la Excepción con Elegancia
Si el rollback falla debido a bloqueos persistentes, el estado de la base de datos puede volverse inconsistente, requiriendo un manejo cuidadoso:

- **Capturar y Registrar**:
  Envuelva la llamada transaccional en un bloque try-catch, registre la excepción y notifique a los administradores:
  ```java
  try {
      myService.performTransactionalWork();
  } catch (TransactionRollbackException e) {
      // Registrar el error
      logger.error("El rollback de la transacción falló después de reintentos: " + e.getMessage(), e);
      // Notificar administradores (por ejemplo, vía email o sistema de monitoreo)
      sistemaDeAlerta.notify("Crítico: Fallo en rollback de transacción");
      // Fallar elegantemente o entrar en un estado seguro
      throw new RuntimeException("Operación falló debido a problemas de transacción", e);
  }
  ```

- **Fallo Seguro**: Si el estado de la transacción es incierto, detenga operaciones posteriores que dependan de ella y señale la necesidad de intervención manual.

#### 6. Aprovechar Características de la Base de Datos
Ajuste la configuración de la base de datos para mitigar problemas relacionados con bloqueos:

- **Lock Timeout**: Configure la base de datos para que falle rápidamente en esperas de bloqueo (por ejemplo, `SET LOCK_TIMEOUT 5000` en SQL Server o `innodb_lock_wait_timeout` en MySQL). Esto hace que la transacción falle antes, permitiendo que Spring maneje la excepción más pronto.
- **Detección de Deadlocks**: Asegúrese de que la detección de deadlocks de la base de datos esté habilitada y configurada para resolver conflictos revirtiendo una transacción automáticamente.
- **Bloqueo Optimista**: Si usa JPA, aplique `@Version` a las entidades para usar bloqueo optimista, reduciendo la contención de bloqueo físico:
  ```java
  @Entity
  public class MyEntity {
      @Id
      private Long id;
      @Version
      private Integer version;
      // Otros campos
  }
  ```
  Esto desplaza la detección de conflictos al momento del commit pero puede no abordar directamente los fallos de rollback.

#### 7. Monitorear e Investigar
Las ocurrencias frecuentes de esta excepción indican un problema subyacente:

- **Agregar Monitoreo**: Use herramientas como Spring Boot Actuator o un framework de logging para rastrear estas excepciones y su frecuencia.
- **Analizar Registros**: Revise los registros de la base de datos y de la aplicación en busca de patrones (por ejemplo, consultas o transacciones específicas que causen bloqueos).
- **Afinar Concurrencia**: Si la contención persiste, reconsidere el modelo de concurrencia de su aplicación o el diseño de la base de datos.

---

### Por Qué Falla el Rollback
El fallo del rollback después de 20 intentos sugiere que el gestor de transacciones de Spring reintenta la operación de rollback cuando encuentra un recurso bloqueado o una conexión perdida, eventualmente dándose por vencido. Esto podría originarse por:

- **Bloqueos Persistentes**: Otra transacción mantiene un bloqueo que no se libera dentro de la ventana de reintento.
- **Problemas de Conexión**: El pool de conexiones de base de datos (por ejemplo, HikariCP) agota sus reintentos para obtener una conexión.
- **Mala Configuración de la Base de Datos**: Los ajustes de timeout o reintento en la base de datos o el pool de conexiones son demasiado agresivos o insuficientes.

---

### Enfoque Recomendado
Aquí hay una solución práctica que combina las estrategias anteriores:

1. **Optimizar Transacciones y Consultas**: Mantenga las transacciones cortas y las consultas eficientes para reducir la duración del bloqueo.
2. **Establecer un Timeout de Transacción**: Use `@Transactional(timeout = 5)` para fallar rápidamente si los bloqueos persisten.
3. **Manejar con Reintento y Recuperación**:
   ```java
   @Service
   public class MyService {
       @Autowired
       private MyRepository repository;

       public void executeOperationWithRetry() {
           int maxAttempts = 3;
           for (int i = 0; i < maxAttempts; i++) {
               try {
                   performTransactionalWork();
                   return;
               } catch (TransactionRollbackException e) {
                   if (i == maxAttempts - 1) {
                       logger.error("Falló después de {} intentos: {}", maxAttempts, e.getMessage(), e);
                       sistemaDeAlerta.notify("Fallo en rollback de transacción");
                       throw e;
                   }
                   try {
                       Thread.sleep(1000); // Esperar antes de reintentar
                   } catch (InterruptedException ie) {
                       Thread.currentThread().interrupt();
                   }
               }
           }
       }

       @Transactional
       private void performTransactionalWork() {
           // Operaciones de base de datos
           repository.save(algunaEntidad);
       }
   }
   ```
4. **Monitorear y Ajustar**: Registre la excepción, configure alertas e investigue las causas de la contención de bloqueo.

---

### Conclusión
Para manejar `SqlTransactionRollbackException` en Spring cuando otra transacción mantiene un bloqueo, causando fallos en la obtención de conexiones e intentos repetidos, concéntrese en minimizar la contención de bloqueo a través de transacciones cortas y consultas optimizadas, ajuste las configuraciones de transacción según sea necesario, implemente lógica de reintento cautelosa a un nivel superior y maneje la excepción registrando y notificando apropiadamente. Esto asegura la estabilidad del sistema y la integridad de los datos mientras aborda la causa raíz con el tiempo a través del monitoreo y ajuste.

---

Al trabajar con el controlador Java de IBM DB2 (específicamente el controlador JDBC), manejar escenarios de rollback de transacciones es esencial para una interacción robusta con la base de datos. La consulta se refiere a `SqlTransactionRollbackException`, lo que parece ser un error ortográfico menor. En JDBC estándar, particularmente desde la versión 4.0 en adelante (compatible con controladores modernos de IBM DB2 como `db2jcc4.jar`), la excepción correcta es **`SQLTransactionRollbackException`**. Esta excepción es una subclase de `SQLException` y se lanza cuando una transacción de base de datos se revierte automáticamente, como en casos de deadlocks o timeouts.

Aquí se explica cómo manejar `SQLTransactionRollbackException` efectivamente en su código Java cuando use el controlador JDBC de IBM DB2:

### Enfoque para Manejar la Excepción

1. **Usar un Bloque Try-Catch**: Envuelva sus operaciones transaccionales de base de datos en un bloque `try` y capture `SQLTransactionRollbackException` para manejar casos donde la transacción es revertida por la base de datos.
2. **Tomar Acción Apropiada**: Dependiendo de los requisitos de su aplicación, podría registrar el error, reintentar la transacción (si el problema es transitorio, como un deadlock) o notificar al usuario del fallo.
3. **Asegurar Limpieza de Recursos**: Gestione adecuadamente los recursos de base de datos (por ejemplo, cerrar la conexión) en un bloque `finally` para evitar fugas de recursos.
4. **Respaldo para Controladores Antiguos**: Si está usando un controlador DB2 antiguo que no soporta JDBC 4.0, puede que necesite capturar `SQLException` y verificar el código de error (por ejemplo, `-911` para un rollback inducido por deadlock en DB2).

### Código de Ejemplo

Aquí hay un ejemplo práctico que demuestra cómo manejar `SQLTransactionRollbackException`:

```java
import java.sql.Connection;
import java.sql.SQLException;
import java.sql.SQLTransactionRollbackException;
import javax.sql.DataSource;

public class DB2TransactionExample {
    public void performTransaction(DataSource dataSource) {
        Connection conn = null;
        try {
            // Obtener una conexión y deshabilitar auto-commit para iniciar una transacción
            conn = dataSource.getConnection();
            conn.setAutoCommit(false);

            // Realizar sus operaciones de base de datos aquí
            // por ejemplo, ejecutar sentencias como INSERT, UPDATE, etc.

            // Si todas las operaciones tienen éxito, confirmar la transacción
            conn.commit();
        } catch (SQLTransactionRollbackException e) {
            // Manejar el caso donde la transacción fue revertida por DB2
            System.err.println("Transacción revertida por la base de datos: " + e.getMessage());
            System.err.println("Estado SQL: " + e.getSQLState() + ", Código de Error: " + e.getErrorCode());
            // Ejemplo: Estado SQL '40001' y Código de Error -911 indican un deadlock o timeout en DB2
            // Opcionalmente reintentar la transacción o notificar al usuario
        } catch (SQLException e) {
            // Manejar otras excepciones SQL
            System.err.println("Error SQL: " + e.getMessage());
            // Intentar revertir manualmente si la transacción aún está activa
            if (conn != null) {
                try {
                    conn.rollback();
                    System.out.println("Transacción revertida manualmente.");
                } catch (SQLException rollbackEx) {
                    System.err.println("El rollback falló: " + rollbackEx.getMessage());
                }
            }
        } finally {
            // Limpiar recursos
            if (conn != null) {
                try {
                    conn.setAutoCommit(true); // Restaurar comportamiento por defecto
                    conn.close();
                } catch (SQLException closeEx) {
                    System.err.println("Falló al cerrar la conexión: " + closeEx.getMessage());
                }
            }
        }
    }
}
```

### Puntos Clave en el Código

- **Capturando `SQLTransactionRollbackException`**: Esto captura específicamente casos donde DB2 revierte la transacción (por ejemplo, debido a un deadlock, indicado por el código de error `-911` o estado SQL `40001`).
- **Captura General de `SQLException`**: Esto sirve como respaldo para otros errores de base de datos, asegurando un manejo de errores más amplio.
- **Rollback Manual**: Si ocurre una `SQLException` y la transacción no ha sido revertida automáticamente, puede intentar un rollback manual.
- **Gestión de Recursos**: El bloque `finally` asegura que la conexión se cierre, previniendo fugas de recursos.

### Consideraciones Adicionales

- **Versión del Controlador**: Asegúrese de usar un controlador IBM DB2 compatible con JDBC 4.0 (por ejemplo, `db2jcc4.jar`). Los controladores más antiguos (por ejemplo, `db2jcc.jar`) pueden solo lanzar `SQLException`, requiriendo que verifique el código de error manualmente. Por ejemplo:
  ```java
  catch (SQLException e) {
      if (e.getErrorCode() == -911) {
          // Manejar rollback de transacción debido a deadlock o timeout
      }
  }
  ```
- **Estados SQL y Códigos de Error**: DB2 usa el estado SQL `40001` para fallos de serialización (como deadlocks) y el código de error `-911` cuando la transacción es revertida automáticamente. El código de error `-913` indica un fallo de sentencia debido a deadlock, pero la transacción permanece activa a menos que se revierta explícitamente.
- **Lógica de Reintento**: Para problemas transitorios como deadlocks, podría implementar un mecanismo de reintento:
  ```java
  int maxReintentos = 3;
  for (int intento = 1; intento <= maxReintentos; intento++) {
      try {
          performTransaction(dataSource);
          break; // Éxito, salir del bucle
      } catch (SQLTransactionRollbackException e) {
          if (intento == maxReintentos) {
              throw e; // Relanzar después de reintentos máximos
          }
          Thread.sleep(1000 * intento); // Retroceso antes de reintentar
      }
  }
  ```

### Conclusión

Para manejar `SQLTransactionRollbackException` (correctamente `SQLTransactionRollbackException`) en el controlador Java de IBM DB2, use un bloque `try-catch` para capturar esta excepción específica para escenarios de rollback de transacciones. Combínelo con una gestión adecuada de recursos y, si es necesario, lógica de respaldo para controladores antiguos verificando códigos de error como `-911`. Este enfoque asegura que su aplicación maneje elegantemente los rollbacks de transacciones mientras mantiene la integridad de la base de datos y la experiencia del usuario.
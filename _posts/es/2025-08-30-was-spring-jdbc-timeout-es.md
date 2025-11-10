---
audio: false
generated: true
image: false
lang: es
layout: post
title: Guía de Clasificación de Tiempos de Espera de Spring JDBC
translated: true
type: note
---

Aquí tienes el modelo mental y un manual de triaje rápido.

# Cómo funciona (WAS + Spring + JDBC)

1.  **DataSource reside en WAS**

    *   Defines un Proveedor JDBC y un **DataSource** (normalmente `XA` para transacciones globales, o no-XA) en la consola de administración de WAS.
    *   WAS gestiona el **pool de conexiones JCA** y entrega Conexiones JDBC.

2.  **Spring obtiene el DataSource vía JNDI**

    *   Tu aplicación Spring busca el DataSource del servidor (ej., `java:comp/env/jdbc/MyDS`) y lo envuelve:

        *   JDBC simple: `JdbcTemplate` usa ese DataSource.
        *   JPA/Hibernate: el `EntityManagerFactory` lo usa.
    *   Las transacciones son típicamente **JTA del contenedor** (`WebSphereUowTransactionManager` o JTA estándar). El `@Transactional` de Spring se une a la transacción del contenedor.

3.  **Ruta de la llamada**

    *   Petición web → hilo de WebContainer → servicio Spring → comienza la transacción (JTA) → `DataSource.getConnection()` del **pool de WAS** → SQL vía driver → BD.
    *   Los tiempos de espera pueden activarse en múltiples capas (Spring, JPA, pool de WAS, transacción JTA, driver JDBC/BD, red).

# Cuando ocurre un timeout — identifica de qué tipo es

Piensa en cuatro categorías. El mensaje/stack trace normalmente te dice cuál.

1.  **Timeout de adquisición de conexión**
    Síntoma: esperando por una conexión del pool.
    Busca mensajes sobre agotamiento del pool o `J2CA0086W / J2CA0030E`.
    Controles típicos: *Maximum Connections*, *Connection Timeout*, *Aged Timeout*, *Purge Policy*.

2.  **Timeout de transacción (JTA)**
    Síntoma: mensajes `WTRN`/`Transaction`; excepción como *"Transaction timed out after xxx seconds"*.
    Control típico: **Total transaction lifetime timeout**. Puede matar operaciones largas de BD incluso si la BD sigue funcionando.

3.  **Timeout de consulta/sentencia**
    Síntoma: `java.sql.SQLTimeoutException`, "query timeout" de Hibernate/JPA, o `QueryTimeoutException` de Spring.
    Controles:

    *   Spring: `JdbcTemplate.setQueryTimeout(...)`, Hibernate `javax.persistence.query.timeout` / `hibernate.jdbc.timeout`.
    *   Propiedades personalizadas del DataSource de WAS (ejemplos para DB2): `queryTimeout`, `queryTimeoutInterruptProcessingMode`.
    *   Timeout de sentencia del lado del driver/BD.

4.  **Timeout de socket/lectura / red**
    Síntoma: después de un tiempo inactivo durante una recuperación larga de datos; `SocketTimeoutException` de bajo nivel o código del proveedor.
    Controles: `loginTimeout`/`socketTimeout` del driver, firewalls/NAT inactivos, keepalives de la BD.

# Dónde comprobar (por capa)

**Rutas en la Consola de Administración de WAS (WAS tradicional)**

*   Proveedor JDBC / DataSource:
    Resources → JDBC → Data sources → *TuDS* →

    *   *Connection pool properties*: **Connection timeout**, **Maximum connections**, **Reap time**, **Unused timeout**, **Aged timeout**, **Purge policy**.
    *   *Custom properties*: específicas del proveedor (ej., DB2 `queryTimeout`, `currentSQLID`, `blockingReadConnectionTimeout`, `queryTimeoutInterruptProcessingMode`).
    *   *JAAS – J2C* si los alias de autenticación son relevantes.
*   Transacciones:
    Application servers → *server1* → Container Settings → **Container Services → Transaction Service** → **Total transaction lifetime timeout**, **Maximum transaction timeout**.
*   WebContainer:
    Tamaño del pool de hilos (si las peticiones se acumulan).

**Logs y trazas**

*   WAS tradicional: `<profile_root>/logs/<server>/SystemOut.log` y `SystemErr.log`.
    Componentes clave: `RRA` (adaptadores de recursos), `JDBC`, `ConnectionPool`, `WTRN` (transacciones).
    Habilita traza (inicio conciso):

    ```
    RRA=all:WTRN=all:Transaction=all:JDBC=all:ConnectionPool=all
    ```

    Busca:

    *   `J2CA0086W`, `J2CA0114W` (problemas de pool/conexión)
    *   `WTRN0037W`, `WTRN0124I` (timeouts/rollbacks de transacciones)
    *   Excepciones `DSRA`/`SQL` con códigos SQL del proveedor.
*   Liberty: `messages.log` en `wlp/usr/servers/<server>/logs/`.

**PMI / Monitorización**

*   Habilita **PMI** para JDBC Connection Pools y métricas de Transacción. Observa:

    *   Tamaño del pool, contador en uso, en espera, tiempo de espera, timeouts.
    *   Contadores de timeouts/rollbacks de transacciones.

**Logs de la aplicación Spring/JPA**

*   Activa SQL + temporización en tu aplicación (`org.hibernate.SQL`, `org.hibernate.type`, debug de Spring JDBC) para correlacionar duraciones vs. timeouts.

**Base de datos y driver**

*   DB2: `db2diag.log`, `MON_GET_PKG_CACHE_STMT`, monitores de eventos de actividad, timeouts a nivel de sentencia.
*   Propiedades del driver en el DataSource de WAS o `DriverManager` si no usas el DataSource del contenedor (no es típico en WAS).

**Red**

*   Dispositivos intermedios con timeouts por inactividad. Configuraciones keepalive del SO / keepalive del driver.

# Flujo de triaje rápido

1.  **Clasifica el timeout**

    *   ¿Espera de conexión? Busca advertencias de pool `J2CA`. Si es así, aumenta **Maximum connections**, corrige fugas, ajusta el pool, establece **Purge Policy = EntirePool** para eventos de conexión dañada.
    *   ¿Timeout de transacción? Mensajes `WTRN`. Aumenta **Total transaction lifetime timeout** o reduce el trabajo por transacción; evita envolver trabajos por lotes enormes en una sola transacción.
    *   ¿Timeout de consulta? `SQLTimeoutException` o `QueryTimeout` de Spring/Hibernate. Alinea los timeouts de **Spring/Hibernate** con los de **WAS DS** y la **BD**; evita configuraciones conflictivas.
    *   ¿Timeout de socket/lectura? Mensajes de red/driver. Comprueba `socketTimeout`/`loginTimeout` del driver, keepalives de la BD y firewalls.

2.  **Correlaciona los tiempos**

    *   Compara la duración del fallo con los umbrales configurados (ej., "falla a los ~30s" → busca cualquier configuración de 30s: ¿timeout de consulta de Spring 30s? ¿tiempo de vida de la transacción 30s? ¿espera en el pool 30s?).

3.  **Comprueba la salud del pool**

    *   PMI: ¿**waiters** > 0? ¿**in-use** está cerca del **máximo**? ¿Tenedores de larga duración? Considera habilitar **connection leak detection** (el trace RRA muestra quién tomó la conexión).

4.  **Visibilidad en la BD**

    *   Confirma en la BD: ¿la sentencia seguía ejecutándose? ¿Fue cancelada? ¿Alguna espera de bloqueo? Si hay bloqueos → considera el timeout de bloqueo vs. el timeout de sentencia.

# Controles útiles y problemas comunes (ejemplos WAS + DB2)

*   **Total transaction lifetime timeout** (a nivel de servidor) matará consultas largas incluso si estableces un timeout mayor en Spring/Hibernate. Mantén estos consistentes.
*   **queryTimeoutInterruptProcessingMode** (propiedad personalizada del DataSource para DB2): controla cómo debe interrumpir DB2 una consulta con timeout (cooperativo/forzoso). Ayuda a evitar hilos atascados más allá de los timeouts.
*   **Purge policy**: `EntirePool` puede recuperarse más rápido de estados SQL fatales (ej., reinicio de BD) a costa de un pico.
*   **Aged/Unused timeout**: retira conexiones obsoletas para esquivar timeouts por inactividad de firewalls/NAT.
*   **Validación**: habilita **validation by SQL** o **validation timeout** para que las conexiones muertas se detecten antes de su uso.
*   **Thread pools**: si los hilos de WebContainer están saturados, *los síntomas parecen timeouts*. Asegúrate de que los pools de hilos WebContainer y Default estén dimensionados apropiadamente.

# Ejemplos mínimos de configuración Spring

**DataSource JNDI (XML)**

```xml
<jee:jndi-lookup id="dataSource" jndi-name="java:comp/env/jdbc/MyDS" expected-type="javax.sql.DataSource"/>
<bean id="txManager" class="org.springframework.transaction.jta.JtaTransactionManager"/>
<tx:annotation-driven transaction-manager="txManager"/>
```

**Timeout de consulta en JdbcTemplate (Java)**

```java
@Bean JdbcTemplate jdbcTemplate(DataSource ds) {
  JdbcTemplate jt = new JdbcTemplate(ds);
  jt.setQueryTimeout(60); // segundos
  return jt;
}
```

**Timeout en Hibernate/JPA**

```properties
javax.persistence.query.timeout=60000  # ms
hibernate.jdbc.timeout=60              # segundos
```

# Qué capturar cuando escalas el problema

*   Texto exacto de la excepción + stack trace.
*   Marcas de tiempo: inicio de la petición, inicio de la transacción, inicio de la consulta, hora del error.
*   Configuración del pool de WAS DS (captura de pantalla o valores), timeouts del Transaction Service.
*   Instantánea de PMI (en espera en el pool, en uso, contadores de timeout).
*   Vista de la BD de la sesión/sentencia en el momento del fallo.
*   Notas sobre la topología de red (firewalls, proxies, temporizadores de inactividad).

Si pegas un fragmento específico de una excepción (estado J2CA/WTRN/SQL), puedo señalar la capa exacta y la configuración correspondiente a ajustar.
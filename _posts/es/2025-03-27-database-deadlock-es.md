---
audio: false
generated: true
lang: es
layout: post
title: Bloqueo de Base de Datos
translated: true
type: note
---

Un **interbloqueo de base de datos** ocurre cuando dos o más transacciones están esperando la una a la otra para liberar bloqueos sobre recursos, creando una dependencia circular que impide que cualquiera de ellas pueda continuar. El sistema de gestión de bases de datos (DBMS) normalmente detecta esta situación y la resuelve revirtiendo una de las transacciones. A continuación se muestra un ejemplo detallado de un escenario de interbloqueo:

---

### Ejemplo: Interbloqueo Entre Dos Transacciones
- **Escenario**:
  - La transacción T1 actualiza una fila en la tabla `Orders` y luego necesita actualizar una fila en la tabla `Customers`.
  - La transacción T2 actualiza una fila en la tabla `Customers` y luego necesita actualizar una fila en la tabla `Orders`.
  - Ambas transacciones bloquean recursos en un orden diferente, lo que lleva a un interbloqueo.

- **Paso a Paso**:
  1. T1 bloquea una fila en `Orders`.
  2. T2 bloquea una fila en `Customers`.
  3. T1 intenta bloquear la fila en `Customers` (bloqueada por T2).
  4. T2 intenta bloquear la fila en `Orders` (bloqueada por T1).
  - Resultado: Ninguna transacción puede proceder, creando un interbloqueo.

- **Ejemplo SQL**:
  ```sql
  -- Transacción T1
  BEGIN TRANSACTION;
  UPDATE Orders SET Status = 'Shipped' WHERE OrderID = 100;  -- Bloquea OrderID 100
  -- (algún retraso o procesamiento)
  UPDATE Customers SET LastOrderDate = '2025-03-27' WHERE CustomerID = 1;  -- Bloqueada por T2

  -- Transacción T2
  BEGIN TRANSACTION;
  UPDATE Customers SET Balance = Balance - 50 WHERE CustomerID = 1;  -- Bloquea CustomerID 1
  -- (algún retraso o procesamiento)
  UPDATE Orders SET PaymentStatus = 'Paid' WHERE OrderID = 100;  -- Bloqueada por T1
  ```

- **Qué Sucede**:
  - T1 mantiene un bloqueo exclusivo en `OrderID = 100` y espera por `CustomerID = 1`.
  - T2 mantiene un bloqueo exclusivo en `CustomerID = 1` y espera por `OrderID = 100`.
  - Esta condición de espera circular es un interbloqueo.
  - El DBMS detecta esto (por ejemplo, mediante un timeout o un algoritmo de detección de interbloqueos) y revierte una transacción (por ejemplo, T2), permitiendo que T1 complete.

---

### Representación Visual del Interbloqueo
```
T1: Bloquea Orders(100) --> Quiere Customers(1)
   |                                      ↑
   |                                      |
T2: Quiere Orders(100)  <-- Bloquea Customers(1)
```

- **Resolución**: El DBMS podría generar un error como:
  ```
  La transacción T2 fue interbloqueada en recursos de bloqueo con otro proceso y ha sido elegida como la víctima del interbloqueo. Vuelva a ejecutar la transacción.
  ```

---

### Por Qué Ocurre
- **Orden de Bloqueo**: T1 y T2 adquieren bloqueos en una secuencia diferente (T1: Orders → Customers; T2: Customers → Orders).
- **Concurrencia**: Ambas transacciones se ejecutan simultáneamente y necesitan recursos que se superponen.
- **Bloqueos Exclusivos**: Las actualizaciones requieren bloqueos exclusivos, que impiden que otras transacciones accedan a los mismos datos.

---

### Cómo Evitar Interbloqueos
1. **Orden de Bloqueo Consistente**: Asegurar que todas las transacciones adquieran bloqueos en el mismo orden (ej., siempre bloquear `Orders` antes que `Customers`).
   ```sql
   -- Tanto T1 como T2 deben bloquear Orders primero, luego Customers
   ```
2. **Reducir el Tiempo de Transacción**: Minimizar los retrasos dentro de las transacciones para reducir la posibilidad de superposición.
3. **Usar Niveles de Aislamiento Más Bajos**: Si es apropiado, usar un nivel de aislamiento menos estricto (ej., Read Committed) para reducir la duración de los bloqueos.
4. **Timeouts**: Establecer timeouts de bloqueo más cortos para fallar rápidamente y reintentar.

---

¡Avísame si quieres un ejemplo más específico (por ejemplo, con un DBMS particular como PostgreSQL o SQL Server) o alguna aclaración adicional!
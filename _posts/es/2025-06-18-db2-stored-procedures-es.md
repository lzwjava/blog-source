---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Invocación de Procedimientos Almacenados de DB2 con Parámetros
translated: true
type: note
---

### Suposiciones y Contexto
Tu consulta parece referirse a llamar a un *stored procedure* (probablemente un error tipográfico por "store procedure") en un sistema de base de datos de IBM, como IBM DB2 (en Linux/Unix/Windows, z/OS o iSeries). Los stored procedures son scripts ejecutables almacenados en la base de datos que pueden aceptar parámetros de entrada, realizar operaciones y devolver salidas o resultados. La sintaxis exacta depende del lenguaje de programación y el entorno de IBM (por ejemplo, SQL, COBOL, RPG o Java vía JDBC). Me centraré en el caso más común: sentencias CALL basadas en SQL en DB2, ya que es estándar para bases de datos relacionales.

Si estás utilizando una plataforma IBM diferente (por ejemplo, comandos CL de IBM i, MQ o Watson Query), proporciona más detalles para un consejo específico.

### Cómo Pasar Parámetros en una Llamada a un Stored Procedure de DB2
Los stored procedures en DB2 se llaman usando la sentencia `CALL` en SQL. Los parámetros se pasan en una lista separada por comas dentro de paréntesis, coincidiendo con la definición del procedimiento (por ejemplo, IN para entrada, OUT para salida, INOUT para ambos).

#### Guía Paso a Paso
1. **Define o Conoce la Firma del Procedimiento**: Asegúrate de conocer el nombre del procedimiento y sus parámetros. Por ejemplo, un procedimiento podría definirse como:
   ```sql
   CREATE PROCEDURE update_employee (IN emp_id INT, IN new_salary DECIMAL(10,2), OUT status_msg VARCHAR(100))
   ```
   - Aquí, `emp_id` es de entrada (IN), `new_salary` es de entrada, y `status_msg` es de salida (OUT).

2. **Usa la Sentencia CALL**: En un entorno SQL (por ejemplo, DB2 Command Line Processor, o embebido en programas como Java), llama al procedimiento así:
   ```sql
   CALL update_employee(12345, 75000.00, ?);
   ```
   - El `?` es un marcador de posición para parámetros OUT. En llamadas programáticas, maneja las salidas con conjuntos de resultados o variables host.
   - Las entradas se pasan como literales o variables; las salidas se capturan mediante marcadores de posición o variables vinculadas.

3. **Manejo de Tipos de Parámetros**:
   - **Parámetros IN**: Pasa valores directamente (por ejemplo, números, cadenas entre comillas).
   - **Parámetros OUT/INOUT**: Usa `?` en el CALL, luego enlázalos en tu código para recuperar los valores después de la ejecución.
   - Coincide el orden y los tipos exactamente; los desajustes causan errores (por ejemplo, SQLCODE -440 para parámetros no válidos).

4. **En Ejemplos de Código**:
   - **Vía DB2 CLP (Command Line)**: Ejecución SQL directa.
     ```sql
     CALL my_proc('input_value', ?);
     ```
     Recupera los parámetros OUT con `FETCH FIRST FROM` o en scripts.
   - **Vía JDBC (Java)**:
     ```java
     CallableStatement stmt = conn.prepareCall("{CALL update_employee(?, ?, ?)}");
     stmt.setInt(1, 12345);          // Parámetro IN
     stmt.setBigDecimal(2, new java.math.BigDecimal("75000.00")); // Parámetro IN
     stmt.registerOutParameter(3, Types.VARCHAR); // Parámetro OUT
     stmt.execute();
     String status = stmt.getString(3); // Recupera OUT
     ```
   - **Vía RPG en IBM i**: Usa `CALLP` con declaraciones de variables que coincidan con los tipos de parámetros.
     ```rpg
     D PROC_PARAM    S                   LIKE(PARAM_TYPE)
     PROC_PARAM = 'value';
     CALLP MY_PROC(PROC_PARAM);
     ```
   - **Manejo de Errores**: Verifica SQLSTATE o SQLCODE después de la llamada; por ejemplo, '00000' significa éxito.

#### Consejos Clave y Evidencia
- **Evidencia de la Documentación de DB2**: Según la Referencia SQL oficial de DB2 de IBM (por ejemplo, para LUW v11.5 o z/OS), la sentencia `CALL` se define con listas de parámetros opcionales. Por ejemplo, la sintaxis es: `CALL procedure-name [(parameter [, parameter] ...)]`. Esto coincide con los estándares de la industria para bases de datos relacionales y es compatible en todas las variantes de DB2 para consistencia (consulta el IBM Knowledge Center).
- **Variaciones**: En IBM i (AS400), los procedimientos podrían usar llamadas CL (Command Language) como `CALL PGM(MYPROC) PARM('value')` para programas RPG. Para COBOL en mainframe, embebe `EXEC SQL CALL...` con variables host.
- **Pruebas**: Usa `db2 describe routine procedure_name` para inspeccionar los parámetros antes de llamar.
- **Limitaciones**: Los conjuntos de parámetros grandes pueden necesitar arrays o conjuntos de resultados; los tipos complejos requieren un manejo específico.

Si esto no coincide con tu configuración (por ejemplo, si es IBM Watson u otra herramienta), comparte más contexto como la plataforma o el lenguaje para instrucciones precisas.
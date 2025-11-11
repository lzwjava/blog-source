---
audio: false
generated: true
lang: es
layout: post
title: Identificar Tablas con Datos en Oracle DB
translated: true
type: note
---

En Oracle Database, si estás explorando esquemas y encuentras que algunas tablas aparecen "vacías" cuando haces clic en ellas (por ejemplo, mediante una herramienta GUI como SQL Developer o Toad), no necesariamente significa que no tengan datos. Puede haber varias razones: permisos, filtros, o simplemente estás mirando las tablas incorrectas. Para descubrir sistemáticamente qué tablas en un esquema contienen datos, puedes consultar los metadatos de la base de datos o inspeccionar las tablas directamente. Aquí te explicamos cómo hacerlo:

#### 1. **Verifica Tus Permisos**
   - Si ves tablas vacías, podrías carecer de los privilegios para ver los datos. Asegúrate de tener privilegios `SELECT` en las tablas del esquema.
   - Ejecuta esto para verificar tus privilegios en una tabla específica:
     ```sql
     SELECT privilege
     FROM dba_tab_privs
     WHERE grantee = UPPER('tu_nombre_de_usuario')
     AND table_name = UPPER('nombre_de_la_tabla');
     ```
     Reemplaza `'tu_nombre_de_usuario'` y `'nombre_de_la_tabla'` según corresponda. Si no aparece nada, solicita al propietario del esquema o al DBA que te otorgue acceso.

#### 2. **Consulta el Número de Filas en las Tablas**
   - Oracle mantiene estadísticas sobre las tablas, incluidos los recuentos de filas, en las vistas `USER_TABLES`, `ALL_TABLES` o `DBA_TABLES` (dependiendo de tu nivel de acceso).
   - Para ver las tablas con datos en el esquema actual:
     ```sql
     SELECT table_name, num_rows
     FROM user_tables
     WHERE num_rows > 0
     ORDER BY num_rows DESC;
     ```
     - `USER_TABLES`: Muestra las tablas propiedad del usuario actual.
     - `NUM_ROWS`: Número aproximado de filas (basado en la última actualización de estadísticas).

   - Si tienes acceso a otro esquema (por ejemplo, a través de `ALL_TABLES`):
     ```sql
     SELECT owner, table_name, num_rows
     FROM all_tables
     WHERE num_rows > 0
     AND owner = UPPER('nombre_del_esquema')
     ORDER BY num_rows DESC;
     ```
     Reemplaza `'nombre_del_esquema'` con el esquema que estás investigando.

   **Nota**: `NUM_ROWS` podría estar desactualizado si las estadísticas no se han recopilado recientemente. Consulta el Paso 5 para actualizarlas.

#### 3. **Verifica Manualmente Tablas Específicas**
   - Si sospechas que `NUM_ROWS` no es confiable o quieres verificarlo, ejecuta un `COUNT(*)` en tablas individuales:
     ```sql
     SELECT table_name
     FROM user_tables;
     ```
     Esto lista todas las tablas en tu esquema. Luego, para cada tabla:
     ```sql
     SELECT COUNT(*) FROM nombre_de_la_tabla;
     ```
     Si el recuento es mayor que 0, la tabla tiene datos. Ten cuidado con las tablas grandes: `COUNT(*)` puede ser lento.

#### 4. **Usa un Script para Automatizar la Verificación**
   - Para evitar consultar manualmente cada tabla, usa un script PL/SQL para verificar los recuentos de filas en todas las tablas de un esquema:
     ```sql
     BEGIN
         FOR t IN (SELECT table_name FROM user_tables)
         LOOP
             EXECUTE IMMEDIATE 'SELECT COUNT(*) FROM ' || t.table_name INTO v_count;
             IF v_count > 0 THEN
                 DBMS_OUTPUT.PUT_LINE(t.table_name || ' tiene ' || v_count || ' filas');
             END IF;
         END LOOP;
     EXCEPTION
         WHEN OTHERS THEN
             DBMS_OUTPUT.PUT_LINE('Error en la tabla ' || t.table_name || ': ' || SQLERRM);
     END;
     /
     ```
     - Habilita la salida en tu herramienta (por ejemplo, `SET SERVEROUTPUT ON` en SQL*Plus o SQL Developer).
     - Esto imprime solo las tablas con datos. Ajusta `user_tables` a `all_tables` y agrega filtrado por `owner` si estás verificando otro esquema.

#### 5. **Actualiza las Estadísticas de la Tabla (si es Necesario)**
   - Si `NUM_ROWS` en `USER_TABLES` o `ALL_TABLES` muestra 0 o parece incorrecto, las estadísticas podrían estar obsoletas. Para actualizarlas:
     ```sql
     EXEC DBMS_STATS.GATHER_SCHEMA_STATS(ownname => 'nombre_del_esquema');
     ```
     Reemplaza `'nombre_del_esquema'` con el nombre del esquema (usa tu nombre de usuario para tu propio esquema). Luego, vuelve a ejecutar la consulta `USER_TABLES` del Paso 2.

#### 6. **Verifica si Hay Tablas Particionadas**
   - Si el esquema utiliza tablas particionadas, los datos podrían estar distribuidos en particiones, y una consulta simple podría no reflejar esto. Verifica las particiones:
     ```sql
     SELECT table_name, partition_name, num_rows
     FROM user_tab_partitions
     WHERE num_rows > 0
     ORDER BY table_name, partition_name;
     ```
     Esto muestra qué particiones contienen datos.

#### 7. **Consejos para Herramientas GUI (por ejemplo, SQL Developer)**
   - Si estás usando una GUI como Oracle SQL Developer:
     1. Haz clic derecho en el esquema en el panel de Conexiones.
     2. Expande el nodo "Tables".
     3. Haz clic derecho en una tabla, selecciona "Count Rows", o abre la pestaña "Data" para previsualizar el contenido (si está permitido).
     - Si la pestaña "Data" está vacía, podría ser un problema de permisos o la tabla realmente no tiene filas.

---

### Ejemplo Práctico
Supongamos que estás en un esquema llamado `HR`. Deberías:
1. Ejecutar:
   ```sql
   SELECT table_name, num_rows
   FROM user_tables
   WHERE num_rows > 0;
   ```
   La salida podría verse así:
   ```
   TABLE_NAME   NUM_ROWS
   ----------   --------
   EMPLOYEES    107
   DEPARTMENTS  27
   ```
   Esto te indica que `EMPLOYEES` y `DEPARTMENTS` tienen datos.

2. Si sospechas que las estadísticas están obsoletas, actualízalas:
   ```sql
   EXEC DBMS_STATS.GATHER_SCHEMA_STATS('HR');
   ```
3. Vuelve a verificar con la misma consulta.

---

### Por Qué las Tablas Podrían Parecer Vacías
- **Sin Datos**: La tabla realmente no tiene filas.
- **Permisos**: Puedes ver la estructura de la tabla pero no los datos.
- **Filtros**: Tu herramienta GUI podría tener filtros que ocultan filas (por ejemplo, una cláusula `WHERE`).
- **Datos Truncados/Eliminados**: Los datos podrían haber sido eliminados recientemente.
- **Sinónimos/Vistas**: Podrías estar mirando un sinónimo o una vista que apunta a una tabla vacía o inaccesible.

Si todavía tienes problemas, ¡avísame tu configuración específica (por ejemplo, nombre del esquema, herramienta utilizada) y puedo adaptar el consejo aún más!
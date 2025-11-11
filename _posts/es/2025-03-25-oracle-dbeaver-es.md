---
audio: false
generated: true
lang: es
layout: post
title: Pasos Para Usar DBeaver Para Verificar Tablas de Base de Datos Oracle en Busca
  de Datos
translated: true
type: note
---

Supongo que estás preguntando cómo usar DBeaver para verificar qué tablas de Oracle Database contienen datos, basándome en tu pregunta anterior sobre encontrar tablas con datos en Oracle DB. DBeaver es una herramienta de base de datos popular, gratuita y multiplataforma que funciona bien con Oracle y otras bases de datos. A continuación, te guiaré sobre cómo usar DBeaver para inspeccionar tus esquemas de Oracle e identificar tablas con datos.

---

#### 1. **Configurar una conexión a tu base de datos Oracle**
   - **Instalar DBeaver**: Si aún no lo has hecho, descarga e instala DBeaver (la Community Edition es suficiente) desde [dbeaver.io](https://dbeaver.io/).
   - **Crear una nueva conexión**:
     1. Abre DBeaver y haz clic en **Database** > **New Database Connection** en el menú.
     2. Selecciona **Oracle** de la lista y haz clic en **Next**.
     3. Ingresa los detalles de tu conexión:
        - **Host**: El nombre de host o IP de tu servidor Oracle.
        - **Port**: Típicamente 1521 (valor por defecto para Oracle).
        - **Database/SID o Service Name**: Dependiendo de tu configuración (por ejemplo, SID = `XE` para Express Edition o un nombre de servicio).
        - **Username** y **Password**: Tus credenciales de Oracle.
     4. Haz clic en **Test Connection** para verificar que funciona. Es posible que necesites descargar el controlador JDBC de Oracle si se te solicita (DBeaver puede hacer esto automáticamente).
     5. Haz clic en **Finish** para guardar la conexión.

#### 2. **Explorar esquemas en el Navegador de bases de datos**
   - En el **Database Navigator** (panel izquierdo), expande tu conexión de Oracle.
   - Verás una lista de esquemas (por ejemplo, tu nombre de usuario u otros a los que tengas acceso). Expande el esquema que deseas inspeccionar.
   - Debajo de cada esquema, expande el nodo **Tables** para ver todas las tablas.

#### 3. **Verificar tablas para datos usando la interfaz gráfica**
   - **Ver datos de la tabla**:
     1. Haz doble clic en un nombre de tabla o haz clic derecho y selecciona **Edit Table**.
     2. Cambia a la pestaña **Data** en el editor que se abre.
     3. Si la tabla tiene datos, verás filas mostradas. Si está vacía, no verás filas (o un mensaje como "No data").
     - Por defecto, DBeaver obtiene hasta 200 filas. Para obtener todas las filas, haz clic en el botón **Fetch All Rows** (un pequeño icono de flecha) en la barra de herramientas inferior de la pestaña Data.
   - **Contar filas rápidamente**:
     1. Haz clic derecho en la tabla en el Database Navigator.
     2. Selecciona **Navigate** > **Row Count**.
     3. DBeaver ejecuta una consulta `SELECT COUNT(*)` y muestra el resultado en una ventana emergente. Si es 0, la tabla está vacía.

#### 4. **Ejecutar consultas SQL para verificar múltiples tablas**
   - Si deseas verificar muchas tablas a la vez (más eficiente que hacer clic en cada una), usa el Editor SQL:
     1. Haz clic en **SQL Editor** > **New SQL Script** (o presiona `Ctrl + [`).
     2. Establece el contexto del esquema:
        - Usa el menú desplegable en la parte superior del Editor SQL para seleccionar tu esquema, o ejecuta:
          ```sql
          ALTER SESSION SET CURRENT_SCHEMA = schema_name;
          ```
          Reemplaza `schema_name` con tu esquema objetivo (por ejemplo, `HR`).
     3. Consulta el recuento de filas para todas las tablas:
        - Usa este SQL para listar tablas con datos (similar a mi respuesta anterior):
          ```sql
          SELECT table_name, num_rows
          FROM user_tables
          WHERE num_rows > 0
          ORDER BY num_rows DESC;
          ```
        - Ejecútalo presionando `Ctrl + Enter`. Los resultados aparecen en la pestaña **Results** debajo.
        - `USER_TABLES` muestra las tablas en tu esquema. Usa `ALL_TABLES` para las tablas a las que puedes acceder en todos los esquemas:
          ```sql
          SELECT owner, table_name, num_rows
          FROM all_tables
          WHERE num_rows > 0
          AND owner = UPPER('schema_name');
          ```
     4. **Nota**: `NUM_ROWS` es una estimación de la última actualización de estadísticas. Si no es precisa, actualiza las estadísticas con:
        ```sql
        EXEC DBMS_STATS.GATHER_SCHEMA_STATS('schema_name');
        ```
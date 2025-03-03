---
audio: true
generated: true
lang: es
layout: post
title: Cliente SQL SQuirreL y Base de Datos DB2
translated: true
---

Para usar tu archivo JAR de IBM DB2 JCC (`db2jcc.jar`) en SQuirreL SQL Client y conectarte a una base de datos DB2, sigue estos pasos detallados. Este proceso implica configurar el controlador DB2 en SQuirreL y establecer un alias de conexión.

---

### Paso 1: Verificar el archivo JAR
- Asegúrate de tener el archivo JAR correcto del controlador JDBC de DB2. El archivo que mencionaste, `db2jcc.jar`, es típicamente el correcto para IBM DB2, aunque algunas configuraciones pueden usar `db2jcc4.jar` dependiendo de la versión.
- Verifica si tu instalación de DB2 requiere un archivo de licencia adicional (por ejemplo, `db2jcc_license_cisuz.jar`). Si es así, localiza este archivo también, ya que puede ser necesario para evitar errores relacionados con la licencia al conectar.

---

### Paso 2: Configurar el controlador DB2 en SQuirreL SQL Client
1. **Abrir SQuirreL SQL Client**:
   - Inicia la aplicación en tu sistema.

2. **Acceder a la pestaña Controladores**:
   - En el panel izquierdo, haz clic en la pestaña **Controladores** para ver la lista de controladores de bases de datos disponibles.

3. **Localizar o agregar el controlador DB2**:
   - Busca un controlador DB2 existente en la lista (por ejemplo, "IBM DB2 App Driver"). Puede estar marcado con una X roja si no está configurado correctamente.
   - Si está presente, puedes modificarlo. Si no, deberás crear un nuevo controlador:
     - **Modificar controlador existente**: Haz doble clic en la entrada del controlador DB2.
     - **Agregar nuevo controlador**: Haz clic en el icono **+** en la pestaña Controladores para abrir el asistente "Agregar controlador".

4. **Configurar los ajustes del controlador**:
   - **Nombre**: Ingresa un nombre descriptivo, como "Controlador JCC de IBM DB2."
   - **URL de ejemplo**: Establece esto en `jdbc:db2://<host>:<port>/<database>` (personalizarás esto más adelante para tu base de datos específica).
   - **Nombre de la clase**: Ingresa `com.ibm.db2.jcc.DB2Driver` (esta es la clase de controlador estándar para JDBC de DB2).

5. **Agregar el archivo JAR**:
   - Ve a la pestaña **Ruta de clase adicional** en la ventana de configuración del controlador.
   - Haz clic en **Agregar**, luego navega y selecciona la ubicación de tu archivo `db2jcc.jar`.
   - Si tienes un archivo JAR de licencia (por ejemplo, `db2jcc_license_cisuz.jar`), haz clic en **Agregar** nuevamente e inclúyelo también.

6. **Guardar la configuración**:
   - Haz clic en **Aceptar** para guardar los ajustes del controlador. El controlador DB2 debería aparecer ahora en la pestaña Controladores con una marca de verificación, indicando que está configurado correctamente.

---

### Paso 3: Crear un alias de base de datos
1. **Cambiar a la pestaña Aliases**:
   - En el panel izquierdo, haz clic en la pestaña **Aliases**, que gestiona tus conexiones de bases de datos.

2. **Agregar un nuevo alias**:
   - Haz clic en el icono **+** para abrir el asistente "Agregar alias".

3. **Configurar el alias**:
   - **Nombre**: Dale a tu conexión un nombre (por ejemplo, "Mi base de datos DB2").
   - **Controlador**: Desde el menú desplegable, selecciona el controlador DB2 que configuraste en el Paso 2 (por ejemplo, "Controlador JCC de IBM DB2").
   - **URL**: Ingresa la URL de conexión para tu base de datos en el formato:
     ```
     jdbc:db2://<host>:<port>/<database>
     ```
     Reemplaza `<host>` (por ejemplo, `localhost` o la IP de tu servidor), `<port>` (por ejemplo, `50000`, el puerto predeterminado de DB2) y `<database>` (el nombre de tu base de datos) con tus detalles reales. Por ejemplo:
     ```
     jdbc:db2://localhost:50000/mydb
     ```
   - **Nombre de usuario** y **Contraseña**: Proporciona tus credenciales de la base de datos DB2.

4. **Guardar y conectar**:
   - Haz clic en **Aceptar** para guardar el alias.
   - En la pestaña Aliases, haz doble clic en tu nuevo alias para conectarte. Ingresa tu contraseña si se te solicita.

---

### Problemas potenciales y soluciones
- **Errores de licencia**:
  - Si ves un error como "La licencia de IBM Data Server para JDBC y SQLJ no es válida," asegúrate de que el archivo JAR de licencia (por ejemplo, `db2jcc_license_cisuz.jar`) esté agregado a la Ruta de clase adicional del controlador.
- **Errores de clase no encontrada**:
  - Si SQuirreL informa "No se pudo encontrar la clase com.ibm.db2.jcc.DB2Driver," verifica que:
    - El archivo `db2jcc.jar` esté correctamente agregado a la Ruta de clase adicional.
    - El nombre de la clase esté establecido en `com.ibm.db2.jcc.DB2Driver` sin errores tipográficos.
- **Conflictos de múltiples JAR**:
  - Evita incluir múltiples versiones del controlador JDBC de DB2 (por ejemplo, tanto `db2jcc.jar` como `db2jcc4.jar`) en la Ruta de clase adicional, ya que esto puede causar conflictos. Usa solo los JAR necesarios para tu versión de DB2.
- **Formato de URL incorrecto**:
  - Verifica nuevamente la sintaxis de tu URL de conexión. Una URL malformada (por ejemplo, puerto faltante o nombre de base de datos incorrecto) impedirá la conexión.

---

Siguiendo estos pasos, deberías poder configurar SQuirreL SQL Client para usar tu archivo `db2jcc.jar` y conectarte exitosamente a tu base de datos DB2. Si encuentras algún problema, revisa las sugerencias de solución de problemas anteriores o asegúrate de que tu servidor de base de datos sea accesible desde tu red.
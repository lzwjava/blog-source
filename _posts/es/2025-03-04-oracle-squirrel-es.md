---
audio: false
generated: true
lang: es
layout: post
title: Agregar el controlador JDBC de Oracle a Squirrel SQL Client
translated: true
---

Para agregar el controlador JDBC de Oracle a Squirrel SQL Client, sigue estos pasos detallados. Este proceso implica configurar el controlador y establecer un alias de conexión para tu base de datos Oracle.

### Paso 1: Localizar el Archivo Requerido
Necesitas el archivo del controlador JDBC de Oracle, específicamente `ojdbc.jar`. Este archivo contiene las clases necesarias para que Squirrel SQL Client se conecte a una base de datos Oracle. Asegúrate de haber descargado este archivo (por ejemplo, desde el sitio web de Oracle o de tu administrador de base de datos) y conocer su ubicación en tu sistema.

### Paso 2: Iniciar Squirrel SQL Client
Abre la aplicación Squirrel SQL Client en tu computadora.

### Paso 3: Acceder a la Pestaña de Controladores
En el lado izquierdo de la interfaz de Squirrel SQL Client, localiza y haz clic en la pestaña **Drivers**. Esta sección te permite gestionar los controladores JDBC disponibles para la aplicación.

### Paso 4: Agregar un Nuevo Controlador
- En la pestaña Drivers, haz clic en el botón **"+"** para abrir la ventana de diálogo "Add Driver".

### Paso 5: Nombre del Controlador
- En el campo "Name" de la ventana de diálogo "Add Driver", ingresa **Oracle Thin Driver**. Este es un nombre descriptivo para identificar el controlador de Oracle dentro de Squirrel SQL Client.

### Paso 6: Agregar el Archivo `ojdbc.jar`
- Cambia a la pestaña **Extra Class Path** dentro de la ventana de diálogo "Add Driver".
- Haz clic en el botón **Add**.
- Navega a la ubicación del archivo `ojdbc.jar` en tu sistema, selecciónalo y confirma para agregarlo al classpath del controlador.

### Paso 7: Especificar la Clase del Controlador Java
- En el campo "Class Name", ingresa la clase del controlador Java: **oracle.jdbc.OracleDriver**. Esto le indica a Squirrel SQL Client qué clase usar del archivo `ojdbc.jar` para manejar las conexiones a la base de datos Oracle.

### Paso 8: Proporcionar una URL de Ejemplo
- Opcionalmente, puedes especificar un formato de URL de ejemplo para conectarte a una base de datos Oracle:
  - **Para conectar mediante SID**: `jdbc:oracle:thin:@HOST[:PORT]:DB`
  - **Para conectar mediante nombre de servicio**: `jdbc:oracle:thin:@//HOST[:PORT]/DB`
- Reemplaza `HOST`, `PORT` y `DB` con valores reales al configurar una conexión más adelante (en la configuración del alias).

### Paso 9: Guardar la Configuración del Controlador
- Haz clic en **OK** para guardar la configuración del controlador y cerrar la ventana de diálogo "Add Driver". El "Oracle Thin Driver" debería aparecer ahora en la pestaña Drivers con una marca de verificación verde, indicando que está correctamente configurado.

### Paso 10: Crear un Alias para tu Base de Datos
- Cambia a la pestaña **Aliases** en el lado izquierdo de Squirrel SQL Client.
- Haz clic en el botón **"+"** para abrir la ventana de diálogo "Add Alias".

### Paso 11: Configurar el Alias
- En la ventana de diálogo "Add Alias":
  - **Name**: Ingresa un nombre para esta conexión (por ejemplo, "My Oracle DB").
  - **Driver**: Selecciona **Oracle Thin Driver** del menú desplegable.
  - **URL**: Ingresa la URL de conexión para tu base de datos Oracle específica:
    - Mediante SID: `jdbc:oracle:thin:@HOST[:PORT]:DB`
    - Mediante nombre de servicio: `jdbc:oracle:thin:@//HOST[:PORT]/DB`
    - Reemplaza `HOST` (por ejemplo, localhost o dirección IP), `PORT` (el valor predeterminado es 1521) y `DB` (SID o nombre de servicio) con los detalles de tu base de datos.
  - **Username**: Ingresa el nombre de usuario de la base de datos.
  - **Password**: Ingresa la contraseña de la base de datos.

### Paso 12: Probar la Conexión
- Haz clic en el botón **Test** en la ventana de diálogo "Add Alias" para verificar que Squirrel SQL Client puede conectarse a tu base de datos Oracle utilizando los detalles proporcionados. Si es exitoso, verás un mensaje de confirmación.

### Paso 13: Guardar el Alias
- Si la prueba de conexión tiene éxito, haz clic en **OK** para guardar el alias. El nuevo alias ahora aparecerá en la pestaña Aliases.

### Paso 14: Conectar a la Base de Datos
- En la pestaña Aliases, selecciona tu alias recién creado (por ejemplo, "My Oracle DB").
- Haz clic en el botón **Connect** para establecer una conexión a tu base de datos Oracle. Una vez conectado, puedes comenzar a consultar tu base de datos utilizando Squirrel SQL Client.

### Resumen de Información Clave
- **Archivo Requerido**: `ojdbc.jar`
- **Clase del Controlador Java**: `oracle.jdbc.OracleDriver`
- **Formatos de URL**:
  - SID: `jdbc:oracle:thin:@HOST[:PORT]:DB`
  - Nombre de Servicio: `jdbc:oracle:thin:@//HOST[:PORT]/DB`

Siguiendo estos pasos, habrás agregado con éxito el controlador JDBC de Oracle a Squirrel SQL Client y configurado una conexión a tu base de datos Oracle. Asegúrate de que todos los detalles (ruta del archivo, URL, credenciales) sean precisos para evitar problemas de conexión.
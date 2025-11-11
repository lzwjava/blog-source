---
audio: false
generated: true
lang: es
layout: post
title: Cómo Agregar el Controlador JDBC de Oracle al Cliente Squirrel SQL
translated: true
type: note
---

Para agregar el controlador JDBC de Oracle a Squirrel SQL Client, siga estos pasos detallados. Este proceso implica configurar el controlador y establecer un alias de conexión para su base de datos Oracle.

### Paso 1: Localizar el Archivo Requerido
Necesita el archivo del controlador JDBC de Oracle, específicamente `ojdbc.jar`. Este archivo contiene las clases necesarias para permitir que Squirrel SQL Client se conecte a una base de datos Oracle. Asegúrese de haber descargado este archivo (por ejemplo, desde el sitio web de Oracle o de su administrador de base de datos) y conozca su ubicación en su sistema.

### Paso 2: Iniciar Squirrel SQL Client
Abra la aplicación Squirrel SQL Client en su computadora.

### Paso 3: Acceder a la Pestaña de Controladores
En el lado izquierdo de la interfaz de Squirrel SQL Client, localice y haga clic en la pestaña **Drivers**. Esta sección le permite gestionar los controladores JDBC disponibles para la aplicación.

### Paso 4: Agregar un Nuevo Controlador
- En la pestaña Drivers, haga clic en el botón **"+"** para abrir el cuadro de diálogo "Add Driver".

### Paso 5: Nombrar el Controlador
- En el campo "Name" del cuadro de diálogo "Add Driver", ingrese **Oracle Thin Driver**. Este es un nombre descriptivo para identificar el controlador de Oracle dentro de Squirrel SQL Client.

### Paso 6: Agregar el Archivo `ojdbc.jar`
- Cambie a la pestaña **Extra Class Path** dentro del cuadro de diálogo "Add Driver".
- Haga clic en el botón **Add**.
- Navegue hasta la ubicación del archivo `ojdbc.jar` en su sistema, selecciónelo y confirme para agregarlo al classpath del controlador.

### Paso 7: Especificar la Clase del Controlador Java
- En el campo "Class Name", ingrese la clase del controlador Java: **oracle.jdbc.OracleDriver**. Esto le indica a Squirrel SQL Client qué clase usar del archivo `ojdbc.jar` para manejar las conexiones a la base de datos Oracle.

### Paso 8: Proporcionar una URL de Ejemplo
- Opcionalmente, puede especificar un formato de URL de ejemplo para conectarse a una base de datos Oracle:
  - **Para conectarse vía SID**: `jdbc:oracle:thin:@HOST[:PORT]:DB`
  - **Para conectarse vía nombre de servicio**: `jdbc:oracle:thin:@//HOST[:PORT]/DB`
- Reemplace `HOST`, `PORT` y `DB` con valores reales cuando configure una conexión más adelante (en la configuración del alias).

### Paso 9: Guardar la Configuración del Controlador
- Haga clic en **OK** para guardar la configuración del controlador y cerrar el cuadro de diálogo "Add Driver". El "Oracle Thin Driver" ahora debería aparecer en la pestaña Drivers con una marca de verificación verde, lo que indica que está configurado correctamente.

### Paso 10: Crear un Alias para su Base de Datos
- Cambie a la pestaña **Aliases** en el lado izquierdo de Squirrel SQL Client.
- Haga clic en el botón **"+"** para abrir el cuadro de diálogo "Add Alias".

### Paso 11: Configurar el Alias
- En el cuadro de diálogo "Add Alias":
  - **Name**: Ingrese un nombre para esta conexión (por ejemplo, "Mi BD Oracle").
  - **Driver**: Seleccione **Oracle Thin Driver** del menú desplegable.
  - **URL**: Ingrese la URL de conexión para su base de datos Oracle específica:
    - Vía SID: `jdbc:oracle:thin:@HOST[:PORT]:DB`
    - Vía nombre de servicio: `jdbc:oracle:thin:@//HOST[:PORT]/DB`
    - Reemplace `HOST` (por ejemplo, localhost o dirección IP), `PORT` (el valor predeterminado es 1521) y `DB` (SID o nombre de servicio) con los detalles de su base de datos.
  - **Username**: Ingrese el nombre de usuario de la base de datos.
  - **Password**: Ingrese la contraseña de la base de datos.

### Paso 12: Probar la Conexión
- Haga clic en el botón **Test** en el cuadro de diálogo "Add Alias" para verificar que Squirrel SQL Client puede conectarse a su base de datos Oracle utilizando los detalles proporcionados. Si es exitoso, verá un mensaje de confirmación.

### Paso 13: Guardar el Alias
- Si la prueba de conexión es exitosa, haga clic en **OK** para guardar el alias. El nuevo alias ahora aparecerá en la pestaña Aliases.

### Paso 14: Conectarse a la Base de Datos
- En la pestaña Aliases, seleccione su alias recién creado (por ejemplo, "Mi BD Oracle").
- Haga clic en el botón **Connect** para establecer una conexión a su base de datos Oracle. Una vez conectado, puede comenzar a consultar su base de datos usando Squirrel SQL Client.

### Resumen de Información Clave
- **Archivo Requerido**: `ojdbc.jar`
- **Clase del Controlador Java**: `oracle.jdbc.OracleDriver`
- **Formatos de URL**:
  - SID: `jdbc:oracle:thin:@HOST[:PORT]:DB`
  - Nombre de Servicio: `jdbc:oracle:thin:@//HOST[:PORT]/DB`

Siguiendo estos pasos, habrá agregado exitosamente el controlador JDBC de Oracle a Squirrel SQL Client y configurado una conexión a su base de datos Oracle. Asegúrese de que todos los detalles (ruta del archivo, URL, credenciales) sean precisos para evitar problemas de conexión.
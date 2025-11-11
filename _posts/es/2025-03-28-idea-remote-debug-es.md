---
audio: false
generated: true
lang: es
layout: post
title: Depuración remota integrada de IntelliJ IDEA
translated: true
type: note
---

Para conectar IntelliJ IDEA al puerto de depuración de un servidor WebSphere Liberty que has iniciado con `server debug default`, sin usar el plugin de WebSphere Liberty, puedes aprovechar la función de depuración remota integrada de IntelliJ IDEA. Este enfoque funciona porque WebSphere Liberty, cuando se inicia en modo de depuración, expone un puerto de depuración (normalmente 7777 por defecto) al que cualquier depurador de JVM, incluido IntelliJ IDEA, puede conectarse. A continuación se detallan los pasos para lograrlo:

---

### Paso 1: Iniciar el Servidor WebSphere Liberty en Modo Depuración
Cuando ejecutas `server debug default` (asumiendo que "default" es el nombre de tu servidor; sustitúyelo por el nombre real de tu servidor si es diferente), WebSphere Liberty se inicia con la depuración habilitada. Por defecto, este comando configura el servidor para escuchar conexiones de depuración en el puerto **7777**.

- **Comando**:
  ```bash
  server debug default
  ```
- **Qué hace**: Esto inicia el servidor "default" en modo de depuración, habilitando automáticamente las opciones de depuración de JVM (ej., `-Xdebug -Xrunjdwp:transport=dt_socket,server=y,suspend=n,address=7777`).
- **Verificación**: Después de ejecutar el comando, revisa la salida de la consola del servidor o los registros (ej., `messages.log`) para confirmar que el servidor está escuchando en el puerto de depuración. Busca un mensaje que indique el puerto de depuración (normalmente 7777 a menos que esté sobrescrito o no esté disponible).

---

### Paso 2: Confirmar el Puerto de Depuración
El puerto de depuración por defecto para WebSphere Liberty es **7777**. Sin embargo, si este puerto está en uso o ha sido personalizado:
- Revisa la salida de la consola después de iniciar el servidor. Podría decir algo como "Listening for debugger connections on port 7777."
- Si el puerto es diferente (ej., se asignó un puerto aleatorio debido a un conflicto), anota el número de puerto real para usarlo en IntelliJ IDEA.

Para esta guía, asumiremos el puerto por defecto **7777** a menos que tu configuración indique lo contrario.

---

### Paso 3: Configurar la Depuración Remota en IntelliJ IDEA
La función de depuración remota de IntelliJ IDEA te permite conectarte a la JVM del servidor sin necesidad de un plugin específico de WebSphere. Así es como configurarlo:

1. **Abrir Configuraciones de Ejecución/Depuración**:
   - En IntelliJ IDEA, ve al menú superior y selecciona **Run > Edit Configurations**.

2. **Añadir una Nueva Configuración de Depuración Remota**:
   - Haz clic en el botón **+** (o "Add New Configuration") en la esquina superior izquierda.
   - De la lista, selecciona **Remote JVM Debug** (puede que solo diga "Remote" dependiendo de tu versión de IntelliJ).

3. **Establecer los Detalles de la Configuración**:
   - **Name**: Dale un nombre significativo, ej., "WebSphere Liberty Debug."
   - **Host**: Establécelo como `localhost` (asumiendo que el servidor se ejecuta en la misma máquina que IntelliJ IDEA; usa la dirección IP del servidor si es remoto).
   - **Port**: Establécelo como `7777` (o el puerto de depuración real si es diferente).
   - **Transport**: Asegúrate de que esté establecido en **Socket**.
   - **Debugger Mode**: Selecciona **Attach** (esto le dice a IntelliJ que se conecte a una JVM que ya se está ejecutando).
   - Deja el resto de configuraciones (como "Command line arguments for remote JVM") por defecto a menos que necesites opciones específicas de JVM.

4. **Guardar la Configuración**:
   - Haz clic en **Apply** y luego en **OK** para guardar.

---

### Paso 4: Iniciar la Depuración
Con el servidor ejecutándose en modo de depuración y la configuración establecida:
- Ve a **Run > Debug** (o haz clic en el icono de error) y selecciona tu nueva configuración (ej., "WebSphere Liberty Debug").
- IntelliJ IDEA intentará conectarse a la JVM del servidor en el host y puerto especificados.
- Si tiene éxito, verás un mensaje en la ventana de Debug como "Connected to the target VM, address: 'localhost:7777'."

---

### Paso 5: Depurar Tu Aplicación
- **Establecer Puntos de Interrupción**: En tu código fuente, haz clic en la canaleta junto a los números de línea para añadir puntos de interrupción donde quieras que se pause la ejecución.
- **Provocar la Ejecución**: Interactúa con tu aplicación (ej., envía una petición al servidor) para alcanzar los puntos de interrupción.
- **Depurar**: Una vez que se alcanza un punto de interrupción, usa las herramientas de depuración de IntelliJ (step over, step into, resume, etc.) para inspeccionar variables y controlar la ejecución.

---

### Notas Adicionales
- **Servidor Local vs. Remoto**: Si WebSphere Liberty se está ejecutando en una máquina diferente, reemplaza `localhost` con la dirección IP del servidor en la configuración de depuración remota. Asegúrate de que el puerto de depuración (ej., 7777) esté abierto y no esté bloqueado por un firewall.
- **Conflictos de Puerto**: Si el puerto 7777 no está disponible cuando el servidor se inicia, WebSphere Liberty podría elegir un puerto aleatorio. Revisa la salida del servidor para confirmar el puerto y actualiza la configuración de IntelliJ en consecuencia.
- **No Se Necesita Plugin**: Este método usa la función estándar de depuración remota de IntelliJ IDEA, por lo que no se requiere el plugin de WebSphere Liberty.

---

### Resumen
Al iniciar tu Servidor WebSphere Liberty con `server debug default` (lo que habilita la depuración en el puerto 7777 por defecto) y configurar una configuración de depuración remota en IntelliJ IDEA, puedes conectarte al puerto de depuración del servidor sin el plugin de WebSphere Liberty. Esto te brinda capacidades completas de depuración—puntos de interrupción, inspección de variables y ejecución paso a paso—directamente dentro de IntelliJ IDEA.

---

Ejecutar y depurar aplicaciones de WebSphere Liberty en IntelliJ IDEA sin el plugin dedicado Liberty Tools es posible configurando manualmente el runtime de Liberty y configurando IntelliJ IDEA para la depuración remota y la ejecución de herramientas externas. Este enfoque requiere algunos pasos manuales en comparación con usar el plugin integrado, pero proporciona la funcionalidad necesaria para desarrollar y solucionar problemas de tus aplicaciones Liberty.

Aquí tienes un desglose del proceso:

**1. Obtener e Instalar el Runtime de WebSphere Liberty:**

Dado que no tienes el plugin para gestionar el runtime por ti, necesitarás descargar e instalar el runtime de WebSphere Liberty manualmente. Puedes obtener el runtime desde el sitio web oficial de IBM o a través de otros métodos de distribución como Maven o Gradle si estás gestionando tu proyecto con esas herramientas.

Típicamente, la instalación manual implica descargar un archivo ZIP o JAR y extraerlo a un directorio en tu sistema. Este directorio será tu directorio de instalación de Liberty (`<LIBERTY_HOME>`).

**2. Configurar el Servidor Liberty para la Depuración:**

Para depurar tu aplicación, necesitas iniciar el servidor Liberty con la depuración habilitada. Esto se hace añadiendo opciones específicas de JVM cuando el servidor se inicia. Estas opciones le dicen a la Java Virtual Machine (JVM) que escuche una conexión de depurador en un puerto específico.

Localiza el archivo `jvm.options` en el directorio de configuración de tu servidor Liberty (`<LIBERTY_HOME>/usr/servers/<your_server_name>/`). Si este archivo no existe, puedes crearlo. Añade la siguiente línea al archivo `jvm.options`:

```
-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=5005
```

  * `-agentlib:jdwp`: Carga la biblioteca Java Debug Wire Protocol (JDWP).
  * `transport=dt_socket`: Especifica que el depurador se conectará usando un socket.
  * `server=y`: Indica que la JVM actuará como servidor, escuchando una conexión del depurador.
  * `suspend=n`: Especifica que la JVM no debe esperar a que el depurador se conecte antes de iniciar. Puedes cambiar esto a `suspend=y` si necesitas depurar código que se ejecuta durante el arranque del servidor.
  * `address=5005`: Establece el número de puerto al que se conectará el depurador. Puedes cambiarlo a cualquier puerto disponible.

**3. Configurar IntelliJ IDEA para Ejecutar Liberty:**

Puedes usar la configuración de "External Tools" de IntelliJ IDEA para iniciar tu servidor Liberty desde dentro del IDE.

  * Ve a `File` > `Settings` (o `IntelliJ IDEA` > `Preferences` en macOS).
  * Navega a `Tools` > `External Tools`.
  * Haz clic en el icono `+` para añadir una nueva herramienta externa.
  * Configura la herramienta con los siguientes detalles:
      * **Name:** Dale un nombre descriptivo, ej., "Start Liberty Server".
      * **Program:** Navega hasta el script del servidor Liberty. Esto será típicamente `<LIBERTY_HOME>/bin/server` para Linux/macOS o `<LIBERTY_HOME>\bin\server.bat` para Windows.
      * **Arguments:** Añade los argumentos para iniciar tu instancia de servidor específica. Esto suele ser `start <your_server_name>`, donde `<your_server_name>` es el nombre de tu directorio de servidor en `<LIBERTY_HOME>/usr/servers/`.
      * **Working directory:** Establécelo en `<LIBERTY_HOME>/bin`.

Ahora puedes iniciar tu servidor Liberty yendo a `Tools` > `External Tools` y seleccionando la herramienta que acabas de configurar.

**4. Configurar IntelliJ IDEA para la Depuración Remota:**

Para depurar tu aplicación ejecutándose en el servidor Liberty iniciado manualmente, usarás la configuración "Remote JVM Debug" de IntelliJ IDEA.

  * Ve a `Run` > `Edit Configurations`.
  * Haz clic en el icono `+` y selecciona `Remote JVM Debug`.
  * Configura los ajustes:
      * **Name:** Dale un nombre descriptivo, ej., "Debug Liberty Server".
      * **Debugger mode:** Selecciona `Attach to remote JVM`.
      * **Host:** Introduce `localhost` (o la dirección IP de la máquina que ejecuta Liberty si no está en tu máquina local).
      * **Port:** Introduce el número de puerto que configuraste en el archivo `jvm.options` (ej., `5005`).
      * **Use module classpath of:** Selecciona el módulo en tu proyecto de IntelliJ IDEA que contiene el código de tu aplicación Liberty. Esto ayuda a IntelliJ IDEA a mapear el código en ejecución con tus archivos fuente para la depuración.

**5. Ejecutar y Depurar:**

1.  Inicia el servidor Liberty usando la configuración de "External Tools" que creaste en IntelliJ IDEA.
2.  Espera a que el servidor se inicie e indique que está escuchando para el depurador en el puerto configurado (deberías ver un mensaje en la salida de la consola del servidor).
3.  Establece puntos de interrupción en el código de tu aplicación dentro de IntelliJ IDEA.
4.  Ve a `Run` > `Debug` y selecciona la configuración "Debug Liberty Server" que creaste.

IntelliJ IDEA intentará conectarse al servidor Liberty en ejecución en el puerto especificado. Una vez conectado, puedes usar todas las funciones de depuración de IntelliJ IDEA, como ejecutar paso a paso, inspeccionar variables y evaluar expresiones.

Siguiendo estos pasos, puedes ejecutar y depurar efectivamente tus aplicaciones WebSphere Liberty en IntelliJ IDEA sin depender del plugin dedicado Liberty Tools, dándote control directo sobre el ciclo de vida del servidor y el proceso de depuración.
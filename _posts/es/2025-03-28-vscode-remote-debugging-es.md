---
audio: false
generated: true
lang: es
layout: post
title: Depuración Remota de VSCode
translated: true
type: note
---

Para realizar depuración remota en Visual Studio Code (VSCode) para un servidor WebSphere Liberty ejecutándose en modo de depuración, puedes utilizar las funciones de depuración de Java integradas en VSCode. A continuación se detallan los pasos para configurar esto sin instalar ningún plugin específico para WebSphere Liberty, asumiendo que ya tienes instalado el **Java Extension Pack** estándar (que incluye el **Debugger for Java**).

---

### Paso 1: Iniciar el Servidor WebSphere Liberty en Modo de Depuración
1. Abre una terminal o símbolo del sistema.
2. Navega hasta tu directorio de instalación de WebSphere Liberty.
3. Ejecuta el siguiente comando para iniciar tu servidor en modo de depuración:
   ```
   server debug default
   ```
   - Reemplaza `default` con el nombre de tu servidor si es diferente.
4. El servidor se iniciará con la depuración habilitada, típicamente escuchando en el puerto **7777**.
5. Verifica la salida de la consola o los registros del servidor para un mensaje como:
   ```
   Listening for transport dt_socket at address: 7777
   ```
   - Esto confirma el puerto de depuración. Si es un puerto diferente (por ejemplo, debido a un conflicto), anota el número que se muestra.

---

### Paso 2: Configurar la Depuración Remota en VSCode
1. **Abre tu Proyecto en VSCode**:
   - Asegúrate de que tu proyecto Java (que contiene el código fuente desplegado en el servidor) esté abierto en VSCode. Esto permite que el depurador mapee los puntos de interrupción al código en ejecución.

2. **Accede a la Vista Ejecutar y Depurar**:
   - Haz clic en el icono **Run and Debug** en la barra lateral izquierda (un botón de reproducir con un error) o presiona `Ctrl+Shift+D` (Windows/Linux) o `Cmd+Shift+D` (Mac).

3. **Crea o Edita el Archivo `launch.json`**:
   - En la vista **Run and Debug**, haz clic en el **icono de engranaje** junto al menú desplegable de configuraciones.
   - Si se te solicita seleccionar un entorno, elige **Java**. Esto crea un archivo `launch.json` en la carpeta `.vscode` de tu espacio de trabajo.
   - Si el archivo ya existe, se abrirá para editar.

4. **Añade una Configuración de Depuración**:
   - En el archivo `launch.json`, asegúrate de que contenga una configuración para adjuntarse a la JVM remota. Aquí tienes un ejemplo:
     ```json
     {
         "version": "0.2.0",
         "configurations": [
             {
                 "type": "java",
                 "name": "Attach to WebSphere Liberty",
                 "request": "attach",
                 "hostName": "localhost",
                 "port": 7777
             }
         ]
     }
     ```
   - **Explicación de los Campos**:
     - `"type": "java"`: Especifica el depurador de Java.
     - `"name": "Attach to WebSphere Liberty"`: Un nombre descriptivo para esta configuración.
     - `"request": "attach"`: Indica que VSCode se adjuntará a un proceso JVM existente.
     - `"hostName": "localhost"`: El nombre de host de la máquina que ejecuta el servidor. Usa la dirección IP o el nombre de host del servidor si está en una máquina diferente.
     - `"port": 7777`: El puerto de depuración del Paso 1. Actualiza esto si el servidor usa un puerto diferente.

5. **Guarda el Archivo**:
   - Guarda el archivo `launch.json` después de añadir o editar la configuración.

---

### Paso 3: Iniciar la Sesión de Depuración
1. **Asegúrate de que el Servidor esté Ejecutándose**:
   - Verifica que el Servidor WebSphere Liberty aún esté ejecutándose en modo de depuración desde el Paso 1.

2. **Selecciona la Configuración**:
   - En la vista **Run and Debug**, selecciona **"Attach to WebSphere Liberty"** del menú desplegable en la parte superior.

3. **Lanza el Depurador**:
   - Haz clic en el **botón verde de reproducir** o presiona `F5`. VSCode se conectará al proceso JVM del servidor.

4. **Establece Puntos de Interrupción**:
   - Abre tus archivos fuente de Java en VSCode.
   - Haz clic en la canaleta (a la izquierda de los números de línea) para establecer puntos de interrupción donde quieras que se pause la ejecución.

5. **Interactúa con la Aplicación**:
   - Usa tu aplicación (por ejemplo, envía solicitudes HTTP) para activar las rutas de código con puntos de interrupción. Cuando se alcance un punto de interrupción, VSCode pausará la ejecución, permitiéndote inspeccionar variables, ejecutar paso a paso el código y depurar.

---

### Notas Adicionales
- **Servidor Local vs. Remoto**:
  - Si el servidor se ejecuta en una máquina diferente, reemplaza `"localhost"` con el nombre de host o la dirección IP del servidor en el archivo `launch.json`. Asegúrate de que el puerto de depuración sea accesible a través de la red (por ejemplo, que no esté bloqueado por un firewall).

- **Confirmación del Puerto de Depuración**:
  - Si no estás seguro del puerto, siempre verifica la salida del servidor después de ejecutar `server debug default`. Este indicará explícitamente el puerto en el que está escuchando.

- **Coincidencia del Código Fuente**:
  - El código fuente en VSCode debe coincidir con el código que se ejecuta en el servidor para que los puntos de interrupción funcionen correctamente. Asegúrate de que tu proyecto esté actualizado y compilado con información de depuración (lo predeterminado en la mayoría de las compilaciones de Java).

- **Comportamiento del Servidor**:
  - Con `server debug default`, el servidor se inicia inmediatamente (sin esperar a un depurador). Puedes adjuntar VSCode en cualquier momento mientras esté en ejecución.

- **Prerrequisitos**:
  - El **Java Extension Pack** (o al menos la extensión **Debugger for Java**) debe estar instalado en VSCode. Esta es una herramienta estándar para el desarrollo en Java y proporciona las capacidades de depuración necesarias.

---

Siguiendo estos pasos, puedes depurar efectivamente tu Servidor WebSphere Liberty de forma remota utilizando las funciones integradas de VSCode, sin necesidad de plugins adicionales específicos para WebSphere.
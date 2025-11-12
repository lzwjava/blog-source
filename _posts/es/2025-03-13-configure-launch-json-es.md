---
audio: false
generated: true
lang: es
layout: post
title: Configuración de launch.json para Spring Boot en VSCode
translated: true
type: note
---

Para configurar el archivo `launch.json` para un proyecto Maven Spring Boot en Visual Studio Code (VSCode), necesitas establecer una configuración de lanzamiento que permita a VSCode ejecutar y depurar tu aplicación utilizando sus extensiones de Java. A continuación, se presenta una guía paso a paso para ayudarte a lograr esto.

### Prerrequisitos
Antes de continuar, asegúrate de lo siguiente:
- Tienes el **Java Extension Pack** instalado en VSCode. Este paquete incluye extensiones esenciales como "Debugger for Java" y "Language Support for Java" de Red Hat, que brindan soporte para ejecutar y depurar aplicaciones Java, incluidos proyectos Spring Boot.
- Tu proyecto Spring Boot es un proyecto Maven con un archivo `pom.xml` válido.
- El proyecto tiene una clase principal anotada con `@SpringBootApplication`, que contiene el método `main` para iniciar la aplicación.

### Pasos para Configurar `launch.json`
1. **Localizar la Clase Principal**
   - En un proyecto típico de Spring Boot, la clase principal se encuentra en el directorio `src/main/java` y está anotada con `@SpringBootApplication`. Por ejemplo, podría llamarse `com.example.demo.DemoApplication`.
   - Abre tu proyecto en VSCode e identifica el nombre completo de esta clase (por ejemplo, `com.example.demo.DemoApplication`).

2. **Determinar el Nombre del Proyecto**
   - El nombre del proyecto en un proyecto Maven corresponde al `artifactId` definido en tu archivo `pom.xml`.
   - Abre tu archivo `pom.xml` y busca la etiqueta `<artifactId>`. Por ejemplo:
     ```xml
     <artifactId>demo</artifactId>
     ```
     En este caso, el nombre del proyecto sería `demo`.

3. **Abrir la Vista de Depuración**
   - En VSCode, haz clic en el icono **Debug** en la barra lateral izquierda (o presiona `Ctrl+Shift+D` / `Cmd+Shift+D` en Mac).
   - Haz clic en el icono de engranaje ⚙️ junto al menú desplegable "Run and Debug" para configurar los ajustes de lanzamiento. Si no existe un `launch.json`, VSCode te pedirá que crees uno.

4. **Crear o Editar `launch.json`**
   - Si se te solicita seleccionar un entorno, elige **Java**. Esto generará un archivo `launch.json` básico en la carpeta `.vscode` de tu proyecto.
   - Abre el archivo `launch.json`. Si ya existe, puedes editarlo directamente.

5. **Agregar una Configuración de Lanzamiento**
   - Agrega la siguiente configuración dentro del array `"configurations"` en `launch.json`. Reemplaza los marcadores de posición con los detalles de tu proyecto:
     ```json
     {
         "type": "java",
         "name": "Launch Spring Boot App",
         "request": "launch",
         "mainClass": "com.example.demo.DemoApplication",
         "projectName": "demo"
     }
     ```
     - **Explicación de los Campos:**
       - `"type": "java"`: Especifica que esta es una configuración de lanzamiento para Java.
       - `"name": "Launch Spring Boot App"`: Un nombre descriptivo para esta configuración, que aparecerá en el menú desplegable de depuración.
       - `"request": "launch"`: Indica que VSCode debe lanzar la aplicación (en lugar de adjuntarse a un proceso existente).
       - `"mainClass"`: El nombre completo de tu clase principal de Spring Boot (por ejemplo, `com.example.demo.DemoApplication`).
       - `"projectName"`: El `artifactId` de tu `pom.xml` (por ejemplo, `demo`), que ayuda a VSCode a localizar el proyecto en una configuración multi-módulo.

   - Aquí tienes un ejemplo de un archivo `launch.json` completo con esta configuración:
     ```json
     {
         "version": "0.2.0",
         "configurations": [
             {
                 "type": "java",
                 "name": "Launch Spring Boot App",
                 "request": "launch",
                 "mainClass": "com.example.demo.DemoApplication",
                 "projectName": "demo"
             }
         ]
     }
     ```

6. **Opcional: Agregar Argumentos VM o Argumentos del Programa**
   - Si tu aplicación requiere configuraciones adicionales (por ejemplo, activar un perfil de Spring), puedes agregarlas usando `"vmArgs"` o `"args"`:
     - Ejemplo con un perfil de Spring:
       ```json
       {
           "type": "java",
           "name": "Launch Spring Boot App with Profile",
           "request": "launch",
           "mainClass": "com.example.demo.DemoApplication",
           "projectName": "demo",
           "vmArgs": "-Dspring.profiles.active=dev"
       }
       ```
       Esto establece la propiedad `spring.profiles.active` en `dev`.
     - Ejemplo con argumentos del programa:
       ```json
       "args": ["arg1", "arg2"]
       ```

7. **Guardar y Ejecutar**
   - Guarda el archivo `launch.json`.
   - Regresa a la vista de Depuración, selecciona **"Launch Spring Boot App"** del menú desplegable y haz clic en el botón de reproducción verde (o presiona `F5`).
   - VSCode compilará y ejecutará tu aplicación Spring Boot usando Maven y la extensión de Java. Deberías ver los registros de inicio de Spring Boot en la Consola de Depuración.

### Verificar la Configuración
- Si tu aplicación Spring Boot es una aplicación web, abre un navegador y ve a `http://localhost:8080` (o al puerto especificado en tu archivo `application.properties` o `application.yml`) para confirmar que se está ejecutando.
- También puedes establecer puntos de interrupción en tu código y usar los controles de depuración (pausar, pasar por paso, etc.) para depurar tu aplicación.

### Notas
- Las extensiones de Java en VSCode manejan automáticamente el classpath y el proceso de compilación basándose en tu `pom.xml`, por lo que normalmente no necesitas ejecutar `mvn clean install` manualmente de antemano.
- Si tu proyecto es parte de una configuración Maven multi-módulo, asegúrate de que `projectName` coincida con el `artifactId` del módulo correcto.
- Para configuraciones avanzadas (por ejemplo, directorios de trabajo personalizados o tareas previas al lanzamiento), consulta la [documentación de depuración de Java para VSCode](https://code.visualstudio.com/docs/java/java-debugging).

¡Con esta configuración, tu archivo `launch.json` debería estar correctamente configurado para ejecutar y depurar tu proyecto Maven Spring Boot en VSCode!
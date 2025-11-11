---
audio: false
generated: true
lang: es
layout: post
title: Depuración de Aplicaciones Spring Boot en Visual Studio Code
translated: true
type: note
---

Para depurar un proyecto Maven Spring Boot en Visual Studio Code (VSCode), puedes seguir estos sencillos pasos para configurar y ejecutar tu aplicación en modo de depuración. Esta guía asume que tienes un proyecto básico de Maven Spring Boot con un archivo `pom.xml` y una clase principal anotada con `@SpringBootApplication`. Así es cómo se hace:

### Paso 1: Instalar las Extensiones Necesarias
Antes de comenzar, asegúrate de que VSCode esté equipado con las extensiones requeridas para el desarrollo con Java y Spring Boot:
- **Java Extension Pack**: Esto incluye herramientas esenciales como Language Support for Java by Red Hat, que proporciona capacidades de depuración, junto con otras utilidades para el desarrollo en Java.
- **Spring Boot Extension Pack**: Este paquete mejora el desarrollo con Spring Boot con características como el Spring Boot Dashboard, Spring Boot Tools y más.

Para instalarlas:
1. Abre VSCode.
2. Ve a la vista de Extensiones (`Ctrl+Shift+X` o `Cmd+Shift+X` en macOS).
3. Busca "Java Extension Pack" y "Spring Boot Extension Pack", luego haz clic en **Instalar** para cada una.

### Paso 2: Abrir tu Proyecto Maven Spring Boot
- Inicia VSCode y abre la carpeta de tu proyecto seleccionando **Archivo > Abrir carpeta** y eligiendo el directorio que contiene tu archivo `pom.xml`.
- VSCode detectará el `pom.xml`, y el Java Extension Pack indexará automáticamente el proyecto y resolverá las dependencias. Esto puede tomar un momento, así que espera hasta que el proceso se complete (verás el progreso en la barra de estado inferior derecha).

### Paso 3: Crear o Editar el Archivo `launch.json`
Para configurar la depuración, necesitas configurar un archivo `launch.json` en VSCode:
1. Abre la vista **Ejecutar y depurar** haciendo clic en el icono del bicho y el play en la barra lateral o presionando `Ctrl+Shift+D`.
2. Si no existe ninguna configuración de depuración, haz clic en **"crear un archivo launch.json"**. Si ya existe una, haz clic en el icono de engranaje para editarla.
3. Cuando se te solicite, selecciona **Java** como el entorno. VSCode generará un archivo `launch.json` por defecto en una carpeta `.vscode` dentro de tu proyecto.
4. Añade o modifica una configuración de depuración para tu aplicación Spring Boot. Aquí tienes un ejemplo de configuración:

    ```json
    {
        "type": "java",
        "name": "Depurar Spring Boot",
        "request": "launch",
        "mainClass": "com.example.demo.DemoApplication",
        "projectName": "demo"
    }
    ```

    - Reemplaza `"com.example.demo.DemoApplication"` con el nombre completo de tu clase principal (por ejemplo, `com.yourcompany.yourapp.YourApplication`).
    - Reemplaza `"demo"` con el nombre de tu proyecto, típicamente el `<artifactId>` de tu `pom.xml`.

5. Guarda el archivo `launch.json`.

#### Opcional: Añadir Argumentos
Si tu aplicación requiere argumentos específicos (por ejemplo, perfiles de Spring), puedes incluirlos:
```json
{
    "type": "java",
    "name": "Depurar Spring Boot",
    "request": "launch",
    "mainClass": "com.example.demo.DemoApplication",
    "projectName": "demo",
    "args": "--spring.profiles.active=dev"
}
```

### Paso 4: Iniciar la Depuración
- En la vista **Ejecutar y depurar**, selecciona **"Depurar Spring Boot"** del menú desplegable en la parte superior.
- Haz clic en el botón verde de play (o presiona `F5`) para lanzar la aplicación en modo de depuración.
- VSCode compilará el proyecto usando Maven, iniciará la aplicación Spring Boot y adjuntará el depurador automáticamente.

### Paso 5: Establecer Puntos de Interrupción y Depurar
- Abre un archivo Java en tu proyecto (por ejemplo, una clase controladora o de servicio).
- Establece puntos de interrupción haciendo clic en la canaleta a la izquierda de los números de línea, donde aparecerá un punto rojo.
- Interactúa con tu aplicación (por ejemplo, mediante un navegador o un cliente de API). Cuando la ejecución llegue a un punto de interrupción, VSCode se pausará, permitiéndote:
  - Inspeccionar variables en el panel **Variables**.
  - Ejecutar paso a paso el código usando controles como **Paso por paso** (`F10`), **Paso a paso por instrucciones** (`F11`) o **Continuar** (`F5`).
  - Ver la pila de llamadas y más en la barra lateral de depuración.

### Métodos Alternativos
Si bien el método `launch.json` es recomendado por su flexibilidad, también puedes depurar usando:
- **Vista Maven**:
  1. Abre la vista Maven en la barra lateral (busca el icono "M" o habilítala a través de Extensiones).
  2. Expande tu proyecto, navega a `spring-boot` bajo Plugins, haz clic derecho en `spring-boot:run` y selecciona **Depurar**.
  3. La aplicación se iniciará y el depurador se adjuntará.
- **Spring Boot Dashboard**:
  1. Abre el Spring Boot Dashboard (usualmente en la vista del Explorador o a través de la paleta de comandos: `Spring Boot Dashboard`).
  2. Localiza tu aplicación, haz clic derecho sobre ella y selecciona **Depurar** (si está disponible).

### Prerrequisitos y Notas
- Asegúrate de que **Maven** esté instalado en tu sistema y sea accesible mediante la línea de comandos, o confía en el Maven integrado de VSCode (configurado a través de los ajustes si es necesario).
- Verifica que tu proyecto se compile exitosamente (`mvn clean install`) para evitar errores en tiempo de ejecución durante la depuración.
- Usa una versión de Java compatible según lo especificado en tu `pom.xml` (por ejemplo, a través de `<java.version>`).

Siguiendo estos pasos, puedes depurar efectivamente tu proyecto Maven Spring Boot en VSCode, aprovechando sus potentes herramientas de depuración para identificar y resolver problemas en tu código.
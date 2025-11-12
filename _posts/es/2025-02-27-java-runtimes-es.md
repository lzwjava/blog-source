---
audio: false
generated: true
lang: es
layout: post
title: Entornos de Ejecución de Java en Visual Studio Code
translated: true
type: note
---

Para usar `java.configuration.runtimes` en la configuración de Visual Studio Code (VS Code), necesitas configurarlo en tu archivo `settings.json`. Esta configuración te permite especificar múltiples versiones del Java Development Kit (JDK) que VS Code puede usar para tus proyectos Java. Es especialmente útil cuando trabajas con diferentes proyectos que requieren versiones específicas de Java. Aquí tienes una guía paso a paso para configurarlo:

### Pasos para Configurar `java.configuration.runtimes`

1. **Abrir la Configuración de VS Code**:
   - En Windows/Linux: Ve a `Archivo > Preferencias > Configuración` o presiona `Ctrl + ,`.
   - En macOS: Ve a `Code > Preferencias > Configuración` o presiona `Cmd + ,`.

2. **Acceder al Archivo JSON de Configuración**:
   - En la interfaz de usuario de Configuración, busca `java.configuration.runtimes`.
   - Verás una opción como "Java: Configuration: Runtimes". Haz clic en "Edit in settings.json" (generalmente un enlace debajo de la descripción de la configuración) para abrir el archivo `settings.json`.

3. **Editar `settings.json`**:
   - En el archivo `settings.json`, añade o modifica el array `java.configuration.runtimes`. Este array contiene objetos, cada uno representando una versión de JDK que quieres que VS Code reconozca.
   - Cada objeto típicamente incluye:
     - `name`: El identificador de la versión de Java (ej., `JavaSE-1.8`, `JavaSE-11`, `JavaSE-17`).
     - `path`: La ruta absoluta al directorio de instalación del JDK en tu sistema.
     - `default` (opcional): Establécelo en `true` para que este sea el JDK predeterminado para carpetas no gestionadas (proyectos sin herramientas de build como Maven o Gradle).

   Aquí tienes un ejemplo de configuración:

   ```json
   {
       "java.configuration.runtimes": [
           {
               "name": "JavaSE-1.8",
               "path": "C:/Program Files/Java/jdk1.8.0_351",
               "default": true
           },
           {
               "name": "JavaSE-11",
               "path": "C:/Program Files/Java/jdk-11.0.15"
           },
           {
               "name": "JavaSE-17",
               "path": "C:/Program Files/Java/jdk-17.0.6"
           }
       ]
   }
   ```

4. **Verificar las Rutas del JDK**:
   - Asegúrate de que la `path` apunte al directorio raíz de tu instalación de JDK (ej., donde está la carpeta `bin` que contiene `java.exe` o `java`).
   - En Windows, usa barras inclinadas (`/`) o escapa las barras invertidas (`\\`) en la ruta.
   - En macOS/Linux, usa la ruta apropiada del sistema de archivos (ej., `/usr/lib/jvm/java-17-openjdk`).

5. **Guardar y Recargar**:
   - Guarda el archivo `settings.json`.
   - Reinicia VS Code o recarga la ventana (`Ctrl + R` o `Cmd + R`) para aplicar los cambios.

6. **Comprobar la Configuración**:
   - Abre la Paleta de Comandos (`Ctrl + Shift + P` o `Cmd + Shift + P`) y ejecuta el comando `Java: Configure Java Runtime`.
   - Esto abre una vista que muestra los JDKs disponibles para tus proyectos. Verifica que tus runtimes configurados aparezcan en la pestaña "Project JDKs".

### Cómo Funciona
- **Carpetas No Gestionadas**: Para proyectos sin herramientas de build (ej., archivos Java simples), VS Code usa el JDK `default` especificado en `java.configuration.runtimes`.
- **Proyectos Gestionados (Maven/Gradle)**: Para proyectos con herramientas de build, la versión de JDK la determina la configuración del build (ej., `pom.xml` o `build.gradle`), pero VS Code seguirá reconociendo los runtimes listados aquí para compatibilidad.
- **Language Server**: El Java Language Server (parte de las extensiones de Java) requiere JDK 17+ para ejecutarse. Puedes especificar esto por separado con `java.jdt.ls.java.home` si es necesario (ej., `"java.jdt.ls.java.home": "C:/Program Files/Java/jdk-17.0.6"`).

### Ejemplo con Múltiples JDKs
Si estás en un Mac y tienes JDK 8 y 17 instalados via Homebrew, tu configuración podría verse así:

```json
{
    "java.configuration.runtimes": [
        {
            "name": "JavaSE-1.8",
            "path": "/Library/Java/JavaVirtualMachines/jdk1.8.0_351.jdk/Contents/Home",
            "default": true
        },
        {
            "name": "JavaSE-17",
            "path": "/Library/Java/JavaVirtualMachines/jdk-17.0.6.jdk/Contents/Home"
        }
    ]
}
```

### Consejos
- Usa el formato correcto para `name` (`JavaSE-<versión>`), que coincida con la versión de Java (ej., `JavaSE-11` para Java 11).
- Si solo tienes un JDK, aún puedes listarlo para asegurarte de que VS Code lo use explícitamente.
- Para encontrar la ruta de tu JDK, ejecuta `java -version` en una terminal y verifica el directorio de instalación (ej., via `where java` en Windows o `which java` en sistemas tipo Unix, luego retrocede hasta la raíz del JDK).

¡Esta configuración te da la flexibilidad de trabajar con múltiples versiones de Java en VS Code sin problemas! Avísame si necesitas ayuda para encontrar las rutas de tu JDK o para resolver problemas.
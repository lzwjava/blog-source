---
audio: false
generated: true
lang: es
layout: post
title: Complemento Liberty Maven
translated: true
type: note
---

Para lograr tu objetivo de ejecutar un script en IntelliJ IDEA en Windows que gestione rápidamente tu servidor Liberty y construya tu programa, mientras te aseguras de que el servidor esté detenido antes de reemplazar el archivo EAR, te recomiendo usar el **Liberty Maven Plugin**. Este enfoque es sencillo, se integra bien con tu proceso de construcción con Maven y evita los problemas que has encontrado con el formato de comandos y los archivos por lotes.

Aquí te explicamos cómo configurarlo:

---

### Solución: Usar el Liberty Maven Plugin

#### Paso 1: Añadir el Liberty Maven Plugin a tu `pom.xml`
El Liberty Maven Plugin te permite controlar el servidor Liberty (iniciar, detener, desplegar, etc.) directamente desde Maven, lo que elimina la necesidad de scripts complejos o archivos por lotes.

- Abre el archivo `pom.xml` de tu proyecto.
- Añade la siguiente configuración del plugin dentro de la sección `<build>`:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>io.openliberty.tools</groupId>
            <artifactId>liberty-maven-plugin</artifactId>
            <version>3.3.4</version>
            <configuration>
                <serverName>default</serverName>
                <installDirectory>C:\ruta\a\liberty</installDirectory>
            </configuration>
        </plugin>
    </plugins>
</build>
```

- **Reemplaza** `C:\ruta\a\liberty` con la ruta real a tu directorio de instalación de Liberty (por ejemplo, `C:\Program Files\IBM\WebSphere\Liberty`).
- El `<serverName>default</serverName>` coincide con tu uso de `default` en los comandos `server start default` y `server stop default`.

#### Paso 2: Crear una configuración de ejecución de Maven en IntelliJ IDEA
En lugar de usar un script o un archivo por lotes, puedes configurar IntelliJ IDEA para ejecutar una secuencia de objetivos de Maven que detengan el servidor, construyan tu proyecto y vuelvan a iniciar el servidor.

- En IntelliJ IDEA, ve a **Ejecutar > Editar Configuraciones...**.
- Haz clic en el botón **+** y selecciona **Maven** de la lista.
- Configura la ejecución:
  - **Nombre:** Dale un nombre significativo, por ejemplo, `Ejecutar Liberty`.
  - **Directorio de trabajo:** Asegúrate de que esté establecido en el directorio de tu proyecto (normalmente se detecta automáticamente).
  - **Línea de comandos:** Introduce la siguiente secuencia de objetivos de Maven:
    ```
    liberty:stop package liberty:start
    ```
- Haz clic en **Aplicar** y luego en **Aceptar**.

#### Paso 3: Ejecutar la configuración
- Usa el botón **Ejecutar** (triángulo verde) en IntelliJ IDEA para ejecutar esta configuración.
- Esto hará lo siguiente:
  1. **Detener el servidor Liberty** (`liberty:stop`): Asegura que el servidor no se esté ejecutando cuando se reemplace el archivo EAR.
  2. **Construir tu proyecto** (`package`): Ejecuta `mvn package` para generar el archivo EAR.
  3. **Iniciar el servidor Liberty** (`liberty:start`): Reinicia el servidor con el archivo EAR actualizado.

---

### Por qué esto funciona para ti
- **Corrige problemas de formato de comandos:** Mencionaste que usar "Script text" en la configuración de ejecución divide `server start default` en argumentos separados (`server`, `start`, `default`). El enfoque con Maven evita esto por completo al usar objetivos de plugin bien definidos.
- **Evita la complejidad de los archivos por lotes:** Te resultó difícil hacer que un archivo `.bat` funcionara correctamente (por ejemplo, debido a rutas o configuraciones de entorno). El Liberty Maven Plugin maneja la gestión del servidor internamente, por lo que no necesitas depurar comandos o rutas de archivos por lotes.
- **Cumple con tu requisito:** Necesitas que el servidor se detenga al reemplazar el archivo EAR para evitar problemas de inicio. Esta solución detiene explícitamente el servidor antes de construir y lo inicia después, asegurando un proceso limpio.

---

### Alternativa: Usar un archivo por lotes (si lo prefieres)
Si prefieres seguir usando un archivo por lotes, aquí tienes un ejemplo funcional, aunque es menos recomendable debido a los problemas que has enfrentado:

1. Crea un archivo llamado `runLiberty.bat` en el directorio de tu proyecto con el siguiente contenido:

```bat
@echo off
set LIBERTY_BIN=C:\ruta\a\liberty\bin
set MAVEN_HOME=C:\ruta\a\maven
set PATH=%PATH%;%LIBERTY_BIN%;%MAVEN_HOME%\bin

"%LIBERTY_BIN%\server" stop default
mvn package
"%LIBERTY_BIN%\server" start default
```

- Reemplaza `C:\ruta\a\liberty` y `C:\ruta\a\maven` con las rutas reales a tus instalaciones de Liberty y Maven.

2. En IntelliJ IDEA:
   - Ve a **Ejecutar > Editar Configuraciones...**.
   - Haz clic en **+** y selecciona **Archivo por lotes**.
   - Establece la **Ruta al archivo por lotes** en la ubicación de `runLiberty.bat`.
   - Establece el **Directorio de trabajo** en el directorio de tu proyecto.
   - Haz clic en **Aplicar** y **Aceptar**.

3. Ejecútalo usando el botón **Ejecutar**.

Sin embargo, este método requiere que te asegures manualmente de que las rutas y las variables de entorno sean correctas, lo que te resultó difícil. El enfoque del plugin de Maven es más simple y confiable.

---

### Recomendación
Usa el método del **Liberty Maven Plugin** descrito anteriormente. Es:
- **Integrado:** Se vincula a tu proceso de construcción con Maven existente.
- **Sencillo:** No es necesario luchar con la sintaxis de los archivos por lotes o las rutas.
- **Confiable:** Maneja correctamente la detención e inicio del servidor, evitando problemas de reemplazo del EAR.

¡Esta configuración te permitirá ejecutar tu programa de forma rápida y consistente en IntelliJ IDEA en tu servidor Liberty!
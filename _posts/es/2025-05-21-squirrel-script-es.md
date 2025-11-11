---
audio: false
generated: true
lang: es
layout: post
title: Script de Lanzamiento de SQuirreL
translated: true
type: note
---

Este script por lotes se utiliza para lanzar SQuirreL SQL Client, una herramienta de administración de bases de datos basada en Java. A continuación se presenta una explicación exhaustiva del script, desglosando su propósito, estructura y funcionalidad paso a paso.

---

### **Descripción General**
El script está diseñado para:
1.  Configurar el entorno Java para ejecutar SQuirreL SQL Client.
2.  Verificar la compatibilidad de la versión de Java (requiere Java 1.6 o 1.7).
3.  Buscar actualizaciones de software y aplicarlas si están disponibles.
4.  Construir el classpath para SQuirreL y sus librerías.
5.  Lanzar la aplicación SQuirreL SQL Client con los parámetros apropiados.

El script está escrito para Windows (usa la extensión `.bat`) y utiliza el lenguaje de scripting por lotes del Símbolo del sistema de Windows.

---

### **Explicación Línea por Línea**

#### **1. `@echo off`**
-   **Propósito**: Desactiva el eco de comandos en la consola, haciendo la salida del script más limpia al mostrar solo la salida prevista (por ejemplo, mensajes de error o declaraciones `echo` específicas).
-   **Efecto**: Los comandos ejecutados en el script no se muestran a menos que se impriman explícitamente usando `echo`.

---

#### **2. `@rem IZPACK_JAVA is filtered in by the IzPack installer when this script is installed`**
-   **Propósito**: Un comentario (`@rem`) que indica que la variable `IZPACK_JAVA` es establecida por el instalador IzPack durante la instalación.
-   **Contexto**: IzPack es una herramienta utilizada para crear instaladores para aplicaciones Java. Establece dinámicamente la variable de entorno `JAVA_HOME` en el script para apuntar a la instalación de Java utilizada durante la configuración.

#### **3. `set IZPACK_JAVA=%JAVA_HOME`**
-   **Propósito**: Asigna el valor de la variable de entorno `JAVA_HOME` (establecida por IzPack) a la variable `IZPACK_JAVA`.
-   **Explicación**: Esto asegura que el script sepa dónde está ubicada la instalación de Java. `JAVA_HOME` típicamente apunta al directorio raíz de un Java Development Kit (JDK) o Java Runtime Environment (JRE).

---

#### **4. Lógica de Detección de Java**
```bat
@rem We detect the java executable to use according to the following algorithm:
@rem 1. If the one used by the IzPack installer is available then use that; otherwise
@rem 2. Use the java that is in the command path.
if exist "%IZPACK_JAVA%\bin\javaw.exe" (
  set LOCAL_JAVA=%IZPACK_JAVA%\bin\javaw.exe
) else (
  set LOCAL_JAVA=javaw.exe
)
```
-   **Propósito**: Determina qué ejecutable de Java usar para ejecutar SQuirreL SQL.
-   **Lógica**:
    1.  **Comprobar Java de IzPack**: El script verifica si `javaw.exe` existe en el directorio `bin` de la instalación de Java especificada por `IZPACK_JAVA` (es decir, `%IZPACK_JAVA%\bin\javaw.exe`).
        -   `javaw.exe` es un ejecutable de Java específico de Windows que ejecuta aplicaciones Java sin abrir una ventana de consola (a diferencia de `java.exe`).
        -   Si se encuentra, `LOCAL_JAVA` se establece en la ruta completa de `javaw.exe`.
    2.  **Respaldo a PATH**: Si `javaw.exe` no se encuentra en el directorio `IZPACK_JAVA`, el script recurre a usar `javaw.exe` desde la variable de entorno `PATH` del sistema.
-   **¿Por qué `javaw.exe`?**: Usar `javaw.exe` asegura que la aplicación se ejecute sin una ventana de comandos persistente, proporcionando una experiencia de usuario más limpia.

#### **5. `echo Using java: %LOCAL_JAVA%`**
-   **Propósito**: Imprime la ruta del ejecutable de Java que se está utilizando en la consola para fines de depuración o informativos.
-   **Ejemplo de Salida**: Si `LOCAL_JAVA` es `C:\Program Files\Java\jre1.6.0_45\bin\javaw.exe`, mostrará:
    ```
    Using java: C:\Program Files\Java\jre1.6.0_45\bin\javaw.exe
    ```

---

#### **6. Determinación del Directorio de Instalación de SQuirreL SQL**
```bat
set basedir=%~f0
:strip
set removed=%basedir:~-1%
set basedir=%basedir:~0,-1%
if NOT "%removed%"=="\" goto strip
set SQUIRREL_SQL_HOME=%basedir%
```
-   **Propósito**: Determina el directorio donde está instalado SQuirreL SQL (`SQUIRREL_SQL_HOME`).
-   **Explicación**:
    -   `%~f0`: Esto se expande a la ruta completa del script por lotes en sí (por ejemplo, `C:\Program Files\SQuirreL\squirrel-sql.bat`).
    -   **Bucle `:strip`**: El script elimina iterativamente el último carácter de `basedir` hasta que encuentra una barra invertida (`\`), eliminando efectivamente el nombre del archivo del script para obtener la ruta del directorio.
    -   **Resultado**: `SQUIRREL_SQL_HOME` se establece en el directorio que contiene el script (por ejemplo, `C:\Program Files\SQuirreL`).
-   **¿Por qué este enfoque?**: Esto asegura que el script pueda determinar dinámicamente su propio directorio de instalación, haciéndolo portable entre diferentes sistemas.

---

#### **7. Verificación de la Versión de Java**
```bat
"%LOCAL_JAVA%" -cp "%SQUIRREL_SQL_HOME%\lib\versioncheck.jar" JavaVersionChecker 1.6 1.7
if ErrorLevel 1 goto ExitForWrongJavaVersion
```
-   **Propósito**: Verifica que la versión de Java sea compatible con SQuirreL SQL (requiere Java 1.6 o 1.7).
-   **Explicación**:
    -   El script ejecuta la clase `JavaVersionChecker` desde `versioncheck.jar`, ubicada en el directorio `lib` de SQuirreL SQL.
    -   **`-cp`**: Especifica el classpath, apuntando a `versioncheck.jar`.
    -   **Argumentos**: `1.6 1.7` indica que la versión de Java debe ser 1.6 o 1.7.
    -   **Nota**: `versioncheck.jar` está compilado con compatibilidad Java 1.2.2, asegurando que pueda ejecutarse en JVMs más antiguos para realizar la verificación de versión.
    -   **Manejo de Errores**: Si la versión de Java es incompatible, `ErrorLevel` se establece en 1, y el script salta a la etiqueta `:ExitForWrongJavaVersion`, terminando la ejecución.
-   **¿Por qué esta verificación?**: SQuirreL SQL requiere versiones específicas de Java para funcionar correctamente, y esto evita que la aplicación se ejecute en JVMs no compatibles.

---

#### **8. Verificación de Actualizaciones de Software**
```bat
if not exist "%SQUIRREL_SQL_HOME%\update\changeList.xml" goto launchsquirrel
SET TMP_CP="%SQUIRREL_SQL_HOME%\update\downloads\core\squirrel-sql.jar"
if not exist %TMP_CP% goto launchsquirrel
dir /b "%SQUIRREL_SQL_HOME%\update\downloads\core\*.*" > %TEMP%\update-lib.tmp
FOR /F %%I IN (%TEMP%\update-lib.tmp) DO CALL "%SQUIRREL_SQL_HOME%\addpath.bat" "%SQUIRREL_SQL_HOME%\update\downloads\core\%%I"
SET UPDATE_CP=%TMP_CP%
SET UPDATE_PARMS=--log-config-file "%SQUIRREL_SQL_HOME%\update-log4j.properties" --squirrel-home "%SQUIRREL_SQL_HOME%" %1 %2 %3 %4 %5 %6 %7 %8 %9
"%LOCAL_JAVA%" -cp %UPDATE_CP% -Dlog4j.defaultInitOverride=true -Dprompt=true net.sourceforge.squirrel_sql.client.update.gui.installer.PreLaunchUpdateApplication %UPDATE_PARAMS%
```
-   **Propósito**: Comprueba y aplica actualizaciones de software antes de lanzar la aplicación principal.
-   **Explicación**:
    1.  **Comprobar Archivos de Actualización**:
        -   El script verifica si `changeList.xml` existe en el directorio `update`. Este archivo es creado por la función de actualización de software de SQuirreL para rastrear actualizaciones.
        -   Si `changeList.xml` no existe, el script omite el proceso de actualización y salta a `:launchsquirrel`.
        -   También comprueba la existencia del `squirrel-sql.jar` actualizado en el directorio `update\downloads\core`. Si no existe, el script salta a `:launchsquirrel`.
    2.  **Construir el Classpath de Actualización**:
        -   El comando `dir /b` lista todos los archivos en el directorio `update\downloads\core` y los escribe en un archivo temporal (`%TEMP%\update-lib.tmp`).
        -   El bucle `FOR /F` itera sobre los archivos en `update-lib.tmp` y llama a `addpath.bat` para añadir cada archivo al classpath almacenado en `TMP_CP`.
        -   `UPDATE_CP` se establece en el classpath, comenzando con `squirrel-sql.jar` desde el directorio de actualización.
    3.  **Establecer Parámetros de Actualización**:
        -   `UPDATE_PARMS` incluye:
            -   `--log-config-file`: Especifica el archivo de configuración de Log4j para el registro durante el proceso de actualización.
            -   `--squirrel-home`: Pasa el directorio de instalación de SQuirreL.
            -   `%1 %2 %3 ... %9`: Pasa cualquier argumento de línea de comandos proporcionado al script.
    4.  **Ejecutar la Aplicación de Actualización**:
        -   El script lanza `PreLaunchUpdateApplication` (una clase Java en `squirrel-sql.jar`) para aplicar las actualizaciones.
        -   **`-Dlog4j.defaultInitOverride=true`**: Anula la configuración predeterminada de Log4j.
        -   **`-Dprompt=true`**: Probablemente habilita mensajes interactivos durante el proceso de actualización.
-   **¿Por qué este paso?**: SQuirreL SQL soporta actualizaciones automáticas, y esta sección asegura que cualquier actualización descargada se aplique antes de lanzar la aplicación principal.

---

#### **9. Lanzar SQuirreL SQL**
```bat
:launchsquirrel
@rem build SQuirreL's classpath
set TMP_CP="%SQUIRREL_SQL_HOME%\squirrel-sql.jar"
dir /b "%SQUIRREL_SQL_HOME%\lib\*.*" > %TEMP%\squirrel-lib.tmp
FOR /F %%I IN (%TEMP%\squirrel-lib.tmp) DO CALL "%SQUIRREL_SQL_HOME%\addpath.bat" "%SQUIRREL_SQL_HOME%\lib\%%I"
SET SQUIRREL_CP=%TMP_CP%
echo "SQUIRREL_CP=%SQUIRREL_CP%"
```
-   **Propósito**: Construye el classpath para la aplicación principal de SQuirreL SQL y se prepara para lanzarla.
-   **Explicación**:
    1.  **Inicializar Classpath**:
        -   `TMP_CP` se inicializa con la ruta a `squirrel-sql.jar` en el directorio de instalación de SQuirreL.
    2.  **Añadir Jars de Librería**:
        -   El comando `dir /b` lista todos los archivos en el directorio `lib` y los escribe en `squirrel-lib.tmp`.
        -   El bucle `FOR /F` itera sobre los archivos y llama a `addpath.bat` para añadir cada archivo de librería (por ejemplo, archivos `.jar`) al classpath `TMP_CP`.
    3.  **Establecer Classpath Final**:
        -   `SQUIRREL_CP` se establece en el classpath completado.
    4.  **Salida de Depuración**:
        -   El script imprime el classpath final (`SQUIRREL_CP`) para fines de depuración.

---

#### **10. Establecer Parámetros de Lanzamiento**
```bat
SET TMP_PARMS=--log-config-file "%SQUIRREL_SQL_HOME%\log4j.properties" --squirrel-home "%SQUIRREL_SQL_HOME%" %1 %2 %3 %4 %5 %6 %7 %8 %9
```
-   **Propósito**: Define los parámetros que se pasarán a la aplicación SQuirreL SQL.
-   **Explicación**:
    -   `--log-config-file`: Especifica el archivo de configuración de Log4j para la aplicación principal.
    -   `--squirrel-home`: Pasa el directorio de instalación de SQuirreL.
    -   `%1 %2 ... %9`: Pasa cualquier argumento de línea de comandos proporcionado al script.

---

#### **11. Lanzar la Aplicación**
```bat
@rem -Dsun.java2d.noddraw=true prevents performance problems on Win32 systems.
start "SQuirreL SQL Client" /B "%LOCAL_JAVA%" -Xmx256m -Dsun.java2d.noddraw=true -cp %SQUIRREL_CP% -splash:"%SQUIRREL_SQL_HOME%/icons/splash.jpg" net.sourceforge.squirrel_sql.client.Main %TMP_PARMS%
```
-   **Propósito**: Lanza la aplicación SQuirreL SQL Client.
-   **Explicación**:
    -   **`start "SQuirreL SQL Client" /B`**: Ejecuta el comando en un nuevo proceso sin abrir una nueva ventana de consola (`/B` suprime la ventana).
    -   **`%LOCAL_JAVA%`**: Especifica el ejecutable de Java a usar.
    -   **`-Xmx256m`**: Establece el tamaño máximo del heap de Java en 256 MB para limitar el uso de memoria.
    -   **`-Dsun.java2d.noddraw=true`**: Desactiva DirectDraw para gráficos Java 2D para evitar problemas de rendimiento en sistemas Windows.
    -   **`-cp %SQUIRREL_CP%`**: Especifica el classpath para la aplicación.
    -   **`-splash:"%SQUIRREL_SQL_HOME%/icons/splash.jpg"`**: Muestra una pantalla de presentación (una imagen) cuando la aplicación inicia.
    -   **`net.sourceforge.squirrel_sql.client.Main`**: La clase principal de Java a ejecutar.
    -   **`%TMP_PARMS%`**: Pasa los parámetros definidos anteriormente.

---

#### **12. Salida por Versión de Java Incorrecta**
```bat
:ExitForWrongJavaVersion
```
-   **Propósito**: Una etiqueta utilizada como punto de salida si la verificación de la versión de Java falla.
-   **Explicación**: Si la versión de Java no es 1.6 o 1.7, el script salta aquí y termina sin lanzar la aplicación.

---

### **Componentes y Conceptos Clave**
1.  **Construcción del Classpath**:
    -   El script construye dinámicamente el classpath tanto para el proceso de actualización (`UPDATE_CP`) como para la aplicación principal (`SQUIRREL_CP`) incluyendo `squirrel-sql.jar` y todos los archivos `.jar` en los directorios `lib` o `update\downloads\core`.
    -   Se asume que el script `addpath.bat` (no mostrado) añade cada archivo a la variable del classpath.

2.  **Configuración de Log4j**:
    -   Log4j es un framework de registro utilizado por SQuirreL SQL. El script especifica archivos de configuración de Log4j separados para el proceso de actualización (`update-log4j.properties`) y la aplicación principal (`log4j.properties`).

3.  **Mecanismo de Actualización de Software**:
    -   SQuirreL SQL soporta actualizaciones automáticas, gestionadas por la clase `PreLaunchUpdateApplication`. El script comprueba la existencia de archivos de actualización y ejecuta el proceso de actualización si es necesario.

4.  **Compatibilidad de Versión de Java**:
    -   El script exige estrictamente compatibilidad con Java 1.6 o 1.7, probablemente debido a dependencias o características específicas de estas versiones.

5.  **Portabilidad**:
    -   El script está diseñado para ser portable determinando dinámicamente el directorio de instalación y la ubicación del ejecutable de Java.

---

### **Problemas Potenciales y Consideraciones**
1.  **Restricción de Versión de Java**:
    -   El script solo permite Java 1.6 o 1.7, que están obsoletas (publicadas en 2006 y 2011, respectivamente). Los sistemas modernos pueden tener versiones más nuevas de Java, haciendo que el script falle a menos que se instale un JRE más antiguo.
    -   **Solución alternativa**: Los usuarios pueden necesitar instalar un JRE compatible o modificar el script para soportar versiones más nuevas (si SQuirreL SQL es compatible).

2.  **Rutas Codificadas**:
    -   El script asume que ciertos archivos (por ejemplo, `squirrel-sql.jar`, `versioncheck.jar`, `addpath.bat`) existen en directorios específicos relativos a `SQUIRREL_SQL_HOME`. Si estos faltan o se mueven, el script fallará.

3.  **Específico de Windows**:
    -   El script usa comandos específicos de Windows (`dir /b`, `FOR /F`, `start /B`) y `javaw.exe`, haciéndolo incompatible con sistemas no Windows sin modificación.

4.  **Manejo de Errores**:
    -   El script maneja errores de versión de Java pero no proporciona mensajes de error detallados para otros fallos (por ejemplo, `squirrel-sql.jar` faltante o classpath inválido).

5.  **Límite de Memoria**:
    -   La bandera `-Xmx256m` limita la JVM a 256 MB de memoria, lo que puede ser insuficiente para bases de datos grandes o consultas complejas, potencialmente causando `OutOfMemoryError`.

---

### **Resumen**
Este script por lotes es un lanzador para SQuirreL SQL Client, realizando las siguientes tareas:
-   Detecta y configura el ejecutable de Java.
-   Verifica la compatibilidad de la versión de Java (1.6 o 1.7).
-   Comprueba y aplica actualizaciones de software si están disponibles.
-   Construye el classpath para la aplicación.
-   Lanza SQuirreL SQL con los parámetros apropiados, incluyendo una pantalla de presentación y configuraciones de memoria.

El script está bien estructurado para su propósito, pero está adaptado a un entorno específico (Windows, Java 1.6/1.7) y puede requerir actualizaciones para soportar sistemas modernos o versiones más nuevas de Java.

Si tienes más preguntas o necesitas ayuda para modificar el script (por ejemplo, para soportar versiones más nuevas de Java), ¡avísame!
---
audio: false
generated: true
lang: es
layout: post
title: Resolución de Problemas con el JDK de Eclipse
translated: true
type: note
---

Al iniciar Eclipse 4.6.3 haciendo clic en `eclipse.exe` y te encuentras con el error "Java was started but returned exit code" con una referencia a `Oracle\Java\javapath\javaw.exe`, significa que Eclipse está intentando usar una Java Virtual Machine (JVM) que es incompatible o está mal configurada. La ruta `Oracle\Java\javapath\javaw.exe` indica que Eclipse está usando por defecto una JVM definida en la variable de entorno PATH del sistema, que puede no ser adecuada para Eclipse 4.6.3. Para resolverlo, necesitas especificar el Java home correcto para Eclipse configurándolo para que use una JVM compatible. Así es cómo hacerlo:

### Solución Paso a Paso

1. **Comprender el Requisito**
   Eclipse 4.6.3 (Neon) requiere al menos Java 8 para ejecutarse correctamente. El error sugiere que la JVM actual (desde `Oracle\Java\javapath`) puede no cumplir con este requisito o tiene problemas de configuración. Deberás dirigir Eclipse a una instalación de Java compatible, como un JDK de Java 8.

2. **Localiza Tu Instalación de Java**
   Identifica dónde está instalada una versión compatible de Java (por ejemplo, JDK 1.8.0) en tu sistema. Las ubicaciones comunes en Windows incluyen:
   - `C:\Program Files\Java\jdk1.8.0_XXX` (para Java de 64-bit)
   - `C:\Program Files (x86)\Java\jdk1.8.0_XXX` (para Java de 32-bit)
   Reemplaza `XXX` con la versión de actualización específica (por ejemplo, `231` para JDK 1.8.0_231). Dentro de este directorio, el archivo `javaw.exe` se encuentra en el subdirectorio `bin` (por ejemplo, `C:\Program Files\Java\jdk1.8.0_XXX\bin\javaw.exe`).

   **Consejo**: Para confirmar la versión y la arquitectura, abre un símbolo del sistema, navega al directorio `bin` (por ejemplo, `cd C:\Program Files\Java\jdk1.8.0_XXX\bin`), y ejecuta:
   ```
   java -version
   ```
   Busca "64-Bit" o "32-Bit" en la salida para verificar la arquitectura. Asegúrate de que coincida con tu versión de Eclipse (probablemente 64-bit si se descargó recientemente).

3. **Encuentra el Archivo `eclipse.ini`**
   El archivo `eclipse.ini` es un archivo de configuración ubicado en el mismo directorio que `eclipse.exe`. Por ejemplo, si Eclipse está instalado en `C:\eclipse`, el archivo estará en `C:\eclipse\eclipse.ini`. Este archivo te permite especificar la JVM que debe usar Eclipse.

4. **Edita el Archivo `eclipse.ini`**
   Abre `eclipse.ini` en un editor de texto (por ejemplo, Notepad) con privilegios de administrador. Lo modificarás para incluir el argumento `-vm`, que le dice a Eclipse qué JVM usar. Sigue estos pasos:

   - **Revisa el Contenido Existente**: Busca un argumento `-vm`. Si ya está presente, le seguirá una ruta en la siguiente línea (por ejemplo, `-vm` seguido de `C:/ruta/ejemplo/bin/javaw.exe`). Si apunta al problemático `Oracle\Java\javapath\javaw.exe`, lo reemplazarás. Si no existe ningún argumento `-vm`, lo agregarás.
   - **Añade o Modifica el Argumento `-vm`**: Inserta las siguientes dos líneas antes de la sección `-vmargs` (si existe) o cerca del inicio del archivo después de los parámetros iniciales de inicio:
     ```
     -vm
     C:/Program Files/Java/jdk1.8.0_XXX/bin/javaw.exe
     ```
     - Usa barras inclinadas (`/`) en lugar de barras invertidas (`\`) para evitar problemas de análisis.
     - Reemplaza `C:/Program Files/Java/jdk1.8.0_XXX` con la ruta real a tu instalación de Java.
   - **Asegura una Colocación Adecuada**: El argumento `-vm` debe aparecer antes de la sección `-vmargs`, que normalmente comienza con `-vmargs` seguido de opciones de la JVM como `-Xms256m` o `-Xmx1024m`. Por ejemplo, tu `eclipse.ini` podría verse así después de la edición:
     ```
     -startup
     plugins/org.eclipse.equinox.launcher_1.3.201.v20161025-1711.jar
     --launcher.library
     plugins/org.eclipse.equinox.launcher.win32.win32.x86_64_1.1.401.v20161122-1740
     -vm
     C:/Program Files/Java/jdk1.8.0_XXX/bin/javaw.exe
     -vmargs
     -Dosgi.requiredJavaVersion=1.8
     -Xms256m
     -Xmx1024m
     ```
   - **Evita Espacios o Líneas en Blanco Extra**: Asegúrate de que no haya espacios innecesarios o líneas en blanco inmediatamente después de las líneas `-vm` o de la ruta, ya que esto puede hacer que Eclipse interprete mal la configuración.

5. **Guarda y Prueba**
   Guarda el archivo `eclipse.ini`, luego haz doble clic en `eclipse.exe` para iniciar Eclipse. Si está configurado correctamente, Eclipse debería iniciarse sin el error "Java was started but returned exit code".

### Notas Adicionales
- **Coincidencia de Arquitectura**: Asegúrate de que la arquitectura de la JVM (32-bit o 64-bit) coincida con tu instalación de Eclipse. Un Eclipse de 64-bit requiere una JVM de 64-bit, típicamente encontrada en `C:\Program Files\Java`, mientras que un Eclipse de 32-bit necesita una JVM de 32-bit de `C:\Program Files (x86)\Java`.
- **Verifica la Ruta**: Verifica dos veces que `javaw.exe` exista en la ubicación especificada. Si la ruta es incorrecta, Eclipse no podrá iniciarse.
- **Opción Alternativa**: Si esto no funciona, considera establecer la variable de entorno `JAVA_HOME` (por ejemplo, `C:\Program Files\Java\jdk1.8.0_XXX`) y actualizar el PATH del sistema para incluir `%JAVA_HOME%\bin`. Sin embargo, modificar `eclipse.ini` es el método preferido y más confiable para Eclipse.

Al editar el archivo `eclipse.ini` para incluir el argumento `-vm` con la ruta a un `javaw.exe` compatible, especificas efectivamente el Java home para Eclipse, asegurando que use la JVM correcta para iniciar.
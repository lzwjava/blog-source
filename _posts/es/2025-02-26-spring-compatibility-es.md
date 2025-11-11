---
audio: false
generated: true
lang: es
layout: post
title: Compatibilidad de Versiones de Java con Spring Boot
translated: true
type: note
---

### Comprender el Error

Cuando ejecutas `mvn spring-boot:run` con Spring Boot 3.4.3 y encuentras el error "class file has wrong version 61.0, should be 52.0", indica un problema de compatibilidad de versiones de Java. En Java, los archivos de clase tienen un número de versión que corresponde a la versión de Java con la que fueron compilados:

- **Versión 52.0** corresponde a Java 8.
- **Versión 61.0** corresponde a Java 17.

El error sugiere que los archivos de clase de tu aplicación Spring Boot fueron compilados con Java 17 (versión 61.0), pero la Java Virtual Machine (JVM) que intenta ejecutarlos espera archivos de clase compatibles con Java 8 (versión 52.0). Dado que la JVM de Java 8 no puede ejecutar archivos de clase compilados con Java 17 (porque Java es compatible con versiones anteriores pero no hacia adelante en este contexto), obtienes este error.

### Por Qué Ocurre Esto

Spring Boot 3.4.3 requiere **Java 17 o posterior** como su versión mínima soportada. Esto significa que tu proyecto debe ser compilado y ejecutado usando al menos Java 17. La discrepancia probablemente ocurre porque:

1. **Compilación**: Tu proyecto está configurado para compilar con Java 17, produciendo archivos de clase con versión 61.0. Esto normalmente se establece en tu `pom.xml` con el `maven-compiler-plugin` o la propiedad `<java.version>`.
2. **Tiempo de Ejecución (Runtime)**: Cuando ejecutas `mvn spring-boot:run`, el plugin Maven de Spring Boot inicia un nuevo proceso Java para ejecutar la aplicación. Sin embargo, el ejecutable `java` que utiliza proviene de una instalación de Java 8 (versión 52.0), que no puede manejar los archivos de clase compilados con Java 17.

### Pasos para Solucionar el Problema

Para resolverlo, necesitas asegurarte de que tanto el entorno de compilación como el de ejecución utilicen Java 17. Así es como solucionarlo:

#### 1. Verifica la Versión de Java de tu Proyecto
Primero, confirma que tu proyecto esté configurado para usar Java 17. En tu `pom.xml`, verifica lo siguiente:

```xml
<properties>
    <java.version>17</java.version>
</properties>
```

Esta propiedad le indica al `maven-compiler-plugin` que compile tu código con Java 17. Spring Boot 3.4.3 establece esto por defecto, pero es bueno verificarlo. Si falta o está configurado en una versión diferente (ej. 8), actualízalo a 17.

#### 2. Instala Java 17
Asegúrate de que Java 17 esté instalado en tu sistema. Puedes descargarlo desde:

- [Adoptium (Eclipse Temurin)](https://adoptium.net/)
- [Oracle JDK](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html) (si aceptas los términos de la licencia)

Para verificar si Java 17 está instalado, abre una terminal y ejecuta:

```bash
java -version
```

Si no muestra Java 17 (ej. `openjdk 17.x.x` o similar), instálalo y continúa.

#### 3. Actualiza tu Entorno para Usar Java 17
El plugin Maven de Spring Boot utiliza el ejecutable `java` de tu entorno, típicamente determinado por la variable de entorno `JAVA_HOME` o el comando `java` en el PATH de tu sistema. Si tu comando `java` actual apunta a Java 8, necesitas actualizarlo.

##### Opción A: Configurar JAVA_HOME y PATH
Establece tu variable de entorno `JAVA_HOME` para que apunte a la instalación de Java 17 y asegúrate de que el comando `java` en tu PATH lo utilice.

- **En Linux/Mac**:
  1. Encuentra tu directorio de instalación de Java 17 (ej. `/usr/lib/jvm/java-17-openjdk` o donde lo hayas instalado).
  2. Establece `JAVA_HOME` y actualiza `PATH` en tu terminal:
     ```bash
     export JAVA_HOME=/ruta/a/java-17
     export PATH=$JAVA_HOME/bin:$PATH
     ```
  3. Verifica:
     ```bash
     java -version
     ```
     Ahora debería mostrar Java 17.

  Para hacer esto permanente, agrega las líneas `export` a tu archivo de configuración del shell (ej. `~/.bashrc`, `~/.zshrc`).

- **En Windows**:
  1. Encuentra el directorio de instalación de Java 17 (ej. `C:\Program Files\Java\jdk-17`).
  2. Establece `JAVA_HOME`:
     - Abre la ventana de Propiedades del Sistema (busca "Variables de entorno" en el menú Inicio).
     - En "Variables del sistema", agrega o actualiza `JAVA_HOME` a `C:\Program Files\Java\jdk-17`.
  3. Actualiza `Path`:
     - En "Variables del sistema", edita `Path` y agrega `%JAVA_HOME%\bin` (asegúrate de que esté en la parte superior o elimina rutas anteriores de Java como Java 8).
  4. Abre un nuevo Símbolo del sistema y verifica:
     ```cmd
     java -version
     ```
     Debería mostrar Java 17.

##### Opción B: Usar una Versión Específica de Java para Maven
Si tienes múltiples versiones de Java instaladas y no quieres cambiar tu `JAVA_HOME` a nivel del sistema, puedes ejecutar Maven con una versión específica de Java:

- Antes de ejecutar `mvn spring-boot:run`, establece `JAVA_HOME` solo para ese comando:
  ```bash
  JAVA_HOME=/ruta/a/java-17 mvn spring-boot:run
  ```
  Esto asegura que el plugin Maven de Spring Boot use Java 17 sin alterar la configuración de tu sistema.

#### 4. Ejecuta la Aplicación Nuevamente
Con Java 17 correctamente configurado, ejecuta:

```bash
mvn spring-boot:run
```

El plugin ahora usará Java 17 para ejecutar tu aplicación, coincidiendo con la versión del archivo de clase compilado (61.0), y el error debería desaparecer.

### Verificaciones Adicionales
- **Versión de Java de Maven**: Ejecuta `mvn -version` para ver qué versión de Java usa Maven. Debería coincidir con tu `JAVA_HOME`. Si no es así, asegúrate de que tu PATH y `JAVA_HOME` estén configurados correctamente.
- **Dependencias**: Si el error persiste, una dependencia podría estar compilada con Java 17 mientras tu entorno de ejecución aún está mal configurado. Dado que Spring Boot 3.4.3 exige Java 17, asegurarte de que tu entorno de ejecución sea Java 17 debería resolver esto.

### ¿Por Qué No Java 8?
Spring Boot 3.4.3 no es compatible con Java 8. Si necesitas usar Java 8, tendrías que hacer un downgrade a una versión anterior de Spring Boot (ej. 2.x), pero no se recomienda a menos que tengas restricciones específicas. Dado que tus archivos de clase son versión 61.0, mantener Java 17 se alinea con los requisitos de Spring Boot 3.4.3.

### Resumen Final de la Solución
Para solucionar "class file has wrong version 61.0, should be 52.0" al ejecutar `mvn spring-boot:run` con Spring Boot 3.4.3:

1. Asegúrate de que `<java.version>17</java.version>` esté en tu `pom.xml`.
2. Instala Java 17 si aún no está presente.
3. Establece `JAVA_HOME` en el directorio de instalación de tu Java 17.
4. Actualiza tu PATH para que `java -version` muestre Java 17.
5. Ejecuta `mvn spring-boot:run` nuevamente.

Esto asegura que tu entorno de ejecución coincida con tus archivos de clase compilados con Java 17, resolviendo el problema de compatibilidad.
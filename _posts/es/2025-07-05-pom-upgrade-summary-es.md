---
audio: false
generated: true
lang: es
layout: post
title: Actualización de Dependencias y Complementos de Maven
translated: true
type: note
---

Aquí tienes una lista de las versiones en tu `pom.xml` que pueden ser actualizadas, junto con sus últimas versiones disponibles al 5 de julio de 2025:

**Dependencias:**

* `org.junit.jupiter:junit-jupiter-api`
    * Actual: `5.9.2`
    * Última Estable: `5.13.2` (Publicada el 24 de junio de 2025)
    * Última Preliminar: `6.0.0-M1` (Publicada el 27 de junio de 2025) - Considera si deseas utilizar una versión milestone.
* `org.junit.jupiter:junit-jupiter-engine`
    * Actual: `5.9.2`
    * Última Estable: `5.13.2` (Publicada el 24 de junio de 2025)
    * Última Preliminar: `6.0.0-M1` (Publicada el 27 de junio de 2025) - Considera si deseas utilizar una versión milestone.

**Plugins:**

* `org.apache.maven.plugins:maven-compiler-plugin`
    * Actual: `3.13.0`
    * Última: `3.14.0` (Publicada el 17 de febrero de 2025)
* `org.apache.maven.plugins:maven-jar-plugin`
    * Actual: `3.4.2`
    * Última: `3.4.2` (No se encontró una versión estable más nueva. Última publicación el 16 de junio de 2024, pero la fecha actual es el 5 de julio de 2025, por lo que aún está actualizada).
* `com.diffplug.spotless:spotless-maven-plugin`
    * Actual: `2.44.5`
    * Última: `2.44.5` (No se encontró una versión estable más nueva. Última publicación el 28 de mayo de 2025, por lo que aún está actualizada).
* `org.apache.maven.plugins:maven-checkstyle-plugin`
    * Actual: `3.6.0`
    * Última: `3.6.0` (No se encontró una versión estable más nueva. Última publicación el 22 de octubre de 2024, por lo que aún está actualizada).
    * **Nota:** La dependencia `checkstyle` dentro de la configuración del plugin checkstyle se puede actualizar:
        * Actual: `10.25.0`
        * Última: `10.26.1` (Publicada el 29 de junio de 2025)
* `org.apache.maven.plugins:maven-surefire-plugin`
    * Actual: `3.0.0-M7`
    * Última Estable: `3.5.3` (Publicada el 27 de marzo de 2025) - Este es un salto significativo desde una versión milestone.
* `org.codehaus.mojo:exec-maven-plugin`
    * Actual: `3.5.1`
    * Última: `3.5.1` (No se encontró una versión estable más nueva. Última publicación el 27 de mayo de 2025, por lo que aún está actualizada).

**Resumen de Actualizaciones:**

* **JUnit Jupiter API:** 5.9.2 -> 5.13.2 (o 6.0.0-M1)
* **JUnit Jupiter Engine:** 5.9.2 -> 5.13.2 (o 6.0.0-M1)
* **Maven Compiler Plugin:** 3.13.0 -> 3.14.0
* **Checkstyle (dependencia dentro del plugin):** 10.25.0 -> 10.26.1
* **Maven Surefire Plugin:** 3.0.0-M7 -> 3.5.3

**Consideraciones Importantes Antes de Actualizar:**

* **Cambios Rompedores:** Siempre revisa las notas de la versión para cada componente que planeas actualizar. Los incrementos de versión principal (como de JUnit 5 a 6, o Surefire 3.0.0-M7 a 3.5.3) pueden introducir cambios rompedores que requieran modificaciones en el código.
* **Compatibilidad:** Asegúrate de que las nuevas versiones sean compatibles con tu versión de Java (JDK 21 en tu caso) y con otras dependencias en tu proyecto.
* **Pruebas:** Después de actualizar, prueba exhaustivamente tu aplicación para asegurarte de que todo sigue funcionando como se espera.
---
audio: false
generated: true
lang: es
layout: post
title: Complemento Maven Surefire
translated: true
type: note
---

A continuación se presenta una explicación del **Maven Surefire Plugin**, un componente clave en proyectos basados en Maven para ejecutar pruebas unitarias durante el proceso de build. Esta explicación cubre su propósito, configuración, uso y opciones de personalización.

---

## ¿Qué es el Maven Surefire Plugin?

El **Maven Surefire Plugin** es un plugin de Apache Maven diseñado para ejecutar pruebas unitarias durante el ciclo de vida del build. Se integra perfectamente con la fase `test` de Maven y se activa automáticamente cuando ejecutas comandos como `mvn test`, `mvn package` o `mvn install`. El plugin soporta frameworks de prueba populares como JUnit (versiones 3, 4 y 5) y TestNG, y genera informes de prueba para ayudar a los desarrolladores a evaluar los resultados.

### Características Principales
- Ejecuta pruebas en un proceso JVM separado para aislarlas.
- Soporta múltiples frameworks de prueba (JUnit, TestNG, etc.).
- Genera informes de prueba en formatos como XML y texto plano.
- Ofrece flexibilidad para omitir pruebas, ejecutar pruebas específicas o personalizar la ejecución.

---

## Configuración Básica en `pom.xml`

El Surefire Plugin se incluye por defecto en el ciclo de vida de build de Maven, por lo que no necesitas configurarlo para un uso básico. Sin embargo, puedes declararlo explícitamente en tu archivo `pom.xml` para especificar una versión o personalizar su comportamiento.

### Configuración Mínima
Si no añades ninguna configuración, Maven usa el plugin con ajustes por defecto:
- Las pruebas se ubican en `src/test/java`.
- Los archivos de prueba siguen patrones de nomenclatura como `**/*Test.java`, `**/Test*.java` o `**/*Tests.java`.

### Declaración Explícita
Para personalizar el plugin o asegurar una versión específica, añádelo a la sección `<build><plugins>` de tu `pom.xml`. Aquí tienes un ejemplo:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-surefire-plugin</artifactId>
            <version>3.0.0-M5</version> <!-- Usa la última versión -->
        </plugin>
    </plugins>
</build>
```

---

## Ejecutar Pruebas con Surefire

El plugin está vinculado a la fase `test` del ciclo de vida de Maven. Así es cómo usarlo:

### Ejecutar Todas las Pruebas
Para ejecutar todas las pruebas unitarias, ejecuta:

```
mvn test
```

### Ejecutar Pruebas en un Build Mayor
Las pruebas se ejecutan automáticamente cuando usas comandos que incluyen la fase `test`, como:

```
mvn package
mvn install
```

### Omitir Pruebas
Puedes omitir la ejecución de pruebas usando flags de línea de comandos:
- **Omitir la ejecución de pruebas**: `-DskipTests`
  ```
  mvn package -DskipTests
  ```
- **Omitir la compilación y ejecución de pruebas**: `-Dmaven.test.skip=true`
  ```
  mvn package -Dmaven.test.skip=true
  ```

---

## Personalizar el Maven Surefire Plugin

Puedes adaptar el comportamiento del plugin añadiendo una sección `<configuration>` en el `pom.xml`. Aquí hay algunas personalizaciones comunes:

### Incluir o Excluir Pruebas Específicas
Especifica qué pruebas ejecutar u omitir usando patrones:
```xml
<configuration>
    <includes>
        <include>**/My*Test.java</include>
    </includes>
    <excludes>
        <exclude>**/SlowTest.java</exclude>
    </excludes>
</configuration>
```

### Ejecutar Pruebas en Paralelo
Acelera la ejecución ejecutando pruebas concurrentemente:
```xml
<configuration>
    <parallel>methods</parallel>
    <threadCount>2</threadCount>
</configuration>
```
*Nota*: Asegúrate de que tus pruebas sean thread-safe antes de activar esto.

### Pasar Propiedades del Sistema
Establece propiedades para la JVM de prueba:
```xml
<configuration>
    <systemPropertyVariables>
        <propertyName>propertyValue</propertyName>
    </systemPropertyVariables>
</configuration>
```

### Generar Informes
Por defecto, los informes se guardan en `target/surefire-reports`. Para un informe HTML, usa el `maven-surefire-report-plugin`:
```xml
<reporting>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-surefire-report-plugin</artifactId>
            <version>3.0.0-M5</version>
        </plugin>
    </plugins>
</reporting>
```
Ejecuta `mvn surefire-report:report` para generar el informe HTML.

---

## Manejar Fallos en las Pruebas

### Fallar el Build ante un Fallo en la Prueba
Por defecto, una prueba que falla hace que el build falle. Para ignorar los fallos y continuar:
```
mvn test -Dmaven.test.failure.ignore=true
```

### Reejecutar Pruebas Fallidas
Maneja pruebas inestables (flaky tests) reintentando los fallos:
```xml
<configuration>
    <rerunFailingTestsCount>2</rerunFailingTestsCount>
</configuration>
```
Esto reejecuta las pruebas fallidas hasta 2 veces.

---

## Usar Surefire con Frameworks de Prueba

El plugin soporta varios frameworks de prueba con una configuración mínima:

### JUnit 4
No se necesita configuración extra; Surefire detecta las pruebas de JUnit 4 automáticamente.

### JUnit 5
Añade la dependencia de JUnit 5:
```xml
<dependencies>
    <dependency>
        <groupId>org.junit.jupiter</groupId>
        <artifactId>junit-jupiter-engine</artifactId>
        <version>5.8.1</version>
        <scope>test</scope>
    </dependency>
</dependencies>
```
Usa la versión 2.22.0 o superior de Surefire para soporte completo.

### TestNG
Añade la dependencia de TestNG:
```xml
<dependencies>
    <dependency>
        <groupId>org.testng</groupId>
        <artifactId>testng</artifactId>
        <version>7.4.0</version>
        <scope>test</scope>
    </dependency>
</dependencies>
```
Surefire ejecutará automáticamente las pruebas de TestNG.

---

## Notas Clave

- **Ubicación de las Pruebas**: Las pruebas deben estar en `src/test/java`, con los recursos en `src/test/resources`.
- **Convenciones de Nomenclatura**: Los patrones por defecto incluyen `**/*Test.java`, `**/Test*.java`, etc., pero estos se pueden personalizar.
- **Versión del Plugin**: Usa una versión reciente (ej. 3.0.0-M5) para las últimas características y soporte de frameworks.

---

## Resumen

El **Maven Surefire Plugin** es esencial para ejecutar pruebas unitarias en proyectos Maven. Para usarlo:
1. Confía en su comportamiento por defecto o decláralo explícitamente en `pom.xml` para personalizarlo.
2. Ejecuta pruebas con `mvn test` o como parte de builds mayores como `mvn package`.
3. Personalízalo con opciones como patrones de inclusión/exclusión, ejecución en paralelo o propiedades del sistema.
4. Maneja los fallos omitiendo pruebas, ignorándolas o reejecutando las inestables.
5. Asegura la compatibilidad con tu framework de prueba (JUnit, TestNG) añadiendo las dependencias correctas.

¡Este plugin proporciona una forma robusta y flexible de gestionar las pruebas unitarias en tus proyectos Maven!
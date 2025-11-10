---
audio: false
generated: true
image: false
lang: es
layout: post
title: Guía de Pruebas Unitarias del Plugin Maven Surefire
translated: true
type: note
---

El **Maven Surefire Plugin** es el complemento que ejecuta sus pruebas unitarias durante la fase **test** del ciclo de vida de compilación de Maven. Es uno de los complementos de Maven más utilizados porque casi todos los proyectos necesitan pruebas automatizadas integradas en su compilación.

---

## Qué Es

* **Nombre**: `maven-surefire-plugin`
* **Propósito**: Ejecuta pruebas escritas con frameworks como JUnit (3, 4, 5), TestNG, etc.
* **Fase**: Vinculado a la fase `test` del ciclo de vida por defecto de Maven.
* **Salida**: Genera informes de pruebas (por defecto en `target/surefire-reports`).

---

## Cómo Funciona

1. Cuando ejecuta `mvn test` o `mvn package`, Maven invoca el plugin Surefire.
2. Escanea su directorio `src/test/java` en busca de clases de prueba.
3. Por defecto, busca archivos que coincidan con convenciones de nomenclatura como:

   * `*Test.java`
   * `Test*.java`
   * `*Tests.java`
   * `*TestCase.java`
4. Los ejecuta en un classloader aislado.
5. Escribe los resultados en `target/surefire-reports` (texto plano, XML y, a veces, HTML a través de plugins de reporting).

---

## Uso Básico

Puede configurarlo en su `pom.xml`:

```xml
<build>
  <plugins>
    <plugin>
      <groupId>org.apache.maven.plugins</groupId>
      <artifactId>maven-surefire-plugin</artifactId>
      <version>3.2.5</version> <!-- usar la última versión estable -->
    </plugin>
  </plugins>
</build>
```

Después de esto, simplemente ejecute:

```bash
mvn test
```

---

## Configuraciones Comunes

* **Patrones de inclusión/exclusión**:

```xml
<configuration>
  <includes>
    <include>**/*MyTest.java</include>
  </includes>
  <excludes>
    <exclude>**/IntegrationTest.java</exclude>
  </excludes>
</configuration>
```

* **Propiedades del sistema**:

```xml
<configuration>
  <systemPropertyVariables>
    <env>dev</env>
  </systemPropertyVariables>
</configuration>
```

* **Ejecución de pruebas en paralelo**:

```xml
<configuration>
  <forkCount>2</forkCount>
  <reuseForks>true</reuseForks>
  <parallel>classes</parallel>
</configuration>
```

Esto ejecuta las pruebas en múltiples procesos JVM o hilos.

---

## Cuándo Usarlo

* Siempre que desee integrar **pruebas unitarias** en su ciclo de vida de Maven.
* Para separar **pruebas unitarias (Surefire)** de **pruebas de integración (Failsafe plugin)**:

  * Surefire → pruebas unitarias (`mvn test`)
  * Failsafe → pruebas de integración (`mvn verify`)

---

✅ **En resumen**: `maven-surefire-plugin` es su complemento de referencia para la ejecución de pruebas unitarias en proyectos Maven. Lo configura en `pom.xml`, lo ejecuta con `mvn test` y revisa los informes en `target/surefire-reports`.

---

¿Quiere que también le explique la **diferencia entre Surefire y Failsafe** (dado que a menudo se confunden)?
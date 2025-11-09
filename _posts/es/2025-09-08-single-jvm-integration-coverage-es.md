---
audio: false
date: 2025-09-08
generated: true
image: false
lang: es
layout: post
title: Estrategia de Cobertura de Integración con una Única JVM
translated: true
type: note
---

No necesitas ejecutar Jetty dos veces ni crear un archivo `.exec` de JaCoCo separado por módulo. Un agente en la única JVM que sirve tu WAR puede registrar la cobertura para **todas las clases que esa JVM carga**—incluyendo `PlaygroundUtils`—en **un único archivo exec compartido**. Luego, cada módulo puede generar su propio informe apuntando a ese mismo archivo exec. Para un reactor grande (10+ módulos), esto escala de forma limpia.

A continuación, se presenta un plan concreto y mínimo, y las ediciones listas para usar en tu repositorio.

---

## La estrategia

1.  **Usar un único archivo exec de IT compartido a nivel del padre.**
    Iniciar Jetty **una vez**, instrumentado con JaCoCo, escribiendo en `../target/it-coverage/jacoco-it.exec` (una ruta de ámbito padre).
2.  **Ejecutar tus pruebas externas de Python una vez.**
    Estas acceden a la aplicación desplegada; el agente registra los impactos para todas las clases cargadas (web + librerías).
3.  **Generar informes por módulo**, cada módulo apunta al `jacoco-it.exec` compartido.
    `PlaygroundUtils` obtendrá un informe aunque no tenga pruebas—mapea el exec compartido a sus propios `target/classes`.
4.  (Opcional) **También generar un HTML agregado** en el padre con `report-aggregate`, o simplemente mantener los informes por módulo.

Solo cuando realmente tienes **múltiples JVMs** (por ejemplo, varios microservicios) necesitas múltiples archivos exec y un paso de `jacoco:merge`. Para tu compilación actual de JVM única (Jetty), mantén un solo exec.

---

## Ediciones exactas

### 1) `pom.xml` del Padre (PlaygroundLib)

Añade propiedades compartidas para que cada módulo pueda referenciar el mismo archivo exec:

```xml
<properties>
  <!-- ... tus versiones existentes ... -->
  <it.coverage.dir>${project.basedir}/target/it-coverage</it.coverage.dir>
  <jacoco.it.exec>${it.coverage.dir}/jacoco-it.exec</jacoco.it.exec>
  <!-- Activar/desactivar la generación del informe de IT por módulo -->
  <it.report.skip>false</it.report.skip>
</properties>
```

(Opcional) Si quieres un único HTML **agregado** en el padre, añade esta ejecución:

```xml
<build>
  <pluginManagement>
    <!-- mantén tus bloques existentes -->
  </pluginManagement>

  <plugins>
    <plugin>
      <groupId>org.jacoco</groupId>
      <artifactId>jacoco-maven-plugin</artifactId>
      <executions>
        <execution>
          <id>it-aggregate-report</id>
          <phase>verify</phase>
          <goals>
            <goal>report-aggregate</goal>
          </goals>
          <configuration>
            <!-- Usar el exec de IT compartido producido por la ejecución de Jetty -->
            <dataFile>${jacoco.it.exec}</dataFile>
            <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
          </configuration>
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

> Si tu versión de JaCoCo rechaza `<dataFile>` en `report-aggregate`, omite este bloque opcional y confía en los informes por módulo que se detallan a continuación. Siempre puedes añadir un pequeño módulo "coverage" agregador más tarde para ejecutar `merge` + `report`.

---

### 2) `PlaygroundWeb/pom.xml`

Dirige el agente de Jetty a la ruta exec a **nivel del padre** y habilita append:

```xml
<plugin>
  <groupId>org.eclipse.jetty</groupId>
  <artifactId>jetty-maven-plugin</artifactId>
  <executions>
    <execution>
      <id>start-jetty</id>
      <phase>pre-integration-test</phase>
      <goals><goal>start</goal></goals>
      <configuration>
        <daemon>true</daemon>
        <jvmArgs>
          -javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${project.parent.basedir}/target/it-coverage/jacoco-it.exec,append=true,includes=org.lzw.*
        </jvmArgs>
        <httpConnector>
          <port>8080</port>
          <host>127.0.0.1</host>
        </httpConnector>
        <webApp><contextPath>/</contextPath></webApp>
        <stopHost>127.0.0.1</stopHost>
        <stopPort>8081</stopPort>
        <stopKey>stop</stopKey>
      </configuration>
    </execution>

    <execution>
      <id>stop-jetty</id>
      <phase>post-integration-test</phase>
      <goals><goal>stop</goal></goals>
      <configuration>
        <stopHost>127.0.0.1</stopHost>
        <stopPort>8081</stopPort>
        <stopKey>stop</stopKey>
        <stopWait>15</stopWait>
      </configuration>
    </execution>
  </executions>
</plugin>
```

Actualiza tu `jacoco:report` en `PlaygroundWeb` para leer el **mismo** exec compartido:

```xml
<plugin>
  <groupId>org.jacoco</groupId>
  <artifactId>jacoco-maven-plugin</artifactId>
  <executions>
    <execution>
      <id>report-it</id>
      <phase>verify</phase>
      <goals><goal>report</goal></goals>
      <configuration>
        <dataFile>${project.parent.basedir}/target/it-coverage/jacoco-it.exec</dataFile>
        <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
      </configuration>
    </execution>
  </executions>
</plugin>
```

Tu Exec Maven Plugin existente que ejecuta `python -m unittest discover tests -v` es perfecto—déjalo como está.

---

### 3) `PlaygroundUtils/pom.xml`

Añade una ejecución de **solo informe** para que pueda mapear el exec compartido a sus propias clases:

```xml
<build>
  <plugins>
    <!-- mantén tus plugins existentes -->

    <plugin>
      <groupId>org.jacoco</groupId>
      <artifactId>jacoco-maven-plugin</artifactId>
      <executions>
        <execution>
          <id>report-it</id>
          <phase>verify</phase>
          <goals><goal>report</goal></goals>
          <configuration>
            <dataFile>${project.parent.basedir}/target/it-coverage/jacoco-it.exec</dataFile>
            <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
            <skip>${it.report.skip}</skip>
          </configuration>
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

Este módulo nunca inicia Jetty ni ejecuta Python; solo consume el exec compartido y sus propios `target/classes`. Si alguna clase de `PlaygroundUtils` es usada por la aplicación web durante las pruebas, aparecerá con cobertura. Si no se ejercitan, estarán al 0%—lo cual es la señal correcta.

---

## Cómo lo ejecutas

Desde la raíz del repositorio:

```bash
mvn -pl PlaygroundWeb -am clean verify
```

El orden de compilación compila ambos módulos, inicia Jetty una vez con el agente, ejecuta tus pruebas de Python, detiene Jetty, y luego genera:

* `PlaygroundWeb/target/site/jacoco-it/index.html`
* `PlaygroundUtils/target/site/jacoco-it/index.html`
* Opcionalmente, un informe agregado bajo el padre si habilitaste `report-aggregate`.

---

## Cuando tengas 10 módulos

* Si los 10 terminan dentro del **mismo WAR/JVM**, mantén el patrón de **único exec compartido**. Cada módulo añade una ejecución `report` que apunta al exec compartido. Todavía inicias Jetty una vez y ejecutas Python una vez.

* Si tienes **múltiples JVMs** (por ejemplo, servicios separados), asigna a cada JVM su propio `destfile` (por ejemplo, `it-coverage/serviceA.exec`, `serviceB.exec`), luego en el padre ejecuta:

  ```xml
  <plugin>
    <groupId>org.jacoco</groupId>
    <artifactId>jacoco-maven-plugin</artifactId>
    <executions>
      <execution>
        <id>merge-it</id>
        <phase>post-integration-test</phase>
        <goals><goal>merge</goal></goals>
        <configuration>
          <destFile>${project.basedir}/target/it-coverage/jacoco-merged.exec</destFile>
          <files>
            <file>${project.basedir}/target/it-coverage/serviceA.exec</file>
            <file>${project.basedir}/target/it-coverage/serviceB.exec</file>
            <!-- añade más según sea necesario -->
          </files>
        </configuration>
      </execution>

      <execution>
        <id>aggregate-report</id>
        <phase>verify</phase>
        <goals><goal>report-aggregate</goal></goals>
        <configuration>
          <dataFile>${project.basedir}/target/it-coverage/jacoco-merged.exec</dataFile>
          <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
        </configuration>
      </execution>
    </executions>
  </plugin>
  ```

* Si quieres limitar el ruido, establece `includes=org.lzw.*` (ya mostrado) o añade `excludes` a la línea del agente para filtrar librerías de terceros.

---

## Por qué ocurre tu problema actual

* Estabas creando **archivos exec por módulo**, por lo que te sentiste forzado a re-ejecutar Jetty con diferentes agentes para poblar cada uno. Eso es innecesario. Al agente no le importa a qué módulo "pertenece" una clase—registra cualquier clase cargada. Centraliza el exec y haz que el `report` de cada módulo apunte a él.

---

## Lista de comprobación rápida

* Un **compartido** `${jacoco.it.exec}` bajo el padre.
* Jetty iniciado **una vez** con `append=true` e `includes=org.lzw.*`.
* Pruebas de Python ejecutadas **una vez**.
* Cada módulo tiene un `jacoco:report` que lee el exec compartido.
* Opcionalmente, `report-aggregate` en el padre para un único HTML de nivel superior.

Eso debería hacer que tu configuración sea más simple y escalable. Si quieres, puedo producir diferencias exactas para tus POMs actuales con estos cambios aplicados.
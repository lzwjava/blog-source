---
audio: false
date: 2025-09-11
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Comprensión de la Integración de JaCoCo y Maven
translated: true
type: note
---

Entendido—así es cómo funcionan las piezas de JaCoCo en **tu POM exacto**, paso a paso, y por qué.

---

# Los dos flujos de cobertura que crea este POM

1. **Cobertura de pruebas unitarias (ruta de Surefire)**

* Vinculas el **`prepare-agent`** de JaCoCo sin ninguna configuración especial:

  ```xml
  <execution>
    <id>prepare-agent</id>
    <goals><goal>prepare-agent</goal></goals>
  </execution>
  ```

  Esto inyecta `-javaagent:...org.jacoco.agent-<ver>-runtime.jar` en la JVM de pruebas de **Surefire** a través de la propiedad `argLine`.
  • El **destfile** predeterminado es `${project.build.directory}/jacoco.exec`.
  • El valor predeterminado de **append** es `true` (el agente de JaCoCo añade datos cuando el archivo ya existe).
  • Efecto: cuando ejecutas las pruebas unitarias (si las hay) durante `test`, la cobertura se guarda en `target/jacoco.exec`.

2. **Cobertura de pruebas de integración (ruta de Jetty)**

* Defines un **archivo separado** para la cobertura de integración:

  ```xml
  <properties>
    <jacoco.it.exec>${project.build.directory}/jacoco-it.exec</jacoco.it.exec>
  </properties>
  ```
* Inicias Jetty **con su propio agente JaCoCo** apuntando a ese archivo:

  ```xml
  <plugin>
    <artifactId>jetty-maven-plugin</artifactId>
    ...
    <execution>
      <id>start-jetty</id>
      <phase>pre-integration-test</phase>
      <goals><goal>start</goal></goals>
      <configuration>
        <daemon>true</daemon>
        <jvmArgs>
          -javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${jacoco.it.exec}
        </jvmArgs>
        ...
      </configuration>
    </execution>
  </plugin>
  ```

  • Jetty se ejecuta en una **JVM separada**; su agente escribe en `target/jacoco-it.exec`.
  • Como no se especifica `append`, se aplica el valor predeterminado de JaCoCo `append=true`—así que múltiples inicios de Jetty añadirán datos al mismo archivo a menos que hagas un `clean` o establezcas `append=false`.

---

# Flujo del ciclo de vida (qué sucede en `mvn verify`)

1. **compile**

   * Spotless formatea (`spotless-maven-plugin`) y Checkstyle se ejecuta (`maven-checkstyle-plugin`).
   * Se prepara tu WAR (`maven-war-plugin`).

2. **test (Surefire)**

   * Si tienes pruebas unitarias, se ejecutan bajo el `argLine` inyectado por **`prepare-agent`** → la cobertura va a `target/jacoco.exec`.

3. **pre-integration-test**

   * Se inicia Jetty **en modo daemon**:

     ```xml
     <daemon>true</daemon>
     ```

     Maven recupera el control inmediatamente; Jetty sigue ejecutándose con el agente JaCoCo adjunto, escribiendo en `jacoco-it.exec`.

4. **integration-test**

   * Tus pruebas de Python acceden a la aplicación en ejecución:

     ```xml
     <plugin>
       <artifactId>exec-maven-plugin</artifactId>
       <execution>
         <id>python-integration-tests</id>
         <phase>integration-test</phase>
         <goals><goal>exec</goal></goals>
         <configuration>
           <executable>python3</executable>
           <workingDirectory>${project.parent.basedir}</workingDirectory>
           <arguments>
             <argument>-m</argument><argument>unittest</argument>
             <argument>discover</argument><argument>tests/</argument>
             <argument>-v</argument>
           </arguments>
         </configuration>
       </execution>
     </plugin>
     ```

     Estas pruebas ejercitan Jetty, por lo que la cobertura se acumula en **`target/jacoco-it.exec`** a través del agente de la JVM de Jetty.

5. **post-integration-test**

   * Jetty se detiene de forma limpia:

     ```xml
     <execution>
       <id>stop-jetty</id>
       <phase>post-integration-test</phase>
       <goals><goal>stop</goal></goals>
       ...
     </execution>
     ```

6. **verify**

   * Generas un **informe de integración separado** usando el archivo de datos de integración y un directorio de salida personalizado:

     ```xml
     <execution>
       <id>report-it</id>
       <phase>verify</phase>
       <goals><goal>report</goal></goals>
       <configuration>
         <dataFile>${jacoco.it.exec}</dataFile>
         <outputDirectory>${project.reporting.outputDirectory}/jacoco-it
         </outputDirectory>
       </configuration>
     </execution>
     ```
   * Resultado: el HTML se genera en `target/site/jacoco-it/index.html` resumiendo solo la cobertura de **integración** (de Jetty).

> Nota: Si también quieres un informe de **pruebas unitarias**, podrías añadir otra ejecución de `jacoco:report` que apunte al `target/jacoco.exec` predeterminado y envíe la salida a `target/site/jacoco`—manteniendo los informes de unidad e integración separados.

---

# Sobre "¿crear nuevo o reemplazar?" para los archivos `.exec`

* **El valor predeterminado del agente JaCoCo es `append=true`**.

  * Para las **pruebas unitarias**, el archivo es `target/jacoco.exec`. Cuando ejecutas `mvn verify` repetidamente **sin `clean`**, los datos pueden acumularse entre ejecuciones.
  * Para las **pruebas de integración con Jetty**, tus `jvmArgs` no anulan `append`, por lo que `target/jacoco-it.exec` también **añade datos** por defecto.

**Mejor práctica** (para evitar mezclar datos antiguos):

* Ejecuta `mvn clean verify`, **O** añade `append=false` en la línea del agente de Jetty:

  ```xml
  -javaagent:...org.jacoco.agent-...-runtime.jar=destfile=${jacoco.it.exec},append=false
  ```
* Si alguna vez quieres fusionar múltiples archivos `.exec` a propósito, usa `jacoco:merge` antes de `jacoco:report`.

---

# Qué hace cada bloque relevante en tu XML original (por referencia)

* **Ubicación del archivo de integración**

  ```xml
  <properties>
    <jacoco.it.exec>${project.build.directory}/jacoco-it.exec</jacoco.it.exec>
    <it.report.skip>false</it.report.skip>
  </properties>
  ```

  Define dónde se almacena la cobertura de integración. `it.report.skip` está declarado pero aún no está conectado a la ejecución del informe (ver consejo más abajo).

* **Agente para pruebas unitarias (ruta Surefire)**

  ```xml
  <plugin>
    <artifactId>jacoco-maven-plugin</artifactId>
    <executions>
      <execution>
        <id>prepare-agent</id>
        <goals><goal>prepare-agent</goal></goals>
      </execution>
      ...
    </executions>
  </plugin>
  ```

* **Jetty con JaCoCo para integración**

  ```xml
  <plugin>
    <artifactId>jetty-maven-plugin</artifactId>
    ...
    <jvmArgs>
      -javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${jacoco.it.exec}
    </jvmArgs>
    ...
  </plugin>
  ```

* **Pruebas de integración con Python mientras Jetty se ejecuta**

  ```xml
  <plugin>
    <artifactId>exec-maven-plugin</artifactId>
    <execution>
      <id>python-integration-tests</id>
      <phase>integration-test</phase>
      <goals><goal>exec</goal></goals>
      ...
    </execution>
  </plugin>
  ```

* **Generar el informe de cobertura de integración en verify**

  ```xml
  <execution>
    <id>report-it</id>
    <phase>verify</phase>
    <goals><goal>report</goal></goals>
    <configuration>
      <dataFile>${jacoco.it.exec}</dataFile>
      <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
    </configuration>
  </execution>
  ```

---

# Consejos prácticos / pequeñas mejoras

* **Evita datos de integración obsoletos**
  Añade `append=false` al agente de Jetty (mostrado arriba), o ejecuta siempre `mvn clean verify`.

* **Conecta tu interruptor `it.report.skip`**
  Si quieres omitir la generación del informe de integración mediante una propiedad:

  ```xml
  <execution>
    <id>report-it</id>
    <phase>verify</phase>
    <goals><goal>report</goal></goals>
    <configuration>
      <skip>${it.report.skip}</skip>
      <dataFile>${jacoco.it.exec}</dataFile>
      <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
    </configuration>
  </execution>
  ```

* **Mantén separados los informes de unidad e integración**
  Ya has separado el informe de integración en `site/jacoco-it`. Si también necesitas el informe de unidad, añade otro `jacoco:report` (sin anular `dataFile`) que escriba en `site/jacoco`.

* **Nota para múltiples módulos**
  Esta configuración local al módulo reporta la cobertura solo para **PlaygroundWeb**. Si más adelante quieres una vista **combinada**, usa `jacoco:merge` (para combinar archivos `.exec`) y/o `report-aggregate` desde un `pom` padre con `packaging=pom` (JaCoCo 0.8.8+).

---

# TL;DR

* **Pruebas unitarias** → `prepare-agent` inyecta JaCoCo en la JVM de Surefire → `target/jacoco.exec`.
* **Pruebas de integración** → Jetty se inicia con su propio agente JaCoCo → `target/jacoco-it.exec`.
* **Informe** → En `verify`, `jacoco:report` renderiza **solo la cobertura de integración** en `target/site/jacoco-it`.
* **Comportamiento de archivos** → JaCoCo **añade por defecto**; prefiere `mvn clean verify` o `append=false` para evitar mezclar ejecuciones.
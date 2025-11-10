---
audio: false
generated: true
image: false
lang: es
layout: post
title: Configuración de Cobertura JaCoCo para Spring con Múltiples Módulos
translated: true
type: note
---

Excelente—JaCoCo funciona bien para un proyecto Spring multi-módulo. Necesitarás:

1.  cobertura de pruebas unitarias por módulo;
2.  un reporte agregado en el padre;
3.  un perfil opcional para incluir la cobertura de **integración** (por ejemplo, la ejecución de Liberty+EAR probada con tests de Python).

A continuación, una configuración probada en batalla que puedes usar directamente.

---

### `pom.xml` Padre (packaging `pom`)

```xml
<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.myco.chat</groupId>
  <artifactId>chat-parent</artifactId>
  <version>1.0.0</version>
  <packaging>pom</packaging>

  <modules>
    <module>ChatCommon</module>
    <module>ChatLib</module>
    <module>ChatCore</module>
    <module>ChatWeb</module>
  </modules>

  <build>
    <pluginManagement>
      <plugins>
        <plugin>
          <groupId>org.jacoco</groupId>
          <artifactId>jacoco-maven-plugin</artifactId>
          <version>0.8.12</version>
        </plugin>
        <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-surefire-plugin</artifactId>
          <version>3.2.5</version>
        </plugin>
        <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-failsafe-plugin</artifactId>
          <version>3.2.5</version>
        </plugin>
      </plugins>
    </pluginManagement>
  </build>

  <!-- Reporte agregado para las pruebas unitarias de TODOS los módulos -->
  <reporting>
    <plugins>
      <plugin>
        <groupId>org.jacoco</groupId>
        <artifactId>jacoco-maven-plugin</artifactId>
        <version>0.8.12</version>
        <reportSets>
          <reportSet>
            <reports>
              <!-- Esto activa 'report-aggregate' cuando ejecutas 'mvn verify' en el padre -->
              <report>report-aggregate</report>
            </reports>
            <configuration>
              <outputDirectory>${project.reporting.outputDirectory}/jacoco-aggregate</outputDirectory>
              <reports>
                <xml>true</xml>
                <html>true</html>
                <csv>false</csv>
              </reports>
              <!-- Filtros globales opcionales -->
              <excludes>
                <exclude>**/*Application.class</exclude>
                <exclude>**/*Configuration.class</exclude>
                <exclude>**/generated/**</exclude>
              </excludes>
            </configuration>
          </reportSet>
        </plugins>
      </plugin>
    </plugins>
  </reporting>

  <!-- Perfil para agregar cobertura de INTEGRACIÓN (ej. Liberty + tests de Python) -->
  <profiles>
    <profile>
      <id>it-coverage</id>
      <activation><activeByDefault>false</activeByDefault></activation>
      <build>
        <plugins>
          <plugin>
            <groupId>org.jacoco</groupId>
            <artifactId>jacoco-maven-plugin</artifactId>
            <version>0.8.12</version>
            <executions>
              <!-- Crea un reporte agregado que también lee archivos .exec externos -->
              <execution>
                <id>report-aggregate-it</id>
                <phase>verify</phase>
                <goals><goal>report-aggregate</goal></goals>
                <configuration>
                  <!-- Apunta a uno o más archivos .exec volcados por el agente JVM de Liberty -->
                  <dataFiles>
                    <!-- Ejemplo de rutas; ajusta según la ubicación en tu CI/Liberty -->
                    <dataFile>${project.basedir}/.jacoco/jacoco-it.exec</dataFile>
                    <!-- Puedes agregar más entradas dataFile si tienes volcados por nodo y los quieres todos -->
                  </dataFiles>
                  <outputDirectory>${project.reporting.outputDirectory}/jacoco-aggregate-it</outputDirectory>
                  <reports>
                    <xml>true</xml>
                    <html>true</html>
                    <csv>false</csv>
                  </reports>
                  <excludes>
                    <exclude>**/generated/**</exclude>
                  </excludes>
                </configuration>
              </execution>
            </executions>
          </plugin>
        </plugins>
      </build>
    </profile>
  </profiles>
</project>
```

---

### Cada módulo hijo (`ChatCommon/pom.xml`, `ChatLib/pom.xml`, `ChatCore/pom.xml`, `ChatWeb/pom.xml`)

```xml
<project>
  <parent>
    <groupId>com.myco.chat</groupId>
    <artifactId>chat-parent</artifactId>
    <version>1.0.0</version>
  </parent>
  <modelVersion>4.0.0</modelVersion>
  <artifactId>ChatCommon</artifactId>
  <packaging>jar</packaging>

  <build>
    <plugins>
      <!-- Conecta el agente para las pruebas UNIT en este módulo -->
      <plugin>
        <groupId>org.jacoco</groupId>
        <artifactId>jacoco-maven-plugin</artifactId>
        <version>0.8.12</version>
        <executions>
          <execution>
            <id>prepare-agent</id>
            <goals><goal>prepare-agent</goal></goals>
            <configuration>
              <!-- Pone el argLine en una propiedad nombrada, para poder mezclarlo con otros args -->
              <propertyName>jacocoArgLine</propertyName>
              <append>true</append>
              <excludes>
                <exclude>**/generated/**</exclude>
              </excludes>
            </configuration>
          </execution>
          <execution>
            <id>report</id>
            <phase>verify</phase>
            <goals><goal>report</goal></goals>
            <configuration>
              <reports>
                <xml>true</xml>
                <html>true</html>
                <csv>false</csv>
              </reports>
            </configuration>
          </execution>
          <!-- Opcional: hacer cumplir mínimos -->
          <execution>
            <id>check</id>
            <goals><goal>check</goal></goals>
            <configuration>
              <rules>
                <rule>
                  <element>PACKAGE</element>
                  <limits>
                    <limit>
                      <counter>LINE</counter>
                      <value>COVEREDRATIO</value>
                      <minimum>0.60</minimum>
                    </limit>
                    <limit>
                      <counter>BRANCH</counter>
                      <value>COVEREDRATIO</value>
                      <minimum>0.40</minimum>
                    </limit>
                  </limits>
                </rule>
              </rules>
            </configuration>
          </execution>
        </executions>
      </plugin>

      <!-- Asegura que Surefire use el agente -->
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-surefire-plugin</artifactId>
        <configuration>
          <argLine>${jacocoArgLine} ${surefireArgLine}</argLine>
        </configuration>
      </plugin>

      <!-- (Opcional) Failsafe para ITs a nivel de módulo -->
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-failsafe-plugin</artifactId>
        <configuration>
          <argLine>${jacocoArgLine} ${failsafeArgLine}</argLine>
        </configuration>
      </plugin>
    </plugins>
  </build>
</project>
```

> Haz lo mismo en `ChatLib`, `ChatCore` y `ChatWeb`.
> Para `ChatWeb` (un WAR/JAR de Spring Boot), la configuración es idéntica.

---

### Cómo ejecutarlo

**Cobertura de pruebas unitarias en todos los módulos (XML agregado en el padre):**

```bash
mvn -q clean verify
# XML:  target/site/jacoco-aggregate/jacoco.xml
# HTML: target/site/jacoco-aggregate/index.html
```

**Cobertura de integración desde Liberty + tests de Python:**

1.  Inicia Liberty con el agente de JaCoCo (como se comentó antes), ejecuta los tests de Python, detén o vuelca.
    Asegúrate de que el `.exec` quede en `${project.basedir}/.jacoco/jacoco-it.exec` (o actualiza esa ruta en el perfil del padre).
2.  Construye el agregado incluyendo los datos de IT:

```bash
mvn -q -Pit-coverage verify
# XML:  target/site/jacoco-aggregate-it/jacoco.xml
# HTML: target/site/jacoco-aggregate-it/index.html
```

---

### Notas que ahorran tiempo

*   **La agregación solo funciona desde el padre** (packaging `pom`) con módulos declarados. Ejecuta `mvn` desde el directorio padre.
*   **El XML** (`jacoco.xml`) se produce cuando lo habilitas en `<reports>`; esto es lo que usan Codecov/Sonar.
*   Si recoges múltiples archivos `.exec` (ej., varios nodos de Liberty), puedes:
    *   listarlos todos bajo `<dataFiles>…</dataFiles>` en el perfil `it-coverage`, o
    *   fusionarlos primero (con `jacococli.jar merge …`) y luego apuntar al archivo fusionado.
*   No apuntes los classfiles al EAR; el reporte de JaCoCo necesita las **clases compiladas de los módulos** (`*/target/classes`) y las fuentes—manejado automáticamente por `report-aggregate`.
*   Si Surefire también establece su propio `argLine`, mantén `${jacocoArgLine` primero para no perder el agente.

Si compartes las raíces exactas de los paquetes de tus módulos y dónde termina tu `.exec` de Liberty, puedo ajustar `<dataFiles>` y cualquier exclusión para que tu XML agregado esté limpio y listo para CI.
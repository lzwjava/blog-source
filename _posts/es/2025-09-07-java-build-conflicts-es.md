---
audio: false
date: 2025-09-07
generated: true
image: false
lang: es
layout: post
title: Resolución de Conflictos de Versión en Compilaciones Java
translated: true
type: note
---

Estás compilando con **Java 8** (archivo de clase 52.0), pero algunos plugins/librerías de construcción en tu POM fueron compilados para versiones más nuevas de Java. El primero en fallar es **Spotless** (archivo de clase 55.0 = Java 11). También tienes otros elementos de Java 11+ que causarán problemas incluso si se elimina Spotless (Checkstyle 10.x, Logback 1.5, y el namespace Jakarta Servlet 5 vs el namespace javax de Spring 5).

A continuación, se presentan dos formas limpias de solucionarlo. Elige una y estarás listo.

---

## Opción A — Mantenerse en Java 8 (funciona con Spring 5.2.x y Jetty 9.4)

* Elimina/retrocede los plugins y librerías de Java 11+.
* Usa **javax.servlet-api 4.0.1** (Spring 5 usa `javax.*`, no `jakarta.*`).
* Mantén Jetty 9.4 (era Servlet 3.1/4).

Pega este POM (solo las partes siguientes difieren del tuyo):

```xml
<project>
  ...
  <properties>
    <maven.compiler.source>8</maven.compiler.source>
    <maven.compiler.target>8</maven.compiler.target>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
  </properties>

  <dependencies>
    <!-- Spring 5.x está bien -->
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-context</artifactId>
      <version>5.2.2.RELEASE</version>
    </dependency>
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-web</artifactId>
      <version>5.2.2.RELEASE</version>
    </dependency>
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-webmvc</artifactId>
      <version>5.2.2.RELEASE</version>
    </dependency>
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-core</artifactId>
      <version>5.2.2.RELEASE</version>
    </dependency>

    <!-- Dependencias de test sin cambios -->
    <dependency>
      <groupId>org.junit.jupiter</groupId>
      <artifactId>junit-jupiter-api</artifactId>
      <version>5.13.1</version>
      <scope>test</scope>
    </dependency>
    <dependency>
      <groupId>org.junit.jupiter</groupId>
      <artifactId>junit-jupiter-engine</artifactId>
      <version>5.13.1</version>
      <scope>test</scope>
    </dependency>
    <dependency>
      <groupId>org.mockito</groupId>
      <artifactId>mockito-core</artifactId>
      <version>5.18.0</version>
      <scope>test</scope>
    </dependency>
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-test</artifactId>
      <version>5.2.2.RELEASE</version>
      <scope>test</scope>
    </dependency>

    <!-- AOP ok -->
    <dependency>
      <groupId>org.aspectj</groupId>
      <artifactId>aspectjrt</artifactId>
      <version>1.9.24</version>
    </dependency>
    <dependency>
      <groupId>org.aspectj</groupId>
      <artifactId>aspectjweaver</artifactId>
      <version>1.9.24</version>
    </dependency>

    <!-- SLF4J 2.0 es Java 8+, OK -->
    <dependency>
      <groupId>org.slf4j</groupId>
      <artifactId>slf4j-api</artifactId>
      <version>2.0.17</version>
    </dependency>

    <!-- ↓ Retrocede Logback a la línea compatible con Java 8 -->
    <dependency>
      <groupId>ch.qos.logback</groupId>
      <artifactId>logback-classic</artifactId>
      <version>1.2.13</version>
    </dependency>

    <!-- ↓ Usa javax servlet para Spring 5.x + Jetty 9.4 -->
    <dependency>
      <groupId>javax.servlet</groupId>
      <artifactId>javax.servlet-api</artifactId>
      <version>4.0.1</version>
      <scope>provided</scope>
    </dependency>

    <dependency>
      <groupId>org.apache.commons</groupId>
      <artifactId>commons-lang3</artifactId>
      <version>3.17.0</version>
    </dependency>
  </dependencies>

  <build>
    <plugins>
      <!-- Mantén tu exec-maven-plugin si necesitas JavadocRemover -->
      <plugin>
        <groupId>org.codehaus.mojo</groupId>
        <artifactId>exec-maven-plugin</artifactId>
        <version>3.5.1</version>
        <executions>
          <execution>
            <id>remove-javadoc</id>
            <phase>compile</phase>
            <goals><goal>java</goal></goals>
            <configuration>
              <mainClass>org.lzw.JavadocRemover</mainClass>
              <arguments><argument>src/main</argument></arguments>
            </configuration>
          </execution>
        </executions>
      </plugin>

      <!-- ↓ ELIMINA Spotless o condicionalo detrás de un perfil de Java 11+.
           Si realmente lo quieres en Java 8, usa una versión antigua de Spotless + JDK8,
           pero lo más simple es eliminarlo ahora. -->
      <!-- (Bloque del plugin Spotless eliminado) -->

      <!-- ↓ Checkstyle: elige un motor compatible con Java 8 -->
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-checkstyle-plugin</artifactId>
        <version>3.1.2</version>
        <dependencies>
          <dependency>
            <groupId>com.puppycrawl.tools</groupId>
            <artifactId>checkstyle</artifactId>
            <version>9.3</version>
          </dependency>
        </dependencies>
        <configuration>
          <configLocation>${project.basedir}/checks.xml</configLocation>
          <failOnViolation>true</failOnViolation>
        </configuration>
        <executions>
          <execution>
            <id>checkstyle-check</id>
            <phase>compile</phase>
            <goals><goal>check</goal></goals>
          </execution>
        </executions>
      </plugin>

      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-war-plugin</artifactId>
        <version>3.4.0</version>
        <configuration>
          <failOnMissingWebXml>true</failOnMissingWebXml>
        </configuration>
      </plugin>

      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-surefire-plugin</artifactId>
        <version>3.5.3</version>
      </plugin>

      <plugin>
        <groupId>org.jacoco</groupId>
        <artifactId>jacoco-maven-plugin</artifactId>
        <version>0.8.12</version>
        <executions>
          <execution>
            <id>prepare-agent</id>
            <goals><goal>prepare-agent</goal></goals>
          </execution>
          <execution>
            <id>report</id>
            <phase>verify</phase>
            <goals><goal>report</goal></goals>
          </execution>
        </executions>
      </plugin>

      <!-- Jetty 9.4 funciona bien en Java 8 + javax.servlet -->
      <plugin>
        <groupId>org.eclipse.jetty</groupId>
        <artifactId>jetty-maven-plugin</artifactId>
        <version>9.4.54.v20240208</version>
        <configuration>
          <httpConnector><port>8080</port></httpConnector>
          <webApp><contextPath>/</contextPath></webApp>
        </configuration>
      </plugin>
    </plugins>
  </build>

  <!-- Mantén tu perfil 'python-integration-tests',
       pero ten en cuenta que spring-boot-maven-plugin 3.5.0 necesita Java 17+.
       Deja este perfil DESACTIVADO cuando compiles con Java 8. -->
  <profiles>
    <profile>
      <id>python-integration-tests</id>
      <build>
        <plugins>
          <plugin>
            <groupId>org.jacoco</groupId>
            <artifactId>jacoco-maven-plugin</artifactId>
            <version>0.8.12</version>
            <executions>
              <execution>
                <id>prepare-agent-integration</id>
                <goals><goal>prepare-agent-integration</goal></goals>
                <configuration>
                  <destFile>${project.build.directory}/jacoco-it.exec</destFile>
                  <propertyName>jacoco.agent.it</propertyName>
                </configuration>
              </execution>
            </executions>
          </plugin>

          <!-- Deja este plugin Boot aquí pero NO actives este perfil en Java 8 -->
          <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
            <version>3.5.0</version>
          </plugin>

          <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.5.1</version>
            <executions>
              <execution>
                <id>python-integration-tests</id>
                <phase>integration-test</phase>
                <goals><goal>exec</goal></goals>
                <configuration>
                  <executable>python</executable>
                  <workingDirectory>${project.basedir}</workingDirectory>
                  <arguments>
                    <argument>-m</argument><argument>unittest</argument>
                    <argument>discover</argument><argument>tests/</argument>
                    <argument>-v</argument>
                  </arguments>
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

Luego ejecuta:

```bash
mvn -v                # confirma que estás usando un JDK 1.8.x
mvn clean package
# o para desarrollo
mvn jetty:run
```

---

## Opción B — Actualiza tu JDK de construcción (Java 17 es un punto ideal)

* Cambia tu **compilación** a JDK 17+ (y `mvn -v` debería mostrar Java 17).
* Mantén Spotless y Checkstyle 10.x como están.
* Puedes mantener `jakarta.servlet-api` **solo si** también mueves el runtime a Jetty 11+ o Tomcat 10+ y migras tu código a los namespaces `jakarta.*` (mundo Spring 6 / Spring Boot 3). Si te mantienes en Spring 5.2.x, usa `javax.servlet-api:4.0.1` y un contenedor Servlet 4 en su lugar.

Comandos típicos:

```bash
# En Ubuntu, instala un JDK 17 y selecciónalo:
sudo apt install openjdk-17-jdk
sudo update-alternatives --config java
sudo update-alternatives --config javac

mvn -v             # debería imprimir la versión de Java 17
mvn clean package
```

Si aún debes generar bytecode de Java 8 mientras compilas con Java 17, configura:

```xml
<properties>
  <maven.compiler.release>8</maven.compiler.release>
</properties>
```

(Pero ten en cuenta: dependencias como Logback 1.5 son Java 11+ de todos modos, por lo que tu **runtime** debe ser 11+ si las incluyes).

---

## Por qué falló (versión corta)

* `UnsupportedClassVersionError ... class file version 55.0` = plugin/librería compilado con **Java 11**, pero Maven se ejecutó bajo **Java 8**.
* Tus infractores específicos en Java 8:

  * Spotless plugin 2.44.5 (Java 11+)
  * Checkstyle 10.25.0 (Java 11+)
  * Logback 1.5.x (Java 11+)
  * `jakarta.servlet-api:5.0.0` no coincide con `javax.*` de Spring 5 y Jetty 9.4.

---

Si me dices qué ruta prefieres (mantenerse en Java 8 vs pasar a Java 17+), ajustaré el POM exactamente para esa configuración y, si es necesario, te daré las diferencias mínimas para tu `web.xml`/configuración de Spring y tu elección de Jetty/Tomcat.
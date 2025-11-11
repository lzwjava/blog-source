---
audio: false
generated: true
lang: es
layout: post
title: Plugin Ejecutivo de Maven
translated: true
type: note
---

Para usar el plugin `org.codehaus.mojo` Exec Maven Plugin en tu proyecto Maven, necesitas configurarlo en tu archivo `pom.xml` y decidir cómo quieres ejecutar programas—ya sean comandos externos o programas Java—durante tu proceso de construcción. El plugin proporciona dos objetivos principales: `exec:exec` para ejecutar programas externos y `exec:java` para ejecutar clases Java. A continuación, te guiaré a través de los pasos para configurarlo y usarlo efectivamente.

### Paso 1: Agregar el Plugin a tu `pom.xml`
Primero, incluye el Exec Maven Plugin en la sección `<build><plugins>` de tu `pom.xml`. Especifica el `groupId`, `artifactId` y una versión (la más reciente hasta ahora es `3.1.0`):

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.0</version>
        </plugin>
    </plugins>
</build>
```

Esto agrega el plugin a tu proyecto, pero aún no hará nada hasta que lo configures o ejecutes sus objetivos manualmente.

### Paso 2: Elige tu Objetivo
El plugin ofrece dos objetivos principales:
- **`exec:exec`**: Ejecuta cualquier programa externo (por ejemplo, scripts de shell, binarios o incluso el comando `java`).
- **`exec:java`**: Ejecuta una clase Java con un método `main` de tu proyecto en la misma JVM que Maven.

Puedes usar estos objetivos ya sea ejecutándolos manualmente desde la línea de comandos (por ejemplo, `mvn exec:exec`) o vinculándolos a una fase específica en el ciclo de vida de construcción de Maven.

### Opción 1: Ejecutar un Programa Java con `exec:java`
Si quieres ejecutar una clase Java de tu proyecto, usa el objetivo `exec:java`. Esto es ideal para ejecutar un método `main` en una clase que es parte de tu proyecto, aprovechando automáticamente el classpath de tiempo de ejecución del proyecto (incluyendo dependencias).

#### Ejecución Manual
Agrega una configuración para especificar la clase principal:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.0</version>
            <configuration>
                <mainClass>com.example.Main</mainClass>
            </configuration>
        </plugin>
    </plugins>
</build>
```

Luego, ejecútalo desde la línea de comandos:

```bash
mvn exec:java
```

Esto ejecuta `com.example.Main` en la misma JVM que Maven, heredando la configuración de la JVM de Maven.

#### Ejecución Automática Durante la Construcción
Para ejecutarlo automáticamente durante una fase de construcción (por ejemplo, `test`), usa la sección `<executions>`:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.0</version>
            <executions>
                <execution>
                    <id>run-my-java</id>
                    <phase>test</phase>
                    <goals>
                        <goal>java</goal>
                    </goals>
                    <configuration>
                        <mainClass>com.example.Main</mainClass>
                    </configuration>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

Ahora, cuando ejecutes `mvn test`, la clase `com.example.Main` se ejecutará durante la fase `test`.

#### Pasar Argumentos o Propiedades del Sistema
Puedes pasar argumentos al método `main` o establecer propiedades del sistema:

```xml
<configuration>
    <mainClass>com.example.Main</mainClass>
    <arguments>
        <argument>arg1</argument>
        <argument>arg2</argument>
    </arguments>
    <systemProperties>
        <systemProperty>
            <key>propertyName</key>
            <value>propertyValue</value>
        </systemProperty>
    </systemProperties>
</configuration>
```

Ten en cuenta que `exec:java` se ejecuta en la misma JVM que Maven, por lo que las opciones de la JVM (por ejemplo, `-Xmx`) se heredan de cómo se invoca Maven (por ejemplo, `mvn -Xmx512m exec:java`).

### Opción 2: Ejecutar un Programa Externo con `exec:exec`
Para ejecutar programas externos como scripts de shell o comandos, usa el objetivo `exec:exec`.

#### Ejecución Manual
Configura el plugin para ejecutar un script:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.0</version>
            <configuration>
                <executable>myScript.sh</executable>
                <workingDirectory>/path/to/dir</workingDirectory>
                <arguments>
                    <argument>param1</argument>
                    <argument>param2</argument>
                </arguments>
            </configuration>
        </plugin>
    </plugins>
</build>
```

Ejecútalo con:

```bash
mvn exec:exec
```

Esto ejecuta `myScript.sh` con los argumentos especificados en el directorio de trabajo dado.

#### Ejecución Automática Durante la Construcción
Vincúlalo a una fase, como iniciar y detener un servidor para pruebas de integración:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.0</version>
            <executions>
                <execution>
                    <id>start-server</id>
                    <phase>pre-integration-test</phase>
                    <goals>
                        <goal>exec</goal>
                    </goals>
                    <configuration>
                        <executable>startServer.sh</executable>
                    </configuration>
                </execution>
                <execution>
                    <id>stop-server</id>
                    <phase>post-integration-test</phase>
                    <goals>
                        <goal>exec</goal>
                    </goals>
                    <configuration>
                        <executable>stopServer.sh</executable>
                    </configuration>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

Ejecutar `mvn integration-test` iniciará el servidor antes de las pruebas y lo detendrá después.

#### Ejecutar Java con Opciones Personalizadas de JVM
Si necesitas una JVM separada con opciones específicas (a diferencia de `exec:java`), usa `exec:exec` con el ejecutable `java`. Necesitarás gestionar el classpath manualmente. Aquí hay un ejemplo:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.0</version>
            <configuration>
                <executable>java</executable>
                <arguments>
                    <argument>-Xmx512m</argument>
                    <argument>-classpath</argument>
                    <argument>${project.build.outputDirectory}</argument>
                    <argument>com.example.Main</argument>
                </arguments>
            </configuration>
        </plugin>
    </plugins>
</build>
```

Para incluir dependencias en el classpath, puedes usar el `maven-dependency-plugin` para generarlo:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-dependency-plugin</artifactId>
            <version>3.2.0</version>
            <executions>
                <execution>
                    <id>build-classpath</id>
                    <phase>generate-resources</phase>
                    <goals>
                        <goal>build-classpath</goal>
                    </goals>
                    <configuration>
                        <outputProperty>project.classpath</outputProperty>
                    </configuration>
                </execution>
            </executions>
        </plugin>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.1.0</version>
            <executions>
                <execution>
                    <id>run-java</id>
                    <phase>test</phase>
                    <goals>
                        <goal>exec</goal>
                    </goals>
                    <configuration>
                        <executable>java</executable>
                        <arguments>
                            <argument>-Xmx512m</argument>
                            <argument>-classpath</argument>
                            <argument>${project.classpath}:${project.build.outputDirectory}</argument>
                            <argument>com.example.Main</argument>
                        </arguments>
                    </configuration>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

Ajusta el separador del classpath (`:` para Unix, `;` para Windows) según sea necesario.

### Opciones de Configuración Adicionales
- **Variables de Entorno** (para `exec:exec`):
  ```xml
  <configuration>
      <executable>myScript.sh</executable>
      <environmentVariables>
          <MY_VAR>value</MY_VAR>
      </environmentVariables>
  </configuration>
  ```
- **Directorio de Trabajo**: Usa `<workingDirectory>` para establecer dónde se ejecuta el comando.

### Resumen
El Exec Maven Plugin es versátil:
- Usa `exec:java` para ejecutar clases Java de tu proyecto fácilmente, aprovechando el classpath del proyecto, pero se ejecuta en la JVM de Maven.
- Usa `exec:exec` para programas externos o Java con opciones personalizadas de JVM, requiriendo gestión manual del classpath si es necesario.
- Configúralo en `pom.xml` y ejecútalo manualmente (`mvn exec:java` o `mvn exec:exec`) o vincúlalo a fases de construcción con `<executions>`.

¡Esta configuración te permite integrar ejecuciones personalizadas de manera fluida en tu proceso de construcción de Maven!
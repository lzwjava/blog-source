---
audio: false
date: 2025-09-08
generated: true
image: false
lang: es
layout: post
title: Estrategia de Reporte de Cobertura Multi-Módulo con JaCoCo
translated: true
type: note
---

Por supuesto. Tu análisis es acertado, especialmente en lo que respecta a las complejidades de JaCoCo con pruebas de integración externas. Ejecutar la construcción dos veces definitivamente no es lo ideal.

La estrategia que buscas implica centralizar la ejecución de las pruebas y luego agregar los resultados. Estás muy cerca, y el objetivo `aggregate` es sin duda la herramienta correcta, pero debe aplicarse de una manera específica para este escenario.

Aquí tienes la estrategia recomendada: **Genera un único archivo de cobertura (`.exec`) en tu módulo de aplicación web, y luego utiliza un módulo de informes separado y dedicado para crear un único informe agregado para todos los módulos relevantes.**

Este enfoque es limpio, escalable y evita construcciones redundantes.

-----

## El Concepto Central

Cuando tu aplicación `PlaygroundWeb` se ejecuta en Jetty con el agente JaCoCo, el agente instrumenta **todas las clases cargadas por el classloader de la aplicación**. Esto incluye las clases del propio `PlaygroundWeb` *y* todas sus dependencias, como `PlaygroundUtils.jar`.

Por lo tanto, el único archivo `jacoco-it.exec` generado durante la construcción de `PlaygroundWeb` ya contiene los datos de cobertura para **ambos módulos**. El desafío es simplemente dirigir la herramienta de informes de JaCoCo al código fuente de todos los módulos que necesita para construir el informe HTML final.

-----

## Una Estrategia Escalable en 4 Pasos

Aquí tienes una guía paso a paso para refactorizar tu proyecto y obtener un informe de cobertura agregado y limpio.

### Paso 1: Crear un Módulo de Informes Dedicado

Primero, crea un nuevo módulo exclusivamente para la agregación. Esta es una buena práctica de Maven que mantiene las responsabilidades separadas.

1.  En tu `pom.xml` raíz (`PlaygroundLib`), añade el nuevo módulo:
    ```xml
    <modules>
        <module>PlaygroundUtils</module>
        <module>PlaygroundWeb</module>
        <module>PlaygroundReports</module> </modules>
    ```
2.  Crea un nuevo directorio `PlaygroundReports` en la raíz con su propio `pom.xml`.

Tu nueva estructura de proyecto se verá así:

```
.
├── PlaygroundReports
│   └── pom.xml
├── PlaygroundUtils
│   └── pom.xml
├── PlaygroundWeb
│   └── pom.xml
└── pom.xml
```

### Paso 2: Configurar el `pom.xml` del Módulo de Informes

Este nuevo `pom.xml` es donde ocurre la magia. Dependerá de todos los módulos que quieras incluir en el informe y ejecutará el objetivo `report-aggregate`.

**`PlaygroundReports/pom.xml`:**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>com.lzw</groupId>
        <artifactId>PlaygroundLib</artifactId>
        <version>1.0</version>
    </parent>
    <artifactId>PlaygroundReports</artifactId>
    <packaging>pom</packaging>
    <name>PlaygroundReports</name>

    <dependencies>
        <dependency>
            <groupId>com.lzw</groupId>
            <artifactId>PlaygroundWeb</artifactId>
            <version>${project.version}</version>
        </dependency>
        <dependency>
            <groupId>com.lzw</groupId>
            <artifactId>PlaygroundUtils</artifactId>
            <version>${project.version}</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.jacoco</groupId>
                <artifactId>jacoco-maven-plugin</artifactId>
                <executions>
                    <execution>
                        <id>aggregate-report</id>
                        <phase>verify</phase>
                        <goals>
                            <goal>report-aggregate</goal>
                        </goals>
                        <configuration>
                            <dataFiles>
                                <dataFile>${project.basedir}/../PlaygroundWeb/target/jacoco-it.exec</dataFile>
                            </dataFiles>
                            <outputDirectory>${project.reporting.outputDirectory}/jacoco-aggregate</outputDirectory>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>
```

### Paso 3: Simplificar el Módulo `PlaygroundWeb`

Tu módulo `PlaygroundWeb` ahora es solo responsable de **generar los datos de cobertura**, no de informar sobre ellos. Puedes eliminar la ejecución de `jacoco:report` de su `pom.xml`.

**`PlaygroundWeb/pom.xml` (solo cambios):**

```xml
<plugin>
    <groupId>org.jacoco</groupId>
    <artifactId>jacoco-maven-plugin</artifactId>
    <executions>
        <execution>
            <id>prepare-agent</id>
            <goals>
                <goal>prepare-agent</goal>
            </goals>
            <configuration>
                <propertyName>jacoco.it.agent</propertyName>
                <destFile>${project.build.directory}/jacoco-it.exec</destFile>
            </configuration>
        </execution>
        </executions>
</plugin>

<plugin>
    <groupId>org.eclipse.jetty</groupId>
    <artifactId>jetty-maven-plugin</artifactId>
    <executions>
        <execution>
            <id>start-jetty</id>
            <phase>pre-integration-test</phase>
            <goals>
                <goal>start</goal>
            </goals>
            <configuration>
                <daemon>true</daemon>
                <jvmArgs>
                    ${jacoco.it.agent}
                </jvmArgs>
                </configuration>
        </execution>
        </executions>
</plugin>
```

*Nota*: He modificado ligeramente la configuración de `prepare-agent` para usar una propiedad (`jacoco.it.agent`) y luego referenciarla en `jetty-maven-plugin`. Esta es una forma robusta de pasar la cadena del agente. La configuración anterior en tu `pom.xml` también era correcta, pero esto hace que la intención sea más clara.

### Paso 4: Limpiar `PlaygroundUtils`

El módulo `PlaygroundUtils` no necesita ninguna configuración del plugin JaCoCo para las pruebas de integración. Su código está cubierto a través de `PlaygroundWeb`, y la generación de informes la maneja `PlaygroundReports`. Puedes eliminar cualquier propiedad o plugin relacionado con JaCoCo de su `pom.xml`.

-----

## Cómo Esto Resuelve el Problema

1.  **Construcción Única:** Ejecutas `mvn clean verify` desde el directorio raíz una sola vez.
2.  **Ciclo de Vida Correcto:**
      * Maven construye `PlaygroundUtils`.
      * Maven construye `PlaygroundWeb`, inicia Jetty con el agente JaCoCo, ejecuta tus pruebas de Python (que acceden a código en ambos módulos), detiene Jetty y produce `PlaygroundWeb/target/jacoco-it.exec`.
      * Maven construye `PlaygroundReports`. En la fase `verify`, se ejecuta el objetivo `report-aggregate`. Encuentra el archivo `.exec` de `PlaygroundWeb` y, debido a las dependencias, sabe dónde encontrar el código fuente tanto de `PlaygroundWeb` como de `PlaygroundUtils`.
      * Genera un **único informe HTML unificado** con la cobertura de ambos módulos.
3.  **Escalabilidad:** Si añades diez módulos de biblioteca más, solo tienes que añadirlos como dependencias en el `PlaygroundReports/pom.xml`. La lógica central no cambia. Esta es la solución limpia y escalable que estabas buscando.
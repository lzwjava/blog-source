---
audio: false
date: 2025-09-08
generated: true
image: false
lang: es
layout: post
title: Estrategia de Cobertura JaCoCo para Pruebas de Python
translated: true
type: note
---

# Análisis y Estrategia para Cobertura JaCoCo con Pruebas de Integración en Python

## Análisis de la Situación Actual

Has configurado un proyecto Maven multi-módulo con:
- POM padre (`PlaygroundLib`)
- Módulo `PlaygroundUtils` (JAR con clases de utilidad)
- Módulo `PlaygroundWeb` (WAR con controladores Spring MVC)

Tu objetivo es usar `unittest` de Python para probar endpoints de API y generar reportes de cobertura para el código Java. El desafío es que las pruebas de Python están fuera del proyecto Java, y necesitas ejecutar Jetty para servir la aplicación durante las pruebas.

## Problemas con el Enfoque Actual

1. **Problema de Múltiples Ejecuciones**: Estás ejecutando `PlaygroundWeb` múltiples veces para generar reportes de cobertura separados para diferentes módulos, lo cual es ineficiente.

2. **Preocupación de Escalabilidad**: Este enfoque no escalará bien con más módulos. Para un proyecto con 10 módulos, necesitarías 10 ejecuciones separadas.

3. **Fragmentación de Cobertura**: Los reportes por módulo dificultan obtener una vista holística de la cobertura en toda la aplicación.

## Estrategia Recomendada

### 1. Enfoque de Recolección de Cobertura Consolidada

En lugar de ejecutar la aplicación múltiples veces, recomiendo:

1. **Ejecutar la aplicación web una vez** con el agente JaCoCo conectado
2. **Ejecutar todas las pruebas de integración de Python** contra esta única instancia
3. **Generar un reporte de cobertura consolidado** que incluya todos los módulos

Este enfoque es más eficiente y proporciona una vista unificada de la cobertura en toda tu aplicación.

### 2. Pasos de Implementación

#### Modificaciones al POM Padre (`PlaygroundLib`)

Agregar un perfil para pruebas de integración con JaCoCo:

```xml
<profiles>
    <profile>
        <id>integration-test</id>
        <build>
            <plugins>
                <plugin>
                    <groupId>org.jacoco</groupId>
                    <artifactId>jacoco-maven-plugin</artifactId>
                    <executions>
                        <execution>
                            <id>merge</id>
                            <phase>post-integration-test</phase>
                            <goals>
                                <goal>merge</goal>
                            </goals>
                            <configuration>
                                <fileSets>
                                    <fileSet>
                                        <directory>${project.basedir}</directory>
                                        <includes>
                                            <include>*/target/jacoco-it.exec</include>
                                        </includes>
                                    </fileSet>
                                </fileSets>
                                <destFile>${project.build.directory}/jacoco-merged.exec</destFile>
                            </configuration>
                        </execution>
                        <execution>
                            <id>report-merged</id>
                            <phase>verify</phase>
                            <goals>
                                <goal>report</goal>
                            </goals>
                            <configuration>
                                <dataFile>${project.build.directory}/jacoco-merged.exec</dataFile>
                                <outputDirectory>${project.reporting.outputDirectory}/jacoco-merged</outputDirectory>
                            </configuration>
                        </execution>
                    </executions>
                </plugin>
            </plugins>
        </build>
    </profile>
</profiles>
```

#### Modificaciones al POM de PlaygroundWeb

Modificar la configuración del agente JaCoCo para incluir todos los módulos:

```xml
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
                    -javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${project.build.directory}/jacoco-it.exec,includes=org.lzw.*
                </jvmArgs>
                <!-- El resto de la configuración permanece igual -->
            </configuration>
        </execution>
        <!-- El resto de las ejecuciones permanece igual -->
    </executions>
</plugin>
```

Nota la adición de `includes=org.lzw.*` en la configuración del agente JaCoCo. Esto asegura que todas las clases en el paquete `org.lzw` (a través de todos los módulos) se incluyan en el reporte de cobertura.

### 3. Flujo de Ejecución

El flujo de ejecución recomendado sería:

```bash
# Construir todos los módulos
mvn clean install

# Ejecutar pruebas de integración con cobertura
mvn verify -Pintegration-test
```

Esto:
1. Compilará todos los módulos
2. Iniciará Jetty con el agente JaCoCo conectado
3. Ejecutará las pruebas de integración de Python
4. Detendrá Jetty
5. Generará un reporte de cobertura fusionado para todos los módulos

### 4. Escalando a Proyectos Más Grandes

Para un proyecto más grande con diez módulos:

1. **Módulos web** (como `PlaygroundWeb`) estarían configurados para ejecutar la aplicación con el agente JaCoCo conectado.
2. **Módulos de utilidad** (como `PlaygroundUtils`) no necesitarían configuración especial.
3. El POM padre manejaría la fusión de datos de cobertura de todos los módulos.

Si tienes múltiples módulos web que necesitan probarse independientemente, podrías crear perfiles Maven separados para cada módulo web y ejecutar pruebas de integración para cada uno por separado, luego fusionar todos los datos de cobertura a nivel del padre.

### 5. Abordando la Complejidad de JaCoCo

Para manejar la complejidad de JaCoCo:

1. **Encapsular la configuración** en perfiles Maven para mantener el POM principal limpio
2. **Documentar el proceso** claramente para que los miembros del equipo entiendan cómo ejecutar pruebas y generar reportes
3. **Considerar automatización CI/CD** para reducir la complejidad manual para desarrolladores

## Resumen

El enfoque recomendado consolida la recolección de cobertura ejecutando la aplicación web una vez con el agente JaCoCo conectado, ejecutando todas las pruebas de integración de Python contra esta instancia, y generando un reporte de cobertura consolidado. Este enfoque es más eficiente, escalable y proporciona una vista unificada de la cobertura en toda tu aplicación.

Esta estrategia debería resolver tus desafíos actuales y escalar bien a medida que tu proyecto crece, mientras también simplifica la gestión de la complejidad de JaCoCo.
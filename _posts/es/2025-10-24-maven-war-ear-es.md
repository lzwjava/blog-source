---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Configuración de Módulos WAR y EAR en Maven
translated: true
type: note
---

### Configuración de Proyecto Multi-Módulo Maven para WAR a EAR

En Maven, para que un módulo produzca un WAR (por ejemplo, una aplicación web) y otro módulo lo ensamble en un EAR (Enterprise Archive), se utiliza una estructura de proyecto multi-módulo. El módulo EAR depende del módulo WAR a través del `maven-ear-plugin`. Esto garantiza que el WAR se incluya en el EAR durante la construcción.

#### Paso 1: Crear el POM Padre
El POM padre define los módulos y gestiona las configuraciones compartidas. Establece su empaquetado como `pom`.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>parent</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>pom</packaging>

    <modules>
        <module>web-module</module>  <!-- Construir esto primero -->
        <module>ear-module</module>
    </modules>

    <!-- Opcional: Dependencias compartidas y versiones de plugins -->
    <dependencyManagement>
        <dependencies>
            <!-- Definir versiones para módulos hijos aquí -->
        </dependencies>
    </dependencyManagement>

    <build>
        <pluginManagement>
            <plugins>
                <!-- Gestionar versiones de plugins -->
                <plugin>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-ear-plugin</artifactId>
                    <version>3.3.0</version>
                </plugin>
            </plugins>
        </pluginManagement>
    </build>
</project>
```

#### Paso 2: Configurar el Módulo WAR
Este módulo construye la aplicación web como un WAR. Establece su empaquetado como `war`. No se necesita configuración especial de EAR aquí—solo necesita ser construido primero.

Estructura de directorio: `web-module/pom.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.example</groupId>
        <artifactId>parent</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>web-module</artifactId>
    <packaging>war</packaging>

    <dependencies>
        <!-- Añade tus dependencias web, ej., servlet-api -->
        <dependency>
            <groupId>javax.servlet</groupId>
            <artifactId>javax.servlet-api</artifactId>
            <version>4.0.1</version>
            <scope>provided</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-war-plugin</artifactId>
                <version>3.3.2</version>
            </plugin>
        </plugins>
    </build>
</project>
```

#### Paso 3: Configurar el Módulo EAR
Este módulo ensambla el EAR. Establece su empaquetado como `ear` y usa el `maven-ear-plugin` para referenciar el módulo WAR. El plugin tomará el artefacto WAR y lo empaquetará en el EAR.

Estructura de directorio: `ear-module/pom.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.example</groupId>
        <artifactId>parent</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>ear-module</artifactId>
    <packaging>ear</packaging>

    <dependencies>
        <!-- Depende del módulo WAR para incluirlo en la construcción -->
        <dependency>
            <groupId>com.example</groupId>
            <artifactId>web-module</artifactId>
            <version>${project.version}</version>
            <type>war</type>
        </dependency>
        <!-- Opcional: Añadir módulos EJB u otros si es necesario -->
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-ear-plugin</artifactId>
                <version>3.3.0</version>
                <configuration>
                    <!-- Versión EAR (ej., para Java EE) -->
                    <version>8</version>
                    
                    <!-- Directorio para librerías en EAR -->
                    <defaultLibBundleDir>lib</defaultLibBundleDir>
                    
                    <!-- WARs delgados (excluir dependencias ya en librerías EAR) -->
                    <skinnyWars>true</skinnyWars>
                    
                    <!-- Definir módulos a incluir -->
                    <modules>
                        <webModule>
                            <groupId>com.example</groupId>
                            <artifactId>web-module</artifactId>
                            <bundleDir>/</bundleDir>  <!-- Raíz del EAR -->
                            <contextRoot>/mywebapp</contextRoot>  <!-- Contexto de despliegue -->
                        </webModule>
                        <!-- Añadir más <ejbModule> o <jarModule> si es necesario -->
                    </modules>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

#### Paso 4: Construir el Proyecto
- Ejecuta desde el **directorio padre**: `mvn clean install`
  - Esto construye los módulos en orden (WAR primero, luego EAR).
- El EAR estará en `ear-module/target/ear-module-1.0-SNAPSHOT.ear`.
- Para construir solo el EAR (asumiendo que el WAR ya está construido): `cd ear-module && mvn clean package`.

#### Notas Clave
- **Orden de Construcción**: Lista el módulo WAR antes del EAR en los `<modules>` del padre para garantizar que Maven construya el WAR primero.
- **Dependencias**: La `<dependency>` del módulo EAR sobre el WAR garantiza que se resuelva durante el empaquetado.
- **Personalización**: Ajusta `<contextRoot>` para la ruta URL de la aplicación web. Añade más módulos (ej., JARs EJB) en `<modules>`.
- **Resolución de Problemas**: Si el WAR no se incluye, verifica que las coordenadas del artefacto coincidan exactamente. Usa `mvn dependency:tree` en el módulo EAR para verificar.

Para más detalles, consulta la documentación oficial del Maven EAR Plugin.

[Apache Maven EAR Plugin](https://maven.apache.org/plugins/maven-ear-plugin/)  
[Maven Multi-Module Projects](https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html#Multi-module_Projects)
---
audio: false
generated: true
lang: es
layout: post
title: Aplicación Java Servlet con Maven
translated: true
type: note
---

Aquí tienes una guía completa para crear y desplegar una aplicación simple de Servlet Java en WebSphere Liberty Profile (WLP) usando Maven para construir el proyecto y el plugin Liberty Maven para el despliegue. Este ejemplo crea un Servlet básico que devuelve "¡Hola Mundo!" cuando se accede a él, lo construye en un archivo WAR con Maven y lo despliega en WLP. Asumiremos que ya has configurado WLP con la característica `servlet-4.0` habilitada, ya que esta proporciona el soporte necesario para Servlets.

---

## Guía Paso a Paso

### 1. Crear la Estructura del Proyecto Maven
Comienza configurando una estructura estándar de aplicación web Maven. Puedes crearla manualmente o usar Maven para generarla.

- **Estructura de Directorios:**
  ```
  SimpleServletApp/
  ├── pom.xml
  └── src/
      └── main/
          ├── java/
          │   └── com/
          │       └── example/
          │           └── HelloServlet.java
          └── webapp/
              └── WEB-INF/
                  └── web.xml
  ```

- **Generar Opcionalmente con Maven:**
  Ejecuta este comando para crear la estructura, luego ajústala según sea necesario:
  ```bash
  mvn archetype:generate -DgroupId=com.example -DartifactId=simple-servlet-app -DarchetypeArtifactId=maven-archetype-webapp -DinteractiveMode=false
  ```
  Esto crea una estructura webapp básica, que modificarás en los siguientes pasos.

### 2. Escribir el Código del Servlet
Crea un archivo llamado `HelloServlet.java` en `src/main/java/com/example/` con el siguiente contenido:

```java
package com.example;

import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class HelloServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {
        resp.setContentType("text/plain");
        resp.getWriter().write("Hello World!");
    }
}
```

- **Explicación:** Este Servlet responde a las peticiones HTTP GET con "¡Hola Mundo!" en texto plano. Utiliza un método `doGet` simple y evita anotaciones para compatibilidad con la configuración explícita de `web.xml`.

### 3. Crear el Descriptor de Despliegue `web.xml`
Crea un archivo llamado `web.xml` en `src/main/webapp/WEB-INF/` con el siguiente contenido:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
         version="4.0">
    <servlet>
        <servlet-name>HelloServlet</servlet-name>
        <servlet-class>com.example.HelloServlet</servlet-class>
    </servlet>
    <servlet-mapping>
        <servlet-name>HelloServlet</servlet-name>
        <url-pattern>/hello</url-pattern>
    </servlet-mapping>
</web-app>
```

- **Explicación:** El archivo `web.xml` define la clase `HelloServlet` y la asigna al patrón de URL `/hello`. Esto es necesario ya que no estamos usando anotaciones `@WebServlet`.

### 4. Configurar el `pom.xml` de Maven
Crea o actualiza `pom.xml` en el directorio `SimpleServletApp/` con el siguiente contenido:

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>simple-servlet-app</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>war</packaging>

    <properties>
        <maven.compiler.source>1.8</maven.compiler.source>
        <maven.compiler.target>1.8</maven.compiler.target>
    </properties>

    <dependencies>
        <!-- Servlet API (proporcionado por WLP) -->
        <dependency>
            <groupId>javax.servlet</groupId>
            <artifactId>javax.servlet-api</artifactId>
            <version>4.0.1</version>
            <scope>provided</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <!-- Maven WAR Plugin para construir el archivo WAR -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-war-plugin</artifactId>
                <version>3.3.1</version>
                <configuration>
                    <finalName>myapp</finalName>
                </configuration>
            </plugin>
            <!-- Liberty Maven Plugin para el despliegue -->
            <plugin>
                <groupId>io.openliberty.tools</groupId>
                <artifactId>liberty-maven-plugin</artifactId>
                <version>3.3.4</version>
                <configuration>
                    <installDirectory>/opt/ibm/wlp</installDirectory>
                    <serverName>myServer</serverName>
                    <appsDirectory>dropins</appsDirectory>
                    <looseApplication>false</looseApplication>
                    <stripVersion>true</stripVersion>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

- **Explicación:**
  - **Coordenadas:** Define el proyecto con `groupId`, `artifactId` y `version`. El `packaging` está configurado como `war` para una aplicación web.
  - **Propiedades:** Establece Java 8 como la versión de origen y destino.
  - **Dependencias:** Incluye la API de Servlet con alcance `provided`, ya que es suministrada por WLP en tiempo de ejecución.
  - **Maven WAR Plugin:** Configura el nombre del archivo WAR como `myapp.war` usando `<finalName>`.
  - **Liberty Maven Plugin:** Configura el despliegue a un servidor Liberty en `/opt/ibm/wlp`, nombre del servidor `myServer`, desplegando en el directorio `dropins`.

### 5. Construir el Proyecto
Desde el directorio `SimpleServletApp/`, construye el archivo WAR usando Maven:

```bash
mvn clean package
```

- **Resultado:** Esto compila el Servlet, lo empaqueta con `web.xml` en `target/myapp.war` y lo prepara para el despliegue.

### 6. Desplegar y Ejecutar en WebSphere Liberty
Asegúrate de que tu servidor Liberty (`myServer`) esté configurado con la característica `servlet-4.0` habilitada. Verifica tu `server.xml` para:
```xml
<featureManager>
    <feature>servlet-4.0</feature>
</featureManager>
```

Despliega y ejecuta la aplicación usando el plugin Liberty Maven:

```bash
mvn liberty:run
```

- **Qué Sucede:**
  - Inicia el servidor Liberty en primer plano (si no se está ejecutando ya).
  - Despliega `myapp.war` en el directorio `dropins` automáticamente.
  - Mantiene el servidor ejecutándose hasta que se detenga.

- **Verificar el Despliegue:** Busca un mensaje de log como:
  ```
  [AUDIT   ] CWWKT0016I: Web application available (default_host): http://localhost:9080/myapp/
  ```
  Los logs típicamente están en `/opt/ibm/wlp/usr/servers/myServer/logs/console.log`.

### 7. Acceder a la Aplicación
Abre un navegador y navega a:

```
http://localhost:9080/myapp/hello
```

- **Salida Esperada:**
  ```
  Hello World!
  ```

- **Desglose de la URL:**
  - `9080`: Puerto HTTP por defecto para WLP.
  - `/myapp`: Raíz de contexto del nombre del archivo WAR (`myapp.war`).
  - `/hello`: Patrón de URL desde `web.xml`.

### 8. Detener el Servidor
Dado que `mvn liberty:run` ejecuta el servidor en primer plano, detenlo presionando `Ctrl+C` en la terminal.

---

## Notas
- **Prerrequisitos:**
  - Maven debe estar instalado y configurado en tu sistema.
  - Liberty debe estar instalado en `/opt/ibm/wlp`, y la instancia del servidor `myServer` debe existir. Ajusta `installDirectory` y `serverName` en `pom.xml` si tu configuración es diferente (por ejemplo, `/usr/local/wlp` o `defaultServer`).
  - La característica `servlet-4.0` debe estar habilitada en `server.xml`.

- **Despliegue Alternativo:**
  - Para construir y desplegar por separado:
    ```bash
    mvn clean package
    mvn liberty:deploy
    ```
    Inicia el servidor manualmente si es necesario:
    ```bash
    /opt/ibm/wlp/bin/server start myServer
    ```

- **Configuración de Puerto:** Si tu servidor Liberty usa un puerto HTTP diferente, verifica `<httpEndpoint>` en `server.xml` y ajusta la URL en consecuencia.

- **Raíz de Contexto:** Renombra `<finalName>` en `pom.xml` (por ejemplo, `<finalName>app</finalName>`) para cambiar la raíz de contexto a `/app`.

- **Solución de Problemas:**
  - Si el despliegue falla, verifica `installDirectory` y `serverName` en `pom.xml`.
  - Revisa los logs en `/opt/ibm/wlp/usr/servers/myServer/logs/messages.log` en busca de errores.
  - Asegúrate de que se use Java 8 o posterior, coincidiendo con la configuración de `maven.compiler`.

---

## Resumen
Esta guía demuestra cómo:
1. Configurar un proyecto Maven con un Servlet simple (`HelloServlet.java`) y `web.xml`.
2. Configurar `pom.xml` con la API de Servlet, el plugin Maven WAR y el plugin Liberty Maven.
3. Construir la aplicación en `myapp.war` usando `mvn clean package`.
4. Desplegarla y ejecutarla en WLP usando `mvn liberty:run`.
5. Acceder a "Hello World!" en `http://localhost:9080/myapp/hello`.

Esto proporciona un enfoque optimizado basado en Maven para desarrollar y desplegar una aplicación Servlet en WebSphere Liberty Profile.
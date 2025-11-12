---
audio: false
generated: true
lang: es
layout: post
title: Complemento Maven de Spring Boot
translated: true
type: note
---

Para utilizar el `spring-boot-maven-plugin` en un proyecto Spring Boot basado en Maven, siga estos pasos para configurar y utilizar el plugin para compilar, ejecutar y gestionar su aplicación. A continuación se presenta una guía completa:

---

### **1. Asegúrese de que su Proyecto es un Proyecto Spring Boot**
Antes de usar el `spring-boot-maven-plugin`, confirme que su proyecto está configurado como un proyecto Spring Boot. Esto normalmente implica:

- **Extender de `spring-boot-starter-parent` (Recomendado)**:
  - En su `pom.xml`, establezca `spring-boot-starter-parent` como el padre para gestionar las dependencias de Spring Boot y las versiones de los plugins.
  - Ejemplo:
    ```xml
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.5.4</version> <!-- Reemplace con su versión de Spring Boot -->
        <relativePath/> <!-- Buscar el padre desde el repositorio -->
    </parent>
    ```

- **Alternativamente, Usar el BOM `spring-boot-dependencies` (Bill of Materials)**:
  - Si no puede usar `spring-boot-starter-parent`, importe el BOM `spring-boot-dependencies` en la sección `dependencyManagement`.
  - Ejemplo:
    ```xml
    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-dependencies</artifactId>
                <version>2.5.4</version> <!-- Reemplace con su versión de Spring Boot -->
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>
    ```

Usar `spring-boot-starter-parent` es recomendable por su simplicidad, ya que gestiona automáticamente las versiones de los plugins.

---

### **2. Agregue el `spring-boot-maven-plugin` a su `pom.xml`**
Para usar el plugin, debe declararlo en la sección `<build><plugins>` de su `pom.xml`.

- **Si Usa `spring-boot-starter-parent`**:
  - Agregue el plugin sin especificar la versión, ya que está gestionada por el padre.
  - Ejemplo:
    ```xml
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
    ```

- **Si No Usa `spring-boot-starter-parent`**:
  - Especifique la versión explícitamente, coincidiendo con la versión de Spring Boot en uso.
  - Ejemplo:
    ```xml
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <version>2.5.4</version> <!-- Reemplace con su versión de Spring Boot -->
            </plugin>
        </plugins>
    </build>
    ```

---

### **3. Utilice los Goals del Plugin**
El `spring-boot-maven-plugin` proporciona varios goals para ayudar a compilar, ejecutar y gestionar su aplicación Spring Boot. A continuación se muestran los goals más comúnmente utilizados:

- **`spring-boot:run`**
  - Ejecuta su aplicación Spring Boot directamente desde Maven usando un servidor web embebido (ej. Tomcat).
  - Útil para desarrollo y testing.
  - Comando:
    ```
    mvn spring-boot:run
    ```

- **`spring-boot:repackage`**
  - Reempaqueta el archivo JAR o WAR generado por `mvn package` en un "fat JAR" o WAR ejecutable que incluye todas las dependencias.
  - Este goal se ejecuta automáticamente durante la fase `package` si el plugin está configurado.
  - Comando:
    ```
    mvn package
    ```
  - Después de ejecutarlo, puede iniciar la aplicación con:
    ```
    java -jar target/miaplicacion.jar
    ```

- **`spring-boot:start` y `spring-boot:stop`**
  - Se utilizan para pruebas de integración para iniciar y detener la aplicación durante las fases `pre-integration-test` y `post-integration-test`, respectivamente.
  - Ejemplo:
    ```
    mvn spring-boot:start
    mvn spring-boot:stop
    ```

- **`spring-boot:build-info`**
  - Genera un archivo `build-info.properties` que contiene información de compilación (ej. tiempo de compilación, versión).
  - Esta información puede ser accedida en su aplicación usando el bean `BuildProperties` de Spring Boot o anotaciones `@Value`.
  - Comando:
    ```
    mvn spring-boot:build-info
    ```

---

### **4. Personalice la Configuración del Plugin (Opcional)**
Puede personalizar el comportamiento del `spring-boot-maven-plugin` agregando opciones de configuración en el `pom.xml`. A continuación se muestran algunas personalizaciones comunes:

- **Especificar la Clase Principal**:
  - Si el plugin no puede detectar automáticamente la clase principal, especifíquela manualmente.
  - Ejemplo:
    ```xml
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <configuration>
                    <mainClass>com.example.MyApplication</mainClass>
                </configuration>
            </plugin>
        </plugins>
    </build>
    ```

- **Excluir Dependencias del Fat JAR**:
  - Excluya dependencias que son proporcionadas por el entorno de ejecución (ej. un contenedor de servlets externo).
  - Ejemplo:
    ```xml
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <configuration>
                    <excludes>
                        <exclude>
                            <groupId>com.example</groupId>
                            <artifactId>alguna-dependencia</artifactId>
                        </exclude>
                    </excludes>
                </configuration>
            </plugin>
        </plugins>
    </build>
    ```

- **Establecer Argumentos de la Aplicación**:
  - Configure argumentos para pasar a la aplicación cuando se ejecuta con `spring-boot:run`.
  - Ejemplo en `pom.xml`:
    ```xml
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <configuration>
                    <arguments>
                        <argument>--server.port=8081</argument>
                    </arguments>
                </configuration>
            </plugin>
        </plugins>
    </build>
    ```
  - Alternativamente, pase argumentos vía línea de comandos:
    ```
    mvn spring-boot:run -Dspring-boot.run.arguments=--server.port=8081
    ```

- **Construir Archivos WAR**:
  - Si construye un archivo WAR para despliegue en un contenedor de servlets externo, asegúrese de que el empaquetado de su proyecto esté establecido como `war` en `pom.xml`:
    ```xml
    <packaging>war</packaging>
    ```
  - También puede necesitar excluir contenedores de servlets embebidos (ej. Tomcat) si son proporcionados por el entorno. Agregue la siguiente dependencia como `provided`:
    ```xml
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-tomcat</artifactId>
            <scope>provided</scope>
        </dependency>
    </dependencies>
    ```

---

### **5. Notas Clave**
- **Comportamiento por Defecto**:
  - Cuando ejecuta `mvn package`, el plugin reempaqueta automáticamente el JAR/WAR durante la fase `package` para hacerlo ejecutable.
  - El artefacto reempaquetado es el artefacto principal, y el JAR/WAR original se adjunta con un clasificador (ej. `original`).

- **Flujo de Trabajo de Desarrollo**:
  - Use `mvn spring-boot:run` para desarrollo y testing rápidos.
  - Use `mvn package` para construir un JAR o WAR ejecutable desplegable.

- **Pruebas de Integración**:
  - Use `spring-boot:start` y `spring-boot:stop` para gestionar el ciclo de vida de la aplicación durante las pruebas de integración.

---

### **Resumen**
Para usar el `spring-boot-maven-plugin`:
1. Asegúrese de que su proyecto es un proyecto Spring Boot, típicamente extendiendo `spring-boot-starter-parent` o usando el BOM `spring-boot-dependencies`.
2. Agregue el plugin a la sección `<build><plugins>` de su `pom.xml`.
3. Use comandos de Maven como:
   - `mvn spring-boot:run` para ejecutar la aplicación.
   - `mvn package` para construir un JAR/WAR ejecutable.
   - Otros goals como `spring-boot:start`, `spring-boot:stop`, y `spring-boot:build-info` según sea necesario.
4. Opcionalmente, personalice la configuración del plugin en `pom.xml` para casos de uso avanzados.

Esta configuración le permite compilar, ejecutar y gestionar aplicaciones Spring Boot de manera eficiente usando Maven.
---
audio: false
generated: true
lang: es
layout: post
title: Ejecutar clases de Java con Maven Exec
translated: true
type: note
---

El objetivo `exec:java` del Maven Exec Plugin es una forma poderosa de ejecutar una clase Java con un método `main` directamente desde tu compilación de Maven. Ejecuta la clase Java especificada **dentro de la misma JVM** que tu compilación de Maven, utilizando las dependencias del proyecto como el classpath.

Aquí se explica cómo usarlo, con escenarios y ejemplos comunes:

## 1. Uso Básico desde la Línea de Comandos

La forma más simple de usar `exec:java` es directamente desde la línea de comandos, especialmente para pruebas rápidas o para ejecutar una clase de utilidad específica.

**Comando:**

```bash
mvn exec:java -Dexec.mainClass="com.yourcompany.YourMainClass"
```

**Explicación:**

*   `mvn exec:java`: Invoca el objetivo `java` del `exec-maven-plugin`.
*   `-Dexec.mainClass="com.yourcompany.YourMainClass"`: Esta propiedad del sistema especifica el nombre completo de la clase Java que contiene el método `public static void main(String[] args)` que deseas ejecutar.

**Ejemplo:**

Supongamos que tienes una clase `com.example.myapp.HelloWorld` con un método `main`:

```java
package com.example.myapp;

public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello from Maven exec:java!");
    }
}
```

La ejecutarías usando:

```bash
mvn compile exec:java -Dexec.mainClass="com.example.myapp.HelloWorld"
```

**Nota:** Es una buena práctica ejecutar `mvn compile` primero para asegurarse de que tus clases estén compiladas antes de que `exec:java` intente ejecutarlas.

## 2. Pasar Argumentos a tu Programa Java

Puedes pasar argumentos al método `main` de tu programa Java usando la propiedad del sistema `exec.args`:

**Comando:**

```bash
mvn exec:java -Dexec.mainClass="com.yourcompany.YourMainClass" -Dexec.args="arg1 arg2 \"arg with spaces\""
```

**Ejemplo:**

Si tu clase `HelloWorld` fuera:

```java
package com.example.myapp;

public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello from Maven exec:java!");
        if (args.length > 0) {
            System.out.println("Argumentos recibidos: ");
            for (String arg : args) {
                System.out.println("- " + arg);
            }
        }
    }
}
```

La ejecutarías así:

```bash
mvn compile exec:java -Dexec.mainClass="com.example.myapp.HelloWorld" -Dexec.args="FirstArgument SecondArgument"
```

Para argumentos con espacios, enciérralos entre comillas:

```bash
mvn compile exec:java -Dexec.mainClass="com.example.myapp.HelloWorld" -Dexec.args="\"Hello World\" AnotherArg"
```

## 3. Configurar `exec:java` en `pom.xml`

Para configuraciones más permanentes o predeterminadas, puedes agregar el `exec-maven-plugin` a tu `pom.xml`. Esto te permite definir un `mainClass` predeterminado y otros parámetros, para que no tengas que especificarlos en la línea de comandos cada vez.

**Configuración en `pom.xml`:**

```xml
<project>
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.yourcompany</groupId>
    <artifactId>my-maven-app</artifactId>
    <version>1.0-SNAPSHOT</modelVersion>

    <build>
        <plugins>
            <plugin>
                <groupId>org.codehaus.mojo</groupId>
                <artifactId>exec-maven-plugin</artifactId>
                <version>3.2.0</version> <executions>
                    <execution>
                        <goals>
                            <goal>java</goal>
                        </goals>
                    </execution>
                </executions>
                <configuration>
                    <mainClass>com.example.myapp.HelloWorld</mainClass>
                    <arguments>
                        <argument>defaultArg1</argument>
                        <argument>defaultArg2</argument>
                    </arguments>
                    <systemProperties>
                        <systemProperty>
                            <key>my.custom.property</key>
                            <value>someValue</value>
                        </systemProperty>
                    </systemProperties>
                </configuration>
            </plugin>
        </plugins>
    </build>

    <properties>
        <maven.compiler.source>11</maven.compiler.source>
        <maven.compiler.target>11</maven.compiler.target>
    </properties>

</project>
```

**Explicación de las opciones de configuración:**

*   `<groupId>org.codehaus.mojo</groupId>` y `<artifactId>exec-maven-plugin</artifactId>`: Coordenadas estándar para el plugin.
*   `<version>3.2.0</version>`: Especifica siempre una versión reciente del plugin.
*   `<goals><goal>java</goal></goals>`: Esto vincula el objetivo `java`. Si no lo vinculas a una fase específica, se ejecutará cuando llames explícitamente a `mvn exec:java`.
*   `<mainClass>com.example.myapp.HelloWorld</mainClass>`: Establece la clase principal predeterminada a ejecutar. Si ejecutas `mvn exec:java` sin `-Dexec.mainClass` en la línea de comandos, se usará esta clase.
*   `<arguments>`: Una lista de argumentos para pasar al método `main`. Estos son argumentos predeterminados que pueden ser anulados por `exec.args` en la línea de comandos.
*   `<systemProperties>`: Te permite definir propiedades del sistema (`-Dkey=value`) que estarán disponibles para tu aplicación Java cuando `exec:java` se ejecute.

**Ejecución con configuración en `pom.xml`:**

Una vez configurado en `pom.xml`:

*   Para ejecutar con la clase principal y los argumentos predeterminados:
    ```bash
    mvn compile exec:java
    ```
*   Para anular la clase principal desde la línea de comandos:
    ```bash
    mvn compile exec:java -Dexec.mainClass="com.example.myapp.AnotherMainClass"
    ```
*   Para anular/agregar argumentos desde la línea de comandos:
    ```bash
    mvn compile exec:java -Dexec.args="commandLineArg1 commandLineArg2"
    ```
    (Nota: `exec.args` típicamente *reemplazará* los `arguments` definidos en `pom.xml` si se proporciona en la línea de comandos).

## 4. Diferencias Clave con `exec:exec`

Es importante entender la distinción entre `exec:java` y `exec:exec`:

*   **`exec:java`**: Ejecuta el programa Java **en la misma JVM** que Maven. Esto es generalmente más rápido ya que evita generar un nuevo proceso. Configura automáticamente las dependencias del proyecto en el classpath.
*   **`exec:exec`**: Ejecuta un programa externo arbitrario (incluyendo `java` mismo) **en un proceso separado**. Esto es útil cuando necesitas especificar un ejecutable Java diferente, pasar argumentos de la JVM (como `-Xmx`), o ejecutar ejecutables que no son de Java. Si usas `exec:exec` para ejecutar un programa Java, típicamente tienes que construir manualmente el classpath usando `%classpath` en los argumentos.

Para la ejecución de aplicaciones Java estándar dentro de una compilación de Maven, `exec:java` es la opción más conveniente.

## 5. Consideraciones Importantes

*   **Classpath:** `exec:java` incluye automáticamente las clases compiladas de tu proyecto y sus dependencias en el classpath.
*   **Argumentos JVM:** Debido a que `exec:java` se ejecuta en la *misma* JVM que Maven, no puedes pasar argumentos JVM (como `-Xmx`, `-XX:MaxPermSize`) directamente a `exec:java` a través de su configuración o `exec.args`. Estos argumentos necesitan ser pasados a la JVM de Maven misma, típicamente a través de la variable de entorno `MAVEN_OPTS`:
    ```bash
    export MAVEN_OPTS="-Xmx1024m -Dsome.jvm.property=value"
    mvn exec:java ...
    ```
*   **System.exit():** Si tu programa Java llama a `System.exit()`, terminará todo el proceso de compilación de Maven, no solo tu programa. Ten esto en cuenta cuando uses `exec:java`. El plugin tiene una opción `blockSystemExit` (desde la versión 3.2.0) que intenta prevenir esto, pero es mejor diseñar tu método principal para que termine correctamente sin llamar a `System.exit()`.
*   **Dependencias:** `exec:java` depende de las dependencias del proyecto. Si necesitas ejecutar una clase desde una dependencia que no es parte de la compilación de tu proyecto, podrías necesitar ajustar la configuración del plugin o considerar usar `exec:exec` con una definición explícita del classpath.
*   **Versión del Plugin:** Usa siempre una versión reciente del `exec-maven-plugin` para obtener las últimas características y correcciones de errores. Consulta el sitio web de MojoHaus para obtener la información más actualizada.
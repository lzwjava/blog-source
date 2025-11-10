---
audio: false
generated: true
lang: es
layout: post
title: Redirección de Entrada en Programas Java de Maven
translated: true
type: note
---

Redirigir la entrada para programas `exec:java` puede ser un poco complicado porque `exec:java` ejecuta el proceso Java dentro *del mismo JVM* que Maven. Esto significa que no puedes usar los operadores de redirección estándar del shell (`<`, `>`) de la misma manera que lo harías para un proceso separado.

Sin embargo, aún tienes algunas opciones para proporcionar entrada a tu programa `exec:java`:

## 1. Entrada Programática (`System.in` estándar)

La forma más directa es diseñar tu programa Java para que lea desde `System.in` como es habitual. Cuando ejecutas `mvn exec:java`, lo que escribas en tu consola se dirigirá a `System.in` de tu programa Java.

**Ejemplo de Programa Java (`MyInputProgram.java`):**

```java
package com.example.app;

import java.util.Scanner;

public class MyInputProgram {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String name = scanner.nextLine();
        System.out.println("Hello, " + name + "!");

        System.out.print("Enter your age: ");
        int age = scanner.nextInt();
        System.out.println("You are " + age + " years old.");

        scanner.close();
    }
}
```

**Ejecución desde la línea de comandos:**

```bash
mvn compile exec:java -Dexec.mainClass="com.example.app.MyInputProgram"
```

Cuando ejecutes esto, Maven iniciará y luego tu programa te pedirá entrada. Escribes directamente en la consola.

## 2. Usar la propiedad `exec.args` para entrada (para casos simples)

Si tu programa espera una entrada muy simple y no interactiva, *podrías* pasarla como un argumento, y tu programa luego lee ese argumento en lugar de `System.in`. Esto no es una verdadera redirección de entrada estándar, pero sirve para un propósito similar con datos simples.

**Ejemplo de Programa Java (`MyArgProgram.java`):**

```java
package com.example.app;

public class MyArgProgram {
    public static void main(String[] args) {
        if (args.length > 0) {
            String inputData = args[0];
            System.out.println("Received input from argument: " + inputData);
        } else {
            System.out.println("No input argument provided.");
        }
    }
}
```

**Ejecución desde la línea de comandos:**

```bash
mvn compile exec:java -Dexec.mainClass="com.example.app.MyArgProgram" -Dexec.args="MyCustomInputString"
```

O con espacios:

```bash
mvn compile exec:java -Dexec.mainClass="com.example.app.MyArgProgram" -Dexec.args="\"Input with spaces\""
```

Este enfoque solo es adecuado si tu programa puede ser modificado para aceptar su "entrada" como argumentos de la línea de comandos.

## 3. Redirigir la entrada usando Redirección del Shell (con `exec:exec`)

Si absolutamente necesitas redirigir la entrada desde un archivo o una tubería, **debes** usar el objetivo `exec:exec` en lugar de `exec:java`. El objetivo `exec:exec` genera un proceso separado, lo que permite al shell manejar la redirección de entrada/salida estándar.

**Configuración en `pom.xml` para `exec:exec`:**

```xml
<project>
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.yourcompany</groupId>
    <artifactId>my-maven-app</artifactId>
    <version>1.0-SNAPSHOT</version>

    <build>
        <plugins>
            <plugin>
                <groupId>org.codehaus.mojo</groupId>
                <artifactId>exec-maven-plugin</artifactId>
                <version>3.2.0</version> <executions>
                    <execution>
                        <id>run-my-java-app</id>
                        <phase>package</phase> <goals>
                            <goal>exec</goal>
                        </goals>
                        <configuration>
                            <executable>java</executable>
                            <arguments>
                                <argument>-classpath</argument>
                                <classpath/> <argument>com.example.app.MyInputProgram</argument>
                                </arguments>
                            <workingDirectory>${project.build.directory}/classes</workingDirectory>
                            </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>

    <properties>
        <maven.compiler.source>11</maven.compiler.source>
        <maven.compiler.target>11</maven.compiler.target>
    </properties>

</project>
```

**Ejemplo de Programa Java (el mismo `MyInputProgram.java` de arriba):**

```java
package com.example.app;

import java.util.Scanner;

public class MyInputProgram {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String name = scanner.nextLine();
        System.out.println("Hello, " + name + "!");

        // Asumiendo que quieres leer otra línea para la edad después del nombre
        System.out.print("Enter your age: ");
        int age = scanner.nextInt();
        System.out.println("You are " + age + " years old.");

        scanner.close();
    }
}
```

**Archivo de Entrada (`input.txt`):**

```
Alice
30
```

**Ejecución con `exec:exec` y redirección de entrada:**

Primero, compila tu proyecto:

```bash
mvn compile
```

Luego, ejecuta el objetivo `exec:exec` y redirige la entrada usando tu shell:

```bash
mvn exec:exec@run-my-java-app < input.txt
```

**Explicación:**

  * `mvn exec:exec@run-my-java-app`: Ejecuta el objetivo `exec` del `exec-maven-plugin` con el `id` "run-my-java-app".
  * `< input.txt`: Este es un operador de redirección estándar del shell. Le dice a tu shell que tome el contenido de `input.txt` y lo alimente como entrada estándar al comando que se está ejecutando (`java com.example.app.MyInputProgram`).

**Notas Importantes para `exec:exec`:**

  * **`executable`:** Especificas explícitamente `java` como el ejecutable.
  * **`arguments`:** Necesitas construir los argumentos del comando `java` manualmente, incluyendo `-classpath` y la `mainClass`. La etiqueta `<classpath/>` es un valor especial que el `exec-maven-plugin` reemplaza con el classpath real calculado de tu proyecto.
  * **`workingDirectory`:** A menudo es útil establecer el `workingDirectory` en `${project.build.directory}/classes` para que Java pueda encontrar tus archivos `.class` compilados.
  * **`outputFile` (Opcional):** El `exec-maven-plugin` para `exec:exec` también proporciona una opción de configuración `<outputFile>` para redirigir la salida estándar y el error del programa a un archivo directamente dentro de la configuración del plugin, en lugar de depender de la redirección del shell. Esto puede ser útil para el registro de logs.

**En resumen:**

  * Para entrada interactiva donde un usuario escribe directamente, `exec:java` y `System.in` funcionan bien.
  * Para proporcionar entrada desde un archivo o una tubería, necesitarás cambiar a `exec:exec` y aprovechar las capacidades de redirección de entrada de tu shell (`<`).
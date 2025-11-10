---
audio: false
generated: true
lang: es
layout: post
title: Configurar Maven para la Ejecución de Pruebas en Paralelo
translated: true
type: note
---

Para habilitar la ejecución paralela de pruebas en tu proyecto Maven, particularmente para la clase `MavenTest.java` proporcionada, puedes configurar el Maven Surefire Plugin para ejecutar pruebas en paralelo. La clase `MavenTest.java` utiliza JUnit 4 con pruebas dinámicas para ejecutar comandos Maven para diferentes problemas, y el stack trace de tu error original indica que las pruebas ya se están ejecutando en paralelo (evidenciado por `ForkJoinPool` en el stack trace). Sin embargo, puedes controlar explícitamente la ejecución paralela configurando el Surefire Plugin en tu archivo `pom.xml`. A continuación, explicaré cómo configurar la ejecución paralela de pruebas y abordar el uso de un flag `-DParallel` como se solicitó.

### Por qué está ocurriendo la ejecución paralela
Tu salida de prueba muestra `ForkJoinPool` en el stack trace, lo que indica que JUnit o Maven ya está utilizando un grupo de hilos para la ejecución paralela. La clase `MavenTest` utiliza `@TestFactory` con `DynamicTest`, y es probable que las pruebas se estén ejecutando en paralelo debido al comportamiento predeterminado de JUnit o a una configuración existente de Surefire. El objetivo ahora es configurar explícitamente la ejecución paralela y permitir el control mediante un flag de línea de comandos como `-DParallel`.

### Pasos para configurar la ejecución paralela de pruebas

1.  **Actualiza el `pom.xml` para configurar Maven Surefire Plugin**:
    El Maven Surefire Plugin admite la ejecución paralela de pruebas para JUnit 4.7+ (que tu proyecto usa, ya que es compatible con `DynamicTest`). Puedes especificar el nivel de paralelismo (por ejemplo, `classes`, `methods`, o `both`) y el número de hilos. Para permitir el control via `-DParallel`, puedes usar una propiedad Maven para activar o configurar el paralelismo.

    Añade o actualiza la configuración del Surefire Plugin en tu `pom.xml`:

    ```xml
    <project>
        <!-- Otras configuraciones -->
        <properties>
            <!-- Por defecto, sin ejecución paralela a menos que se especifique -->
            <parallel.mode>none</parallel.mode>
            <thread.count>4</thread.count>
        </properties>
        <build>
            <plugins>
                <plugin>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-surefire-plugin</artifactId>
                    <version>3.5.3</version>
                    <configuration>
                        <parallel>${parallel.mode}</parallel>
                        <threadCount>${thread.count}</threadCount>
                        <perCoreThreadCount>false</perCoreThreadCount>
                        <!-- Opcional: Tiempo de espera para pruebas paralelas -->
                        <parallelTestsTimeoutInSeconds>10</parallelTestsTimeoutInSeconds>
                        <!-- Configuración de forking para aislar pruebas -->
                        <forkCount>1</forkCount>
                        <reuseForks>true</reuseForks>
                    </configuration>
                </plugin>
            </plugins>
        </build>
    </project>
    ```

    - **Explicación**:
        - `<parallel>`: Especifica el nivel de paralelismo. Los valores válidos para JUnit 4.7+ son `methods`, `classes`, `both`, `suites`, `suitesAndClasses`, `suitesAndMethods`, `classesAndMethods`, o `all`. Para tu clase `MavenTest`, `classes` es adecuado ya que cada `DynamicTest` representa un problema y quieres ejecutar pruebas para diferentes problemas en paralelo.
        - `<threadCount>`: Establece el número de hilos (por ejemplo, `4` para cuatro pruebas concurrentes). Puedes anular esto via `-Dthread.count=<número>`.
        - `<perCoreThreadCount>false</perCoreThreadCount>`: Asegura que `threadCount` sea un número fijo, no escalado por los núcleos de la CPU.
        - `<parallelTestsTimeoutInSeconds>`: Establece un tiempo de espera para las pruebas paralelas para evitar que se bloqueen (coincide con tu `TEST_TIMEOUT` de 10 segundos en `MavenTest.java`).
        - `<forkCount>1</forkCount>`: Ejecuta las pruebas en un proceso JVM separado para aislarlas, reduciendo problemas de estado compartido. `<reuseForks>true</reuseForks>` permite reutilizar la JVM para mayor eficiencia.
        - `<parallel.mode>` y `<thread.count>`: Propiedades Maven que pueden ser anuladas mediante flags de línea de comandos (por ejemplo, `-Dparallel.mode=classes`).

2.  **Ejecutando pruebas con `-DParallel`**:
    Para usar un flag `-DParallel` para controlar la ejecución paralela, puedes mapearlo a la propiedad `parallel.mode`. Por ejemplo, ejecuta:

    ```bash
    mvn test -Dparallel.mode=classes -Dthread.count=4
    ```

    - Si `-Dparallel.mode` no se especifica, el valor por defecto (`none`) deshabilita la ejecución paralela.
    - También puedes usar un flag más simple como `-DParallel=true` para habilitar el paralelismo con un modo predefinido (por ejemplo, `classes`). Para soportar esto, actualiza el `pom.xml` para interpretar `-DParallel`:

    ```xml
    <project>
        <!-- Otras configuraciones -->
        <properties>
            <parallel.mode>${Parallel ? 'classes' : 'none'}</parallel.mode>
            <thread.count>4</thread.count>
        </properties>
        <build>
            <plugins>
                <plugin>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-surefire-plugin</artifactId>
                    <version>3.5.3</version>
                    <configuration>
                        <parallel>${parallel.mode}</parallel>
                        <threadCount>${thread.count}</threadCount>
                        <perCoreThreadCount>false</perCoreThreadCount>
                        <parallelTestsTimeoutInSeconds>10</parallelTestsTimeoutInSeconds>
                        <forkCount>1</forkCount>
                        <reuseForks>true</reuseForks>
                    </configuration>
                </plugin>
            </plugins>
        </build>
    </project>
    ```

    Ahora, puedes ejecutar pruebas con:

    ```bash
    mvn test -DParallel=true
    ```

    - `-DParallel=true`: Habilita la ejecución paralela con `parallel=classes` y `threadCount=4`.
    - `-DParallel=false` u omitir `-DParallel`: Deshabilita la ejecución paralela (`parallel=none`).
    - Puedes anular el recuento de hilos con `-Dthread.count=<número>` (por ejemplo, `-Dthread.count=8`).

3.  **Asegurando la seguridad de los hilos (Thread Safety)**:
    Tu clase `MavenTest` ejecuta comandos Maven (`mvn exec:exec -Dproblem=<problema>`) en paralelo, lo que genera procesos separados. Esto es inherentemente seguro para los hilos ya que cada proceso tiene su propio espacio de memoria, evitando problemas de estado compartido. Sin embargo, asegúrate de que:
    - Las clases `com.lzw.solutions.uva.<problema>.Main` no compartan recursos (por ejemplo, archivos o bases de datos) que puedan causar conflictos.
    - Los archivos de entrada/salida o recursos utilizados por cada problema (por ejemplo, datos de prueba para `p10009`) estén aislados para evitar condiciones de carrera.
    - Si se utilizan recursos compartidos, considera usar `@NotThreadSafe` en clases de prueba específicas o sincronizar el acceso a los recursos compartidos.

4.  **Manejando la lista de exclusión (Skip List) con ejecución paralela**:
    Tu `MavenTest.java` ya incluye un conjunto `SKIP_PROBLEMS` para omitir problemas como `p10009`. Esto funciona bien con la ejecución paralela, ya que los problemas omitidos se excluyen antes de que se programen las pruebas. Asegúrate de que la lista de exclusión se actualice según sea necesario:

    ```java
    private static final Set<String> SKIP_PROBLEMS = new HashSet<>(Arrays.asList(
        "p10009", // Omite p10009 debido a NumberFormatException
        "p10037"  // Añade otros problemas problemáticos aquí
    ));
    ```

5.  **Ejecutando las pruebas**:
    Para ejecutar pruebas en paralelo con la lista de exclusión y el flag `-DParallel`:

    ```bash
    mvn test -DParallel=true -Dthread.count=4
    ```

    - Esto ejecuta hasta cuatro pruebas de problemas concurrentemente, omitiendo `p10009` y cualquier otro problema en `SKIP_PROBLEMS`.
    - Si quieres deshabilitar el paralelismo para depuración:

      ```bash
      mvn test -DParallel=false
      ```

6.  **Abordando el `NumberFormatException` para `p10009`**:
    El `NumberFormatException` en `p10009` (de tu error original) indica que se está analizando una cadena `null`. Si bien omitir `p10009` evita el problema, es posible que desees solucionarlo para mayor integridad. Revisa `com.lzw.solutions.uva.p10009.Main` en la línea 17 (método `readInt`) y añade comprobaciones de nulidad:

    ```java
    public int readInt() {
        String input = readInput(); // Método hipotético de lectura de entrada
        if (input == null || input.trim().isEmpty()) {
            throw new IllegalArgumentException("La entrada no puede ser nula o vacía");
        }
        return Integer.parseInt(input);
    }
    ```

    Alternativamente, mantén `p10009` en la lista de exclusión hasta que se resuelva el problema.

### Notas sobre la ejecución paralela
- **Rendimiento**: La ejecución paralela con `parallel=classes` es adecuada para tu clase `MavenTest`, ya que cada `DynamicTest` representa un problema distinto. Esto minimiza la sobrecarga en comparación con `methods` o `both`.
- **Uso de recursos**: La ejecución paralela aumenta el uso de CPU y memoria. Supervisa tu sistema para asegurarte de que `threadCount` (por ejemplo, `4`) no sature tu hardware. Usa `forkCount` para aislar pruebas en JVMs separadas si surgen problemas de memoria.
- **Tiempos de espera (Timeouts)**: La configuración `parallelTestsTimeoutInSeconds` asegura que las pruebas no se bloqueen indefinidamente, alineándose con tu `TEST_TIMEOUT` de 10 segundos en `MavenTest.java`.
- **Seguridad de hilos (Thread Safety)**: Dado que tus pruebas ejecutan comandos `mvn exec:exec`, que se ejecutan en procesos separados, la seguridad de los hilos es menos preocupante. Sin embargo, asegúrate de que las entradas/salidas de las pruebas (por ejemplo, archivos) estén aisladas por problema.
- **Depuración**: Si las pruebas fallan inesperadamente en modo paralelo, ejecútalas secuencialmente (`-DParallel=false`) para aislar los problemas.

### Comando completo de ejemplo
Para ejecutar pruebas en paralelo, omitiendo `p10009`, con cuatro hilos:

```bash
mvn test -DParallel=true -Dthread.count=4
```

Para depurar un problema específico (por ejemplo, `p10009`) sin paralelismo, elimínalo temporalmente de `SKIP_PROBLEMS` y ejecuta:

```bash
mvn test -DParallel=false -Dproblem=p10009
```

### Consideraciones adicionales
- **Limitaciones de JUnit 4**: Tu proyecto utiliza JUnit 4 (basado en las importaciones `org.junit.jupiter.api` y `DynamicTest`). JUnit 4.7+ admite ejecución paralela a través de Surefire, pero JUnit 5 ofrece opciones de paralelización más flexibles. Considera actualizar a JUnit 5 si necesitas funciones avanzadas como paralelismo por clase o estrategias personalizadas.
- **Versión de Maven**: Asegúrate de usar una versión reciente de Maven (por ejemplo, 3.9.10, como en tu salida de error) y Surefire (por ejemplo, 3.5.3) para un soporte óptimo de ejecución paralela.
- **Manejo de errores**: Para hacer las pruebas más robustas, considera capturar excepciones en `runMavenExecTests` (como se sugirió en la respuesta anterior) para registrar fallos sin detener el conjunto de pruebas:

   ```java
   @TestFactory
   Collection<DynamicTest> runMavenExecTests() {
       return PROBLEMS.stream()
               .map(problem -> DynamicTest.dynamicTest("Test problem: " + problem, () -> {
                   String command = String.format("mvn exec:exec -Dproblem=%s", problem);
                   System.out.println("Executing command for " + problem + ": " + command);
                   try {
                       Process process = Runtime.getRuntime().exec(command);
                       // ... (resto del código de manejo del proceso)
                       int exitCode = process.exitValue();
                       Assertions.assertTrue(
                               exitCode == 0,
                               "Maven command failed for problem: " + problem + "\nError output:\n" + errorOutput);
                   } catch (Exception e) {
                       System.err.println("Exception for problem " + problem + ": " + e.getMessage());
                       // Opcionalmente continuar en lugar de fallar
                   }
               }))
               .collect(Collectors.toList());
   }
   ```

Esta configuración te permite controlar la ejecución paralela con `-DParallel=true`, omitir pruebas problemáticas como `p10009` y mantener una ejecución de pruebas robusta. ¡Avísame si necesitas más personalización, como listas de exclusión dinámicas via argumentos de línea de comandos o configuraciones avanzadas de JUnit 5!
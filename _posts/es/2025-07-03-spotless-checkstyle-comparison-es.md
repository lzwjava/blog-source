---
audio: false
generated: true
lang: es
layout: post
title: Spotless frente a Checkstyle en Java
translated: true
type: note
---

Puedes usar el **Spotless Maven Plugin** y el **Checkstyle Maven Plugin** juntos en un proyecto Java, ya que cumplen propósitos complementarios. Sin embargo, si *necesitas* ambos depende de los requisitos de tu proyecto. A continuación, explicaré cómo pueden trabajar juntos, sus diferencias y cuándo podrías elegir uno sobre el otro.

### Diferencias Clave Entre Spotless y Checkstyle

| **Aspecto**           | **Spotless**                                                                 | **Checkstyle**                                                              |
|-----------------------|------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| **Propósito**         | Formatea automáticamente el código para imponer un estilo consistente y corrige problemas. | Analiza estáticamente el código para hacer cumplir estándares de codificación y detectar violaciones. |
| **Acción**            | Modifica el código (ej., corrige indentación, orden de imports, elimina imports no usados). | Reporta violaciones sin modificar el código; falla la build si las verificaciones fallan. |
| **Configuración**     | Configura formateadores como `palantir-java-format`, `google-java-format`, etc. | Utiliza un conjunto de reglas (ej., verificaciones Google o Sun) para definir estándares de codificación. |
| **Salida**            | Archivos fuente formateados (con `mvn spotless:apply`).                      | Reportes (XML, HTML o consola) que enumeran las violaciones de estilo.      |
| **Caso de Uso**       | Asegura que el código esté formateado consistentemente antes de commits o builds. | Hace cumplir estándares de codificación y detecta problemas como complejidad o malas prácticas. |

### Usando Spotless y Checkstyle Juntos

Puedes combinar Spotless y Checkstyle para lograr tanto el **formateo automático** como la **aplicación de estilo**. Así es como se complementan:

1.  **Spotless para Formateo**:
    - Spotless aplica reglas de formato (ej., indentación, orden de imports) usando herramientas como `palantir-java-format`.
    - Asegura que el código esté formateado consistentemente, reduciendo el esfuerzo manual.
    - Ejemplo: Corrige indentación de 2 espacios vs. 4 espacios, ordena imports y elimina imports no utilizados.

2.  **Checkstyle para Validación**:
    - Checkstyle hace cumplir estándares de codificación más allá del formato, como longitud de métodos, convenciones de nomenclatura o complejidad.
    - Detecta problemas que los formateadores podrían no abordar, como Javadoc faltante o métodos excesivamente complejos.
    - Ejemplo: Señala un método con demasiados parámetros o exige Javadoc en métodos públicos.

3.  **Flujo de Trabajo**:
    - Ejecuta Spotless primero (`mvn spotless:apply`) para formatear el código.
    - Luego ejecuta Checkstyle (`mvn checkstyle:check`) para verificar el cumplimiento de reglas adicionales.
    - Esto asegura que el código esté tanto formateado como que se adhiera a pautas de estilo más amplias.

### Ejemplo de Configuración en `pom.xml`

Así es como puedes configurar ambos plugins en tu `pom.xml`:

```xml
<build>
    <plugins>
        <!-- Spotless Plugin para Formateo -->
        <plugin>
            <groupId>com.diffplug.spotless</groupId>
            <artifactId>spotless-maven-plugin</artifactId>
            <version>2.43.0</version>
            <configuration>
                <java>
                    <includes>
                        <include>src/main/java/**/*.java</include>
                        <include>src/test/java/**/*.java</include>
                    </includes>
                    <palantirJavaFormat>
                        <version>2.53.0</version>
                        <style>GOOGLE</style> <!-- Usar estilo Google -->
                    </palantirJavaFormat>
                    <indent>
                        <spacesPerTab>2</spacesPerTab> <!-- Indentación de 2 espacios -->
                    </indent>
                    <importOrder>
                        <order>java,javax,org,com,\\#</order>
                    </importOrder>
                    <removeUnusedImports/>
                    <trimTrailingWhitespace/>
                    <endWithNewline/>
                </java>
            </configuration>
            <executions>
                <execution>
                    <goals>
                        <goal>apply</goal>
                    </goals>
                    <phase>validate</phase>
                </execution>
            </executions>
        </plugin>

        <!-- Checkstyle Plugin para Validación -->
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-checkstyle-plugin</artifactId>
            <version>3.4.0</version>
            <configuration>
                <configLocation>google_checks.xml</configLocation> <!-- Usar estilo Google o XML personalizado -->
                <includeTestSourceDirectory>true</includeTestSourceDirectory>
                <failOnViolation>true</failOnViolation> <!-- Fallar la build por violaciones -->
                <consoleOutput>true</consoleOutput> <!-- Mostrar violaciones en consola -->
            </configuration>
            <executions>
                <execution>
                    <goals>
                        <goal>check</goal>
                    </goals>
                    <phase>validate</phase>
                </execution>
            </executions>
            <dependencies>
                <!-- Especificar versión de Checkstyle -->
                <dependency>
                    <groupId>com.puppycrawl.tools</groupId>
                    <artifactId>checkstyle</artifactId>
                    <version>10.17.0</version>
                </dependency>
            </dependencies>
        </plugin>
    </plugins>
</build>
```

### Notas Clave de Configuración

1.  **Reglas de Estilo Compartidas**:
    - Para evitar conflictos, alinea las configuraciones de Spotless y Checkstyle. Por ejemplo, usa `palantirJavaFormat` con `style>GOOGLE` en Spotless y `google_checks.xml` en Checkstyle.
    - Descarga `google_checks.xml` desde el [GitHub de Checkstyle](https://github.com/checkstyle/checkstyle/blob/master/src/main/resources/google_checks.xml) o crea un conjunto de reglas personalizado.

2.  **Orden de Ejecución**:
    - Ejecuta Spotless antes que Checkstyle en la fase `validate` para asegurar que el código esté formateado antes de la validación.
    - Ejemplo: `mvn spotless:apply checkstyle:check`.

3.  **Reglas Personalizadas de Checkstyle**:
    - Personaliza `google_checks.xml` o crea la tuya propia (ej., `my_checks.xml`) para hacer cumplir reglas específicas, como:
      ```xml
      <module name="Indentation">
          <property name="basicOffset" value="2"/>
          <property name="lineWrappingIndentation" value="4"/>
      </module>
      <module name="ImportOrder">
          <property name="groups" value="java,javax,org,com"/>
          <property name="ordered" value="true"/>
          <property name="separated" value="true"/>
      </module>
      ```

4.  **Evitar Redundancia**:
    - Si Spotless maneja el formateo (ej., indentación, orden de imports), deshabilita las reglas superpuestas de Checkstyle para evitar verificaciones duplicadas. Por ejemplo, deshabilita el módulo `Indentation` de Checkstyle si Spotless aplica la indentación:
      ```xml
      <module name="Indentation">
          <property name="severity" value="ignore"/>
      </module>
      ```

### Cuándo Usar Uno vs. Ambos

-   **Usar Solo Spotless**:
    - Si solo necesitas un formateo de código consistente (ej., indentación, orden de imports, espacios en blanco).
    - Ideal para equipos que quieren formateo automático sin una aplicación estricta de estilo.
    - Ejemplo: Proyectos pequeños o equipos con formateo basado en IDE.

-   **Usar Solo Checkstyle**:
    - Si necesitas hacer cumplir estándares de codificación (ej., convenciones de nomenclatura, Javadoc, complejidad de métodos) sin modificar el código.
    - Adecuado para proyectos donde los desarrolladores formatean el código manualmente pero necesitan validación.

-   **Usar Ambos**:
    - Para una calidad de código robusta: Spotless formatea el código automáticamente, y Checkstyle detecta problemas adicionales (ej., Javadoc faltante, métodos complejos).
    - Común en equipos grandes o proyectos con estándares de codificación estrictos.
    - Ejemplo: Proyectos empresariales o repositorios de código abierto que requieren estilo consistente y verificaciones de calidad.

### Consideraciones Prácticas

-   **Rendimiento**: Ejecutar ambos plugins aumenta el tiempo de build. Usa `spotless:check` (en lugar de `apply`) y `checkstyle:check` en pipelines de CI para validar sin modificar el código.
-   **Integración con el IDE**:
    - Spotless: Usa las tareas Spotless Gradle/Maven o plugins del IDE (ej., `palantir-java-format` para IntelliJ).
    - Checkstyle: Usa el plugin Checkstyle-IDEA para IntelliJ o el plugin Eclipse Checkstyle, configurado con el mismo `google_checks.xml`.
-   **CI/CD**: Configura ambos plugins en tu pipeline de CI (ej., Jenkins, GitHub Actions) para hacer cumplir el formateo y las verificaciones de estilo en pull requests.
    ```yaml
    # Ejemplo de workflow de GitHub Actions
    name: CI
    on: [pull_request]
    jobs:
      build:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v3
          - name: Set up JDK 17
            uses: actions/setup-java@v3
            with: { java-version: '17' }
          - name: Run Spotless and Checkstyle
            run: mvn spotless:check checkstyle:check
    ```

### Posibles Conflictos y Soluciones

-   **Reglas Superpuestas**: Si Spotless formatea el código de manera diferente a las reglas de Checkstyle (ej., indentación de 2 espacios vs. 4 espacios), las builds pueden fallar. Solución: Alinea las configuraciones (ej., usa estilo `GOOGLE` para ambos).
-   **Fallos de Build**: El `failOnViolation` de Checkstyle puede romper builds si Spotless no se ha ejecutado. Solución: Asegúrate de que Spotless se ejecute primero o usa `spotless:check` para validar el formateo.
-   **Adopción del Equipo**: Los desarrolladores pueden resistirse al formateo automático. Solución: Usa `spotless:check` en CI y educa al equipo sobre la integración con el IDE.

### Fuentes

-   Documentación de Spotless: [GitHub](https://github.com/diffplug/spotless/tree/main/plugin-maven)
-   Maven Checkstyle Plugin: [Sitio de Maven](https://maven.apache.org/plugins/maven-checkstyle-plugin/)
-   Discusiones comunitarias en Stack Overflow y GitHub issues

### Conclusión

Usar Spotless y Checkstyle juntos es una combinación poderosa para mantener la calidad del código: Spotless asegura un formateo consistente, mientras que Checkstyle hace cumplir estándares de codificación más amplios. Configúralos para que estén alineados (ej., mismas reglas de indentación y orden de imports) y ejecútalos secuencialmente en tu proceso de build. Si tu proyecto solo necesita formateo, Spotless por sí mismo puede ser suficiente; si necesitas una validación estricta, considera añadir Checkstyle. ¡Déjame saber si necesitas ayuda con configuraciones específicas o un archivo de ejemplo `google_checks.xml`
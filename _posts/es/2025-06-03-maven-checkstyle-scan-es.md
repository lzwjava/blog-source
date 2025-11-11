---
audio: false
generated: true
lang: es
layout: post
title: 'Verificación de Estilo Maven: Continuar Escaneo'
translated: true
type: note
---

Para que `mvn checkstyle:check` continúe escaneando todos los módulos sin fallar prematuramente ante violaciones, necesitas configurar el plugin Checkstyle de Maven para deshabilitar la opción `failOnViolation`. Por defecto, `failOnViolation` está establecido en `true`, lo que hace que la construcción se detenga tan pronto como se encuentren violaciones. Establecerlo en `false` permite que el escaneo se complete en todos los módulos, reportando todas las violaciones sin detener la construcción.

### Solución
Actualiza tu `pom.xml` para configurar el plugin Checkstyle de la siguiente manera:

```xml
<build>
  <plugins>
    <plugin>
      <groupId>org.apache.maven.plugins</groupId>
      <artifactId>maven-checkstyle-plugin</artifactId>
      <version>3.3.1</version> <!-- Usa la versión más reciente -->
      <configuration>
        <failOnViolation>false</failOnViolation>
        <logViolationsToConsole>true</logViolationsToConsole> <!-- Opcional: Registra las violaciones en la consola -->
      </configuration>
      <executions>
        <execution>
          <id>checkstyle</id>
          <phase>validate</phase> <!-- O tu fase preferida -->
          <goals>
            <goal>check</goal>
          </goals>
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

### Explicación
- **`<failOnViolation>false</failOnViolation>`**: Esta configuración evita que la construcción falle cuando se detectan violaciones de Checkstyle, permitiendo que el escaneo continúe en todos los módulos.
- **`<logViolationsToConsole>true</logViolationsToConsole>`**: (Opcional) Asegura que las violaciones se impriman en la consola para mayor visibilidad, incluso si la construcción no falla.
- **Fase de Ejecución**: El `<phase>validate</phase>` vincula la verificación de Checkstyle a la fase `validate` del ciclo de vida de Maven. Ajusta la fase (por ejemplo, `compile`, `verify`) si deseas que se ejecute en una etapa diferente.

### Ejecutando el Comando
Ejecuta el comando nuevamente:
```bash
mvn checkstyle:check
```
Con `failOnViolation` establecido en `false`, Maven escaneará todos los módulos, reportará todas las violaciones y completará la construcción sin detenerse prematuramente.

### Notas
- Asegúrate de usar una versión reciente del `maven-checkstyle-plugin` (por ejemplo, 3.3.1 como se muestra). Verifica la versión más reciente en Maven Central si es necesario.
- Si estás trabajando en un proyecto multi-módulo, esta configuración se aplica a todos los módulos a menos que se sobrescriba en un `pom.xml` hijo.
- Para generar un reporte de violaciones, considera ejecutar `mvn checkstyle:checkstyle` en su lugar, que produce un reporte HTML sin fallar la construcción por defecto.

Si tienes requisitos específicos (por ejemplo, reglas personalizadas de Checkstyle o una configuración diferente), ¡házmelo saber y puedo adaptar la solución aún más!
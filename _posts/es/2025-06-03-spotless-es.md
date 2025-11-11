---
audio: false
generated: true
lang: es
layout: post
title: Usar Spotless para Formatear Código
translated: true
type: note
---

No existe un comando `mvn checkstyle:format` en el Maven Checkstyle Plugin. El plugin está diseñado principalmente para verificar el código contra una configuración de Checkstyle e informar violaciones, no para formatear código automáticamente. Sin embargo, puedes lograr el formateo de código basado en una configuración de Checkstyle usando otras herramientas como Spotless o el Maven Formatter Plugin, que pueden configurarse para alinearse con tus reglas de Checkstyle.

A continuación, explicaré cómo formatear código basado en tu configuración de Checkstyle usando el **Spotless Maven Plugin**, ya que es una opción popular para este propósito y puede integrarse con reglas de Checkstyle.

### Solución: Usar Spotless con Configuración de Checkstyle

El Spotless Maven Plugin puede formatear código Java de acuerdo con un archivo de configuración de Checkstyle (por ejemplo, `checkstyle.xml`). Así es como puedes configurarlo:

#### 1. Agregar Spotless a tu `pom.xml`
Agrega el plugin Spotless a tu `pom.xml` y configúralo para usar tu archivo de configuración de Checkstyle.

```xml
<build>
  <plugins>
    <plugin>
      <groupId>com.diffplug.spotless</groupId>
      <artifactId>spotless-maven-plugin</artifactId>
      <version>2.43.0</version> <!-- Usa la versión más reciente -->
      <configuration>
        <java>
          <!-- Apunta a tu archivo de configuración de Checkstyle -->
          <googleJavaFormat>
            <version>1.22.0</version> <!-- Opcional: Usa una versión específica -->
            <style>GOOGLE</style> <!-- O AOSP, u omitir para el valor por defecto -->
          </googleJavaFormat>
          <formatAnnotations>
            <!-- Usa la configuración de Checkstyle para el formateo -->
            <checkstyle>
              <file>${project.basedir}/checkstyle.xml</file> <!-- Ruta a tu configuración de Checkstyle -->
              <version>10.17.0</version> <!-- Coincide con tu versión de Checkstyle -->
            </checkstyle>
          </formatAnnotations>
        </java>
      </configuration>
      <executions>
        <execution>
          <goals>
            <goal>apply</goal> <!-- Formatea el código automáticamente -->
          </goals>
          <phase>process-sources</phase> <!-- Opcional: Vincular a una fase -->
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

#### 2. Asegúrate de que tu Configuración de Checkstyle Exista
Asegúrate de tener un archivo `checkstyle.xml` en tu proyecto (por ejemplo, en el directorio raíz o en un subdirectorio). Este archivo define los estándares de codificación (por ejemplo, indentación, espacios en blanco, etc.) que Spotless usará para formatear tu código. Si estás usando un estándar como Google Java Format, puedes hacer referencia a él, o usar una configuración de Checkstyle personalizada adaptada a tu proyecto.

Ejemplo de fragmento de `checkstyle.xml` para reglas básicas de formateo:
```xml
<?xml version="1.0"?>
<!DOCTYPE module PUBLIC "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN" "https://checkstyle.sourceforge.io/dtds/configuration_1_3.dtd">
<module name="Checker">
  <module name="TreeWalker">
    <module name="Indentation">
      <property name="basicOffset" value="2"/>
      <property name="braceAdjustment" value="0"/>
    </module>
  </module>
</module>
```

#### 3. Ejecuta Spotless para Formatear el Código
Para formatear tu código basado en la configuración de Checkstyle, ejecuta:
```bash
mvn spotless:apply
```

Este comando formateará todos los archivos Java en tu proyecto de acuerdo con las reglas definidas en tu configuración de Checkstyle y cualquier configuración de formateo adicional (por ejemplo, Google Java Format).

#### 4. Verifica el Formateo con Checkstyle
Después del formateo, puedes ejecutar `mvn checkstyle:check` para verificar que el código formateado cumple con tus reglas de Checkstyle. Si seguiste el consejo anterior de establecer `<failOnViolation>false</failOnViolation>`, informará cualquier violación restante sin detener la build.

### Alternativa: Maven Formatter Plugin
Si prefieres no usar Spotless, puedes usar el **Maven Formatter Plugin**, que también admite el formateo basado en reglas pero se usa menos comúnmente con configuraciones de Checkstyle directamente. Aquí hay una configuración básica:

```xml
<build>
  <plugins>
    <plugin>
      <groupId>net.revelc.code.formatter</groupId>
      <artifactId>formatter-maven-plugin</artifactId>
      <version>2.23.0</version> <!-- Usa la versión más reciente -->
      <configuration>
        <configFile>${project.basedir}/checkstyle.xml</configFile> <!-- Ruta a la configuración de Checkstyle -->
      </configuration>
      <executions>
        <execution>
          <goals>
            <goal>format</goal>
          </goals>
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

Ejecuta el formateo con:
```bash
mvn formatter:format
```

### Notas
- **No Hay Comando Directo de Formateo en Checkstyle**: El Maven Checkstyle Plugin no proporciona un objetivo `format`. Se necesitan herramientas como Spotless o el Formatter Plugin para aplicar el formateo basado en reglas de Checkstyle.
- **Compatibilidad de Versiones de Checkstyle**: Asegúrate de que la versión de Checkstyle especificada en Spotless (o Formatter) coincida con la versión utilizada en tu plugin de Checkstyle para evitar discrepancias en las reglas.
- **Reglas Personalizadas de Checkstyle**: Tu `checkstyle.xml` debe incluir reglas relacionadas con el formateo (por ejemplo, `Indentation`, `WhitespaceAround`, etc.) para que Spotless las aplique correctamente.
- **Proyectos Multi-Módulo**: En un proyecto Maven multi-módulo, puedes colocar la configuración de Spotless/Formatter en el `pom.xml` padre para aplicarla en todos los módulos, o configurarla por módulo según sea necesario.
- **Verificar Después del Formateo**: Siempre ejecuta `mvn checkstyle:check` después del formateo para confirmar el cumplimiento, especialmente si tienes reglas que no son de formateo (por ejemplo, longitud de métodos, complejidad) en tu configuración de Checkstyle.

Si no tienes un `checkstyle.xml` o necesitas ayuda para crear uno, ¡avísame y puedo proporcionar una muestra o guiarte más! Además, si prefieres una herramienta diferente o tienes requisitos de formateo específicos, compártelos y ajustaré la solución.
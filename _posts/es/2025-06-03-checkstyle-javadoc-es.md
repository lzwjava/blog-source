---
audio: false
generated: true
lang: es
layout: post
title: Deshabilitar las comprobaciones de Javadoc en Checkstyle
translated: true
type: note
---

Para configurar Checkstyle para ignorar todas las verificaciones relacionadas con Javadoc y tratarlas como infracciones, necesitas modificar tu archivo de configuración de Checkstyle (normalmente `checkstyle.xml`) para deshabilitar o suprimir los módulos relacionados con Javadoc. Aquí te explicamos cómo puedes hacerlo:

### Opción 1: Deshabilitar las verificaciones relacionadas con Javadoc
Checkstyle tiene varios módulos relacionados con Javadoc, como `JavadocMethod`, `JavadocType`, `JavadocVariable`, `JavadocStyle` y `JavadocPackage`. Para deshabilitarlos, asegúrate de que estos módulos estén eliminados o comentados en tu archivo de configuración. Por ejemplo:

```xml
<module name="Checker">
    <!-- Otros módulos -->
    <!-- Comenta o elimina las verificaciones relacionadas con Javadoc -->
    <!--
    <module name="JavadocMethod"/>
    <module name="JavadocType"/>
    <module name="JavadocVariable"/>
    <module name="JavadocStyle"/>
    <module name="JavadocPackage"/>
    -->
</module>
```

Si estos módulos no están presentes en tu configuración, Checkstyle no aplicará las verificaciones de Javadoc.

### Opción 2: Suprimir verificaciones de Javadoc usando filtros de supresión
Puedes usar el `SuppressionFilter` de Checkstyle para suprimir todas las verificaciones relacionadas con Javadoc en tu base de código. Añade una regla de supresión a un archivo de supresiones separado (por ejemplo, `suppressions.xml`) y refiérelo en tu configuración de Checkstyle.

1. **Crea un archivo de supresiones** (por ejemplo, `suppressions.xml`):
   ```xml
   <!DOCTYPE suppressions PUBLIC
       "-//Checkstyle//DTD Suppression DTD 1.0//EN"
       "https://checkstyle.org/dtds/suppressions_1_0.dtd">
   <suppressions>
       <!-- Suprime todas las verificaciones relacionadas con Javadoc -->
       <suppress checks="Javadoc.*" files=".*"/>
   </suppressions>
   ```

   El patrón `checks="Javadoc.*"` coincide con todas las verificaciones que comienzan con "Javadoc" (por ejemplo, `JavadocMethod`, `JavadocType`, etc.), y `files=".*"` aplica la supresión a todos los archivos.

2. **Referencia el archivo de supresiones en tu configuración de Checkstyle**:
   ```xml
   <module name="Checker">
       <module name="SuppressionFilter">
           <property name="file" value="suppressions.xml"/>
       </module>
       <!-- Otros módulos -->
   </module>
   ```

### Opción 3: Usar anotaciones `@SuppressWarnings`
Si deseas suprimir las verificaciones de Javadoc para clases o métodos específicos, puedes usar la anotación `@SuppressWarnings("checkstyle:javadoc")` en tu código Java. Por ejemplo:

```java
@SuppressWarnings("checkstyle:javadoc")
public class MyClass {
    // El código sin Javadoc no activará violaciones
}
```

Este enfoque es útil para una supresión dirigida, pero requiere añadir anotaciones al código, lo que puede no ser ideal para deshabilitar las verificaciones de Javadoc de forma global.

### Notas
- **Verifica tu configuración**: Después de modificar la configuración, ejecuta Checkstyle para asegurarte de que las violaciones relacionadas con Javadoc ya no se reporten. Por ejemplo, usa el comando:
  ```bash
  java -jar checkstyle.jar -c checkstyle.xml TusArchivosFuente
  ```
- **Módulos comunes de Javadoc**: Asegúrate de abordar todos los módulos relevantes, incluyendo `JavadocMethod`, `JavadocType`, `JavadocVariable`, `JavadocStyle`, `JavadocPackage`, `MissingJavadocMethod`, `MissingJavadocType` e `InvalidJavadocPosition`.
- **Versión de Checkstyle**: Los nombres exactos de los módulos y la sintaxis de supresión pueden variar ligeramente según tu versión de Checkstyle. Los ejemplos anteriores son compatibles con Checkstyle 8.x y versiones posteriores.
- **Supresión global**: El enfoque de `SuppressionFilter` (Opción 2) es típicamente la forma más limpia de deshabilitar todas las verificaciones de Javadoc sin modificar extensivamente la configuración central.

Si estás usando una herramienta de construcción específica como Maven o Gradle, ¡házmelo saber y puedo proporcionarte orientación adicional sobre cómo integrar la configuración actualizada de Checkstyle!
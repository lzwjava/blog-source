---
audio: false
generated: true
lang: es
layout: post
title: Ubicación de la Configuración de Checkstyle
translated: true
type: note
---

Para solucionar los problemas que estás experimentando con el `maven-checkstyle-plugin` al ejecutar `mvn clean checkstyle:check`, donde no puede encontrar el archivo `checks.xml` y falla al inicializar el módulo `SuppressWithNearbyTextFilter`, sigue estos pasos. Los problemas provienen de la ubicación del archivo y de una versión incompatible de Checkstyle. Aquí tienes una solución completa:

---

### Paso 1: Corregir la Ubicación del Archivo `checks.xml`
El error indica que el plugin no puede encontrar `checks.xml`. Dado que está ubicado en la raíz de tu proyecto (no en `src/main/resources`, donde el plugin normalmente busca), necesitas indicarle explícitamente al plugin dónde encontrarlo.

- **Acción**: Actualiza la etiqueta `<configLocation>` en tu `pom.xml` para que apunte a la raíz del proyecto.

---

### Paso 2: Resolver el Error de `SuppressWithNearbyTextFilter`
El módulo `SuppressWithNearbyTextFilter` falla al inicializarse porque la versión de Checkstyle que usa el plugin está desactualizada y no es compatible con este filtro. Necesitas actualizar el plugin y especificar una versión compatible de Checkstyle.

- **Acción**: Actualiza el `maven-checkstyle-plugin` a la versión `3.3.1` y añade una dependencia a la versión de Checkstyle `10.17.0`, que es compatible con `SuppressWithNearbyTextFilter`.

---

### Configuración Actualizada del `pom.xml`
Modifica la sección del `maven-checkstyle-plugin` en tu `pom.xml` de la siguiente manera:

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-checkstyle-plugin</artifactId>
    <version>3.3.1</version> <!-- Actualizar a la última versión -->
    <configuration>
        <configLocation>${project.basedir}/checks.xml</configLocation> <!-- Apuntar a checks.xml en la raíz del proyecto -->
    </configuration>
    <dependencies>
        <dependency>
            <groupId>com.puppycrawl.tools</groupId>
            <artifactId>checkstyle</artifactId>
            <version>10.17.0</version> <!-- Es compatible con SuppressWithNearbyTextFilter -->
        </dependency>
    </dependencies>
    <executions>
        <execution>
            <id>checkstyle-check</id>
            <phase>compile</phase>
            <goals>
                <goal>check</goal>
            </goals>
        </execution>
    </executions>
</plugin>
```

#### Explicación:
- **`<configLocation>${project.basedir}/checks.xml</configLocation>`**: Especifica que `checks.xml` está en la raíz del proyecto (`${project.basedir}` es una propiedad de Maven para el directorio raíz).
- **`version 3.3.1`**: Utiliza una versión más reciente del plugin para una mejor compatibilidad.
- **Dependencia de Checkstyle `10.17.0`**: Asegura que el plugin use una versión de Checkstyle que incluya `SuppressWithNearbyTextFilter`.

---

### Paso 3: Verificar la Configuración de `checks.xml`
Asegúrate de que el módulo `SuppressWithNearbyTextFilter` en tu `checks.xml` esté definido correctamente. Una configuración de ejemplo podría verse así:

```xml
<module name="SuppressWithNearbyTextFilter">
    <property name="nearbyTextPattern" value="@SuppressWarnings"/>
</module>
```

- **Acción**: Revisa `checks.xml` en busca de errores tipográficos o propiedades incorrectas. Consulta la [documentación de Checkstyle](https://checkstyle.org/filters/suppresswithnearbytextfilter.html) para obtener más detalles.
- **Consejo para Solucionar Problemas**: Si el error persiste, elimina temporalmente el módulo `SuppressWithNearbyTextFilter` de `checks.xml` y ejecuta `mvn checkstyle:check` para ver si el problema es específico de este filtro.

---

### Paso 4: Probar la Corrección
- Ejecuta el siguiente comando para probar:
  ```bash
  mvn clean checkstyle:check
  ```
- Si funciona, el plugin debería encontrar `checks.xml` y procesar todos los módulos sin errores.
- Para asegurarte de que Checkstyle se ejecute durante la compilación, usa:
  ```bash
  mvn compile
  ```

---

### Opcional: Ubicación Alternativa del Archivo
Si prefieres una configuración más estándar de Maven:
- Mueve `checks.xml` a `src/main/resources/checks.xml`.
- Actualiza `<configLocation>` a:
  ```xml
  <configLocation>classpath:checks.xml</configLocation>
  ```
- Esto se alinea con la convención de Maven de colocar los recursos en `src/main/resources`.

---

### Notas Adicionales
- **Advertencia No Relacionada**: Si ves una advertencia sobre una etiqueta `<blocked>` en `/usr/share/maven/conf/settings.xml`, no está relacionada con este problema, pero sugiere un problema en tu archivo de configuración de Maven. Revísalo por separado si es necesario.
- **¿Sigues Teniendo Problemas?** Comparte lo siguiente para obtener más ayuda:
  - El contenido (o un fragmento) de `checks.xml`.
  - La salida completa de `mvn clean checkstyle:check -X` (modo debug).

---

Al aplicar estos cambios, el `maven-checkstyle-plugin` debería localizar correctamente `checks.xml` y ser compatible con `SuppressWithNearbyTextFilter`, resolviendo así tus errores.

---

El error que encontraste anteriormente indicaba que el `maven-checkstyle-plugin` no podía encontrar `checks.xml` en el classpath y luego fallaba debido a un problema con el módulo `SuppressWithNearbyTextFilter`. Según la estructura actualizada de tu proyecto, parece que `checks.xml` está ubicado en la raíz del proyecto (`~/Projects/blog-server/checks.xml`), no en `src/main/resources` como se asumió previamente. Esto explica por qué el plugin no pudo encontrarlo cuando se configuró con `<configLocation>classpath:checks.xml</configLocation>` o `<configLocation>checks.xml</configLocation>`, ya que esas configuraciones esperan el archivo en el classpath (típicamente `src/main/resources`).

Para solucionar esto y asegurar que el `maven-checkstyle-plugin` se ejecute con `mvn compile` usando tu `checks.xml` personalizado en la raíz del proyecto, necesitas actualizar `<configLocation>` para que apunte a la ruta absoluta o relativa del proyecto del archivo. Adicionalmente, necesitas abordar el problema de `SuppressWithNearbyTextFilter` asegurando la compatibilidad con la versión de Checkstyle. A continuación, se presenta la solución paso a paso.

### Configuración Actualizada del `pom.xml`
Modifica el `maven-checkstyle-plugin` en tu `pom.xml` para que haga referencia a `checks.xml` en la raíz del proyecto y use una versión compatible de Checkstyle para dar soporte a `SuppressWithNearbyTextFilter`.

```xml
<build>
    <resources>
        <resource>
            <directory>src/main/resources</directory>
            <includes>
                <include>**/*.xml</include>
                <include>**/*.yaml</include>
            </includes>
        </resource>
    </resources>
    <plugins>
        <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
            <version>3.4.2</version>
            <executions>
                <execution>
                    <goals>
                        <goal>repackage</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-surefire-plugin</artifactId>
            <version>3.0.0-M8</version>
        </plugin>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-checkstyle-plugin</artifactId>
            <version>3.3.1</version> <!-- Última versión para mejor compatibilidad -->
            <configuration>
                <configLocation>${project.basedir}/checks.xml</configLocation> <!-- Apuntar a checks.xml en la raíz del proyecto -->
            </configuration>
            <dependencies>
                <dependency>
                    <groupId>com.puppycrawl.tools</groupId>
                    <artifactId>checkstyle</artifactId>
                    <version>10.17.0</version> <!-- Es compatible con SuppressWithNearbyTextFilter -->
                </dependency>
            </dependencies>
            <executions>
                <execution>
                    <id>checkstyle-check</id>
                    <phase>compile</phase>
                    <goals>
                        <goal>check</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

### Explicación de los Cambios
1. **`<configLocation>` Actualizado**:
   - Cambiado a `${project.basedir}/checks.xml` para apuntar a `checks.xml` en la raíz del proyecto (`~/Projects/blog-server/checks.xml`).
   - `${project.basedir}` se resuelve al directorio que contiene `pom.xml`, asegurando que el plugin encuentre el archivo independientemente del classpath.

2. **Versión del Plugin Actualizada**:
   - Se actualizó `maven-checkstyle-plugin` a `3.3.1` (la más reciente a junio de 2025) para una mejor compatibilidad y corrección de errores.

3. **Dependencia de Checkstyle Añadida**:
   - Se añadió `<dependency>` para Checkstyle `10.17.0`, que incluye soporte para `SuppressWithNearbyTextFilter`. La versión por defecto de Checkstyle en `maven-checkstyle-plugin:3.1.1` (`8.29`) no es compatible con este filtro, lo que causaba el error anterior.

4. **Se mantuvo `<phase>compile</phase>`**:
   - Asegura que `checkstyle:check` se ejecute durante `mvn compile`, como se solicitó.

5. **Sección de Recursos**:
   - Se mantuvo la sección `<resources>` para asegurar que los archivos de `src/main/resources` (como `application.yaml`) se procesen, aunque no está directamente relacionado con `checks.xml` ya que ahora está en la raíz del proyecto.

### Verificar el Contenido de `checks.xml`
El error sobre `SuppressWithNearbyTextFilter` sugiere que tu `checks.xml` hace referencia a este filtro. Asegúrate de que esté configurado correctamente. Un ejemplo válido:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE module PUBLIC
    "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN"
    "https://checkstyle.org/dtds/configuration_1_3.dtd">
<module name="Checker">
    <module name="SuppressWithNearbyTextFilter">
        <!-- Propiedades de ejemplo, ajústalas según sea necesario -->
        <property name="nearbyTextPattern" value="@SuppressWarnings"/>
    </module>
    <module name="TreeWalker">
        <!-- Otras comprobaciones -->
        <module name="ConstantName"/>
    </module>
</module>
```

- **Comprobar**: Abre `checks.xml` en `~/Projects/blog-server/checks.xml` y verifica que `SuppressWithNearbyTextFilter` esté escrito correctamente e incluya las propiedades requeridas (consulta la [documentación de Checkstyle](https://checkstyle.org/filters/suppresswithnearbytextfilter.html)).
- **Acción**: Si no estás seguro, elimina temporalmente la sección `<module name="SuppressWithNearbyTextFilter"/>` y realiza una prueba para aislar el problema.

### Probar la Configuración
1. **Limpiar el Proyecto**:
   ```bash
   mvn clean
   ```
   Esto elimina el directorio `target`, incluyendo `checkstyle-checker.xml` y `checkstyle-result.xml`, asegurando que no haya artefactos obsoletos que interfieran.

2. **Ejecutar Checkstyle**:
   ```bash
   mvn checkstyle:check
   ```
   Esto prueba la configuración de Checkstyle de forma independiente.

3. **Ejecutar Compilación**:
   ```bash
   mvn compile
   ```
   Esto debería ejecutar Checkstyle (debido al enlace con la fase `compile`) y luego compilar si no hay violaciones que fallen en la build.

### Depurar si los Problemas Persisten
Si encuentras errores:
1. **Comprobar la Ruta del Archivo**:
   - Confirma que `checks.xml` existe en `~/Projects/blog-server/checks.xml`.
   - Verifica que el nombre del archivo sea exactamente `checks.xml` (sensible a mayúsculas y minúsculas, sin extensiones ocultas).

2. **Ejecutar con Registro de Depuración**:
   ```bash
   mvn clean checkstyle:check -X
   ```
   Busca mensajes sobre la carga de `checks.xml` o la inicialización de `SuppressWithNearbyTextFilter`. Comparte la salida relevante si el error persiste.

3. **Probar con un `checks.xml` Mínimo**:
   Reemplaza temporalmente `checks.xml` con una configuración mínima para descartar problemas con el contenido del archivo:
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE module PUBLIC
       "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN"
       "https://checkstyle.org/dtds/configuration_1_3.dtd">
   <module name="Checker">
       <module name="TreeWalker">
           <module name="ConstantName"/>
       </module>
   </module>
   ```
   Luego ejecuta `mvn checkstyle:check`. Si esto funciona, el problema está en `SuppressWithNearbyTextFilter` u otros módulos en tu `checks.xml` original.

### Notas Adicionales
- **Advertencia de settings.xml**: Tu salida muestra una advertencia sobre una etiqueta `<blocked>` no reconocida en `/usr/share/maven/conf/settings.xml`. Esto no está relacionado con el problema de Checkstyle, pero indica un problema potencial con tu configuración de Maven. Revisa la línea 164 de `/usr/share/maven/conf/settings.xml` y elimina o corrige la etiqueta `<blocked>`, ya que no es un elemento estándar de la configuración de Maven.
- **Ubicación Alternativa del Archivo**: Si lo prefieres, puedes mover `checks.xml` a `src/main/resources/checks.xml` y revertir `<configLocation>` a `classpath:checks.xml`. Esto es más convencional para proyectos Maven, ya que los recursos se incluyen automáticamente en el classpath.
- **Fallar en Violación**: Si las violaciones de Checkstyle están fallando la build y quieres permitir que la compilación proceda, añade `<failOnViolation>false</failOnViolation>` a la `<configuration>` del plugin:
  ```xml
  <configuration>
      <configLocation>${project.basedir}/checks.xml</configLocation>
      <failOnViolation>false</failOnViolation>
  </configuration>
  ```

### Verificación
Después de aplicar los cambios:
1. Ejecuta `mvn clean compile` y confirma que:
   - Checkstyle se ejecuta usando `checks.xml` desde la raíz del proyecto.
   - No ocurren errores relacionados con `checks.xml` o `SuppressWithNearbyTextFilter`.
   - La compilación procede si Checkstyle pasa o está configurado para no fallar la build.
2. Revisa `target/checkstyle-result.xml` para ver los resultados de Checkstyle.

Si el error persiste, por favor comparte:
- El contenido (o el fragmento relevante) de `checks.xml`.
- La salida de depuración de `mvn clean checkstyle:check -X`.
- Cualquier regla específica de Checkstyle que estés intentando aplicar con `SuppressWithNearbyTextFilter`.
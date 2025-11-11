---
audio: false
generated: true
lang: es
layout: post
title: Resolución de Dependencias Circulares con AspectJ
translated: true
type: note
---

Las dependencias circulares en tu escenario surgen porque `BlogConfig`, `BlogCore` y `BlogWeb` se referencian entre sí, creando un bucle de dependencia. Además, el `LoggingAspect` de AspectJ en `BlogCore` (o potencialmente en `BlogWeb`) puede exacerbar el problema si se aplica a métodos entre módulos, incluyendo `BlogConfig`, que depende de `BlogCore`. Vamos a desglosarlo y proporcionar una solución para resolver la dependencia circular manteniendo la funcionalidad de AspectJ intacta.

### Análisis del Problema
1. **Dependencias de Módulos**:
   - `BlogCore` depende de `BlogConfig`.
   - `BlogWeb` depende tanto de `BlogCore` como de `BlogConfig`.
   - `BlogConfig` depende de `BlogCore` (esto crea la dependencia circular: `BlogCore` ↔ `BlogConfig`).
   - La dependencia de `BlogWeb` en ambos módulos puede arrastrar la dependencia circular.

2. **AspectJ LoggingAspect**:
   - El `LoggingAspect` en `BlogCore` (o `BlogWeb`) utiliza un pointcut amplio (`execution(* *(..))`), que se aplica a todas las ejecuciones de métodos en el contexto de la aplicación, incluyendo métodos en `BlogConfig`, `BlogCore` y `BlogWeb`.
   - Si `LoggingAspect` está en `BlogCore` y se aplica (weaving) a `BlogConfig`, y `BlogConfig` depende de `BlogCore`, el proceso de weaving de AspectJ puede complicar la dependencia circular durante la inicialización.

3. **Impacto de la Dependencia Circular**:
   - En un sistema de construcción como Maven o Gradle, las dependencias circulares entre módulos pueden causar problemas de compilación o en tiempo de ejecución (por ejemplo, `BeanCurrentlyInCreationException` de Spring si se usa Spring, o problemas de carga de clases).
   - El weaving de AspectJ en tiempo de compilación o en tiempo de carga puede fallar o producir comportamientos inesperados si las clases de `BlogConfig` y `BlogCore` son interdependientes y no están completamente inicializadas.

### Solución
Para resolver la dependencia circular y asegurar que el `LoggingAspect` de AspectJ funcione correctamente, sigue estos pasos:

#### 1. Romper la Dependencia Circular
El problema principal es la dependencia `BlogCore` ↔ `BlogConfig`. Para solucionarlo, extrae la funcionalidad o configuración compartida que causa que `BlogConfig` dependa de `BlogCore` en un nuevo módulo o refactoriza las dependencias.

**Opción A: Introducir un Nuevo Módulo (`BlogCommon`)**
- Crea un nuevo módulo, `BlogCommon`, para contener interfaces, configuraciones o utilidades compartidas que tanto `BlogCore` como `BlogConfig` necesiten.
- Mueve las partes de `BlogCore` de las que depende `BlogConfig` (por ejemplo, interfaces, constantes o servicios compartidos) a `BlogCommon`.
- Actualiza las dependencias:
  - `BlogConfig` depende de `BlogCommon`.
  - `BlogCore` depende de `BlogCommon` y `BlogConfig`.
  - `BlogWeb` depende de `BlogCore` y `BlogConfig`.

**Ejemplo de Estructura de Dependencias**:
```
BlogCommon ← BlogConfig ← BlogCore ← BlogWeb
```

**Implementación**:
- En `BlogCommon`, define interfaces o componentes compartidos. Por ejemplo:
  ```java
  // Módulo BlogCommon
  public interface BlogService {
      void performAction();
  }
  ```
- En `BlogCore`, implementa la interfaz:
  ```java
  // Módulo BlogCore
  public class BlogCoreService implements BlogService {
      public void performAction() { /* lógica */ }
  }
  ```
- En `BlogConfig`, usa la interfaz de `BlogCommon`:
  ```java
  // Módulo BlogConfig
  import com.example.blogcommon.BlogService;
  public class BlogConfiguration {
      private final BlogService blogService;
      public BlogConfiguration(BlogService blogService) {
          this.blogService = blogService;
      }
  }
  ```
- En `BlogWeb`, usa ambos módulos según sea necesario.

Esto elimina la dependencia circular asegurando que `BlogConfig` ya no dependa directamente de `BlogCore`.

**Opción B: Inversión de Control (IoC) con Inyección de Dependencias**
- Si usas un framework como Spring, refactoriza `BlogConfig` para que dependa de abstracciones (interfaces) definidas en `BlogCore` en lugar de clases concretas.
- Usa la inyección de dependencias para proporcionar la implementación de `BlogCore` a `BlogConfig` en tiempo de ejecución, evitando una dependencia circular en tiempo de compilación.
- Ejemplo:
  ```java
  // Módulo BlogCore
  public interface BlogService {
      void performAction();
  }
  @Component
  public class BlogCoreService implements BlogService {
      public void performAction() { /* lógica */ }
  }

  // Módulo BlogConfig
  @Configuration
  public class BlogConfiguration {
      private final BlogService blogService;
      public BlogConfiguration(BlogService blogService) {
          this.blogService = blogService;
      }
  }
  ```
- El contenedor de IoC de Spring resuelve la dependencia en tiempo de ejecución, rompiendo la circularidad en tiempo de compilación.

#### 2. Ajustar la Configuración de AspectJ
El pointcut amplio del `LoggingAspect` (`execution(* *(..))`) puede aplicarse a todos los módulos, incluyendo `BlogConfig`, lo que podría complicar la inicialización. Para hacer el aspecto más manejable y evitar problemas de weaving:

- **Reducir el Alcance del Pointcut**: Limita el aspecto a paquetes o módulos específicos para evitar aplicarlo a `BlogConfig` u otro código de infraestructura.
  ```java
  import org.aspectj.lang.JoinPoint;
  import org.aspectj.lang.annotation.After;
  import org.aspectj.lang.annotation.Aspect;
  import java.util.Arrays;

  @Aspect
  public class LoggingAspect {
      @After("execution(* com.example.blogcore..*(..)) || execution(* com.example.blogweb..*(..))")
      public void logAfter(JoinPoint joinPoint) {
          System.out.println("Método ejecutado: " + joinPoint.getSignature());
          System.out.println("Argumentos: " + Arrays.toString(joinPoint.getArgs()));
      }
  }
  ```
  Este pointcut se aplica solo a métodos en `BlogCore` (`com.example.blogcore`) y `BlogWeb` (`com.example.blogweb`), excluyendo `BlogConfig`.

- **Mover el Aspecto a un Módulo Separado**: Para evitar problemas de weaving durante la inicialización del módulo, coloca `LoggingAspect` en un nuevo módulo (por ejemplo, `BlogAspects`) que dependa de `BlogCore` y `BlogWeb` pero no de `BlogConfig`.
  - Estructura de dependencias:
    ```
    BlogCommon ← BlogConfig ← BlogCore ← BlogWeb
                       ↑          ↑
                       └─ BlogAspects ─┘
    ```
  - Actualiza la configuración de construcción (por ejemplo, Maven/Gradle) para asegurar que `BlogAspects` se aplica (weaving) después de `BlogCore` y `BlogWeb`.

- **Usar Load-Time Weaving (LTW)**: Si el weaving en tiempo de compilación causa problemas debido a dependencias circulares, cambia a load-time weaving con AspectJ. Configura LTW en tu aplicación (por ejemplo, vía `@EnableLoadTimeWeaving` de Spring o un archivo `aop.xml`) para diferir la aplicación del aspecto hasta el tiempo de ejecución, después de que las clases se carguen.

#### 3. Actualizar la Configuración de Construcción
Asegúrate de que tu herramienta de construcción (Maven, Gradle, etc.) refleje la nueva estructura de módulos y resuelva las dependencias correctamente.

**Ejemplo en Maven**:
```xml
<!-- BlogCommon/pom.xml -->
<dependencies>
    <!-- Sin dependencias -->
</dependencies>

<!-- BlogConfig/pom.xml -->
<dependencies>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>BlogCommon</artifactId>
        <version>1.0</version>
    </dependency>
</dependencies>

<!-- BlogCore/pom.xml -->
<dependencies>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>BlogCommon</artifactId>
        <version>1.0</version>
    </dependency>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>BlogConfig</artifactId>
        <version>1.0</version>
    </dependency>
</dependencies>

<!-- BlogWeb/pom.xml -->
<dependencies>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>BlogCore</artifactId>
        <version>1.0</version>
    </dependency>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>BlogConfig</artifactId>
        <version>1.0</version>
    </dependency>
</dependencies>

<!-- BlogAspects/pom.xml -->
<dependencies>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>BlogCore</artifactId>
        <version>1.0</version>
    </dependency>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>BlogWeb</artifactId>
        <version>1.0</version>
    </dependency>
    <dependency>
        <groupId>org.aspectj</groupId>
        <artifactId>aspectjrt</artifactId>
        <version>1.9.7</version>
    </dependency>
</dependencies>
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>aspectj-maven-plugin</artifactId>
            <version>1.14.0</version>
            <configuration>
                <complianceLevel>11</complianceLevel>
                <source>11</source>
                <target>11</target>
            </configuration>
            <executions>
                <execution>
                    <goals>
                        <goal>compile</goal>
                        <goal>test-compile</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

**Ejemplo en Gradle**:
```groovy
// BlogCommon/build.gradle
dependencies {
    // Sin dependencias
}

// BlogConfig/build.gradle
dependencies {
    implementation project(':BlogCommon')
}

// BlogCore/build.gradle
dependencies {
    implementation project(':BlogCommon')
    implementation project(':BlogConfig')
}

// BlogWeb/build.gradle
dependencies {
    implementation project(':BlogCore')
    implementation project(':BlogConfig')
}

// BlogAspects/build.gradle
plugins {
    id 'java'
    id 'io.freefair.aspectj.post-compile-weaving' version '6.5.1'
}
dependencies {
    implementation project(':BlogCore')
    implementation project(':BlogWeb')
    implementation 'org.aspectj:aspectjrt:1.9.7'
    aspect 'org.aspectj:aspectjweaver:1.9.7'
}
```

#### 4. Probar la Aplicación
- Verifica que la dependencia circular se resuelva construyendo y ejecutando la aplicación.
- Asegúrate de que el `LoggingAspect` registre las ejecuciones de métodos en `BlogCore` y `BlogWeb` pero no en `BlogConfig` (a menos que se desee explícitamente).
- Si usas Spring, comprueba que no haya `BeanCurrentlyInCreationException` o errores similares durante la inicialización del contexto.
- Prueba el weaving de AspectJ para confirmar que los registros aparecen para los métodos correctos.

#### 5. Consejos Adicionales
- **Usar una Herramienta de Análisis de Dependencias**: Usa herramientas como `mvn dependency:tree` de Maven o la tarea `dependencies` de Gradle para detectar cualquier dependencia circular restante.
- **Considerar la Granularidad del Aspecto**: Si el registro (logging) solo se necesita para servicios específicos, refina aún más el pointcut para apuntar a clases o métodos específicos (por ejemplo, `execution(* com.example.blogcore.service.*.*(..))`).
- **Evitar AspectJ para Módulos de Configuración**: En general, evita aplicar aspectos al código de configuración o infraestructura (como `BlogConfig`) para reducir la complejidad.

### Estructura Final de Dependencias
Después de la refactorización:
```
BlogCommon → BlogConfig → BlogCore → BlogWeb
   ↑                        ↑
   └────── BlogAspects ─────┘
```

### Por Qué Esto Funciona
- **Romper el Círculo**: Mover las dependencias compartidas a `BlogCommon` o usar IoC asegura que `BlogConfig` no dependa de `BlogCore`, eliminando la dependencia circular.
- **Aislar los Aspectos**: Colocar `LoggingAspect` en un módulo separado (`BlogAspects`) o reducir su pointcut evita problemas de weaving y mantiene la lógica del aspecto independiente de la cadena de dependencias.
- **Configuración de Construcción**: La configuración correcta de la herramienta de construcción asegura que los módulos se compilen y se aplique el weaving en el orden correcto.

Este enfoque mantiene tu funcionalidad de registro de AspectJ mientras asegura una estructura de módulos limpia y mantenible. Si tienes detalles adicionales sobre tu configuración (por ejemplo, uso de Spring, clases específicas que causan el ciclo), ¡puedo refinar la solución aún más!
---
audio: false
generated: true
lang: es
layout: post
title: Uso De Springrunner En Pruebas De Java
translated: true
type: note
---

Para usar `SpringRunner` con el runner `@RunWith` de JUnit en pruebas de Java, sigue estos pasos. Ten en cuenta que asumo que "SpringRuner" en tu consulta es un error tipográfico y te refieres a `SpringRunner`. Aquí tienes una guía completa:

### Paso 1: Agregar la Dependencia de Spring Test
Para usar `SpringRunner`, necesitas el módulo Spring Test en tu proyecto. Si estás usando Maven, agrega esta dependencia a tu `pom.xml`:

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-test</artifactId>
    <version>${spring.version}</version>
    <scope>test</scope>
</dependency>
```

Reemplaza `${spring.version}` con la versión de Spring que estás usando (por ejemplo, `5.3.22`). Si estás usando Gradle, agrega esto a tu `build.gradle`:

```gradle
testImplementation 'org.springframework:spring-test:${springVersion}'
```

Esto asegura que `SpringRunner` y otras utilidades de prueba de Spring estén disponibles.

### Paso 2: Anotar la Clase de Prueba con `@RunWith(SpringRunner.class)`
La anotación `@RunWith` le dice a JUnit que use un runner específico en lugar del predeterminado. Para la integración con Spring, usa `SpringRunner`, que es parte del Spring TestContext Framework. Agrega esta anotación a tu clase de prueba:

```java
import org.junit.runner.RunWith;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
public class MyServiceTest {
    // El código de prueba va aquí
}
```

`SpringRunner` habilita características de Spring como la inyección de dependencias y la carga de contexto en tus pruebas. Ten en cuenta que `@RunWith` es una anotación de JUnit 4, por lo que este enfoque asume que estás usando JUnit 4. Para JUnit 5, usarías `@ExtendWith(SpringExtension.class)` en su lugar, pero tu mención de "RunWith runner" sugiere JUnit 4.

### Paso 3: Configurar el Contexto de la Aplicación Spring con `@ContextConfiguration`
Para usar beans gestionados por Spring en tus pruebas, necesitas cargar un contexto de aplicación Spring. La anotación `@ContextConfiguration` especifica cómo hacer esto. Por ejemplo, si tienes una clase de configuración (por ejemplo, `AppConfig`), usa:

```java
import org.springframework.test.context.ContextConfiguration;

@RunWith(SpringRunner.class)
@ContextConfiguration(classes = AppConfig.class)
public class MyServiceTest {
    // El código de prueba va aquí
}
```

Si tu configuración está en un archivo XML (por ejemplo, `applicationContext.xml`), usa:

```java
@ContextConfiguration(locations = "classpath:applicationContext.xml")
```

Esto le dice a `SpringRunner` qué beans y configuraciones cargar para la prueba.

### Paso 4: Inyectar Beans de Spring con `@Autowired`
Una vez que el contexto está cargado, puedes inyectar beans gestionados por Spring en tu clase de prueba usando `@Autowired`. Por ejemplo, si tienes un servicio llamado `MyService`:

```java
import org.springframework.beans.factory.annotation.Autowired;

@RunWith(SpringRunner.class)
@ContextConfiguration(classes = AppConfig.class)
public class MyServiceTest {
    @Autowired
    private MyService myService;

    // Los métodos de prueba van aquí
}
```

Esto te permite usar el bean inyectado en tus pruebas.

### Paso 5: Escribir Métodos de Prueba con `@Test`
Define tus métodos de prueba usando la anotación `@Test` de JUnit. Por ejemplo:

```java
import org.junit.Test;
import static org.junit.Assert.assertEquals;

@RunWith(SpringRunner.class)
@ContextConfiguration(classes = AppConfig.class)
public class MyServiceTest {
    @Autowired
    private MyService myService;

    @Test
    public void testMyServiceMethod() {
        String result = myService.doSomething();
        assertEquals("Resultado esperado", result);
    }
}
```

La anotación `@Test` marca los métodos que
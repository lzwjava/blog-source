---
audio: false
generated: true
lang: es
layout: post
title: Usando SpringRunner en Pruebas de Java
translated: true
---

Para usar `SpringRunner` con el runner `@RunWith` de JUnit en pruebas de Java, sigue estos pasos. Ten en cuenta que asumo que "SpringRuner" en tu consulta es un error tipográfico y te refieres a `SpringRunner`. Aquí tienes una guía completa:

### Paso 1: Agregar la Dependencia de Prueba de Spring
Para usar `SpringRunner`, necesitas el módulo de prueba de Spring en tu proyecto. Si usas Maven, agrega esta dependencia a tu `pom.xml`:

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-test</artifactId>
    <version>${spring.version}</version>
    <scope>test</scope>
</dependency>
```

Reemplaza `${spring.version}` con la versión de Spring que estás usando (por ejemplo, `5.3.22`). Si usas Gradle, agrega esto a tu `build.gradle`:

```gradle
testImplementation 'org.springframework:spring-test:${springVersion}'
```

Esto asegura que `SpringRunner` y otras utilidades de prueba de Spring estén disponibles.

### Paso 2: Anotar la Clase de Prueba con `@RunWith(SpringRunner.class)`
La anotación `@RunWith` le dice a JUnit que use un runner específico en lugar del predeterminado. Para la integración de Spring, usa `SpringRunner`, que es parte del marco de contexto de prueba de Spring. Agrega esta anotación a tu clase de prueba:

```java
import org.junit.runner.RunWith;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
public class MyServiceTest {
    // Código de prueba va aquí
}
```

`SpringRunner` habilita características de Spring como la inyección de dependencias y la carga de contexto en tus pruebas. Ten en cuenta que `@RunWith` es una anotación de JUnit 4, por lo que este enfoque asume que estás usando JUnit 4. Para JUnit 5, usarías `@ExtendWith(SpringExtension.class)` en su lugar, pero tu mención del "runner de RunWith" sugiere JUnit 4.

### Paso 3: Configurar el Contexto de Aplicación de Spring con `@ContextConfiguration`
Para usar beans gestionados por Spring en tus pruebas, necesitas cargar un contexto de aplicación de Spring. La anotación `@ContextConfiguration` especifica cómo hacerlo. Por ejemplo, si tienes una clase de configuración (por ejemplo, `AppConfig`), usa:

```java
import org.springframework.test.context.ContextConfiguration;

@RunWith(SpringRunner.class)
@ContextConfiguration(classes = AppConfig.class)
public class MyServiceTest {
    // Código de prueba va aquí
}
```

Si tu configuración está en un archivo XML (por ejemplo, `applicationContext.xml`), usa:

```java
@ContextConfiguration(locations = "classpath:applicationContext.xml")
```

Esto le dice a `SpringRunner` qué beans y configuraciones cargar para la prueba.

### Paso 4: Inyectar Beans de Spring con `@Autowired`
Una vez que el contexto se haya cargado, puedes inyectar beans gestionados por Spring en tu clase de prueba usando `@Autowired`. Por ejemplo, si tienes un servicio llamado `MyService`:

```java
import org.springframework.beans.factory.annotation.Autowired;

@RunWith(SpringRunner.class)
@ContextConfiguration(classes = AppConfig.class)
public class MyServiceTest {
    @Autowired
    private MyService myService;

    // Métodos de prueba van aquí
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

La anotación `@Test` marca los métodos que JUnit debe ejecutar como pruebas. Con `SpringRunner`, estos métodos pueden interactuar con el contexto de Spring.

### Ejemplo: Ponerlo Todo Juntos
Aquí tienes un ejemplo completo:

```java
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringRunner;
import static org.junit.Assert.assertEquals;

// Clase de configuración para la prueba
@Configuration
class AppConfig {
    @Bean
    public MyService myService() {
        return new MyService();
    }
}

// Clase de servicio para probar
class MyService {
    public String doSomething() {
        return "¡Hola, Spring!";
    }
}

// Clase de prueba
@RunWith(SpringRunner.class)
@ContextConfiguration(classes = AppConfig.class)
public class MyServiceTest {
    @Autowired
    private MyService myService;

    @Test
    public void testMyServiceMethod() {
        String result = myService.doSomething();
        assertEquals("¡Hola, Spring!", result);
    }
}
```

### Notas Adicionales
- **Propósito**: `SpringRunner` es ideal para pruebas de integración donde necesitas la inyección de dependencias o características de contexto de Spring. Para pruebas unitarias, considera usar Mockito o JUnit plano en su lugar.
- **Problemas Comunes**: Asegúrate de que la dependencia `spring-test` esté incluida, o obtendrás errores como `ClassNotFoundException`. También verifica que `@ContextConfiguration` apunte a una configuración válida.
- **Anotaciones Opcionales**: Usa `@Transactional` para pruebas que modifiquen la base de datos (para revertir los cambios) o `@ActiveProfiles` para especificar un perfil (por ejemplo, "test").

Esta configuración te permite ejecutar pruebas de JUnit con el soporte de prueba de Spring, aprovechando características como la inyección de dependencias y la gestión de contexto.
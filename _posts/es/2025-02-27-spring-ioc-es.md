---
audio: false
generated: true
lang: es
layout: post
title: Contenedor IoC de Spring
translated: true
type: note
---

Permíteme desglosar cómo usar el Contenedor IoC (Inversión de Control) de Spring de una manera clara y práctica. El Contenedor IoC de Spring es el núcleo del Spring Framework, responsable de gestionar el ciclo de vida y la configuración de los objetos de la aplicación (llamados beans). "Invierte" el control manejando la creación de objetos y la inyección de dependencias por ti, en lugar de que tú los crees y conectes manualmente.

Aquí tienes una guía paso a paso para empezar:

---

### 1. **Comprende los Conceptos Básicos**
- **Qué hace**: El Contenedor IoC crea, configura y gestiona beans (tus objetos de aplicación) basándose en metadatos que tú proporcionas (vía XML, anotaciones Java o código Java).
- **Conceptos clave**:
  - **Beans**: Objetos gestionados por el contenedor.
  - **Inyección de Dependencias (DI)**: El contenedor inyecta dependencias (otros beans o valores) en tus objetos.
  - **Configuración**: Le indicas al contenedor qué beans crear y cómo conectarlos.

---

### 2. **Configura tu Proyecto**
Para usar Spring IoC, necesitas un proyecto Spring. Si empiezas desde cero:
- Usa **Spring Boot** (la forma más sencilla) o Spring plano.
- Añade dependencias en tu `pom.xml` (si usas Maven):
  ```xml
  <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-context</artifactId>
      <version>6.1.3</version> <!-- Usa la última versión -->
  </dependency>
  ```
- Para Spring Boot, usa:
  ```xml
  <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter</artifactId>
      <version>3.2.2</version> <!-- La más reciente hasta ahora -->
  </dependency>
  ```

---

### 3. **Define tus Beans**
Puedes definir beans de tres formas principales:

#### a) **Usando Anotaciones (La más Común)**
- Crea una clase Java simple y anótala con `@Component` (o anotaciones especializadas como `@Service`, `@Repository`, etc.).
- Ejemplo:
  ```java
  import org.springframework.stereotype.Component;

  @Component
  public class MyService {
      public void doSomething() {
          System.out.println("Doing something!");
      }
  }
  ```

#### b) **Usando Configuración Java**
- Crea una clase de configuración con `@Configuration` y define beans con `@Bean`.
- Ejemplo:
  ```java
  import org.springframework.context.annotation.Bean;
  import org.springframework.context.annotation.Configuration;

  @Configuration
  public class AppConfig {
      @Bean
      public MyService myService() {
          return new MyService();
      }
  }
  ```

#### c) **Usando XML (Enfoque Heredado)**
- Define beans en un archivo XML (ej., `beans.xml`):
  ```xml
  <beans xmlns="http://www.springframework.org/schema/beans"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://www.springframework.org/schema/beans
         http://www.springframework.org/schema/beans/spring-beans.xsd">
      <bean id="myService" class="com.example.MyService"/>
  </beans>
  ```

---

### 4. **Inicializa el Contenedor IoC**
Necesitas iniciar el contenedor para gestionar tus beans.

#### a) **Con Spring Boot**
- Spring Boot lo hace automáticamente. Solo crea una clase principal con `@SpringBootApplication`:
  ```java
  import org.springframework.boot.SpringApplication;
  import org.springframework.boot.autoconfigure.SpringBootApplication;

  @SpringBootApplication
  public class MyApp {
      public static void main(String[] args) {
          SpringApplication.run(MyApp.class, args);
      }
  }
  ```
- El contenedor escanea las clases con `@Component` y las gestiona.

#### b) **Con Spring Plano (Basado en Anotaciones)**
- Usa `AnnotationConfigApplicationContext`:
  ```java
  import org.springframework.context.annotation.AnnotationConfigApplicationContext;

  public class Main {
      public static void main(String[] args) {
          AnnotationConfigApplicationContext context = 
              new AnnotationConfigApplicationContext(AppConfig.class);
          MyService service = context.getBean(MyService.class);
          service.doSomething();
          context.close();
      }
  }
  ```

#### c) **Con XML**
- Usa `ClassPathXmlApplicationContext`:
  ```java
  import org.springframework.context.support.ClassPathXmlApplicationContext;

  public class Main {
      public static void main(String[] args) {
          ClassPathXmlApplicationContext context = 
              new ClassPathXmlApplicationContext("beans.xml");
          MyService service = context.getBean("myService", MyService.class);
          service.doSomething();
          context.close();
      }
  }
  ```

---

### 5. **Inyecta Dependencias**
El Contenedor IoC puede inyectar dependencias en tus beans.

#### a) **Inyección por Constructor (Recomendada)**
```java
@Component
public class MyController {
    private final MyService myService;

    public MyController(MyService myService) {
        this.myService = myService;
    }

    public void execute() {
        myService.doSomething();
    }
}
```

#### b) **Inyección por Setter**
```java
@Component
public class MyController {
    private MyService myService;

    @Autowired
    public void setMyService(MyService myService) {
        this.myService = myService;
    }
}
```

#### c) **Inyección por Campo (Menos Preferida)**
```java
@Component
public class MyController {
    @Autowired
    private MyService myService;

    public void execute() {
        myService.doSomething();
    }
}
```
- Usa `@Autowired` (específico de Spring) o `@Inject` (estándar JSR-330) para marcar los puntos de inyección.

---

### 6. **Ejecuta y Usa los Beans**
- Una vez que el contenedor está en ejecución, conecta tus beans y sus dependencias. Puedes obtener beans con `context.getBean()` (Spring plano) o dejar que Spring Boot lo maneje automáticamente mediante inyección.

Ejemplo con Spring Boot:
```java
@SpringBootApplication
public class MyApp {
    public static void main(String[] args) {
        ApplicationContext context = SpringApplication.run(MyApp.class, args);
        MyController controller = context.getBean(MyController.class);
        controller.execute();
    }
}
```

---

### 7. **Consejos Adicionales**
- **Ámbitos**: Por defecto, los beans son singletons. Usa `@Scope("prototype")` para nuevas instancias por solicitud.
- **Escaneo de Componentes**: Añade `@ComponentScan` a tu clase de configuración si los beans están en paquetes diferentes.
- **Perfiles**: Usa `@Profile` para activar beans en entornos específicos (ej., "dev", "prod").
- **Cierra el Contexto**: En aplicaciones que no son Spring Boot, llama a `context.close()` para liberar recursos.

---

¡Esa es la esencia! Empieza con Spring Boot y anotaciones para simplificar. Si te quedas estancado en una parte específica—como conectar una dependencia complicada o depurar—¡no dudes en preguntar y profundizaré más contigo!
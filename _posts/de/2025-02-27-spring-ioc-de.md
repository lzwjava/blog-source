---
audio: false
generated: true
lang: de
layout: post
title: Spring IoC (Inversion of Control) Container
translated: true
type: note
---

Lassen Sie mich erklären, wie Sie den Spring IoC (Inversion of Control) Container auf klare und praktische Weise verwenden können. Der Spring IoC Container ist das Kernstück des Spring Frameworks und für die Verwaltung des Lebenszyklus und der Konfiguration von Anwendungsobjekten (sogenannte Beans) zuständig. Er "invertiert" die Kontrolle, indem er die Objekterstellung und Abhängigkeitsinjektion für Sie übernimmt, anstatt dass Sie diese manuell erstellen und verbinden müssen.

Hier ist eine Schritt-für-Schritt-Anleitung für den Einstieg:

---

### 1. **Grundlagen verstehen**
- **Was er tut**: Der IoC Container erstellt, konfiguriert und verwaltet Beans (Ihre Anwendungsobjekte) basierend auf Metadaten, die Sie bereitstellen (über XML, Java-Annotationen oder Java-Code).
- **Schlüsselkonzepte**:
  - **Beans**: Vom Container verwaltete Objekte.
  - **Dependency Injection (DI)**: Der Container injiziert Abhängigkeiten (andere Beans oder Werte) in Ihre Objekte.
  - **Konfiguration**: Sie teilen dem Container mit, welche Beans er erstellen und wie er sie verbinden soll.

---

### 2. **Ihr Projekt einrichten**
Um Spring IoC zu verwenden, benötigen Sie ein Spring-Projekt. Wenn Sie neu starten:
- Verwenden Sie **Spring Boot** (einfachste Methode) oder plain Spring.
- Fügen Sie Abhängigkeiten in Ihrer `pom.xml` hinzu (falls Sie Maven verwenden):
  ```xml
  <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-context</artifactId>
      <version>6.1.3</version> <!-- Verwenden Sie die neueste Version -->
  </dependency>
  ```
- Für Spring Boot verwenden Sie:
  ```xml
  <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter</artifactId>
      <version>3.2.2</version> <!-- Aktuellste zum jetzigen Zeitpunkt -->
  </dependency>
  ```

---

### 3. **Definieren Sie Ihre Beans**
Sie können Beans auf drei Hauptwegen definieren:

#### a) **Verwendung von Annotationen (Am gebräuchlichsten)**
- Erstellen Sie eine einfache Java-Klasse und annotieren Sie sie mit `@Component` (oder spezialisierten Annotationen wie `@Service`, `@Repository`, etc.).
- Beispiel:
  ```java
  import org.springframework.stereotype.Component;

  @Component
  public class MyService {
      public void doSomething() {
          System.out.println("Doing something!");
      }
  }
  ```

#### b) **Verwendung von Java-Konfiguration**
- Erstellen Sie eine Konfigurationsklasse mit `@Configuration` und definieren Sie Beans mit `@Bean`.
- Beispiel:
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

#### c) **Verwendung von XML (Legacy-Ansatz)**
- Definieren Sie Beans in einer XML-Datei (z.B. `beans.xml`):
  ```xml
  <beans xmlns="http://www.springframework.org/schema/beans"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://www.springframework.org/schema/beans
         http://www.springframework.org/schema/beans/spring-beans.xsd">
      <bean id="myService" class="com.example.MyService"/>
  </beans>
  ```

---

### 4. **Initialisieren Sie den IoC Container**
Sie müssen den Container starten, um Ihre Beans zu verwalten.

#### a) **Mit Spring Boot**
- Spring Boot erledigt dies automatisch. Erstellen Sie einfach eine Hauptklasse mit `@SpringBootApplication`:
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
- Der Container scannt nach `@Component`-Klassen und verwaltet sie.

#### b) **Mit Plain Spring (Annotationsbasiert)**
- Verwenden Sie `AnnotationConfigApplicationContext`:
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

#### c) **Mit XML**
- Verwenden Sie `ClassPathXmlApplicationContext`:
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

### 5. **Injecten Sie Abhängigkeiten**
Der IoC Container kann Abhängigkeiten in Ihre Beans injecten.

#### a) **Constructor Injection (Empfohlen)**
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

#### b) **Setter Injection**
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

#### c) **Field Injection (Weniger bevorzugt)**
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
- Verwenden Sie `@Autowired` (Spring-spezifisch) oder `@Inject` (JSR-330 Standard), um Injection-Points zu markieren.

---

### 6. **Führen Sie die Beans aus und verwenden Sie sie**
- Sobald der Container läuft, verbindet er Ihre Beans und ihre Abhängigkeiten. Sie können Beans mit `context.getBean()` (plain Spring) abrufen oder Spring Boot die Arbeit automatisch via Injection erledigen lassen.

Beispiel mit Spring Boot:
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

### 7. **Zusätzliche Tipps**
- **Scopes**: Standardmäßig sind Beans Singletons. Verwenden Sie `@Scope("prototype")` für neue Instanzen pro Anfrage.
- **Component Scanning**: Fügen Sie Ihrer Konfigurationsklasse `@ComponentScan` hinzu, wenn sich Beans in verschiedenen Packages befinden.
- **Profiles**: Verwenden Sie `@Profile`, um Beans in bestimmten Umgebungen zu aktivieren (z.B. "dev", "prod").
- **Context schließen**: In Nicht-Spring-Boot-Apps rufen Sie `context.close()` auf, um Ressourcen freizugeben.

---

Das ist die Kurzfassung! Beginnen Sie mit Spring Boot und Annotationen für Einfachheit. Wenn Sie bei einem bestimmten Teil feststecken – wie dem Verbinden einer kniffligen Abhängigkeit oder dem Debuggen – fragen Sie gerne, und ich gehe mit Ihnen tiefer ins Detail!
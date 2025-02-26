---
audio: false
lang: de
layout: post
title: Spring IoC (Inversion of Control) Container
translated: true
---

Lassen Sie mich Ihnen erklären, wie Sie den Spring IoC (Inversion of Control) Container auf eine klare und praktische Weise verwenden. Der Spring IoC Container ist das Herzstück des Spring Frameworks und verantwortlich für das Management des Lebenszyklus und der Konfiguration von Anwendungsobjekten (genannt Beans). Er "kehrt die Kontrolle um", indem er die Erstellung und die Abhängigkeitsinjektion von Objekten für Sie übernimmt, anstatt dass Sie dies manuell tun.

Hier ist eine Schritt-für-Schritt-Anleitung, um Ihnen den Einstieg zu erleichtern:

---

### 1. **Grundlagen verstehen**
- **Was es tut**: Der IoC Container erstellt, konfiguriert und verwaltet Beans (Ihre Anwendungsobjekte) basierend auf den Metadaten, die Sie bereitstellen (über XML, Java-Anmerkungen oder Java-Code).
- **Wichtige Konzepte**:
  - **Beans**: Objekte, die vom Container verwaltet werden.
  - **Dependency Injection (DI)**: Der Container injiziert Abhängigkeiten (andere Beans oder Werte) in Ihre Objekte.
  - **Konfiguration**: Sie sagen dem Container, welche Beans er erstellen und wie er sie verdrahten soll.

---

### 2. **Projekt einrichten**
Um Spring IoC zu verwenden, benötigen Sie ein Spring-Projekt. Wenn Sie ganz neu anfangen:
- Verwenden Sie **Spring Boot** (einfachste Methode) oder einfaches Spring.
- Fügen Sie Abhängigkeiten in Ihrer `pom.xml` hinzu (wenn Sie Maven verwenden):
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
      <version>3.2.2</version> <!-- Aktuellste Version -->
  </dependency>
  ```

---

### 3. **Beans definieren**
Sie können Beans auf drei Hauptweisen definieren:

#### a) **Verwendung von Annotationen (am häufigsten)**
- Erstellen Sie eine einfache Java-Klasse und versehen Sie sie mit `@Component` (oder spezialisierten Annotationen wie `@Service`, `@Repository` usw.).
- Beispiel:
  ```java
  import org.springframework.stereotype.Component;

  @Component
  public class MyService {
      public void doSomething() {
          System.out.println("Etwas tun!");
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

#### c) **Verwendung von XML (veraltete Methode)**
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

### 4. **IoC-Container initialisieren**
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

#### b) **Mit einfachem Spring (annotation-basiert)**
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

### 5. **Abhängigkeiten injizieren**
Der IoC-Container kann Abhängigkeiten in Ihre Beans injizieren.

#### a) **Konstruktor-Injektion (empfohlen)**
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

#### b) **Setter-Injektion**
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

#### c) **Feld-Injektion (weniger bevorzugt)**
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
- Verwenden Sie `@Autowired` (Spring-spezifisch) oder `@Inject` (JSR-330-Standard), um Injektionspunkte zu markieren.

---

### 6. **Beans ausführen und verwenden**
- Sobald der Container läuft, verdrahtet er Ihre Beans und deren Abhängigkeiten. Sie können Beans mit `context.getBean()` (einfaches Spring) abrufen oder lassen Sie Spring Boot dies automatisch über Injektion erledigen.

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
- **Component Scanning**: Fügen Sie `@ComponentScan` Ihrer Konfigurationsklasse hinzu, wenn sich Beans in verschiedenen Paketen befinden.
- **Profile**: Verwenden Sie `@Profile`, um Beans in bestimmten Umgebungen zu aktivieren (z.B. "dev", "prod").
- **Context schließen**: In nicht-Spring-Boot-Anwendungen rufen Sie `context.close()` auf, um Ressourcen freizugeben.

---

Das ist die Essenz! Beginnen Sie mit Spring Boot und Annotationen für Einfachheit. Wenn Sie bei einem bestimmten Teil stecken bleiben – wie z.B. beim Verdrahten einer kniffligen Abhängigkeit oder beim Debuggen – zögern Sie nicht zu fragen, und ich werde tiefer mit Ihnen eintauchen!
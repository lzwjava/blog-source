---
audio: false
generated: true
lang: fr
layout: post
title: Conteneur IoC (Inversion of Control) de Spring
translated: true
type: note
---

Permettez-moi de décomposer comment utiliser le conteneur Spring IoC (Inversion of Control) de manière claire et pratique. Le conteneur Spring IoC est le cœur du Spring Framework, responsable de la gestion du cycle de vie et de la configuration des objets de l'application (appelés beans). Il "inverse" le contrôle en gérant pour vous la création des objets et l'injection de dépendances, plutôt que de les créer et de les câbler manuellement.

Voici un guide étape par étape pour commencer :

---

### 1. **Comprendre les bases**
- **Ce qu'il fait** : Le conteneur IoC crée, configure et gère les beans (vos objets d'application) en fonction des métadonnées que vous fournissez (via XML, des annotations Java ou du code Java).
- **Concepts clés** :
  - **Beans** : Objets gérés par le conteneur.
  - **Injection de Dépendances (DI)** : Le conteneur injecte les dépendances (d'autres beans ou valeurs) dans vos objets.
  - **Configuration** : Vous indiquez au conteneur quels beans créer et comment les câbler.

---

### 2. **Configurer votre projet**
Pour utiliser Spring IoC, vous avez besoin d'un projet Spring. Si vous partez de zéro :
- Utilisez **Spring Boot** (méthode la plus simple) ou Spring standard.
- Ajoutez les dépendances dans votre `pom.xml` (si vous utilisez Maven) :
  ```xml
  <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-context</artifactId>
      <version>6.1.3</version> <!-- Utilisez la dernière version -->
  </dependency>
  ```
- Pour Spring Boot, utilisez :
  ```xml
  <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter</artifactId>
      <version>3.2.2</version> <!-- Dernière version à ce jour -->
  </dependency>
  ```

---

### 3. **Définir vos beans**
Vous pouvez définir les beans de trois manières principales :

#### a) **En utilisant des annotations (le plus courant)**
- Créez une classe Java simple et annotez-la avec `@Component` (ou des annotations spécialisées comme `@Service`, `@Repository`, etc.).
- Exemple :
  ```java
  import org.springframework.stereotype.Component;

  @Component
  public class MyService {
      public void doSomething() {
          System.out.println("Doing something!");
      }
  }
  ```

#### b) **En utilisant la configuration Java**
- Créez une classe de configuration avec `@Configuration` et définissez les beans avec `@Bean`.
- Exemple :
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

#### c) **En utilisant XML (approche legacy)**
- Définissez les beans dans un fichier XML (par exemple, `beans.xml`) :
  ```xml
  <beans xmlns="http://www.springframework.org/schema/beans"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://www.springframework.org/schema/beans
         http://www.springframework.org/schema/beans/spring-beans.xsd">
      <bean id="myService" class="com.example.MyService"/>
  </beans>
  ```

---

### 4. **Initialiser le conteneur IoC**
Vous devez démarrer le conteneur pour gérer vos beans.

#### a) **Avec Spring Boot**
- Spring Boot le fait automatiquement. Créez simplement une classe principale avec `@SpringBootApplication` :
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
- Le conteneur scanne les classes annotées avec `@Component` et les gère.

#### b) **Avec Spring standard (basé sur les annotations)**
- Utilisez `AnnotationConfigApplicationContext` :
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

#### c) **Avec XML**
- Utilisez `ClassPathXmlApplicationContext` :
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

### 5. **Injecter les dépendances**
Le conteneur IoC peut injecter des dépendances dans vos beans.

#### a) **Injection par constructeur (recommandée)**
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

#### b) **Injection par setter**
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

#### c) **Injection par champ (moins préférée)**
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
- Utilisez `@Autowired` (spécifique à Spring) ou `@Inject` (standard JSR-330) pour marquer les points d'injection.

---

### 6. **Exécuter et utiliser les beans**
- Une fois le conteneur démarré, il câble vos beans et leurs dépendances. Vous pouvez récupérer les beans avec `context.getBean()` (Spring standard) ou laisser Spring Boot les gérer automatiquement via l'injection.

Exemple avec Spring Boot :
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

### 7. **Conseils supplémentaires**
- **Portées** : Par défaut, les beans sont des singletons. Utilisez `@Scope("prototype")` pour de nouvelles instances par requête.
- **Scan de composants** : Ajoutez `@ComponentScan` à votre classe de configuration si les beans se trouvent dans des packages différents.
- **Profils** : Utilisez `@Profile` pour activer les beans dans des environnements spécifiques (par exemple, "dev", "prod").
- **Fermer le contexte** : Dans les applications non-Spring Boot, appelez `context.close()` pour libérer les ressources.

---

Voilà l'essentiel ! Commencez avec Spring Boot et les annotations pour plus de simplicité. Si vous êtes bloqué sur un point spécifique—comme câbler une dépendance délicate ou déboguer—n'hésitez pas à demander, et nous approfondirons ensemble !
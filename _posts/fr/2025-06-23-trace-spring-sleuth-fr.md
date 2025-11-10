---
audio: false
generated: true
lang: fr
layout: post
title: Maîtriser Spring Cloud Sleuth dans Spring Boot
translated: true
type: note
---

Spring Cloud Sleuth est un outil puissant pour ajouter des capacités de traçage distribué aux applications Spring. Bien qu'il soit particulièrement utile dans les architectures de microservices pour suivre les requêtes à travers plusieurs services, il offre également des avantages significatifs pour les applications uniques (monolithes) en améliorant la corrélation des logs et le débogage.

Ce guide fournira une vue d'ensemble complète de l'utilisation de Spring Cloud Sleuth au sein d'une application Spring Boot unique, en s'inspirant de l'approche de Baeldung.

## 1\. Qu'est-ce que Spring Cloud Sleuth ?

Fondamentalement, Spring Cloud Sleuth instrumente les applications Spring pour ajouter automatiquement des informations de traçage aux logs et les propager à travers différents composants et même différents threads au sein d'une même application. Il s'appuie sur la bibliothèque Brave d'OpenZipkin pour cette fonctionnalité.

**Terminologie clé :**

  * **Trace :** Représente une requête ou un travail unique qui traverse l'application. Chaque trace a un `traceId` unique. Considérez-la comme le parcours complet d'une requête.
  * **Span :** Représente une unité logique de travail au sein d'une trace. Une trace est composée de plusieurs spans, formant une structure arborescente. Chaque span a un `spanId` unique. Par exemple, une requête HTTP entrante peut être un span, et un appel de méthode au sein de cette requête pourrait être un autre span (enfant).
  * **MDC (Mapped Diagnostic Context) :** Sleuth s'intègre au MDC de Slf4J pour injecter `traceId` et `spanId` dans vos messages de log, facilitant le filtrage et la corrélation des logs pour une requête spécifique.

## 2\. Pourquoi utiliser Sleuth dans une application unique ?

Même dans un monolithe, les requêtes impliquent souvent plusieurs couches, des opérations asynchrones et différents threads. Corréler manuellement les messages de log pour une seule requête peut être fastidieux et sujet aux erreurs. Sleuth automatise cela en :

  * **Simplifiant le débogage :** En ajoutant `traceId` et `spanId` à chaque entrée de log, vous pouvez facilement filtrer les logs pour voir tout ce qui concerne une requête utilisateur spécifique, même si elle traverse plusieurs méthodes, services ou threads au sein de votre application unique.
  * **Améliorant l'observabilité :** Fournit une image plus claire de la façon dont une requête circule et où les goulots d'étranglement ou les problèmes potentiels peuvent survenir.
  * **Garantissant la cohérence :** Assure une approche cohérente de la corrélation des logs sans nécessiter d'effort manuel dans chaque partie de votre base de code.

## 3\. Pour commencer : Configuration et installation

### 3.1. Configuration du projet (Maven)

Pour commencer, créez un nouveau projet Spring Boot (vous pouvez utiliser Spring Initializr) et ajoutez la dépendance `spring-cloud-starter-sleuth` à votre `pom.xml` :

```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-sleuth</artifactId>
</dependency>
```

**Important :** Assurez-vous d'utiliser une version compatible de Spring Boot et Spring Cloud. Les dépendances Spring Cloud sont généralement gérées à l'aide d'un Bill of Materials (BOM).

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-dependencies</artifactId>
            <version>${spring-cloud.version}</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

Remplacez `${spring-cloud.version}` par la version appropriée du train de release (par exemple, `2021.0.1`, `2022.0.0`).

### 3.2. Nom de l'application

Il est fortement recommandé de définir un nom d'application dans votre fichier `application.properties` ou `application.yml`. Ce nom apparaîtra dans vos logs, ce qui est utile pour identifier la source des logs, surtout si vous passez plus tard à un système distribué.

```properties
# application.properties
spring.application.name=my-single-app
```

### 3.3. Modèle de journalisation

Spring Cloud Sleuth modifie automatiquement le modèle de journalisation par défaut pour inclure `traceId` et `spanId`. Une sortie de log typique avec Sleuth peut ressembler à ceci :

```
2025-06-23 23:30:00.123 INFO [my-single-app,a1b2c3d4e5f6a7b8,a1b2c3d4e5f6a7b8,false] 12345 --- [nio-8080-exec-1] c.e.m.MyController : This is a log message.
```

Ici :

  * `my-single-app` : Est le `spring.application.name`.
  * `a1b2c3d4e5f6a7b8` : Est le `traceId`.
  * `a1b2c3d4e5f6a7b8` (le deuxième) : Est le `spanId` (pour la span racine, traceId et spanId sont souvent identiques).
  * `false` : Indique si la span est exportable (true signifie qu'elle sera envoyée à un collecteur de traçage comme Zipkin).

Si vous avez un modèle de journalisation personnalisé, vous devrez explicitement ajouter le `traceId` et le `spanId` en utilisant `%X{traceId}` et `%X{spanId}` (pour Logback).

Exemple de modèle Logback personnalisé dans `logback-spring.xml` :

```xml
<appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
    <encoder>
        <pattern>%d{yyyy-MM-dd HH:mm:ss.SSS} %-5level [${spring.application.name:-},%X{traceId:-},%X{spanId:-}] %thread %logger{36} - %msg%n</pattern>
    </encoder>
</appender>
```

## 4\. Comment fonctionne Sleuth dans une application unique

Une fois la dépendance `spring-cloud-starter-sleuth` dans le classpath, l'auto-configuration de Spring Boot prend le relais.

### 4.1. Instrumentation automatique

Sleuth instrumente automatiquement les composants Spring communs et les canaux de communication :

  * **Filtre Servlet :** Pour les requêtes HTTP entrantes vers vos contrôleurs.
  * **RestTemplate :** Pour les appels HTTP sortants effectués avec `RestTemplate` (assurez-vous d'utiliser un `RestTemplate` géré par un bean pour que Sleuth l'instrumente automatiquement).
  * **Actions planifiées :** Pour les méthodes `@Scheduled`.
  * **Canaux de messages :** Pour Spring Integration et Spring Cloud Stream.
  * **Méthodes asynchrones :** Pour les méthodes `@Async` (garantit que le contexte de trace/span est propagé à travers les threads).

### 4.2. Exemple de requête web simple

Considérez une application Spring Boot simple avec un contrôleur REST :

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class MyController {

    private static final Logger logger = LoggerFactory.getLogger(MyController.class);

    @GetMapping("/")
    public String helloSleuth() {
        logger.info("Hello from MyController");
        return "success";
    }
}
```

Lorsque vous accédez à `http://localhost:8080/`, vous verrez des messages de log comme :

```
2025-06-23 23:35:00.123 INFO [my-single-app,c9d0e1f2a3b4c5d6,c9d0e1f2a3b4c5d6,false] 7890 --- [nio-8080-exec-1] c.e.m.MyController : Hello from MyController
```

Remarquez l'ajout automatique du `traceId` et du `spanId`.

### 4.3. Propagation du contexte à travers les méthodes (même span)

Si votre requête traverse plusieurs méthodes au sein de la même application et que vous voulez que ces méthodes fassent partie de la *même span*, Sleuth gère cela automatiquement.

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.stereotype.Service;

@Service
class MyService {
    private static final Logger logger = LoggerFactory.getLogger(MyService.class);

    public void doSomeWork() throws InterruptedException {
        Thread.sleep(100); // Simuler un travail
        logger.info("Doing some work in MyService");
    }
}

@RestController
public class MyController {
    private static final Logger logger = LoggerFactory.getLogger(MyController.class);

    @Autowired
    private MyService myService;

    @GetMapping("/same-span-example")
    public String sameSpanExample() throws InterruptedException {
        logger.info("Entering same-span-example endpoint");
        myService.doSomeWork();
        logger.info("Exiting same-span-example endpoint");
        return "success";
    }
}
```

Les logs pour `/same-span-example` montreront le même `traceId` et `spanId` pour les méthodes du contrôleur et du service :

```
2025-06-23 23:40:00.100 INFO [my-single-app,e4f5g6h7i8j9k0l1,e4f5g6h7i8j9k0l1,false] 1234 --- [nio-8080-exec-2] c.e.m.MyController : Entering same-span-example endpoint
2025-06-23 23:40:00.200 INFO [my-single-app,e4f5g6h7i8j9k0l1,e4f5g6h7i8j9k0l1,false] 1234 --- [nio-8080-exec-2] c.e.m.MyService : Doing some work in MyService
2025-06-23 23:40:00.205 INFO [my-single-app,e4f5g6h7i8j9k0l1,e4f5g6h7i8j9k0l1,false] 1234 --- [nio-8080-exec-2] c.e.m.MyController : Exiting same-span-example endpoint
```

### 4.4. Création manuelle de nouvelles spans

Vous pourriez vouloir créer une nouvelle span pour une unité de travail distincte au sein de votre application, même si elle fait partie de la même trace globale. Cela permet un suivi et un minutage plus fins. Spring Cloud Sleuth fournit l'API `Tracer` pour cela.

```java
import brave.Tracer;
import brave.Span;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@Service
class MyService {
    private static final Logger logger = LoggerFactory.getLogger(MyService.class);

    @Autowired
    private Tracer tracer; // Injecter le Brave Tracer

    public void doSomeWorkNewSpan() throws InterruptedException {
        logger.info("I'm in the original span before new span");

        // Créer une nouvelle span avec un nom descriptif
        Span newSpan = tracer.nextSpan().name("custom-internal-work").start();
        try (Tracer.SpanInScope ws = tracer.withSpanInScope(newSpan)) {
            Thread.sleep(200); // Simuler un travail dans la nouvelle span
            logger.info("I'm in the new custom span doing some cool work");
        } finally {
            newSpan.finish(); // Toujours terminer la span
        }

        logger.info("I'm back in the original span");
    }
}

@RestController
public class MyController {
    private static final Logger logger = LoggerFactory.getLogger(MyController.class);

    @Autowired
    private MyService myService;

    @GetMapping("/new-span-example")
    public String newSpanExample() throws InterruptedException {
        logger.info("Entering new-span-example endpoint");
        myService.doSomeWorkNewSpan();
        logger.info("Exiting new-span-example endpoint");
        return "success";
    }
}
```

Les logs pour `/new-span-example` montreront que l'ID de trace reste le même, mais un nouveau `spanId` apparaîtra pour le "custom-internal-work" :

```
2025-06-23 23:45:00.100 INFO [my-single-app,f0e1d2c3b4a5f6e7,f0e1d2c3b4a5f6e7,false] 1234 --- [nio-8080-exec-3] c.e.m.MyController : Entering new-span-example endpoint
2025-06-23 23:45:00.105 INFO [my-single-app,f0e1d2c3b4a5f6e7,f0e1d2c3b4a5f6e7,false] 1234 --- [nio-8080-exec-3] c.e.m.MyService : I'm in the original span before new span
2025-06-23 23:45:00.300 INFO [my-single-app,f0e1d2c3b4a5f6e7,8a9b0c1d2e3f4a5b,false] 1234 --- [nio-8080-exec-3] c.e.m.MyService : I'm in the new custom span doing some cool work
2025-06-23 23:45:00.305 INFO [my-single-app,f0e1d2c3b4a5f6e7,f0e1d2c3b4a5f6e7,false] 1234 --- [nio-8080-exec-3] c.e.m.MyService : I'm back in the original span
2025-06-23 23:45:00.310 INFO [my-single-app,f0e1d2c3b4a5f6e7,f0e1d2c3b4a5f6e7,false] 1234 --- [nio-8080-exec-3] c.e.m.MyController : Exiting new-span-example endpoint
```

Remarquez comment le `spanId` change en `8a9b0c1d2e3f4a5b` dans la section `custom-internal-work` puis revient.

### 4.5. Traitement asynchrone

Sleuth s'intègre de manière transparente avec l'annotation `@Async` de Spring pour propager le contexte de trace à travers les limites des threads.

Premièrement, activez le traitement asynchrone dans votre classe d'application principale :

```java
@SpringBootApplication
@EnableAsync // Activer l'exécution asynchrone
public class MyApplication {
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
}
```

Ensuite, créez un service asynchrone :

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;

@Service
public class AsyncService {
    private static final Logger logger = LoggerFactory.getLogger(AsyncService.class);

    @Async
    public void performAsyncTask() throws InterruptedException {
        logger.info("Starting async task");
        Thread.sleep(500); // Simuler une tâche de longue durée
        logger.info("Finished async task");
    }
}

@RestController
public class MyController {
    private static final Logger logger = LoggerFactory.getLogger(MyController.class);

    @Autowired
    private AsyncService asyncService;

    @GetMapping("/async-example")
    public String asyncExample() throws InterruptedException {
        logger.info("Calling async task");
        asyncService.performAsyncTask();
        logger.info("Async task initiated, returning from controller");
        return "success";
    }
}
```

Les logs montreront le même `traceId` mais un `spanId` différent pour la méthode asynchrone, car elle s'exécute dans un nouveau thread et représente une nouvelle unité de travail :

```
2025-06-23 23:50:00.100 INFO [my-single-app,1a2b3c4d5e6f7a8b,1a2b3c4d5e6f7a8b,false] 1234 --- [nio-8080-exec-4] c.e.m.MyController : Calling async task
2025-06-23 23:50:00.105 INFO [my-single-app,1a2b3c4d5e6f7a8b,9c0d1e2f3a4b5c6d,false] 1234 --- [           task-1] c.e.m.AsyncService : Starting async task
2025-06-23 23:50:00.110 INFO [my-single-app,1a2b3c4d5e6f7a8b,1a2b3c4d5e6f7a8b,false] 1234 --- [nio-8080-exec-4] c.e.m.MyController : Async task initiated, returning from controller
// ... quelque temps plus tard ...
2025-06-23 23:50:00.605 INFO [my-single-app,1a2b3c4d5e6f7a8b,9c0d1e2f3a4b5c6d,false] 1234 --- [           task-1] c.e.m.AsyncService : Finished async task
```

Remarquez que le `traceId` reste le même, mais le `spanId` change pour la méthode asynchrone, et le nom du thread reflète également l'exécuteur asynchrone.

### 4.6. Personnalisation des noms de spans avec `@SpanName`

Vous pouvez utiliser l'annotation `@SpanName` pour fournir des noms plus significatifs pour vos spans générées automatiquement.

```java
import org.springframework.cloud.sleuth.annotation.SpanName;
import org.springframework.stereotype.Service;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@Service
public class AnnotatedService {
    private static final Logger logger = LoggerFactory.getLogger(AnnotatedService.class);

    @SpanName("Annotated_Service_Method") // Nom de span personnalisé
    public void annotatedMethod() throws InterruptedException {
        logger.info("Inside annotated method");
        Thread.sleep(50);
    }
}

// ... dans votre contrôleur ou un autre service ...
@Autowired
private AnnotatedService annotatedService;

@GetMapping("/annotated-span")
public String annotatedSpanExample() throws InterruptedException {
    logger.info("Calling annotated method");
    annotatedService.annotatedMethod();
    logger.info("Finished calling annotated method");
    return "success";
}
```

Les logs refléteront le nom de span personnalisé :

```
2025-06-23 23:55:00.100 INFO [my-single-app,g1h2i3j4k5l6m7n8,g1h2i3j4k5l6m7n8,false] 1234 --- [nio-8080-exec-5] c.e.m.MyController : Calling annotated method
2025-06-23 23:55:00.150 INFO [my-single-app,g1h2i3j4k5l6m7n8,g1h2i3j4k5l6m7n8,false] 1234 --- [nio-8080-exec-5] c.e.m.AnnotatedService : Inside annotated method (span name: Annotated_Service_Method)
2025-06-23 23:55:00.155 INFO [my-single-app,g1h2i3j4k5l6m7n8,g1h2i3j4k5l6m7n8,false] 1234 --- [nio-8080-exec-5] c.e.m.MyController : Finished calling annotated method
```

## 5\. Intégration avec Zipkin (Optionnel mais recommandé)

Bien que ce guide se concentre sur les applications uniques, la véritable puissance de Sleuth apparaît lorsqu'il est intégré à un système de traçage distribué comme Zipkin. Zipkin collecte les données de trace et de span exportées par Sleuth et fournit une interface utilisateur pour visualiser le flux et le minutage des requêtes.

Pour intégrer Zipkin, ajoutez la dépendance `spring-cloud-starter-zipkin` :

```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-zipkin</artifactId>
</dependency>
```

Par défaut, Sleuth tentera d'envoyer les traces à un collecteur Zipkin s'exécutant sur `http://localhost:9411`. Vous pouvez configurer cela dans `application.properties` :

```properties
spring.zipkin.base-url=http://localhost:9411
```

Vous pouvez exécuter un serveur Zipkin facilement avec Docker :

```bash
docker run -d -p 9411:9411 openzipkin/zipkin
```

Une fois Zipkin en cours d'exécution, votre application Spring Boot unique enverra automatiquement ses données de trace, et vous pourrez visualiser les traces sur `http://localhost:9411/`.

## 6\. Échantillonnage

Par défaut, Sleuth applique une stratégie d'échantillonnage pour éviter de submerger le système de traçage avec des données. Il échantillonne généralement un pourcentage de requêtes. Vous pouvez configurer le taux d'échantillonnage dans `application.properties` :

```properties
# Échantillonne 100% des requêtes
spring.sleuth.sampler.probability=1.0
```

Une valeur de `1.0` signifie que toutes les requêtes seront tracées, tandis que `0.1` signifie que 10% seront tracées.

## 7\. Conclusion

Spring Cloud Sleuth, même dans une application unique, améliore considérablement la journalisation et le débogage en injectant automatiquement `traceId` et `spanId` dans vos messages de log. Cela vous permet de suivre facilement le flux d'exécution d'une seule requête, même lorsqu'elle traverse différentes méthodes et threads. En comprenant les concepts fondamentaux des traces et des spans et en utilisant l'instrumentation automatique de Sleuth ou la création manuelle de spans, vous pouvez obtenir une bien meilleure observabilité de vos applications monolithiques. L'intégration avec Zipkin débloque en outre le potentiel de visualisation et d'analyse du comportement de votre application.
---
audio: false
generated: true
lang: fr
layout: post
title: Dépannage des `traceId` et `spanId` vides dans les journaux
translated: true
type: note
---

Les `traceId` et `spanId` sont vides dans vos lignes de log `[blog-server,,]`, probablement pour l'une des raisons suivantes :

* **Dépendance Sleuth manquante ou incorrecte :** Assurez-vous que la dépendance `spring-cloud-starter-sleuth` est correctement ajoutée dans le `pom.xml` (pour Maven) ou le `build.gradle` (pour Gradle) de votre projet, et que vous utilisez des versions compatibles de Spring Boot et Spring Cloud. Sans cette dépendance, l'auto-configuration de Spring Cloud Sleuth ne s'activera pas.

    ```xml
    <dependency>
        <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-sleuth</artifactId>
    </dependency>
    ```

* **Modèle de journalisation personnalisé :** Si vous avez défini un modèle de journalisation personnalisé (par exemple, dans `logback-spring.xml` ou `application.properties`), vous devez explicitement inclure les espaces réservés pour `traceId` et `spanId`. Si ces espaces réservés sont manquants, les identifiants n'apparaîtront pas dans vos logs même si Sleuth est actif.

    Pour Logback, assurez-vous que votre modèle inclut `%X{traceId}` et `%X{spanId}` :

    ```xml
    <pattern>%d{yyyy-MM-dd HH:mm:ss.SSS} %-5level [${spring.application.name:-},%X{traceId:-},%X{spanId:-}] %thread %logger{36} - %msg%n</pattern>
    ```

* **Aucun contexte de trace/span actif :** Bien que Sleuth instrumente automatiquement de nombreux composants Spring (comme `DispatcherServlet` pour les requêtes HTTP), il est possible que ces messages de log spécifiques soient générés dans un contexte où aucune trace ou span n'a encore été initiée ou propagée. Par exemple, certains logs très précoces du démarrage de l'application ou les logs provenant de threads non gérés par la propagation de contexte de Sleuth pourraient ne pas avoir ces identifiants. Cependant, pour les logs pendant le traitement actif d'une requête HTTP, comme `HttpEntityMethodProcessor` et `DispatcherServlet` complétant une requête, cela est moins courant si Sleuth est correctement configuré.

Pour résoudre le problème, vérifiez d'abord vos dépendances et votre configuration de journalisation. Si celles-ci sont correctes, assurez-vous que les requêtes atteignent bien votre application et sont traitées par le `DispatcherServlet` Spring MVC, ce qui devrait déclencher l'instrumentation de Sleuth.
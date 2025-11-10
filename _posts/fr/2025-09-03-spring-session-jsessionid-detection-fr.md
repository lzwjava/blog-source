---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Session de printemps, JSESSIONID et détection du serveur
translated: true
type: note
---

Décomposons cela en deux parties : comment **Spring Session/JSESSIONID** fonctionne, et comment déterminer si Spring s'exécute sur **Tomcat ou Netty**.

---

## 1. Comment Spring Session et `JSESSIONID` fonctionnent

* **JSESSIONID** est l'identifiant de session HTTP standard utilisé par les conteneurs de servlets (Tomcat, Jetty, Undertow, etc.).
* Lorsqu'un client effectue la première requête nécessitant une session, le conteneur (ou Spring Session si vous l'utilisez) génère un ID de session aléatoire, stocke les données de session sur le serveur et renvoie l'ID au client dans un en-tête `Set-Cookie`.
* Le client inclut ce cookie `JSESSIONID` dans les requêtes suivantes, permettant au serveur de trouver la session correcte.
* Par défaut, les données de session sont stockées **dans la mémoire du conteneur de servlets**. Par exemple :

  * Tomcat stocke les sessions en mémoire (sauf si vous configurez la persistance).
  * Si vous utilisez **Spring Session**, le stockage des sessions peut être externalisé (Redis, JDBC, Hazelcast, etc.), tout en utilisant toujours le cookie `JSESSIONID` pour identifier les utilisateurs.
* Spring Security et d'autres fonctionnalités de Spring s'appuient sur ce mécanisme de session pour l'authentification et la gestion d'état.

---

## 2. Comment savoir si Spring utilise Tomcat ou Netty

Spring Boot peut s'exécuter avec différents serveurs embarqués :

* **Tomcat** (par défaut pour spring-boot-starter-web)
* **Jetty** (si vous échangez les dépendances)
* **Undertow** (conteneur de servlets alternatif)
* **Netty** (utilisé par Spring WebFlux, qui n'est pas basé sur les servlets)

### Méthodes pour vérifier :

1. **Examinez vos dépendances**

   * Si votre `pom.xml` ou `build.gradle` inclut `spring-boot-starter-web`, il utilise **Tomcat** par défaut.
   * S'il inclut `spring-boot-starter-webflux`, il utilise **Netty** par défaut.

2. **Vérifiez les logs de démarrage**

   * Lorsque l'application démarre, Spring Boot journalise le serveur embarqué.
   * Exemple (Tomcat) :

     ```
     Tomcat started on port(s): 8080 (http)
     ```
   * Exemple (Netty) :

     ```
     Netty started on port(s): 8080
     ```

3. **Vérifiez les classes à l'exécution**

   * Dans le code ou via l'actuator, vérifiez quelles classes de serveur sont chargées.
   * Les classes Tomcat commencent par `org.apache.catalina.`
   * Les classes Netty commencent par `io.netty.`

---

✅ **Résumé** :

* `JSESSIONID` est simplement le cookie qui pointe vers une session côté serveur, gérée par Tomcat (par défaut) ou par Spring Session (Redis/BDD).
* Vous pouvez déterminer si Spring utilise **Tomcat ou Netty** en vérifiant les dépendances, les logs de démarrage ou les classes à l'exécution.

---

Souhaitez-vous que j'explique également **comment la gestion des sessions diffère entre Spring MVC (Tomcat) et Spring WebFlux (Netty)** ? C'est là que la distinction est la plus importante.
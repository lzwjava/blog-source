---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Options de déploiement d'applications Web expliquées
translated: true
type: note
---

Compris — laissez-moi vous expliquer clairement ces options.

### Option 1 : Configuration de développement rapide (Recommandée)

C'est la façon la plus simple de démarrer le projet pendant le développement.
Si votre `pom.xml` inclut un plugin Tomcat ou Jetty, vous pouvez lancer l'application directement avec :

```bash
mvn tomcat7:run
```

ou

```bash
mvn jetty:run
```

Cela lance l'application web dans un Tomcat/Jetty embarqué sans construire un WAR ou déployer manuellement. Si vous n'avez pas déjà le plugin, vous devrez d'abord l'ajouter au `pom.xml`.

---

### Option 2 : Construire et déployer le WAR

C'est l'approche plus « traditionnelle ». Vous empaquetez l'application dans un fichier WAR :

```bash
mvn clean package
```

Cela produit quelque chose comme `target/playground-server-1.0.war`.
Vous copiez ensuite ce WAR dans le dossier `webapps/` d'un serveur Tomcat/Jetty autonome, redémarrez le serveur, et accédez à l'application déployée dans le navigateur.

---

### Option 3 : Utiliser un serveur embarqué (Configuration manuelle)

Actuellement, votre `Application.main()` démarre seulement le contexte Spring — il ne démarre pas réellement un serveur web.
Si vous voulez que l'application elle-même lance Tomcat (sans dépendre d'un serveur externe), vous devriez modifier votre classe principale pour configurer et démarrer une instance Tomcat embarquée de manière programmatique.

Cela vous donne un JAR exécutable autonome, mais nécessite du code de configuration supplémentaire.

---

### Option 4 : Migration vers Spring Boot

Ce projet a **une certaine configuration de test Spring Boot**, mais n'est pas encore une vraie application Spring Boot. C'est pourquoi l'exécution de :

```bash
mvn spring-boot:run
```

ne fonctionne pas.

Si vous le souhaitez, vous pouvez migrer :

* Ajoutez les dépendances starter Spring Boot appropriées.
* Changez votre classe principale en `@SpringBootApplication`.
* Ensuite, vous pourriez simplement exécuter avec `mvn spring-boot:run` ou même `java -jar target/app.jar`.

C'est l'approche la plus moderne, mais nécessite quelques modifications de votre code et du `pom.xml`.

---

✅ **En bref** :

* Si vous voulez juste tester rapidement → utilisez l'**Option 1**.
* Si vous déployez sur un serveur existant → utilisez l'**Option 2**.
* Si vous voulez une application autonome sans Tomcat externe → utilisez l'**Option 3**.
* Si vous voulez moderniser et simplifier à long terme → utilisez l'**Option 4**.

---

Voulez-vous que je vous montre **l'extrait exact du `pom.xml`** pour l'Option 1 (plugin Tomcat/Jetty) afin que vous puissiez exécuter `mvn tomcat7:run` immédiatement ?
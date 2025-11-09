---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: API JMS et JNDI pour WebSphere
translated: true
type: note
---

### Packages et APIs requis pour JMS en Java

Pour utiliser l'extrait de code JMS que vous avez référencé (pour rechercher et se connecter à une fabrique de connexions JMS dans IBM WebSphere Application Server), vous devrez importer les packages Java pertinents. Ce sont des APIs standard de l'écosystème Java EE/Jakarta EE :

- **JNDI (Java Naming and Directory Interface)** : Pour la recherche `InitialContext`.
  - Package : `javax.naming` (ou `jakarta.naming` dans les versions plus récentes de Jakarta EE).
  - Classe principale : `InitialContext` – C'est le point de départ pour les opérations JNDI. Il fournit un contexte pour rechercher des ressources (comme des fabriques JMS ou des files d'attente) par leur nom JNDI (p. ex., `"jms/MyConnectionFactory"`). Dans un conteneur comme WAS, il se connecte automatiquement au service d'annuaire du serveur.

- **API JMS (Java Message Service)** : Pour créer des connexions, des sessions, des expéditeurs/récepteurs et des messages.
  - Package : `javax.jms` (JMS 1.1/2.0) ou `jakarta.jms` (Jakarta JMS 3.0+ dans les EE modernes).
  - Interfaces principales : `QueueConnectionFactory`, `QueueConnection`, `QueueSession`, `QueueSender`, `Queue`, `TextMessage`, etc.

Exemple d'imports en haut de votre classe Java :
```java
import javax.naming.InitialContext;
import javax.naming.NamingException;
import javax.jms.QueueConnectionFactory;
import javax.jms.QueueConnection;
import javax.jms.QueueSession;
import javax.jms.Queue;
import javax.jms.QueueSender;
import javax.jms.TextMessage;
import javax.jms.JMSException;
```

**Qu'est-ce que `InitialContext` ?**  
C'est une classe dans l'API JNDI qui agit comme un point d'entrée vers un service d'annuaire. Dans votre code :  
```java
InitialContext ctx = new InitialContext();  // Crée un contexte par défaut lié à l'environnement JNDI du serveur d'applications
QueueConnectionFactory qcf = (QueueConnectionFactory) ctx.lookup("jms/MyConnectionFactory");  // Recherche la fabrique préconfigurée par son nom JNDI
```  
Aucune propriété n'est nécessaire dans le constructeur pour les applications s'exécutant *à l'intérieur* de WAS, car le conteneur injecte l'environnement (p. ex., via `java.naming.factory.initial`). Si vous exécutez un client autonome *en dehors* de WAS, vous devriez passer une `Hashtable` avec des propriétés comme l'URL du fournisseur.

### Dépendances Maven (pom.xml)

Si votre application Java est **déployée et s'exécute à l'intérieur de WAS** (p. ex., en tant qu'application web, EJB ou entreprise bean) :  
- **Aucune dépendance supplémentaire n'est nécessaire**. WAS fournit les APIs JMS et JNDI prêtes à l'emploi dans le cadre de son runtime Java EE. Compilez simplement contre elles (elles sont dans le classpath pendant la construction/le déploiement).  
- Dans `pom.xml`, vous pouvez les déclarer explicitement avec `<scope>provided</scope>` pour éviter de les inclure dans votre WAR/EAR (le garde léger) :  
  ```xml
  <dependencies>
      <dependency>
          <groupId>javax.jms</groupId>  <!-- Ou jakarta.jms pour les versions plus récentes -->
          <artifactId>javax.jms-api</artifactId>
          <version>2.0.1</version>  <!-- JMS 2.0, compatible avec WAS 8.5+ -->
          <scope>provided</scope>
      </dependency>
      <dependency>
          <groupId>javax.naming</groupId>
          <artifactId>javax.naming-api</artifactId>
          <version>1.0</version>  <!-- JNDI 1.0, standard -->
          <scope>provided</scope>
      </dependency>
  </dependencies>
  ```

Si votre application est un **client autonome** (s'exécutant en dehors de WAS, p. ex., un client léger se connectant au serveur) :  
- Vous aurez besoin des bibliothèques **WebSphere Application Client** pour une prise en charge JMS complète via IIOP. Téléchargez le package client "IBM WebSphere Application Server traditional" depuis IBM, puis ajoutez-le à votre classpath.  
- Dans `pom.xml`, incluez :  
  ```xml
  <dependency>
      <groupId>com.ibm.ws</groupId>
      <artifactId>was-jms-client</artifactId>  <!-- Approximatif ; utilisez le dépôt Maven d'IBM s'il est disponible -->
      <version>9.0.5</version>  <!-- Correspond à votre version de WAS -->
  </dependency>
  ```  
  Ou utilisez les JARs complets du client léger (p. ex., `com.ibm.ws.orb_8.5.5.jar`, `com.ibm.ws.jndi_*.jar`). Vérifiez la documentation d'IBM pour la configuration exacte.

Pour la migration vers Jakarta EE (post-2020), passez aux packages `jakarta.*`, mais WAS 9.x utilise toujours `javax.*` par défaut — activez Jakarta via les feature packs si nécessaire.

[Documentation de l'API JMS WebSphere IBM](https://www.ibm.com/docs/en/was/9.0.5?topic=resources-jms-api)  
[Tutoriel JNDI Java EE](https://docs.oracle.com/javase/tutorial/jndi/)
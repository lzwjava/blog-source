---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Guide de triage des délais d’attente Spring JDBC
translated: true
type: note
---

Voici le modèle mental et un guide de triage rapide.

# Fonctionnement (WAS + Spring + JDBC)

1.  **DataSource réside dans WAS**

    * Vous définissez un fournisseur JDBC et une **DataSource** (généralement `XA` pour les transactions globales, ou non-XA) dans la console d'administration WAS.
    * WAS gère le **pool de connexions JCA** et distribue les connexions JDBC.

2.  **Spring obtient la DataSource via JNDI**

    * Votre application Spring recherche la DataSource du serveur (par exemple, `java:comp/env/jdbc/MyDS`) et l'encapsule :

        * JDBC simple : `JdbcTemplate` utilise cette DataSource.
        * JPA/Hibernate : `EntityManagerFactory` l'utilise.
    * Les transactions sont généralement **JTA du conteneur** (`WebSphereUowTransactionManager` ou JTA standard). L'annotation `@Transactional` de Spring rejoint la transaction du conteneur.

3.  **Chemin d'appel**

    * Requête Web → thread WebContainer → service Spring → début de la transaction (JTA) → `DataSource.getConnection()` depuis le **pool WAS** → SQL via le pilote → Base de données.
    * Les timeouts peuvent se déclencher à plusieurs niveaux (Spring, JPA, pool WAS, transaction JTA, pilote JDBC/BDD, réseau).

# Quand un timeout se produit — identifier le type

Pensez en quatre catégories. Le message/la pile d'exécution vous indique généralement laquelle.

1.  **Timeout d'acquisition de connexion**
    Symptôme : attente d'une connexion du pool.
    Recherchez des messages concernant l'épuisement du pool ou `J2CA0086W` / `J2CA0030E`.
    Paramètres typiques : *Maximum Connections*, *Connection Timeout*, *Aged Timeout*, *Purge Policy*.

2.  **Timeout de transaction (JTA)**
    Symptôme : messages `WTRN`/`Transaction` ; exception comme *"Transaction timed out after xxx seconds"*.
    Paramètre typique : **Total transaction lifetime timeout**. Peut interrompre des opérations BDD longues même si la BDD fonctionne toujours.

3.  **Timeout de requête/statement**
    Symptôme : `java.sql.SQLTimeoutException`, "query timeout" Hibernate/JPA, ou `QueryTimeoutException` de Spring.
    Paramètres :

    * Spring : `JdbcTemplate.setQueryTimeout(...)`, Hibernate `javax.persistence.query.timeout` / `hibernate.jdbc.timeout`.
    * Propriétés personnalisées de la DataSource WAS (exemples DB2) : `queryTimeout`, `queryTimeoutInterruptProcessingMode`.
    * Timeout de statement côté pilote/BDD.

4.  **Timeout de socket/lecture / réseau**
    Symptôme : après un temps d'inactivité lors d'une extraction longue ; `SocketTimeoutException` de bas niveau ou code fournisseur.
    Paramètres : `loginTimeout`/`socketTimeout` du pilote, pare-feu/NAT inactifs, keepalives de la BDD.

# Où vérifier (par couche)

**Chemins dans la console d'administration WAS (WAS traditionnel)**

* Fournisseur JDBC / DataSource :
  Resources → JDBC → Data sources → *VotreDS* →

    * *Connection pool properties* : **Connection timeout**, **Maximum connections**, **Reap time**, **Unused timeout**, **Aged timeout**, **Purge policy**.
    * *Custom properties* : spécifiques au fournisseur (par exemple, DB2 `queryTimeout`, `currentSQLID`, `blockingReadConnectionTimeout`, `queryTimeoutInterruptProcessingMode`).
    * *JAAS – J2C* si les alias d'authentification sont importants.
* Transactions :
  Application servers → *server1* → Container Settings → **Container Services → Transaction Service** → **Total transaction lifetime timeout**, **Maximum transaction timeout**.
* WebContainer :
  Taille du pool de threads (si les requêtes s'accumulent).

**Journaux et traces**

* WAS traditionnel : `<profile_root>/logs/<server>/SystemOut.log` et `SystemErr.log`.
  Composants clés : `RRA` (adaptateurs de ressources), `JDBC`, `ConnectionPool`, `WTRN` (transactions).
  Activer la trace (début concis) :

  ```
  RRA=all:WTRN=all:Transaction=all:JDBC=all:ConnectionPool=all
  ```

  Recherchez :

    * `J2CA0086W`, `J2CA0114W` (problèmes de pool/connexion)
    * `WTRN0037W`, `WTRN0124I` (timeouts/annulations de transaction)
    * Exceptions `DSRA`/`SQL` avec les codes SQL du fournisseur.
* Liberty : `messages.log` sous `wlp/usr/servers/<server>/logs/`.

**PMI / Surveillance**

* Activez **PMI** pour les métriques des pools de connexions JDBC et des transactions. Surveillez :

    * Taille du pool, nombre de connexions utilisées, en attente, temps d'attente, timeouts.
    * Timeouts/annulations de transaction.

**Journaux de l'application Spring/JPA**

* Activez le SQL + le timing dans votre application (`org.hibernate.SQL`, `org.hibernate.type`, debug Spring JDBC) pour corréler les durées avec les timeouts.

**Base de données et pilote**

* DB2 : `db2diag.log`, `MON_GET_PKG_CACHE_STMT`, moniteurs d'activité, timeouts au niveau du statement.
* Propriétés du pilote dans la DataSource WAS ou `DriverManager` si vous n'utilisez pas la DS du conteneur (pas typique sur WAS).

**Réseau**

* Équipements intermédiaires avec des timeouts d'inactivité. Paramètres keepalive du système d'exploitation / du pilote.

# Flux de triage rapide

1.  **Classifiez le timeout**

    * *Attente de connexion ?* Recherchez les avertissements de pool `J2CA`. Si oui, augmentez **Maximum connections**, corrigez les fuites, ajustez le pool, définissez **Purge Policy = EntirePool** pour les événements "poison".
    * *Timeout de transaction ?* Messages `WTRN`. Augmentez **Total transaction lifetime timeout** ou réduisez le travail par transaction ; évitez d'encapsuler de gros travaux par lots dans une seule transaction.
    * *Timeout de requête ?* `SQLTimeoutException` ou `QueryTimeout` Spring/Hibernate. Alignez les timeouts **Spring/Hibernate** avec ceux de la **DS WAS** et de la **BDD** ; évitez les paramètres conflictuels.
    * *Timeout de socket/lecture ?* Messages réseau/pilote. Vérifiez `socketTimeout`/`loginTimeout` du pilote, les keepalives de la BDD et les pare-feu.

2.  **Corrélez les durées**

    * Comparez la durée de l'échec avec les seuils configurés (par exemple, "échoue à ~30s" → recherchez un paramètre à 30s : timeout de requête Spring à 30s ? durée de vie de la transaction à 30s ? attente du pool à 30s ?).

3.  **Vérifiez l'état du pool**

    * PMI : **waiters** > 0 ? **in-use** est proche de **max** ? Des détenteurs de connexion de longue durée ? Envisagez d'activer la **détection de fuite de connexion** (la trace RRA montre qui a pris la connexion).

4.  **Visibilité sur la BDD**

    * Confirmez sur la BDD : le statement était-il encore en cours d'exécution ? A-t-il été annulé ? Des attentes de verrous ? Si verrous → considérez le timeout de verrou vs. le timeout de statement.

# Paramètres utiles et pièges (exemples WAS + DB2)

* **Total transaction lifetime timeout** (niveau serveur) tuera les requêtes longues même si vous définissez un timeout Spring/Hibernate plus élevé. Maintenez-les cohérents.
* **queryTimeoutInterruptProcessingMode** (propriété personnalisée de la DataSource pour DB2) : contrôle comment DB2 doit interrompre une requête expirée (coopératif/forcé). Aide à éviter les threads bloqués après les timeouts.
* **Purge policy** : `EntirePool` peut récupérer plus rapidement des états SQL fatals (par exemple, redémarrage de la BDD) au prix d'une perturbation.
* **Aged/Unused timeout** : retire les connexions obsolètes pour éviter les timeouts d'inactivité des pare-feu/NAT.
* **Validation** : activez **validation by SQL** ou **validation timeout** pour que les connexions mortes soient détectées avant utilisation.
* **Pools de threads** : si les threads WebContainer sont saturés, les *symptômes ressemblent à des timeouts*. Assurez-vous que les pools de threads WebContainer et Default sont dimensionnés correctement.

# Exemples minimaux de configuration Spring

**DataSource JNDI (XML)**

```xml
<jee:jndi-lookup id="dataSource" jndi-name="java:comp/env/jdbc/MyDS" expected-type="javax.sql.DataSource"/>
<bean id="txManager" class="org.springframework.transaction.jta.JtaTransactionManager"/>
<tx:annotation-driven transaction-manager="txManager"/>
```

**Timeout de requête JdbcTemplate (Java)**

```java
@Bean JdbcTemplate jdbcTemplate(DataSource ds) {
  JdbcTemplate jt = new JdbcTemplate(ds);
  jt.setQueryTimeout(60); // secondes
  return jt;
}
```

**Timeout Hibernate/JPA**

```properties
javax.persistence.query.timeout=60000  # ms
hibernate.jdbc.timeout=60              # secondes
```

# Que capturer lorsque vous escaladez

* Texte exact de l'exception + pile d'exécution.
* Horodatages : début de la requête, début de la transaction, début de la requête, heure de l'erreur.
* Configuration du pool de la DS WAS (capture d'écran ou valeurs), timeouts du Service de Transaction.
* Instantané PMI (en attente, en cours d'utilisation, nombre de timeouts).
* Vue de la session/du statement sur la BDD au moment de l'échec.
* Notes sur la topologie du réseau (pare-feu, proxys, minuteries d'inactivité).

Si vous collez un extrait d'exception spécifique (état J2CA/WTRN/SQL), je peux identifier exactement la couche et le paramètre correspondant à ajuster.
---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Guide d'Emballage WAR vs EAR
translated: true
type: note
---

Voici une comparaison pratique, sans tableau, entre les packaging Maven **WAR** et **EAR**, et comment les utiliser dans des projets réels.

# À quoi sert chaque packaging

* **WAR (`packaging: war`)** – Une application web unique : servlets/Jakarta REST, JSP/JSF, Spring MVC/Boot (en tant que WAR), etc. Déployée dans un conteneur de servlets (Tomcat/Jetty) ou dans la couche web d'un serveur d'applications complet.
* **EAR (`packaging: ear`)** – Un regroupement de plusieurs modules déployés ensemble sur un serveur d'applications Java EE/Jakarta EE complet (WildFly/JBoss EAP, WebLogic, WebSphere). Contient typiquement un ou plusieurs WARs, des JARs EJB et des bibliothèques partagées dans une seule unité de déploiement.

# Quand choisir l'un ou l'autre

* Choisissez **WAR** si vous avez une application web unique ou une application Spring Boot et que vous n'avez pas besoin d'EJB ou des fonctionnalités serveur multi-modules.
* Choisissez **EAR** si vous devez déployer plusieurs modules ensemble (par exemple, EJBs + plusieurs WARs + librairies partagées), si vous avez besoin de services du serveur d'applications (XA, domaines de sécurité centralisés, JMS, transactions distribuées) entre les modules, ou si votre organisation impose les EAR.

# Contenu de l'artefact

* Contenu du **WAR** : `/WEB-INF/classes`, `/WEB-INF/lib`, `web.xml` optionnel (ou annotations), ressources statiques. Un classloader par WAR dans la plupart des serveurs.
* Contenu du **EAR** : `*.war`, `*.jar` (EJBs/utilitaires), `META-INF/application.xml` (ou annotations/configuration simplifiée), et un `lib/` optionnel pour les bibliothèques partagées entre les modules. Fournit un classloader au niveau EAR visible par tous les modules.

# Considérations sur les dépendances et le classloading

* **WAR** : Déclarez les APIs servlet/Jakarta EE comme `provided` ; tout le reste va dans `/WEB-INF/lib`. L'isolation est plus simple ; moins de conflits de versions.
* **EAR** : Placez les librairies communes dans le `lib/` de l'EAR (via `maven-ear-plugin`), ainsi tous les modules partagent une même version. Attention aux conflits entre les librairies des modules et les APIs fournies par le serveur ; alignez les versions et utilisez `provided` où c'est approprié.

# Plugins Maven que vous utiliserez

* **Projets WAR** : `maven-war-plugin`
* **Aggrégateur EAR** : `maven-ear-plugin`
* **Modules EJB (le cas échéant)** : `maven-ejb-plugin`
* Le parent/aggrégateur utilise souvent `packaging: pom` pour lier les modules.

# Exemples minimaux

Application web unique (WAR) :

```xml
<!-- pom.xml -->
<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.example</groupId><artifactId>my-web</artifactId><version>1.0.0</version>
  <packaging>war</packaging>

  <dependencies>
    <!-- Utilisez provided pour les APIs du serveur -->
    <dependency>
      <groupId>jakarta.platform</groupId><artifactId>jakarta.jakartaee-web-api</artifactId>
      <version>10.0.0</version><scope>provided</scope>
    </dependency>
    <!-- Vos dépendances d'application -->
  </dependencies>

  <build>
    <plugins>
      <plugin>
        <artifactId>maven-war-plugin</artifactId>
        <version>3.4.0</version>
        <!-- Optionnel : configurer webResources, warName, filtering -->
      </plugin>
    </plugins>
  </build>
</project>
```

EAR multi-modules avec un WAR et un EJB :

```xml
<!-- parent/pom.xml -->
<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.example</groupId><artifactId>my-app</artifactId><version>1.0.0</version>
  <packaging>pom</packaging>
  <modules>
    <module>ejb-module</module>
    <module>web-module</module>
    <module>ear-assembly</module>
  </modules>
</project>
```

```xml
<!-- ejb-module/pom.xml -->
<project>
  <parent>…</parent>
  <artifactId>ejb-module</artifactId>
  <packaging>ejb</packaging>
  <dependencies>
    <dependency>
      <groupId>jakarta.platform</groupId><artifactId>jakarta.jakartaee-api</artifactId>
      <version>10.0.0</version><scope>provided</scope>
    </dependency>
  </dependencies>
</project>
```

```xml
<!-- web-module/pom.xml -->
<project>
  <parent>…</parent>
  <artifactId>web-module</artifactId>
  <packaging>war</packaging>
  <dependencies>
    <dependency>
      <groupId>jakarta.platform</groupId><artifactId>jakarta.jakartaee-web-api</artifactId>
      <version>10.0.0</version><scope>provided</scope>
    </dependency>
    <dependency>
      <groupId>com.example</groupId><artifactId>ejb-module</artifactId><version>1.0.0</version>
      <type>ejb</type> <!-- permet l'injection @EJB -->
    </dependency>
  </dependencies>
</project>
```

```xml
<!-- ear-assembly/pom.xml -->
<project>
  <parent>…</parent>
  <artifactId>ear-assembly</artifactId>
  <packaging>ear</packaging>

  <dependencies>
    <dependency>
      <groupId>com.example</groupId><artifactId>web-module</artifactId><version>1.0.0</version>
      <type>war</type>
    </dependency>
    <dependency>
      <groupId>com.example</groupId><artifactId>ejb-module</artifactId><version>1.0.0</version>
      <type>ejb</type>
    </dependency>
    <!-- Bibliothèques à placer dans EAR/lib partagées par tous les modules -->
    <dependency>
      <groupId>com.fasterxml.jackson.core</groupId><artifactId>jackson-databind</artifactId>
      <version>2.17.2</version>
    </dependency>
  </dependencies>

  <build>
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-ear-plugin</artifactId>
        <version>3.4.0</version>
        <configuration>
          <defaultLibBundleDir>lib</defaultLibBundleDir>
          <modules>
            <webModule>
              <groupId>com.example</groupId>
              <artifactId>web-module</artifactId>
              <contextRoot>/myapp</contextRoot>
            </webModule>
            <ejbModule>
              <groupId>com.example</groupId>
              <artifactId>ejb-module</artifactId>
            </ejbModule>
          </modules>
          <!-- Optionnel : générer application.xml, ou en fournir un personnalisé -->
          <generateApplicationXml>true</generateApplicationXml>
        </configuration>
      </plugin>
    </plugins>
  </build>
</project>
```

Résultats de la construction :

* `mvn -pl web-module -am clean package` → `web-module-1.0.0.war`
* `mvn -pl ear-assembly -am clean package` → `ear-assembly-1.0.0.ear` contenant le WAR, l'EJB, et `lib/`.

# Différences opérationnelles importantes

* **Cible de déploiement**

  * WAR : conteneur de servlets ou couche web du serveur d'applications.
  * EAR : serveur d'applications complet ; déploie tous les modules de manière atomique.
* **Transactions et messagerie**

  * Le WAR seul utilise ce que le conteneur expose ; les configurations complexes XA/JMS résident souvent dans les EJBs au sein des EARs.
* **Gestion de version et déploiement**

  * WAR : simple à reconstruire et redéployer pour une application unique.
  * EAR : coordonne les versions de nombreux modules ; une unité de déploiement pour la cohérence.
* **Temps de démarrage et développement local**

  * WAR : retour rapide, runtime plus léger.
  * EAR : plus lourd ; l'intégration IDE/serveur aide mais les cycles sont plus lents.
* **Note sur Spring Boot moderne**

  * Boot préfère le **JAR** exécutable ; le WAR est supporté si vous déployez vers un conteneur externe.
  * Boot **ne** cible **pas** EAR ; si vous devez utiliser un serveur d'applications, déployez Boot en tant que WAR, et évitez EAR sauf si votre plateforme l'exige.

# Pièges courants et conseils

* Utilisez `provided` pour les APIs du serveur pour éviter de les inclure.
* Pour les EARs, placez les librairies partagées dans `defaultLibBundleDir` pour éviter les copies dupliquées dans chaque WAR/EJB.
* Alignez les versions Jakarta EE entre les modules ; les incohérences provoquent des erreurs de classloading.
* Sur WebLogic/WebSphere, faites attention aux politiques de classloader (parent-first vs parent-last) ; parfois vous avez besoin de descripteurs spécifiques au fournisseur.
* Si vous n'avez pas besoin d'EJBs/XA, un WAR simple (ou un Boot JAR) est plus simple et généralement plus portable.

Si vous me dites votre serveur d'applications (Tomcat vs WildFly/WebLogic/etc.) et si vous avez des EJBs ou plusieurs applications web, je peux esquisser les POMs et descripteurs de déploiement exacts dont vous aurez besoin.
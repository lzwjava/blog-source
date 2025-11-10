---
audio: false
generated: true
lang: fr
layout: post
title: 'Guide des micromètres : outils et observabilité'
translated: true
type: note
---

Ce guide complet couvre deux sujets distincts : **Les Micromètres (l'outil de mesure)** et **Micrometer (la façade d'observabilité pour les applications Java, notamment Spring Boot), en se concentrant sur les solutions de tracing.**

Décomposons-les :

-----

## Partie 1 : Guide Complet sur les Micromètres (Outil de Mesure)

Un micromètre, souvent appelé palmer, est un instrument de mesure de précision utilisé pour obtenir des mesures très précises de petites distances, généralement de l'ordre du millième de pouce ou du centième de millimètre. Il est largement utilisé dans les domaines de l'ingénierie, de l'usinage, de la fabrication et scientifiques où les dimensions précises sont critiques.

### 1\. Qu'est-ce qu'un Micromètre ?

Fondamentalement, un micromètre utilise un mécanisme à vis usiné avec précision pour transformer un mouvement rotatif en mouvement linéaire. Cela permet des réglages fins et des lectures précises des dimensions d'un objet en le serrant entre une enclume fixe et un broche mobile.

### 2\. Composants Clés d'un Micromètre :

  * **Bâti :** Le corps principal en forme de C qui maintient tous les autres composants. Il assure la stabilité et doit être manipulé avec précaution pour éviter les erreurs de dilatation thermique.
  * **Enclume :** La face de mesure fixe contre laquelle l'objet est placé.
  * **Broche :** La face de mesure mobile qui se déplace vers ou s'éloigne de l'enclume lorsque le tambour est tourné.
  * **Barillet (ou Corps) :** La partie fixe du micromètre qui abrite l'échelle linéaire principale, affichant les nombres entiers et les demi-incréments (par exemple, en pouces ou en millimètres).
  * **Tambour :** La partie rotative qui déplace la broche et possède une échelle finement graduée pour des lectures plus précises.
  * **Limiteur de force (ou cliquet) :** Situé à l'extrémité du tambour, il assure une pression de mesure constante en glissant lorsque la force correcte est appliquée, empêchant un serrage excessif et la déformation de la pièce.
  * **Verrou (ou levier de blocage) :** Utilisé pour bloquer la broche en place une fois qu'une mesure a été prise, empêchant tout mouvement accidentel et préservant la lecture.

### 3\. Types de Micromètres :

Il existe différents types de micromètres, chacun conçu pour des tâches de mesure spécifiques :

  * **Micromètre externe :** Le type le plus courant, utilisé pour mesurer les dimensions externes comme le diamètre d'un arbre ou l'épaisseur d'une plaque.
  * **Micromètre interne :** Utilisé pour mesurer les dimensions internes, comme le diamètre d'un alésage ou d'un trou. Ils ont souvent des conceptions différentes, comme les micromètres tubulaires ou à mâchoires.
  * **Micromètre de profondeur :** Utilisé pour mesurer la profondeur des trous, des rainures ou des épaulements.
  * **Micromètre pour filetages :** Conçu pour mesurer le diamètre primitif des filetages de vis.
  * **Micromètre à palpeurs sphériques :** Doté d'enclumes/broches de forme sphérique pour mesurer l'épaisseur des surfaces courbes ou des caractéristiques spécifiques comme les parois de tubes.
  * **Micromètre à disques :** Possède des faces de mesure plates et en forme de disque pour mesurer les matériaux minces, le papier ou les dents d'engrenages.
  * **Micromètre numérique :** Doté d'un affichage électronique pour des lectures numériques directes, éliminant l'erreur de parallaxe et facilitant les lectures.
  * **Micromètre analogique :** Nécessite une lecture manuelle des échelles sur le barillet et le tambour.
  * **Micromètre à vernier :** Comprend une échelle vernier supplémentaire pour une précision encore plus élevée, permettant des lectures au-delà des graduations principales du tambour.

### 4\. Comment Lire un Micromètre (Exemple Analogique/Impérial) :

Bien que les lectures spécifiques varient entre le système impérial (pouces) et le système métrique (millimètres) et entre les modèles analogiques/numériques, le principe général pour les micromètres analogiques est le suivant :

1.  **Lire l'Échelle du Barillet (Échelle Principale) :**
      * **Pouces Entiers :** Notez la marque de pouce entier la plus grande visible.
      * **Dixièmes de Pouce (0,100") :** Chaque ligne numérotée sur le barillet représente 0,100 pouce.
      * **Vingt-cinq Millièmes (0,025") :** Chaque ligne non numérotée entre les marques des dixièmes représente 0,025 pouce.
2.  **Lire l'Échelle du Tambour :**
      * Le tambour a 25 graduations, chaque marque représentant 0,001 pouce.
      * Lisez la ligne sur le tambour qui s'aligne avec la ligne d'index sur le barillet.
3.  **Combiner les Lectures :** Additionnez les valeurs du barillet (pouces entiers, dixièmes et vingt-cinq millièmes) et du tambour (millièmes) pour obtenir la mesure finale.

**Exemple (Impérial) :**

  * Barillet :
      * Disons que vous voyez "1" (pour 1,000")
      * Puis 3 lignes après le "1" (3 x 0,100" = 0,300")
      * Et 2 lignes en dessous de la ligne principale (2 x 0,025" = 0,050")
      * Total du Barillet : 1,000 + 0,300 + 0,050 = 1,350"
  * Tambour :
      * La 15ème marque sur le tambour s'aligne avec la ligne d'index (0,015")
  * **Lecture Totale :** 1,350" + 0,015" = **1,365"**

### 5\. Utilisation Correcte et Bonnes Pratiques :

  * **Propreté :** Assurez-vous toujours que les faces de mesure (enclume et broche) sont propres et exemptes de poussière, d'huile ou de débris.
  * **Mise à Zéro :** Avant utilisation, toujours "mettre à zéro" le micromètre. Fermez doucement les faces de mesure en utilisant le limiteur de force jusqu'à ce qu'elles se touchent. La lecture doit être 0,000 (ou la plage de départ, par exemple 25-50mm). Sinon, ajustez le micromètre pour l'erreur zéro. Les micromètres numériques ont généralement un bouton de réinitialisation.
  * **Température :** Manipulez le micromètre par son bâti isolant ou portez des gants, car la chaleur corporelle peut provoquer une dilatation thermique et affecter la précision, surtout pour les micromètres de grande taille. Laissez l'outil et l'objet atteindre la température ambiante.
  * **Pression Constante :** Utilisez toujours le limiteur de force pour appliquer une pression de mesure constante et appropriée. Un serrage excessif peut déformer l'objet ou le micromètre.
  * **Positionnement de l'Objet :** Positionnez l'objet perpendiculairement entre l'enclume et la broche pour éviter des lectures biaisées.
  * **Mesures Multiples :** Pour les dimensions critiques, prenez plusieurs mesures à différents points de l'objet pour tenir compte des variations.
  * **Stockage :** Rangez les micromètres dans leurs étuis de protection pour éviter les dommages.
  * **Étalonnage :** Vérifiez et étalonnez régulièrement les micromètres par rapport à des étalons connus (par exemple, des jauges étalons) pour garantir leur exactitude.

-----

## Partie 2 : Micrometer comme Solution de Tracing pour les Projets Spring Java

Dans le contexte des projets Spring Java, "Micrometer" désigne une **façade d'observabilité d'application** qui fournit une API indépendante du fournisseur pour instrumenter les applications basées sur la JVM. Il vous permet de collecter et d'exporter diverses données de télémétrie, y compris les métriques, la journalisation et le **tracing distribué**.

Micrometer Tracing est le successeur de Spring Cloud Sleuth et est conçu pour fournir une visibilité sur les systèmes distribués complexes en suivant les requêtes à travers plusieurs services.

### 1\. Qu'est-ce que le Tracing Distribué ?

Dans une architecture de microservices, une seule requête utilisateur traverse souvent plusieurs services. Le tracing distribué vous permet de :

  * **Suivre le flux :** Voir le chemin complet qu'une requête emprunte dans votre système.
  * **Identifier les goulots d'étranglement :** Localiser quel service ou opération cause la latence.
  * **Comprendre les dépendances :** Visualiser les interactions entre les différents services.
  * **Simplifier le débogage :** Corréler les logs avec des requêtes spécifiques, ce qui facilite grandement le dépannage.

Une trace distribuée est composée de **spans**. Un **span** représente une opération unique ou une unité de travail au sein d'une trace (par exemple, une requête HTTP vers un service, une requête base de données, une exécution de méthode). Les spans ont un ID unique, un temps de début et de fin, et peuvent inclure des tags (paires clé-valeur) et des événements pour des métadonnées supplémentaires. Les spans sont organisés hiérarchiquement, avec des relations parent-enfant, formant une trace.

### 2\. Micrometer Tracing dans Spring Boot 3.x+

Spring Boot 3.x+ intègre profondément l'API Observation de Micrometer et Micrometer Tracing, ce qui rend la mise en œuvre du tracing distribué considérablement plus facile.

#### 2.1. Concepts de Base :

  * **API Observation :** L'API unifiée de Micrometer pour instrumenter votre code, capable de produire des métriques, des traces et des logs à partir d'un seul point d'instrumentation.
  * **Micrometer Tracing :** Une façade au-dessus des bibliothèques de tracing populaires comme OpenTelemetry et OpenZipkin Brave. Elle gère le cycle de vie des spans, la propagation du contexte et le reporting vers les backends de tracing.
  * **Ponts Tracer :** Micrometer Tracing fournit des "ponts" pour connecter son API à des implémentations de tracing spécifiques (par exemple, `micrometer-tracing-bridge-otel` pour OpenTelemetry, `micrometer-tracing-bridge-brave` pour OpenZipkin Brave).
  * **Reporters/Exporters :** Ces composants envoient les données de trace collectées vers un backend de tracing (par exemple, Zipkin, Jaeger, Grafana Tempo).

#### 2.2. Configuration de Micrometer Tracing dans un Projet Java Spring Boot :

Voici un guide étape par étape :

**Étape 1 : Ajouter les Dépendances**

Vous avez besoin de `spring-boot-starter-actuator` pour les fonctionnalités d'observabilité, d'un pont Micrometer Tracing et d'un reporter/exporter pour votre backend de tracing choisi.

**Exemple avec OpenTelemetry et Zipkin (choix courant) :**

Dans votre `pom.xml` (Maven) :

```xml
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-actuator</artifactId>
    </dependency>

    <dependency>
        <groupId>io.micrometer</groupId>
        <artifactId>micrometer-observation</artifactId>
    </dependency>

    <dependency>
        <groupId>io.micrometer</groupId>
        <artifactId>micrometer-tracing-bridge-otel</artifactId>
    </dependency>

    <dependency>
        <groupId>io.opentelemetry</groupId>
        <artifactId>opentelemetry-exporter-zipkin</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-webflux</artifactId>
    </dependency>
</dependencies>
```

**Étape 2 : Configurer les Propriétés de Tracing**

Dans `application.properties` ou `application.yml`, vous pouvez configurer le comportement du tracing.

```properties
# Activer le tracing (généralement vrai par défaut avec actuator et les dépendances de tracing)
management.tracing.enabled=true

# Configurer la probabilité d'échantillonnage (1.0 = 100% des requêtes sont tracées)
# La valeur par défaut est souvent 0.1 (10%), définir à 1.0 pour le développement/les tests
management.tracing.sampling.probability=1.0

# Configurer l'URL de base de Zipkin (si vous utilisez Zipkin)
spring.zipkin.base-url=http://localhost:9411
```

**Étape 3 : Exécuter un Backend de Tracing (par exemple, Zipkin)**

Vous avez besoin d'un serveur de tracing pour collecter et visualiser vos traces. Zipkin est un choix populaire pour le développement local.

Vous pouvez exécuter Zipkin via Docker :

```bash
docker run -d -p 9411:9411 openzipkin/zipkin
```

Une fois en cours d'exécution, vous pouvez accéder à l'interface utilisateur de Zipkin à l'adresse `http://localhost:9411`.

**Étape 4 : Instrumentation Automatique (La Magie de Spring Boot !)**

Pour de nombreux composants courants dans Spring Boot (comme les endpoints `RestController`, `RestTemplate`, `WebClient`, `JdbcTemplate`, les producteurs/consommateurs Kafka, etc.), Micrometer Tracing fournit une **instrumentation automatique**. Cela signifie que vous n'avez souvent pas besoin d'écrire de code de tracing explicite pour que le tracing de requêtes de base fonctionne.

Spring Boot garantit que :

  * Les requêtes HTTP entrantes créent automatiquement une nouvelle trace ou continuent une trace existante si des en-têtes de trace sont présents.
  * Les requêtes sortantes effectuées avec `RestTemplateBuilder`, `RestClient.Builder` ou `WebClient.Builder` auto-configurés propagent le contexte de trace vers les services en aval.
  * Les instructions de journalisation incluent automatiquement le `traceId` et le `spanId` (si vous configurez votre modèle de journalisation).

**Exemple de Modèle de Journalisation (dans `application.properties`) :**

```properties
logging.pattern.level=%5p [${spring.application.name:},%X{traceId:-},%X{spanId:-}] %c{1.}:%M:%L - %m%n
```

Ce modèle injectera le `traceId` et le `spanId` dans vos lignes de log, facilitant la corrélation des logs avec une trace spécifique.

**Étape 5 : Instrumentation Manuelle (pour la logique personnalisée)**

Bien que l'instrumentation automatique couvre beaucoup de choses, vous voudrez souvent tracer une logique métier spécifique ou des opérations critiques au sein de votre application. Vous pouvez le faire en utilisant :

  * **Annotation `@Observed` (Recommandée pour Spring Boot 3.x+) :**
    Cette annotation fait partie de l'API Observation de Micrometer et est la méthode préférée pour créer des observations (qui peuvent produire à la fois des métriques et des traces).

    ```java
    import io.micrometer.observation.annotation.Observed;
    import org.springframework.stereotype.Service;

    @Service
    public class MyService {

        @Observed(name = "myService.processData", contextualName = "processing-data")
        public String processData(String input) {
            // ... votre logique métier ...
            System.out.println("Processing data: " + input);
            return "Processed: " + input;
        }
    }
    ```

    L'attribut `name` définit le nom de l'observation (qui devient le nom de la métrique et le nom du span de trace). `contextualName` fournit un nom plus lisible pour le span dans les outils de tracing.

  * **API Programmative (pour plus de contrôle) :**
    Vous pouvez utiliser directement les beans `ObservationRegistry` et `Tracer` fournis par Spring Boot.

    ```java
    import io.micrometer.observation.Observation;
    import io.micrometer.observation.ObservationRegistry;
    import org.springframework.stereotype.Service;

    @Service
    public class AnotherService {

        private final ObservationRegistry observationRegistry;

        public AnotherService(ObservationRegistry observationRegistry) {
            this.observationRegistry = observationRegistry;
        }

        public String performComplexOperation(String id) {
            return Observation.createNotStarted("complex.operation", observationRegistry)
                    .lowCardinalityKeyValue("operation.id", id) // Ajouter un tag
                    .observe(() -> {
                        // ... logique complexe ici ...
                        try {
                            Thread.sleep(100); // Simuler un travail
                        } catch (InterruptedException e) {
                            Thread.currentThread().interrupt();
                        }
                        return "Completed complex operation for " + id;
                    });
        }
    }
    ```

    Ici, `observe()` encapsule le bloc de code, et `lowCardinalityKeyValue` ajoute un tag au span.

### 3\. Tracing Distribué dans les Microservices :

Lorsque vous avez plusieurs services Spring Boot, Micrometer Tracing facilite la propagation du contexte automatiquement pour `RestTemplate`, `WebClient` et autres clients instrumentés. Cela signifie que le `traceId` et le `spanId` sont transmis dans les en-têtes HTTP entre les services (par exemple, l'en-tête `traceparent` pour le W3C Trace Context).

Lorsqu'une requête arrive dans un service en aval, Micrometer Tracing détecte ces en-têtes et continue la trace existante, créant de nouveaux spans qui sont des enfants du span parent du service appelant. Cela forme la trace complète de bout en bout.

### 4\. Visualisation des Traces :

Une fois que votre application est instrumentée et envoie des traces vers un backend comme Zipkin (ou Jaeger, Lightstep, etc.), vous pouvez :

1.  **Accéder à l'UI :** Allez dans l'interface utilisateur web du backend de tracing (par exemple, `http://localhost:9411` pour Zipkin).
2.  **Trouver des Traces :** Utilisez des filtres (nom du service, nom du span, ID de trace) pour trouver des traces spécifiques.
3.  **Analyser les Détails de la Trace :** Cliquez sur une trace pour voir sa chronologie, les spans individuels, leurs durées, leurs tags et leurs événements.
4.  **Graphe de Dépendances :** La plupart des backends de tracing peuvent visualiser les dépendances entre les services basées sur les traces collectées.

### 5\. Bonnes Pratiques pour Micrometer Tracing :

  * **Nommez vos Spans de Manière Significative :** Utilisez des noms clairs, concis et à faible cardinalité pour vos spans (par exemple, "userService.getUser", "productService.updateStock"). Évitez d'inclure des données très dynamiques dans les noms des spans.
  * **Utilisez les Tags pour les Détails (Données à Haute Cardinalité) :** Au lieu de mettre des données dynamiques dans les noms des spans, utilisez des tags (paires clé-valeur) pour un contexte supplémentaire. Par exemple, `userId`, `orderId`, `customerType`. Soyez conscient des tags à **haute cardinalité**, car ils peuvent augmenter considérablement les coûts de stockage et les temps de requête dans votre backend de tracing. Utilisez-les avec discernement.
  * **Gardez les Spans Granulaires mais pas Excessifs :** Créez des spans pour des opérations significatives, mais évitez de créer trop de petits spans, car cela peut ajouter de la surcharge. Cherchez un équilibre qui fournit une visibilité suffisante sans submerger le système.
  * **Propagez le Contexte :** Assurez-vous que le contexte de trace est correctement propagé à travers les limites des services. L'auto-configuration de Spring Boot gère cela pour les scénarios courants, mais soyez conscient lors de l'utilisation de clients personnalisés ou d'opérations asynchrones.
  * **Échantillonnage :** Pour les environnements de production à fort trafic, envisagez d'utiliser des stratégies d'échantillonnage pour réduire le volume de données de trace envoyé à votre backend. Spring Boot permet de configurer `management.tracing.sampling.probability`.
  * **Corrélez les Logs :** Tirez parti du `traceId` et du `spanId` injectés dans les logs pour un débogage plus facile et une corrélation du comportement de l'application avec des requêtes spécifiques.
  * **Surveillez votre Backend de Tracing :** Assurez-vous que votre backend de tracing (par exemple, le serveur Zipkin) a des ressources suffisantes pour gérer le volume de traces entrant.
  * **Intégrez avec d'Autres Outils d'Observabilité :** Le tracing est une partie de l'observabilité. Combinez-le avec les métriques (également via Micrometer) et la journalisation structurée pour une vue holistique de la santé et des performances de votre application.

En suivant ces directives, vous pouvez exploiter efficacement Micrometer Tracing pour obtenir des informations approfondies sur vos applications Spring Boot, en particulier dans les environnements distribués.
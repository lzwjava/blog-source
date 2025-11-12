---
audio: false
generated: true
lang: fr
layout: post
title: Métriques d'Application en Java
translated: true
type: note
---

La bibliothèque `com.yammer.metrics`, initialement développée par Yammer, fait désormais partie de la bibliothèque **Dropwizard Metrics**. Elle offre un moyen robuste de collecter et de rapporter des métriques d'application en Java, vous aidant à surveiller des aspects de performance comme le nombre de requêtes, les temps de réponse, et plus encore. Voici un guide pour l'utiliser efficacement.

---

### Étape 1 : Ajouter la Dépendance
Étant donné que `com.yammer.metrics` a évolué pour devenir Dropwizard Metrics, vous devez utiliser la bibliothèque Dropwizard Metrics. Si vous utilisez Maven, ajoutez la dépendance suivante à votre fichier `pom.xml` :

```xml
<dependency>
    <groupId>io.dropwizard.metrics</groupId>
    <artifactId>metrics-core</artifactId>
    <version>4.2.0</version> <!-- Utilisez la dernière version disponible -->
</dependency>
```

En fonction de vos besoins, vous pourriez également avoir besoin de modules supplémentaires, tels que :
- `metrics-jvm` pour les métriques liées à la JVM.
- `metrics-httpclient` pour les métriques de client HTTP.
- `metrics-jersey` pour l'intégration avec le framework web Jersey.

Consultez la [documentation Dropwizard Metrics](https://metrics.dropwizard.io/) pour la dernière version et les modules disponibles.

---

### Étape 2 : Créer un Registre de Métriques
Le `MetricRegistry` est l'endroit central où toutes les métriques sont stockées. Vous en créez généralement une instance pour votre application :

```java
import com.codahale.metrics.MetricRegistry;

public class MyApplication {
    public static void main(String[] args) {
        MetricRegistry registry = new MetricRegistry();
    }
}
```

---

### Étape 3 : Utiliser Différents Types de Métriques
Dropwizard Metrics prend en charge plusieurs types de métriques, chacun adapté à différents besoins de surveillance :

#### **Compteurs (Counters)**
Les compteurs sont utilisés pour suivre des valeurs qui peuvent augmenter ou diminuer (par exemple, le nombre de requêtes traitées).

```java
import com.codahale.metrics.Counter;

Counter counter = registry.counter("requests.processed");
counter.inc();  // Incrémenter de 1
counter.inc(5); // Incrémenter de 5
counter.dec();  // Décrémenter de 1
```

#### **Jauges (Gauges)**
Les jauges fournissent un instantané d'une valeur à un moment spécifique (par exemple, la taille actuelle d'une file d'attente). Vous définissez une jauge en implémentant l'interface `Gauge` :

```java
import com.codahale.metrics.Gauge;

registry.register("queue.size", new Gauge<Integer>() {
    @Override
    public Integer getValue() {
        return someQueue.size(); // Remplacez par votre logique
    }
});
```

#### **Histogrammes (Histograms)**
Les histogrammes suivent la distribution statistique des valeurs (par exemple, la taille des requêtes) :

```java
import com.codahale.metrics.Histogram;

Histogram histogram = registry.histogram("request.sizes");
histogram.update(150); // Enregistrer une valeur
```

#### **Compteurs de débit (Meters)**
Les compteurs de débit mesurent le taux d'événements (par exemple, les requêtes par seconde) :

```java
import com.codahale.metrics.Meter;

Meter meter = registry.meter("requests.rate");
meter.mark(); // Enregistrer un événement
```

#### **Minuteries (Timers)**
Les minuteries mesurent à la fois le taux et la durée des événements (par exemple, le temps de traitement d'une requête) :

```java
import com.codahale.metrics.Timer;

Timer timer = registry.timer("request.duration");
Timer.Context context = timer.time();
try {
    // Simuler un travail
    Thread.sleep(100);
} finally {
    context.stop(); // Enregistrer la durée
}
```

---

### Étape 4 : Rapporter les Métriques
Pour rendre les métriques utiles, vous devez les rapporter quelque part. Dropwizard Metrics prend en charge divers reporters, tels que la console, JMX ou Graphite. Voici un exemple de reporter console qui enregistre les métriques toutes les 10 secondes :

```java
import com.codahale.metrics.ConsoleReporter;
import java.util.concurrent.TimeUnit;

ConsoleReporter reporter = ConsoleReporter.forRegistry(registry)
    .convertRatesTo(TimeUnit.SECONDS)
    .convertDurationsTo(TimeUnit.MILLISECONDS)
    .build();
reporter.start(10, TimeUnit.SECONDS); // Rapporter toutes les 10 secondes
```

Pour une utilisation en production, envisagez d'intégrer des systèmes comme Graphite ou d'exposer les métriques via JMX.

---

### Étape 5 : Intégrer avec des Frameworks (Optionnel)
Si vous utilisez un framework web comme Jersey, vous pouvez utiliser le module `metrics-jersey` pour instrumenter automatiquement vos endpoints. De plus, des annotations comme `@Timed` ou `@Counted` peuvent simplifier la collecte de métriques :

```java
import com.codahale.metrics.annotation.Timed;

@Path("/example")
public class ExampleResource {
    @GET
    @Timed
    public String getExample() {
        return "Hello, world!";
    }
}
```

Ajoutez la dépendance `metrics-jersey` et configurez-la avec votre application Jersey pour activer cette fonctionnalité.

---

### Bonnes Pratiques
- **Conventions de dénomination** : Utilisez un schéma de nommage hiérarchique pour plus de clarté (par exemple, `com.example.myapp.requests.total`).
- **Performance** : Soyez prudent avec le nombre et la fréquence des métriques, car une collecte excessive peut affecter les performances.
- **Documentation** : Reportez-vous à la [documentation Dropwizard Metrics](https://metrics.dropwizard.io/) pour des exemples à jour et des fonctionnalités avancées.

---

### Exemple : Mettre Tout Ensemble
Voici un exemple simple combinant plusieurs concepts :

```java
import com.codahale.metrics.*;
import java.util.concurrent.TimeUnit;

public class MetricsExample {
    public static void main(String[] args) throws InterruptedException {
        MetricRegistry registry = new MetricRegistry();

        // Créer un compteur
        Counter counter = registry.counter("example.counter");
        counter.inc();

        // Créer une minuterie
        Timer timer = registry.timer("example.timer");
        Timer.Context context = timer.time();
        Thread.sleep(100); // Simuler un travail
        context.stop();

        // Démarrer un reporter console
        ConsoleReporter reporter = ConsoleReporter.forRegistry(registry)
            .convertRatesTo(TimeUnit.SECONDS)
            .convertDurationsTo(TimeUnit.MILLISECONDS)
            .build();
        reporter.start(1, TimeUnit.SECONDS);

        // Maintenir le programme en cours d'exécution pour voir les rapports
        Thread.sleep(5000);
    }
}
```

Ce code suit un compteur et une minuterie, en rapportant les résultats sur la console chaque seconde.

---

### Notes Finales
La bibliothèque `com.yammer.metrics` a évolué pour devenir Dropwizard Metrics, utilisez donc toujours la dernière version du groupe `io.dropwizard.metrics`. Si vous démarrez un nouveau projet, vous pourriez également explorer des alternatives modernes comme Micrometer, mais Dropwizard Metrics reste un choix solide pour de nombreuses applications Java. Pour plus de détails, consultez la documentation officielle !
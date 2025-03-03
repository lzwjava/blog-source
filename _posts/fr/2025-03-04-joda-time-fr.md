---
audio: false
generated: true
lang: fr
layout: post
title: Opérations de date et d'heure en Java
translated: true
---

### Points Clés
- Il semble probable que pour utiliser `org.joda.time`, il faille l'ajouter à votre projet Java et importer ses classes pour les opérations de date et d'heure.
- La recherche suggère d'inclure la bibliothèque via Maven avec la version 2.13.1 ou de télécharger le fichier JAR, puis d'utiliser des classes comme `DateTime` et `LocalDate`.
- Les preuves penchent en faveur de Joda-Time étant utile pour gérer les fuseaux horaires, les systèmes de calendrier et les intervalles de temps, avec des exemples comme la création d'objets de date et leur modification.

### Qu'est-ce que Joda-Time et Comment l'Installer
Joda-Time est une bibliothèque pour manipuler les dates et les heures en Java, particulièrement utile avant Java 8, offrant une API intuitive pour remplacer les anciennes classes `Date` et `Calendar` moins sûres pour les threads. Pour l'utiliser, incluez d'abord la bibliothèque dans votre projet. Si vous utilisez Maven, ajoutez cette dépendance à votre `pom.xml` :
```xml
<dependency>
    <groupId>joda-time</groupId>
    <artifactId>joda-time</artifactId>
    <version>2.13.1</version>
</dependency>
```
Alternativement, téléchargez le fichier JAR depuis [ce site web](https://www.joda.org/joda-time/download.html) et ajoutez-le au classpath de votre projet, par exemple dans Eclipse en créant un dossier "libs" et en liant le JAR via les propriétés du projet.

### Exemples d'Utilisation de Base
Une fois installé, importez des classes comme `org.joda.time.DateTime` ou `org.joda.time.LocalDate`. Voici quelques exemples :
- Créer une date-heure actuelle : `DateTime now = new DateTime();`
- Accéder aux champs : `int year = now.getYear(); String monthName = now.monthOfYear().getAsText();`
- Modifier : `DateTime future = now.plusDays(5);`

### Fonctionnalités Avancées
Joda-Time prend en charge les fuseaux horaires (par exemple, `DateTimeZone.forID("America/New_York")`) et différents systèmes de calendrier (par exemple, Coptic via `CopticChronology.getInstance()`). Il gère également les intervalles et les durées, comme `Interval interval = new Interval(startDt, endDt);`.

Un détail inattendu est que Joda-Time est considéré comme un projet "terminé", avec le package `java.time` de Java 8 recommandé pour les nouveaux projets, mais il reste pertinent pour les systèmes hérités ou des besoins spécifiques.

---

### Note de l'Enquête : Guide Complet pour Utiliser `org.joda.time`

Cette section fournit une exploration détaillée de l'utilisation de la bibliothèque `org.joda.time`, en approfondissant la réponse directe avec un contexte et une profondeur technique supplémentaires, adaptée aux développeurs cherchant une compréhension approfondie. Elle inclut la configuration, des exemples d'utilisation, des fonctionnalités clés et des ressources supplémentaires, assurant une référence complète pour la mise en œuvre.

#### Introduction à Joda-Time
Joda-Time, développé par joda.org, est une bibliothèque largement utilisée pour le traitement des dates et des heures, particulièrement avant la sortie de Java 8. Il aborde les problèmes de conception des classes `Date` et `Calendar` de Java, comme les préoccupations de sécurité des threads, en utilisant des classes immuables. Avant Java 8, la classe `Date` et `SimpleDateFormatter` n'étaient pas sûres pour les threads, et les opérations comme les décalages jour/mois/année étaient contre-intuitives (par exemple, les jours commençant à 0, les mois à 1, nécessitant `Calendar`). Joda-Time offre une API propre et fluide et prend en charge huit systèmes de calendrier, contre les deux de Java (grégorien et impérial japonais). Après Java 8, les auteurs considèrent Joda-Time largement terminé, recommandant la migration vers `java.time` (JSR-310) pour les nouveaux projets, mais il reste pertinent pour les systèmes hérités ou des cas d'utilisation spécifiques.

#### Configuration de Joda-Time
Pour utiliser Joda-Time, vous devez d'abord l'inclure dans votre projet Java. La dernière version à partir du 3 mars 2025 est 2.13.1, assurant stabilité et compatibilité avec JDK 1.5 ou ultérieur. Pour les utilisateurs de Maven, ajoutez la dépendance suivante à votre `pom.xml` :
```xml
<dependency>
    <groupId>joda-time</groupId>
    <artifactId>joda-time</artifactId>
    <version>2.13.1</version>
</dependency>
```
Cela peut être trouvé sur [Maven Repository](https://mvnrepository.com/artifact/joda-time/joda-time). Pour les projets non-Maven, téléchargez le fichier `.tar.gz` depuis [ce site web](https://www.joda.org/joda-time/download.html), extrayez-le et ajoutez le `joda-time-2.13.1.jar` au classpath de votre projet. Par exemple, dans Eclipse, créez un dossier "libs", copiez le JAR et liez-le via Properties -> Java Build Path -> Libraries -> Add Jars. Testez la configuration avec `DateTime test = new DateTime();` pour assurer le bon fonctionnement.

#### Utilisation de Base et Exemples
Une fois inclus, importez des classes de `org.joda.time`, telles que `DateTime`, `LocalDate`, `LocalTime` et `LocalDateTime`, toutes immuables pour la sécurité des threads. Voici des exemples détaillés :

- **Création d'Objets Date-Heure :**
  - À partir de l'heure actuelle : `DateTime now = new DateTime();` utilise le fuseau horaire par défaut et le calendrier ISO.
  - À partir d'une `Date` Java : `java.util.Date juDate = new Date(); DateTime dt = new DateTime(juDate);` pour l'interopérabilité.
  - À partir de valeurs spécifiques : Les constructeurs acceptent `Long` (millisecondes), `String` (ISO8601), ou d'autres objets Joda-Time, par exemple, `DateTime dt = new DateTime(2025, 3, 3, 8, 39);`.

- **Accès aux Champs :**
  - Utilisez les méthodes getters : `int year = now.getYear(); int month = now.getMonthOfYear();` où janvier est 1 et décembre est 12.
  - Pour la représentation textuelle : `String dayName = now.dayOfWeek().getAsText();` affiche, par exemple, "Monday" pour le 3 mars 2025.
  - Vérifiez les propriétés : `boolean isLeap = now.year().isLeap();` retourne `false` pour 2025.

- **Modification de la Date-Heure :**
  - Créez de nouvelles instances avec des modifications : `DateTime newDt = now.withYear(2025);` ou `DateTime future = now.plusDays(5);`.
  - Ajoutez des durées : `DateTime later = now.plusHours(2);` pour ajouter deux heures, retournant une nouvelle instance.

Un exemple pratique de GeeksforGeeks illustre l'utilisation :
```java
import org.joda.time.DateTime;
import org.joda.time.LocalDateTime;
public class JodaTime {
    public static void main(String[] args) {
        DateTime now = new DateTime();
        System.out.println("Jour actuel : " + now.dayOfWeek().getAsText());
        System.out.println("Mois actuel : " + now.monthOfYear().getAsText());
        System.out.println("Année actuelle : " + now.year().getAsText());
        System.out.println("L'année actuelle est une année bissextile : " + now.year().isLeap());
        LocalDateTime dt = LocalDateTime.now();
        System.out.println(dt);
    }
}
```
Pour le 3 mars 2025, la sortie pourrait inclure "Jour actuel : Monday", "Mois actuel : March", "Année actuelle : 2025", "L'année actuelle est une année bissextile : false", et un horodatage comme "2025-03-03T08:39:00.000".

#### Fonctionnalités Clés et Utilisation Avancée
Joda-Time offre des fonctionnalités robustes pour des opérations de date-heure complexes, détaillées comme suit :

- **Fuseaux Horaires :**
  - Gérés via `DateTimeZone`, prenant en charge les zones nommées (par exemple, "Asia/Tokyo") et les décalages fixes. Exemple :
    ```java
    DateTimeZone zone = DateTimeZone.forID("America/New_York");
    DateTime nyTime = new DateTime(zone);
    ```
  - Le fuseau horaire par défaut correspond à celui de JDK, mais peut être remplacé avec `DateTimeZone.setDefault(zone);`. Les données de fuseau horaire sont mises à jour manuellement plusieurs fois par an, basées sur [global-tz](https://github.com/JodaOrg/global-tz).

- **Systèmes de Calendrier :**
  - Prend en charge sept systèmes : bouddhiste, copte, éthiopien, grégorien, grégorien-julien, islamique, julien, avec provision pour des systèmes personnalisés. Exemple :
    ```java
    Chronology coptic = CopticChronology.getInstance();
    LocalDate copticDate = new LocalDate(coptic);
    ```
  - Par défaut, utilise le calendrier ISO, historiquement inexact avant 1583, mais adapté à l'utilisation civile moderne.

- **Intervalles, Durées et Périodes :**
  - `Interval` : Représente une plage de temps, semi-ouverte (début inclusif, fin exclusive), par exemple, `Interval interval = new Interval(startDt, endDt);`.
  - `Duration` : Temps exact en millisecondes, par exemple, `Duration duration = new Duration(interval);`, utile pour ajouter à des instants.
  - `Period` : Définie en champs (années, mois, jours, etc.), inexacte en millisecondes, par exemple, `Period period = new Period(startDt, endDt);`. Exemple de différence : Ajouter 1 jour à l'heure d'été (par exemple, 2005-03-26 12:00:00) avec `plus(Period.days(1))` ajoute 23 heures, tandis que `plus(new Duration(24L*60L*60L*1000L))` ajoute 24 heures, mettant en évidence le comportement de la période par rapport à la durée.

Le guide de démarrage rapide fournit un tableau résumant les principales classes et les cas d'utilisation :
| **Aspect**                  | **Détails**                                                                                     |
|-----------------------------|-------------------------------------------------------------------------------------------------|
| **Classes Principales de Date-Heure** | Instant, DateTime, LocalDate, LocalTime, LocalDateTime (5 classes, toutes immuables)               |
| **Cas d'Utilisation d'Instant** | Horodatage d'un événement, sans système de calendrier ou fuseau horaire                                          |
| **Cas d'Utilisation de LocalDate** | Date de naissance, pas besoin de l'heure de la journée                                                           |
| **Cas d'Utilisation de LocalTime** | Heure de la journée, par exemple, ouverture/fermeture d'un magasin, sans date                                               |
| **Cas d'Utilisation de DateTime** | Usage général, remplace le calendrier JDK, inclut des informations de fuseau horaire                          |
| **Types de Constructeurs** | Le constructeur d'objet accepte : Date, Calendar, String (ISO8601), Long (millisecondes), classes Joda-Time |
| **Exemple de Conversion** | `java.util.Date` vers `DateTime` : `DateTime dt = new DateTime(new Date());`                      |
| **Méthodes d'Accès aux Champs** | `getMonthOfYear()` (1=Janvier, 12=Décembre), `getYear()`                                        |
| **Méthodes de Modification** | `withYear(2000)`, `plusHours(2)`                                                               |
| **Exemples de Méthodes de Propriété** | `monthOfYear().getAsText()`, `monthOfYear().getAsShortText(Locale.FRENCH)`, `year().isLeap()`, `dayOfMonth().roundFloorCopy()` |
| **Système de Calendrier par Défaut** | Système de calendrier ISO (calendrier civil de facto, historiquement inexact avant 1583)              |
| **Fuseau Horaire par Défaut** | Même que le défaut de JDK, peut être remplacé                                                         |
| **Classe Chronology** | Prend en charge plusieurs systèmes de calendrier, par exemple, `CopticChronology.getInstance()`                     |
| **Exemple de Fuseau Horaire** | `DateTimeZone zone = DateTimeZone.forID("Asia/Tokyo");`, `GJChronology.getInstance(zone)`      |
| **Classe Interval** | `Interval` - contient la date-heure de début et de fin, opérations basées sur la plage                          |
| **Classe Period** | `Period` - contient une période comme 6 mois, 3 jours, 7 heures, peut être dérivée d'un intervalle               |
| **Classe Duration** | `Duration` - durée exacte en millisecondes, peut être dérivée d'un intervalle                          |
| **Exemple Période vs Durée** | Ajouter 1 jour à l'heure d'été (2005-03-26 12:00:00) : `plus(Period.days(1))` ajoute 23 heures, `plus(new Duration(24L*60L*60L*1000L))` ajoute 24 heures |

Un détail intéressant est l'extensibilité des constructeurs d'objets, permettant la conversion à partir de `Date` ou `Calendar` de JDK en les passant directement, simplifiant la migration à partir du code hérité.

#### Apprentissage et Ressources Supplémentaires
Pour une exploration plus approfondie, consultez la documentation officielle à [Joda-Time User Guide](https://www.joda.org/joda-time/userguide.html), qui couvre des sujets avancés comme le formatage et l'analyse. Le guide de démarrage rapide à [Joda-Time Quick Start](https://www.joda.org/joda-time/quickstart.html) offre une introduction concise. Des tutoriels supplémentaires sont disponibles à [Baeldung Joda-Time](https://www.baeldung.com/joda-time) et [GeeksforGeeks Joda-Time](https://www.geeksforgeeks.org/joda-time/), avec des exemples de code et des instructions de configuration. La documentation de l'API à [Joda-Time API Docs](https://www.joda.org/joda-time/apidocs/index.html) est utile pour référence, bien que plus technique.

#### Conclusion
Joda-Time fournit une alternative robuste et sûre pour les threads pour les opérations de date et d'heure, avec un support étendu pour les fuseaux horaires, les systèmes de calendrier et les calculs de temps. Bien que considéré comme terminé après Java 8, il reste précieux pour les systèmes hérités, avec une configuration via Maven ou une inclusion manuelle de JAR, et une utilisation à travers des classes immuables comme `DateTime` et `LocalDate`. Ce guide assure que les développeurs disposent de toutes les informations nécessaires pour la mise en œuvre, des exemples de base aux fonctionnalités avancées, soutenues par des ressources complètes.
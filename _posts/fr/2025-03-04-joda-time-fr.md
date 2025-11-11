---
audio: false
generated: true
lang: fr
layout: post
title: Opérations de date et d'heure en Java
translated: true
type: note
---

### Points Clés
- Il semble probable que pour utiliser `org.joda.time`, vous deviez l'ajouter à votre projet Java et importer ses classes pour les opérations de date et d'heure.
- Les recherches suggèrent d'inclure la bibliothèque via Maven avec la version 2.13.1 ou de télécharger le fichier JAR, puis d'utiliser des classes comme `DateTime` et `LocalDate`.
- Les preuves tendent à indiquer que Joda-Time est utile pour gérer les fuseaux horaires, les systèmes calendaires et les intervalles de temps, avec des exemples comme la création d'objets de date et leur modification.

### Qu'est-ce que Joda-Time et comment le configurer
Joda-Time est une bibliothèque pour gérer les dates et les heures en Java, particulièrement utile avant Java 8, offrant une API intuitive pour remplacer les anciennes classes `Date` et `Calendar` moins thread-safe. Pour l'utiliser, incluez d'abord la bibliothèque dans votre projet. Si vous utilisez Maven, ajoutez cette dépendance à votre `pom.xml` :
```xml
<dependency>
    <groupId>joda-time</groupId>
    <artifactId>joda-time</artifactId>
    <version>2.13.1</version>
</dependency>
```
Alternativement, téléchargez le fichier JAR depuis [ce site web](https://www.joda.org/joda-time/download.html) et ajoutez-le au classpath de votre projet, par exemple dans Eclipse en créant un dossier "libs" et en liant le JAR via les propriétés du projet.

### Exemples d'utilisation de base
Une fois configuré, importez des classes comme `org.joda.time.DateTime` ou `org.joda.time.LocalDate`. Voici quelques exemples :
- Créer une date-heure actuelle : `DateTime now = new DateTime();`
- Accéder aux champs : `int year = now.getYear(); String monthName = now.monthOfYear().getAsText();`
- Modifier : `DateTime future = now.plusDays(5);`

### Fonctionnalités avancées
Joda-Time prend en charge les fuseaux horaires (par exemple, `DateTimeZone.forID("America/New_York")`) et différents systèmes calendaires (par exemple, Copte via `CopticChronology.getInstance()`). Il gère également les intervalles et les durées, comme `Interval interval = new Interval(startDt, endDt);`.

Un détail inattendu est que Joda-Time est considéré comme un projet "terminé", le package `java.time` de Java 8 étant recommandé pour les nouveaux projets, mais il reste pertinent pour les systèmes hérités ou des besoins spécifiques.

---

### Note d'enquête : Guide complet pour utiliser `org.joda.time`

Cette section fournit une exploration détaillée de l'utilisation de la bibliothèque `org.joda.time`, élargissant la réponse directe avec un contexte supplémentaire et une profondeur technique, adaptée aux développeurs cherchant une compréhension approfondie. Elle inclut la configuration, des exemples d'utilisation, les fonctionnalités clés et des ressources supplémentaires, assurant une référence complète pour la mise en œuvre.

#### Introduction à Joda-Time
Joda-Time, développé par joda.org, est une bibliothèque de traitement des dates et heures largement utilisée, particulièrement avant la sortie de Java 8. Elle résout les problèmes de conception des classes Java `Date` et `Calendar`, tels que les problèmes de thread-safety, en utilisant des classes immuables. Avant Java 8, la classe `Date` et `SimpleDateFormatter` n'étaient pas thread-safe, et des opérations comme les décalages jour/mois/année étaient contre-intuitives (par exemple, les jours commençant à 0, les mois à 1, nécessitant `Calendar`). Joda-Time offre une API propre et fluide et prend en charge huit systèmes calendaires, contre deux pour Java (Grégorien et Impérial Japonais). Après Java 8, les auteurs considèrent Joda-Time comme largement terminé, recommandant la migration vers `java.time` (JSR-310) pour les nouveaux projets, mais il reste pertinent pour les systèmes hérités ou des cas d'utilisation spécifiques.

#### Configuration de Joda-Time
Pour utiliser Joda-Time, vous devez d'abord l'inclure dans votre projet Java. La dernière version au 3 mars 2025 est la 2.13.1, assurant stabilité et compatibilité avec JDK 1.5 ou ultérieur. Pour les utilisateurs de Maven, ajoutez la dépendance suivante à votre `pom.xml` :
```xml
<dependency>
    <groupId>joda-time</groupId>
    <artifactId>joda-time</artifactId>
    <version>2.13.1</version>
</dependency>
```
Celle-ci peut être trouvée sur [Maven Repository](https://mvnrepository.com/artifact/joda-time/joda-time). Pour les projets non-Maven, téléchargez le fichier `.tar.gz` depuis [ce site web](https://www.joda.org/joda-time/download.html), extrayez-le et ajoutez le `joda-time-2.13.1.jar` au classpath de votre projet. Par exemple, dans Eclipse, créez un dossier "libs", copiez le JAR et liez-le via Propriétés -> Java Build Path -> Libraries -> Add Jars. Testez la configuration avec `DateTime test = new DateTime();` pour assurer la fonctionnalité.

#### Utilisation de base et exemples
Une fois inclus, importez les classes de `org.joda.time`, telles que `DateTime`, `LocalDate`, `LocalTime` et `LocalDateTime`, toutes immuables pour la thread-safety. Voici des exemples détaillés :

- **Création d'objets Date-Heure :**
  - À partir de l'heure actuelle : `DateTime now = new DateTime();` utilise le fuseau horaire par défaut et le calendrier ISO.
  - À partir d'un `Date` Java : `java.util.Date juDate = new Date(); DateTime dt = new DateTime(juDate);` pour l'interopérabilité.
  - À partir de valeurs spécifiques : Les constructeurs acceptent `Long` (millisecondes), `String` (ISO8601), ou d'autres objets Joda-Time, par exemple, `DateTime dt = new DateTime(2025, 3, 3, 8, 39);`.

- **Accès aux champs :**
  - Utilisez les méthodes getter : `int year = now.getYear(); int month = now.getMonthOfYear();` où Janvier est 1 et Décembre est 12.
  - Pour la représentation textuelle : `String dayName = now.dayOfWeek().getAsText();` affiche, par exemple, "Lundi" pour le 3 mars 2025.
  - Vérifiez les propriétés : `boolean isLeap = now.year().isLeap();` retourne `false` pour 2025.

- **Modification de la date-heure :**
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
        System.out.println("L'année actuelle est bissextile : " + now.year().isLeap());
        LocalDateTime dt = LocalDateTime.now();
        System.out.println(dt);
    }
}
```
Pour le 3 mars 2025, la sortie pourrait inclure "Jour actuel : Lundi", "Mois actuel : Mars", "Année actuelle : 2025", "L'année actuelle est bissextile : false", et un horodatage comme "2025-03-03T08:39:00.000".

#### Fonctionnalités clés et utilisation avancée
Joda-Time offre des fonctionnalités robustes pour les opérations de date-heure complexes, détaillées comme suit :

- **Fuseaux horaires :**
  - Gérés via `DateTimeZone`, prenant en charge les zones nommées (par exemple, "Asia/Tokyo") et les décalages fixes. Exemple :
    ```java
    DateTimeZone zone = DateTimeZone.forID("America/New_York");
    DateTime nyTime = new DateTime(zone);
    ```
  - La zone par défaut correspond à celle du JDK, mais peut être remplacée avec `DateTimeZone.setDefault(zone);`. Les données de fuseaux horaires sont mises à jour manuellement plusieurs fois par an, basées sur [global-tz](https://github.com/JodaOrg/global-tz).

- **Systèmes calendaires :**
  - Prend en charge sept systèmes : Bouddhiste, Copte, Éthiopien, Grégorien, GrégorienJulien, Islamique, Julien, avec possibilité de systèmes personnalisés. Exemple :
    ```java
    Chronology coptic = CopticChronology.getInstance();
    LocalDate copticDate = new LocalDate(coptic);
    ```
  - Par défaut, utilise le calendrier ISO, historiquement inexact avant 1583, mais adapté à un usage civil moderne.

- **Intervalles, Durées et Périodes :**
  - `Interval` : Représente une plage de temps, semi-ouverte (début inclus, fin exclusive), par exemple, `Interval interval = new Interval(startDt, endDt);`.
  - `Duration` : Temps exact en millisecondes, par exemple, `Duration duration = new Duration(interval);`, utile pour l'ajout à des instants.
  - `Period` : Défini en champs (années, mois, jours, etc.), inexact en millisecondes, par exemple, `Period period = new Period(startDt, endDt);`. Exemple de différence : Ajouter 1 jour lors du passage à l'heure d'été (par exemple, 2005-03-26 12:00:00) avec `plus(Period.days(1))` ajoute 23 heures, tandis que `plus(new Duration(24L*60L*60L*1000L))` ajoute 24 heures, mettant en évidence le comportement période vs. durée.

Le guide de démarrage rapide fournit un tableau résumant les classes principales et les cas d'utilisation :
| **Aspect**                  | **Détails**                                                                                     |
|-----------------------------|-------------------------------------------------------------------------------------------------|
| **Classes Date-Heure Principales**   | Instant, DateTime, LocalDate, LocalTime, LocalDateTime (5 classes, toutes immuables)               |
| **Cas d'utilisation d'Instant**         | Horodatage d'un événement, pas de système calendaire ou de fuseau horaire                                          |
| **Cas d'utilisation de LocalDate**       | Date de naissance, pas besoin de l'heure du jour                                                           |
| **Cas d'utilisation de LocalTime**       | Heure du jour, par exemple, ouverture/fermeture d'un magasin, pas de date                                               |
| **Cas d'utilisation de DateTime**        | Usage général, remplace le Calendar du JDK, inclut les informations de fuseau horaire                          |
| **Types de Constructeurs**        | Le constructeur d'objet accepte : Date, Calendar, String (ISO8601), Long (millisecondes), classes Joda-Time |
| **Exemple de Conversion**       | `java.util.Date` vers `DateTime` : `DateTime dt = new DateTime(new Date());`                      |
| **Méthodes d'Accès aux Champs**     | `getMonthOfYear()` (1=Janvier, 12=Décembre), `getYear()`                                        |
| **Méthodes de Modification**     | `withYear(2000)`, `plusHours(2)`                                                               |
| **Exemples de Méthodes de Propriété**| `monthOfYear().getAsText()`, `monthOfYear().getAsShortText(Locale.FRENCH)`, `year().isLeap()`, `dayOfMonth().roundFloorCopy()` |
| **Système Calendaire par Défaut**  | Système de calendrier ISO (calendrier civil de facto, historiquement inexact avant 1583)              |
| **Fuseau Horaire par Défaut**        | Identique au défaut du JDK, peut être remplacé                                                         |
| **Classe de Chronologie**         | Prend en charge plusieurs systèmes calendaires, par exemple, `CopticChronology.getInstance()`                     |
| **Exemple de Fuseau Horaire**        | `DateTimeZone zone = DateTimeZone.forID("Asia/Tokyo");`, `GJChronology.getInstance(zone)`      |
| **Classe Intervalle**           | `Interval` - contient les dates-heures de début et de fin, opérations basées sur la plage                          |
| **Classe Période**             | `Period` - contient une période comme 6 mois, 3 jours, 7 heures, peut être dérivée d'un intervalle               |
| **Classe Durée**           | `Duration` - durée exacte en millisecondes, peut être dérivée d'un intervalle                          |
| **Exemple Période vs Durée**| Ajouter 1 jour lors du passage à l'heure d'été (2005-03-26 12:00:00) : `plus(Period.days(1))` ajoute 23 heures, `plus(new Duration(24L*60L*60L*1000L))` ajoute 24 heures |

Un détail intéressant est l'extensibilité des constructeurs d'objets, permettant la conversion depuis le JDK `Date` ou `Calendar` en les passant directement, simplifiant la migration du code hérité.

#### Apprentissage supplémentaire et ressources
Pour une exploration plus approfondie, consultez la documentation officielle sur [Joda-Time User Guide](https://www.joda.org/joda-time/userguide.html), qui couvre des sujets avancés comme le formatage et l'analyse. Le guide de démarrage rapide sur [Joda-Time Quick Start](https://www.joda.org/joda-time/quickstart.html) offre une introduction concise. Des tutoriels supplémentaires sont disponibles sur [Baeldung Joda-Time](https://www.baeldung.com/joda-time) et [GeeksforGeeks Joda-Time](https://www.geeksforgeeks.org/joda-time/), avec des exemples de code et des instructions de configuration. La documentation de l'API sur [Joda-Time API Docs](https://www.joda.org/joda-time/apidocs/index.html) est utile pour la référence, bien que plus technique.

#### Conclusion
Joda-Time fournit une alternative robuste et thread-safe pour les opérations de date et d'heure, avec un support étendu des fuseaux horaires, des systèmes calendaires et des calculs de temps. Bien que considéré comme terminé après Java 8, il reste précieux pour les systèmes hérités, avec une configuration via Maven ou l'inclusion manuelle de JAR, et une utilisation via des classes immuables comme `DateTime` et `LocalDate`. Ce guide assure que les développeurs disposent de toutes les informations nécessaires pour la mise en œuvre, des exemples de base aux fonctionnalités avancées, soutenues par des ressources complètes.

### Citations Clés
- [Page d'accueil de Joda-Time avec informations générales](https://www.joda.org/joda-time/)
- [Guide de démarrage rapide de Joda-Time pour les débutants](https://www.joda.org/joda-time/quickstart.html)
- [Tutoriel Baeldung sur l'utilisation de Joda-Time](https://www.baeldung.com/joda-time)
- [Article GeeksforGeeks sur Joda-Time avec exemples](https://www.geeksforgeeks.org/joda-time/)
- [Guide de l'utilisateur de Joda-Time pour une référence détaillée](https://www.joda.org/joda-time/userguide.html)
- [Page de téléchargement et d'installation de Joda-Time](https://www.joda.org/joda-time/download.html)
- [Dépôt Maven pour la dépendance Joda-Time](https://mvnrepository.com/artifact/joda-time/joda-time)
- [Documentation de l'API Joda-Time pour référence technique](https://www.joda.org/joda-time/apidocs/index.html)
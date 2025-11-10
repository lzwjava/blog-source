---
audio: false
generated: true
lang: fr
layout: post
title: Configuration de Logback pour un format de journal personnalisé
translated: true
type: note
---

Pour obtenir le format de journal que vous avez fourni, vous devez configurer votre fichier `logback.xml`. La clé est d'utiliser un `PatternLayout` dans votre appender et de définir correctement la propriété `pattern`.

Voici une décomposition des composants de votre format de journal souhaité et comment les mapper aux convertisseurs de motif Logback :

*   **`2025-06-15T01:37:52.452+08:00`** : Il s'agit de l'horodatage. Vous utiliserez `%d{yyyy-MM-dd'T'HH:mm:ss.SSSXXX}` pour cela.
    *   `yyyy-MM-dd'T'HH:mm:ss.SSS` : Date et heure avec millisecondes.
    *   `XXX` : Décalage ISO 8601 par rapport à UTC (par exemple, `+08:00`).
*   **`DEBUG`** : Il s'agit du niveau de journalisation. Vous utiliserez `%-5p` (aligné à gauche, 5 caractères de large).
*   **`302244`** : Il s'agit de l'ID de processus. Logback n'expose pas directement l'ID de processus dans ses convertisseurs standard. Cependant, il expose l'**ID de thread** (`%t` ou `%thread`). Si "302244" dans votre exemple est en réalité un ID de thread (ce qui est très courant dans les journaux d'application), alors `%thread` est ce dont vous avez besoin. Si ce *doit* être l'ID de processus du système d'exploitation, vous pourriez avoir besoin d'un convertisseur Logback personnalisé ou d'une propriété système si votre environnement le permet. Pour les applications Spring Boot typiques, il s'agit généralement de l'ID de thread. Je supposerai que c'est l'ID de thread pour cet exemple.
*   **`---`** : Une chaîne de caractères littérale.
*   **`[nio-8090-exec-1]`** : Il s'agit du nom du thread. Vous utiliserez `[%thread]` ou `%-40.40thread` si vous le souhaitez de largeur fixe.
*   **`o.s.w.s.m.m.a.HttpEntityMethodProcessor`** : Il s'agit du nom du logger (généralement le nom complet de la classe). Vous utiliserez `%-40.40logger{39}` pour obtenir un nom de logger tronqué, aligné à droite, jusqu'à 39 caractères.
*   **`:`** : Un deux-points littéral.
*   **`Writing ["{"vnstatversion":"2.9","jsonversion":"2","interfaces":[{"name":"enp4s0","alias":"","created":{"date" (tronqué)..."]`** : Il s'agit du message de journal. Vous utiliserez `%msg%n`.

Voici un exemple de configuration `logback.xml` qui devrait produire une sortie très similaire :

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>

    <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%d{yyyy-MM-dd'T'HH:mm:ss.SSSXXX} %highlight(%-5p) %thread --- [%thread] %-40.40logger{39} : %msg%n</pattern>
        </encoder>
    </appender>

    <root level="INFO">
        <appender-ref ref="CONSOLE"/>
    </root>

    <logger name="org.springframework.web.servlet.mvc.method.annotation.HttpEntityMethodProcessor" level="DEBUG"/>
    <logger name="org.springframework.web.servlet.DispatcherServlet" level="DEBUG"/>

</configuration>
```

**Explication du `pattern` :**

*   `%d{yyyy-MM-dd'T'HH:mm:ss.SSSXXX}` : Date et heure au format ISO 8601 avec millisecondes et décalage de fuseau horaire.
*   `%highlight(%-5p)` : Cela affichera le niveau de journalisation (par exemple, DEBUG, INFO) aligné à gauche sur 5 caractères, et si vous sortez vers une console, Logback tentera de le coloriser.
*   `%thread` : Le nom du thread qui a journalisé l'événement. (Si vous avez besoin de l'ID de processus, c'est plus complexe, mais pour les applications Spring, l'ID de thread est généralement ce qui est pertinent ici).
*   `---` : Un séparateur de chaîne de caractères littérale.
*   `[%thread]` : Le nom du thread entre crochets.
*   `%-40.40logger{39}` : Le nom du logger (généralement le nom de la classe).
    *   `%-40` : Aligné à gauche et complété à 40 caractères.
    *   `.40logger` : Tronque le nom du logger s'il dépasse 40 caractères.
    *   `{39}` : Cela indique à Logback d'afficher au maximum 39 caractères du nom du logger, en commençant par la fin du nom du package (par exemple, `o.s.w.s.m.m.a.HttpEntityMethodProcessor` pourrait devenir `o.s.w.s.m.m.a.HttpEntityMethodProcessor` s'il tient, ou `...HttpEntityMethodProcessor` s'il est tronqué depuis le début). Vous pouvez ajuster ce nombre.
*   ` :  ` : Un deux-points et un espace littéraux.
*   `%msg%n` : Le message de journal actuel suivi d'une nouvelle ligne.

**Notes importantes :**

1.  **Emplacement :** Enregistrez ce XML en tant que `logback.xml` dans votre répertoire `src/main/resources` de votre projet Spring Boot.
2.  **ID de processus vs ID de thread :** Comme mentionné, les convertisseurs de motif standard de Logback n'exposent pas directement l'ID de processus du système d'exploitation. Si `302244` *doit* être l'ID de processus, vous devriez généralement implémenter un `PatternLayoutConverter` personnalisé ou définir une propriété système au démarrage que vous référencez ensuite dans votre motif Logback. Cependant, pour la plupart des journaux d'application, l'ID de thread (`%thread`) est suffisant et couramment utilisé à cette position.
3.  **Par défaut de Spring Boot :** Spring Boot fournit souvent sa propre configuration Logback par défaut si vous n'en fournissez pas une. En plaçant `logback.xml` dans `src/main/resources`, vous remplacez la configuration par défaut.
4.  **Niveaux des Loggers :** Assurez-vous que les loggers spécifiques (comme `HttpEntityMethodProcessor` et `DispatcherServlet`) sont définis au niveau `DEBUG` si vous voulez voir leurs messages DEBUG. Si le niveau racine est `INFO`, alors par défaut, les messages DEBUG ne seront pas affichés à moins que vous ne définissiez explicitement le niveau pour des loggers spécifiques.

Cette configuration devrait vous rapprocher considérablement de votre format de journal souhaité.
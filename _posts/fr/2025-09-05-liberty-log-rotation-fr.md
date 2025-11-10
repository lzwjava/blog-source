---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Guide de Configuration de la Rotation des Journaux Liberty
translated: true
type: note
---

Voici la version courte, suivie d'exemples que vous pouvez coller dans `server.xml`.

### Fonctionnement de la rotation des logs Liberty

* **Ce qui tourne :** `messages.log` et `trace.log`.
  La rotation peut être **basée sur la taille** et/ou **basée sur le temps**. ([openliberty.io][1])
* **Ce qui ne tourne pas :** `console.log` (c'est juste stdout/stderr). Vous pouvez plutôt la réduire/désactiver. ([openliberty.io][2], [IBM][3])
* **Où configurer :** l'élément `<logging …/>` dans `server.xml`. (Vous pouvez aussi définir les mêmes valeurs dans `bootstrap.properties`/variables d'environnement si vous avez besoin qu'elles s'appliquent *avant* le chargement de `server.xml`.) ([openliberty.io][2])
* **Logs d'accès :** le journal d'accès HTTP a ses **propres** paramètres de rotation basée sur le temps sous `httpAccessLogging` / `accessLogging`. ([openliberty.io][4])
* **Taille + temps :** Liberty moderne prend en charge la rotation basée sur le temps en plus de l'option classique basée sur la taille, vous pouvez donc utiliser l'une ou l'autre ou les deux (sauf pour `console.log`). ([IBM][5])

---

### Recettes courantes pour `server.xml`

#### 1) Rotation basée sur la taille (classique)

Conserve jusqu'à 10 fichiers, chacun jusqu'à 256 Mo.

```xml
<logging
  logDirectory="${server.output.dir}/logs"
  maxFileSize="256"
  maxFiles="10"/>
```

Effet : quand `messages.log` ou `trace.log` dépasse 256 Mo, Liberty l'archive dans un fichier horodaté et conserve au maximum 10 de ces fichiers. (N'affecte pas `console.log`.) ([openliberty.io][1])

#### 2) Rotation basée sur le temps (par exemple, quotidienne à minuit)

```xml
<logging
  rolloverStartTime="00:00"
  rolloverInterval="1d"/>
```

Effet : `messages.log` et `trace.log` sont archivés chaque jour à 00:00. Vous pouvez aussi utiliser des minutes (`m`) ou des heures (`h`), par exemple `30m` ou `6h`. ([openliberty.io][2])

#### 3) Combiner taille + temps (typique en production)

```xml
<logging
  logDirectory="${server.output.dir}/logs"
  maxFileSize="256"
  maxFiles="14"
  rolloverStartTime="00:00"
  rolloverInterval="1d"/>
```

Effet : archivez **selon la condition qui arrive en premier** (taille ou planification), et conservez un historique de 14 fichiers. ([IBM][5])

#### 4) Maîtriser ou désactiver la croissance de `console.log`

`console.log` ne peut pas tourner ; réduisez-le ou désactivez-le et comptez sur `messages.log`.

```xml
<logging
  consoleLogLevel="OFF"
  copySystemStreams="false"/>
```

Notes : désactiver la console arrête la copie des logs Liberty vers `console.log`, mais la JVM peut encore écrire des éléments comme `-verbose:gc` vers stdout/stderr. ([openliberty.io][2])

#### 5) Ajustements de nom/format (optionnel)

```xml
<logging
  messageFileName="messages.log"
  traceFileName="trace.log"
  messageFormat="JSON"/>
```

JSON est pratique pour l'envoi vers une stack de logs ; laissez les valeurs par défaut si vous n'en avez pas besoin. ([openliberty.io][1])

---

### Journal d'accès HTTP (séparé de ce qui précède)

Activez la journalisation d'accès et archivez-la quotidiennement à minuit :

```xml
<httpAccessLogging id="accessLogging"
  rolloverStartTime="00:00"
  rolloverInterval="1d"/>

<httpEndpoint id="defaultHttpEndpoint"
  httpPort="9080" httpsPort="9443"
  accessLoggingRef="accessLogging"/>
```

(Ou placez `rolloverStartTime`/`rolloverInterval` directement sur un enfant `<accessLogging …/>` de `httpEndpoint`.) ([openliberty.io][4])

---

### Liste de contrôle rapide

* Utilisez **`maxFileSize` + `maxFiles`** pour la rotation basée sur la taille. ([openliberty.io][1])
* Utilisez **`rolloverStartTime` + `rolloverInterval`** pour la rotation basée sur le temps. ([openliberty.io][2])
* **N'attendez pas que `console.log` tourne** ; définissez `consoleLogLevel="OFF"` et `copySystemStreams="false"` si vous voulez éviter les gros fichiers console. ([openliberty.io][2], [IBM][3])

Si vous partagez votre extrait actuel de `server.xml` ou vos objectifs de rétention (par exemple, "conserver ~7 jours" ou "limiter à 2 Go"), j'adapterai les valeurs exactes.

[1]: https://openliberty.io/docs/latest/reference/config/logging.html "Logging (logging) :: Open Liberty Docs"
[2]: https://openliberty.io/docs/latest/log-trace-configuration.html "Log and trace configuration :: Open Liberty Docs"
[3]: https://www.ibm.com/support/pages/how-turn-console-logging-prevent-excess-file-growth-and-use-only-message-log-rotation-liberty-profile-or-open-liberty?utm_source=chatgpt.com "How to turn off Console logging, prevent excess file growth ..."
[4]: https://openliberty.io/docs/latest/access-logging.html "HTTP access logging :: Open Liberty Docs"
[5]: https://www.ibm.com/support/pages/how-setup-liberty-log-rollover-both-time-based-and-size-based-options-similar-traditional-websphere-0?utm_source=chatgpt.com "How to setup Liberty Log Rollover with both Time-Based ..."
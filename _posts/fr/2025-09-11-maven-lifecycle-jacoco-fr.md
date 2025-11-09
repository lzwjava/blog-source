---
audio: false
date: 2025-09-11
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Comprendre les cycles de vie Maven et JaCoCo
translated: true
type: note
---

Bonne question — cela revient aux *phases du cycle de vie* de Maven et à la façon dont les plugins s'y lient.

### Les bases du cycle de vie

Maven a trois cycles de vie standard : `clean`, `default` (parfois appelé *build*), et `site`.
À l'intérieur du cycle de vie *default*, les phases importantes se déroulent dans cet ordre :

* `validate`
* `compile`
* `test`
* `package`
* `verify`
* `install`
* `deploy`

Chaque phase inclut toutes les précédentes (si vous exécutez `mvn verify`, Maven exécute tout de `validate` jusqu'à `verify`). Exécuter `mvn package` s'arrêtera après avoir créé l'artefact (JAR/WAR), et n'exécutera pas `verify`.

### Pourquoi JaCoCo intervient

Le plugin Maven JaCoCo lie généralement son objectif **`prepare-agent`** à la phase `initialize` ou `verify` selon la configuration.

* S'il est lié à `verify` (la configuration courante pour les rapports de couverture), alors `mvn verify` le déclenchera.
* `mvn package` ne va pas aussi loin dans le cycle de vie, donc la phase `verify` (et par conséquent l'étape de JaCoCo) est ignorée.

C'est pourquoi vous voyez JaCoCo s'exécuter lorsque vous lancez `mvn verify` mais pas lorsque vous lancez `mvn package`.

### Conséquence pratique

* Utilisez **`mvn package`** lorsque vous voulez juste l'artefact de build (rapide, pas de vérifications supplémentaires).
* Utilisez **`mvn verify`** lorsque vous voulez exécuter *les tests d'intégration, les vérifications, les rapports de couverture, ou les plugins de qualité* qui sont liés aux phases ultérieures.

👉 Si vous voulez que JaCoCo s'exécute toujours, même avec `mvn package`, vous pouvez relier l'objectif `prepare-agent` à une phase antérieure comme `test` ou `package` dans votre `pom.xml`.

Souhaitez-vous que je vous montre un extrait concret de `pom.xml` qui fait s'exécuter le `prepare-agent` de JaCoCo dès la phase `test` au lieu de `verify` ?
---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Typage par Défaut Jackson Expliqué et Désactivé
translated: true
type: note
---

Dans Jackson (la bibliothèque `com.fasterxml.jackson.databind`), le **default typing** (typage par défaut) est une fonctionnalité de `ObjectMapper` qui inclut automatiquement des métadonnées de type (comme `@class` ou `@type`) dans le JSON sérialisé afin que les objets puissent être désérialisés dans leurs types polymorphes d'origine.

Par exemple, si vous sérialisez une `List<Animal>` contenant à la fois `Dog` et `Cat`, le typage par défaut ajoute des champs JSON supplémentaires pour que Jackson sache quelle sous-classe réinstancier plus tard.

---

### Fonctionnement de la Désactivation

Lorsque vous **désactivez le typage par défaut**, Jackson cesse d'injecter ces champs de métadonnées de type supplémentaires. Cela signifie :

* La sortie JSON sera « plus propre », sans les indicateurs `@class`/`@type`.
* Lors de la désérialisation, Jackson ne peut reconstruire les objets qu'en utilisant les types statiques déclarés (le type cible que vous fournissez), et non les types d'exécution d'origine.
* Toute utilisation de cas polymorphes sera rompue à moins que vous ne configuriez explicitement `@JsonTypeInfo`, `@JsonSubTypes` ou des modules personnalisés.

---

### Méthodes Pertinentes

* **Activation** (style pré-2.10) :

  ```java
  objectMapper.enableDefaultTyping();
  ```

  (obsolète, car trop permissif et introduisait des risques de sécurité.)

* **Désactivation** :

  ```java
  objectMapper.disableDefaultTyping();
  ```

  ou dans les versions plus récentes (2.10+), vous appelez :

  ```java
  objectMapper.activateDefaultTyping(PolymorphicTypeValidator, ObjectMapper.DefaultTyping.NON_FINAL);
  ```

  Pour *désactiver*, vous **n'appelez simplement pas** cette méthode (il n'y a pas de typage par défaut à moins que vous ne l'activiez), ou vous pouvez appeler :

  ```java
  objectMapper.deactivateDefaultTyping();
  ```

---

### Sécurité et Justification

* **Le typage par défaut est désactivé par défaut** dans les versions modernes de Jackson car il peut être exploité (les attaquants pourraient créer un JSON qui instancie des classes dangereuses).
* Si vous le désactivez, Jackson fonctionne dans un mode « plus sûr », où la désérialisation ne fonctionne que pour les types que vous liez explicitement, et non pour des types d'exécution arbitraires.
* Si vous avez besoin d'une prise en charge polymorphe, vous devez annoter vos classes avec `@JsonTypeInfo` au lieu de vous fier au typage par défaut global.

---

✅ **En bref :**
Désactiver le typage par défaut indique à Jackson de **ne pas** inclure les métadonnées de type dans le JSON, ce qui signifie qu'il ne reconstruira pas automatiquement les sous-types polymorphes lors de la désérialisation. Cela réduit la flexibilité mais est plus sûr et garde le JSON propre.

Voulez-vous que je vous montre un **exemple JSON avant/après** avec le typage par défaut activé vs désactivé ?
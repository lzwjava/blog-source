---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Présentation de la désérialisation polymorphe Jackson
translated: true
type: note
---

### Aperçu de la désérialisation polymorphe de Jackson

Jackson est une bibliothèque Java pour la sérialisation et la désérialisation JSON. La désérialisation polymorphe permet à Jackson d'instancier automatiquement la sous-classe correcte d'une classe de base lors de la désérialisation, en se basant sur les informations de type intégrées au JSON. Ceci est utile lors de la gestion d'hiérarchies d'héritage, garantissant que le bon type d'objet est créé à partir des données JSON.

Composants clés :
- **@JsonTypeInfo** : Annotations qui contrôlent où et comment les informations de type sont stockées dans le JSON.
- **@JsonSubTypes** : Annotations qui listent les sous-classes (sous-types) et leurs identifiants.
- La résolution des sous-types par Jackson gère le mapping.

Sans cela, Jackson désérialiserait par défaut tous les objets comme la classe de base, risquant de perdre les données spécifiques aux sous-classes.

### Fonctionnement étape par étape

1. **Annotations sur la classe de base** :
   - Utilisez `@JsonTypeInfo` pour spécifier où les informations de type sont intégrées (par exemple, en tant que propriété dans l'objet JSON).
   - Exemple :
     ```java
     @JsonTypeInfo(use = JsonTypeInfo.Id.NAME, include = JsonTypeInfo.As.PROPERTY, property = "@type")
     @JsonSubTypes({
         @JsonSubType(value = Cat.class, name = "cat"),
         @JsonSubType(value = Dog.class, name = "dog")
     })
     public abstract class Animal {
         public String name;
     }
     ```
     - `use = JsonTypeInfo.Id.NAME` : Utilise un nom (identifiant de type chaîne de caractères) pour le type.
     - `include = JsonTypeInfo.As.PROPERTY` : Ajoute les informations de type en tant que propriété ("@type") dans l'objet JSON.
     - `@JsonSubTypes` : Mappe les noms des sous-classes vers leurs classes Java (par exemple, "cat" → Cat.class).

2. **Processus de sérialisation** :
   - Lors de la sérialisation d'un objet Cat ou Dog, Jackson ajoute l'identifiant de type au JSON.
   - Exemple de sortie : `{"@type": "cat", "name": "Whiskers", "purr": true}` (si Cat a un champ "purr").

3. **Processus de désérialisation** :
   - Jackson lit le JSON et vérifie les informations de type (par exemple, la propriété "@type").
   - Il mappe l'identifiant ("cat") vers la sous-classe enregistrée (Cat.class) en utilisant `@JsonSubTypes`.
   - Il instancie la sous-classe correcte et peuple ses champs.
   - Si aucune correspondance n'est trouvée ou si les informations de type sont manquantes, il utilise par défaut la classe de base ou lève des exceptions (configurable via `defaultImpl`).

4. **Formats d'informations de type pris en charge** :
   - `@JsonTypeInfo.As.PROPERTY` : Le type en tant que champ (par exemple, `{"@type": "cat", ...}`).
   - `@JsonTypeInfo.As.WRAPPER_OBJECT` : Encapsule l'objet dans un wrapper avec le type comme clé (par exemple, `{"cat": {...}}`).
   - `@JsonTypeInfo.As.WRAPPER_ARRAY` : Utilise un format de tableau.
   - `@JsonTypeInfo.As.EXTERNAL_PROPERTY` : Informations de type dans un champ séparé (avancé, pour des structures de type XML).

### Configuration avancée et cas particuliers

- **Mappeurs de noms personnalisés** : Utilisez `@JsonTypeInfo(use = JsonTypeInfo.Id.CLASS)` pour intégrer le nom de classe complet directement dans le JSON (par exemple, `{"@class": "com.example.Cat", ...}`), ce qui peut être fragile lors des refactorisations.
- **Implémentation par défaut** : Ajoutez `defaultImpl = Animal.class` pour revenir à cette classe si les informations de type sont manquantes.
- **Visibilité et Mix-Ins** : Appliquez les annotations via des classes mix-in si vous ne pouvez pas modifier les classes sources.
- **Gestion des erreurs** : Si les informations de type ne correspondent à aucun sous-type enregistré, Jackson lève une `JsonMappingException`. Cela peut être géré avec des désérialiseurs personnalisés.
- **Performance** : Surcharge minimale lors de la désérialisation en raison de recherches efficaces, mais l'intégration des informations de type augmente la taille de la charge utile JSON.

Pour la documentation complète, consultez le guide officiel de Jackson : [Polymorphic Type Handling](https://github.com/FasterXML/jackson-docs/wiki/JacksonPolymorphicDeserialization). Cette fonctionnalité est stable depuis Jackson 2.x, avec des concepts similaires dans d'autres bibliothèques JSON comme Gson. Pour des personnalisations avancées, étendez `PolymorphicTypeValidator` pour la sécurité avec des entrées non fiables.
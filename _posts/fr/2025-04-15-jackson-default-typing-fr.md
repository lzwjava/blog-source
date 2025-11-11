---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Typage par défaut de Jackson expliqué
translated: true
type: note
---

### Qu'est-ce que le Typage par Défaut dans ObjectMapper de Jackson ?

L'`ObjectMapper` de Jackson est une classe centrale de la bibliothèque JSON Jackson pour Java, responsable de la sérialisation d'objets Java en JSON et de la désérialisation du JSON en objets. Le "typage par défaut" est une fonctionnalité qui améliore la gestion des types polymorphes (par exemple, lorsqu'un champ peut contenir différentes sous-classes). Il fonctionne en intégrant des informations de type dans la sortie JSON lors de la sérialisation, que le mapper utilise ensuite pendant la désérialisation pour instancier la classe concrète correcte.

Sans le typage par défaut, Jackson s'appuie sur le type déclaré (par exemple, une classe de base abstraite ou une interface), et vous pourriez avoir besoin d'une configuration personnalisée comme les annotations `@JsonTypeInfo` pour spécifier les sous-types. L'activation du typage par défaut fournit un mécanisme de repli global ou semi-global pour le polymorphisme, particulièrement utile pour les collections ou les maps contenant des types mélangés.

### Comment cela fonctionne-t-il ?

L'activation du typage par défaut modifie le processus de sérialisation :
1. **Sérialisation** : Lors de la sérialisation d'un graphe d'objets, Jackson ajoute un champ spécial `@class` ou des métadonnées similaires au JSON pour indiquer le type d'exécution des objets polymorphes. Cela se produit uniquement pour les types où le type déclaré ne spécifie pas entièrement la classe concrète (par exemple, une `List` contenant des objets `String` et `Integer`, ou des champs de classe abstraite).

2. **Désérialisation** : Pendant la désérialisation, le mapper utilise ces informations de type intégrées pour rechercher et instancier la classe exacte. Il s'appuie sur le `TypeFactory` de Jackson pour résoudre les types dynamiquement.

Pour l'activer, vous appelez l'une de ces méthodes sur une instance d'`ObjectMapper` :
- `mapper.enableDefaultTyping()` : Une méthode obsolète qui active l'inclusion de typage polymorphe à temps constant (susceptible de présenter des problèmes de sécurité).
- `mapper.activateDefaultTyping(ObjectMapper.DefaultTyping policy)` : Une alternative plus sûre et recommandée, introduite dans Jackson 2.10. Elle permet de spécifier une valeur d'énumération `DefaultTyping`, telle que :
  - `JAVA_LANG_OBJECT` : Inclut le typage pour toutes les références `Object`.
  - `NON_CONCRETE_AND_ARRAYS` : Inclut le typage pour les types abstraits/non concrets et les tableaux.
  - `NON_FINAL` : Inclut le typage pour les classes non finales.

Exemple d'utilisation :
```java
import com.fasterxml.jackson.databind.ObjectMapper;
import static com.fasterxml.jackson.databind.ObjectMapper.DefaultTyping;

ObjectMapper mapper = new ObjectMapper();
mapper.activateDefaultTyping(DefaultTyping.NON_CONCRETE_AND_ARRAYS);
```

Sans activation, si vous sérialisez une `List<Object>` avec des types mélangés, le JSON pourrait omettre les détails de type, entraînant des erreurs de désérialisation. Une fois activé, le JSON inclut des indices de type, par exemple : `[{"@class": "java.lang.String", "value": "hello"}, {"@class": "java.lang.Integer", "value": 42}]`.

### Considérations de sécurité et limitations

- **Vulnérabilités** : Activer aveuglément le typage par défaut (surtout l'ancienne méthode `enableDefaultTyping()`) peut exposer les systèmes à des attaques comme l'extraction de données, car cela permet de désérialiser des classes arbitraires via un JSON conçu à cet effet. Jackson limite cela par défaut dans les versions plus récentes, n'autorisant que les types courants sauf personnalisation.
- **Adéquation au cas d'usage** : Il est préférable de l'utiliser dans des environnements de confiance avec des données polymorphes (par exemple, des API internes). Pour les API publiques, préférez les annotations de type explicites ou les sérialiseurs/désérialiseurs personnalisés pour une meilleure sécurité.
- **Performance** : Ajoute une légère surcharge due aux informations de type intégrées, ce qui augmente la taille du JSON.

Si cela concerne un autre "object mapper" (par exemple, celui d'Elasticsearch ou d'une autre bibliothèque), fournissez plus de contexte pour une explication adaptée. Pour plus de détails, reportez-vous à la documentation officielle de Jackson.
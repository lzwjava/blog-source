---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Présentation de NSArray pour le développement iOS
translated: true
type: note
---

### Qu'est-ce que NSArray ?

`NSArray` est une classe du framework Foundation d'Apple, faisant partie du SDK iOS (et macOS, etc.). Elle représente une collection ordonnée et immuable d'objets, similaire à un tableau dans d'autres langages. Cela signifie qu'une fois que vous avez créé un `NSArray`, vous ne pouvez pas ajouter, supprimer ou remplacer des éléments — vous pouvez seulement le lire. Elle est couramment utilisée en Objective-C pour le développement d'applications iOS pour stocker et gérer des listes de données, comme les préférences utilisateur, les résultats de requêtes de base de données ou les éléments d'interface utilisateur.

Caractéristiques principales :
- **Immuable** : Taille et contenu fixes après la création (utilisez `NSMutableArray` pour les versions mutables).
- **Type-safe pour les objets** : Stocke des pointeurs vers des objets Objective-C (par exemple, `NSString`, `NSNumber`, classes personnalisées). Ne prend pas en charge les primitives directement — enveloppez-les dans `NSNumber` ou similaire.
- **Accès indexé** : Les éléments sont accessibles par un index entier (base 0).
- **Thread-safe** : Généralement sûr pour les lectures concurrentes, mais pas pour les écritures (puisqu'il est immuable).
- **Intégration** : Fonctionne de manière transparente avec d'autres classes Foundation comme `NSDictionary`, `NSString` et les composants UI Cocoa Touch.

Dans Swift, `NSArray` est bridgé vers `Array`, mais si vous travaillez en Objective-C (courant pour le code iOS legacy), vous utiliserez `NSArray` directement.

### Comment utiliser NSArray dans iOS

Pour utiliser `NSArray` dans un projet iOS :
1. Importez le framework Foundation (il est généralement inclus par défaut dans les apps iOS).
   ```objc
   #import <Foundation/Foundation.h>
   ```

2. **Créer un NSArray** :
   - Syntaxe littérale (iOS 6+) : `@[object1, object2, ...]`
   - Méthode init : `[[NSArray alloc] initWithObjects:object1, object2, nil]`
   - À partir d'un tableau C : `initWithArray:copyItems:`

   Exemple :
   ```objc
   NSArray *fruits = @[@"apple", @"banana", @"cherry"];
   // Ou :
   NSArray *numbers = [[NSArray alloc] initWithObjects:@1, @2, @3, nil];
   ```

3. **Accéder aux éléments** :
   - `objectAtIndex:` pour obtenir un élément.
   - `count` pour la longueur.
   - `firstObject` / `lastObject` pour les extrémités.
   - `containsObject:` pour vérifier l'existence.

   Exemple :
   ```objc
   NSString *firstFruit = [fruits objectAtIndex:0]; // "apple"
   NSUInteger count = [fruits count]; // 3
   BOOL hasOrange = [fruits containsObject:@"orange"]; // NO
   ```

4. **Itération** :
   - Énumération rapide : `for (id obj in array) { ... }`
   - `enumerateObjectsUsingBlock:` pour l'itération basée sur les blocs (iOS 4+).

   Exemple :
   ```objc
   for (NSString *fruit in fruits) {
       NSLog(@"Fruit: %@", fruit);
   }
   ```

5. **Opérations courantes** :
   - Tri : `sortedArrayUsingSelector:` ou `sortedArrayUsingComparator:`.
   - Filtrage : `filteredArrayUsingPredicate:` (avec NSPredicate).
   - Jointure : `componentsJoinedByString:` pour les chaînes de caractères.
   - Écriture dans un fichier : `writeToFile:atomically:`.

   Exemple (filtrage) :
   ```objc
   NSPredicate *predicate = [NSPredicate predicateWithFormat:@"length > 5"];
   NSArray *longFruits = [fruits filteredArrayUsingPredicate:predicate];
   // Résultats : @[@"banana", @"cherry"]
   ```

6. **Dans les contextes iOS** :
   - **Table Views** : Passez un `NSArray` aux méthodes de data source de `UITableView` comme `tableView:numberOfRowsInSection:` (via `count`) et `tableView:cellForRowAtIndexPath:` (via `objectAtIndex:`).
   - **User Defaults** : Stockez/retrievez avec `NSUserDefaults` : `[defaults setObject:array forKey:@"savedItems"];`.
   - **Gestion JSON** : Convertissez vers/depuis `NSData` avec `JSONObjectWithData:options:error:`.

Pour des besoins mutables (par exemple, ajouter des éléments dynamiquement), passez à `NSMutableArray` :
```objc
NSMutableArray *mutableFruits = [NSMutableArray arrayWithArray:fruits];
[mutableFruits addObject:@"date"];
```

### Conseils
- Vérifiez toujours `nil` ou les limites pour éviter les plantages : Utilisez `objectAtIndex:` avec validation de l'index.
- Performance : O(1) pour l'accès, O(n) pour les recherches.
- iOS moderne : Envisagez `Array` de Swift pour les nouveaux projets — il est plus type-safe.

[Documentation NSArray](https://developer.apple.com/documentation/foundation/nsarray)  
[Documentation NSMutableArray](https://developer.apple.com/documentation/foundation/nsmutablearray)
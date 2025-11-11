---
audio: false
generated: true
lang: fr
layout: post
title: Guide de style Java de Google
translated: true
type: note
---

## 1. Principes de base des fichiers sources
- **Nommage des fichiers** : 
  - Les fichiers sources sont nommés avec le nom sensible à la casse de la classe de premier niveau qu'ils contiennent
  - Les fichiers doivent utiliser l'encodage UTF-8
  - Les caractères spéciaux dans les noms de fichiers sont déconseillés

## 2. Structure des fichiers sources
### Organisation des fichiers sources
1. Instruction package
2. Instructions d'import
3. Exactement une classe de premier niveau

### Règles pour les instructions d'import
- Pas d'imports avec des caractères génériques (*)
- Les imports statiques sont autorisés
- Les imports sont organisés dans un ordre spécifique :
  - Tous les imports statiques
  - Tous les imports non statiques
  - Les imports dans chaque groupe sont classés par ordre alphabétique

## 3. Règles de formatage

### Indentation et accolades
- Utiliser 2 espaces pour l'indentation (pas de tabulations)
- Les accolades sont utilisées avec les instructions `if`, `else`, `for`, `do` et `while`, même pour les blocs d'une seule ligne
- Le style K&R pour le placement des accolades est recommandé
  ```java
  public void method() {
    if (condition) {
      // Bloc de code
    }
  }
  ```

### Longueur de ligne et retour à la ligne
- La longueur maximale de ligne est de 100 caractères
- Les retours à la ligne sont préférés au niveau des ruptures de syntaxe de plus haut niveau
- Lors de la rupture de chaînes d'appels de méthode, la rupture se produit avant le `.`

## 4. Conventions de nommage

### Règles générales
- **Packages** : minuscules, pas de tirets bas
- **Classes** : UpperCamelCase
- **Méthodes** : lowerCamelCase
- **Constantes** : UPPER_SNAKE_CASE
- **Champs non constants** : lowerCamelCase
- **Paramètres** : lowerCamelCase
- **Variables locales** : lowerCamelCase

### Pratiques de nommage spécifiques
- Éviter les abréviations
- Les noms d'exception doivent se terminer par `Exception`
- Les classes de test sont nommées `TestClassName`

## 5. Pratiques de programmation

### Règles du langage Java
- **Exceptions** : 
  - Intercepter des exceptions spécifiques
  - Éviter les blocs catch vides
  - Toujours inclure un message d'erreur détaillé
- **Mot-clé Final** : 
  - Utiliser `final` pour les paramètres de méthode
  - Préférer les objets immuables
- **Annotations** : 
  - `@Override` est obligatoire pour les méthodes de substitution
  - Utiliser les annotations standard de manière appropriée

### Structure du code
- Préférer la composition à l'héritage
- Garder les méthodes courtes et ciblées
- Une instruction par ligne
- Éviter l'imbrication profonde des conditionnelles

## 6. Commentaires et documentation

### Règles pour les Javadoc
- Toutes les classes et méthodes publiques doivent avoir une Javadoc
- Les commentaires Javadoc commencent par `/**`
- Inclure la description, les paramètres, les valeurs de retour et les exceptions
- Utiliser les balises `@param`, `@return`, `@throws`

### Commentaires en ligne
- À utiliser avec parcimonie
- Expliquer le "pourquoi", pas le "quoi"
- Garder les commentaires concis et significatifs

## 7. Considérations sur le contrôle de version
- Éviter de commettre du code commenté
- Utiliser les fonctionnalités du système de contrôle de version au lieu des commentaires de code pour suivre les modifications

## 8. Considérations de performance
- Préférer les boucles `for` améliorées
- Utiliser `StringBuilder` pour la concaténation de chaînes
- Fermer les ressources en utilisant try-with-resources
- Éviter de créer des objets inutiles

## 9. Principes de test
- Écrire des tests unitaires
- Viser une couverture de code élevée
- Utiliser JUnit pour les tests
- Simuler les dépendances externes
- Tester les cas limites et les conditions d'erreur

## 10. Outils supplémentaires
- Google fournit un formateur Java et des outils d'analyse statique
- CheckStyle et Error Prone peuvent être utilisés pour faire respecter les règles de style

## Conclusion
Le Google Java Style Guide fournit un ensemble complet de règles pour garantir un code Java cohérent, lisible et maintenable entre les projets.
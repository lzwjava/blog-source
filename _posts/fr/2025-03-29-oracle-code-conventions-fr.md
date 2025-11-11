---
audio: false
generated: true
lang: fr
layout: post
title: Conventions de codage d'Oracle pour le langage de programmation Java
translated: true
type: note
---

## 1. Organisation des fichiers

### 1.1 Noms de fichiers
- Les fichiers sources doivent avoir l'extension `.java`
- Les noms de fichiers sources doivent correspondre exactement au nom de la classe publique dans le fichier
- Exemples :
  - `MyClass.java` contient une classe publique nommée `MyClass`
  - `CircleShape.java` contient une classe publique nommée `CircleShape`

### 1.2 Structure des fichiers
1. Commentaires d'en-tête
2. Instruction package
3. Instructions import
4. Déclarations de classes et d'interfaces

## 2. Formatage et indentation

### 2.1 Indentation
- Utiliser 4 espaces pour l'indentation (pas de tabulations)
- Indenter les lignes de continuation de 8 espaces
- Les accolades doivent s'aligner verticalement

### 2.2 Longueur de ligne
- La longueur maximale recommandée est de 80 caractères
- Pour les instructions longues, couper les lignes à un niveau logique supérieur

### 2.3 Retour à la ligne
- Couper la ligne avant un opérateur
- Aligner la nouvelle ligne avec le début de l'expression au même niveau

## 3. Commentaires

### 3.1 Commentaires de fichier
- Chaque fichier source doit commencer par un bloc de commentaire :
  ```java
  /*
   * Nom de la classe
   * 
   * Informations sur la version
   * 
   * Date
   * 
   * Notice de copyright
   */
  ```

### 3.2 Commentaires d'implémentation
- Utiliser `/* */` pour les commentaires multi-lignes
- Utiliser `//` pour les commentaires d'une seule ligne
- Les commentaires doivent expliquer le "pourquoi", pas le "quoi"

### 3.3 Commentaires de documentation
- Utiliser les commentaires de style Javadoc pour les classes, interfaces, méthodes
- Inclure :
  - Une brève description
  - `@param` pour les paramètres de méthode
  - `@return` pour les valeurs de retour
  - `@throws` pour les exceptions

## 4. Déclarations

### 4.1 Nombre par ligne
- Une déclaration par ligne
- Recommandé :
  ```java
  int level;        // Correct
  int size;         // Correct
  
  // À éviter :
  int level, size;  // Non recommandé
  ```

### 4.2 Initialisation
- Initialiser les variables lors de la déclaration quand c'est possible
- Grouper les déclarations liées ensemble

## 5. Instructions

### 5.1 Instructions simples
- Une instruction par ligne
- Utiliser un espace après les virgules
- Utiliser des espaces autour des opérateurs

### 5.2 Instructions composées
- Les accolades sont utilisées avec les instructions `if`, `else`, `for`, `while`, `do`, même pour les blocs d'une seule ligne

### 5.3 Instructions return
- Préférer un return explicite
- Éviter les `else` inutiles après un `return`

## 6. Conventions de nommage

### 6.1 Noms de packages
- Tout en minuscules
- Préfixe unique, souvent le domaine de l'entreprise inversé
- Exemple : `com.company.project`

### 6.2 Noms de classes
- UpperCamelCase
- Nom ou groupe nominal
- Exemples : `DataProcessor`, `HttpClient`

### 6.3 Noms d'interfaces
- Similaires aux noms de classes
- Considérer la description d'un comportement
- Exemples : `Runnable`, `Serializable`

### 6.4 Noms de méthodes
- lowerCamelCase
- Verbe ou groupe verbal
- Exemples : `calculateTotal()`, `sendMessage()`

### 6.5 Noms de variables
- lowerCamelCase
- Significatifs et descriptifs
- Éviter les noms d'une seule lettre sauf pour les variables temporaires

### 6.6 Noms de constantes
- TOUT_EN_MAJUSCULES avec des underscores
- Exemple : `MAX_VALUE`, `COLOR_RED`

## 7. Pratiques de programmation

### 7.1 Visibilité
- Utiliser la visibilité la plus basse possible
- Préférer `private` à `public`
- Utiliser des méthodes d'accès pour les champs de classe

### 7.2 Portée des variables
- Déclarer les variables dans la plus petite portée possible
- Initialiser les variables près de leur première utilisation

### 7.3 Gestion des exceptions
- Toujours inclure un message dans les exceptions
- Capturer des exceptions spécifiques
- Utiliser try-catch-finally de manière appropriée

## 8. Bonnes pratiques

### 8.1 Éviter les nombres magiques
- Utiliser des constantes nommées au lieu de nombres littéraux
- Améliorer la lisibilité et la maintenabilité du code

### 8.2 Préférer l'immuabilité
- Utiliser `final` pour les variables qui ne changent pas
- Créer des classes immuables quand c'est possible

## Conclusion
Ces conventions visent à améliorer la lisibilité, la maintenabilité et la cohérence du code dans les projets Java.
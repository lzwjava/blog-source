---
audio: false
generated: true
lang: fr
layout: post
title: Modèles de remplacement structurel IntelliJ
translated: true
type: note
---

Voici 10 exemples de modèles de Remplacement Structurel d'IntelliJ, classés pour plus de clarté. Ils peuvent être incroyablement puissants pour le refactoring, l'application de normes de codage et l'automatisation de transformations de code courantes.

**Refactoring et Simplification de base :**

1.  **Remplacer `if (condition) return true; else return false;` par `return condition;`**

      * **Modèle de Recherche :**
        ```java
        if ($CONDITION$) {
            return true;
        } else {
            return false;
        }
        ```
      * **Modèle de Remplacement :**
        ```java
        return $CONDITION$;
        ```
      * **Contexte :** Simplifie les instructions de retour booléennes.

2.  **Remplacer `if (condition) { statement; }` par `if (!condition) { continue/break/return; }` (Clause de Garde)**

      * **Modèle de Recherche :**
        ```java
        if ($CONDITION$) {
            $STATEMENTS$;
        }
        ```
      * **Modèle de Remplacement :** (Celui-ci suggère plus une transformation, vous devriez ajuster manuellement la partie interne)
        ```java
        if (!$CONDITION$) {
            // Envisagez continue, break ou return ici
        }
        $STATEMENTS$;
        ```
      * **Contexte :** Encourage l'utilisation de clauses de garde pour un flux de code plus propre. Vous utiliseriez typiquement une action "Remplacer par" après avoir trouvé la structure.

**Opérations sur les Collections et Streams :**

3.  **Remplacer `for (Type item : collection) { if (item.getProperty() == value) { ... } }` par un Stream `filter`**

      * **Modèle de Recherche :**
        ```java
        for ($TYPE$ $ITEM$ : $COLLECTION$) {
            if ($ITEM$.$METHOD$($VALUE$)) {
                $STATEMENTS$;
            }
        }
        ```
      * **Modèle de Remplacement :**
        ```java
        $COLLECTION$.stream()
            .filter($ITEM$ -> $ITEM$.$METHOD$($VALUE$))
            .forEach($ITEM$ -> $STATEMENTS$); // Ou .map().collect(), etc.
        ```
      * **Contexte :** Migration des boucles traditionnelles vers les Java Streams pour le filtrage. C'est un exemple général ; vous auriez probablement besoin de modèles plus spécifiques pour `map`, `collect`, etc.

4.  **Remplacer `new ArrayList<>().add(item1); new ArrayList<>().add(item2);` par `List.of(item1, item2);`**

      * **Modèle de Recherche :** (Cela pourrait nécessiter plusieurs modèles pour un nombre variable d'appels `add`, ou une expression régulière plus complexe. Une approche plus simple pour 2 éléments) :
        ```java
        java.util.ArrayList<$TYPE$> $LIST$ = new java.util.ArrayList<>();
        $LIST$.add($ITEM1$);
        $LIST$.add($ITEM2$);
        ```
      * **Modèle de Remplacement :**
        ```java
        java.util.List<$TYPE$> $LIST$ = java.util.List.of($ITEM1$, $ITEM2$);
        ```
      * **Contexte :** Utilisation de `List.of()` (Java 9+) pour les listes immuables.

**Gestion des Erreurs et des Ressources :**

5.  **Remplacer `try { ... } catch (Exception e) { e.printStackTrace(); }` par une journalisation plus spécifique**

      * **Modèle de Recherche :**
        ```java
        try {
            $STATEMENTS$;
        } catch (java.lang.Exception $EXCEPTION$) {
            $EXCEPTION$.printStackTrace();
        }
        ```
      * **Modèle de Remplacement :**
        ```java
        try {
            $STATEMENTS$;
        } catch (java.lang.Exception $EXCEPTION$) {
            // Remplacez par votre framework de journalisation préféré, par ex. :
            // logger.error("An error occurred", $EXCEPTION$);
            throw new RuntimeException($EXCEPTION$); // Ou relancez une exception spécifique
        }
        ```
      * **Contexte :** Encourage une journalisation appropriée des erreurs au lieu de simplement imprimer les traces de pile.

6.  **Remplacer `try { ... } finally { closeable.close(); }` par `try-with-resources`**

      * **Modèle de Recherche :**
        ```java
        java.io.Closeable $CLOSEABLE$ = null;
        try {
            $CLOSEABLE$ = $INITIALIZATION$;
            $STATEMENTS$;
        } finally {
            if ($CLOSEABLE$ != null) {
                $CLOSEABLE$.close();
            }
        }
        ```
      * **Modèle de Remplacement :**
        ```java
        try ($CLOSEABLE$ = $INITIALIZATION$) {
            $STATEMENTS$;
        }
        ```
      * **Contexte :** Modernisation de la gestion des ressources pour utiliser `try-with-resources` (Java 7+).

**Structure de Classe et de Méthode :**

7.  **Trouver les champs qui peuvent être `final`**

      * **Modèle de Recherche :**
        ```java
        class $CLASS$ {
            $TYPE$ $FIELD$;
        }
        ```
      * **Modèle de Remplacement :** (Cela sert plus à trouver, puis à utiliser un correctif rapide)
        ```java
        class $CLASS$ {
            // Envisagez de rendre ce champ final s'il n'est assigné qu'une seule fois
            final $TYPE$ $FIELD$;
        }
        ```
      * **Contexte :** Identifier les opportunités d'améliorer l'immuabilité. Vous configureriez un filtre pour n'afficher que les champs sans assignations multiples.

8.  **Remplacer `private static final Logger logger = LoggerFactory.getLogger(MyClass.class);` par un utilitaire de journalisation personnalisé**

      * **Modèle de Recherche :**
        ```java
        private static final org.slf4j.Logger $LOGGER_VAR$ = org.slf4j.LoggerFactory.getLogger($CLASS_NAME$.class);
        ```
      * **Modèle de Remplacement :**
        ```java
        private static final org.slf4j.Logger $LOGGER_VAR$ = com.yourcompany.util.LoggerProvider.getLogger(); // Ou un getLogger($CLASS_NAME$.class) plus spécifique depuis votre utilitaire
        ```
      * **Contexte :** Imposer un modèle d'initialisation de journalisation spécifique dans toute votre base de code.

**Annotations et Code Boilerplate :**

9.  **Ajouter `@Override` aux méthodes qui redéfinissent les méthodes de la superclasse (si manquant)**

      * **Modèle de Recherche :** (C'est plus complexe et souvent mieux géré par les inspections intégrées d'IntelliJ, mais pour démonstration)
        ```java
        class $CLASS$ {
            $RETURN_TYPE$ $METHOD$($PARAMS$) {
                $STATEMENTS$;
            }
        }
        ```
      * **Modèle de Remplacement :** (Encore une fois, pour trouver, puis appliquer un correctif rapide)
        ```java
        class $CLASS$ {
            @Override // Ajoutez si elle redéfinit une méthode de la superclasse
            $RETURN_TYPE$ $METHOD$($PARAMS$) {
                $STATEMENTS$;
            }
        }
        ```
      * **Contexte :** Appliquer les bonnes pratiques et détecter les fautes de frappe. Vous utiliseriez un filtre pour vérifier si la méthode existe dans une superclasse/interface.

10. **Remplacer les méthodes `getter/setter` répétitives par des annotations Lombok**

      * **Modèle de Recherche :** (Pour un seul getter, ce serait très répétitif pour une classe)
        ```java
        public $TYPE$ get$PROPERTY_NAME$() {
            return this.$FIELD_NAME$;
        }
        ```
      * **Modèle de Remplacement :** (C'est conceptuel, car vous supprimeriez le getter et ajouteriez `@Getter` au champ ou à la classe)
        ```java
        // Envisagez de remplacer par @lombok.Getter sur le champ :
        // @lombok.Getter
        // private $TYPE$ $FIELD_NAME$;
        ```
      * **Contexte :** Automatiser la transition vers Lombok. Pour une classe complète, vous pourriez cibler la classe elle-même et suggérer les annotations `@Data` ou `@Getter/@Setter` basées sur la présence de ces méthodes. C'est l'une des transformations les plus avancées et potentiellement multi-étapes.

**Comment les Utiliser dans IntelliJ :**

1.  Allez dans `Analyze` -> `Inspect Code...`
2.  Dans la fenêtre `Inspection Profile`, cliquez sur le `...` à côté du nom du profil pour le modifier.
3.  Naviguez jusqu'à `Java` -> `General` -> `Structural Search Inspection`.
4.  Cliquez sur le bouton `+` pour ajouter un nouveau modèle de recherche/remplacement.
5.  Définissez votre `Search Template` et votre `Replacement Template`.
6.  Utilisez l'onglet `Variables` pour définir des contraintes pour vos variables (par ex. type, texte, comptage).
7.  Exécutez l'inspection sur votre code. IntelliJ suggérera des remplacements ou mettra en évidence les résultats.

Ces exemples démontrent la polyvalence de la Recherche et du Remplacement Structurel. Plus vos modèles sont spécifiques et contraints, plus les remplacements seront précis et utiles.
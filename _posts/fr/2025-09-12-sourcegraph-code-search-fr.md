---
audio: false
date: 2025-09-12
generated: true
image: false
lang: fr
layout: post
model: mistralai/mistral-medium-3.1
title: Guide de Recherche de Code Sourcegraph
translated: true
type: note
---

Sourcegraph est un outil puissant de recherche et de navigation dans le code qui permet aux développeurs de rechercher dans plusieurs dépôts, de comprendre les dépendances du code et de naviguer efficacement dans de grandes bases de code. Ce guide couvre **la syntaxe de recherche, les bonnes pratiques et les recherches spécifiques au langage (Java & Python)**.

---

## **1. Syntaxe de Recherche de Base**
Sourcegraph prend en charge **la recherche littérale, par expression régulière et structurelle** avec des filtres.

### **1.1. Recherche Littérale**
Rechercher du texte exact :
```
"def calculate_sum"
```

### **1.2. Recherche par Expression Régulière**
Utiliser `/.../` pour les expressions régulières :
```
/def \w+_sum\(/
```

### **1.3. Recherche Structurelle (Bêta)**
Rechercher des modèles de code (par exemple, des définitions de fonction) :
```
type:func def calculate_sum
```

### **1.4. Filtres**
Affiner les recherches avec des filtres :
- `repo:` – Rechercher dans un dépôt spécifique
  ```
  repo:github.com/elastic/elasticsearch "def search"
  ```
- `file:` – Rechercher dans des fichiers spécifiques
  ```
  file:src/main/java "public class"
  ```
- `lang:` – Rechercher dans un langage spécifique
  ```
  lang:python "def test_"
  ```
- `type:` – Rechercher des symboles (fonctions, classes, etc.)
  ```
  type:func lang:go "func main"
  ```

---

## **2. Techniques de Recherche Avancées**
### **2.1. Opérateurs Booléens**
- `AND` (par défaut) : `def calculate AND sum`
- `OR` : `def calculate OR def sum`
- `NOT` : `def calculate NOT def subtract`

### **2.2. Caractères de Substitution**
- `*` – Correspond à n'importe quelle séquence de caractères
  ```
  "def calculate_*"
  ```
- `?` – Correspond à un seul caractère
  ```
  "def calculate_?"
  ```

### **2.3. Sensibilité à la Casse**
- Insensible à la casse par défaut
- Forcer la sensibilité à la casse avec `case:yes`
  ```
  case:yes "Def Calculate"
  ```

### **2.4. Recherche dans les Commentaires**
Utiliser `patternType:literal` pour rechercher dans les commentaires :
```
patternType:literal "// TODO:"
```

---

## **3. Recherche dans le Code Java**
### **3.1. Trouver des Classes**
```
type:symbol lang:java "public class"
```
### **3.2. Trouver des Méthodes**
```
type:func lang:java "public void"
```
### **3.3. Trouver des Annotations**
```
lang:java "@Override"
```
### **3.4. Trouver des Imports**
```
lang:java "import org.springframework"
```
### **3.5. Trouver la Gestion des Exceptions**
```
lang:java "try {" AND "catch (Exception"
```

---

## **4. Recherche dans le Code Python**
### **4.1. Trouver des Fonctions**
```
type:func lang:python "def calculate"
```
### **4.2. Trouver des Classes**
```
type:symbol lang:python "class Calculator"
```
### **4.3. Trouver des Imports**
```
lang:python "import pandas"
```
### **4.4. Trouver des Décorateurs**
```
lang:python "@app.route"
```
### **4.5. Trouver les Docstrings**
```
lang:python '"""'
```

---

## **5. Bonnes Pratiques**
1. **Utilisez `lang:`** pour affiner les résultats.
2. **Combinez les filtres** (`repo:`, `file:`, `type:`) pour plus de précision.
3. **Utilisez les expressions régulières** pour une correspondance de modèles flexible.
4. **Sauvegardez les recherches** pour les requêtes fréquentes.
5. **Utilisez `case:yes`** lorsque nécessaire.

---

## **6. Exemples de Requêtes**

| **Objectif** | **Requête** |
|----------|-----------|
| Trouver toutes les méthodes `main` en Java | `lang:java "public static void main"` |
| Trouver les fonctions de test Python | `lang:python "def test_"` |
| Trouver les commentaires TODO en Go | `lang:go "// TODO:"` |
| Trouver les contrôleurs Spring Boot | `lang:java "@RestController"` |
| Trouver toutes les instructions `if` en JS | `lang:javascript "if ("` |

---

## **7. Conclusion**
La recherche de Sourcegraph est **puissante et flexible**, prenant en charge **les recherches littérales, par expression régulière et structurelles** dans plusieurs langages. En maîtrisant les filtres (`lang:`, `repo:`, `type:`), vous pouvez naviguer efficacement dans de grandes bases de code.

### **Prochaines Étapes**
- Essayez les **recherches sauvegardées** pour les requêtes récurrentes.
- Explorez l'**intelligence du code** (info-bulles, navigation inter-dépôts).
- Utilisez les **extensions Sourcegraph** (VS Code, JetBrains).

Souhaitez-vous une exploration plus approfondie d'une fonctionnalité spécifique ? 🚀
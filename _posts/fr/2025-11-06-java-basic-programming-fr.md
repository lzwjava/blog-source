---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Guide de Programmation Java de Base
translated: true
type: note
---

Voici un guide ciblé pour **Partie II : Programmation de base** de *08553 Introduction à la programmation — Java*, adapté pour l'**Examen national d'auto-enseignement de l'enseignement supérieur (自考)**. Cette section vous entraîne à écrire de petits programmes Java corrects et à comprendre comment Java gère les données et les expressions.

---

## 1. Lecture des entrées depuis la console

### 1.1 Utilisation de `Scanner`

Java lit les entrées avec la classe `Scanner` de `java.util`.

```java
import java.util.Scanner;

public class InputExample {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Entrez votre nom : ");
        String name = sc.nextLine();
        System.out.print("Entrez votre âge : ");
        int age = sc.nextInt();
        System.out.println("Bonjour " + name + ", vous avez " + age + " ans.");
        sc.close();
    }
}
```

**Points clés :**

* Toujours `import java.util.Scanner;`
* Utilisez `nextInt()`, `nextDouble()`, `nextLine()` selon le type de données.
* Fermez le `Scanner` pour libérer les ressources.
* Attention : `nextLine()` lit le reste d'une ligne, donc la mélanger avec `nextInt()` peut entraîner une entrée ignorée.

---

## 2. Identifiants, Variables, Expressions, Affectations et Constantes

### 2.1 Identifiants

Noms que vous donnez aux variables, méthodes ou classes.
**Règles :**

* Doit commencer par une lettre, `_` ou `$`.
* Ne peut pas commencer par un chiffre.
* Sensible à la casse (`score` ≠ `Score`).
* Ne peut pas être un mot-clé (`int`, `class`, `if`, etc.).

**Exemples :**
`studentName`, `_total`, `$price`

### 2.2 Variables

Une variable contient des données d'un certain **type**.
Exemples de déclaration :

```java
int age = 20;
double price = 12.5;
char grade = 'A';
boolean passed = true;
```

### 2.3 Instructions d'affectation

Affectez une valeur en utilisant `=` (droite → gauche) :

```java
x = 5;
y = x + 2;
```

### 2.4 Constantes

Déclarées avec `final`, ne peuvent pas être modifiées ensuite :

```java
final double PI = 3.14159;
```

Utilisez des noms en majuscules pour les constantes.

---

## 3. Types de données numériques et opérations

### 3.1 Types numériques courants

* `byte` (entier 8 bits)
* `short` (16 bits)
* `int` (32 bits, le plus courant)
* `long` (64 bits)
* `float` (décimal 32 bits)
* `double` (décimal 64 bits, plus précis)

**Exemple :**

```java
int count = 5;
double price = 19.99;
```

### 3.2 Opérateurs arithmétiques de base

`+`, `-`, `*`, `/`, `%`

Exemples :

```java
int a = 10, b = 3;
System.out.println(a / b);  // 3 (division entière)
System.out.println(a % b);  // 1
System.out.println((double)a / b); // 3.3333 (conversion de type)
```

---

## 4. Conversion de type (Casting)

### 4.1 Conversion automatique (Élargissement)

Petit → grand type automatiquement :
`int` → `long` → `float` → `double`

Exemple :

```java
int i = 10;
double d = i;  // conversion automatique
```

### 4.2 Conversion manuelle (Casting)

Convertir explicitement un plus grand → plus petit type :

```java
double d = 9.7;
int i = (int) d; // i = 9 (fraction perdue)
```

Attention à la **perte de précision**.

---

## 5. Évaluation des expressions et priorité des opérateurs

### 5.1 Ordre des opérations

Java suit un ordre défini :

1. Parenthèses `( )`
2. Opérateurs unaires `+`, `-`, `++`, `--`
3. Multiplication, division, modulo `* / %`
4. Addition et soustraction `+ -`
5. Affectation `=`

Exemple :

```java
int x = 2 + 3 * 4;   // 14, pas 20
int y = (2 + 3) * 4; // 20
```

### 5.2 Expressions mixtes

Si un opérande est `double`, le résultat devient `double` :

```java
double result = 5 / 2;     // 2.0 (division entière d'abord)
double result2 = 5.0 / 2;  // 2.5 (division flottante)
```

---

## 6. Affectation augmentée et Incrémentation/Décrémentation

### 6.1 Affectation augmentée

Opérateurs raccourcis :

```java
x += 3;  // identique à x = x + 3
y *= 2;  // identique à y = y * 2
```

### 6.2 Incrémentation et Décrémentation

`++` augmente de 1, `--` diminue de 1.
Deux formes :

```java
int a = 5;
System.out.println(a++); // affiche 5, puis a = 6
System.out.println(++a); // a = 7, puis affiche 7
```

**Rappel :**

* Postfixe (`a++`) → utiliser puis incrémenter
* Préfixe (`++a`) → incrémenter puis utiliser

---

## 7. Erreurs courantes à éviter

* Utiliser `=` au lieu de `==` dans les comparaisons.
* Division entière quand on attend des décimales.
* Oublier d'initialiser une variable avant de l'utiliser.
* Perdre des données dans la conversion de type (ex: `(int) 3.9` → 3).

---

## 8. Questions d'examen typiques

**Exemple 1 :**

> Quel est le résultat du code suivant ?
>
> ```java
> int x = 5, y = 2;
> double z = x / y;
> System.out.println(z);
> ```

**Réponse :** `2.0` (division entière avant l'affectation)

**Exemple 2 :**

> Quel opérateur a la priorité la plus élevée ?
> A. `+`
> B. `*`
> C. `=`
> D. `++`
> **Réponse :** D

**Exemple 3 :**

> Quel est le résultat de ce code ?
>
> ```java
> int a = 3;
> int b = ++a + a++;
> System.out.println(b);
> ```

**Explication :**
`++a` rend `a = 4`, ajoute `4`, puis `a++` utilise `4` et incrémente à `5`.
Donc `b = 8`.

---

Souhaitez-vous que je continue avec la **Partie III : Structures de contrôle (Instructions de sélection et de boucle)** ensuite ? Elle couvre `if`, `switch`, `for`, `while` et constitue le cœur de la logique procédurale dans l'examen Java.
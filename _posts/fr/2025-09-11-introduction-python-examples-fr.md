---
audio: false
date: 2025-09-11
generated: true
image: false
lang: fr
layout: post
model: google/gemini-2.5-flash
title: Introduction aux exemples de code Python
translated: true
type: note
---

D'accord, "du code Python" peut vouloir dire beaucoup de choses ! Python est incroyablement polyvalent. Je vais vous donner quelques exemples courants, du plus basique au plus élaboré, couvrant différents concepts.

---

### 1. Hello World (Le Démarrage Classique)

C'est le programme Python le plus simple possible.

```python
# Ceci est un commentaire. Les commentaires sont ignorés par Python.
print("Hello, World!")
```

**Explication :**
*   `print()` est une fonction intégrée qui affiche l'argument donné dans la console.
*   `"Hello, World!"` est une chaîne de caractères (texte).

---

### 2. Variables, Arithmétique de Base et Saisie Utilisateur

Ce code montre comment stocker des données dans des variables, effectuer des calculs simples et obtenir une saisie de l'utilisateur.

```python
# Variables pour stocker des données
name = input("Quel est votre nom ? ") # Obtenir une saisie de l'utilisateur
age_str = input("Quel âge avez-vous ? ")

# Convertir l'âge d'une chaîne de caractères en entier pour les calculs
age = int(age_str)

# Arithmétique de base
year_of_birth = 2023 - age # En supposant que l'année en cours est 2023 pour simplifier
# Vous pourriez aussi utiliser : import datetime; year_of_birth = datetime.date.today().year - age

# Afficher une sortie formatée en utilisant un f-string (formatted string literal)
print(f"Bonjour, {name} ! Vous avez {age} ans.")
print(f"Vous êtes probablement né(e) en {year_of_birth}.")

# Une vérification conditionnelle simple
if age < 18:
    print("Vous êtes mineur.")
else:
    print("Vous êtes majeur.")
```

**Explication :**
*   `input()` : Invite l'utilisateur à saisir du texte et le renvoie sous forme de chaîne de caractères.
*   `name`, `age_str`, `age`, `year_of_birth` : Ce sont des variables stockant différents types de données (string, integer).
*   `int()` : Convertit une chaîne de caractères en entier. C'est nécessaire car `input()` renvoie toujours une chaîne, et on ne peut pas faire de calculs directement avec des chaînes.
*   `f-strings` : Un moyen pratique d'intégrer des expressions dans des littéraux de chaîne. Notez le `f` avant la guillemet ouvrant.
*   `if/else` : Instructions de contrôle de flux qui exécutent différents blocs de code en fonction d'une condition.

---

### 3. Listes et Boucles

Les listes sont des collections ordonnées d'éléments. Les boucles sont utilisées pour répéter un bloc de code plusieurs fois.

```python
# Une liste de fruits
fruits = ["apple", "banana", "cherry", "date"]

print("\nMes fruits préférés :")

# Parcourir la liste en utilisant une boucle 'for'
for fruit in fruits:
    print(f"- {fruit.capitalize()}") # .capitalize() met la première lettre en majuscule

# Accéder aux éléments par index (les listes sont indexées à partir de zéro)
print(f"\nLe premier fruit est : {fruits[0]}")
print(f"Le dernier fruit est : {fruits[-1]}") # Un index négatif accède depuis la fin

# Ajouter un élément
fruits.append("elderberry")
print(f"Liste mise à jour : {fruits}")

# Supprimer un élément
fruits.remove("banana")
print(f"Liste après suppression de 'banana' : {fruits}")

# Boucler en utilisant 'range' pour obtenir les indices
print("\nFruits avec leurs indices :")
for i in range(len(fruits)): # len() donne le nombre d'éléments dans la liste
    print(f"Index {i}: {fruits[i]}")
```

**Explication :**
*   `[]` : Utilisé pour définir une liste.
*   `for ... in ...` : Une boucle `for` qui itère sur chaque élément d'une séquence (comme une liste).
*   `fruit.capitalize()` : Une méthode de chaîne qui renvoie une copie de la chaîne avec son premier caractère en majuscule.
*   `fruits[0]` : Accède au premier élément (index 0).
*   `fruits[-1]` : Accède au dernier élément.
*   `list.append()` : Ajoute un élément à la fin de la liste.
*   `list.remove()` : Supprime la première occurrence d'un élément spécifié.
*   `range(len(fruits))` : Génère une séquence de nombres de 0 jusqu'à (sans inclure) la longueur de la liste, utile pour accéder aux éléments par leur index.

---

### 4. Fonctions

Les fonctions sont des blocs de code réutilisables qui effectuent une tâche spécifique.

```python
# Définir une fonction qui prend des arguments
def greet_person(name, age):
    """
    Cette fonction salue une personne et lui dit son âge.
    C'est une bonne pratique d'inclure une docstring comme celle-ci.
    """
    return f"Bonjour, {name} ! Vous avez {age} ans."

# Appeler la fonction
message1 = greet_person("Alice", 30)
print(message1)

# L'appeler à nouveau avec des arguments différents
message2 = greet_person("Bob", 25)
print(message2)

# Définir une fonction avec un paramètre par défaut
def calculate_area(length, width=10):
    """Calcule l'aire d'un rectangle."""
    return length * width

print(f"\nAire d'un rectangle de 5x10 : {calculate_area(5)}") # Utilise la largeur par défaut
print(f"Aire d'un rectangle de 5x7 : {calculate_area(5, 7)}") # Remplace la largeur par défaut
```

**Explication :**
*   `def` : Mot-clé pour définir une fonction.
*   `greet_person(name, age)` : Nom de la fonction et ses paramètres (entrées).
*   `return` : Renvoie une valeur depuis la fonction.
*   Docstrings (`"""La docstring va ici"""`) : Expliquent ce que fait la fonction. Utile pour la documentation.
*   `calculate_area(length, width=10)` : Montre un paramètre par défaut. Si `width` n'est pas fourni lors de l'appel de la fonction, il prend la valeur 10 par défaut.

---

### 5. Dictionnaires

Les dictionnaires stockent des données sous forme de paires clé-valeur. Ils sont non ordonnés (dans les anciennes versions de Python, ordonnés à partir de Python 3.7+).

```python
# Un dictionnaire représentant une personne
person = {
    "first_name": "Charlie",
    "last_name": "Smith",
    "age": 40,
    "city": "London",
    "occupations": ["Engineer", "Teacher"] # Une liste peut être une valeur
}

print("\nDétails de la personne :")

# Accéder aux valeurs par clé
print(f"Nom : {person['first_name']} {person['last_name']}")
print(f"Vit à : {person.get('city', 'Inconnu')}") # .get() est plus sûr, renvoie None/une valeur par défaut si la clé n'est pas trouvée
print(f"Première profession : {person['occupations'][0]}")

# Modifier une valeur
person["age"] = 41
print(f"Nouvel âge : {person['age']}")

# Ajouter une nouvelle paire clé-valeur
person["email"] = "charlie.smith@example.com"
print(f"Email : {person['email']}")

# Parcourir un dictionnaire
print("\nToutes les clés :")
for key in person: # Parcourt les clés par défaut
    print(key)

print("\nToutes les valeurs :")
for value in person.values():
    print(value)

print("\nToutes les paires clé-valeur :")
for key, value in person.items():
    print(f"{key}: {value}")
```

**Explication :**
*   `{}` : Utilisé pour définir un dictionnaire.
*   `"key": value` : Paires clé-valeur. Les clés doivent être uniques et immuables (comme des chaînes ou des nombres). Les valeurs peuvent être de n'importe quel type de données.
*   `person['key']` : Accède à la valeur associée à `key`.
*   `person.get('key', 'default_value')` : Un moyen plus sûr d'accéder, évite une `KeyError` si la clé n'existe pas, renvoie `default_value` à la place.
*   `dict.values()` : Renvoie un objet de vue qui affiche une liste de toutes les valeurs du dictionnaire.
*   `dict.items()` : Renvoie un objet de vue qui affiche une liste des paires (clé, valeur) du dictionnaire sous forme de tuples.

---

Ceci ne fait qu'effleurer la surface, mais ces exemples couvrent de nombreux concepts fondamentaux de Python que vous utiliserez fréquemment !
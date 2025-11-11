---
audio: false
generated: true
lang: fr
layout: post
title: Guide Python
translated: true
type: note
---

Voici un guide concis Python couvrant les opérations sur les chaînes, les mathématiques, le traitement de texte, les E/S, la gestion des fichiers, la mise en réseau, les collections et le multithreading. Chaque section comprend un bref aperçu et des exemples pratiques pour vous aider à démarrer ou à rafraîchir vos connaissances.

---

## Guide Python : Thèmes Essentiels

### 1. Opérations sur les Chaînes
Les chaînes en Python sont des séquences immuables de caractères. Vous pouvez effectuer des opérations comme la concaténation, la répétition, le découpage et utiliser des méthodes intégrées pour la manipulation.

**Exemples :**
```python
# Concaténation et répétition
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)  # Sortie : Hello World
print(s1 * 3)         # Sortie : HelloHelloHello

# Découpage
print(s1[1:4])        # Sortie : ell

# Méthodes intégrées
print(s1.upper())     # Sortie : HELLO
print(s2.lower())     # Sortie : world
print("  hi  ".strip())  # Sortie : hi
print("a,b,c".split(','))  # Sortie : ['a', 'b', 'c']
print(','.join(['a', 'b', 'c']))  # Sortie : a,b,c

# Formatage de chaîne avec les f-strings
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")  # Sortie : My name is Alice and I am 30 years old.
```

---

### 2. Mathématiques
Le module `math` fournit des fonctions mathématiques et des constantes pour les calculs courants.

**Exemple :**
```python
import math

print(math.sqrt(16))    # Sortie : 4.0
print(math.pow(2, 3))   # Sortie : 8.0
print(math.sin(math.pi / 2))  # Sortie : 1.0
print(math.pi)          # Sortie : 3.141592653589793
```

---

### 3. Traitement de Texte (Expressions Régulières)
Le module `re` permet la recherche de motifs et la manipulation de texte en utilisant des expressions régulières.

**Exemple :**
```python
import re

text = "The rain in Spain"
match = re.search(r"rain", text)
if match:
    print("Found:", match.group())  # Sortie : Found: rain

# Trouver tous les mots de 4 lettres
print(re.findall(r"\b\w{4}\b", text))  # Sortie : ['rain', 'Spain']
```

---

### 4. E/S (Entrée et Sortie)
Les opérations d'entrée et de sortie de base permettent l'interaction avec l'utilisateur.

**Exemple :**
```python
name = input("Entrez votre nom : ")
print("Hello, " + name + "!")
```

---

### 5. Gestion des Fichiers
Python simplifie la lecture et l'écriture dans les fichiers en utilisant la fonction `open()`, avec la déclaration `with` recommandée pour la fermeture automatique des fichiers.

**Exemple :**
```python
# Écrire dans un fichier
with open("example.txt", "w") as f:
    f.write("Hello, World!\n")

# Lire depuis un fichier
with open("example.txt", "r") as f:
    content = f.read()
    print(content)  # Sortie : Hello, World!
```

---

### 6. Mise en Réseau
La bibliothèque `requests` (à installer avec `pip install requests`) simplifie les requêtes HTTP.

**Exemple :**
```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)  # Sortie : 200
print(response.json())       # Sortie : Données JSON de l'API GitHub
```

---

### 7. Collections
Le module `collections` offre des structures de données spécialisées comme `Counter`, `deque`, `namedtuple`, etc. Voici un exemple avec `Counter`.

**Exemple :**
```python
from collections import Counter

words = ["apple", "banana", "apple", "cherry"]
word_count = Counter(words)
print(word_count)  # Sortie : Counter({'apple': 2, 'banana': 1, 'cherry': 1})
```

**Autres Collections :**
- `namedtuple` : Crée des sous-classes de tuple avec des champs nommés.
- `deque` : File doublement chaînée pour des ajouts/suppressions efficaces aux deux extrémités.
- `OrderedDict` : Dictionnaire qui mémorise l'ordre d'insertion.
- `defaultdict` : Dictionnaire avec une valeur par défaut pour les clés manquantes.

---

### 8. Multithreading
Le module `threading` permet l'exécution concurrente de tâches, idéal pour les opérations liées aux E/S.

**Exemple :**
```python
import threading
import time

def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)

# Créer et démarrer un thread
t = threading.Thread(target=print_numbers)
t.start()

# Le thread principal continue
print("Main thread finished")
```

---

Ce guide fournit un point de départ pour chaque thème avec des exemples pratiques. Pour un apprentissage plus approfondi, consultez la documentation officielle de Python ou des ressources spécialisées. Bon codage !
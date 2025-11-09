---
audio: false
date: 2025-09-10
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Utiliser l'Option -m de Python pour les Modules
translated: true
type: note
---

Oui, `-m` signifie **exécuter un module comme un script**. Décomposons cela avec vos exemples :

### `python -m unittest`

Cela indique à Python :

* De rechercher le module `unittest` (qui fait partie de la bibliothèque standard).
* De l'exécuter comme s'il s'agissait d'un script (c'est ce que fait `-m`).
* C'est pourquoi vous pouvez faire des choses comme :

  ```bash
  python -m unittest test_example.py
  python -m unittest discover
  ```

  Cela fonctionne même si vous n'avez pas de fichier `unittest` autonome dans votre projet — c'est un module de la bibliothèque standard.

### `python -m pip`

C'est le même principe :

* Il recherche le module `pip` (installé avec Python).
* L'exécute comme s'il s'agissait de l'exécutable `pip`.
* Ainsi, `python -m pip install requests` est la manière "officielle" et sûre d'exécuter pip, car cela garantit que vous utilisez le pip de l'interpréteur Python qui correspond à votre commande `python`.
  (Parfois, `pip` sur votre système peut pointer vers une installation Python différente, donc `python -m pip` évite toute confusion.)

### Différence avec `python test_xx.py`

Lorsque vous faites :

```bash
python test_xx.py
```

vous exécutez ce fichier spécifique directement, sans utiliser la découverte de tests ou le lanceur de `unittest`.

* Si `test_xx.py` a un `unittest.main()` à la fin, il exécutera les tests.
* Mais si vous voulez que Python découvre automatiquement tous les tests dans un répertoire, vous utilisez généralement `python -m unittest discover`.

---

✅ **Résumé** :

* `-m` = exécuter un module comme un script.
* `python -m unittest` exécute le lanceur de tests de la bibliothèque standard.
* `python -m pip` garantit que pip correspond au même interpréteur Python.
* `python test_xx.py` exécute simplement un fichier, pas le lanceur de tests général.

Souhaitez-vous que je vous montre également comment **pytest** gère cela différemment, puisque vous pourriez comparer `unittest` vs `pytest` ?
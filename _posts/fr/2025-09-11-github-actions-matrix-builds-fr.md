---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Guide des Matrices de Compilation GitHub Actions
translated: true
type: note
---

On dirait que vous vous interrogez sur l'utilisation des builds de **matrice GitHub Actions** pour exécuter des tests en parallèle, et sur la façon d'utiliser l'option `fail-fast` dans une stratégie de matrice. Laissez-moi vous l'expliquer en détail.

---

### Matrices de builds dans GitHub Actions
La **stratégie de matrice** vous permet d'exécuter la même tâche en parallèle avec différents paramètres—par exemple, pour tester sur plusieurs versions de Python ou de Node, ou sur différents systèmes d'exploitation.

Un exemple minimal :

```yaml
name: CI

on:
  push:
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, 3.10]
        os: [ubuntu-latest, windows-latest]
      fail-fast: false
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest
```

---

### Points Clés

- **`matrix`:** Définit les variables pour créer des combinaisons de jobs.  
  L'exemple ci-dessus exécute les tests pour toutes les combinaisons de (`python-version`, `os`).

- **Exécution parallèle :** Chaque job généré par la matrice s'exécute **en parallèle** par défaut.

- **`fail-fast` :**
  - La valeur par défaut est `true`. Cela signifie que si un job échoue, les autres jobs de la matrice sont annulés.
  - Définissez `fail-fast: false` si vous voulez que tous les jobs de la matrice continuent de s'exécuter, même si l'un d'eux échoue.

  Exemple :
  ```yaml
  strategy:
    matrix:
      node: [14, 16, 18]
    fail-fast: false
  ```

- **Limiter le nombre total de jobs :** Vous pouvez exclure certaines combinaisons :
  ```yaml
  strategy:
    matrix:
      python-version: [3.8, 3.9, 3.10]
      os: [ubuntu-latest, windows-latest]
    exclude:
      - python-version: 3.8
        os: windows-latest
  ```

---

### Exécution des tests en parallèle
- Chaque **job de la matrice s'exécute en parallèle** sur son propre runner, vous n'avez donc rien de spécial à faire.
- À l'intérieur de chaque job, si vous souhaitez une **exécution de tests parallèle** (par exemple, l'option `-n auto` de pytest), vous pouvez l'ajouter au niveau de la commande de test.

Exemple :
```yaml
- name: Run pytest in parallel
  run: pytest -n auto
```

---

✅ **Résumé :**
- Utilisez `strategy.matrix` pour définir différentes combinaisons de paramètres.
- Définissez `fail-fast: false` si vous voulez que tous les jobs de la matrice s'exécutent même si l'un échoue.
- Les jobs de la matrice s'exécutent en parallèle automatiquement.
- Pour un temps d'exécution plus rapide à l'intérieur de chaque job, utilisez la parallélisation du framework de test (par exemple pytest-xdist).

---

Souhaitez-vous que je vous montre un exemple réel pour **exécuter des tests Node/JavaScript** avec une matrice (plusieurs versions de Node, `fail-fast: false`, tests parallélisés avec `npm test`) ?
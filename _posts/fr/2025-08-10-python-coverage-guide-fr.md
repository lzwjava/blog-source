---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Guide Essentiel de la Couverture du Code Python
translated: true
type: note
---

Voici une introduction pratique et axée développement au package **coverage** (coverage.py) : ce qu'il mesure, comment bien l'utiliser et les réglages qui vous importeront vraiment.

# Qu'est-ce que coverage.py

* Un outil Python qui **mesure quelles lignes et branches de votre code s'exécutent** pendant les tests ou toute exécution.
* Génère des rapports en **texte, HTML, XML et JSON** pour que vous puissiez voir les lacunes et l'intégrer dans les portes de qualité d'intégration continue.
* Fonctionne avec unittest, pytest, nose ou de simples scripts.

# Concepts fondamentaux (en termes simples)

* **Couverture de lignes** : Est-ce qu'une ligne s'est exécutée au moins une fois ?
* **Couverture de branches** : Est-ce que chaque branche possible d'une décision s'est exécutée ? (if/else, court-circuit booléen, exceptions, compréhensions, etc.)
* **Sélection de la source** : Ne mesurez que votre propre code pour éviter le bruit de venv/site-packages.
* **Stockage des données** : Les exécutions créent un fichier de données `.coverage` (SQLite) ; vous pouvez fusionner plusieurs exécutions.
* **Contextes** : Étiquetez l'exécution avec des labels (par exemple, par test), afin de pouvoir segmenter les rapports par noms de tests, commandes, etc.

# Démarrage rapide

```bash
# 1) Installer
pip install coverage

# 2) Exécutez vos tests sous coverage (pytest n'est qu'un exemple)
coverage run -m pytest

# 3) Voyez un rapport terminal (avec les numéros des lignes manquantes)
coverage report -m

# 4) Générez le HTML (ouvrez htmlcov/index.html dans un navigateur)
coverage html

# Optionnel : rapports lisibles par machine
coverage xml        # pour les outils d'IC comme Sonar, Jenkins, Azure DevOps
coverage json       # analyse scriptée
```

# .coveragerc recommandé

Créez une configuration à la racine de votre dépôt pour uniformiser les résultats localement et en IC.

```ini
[run]
# Ne mesurez que vos packages pour réduire le bruit
source = src, your_package
branch = True
parallel = True                 # permet à plusieurs processus/exécutions d'écrire leurs propres données
relative_files = True           # chemins plus propres dans les rapports (compatible IC)
concurrency = thread, multiprocessing

# Vous pouvez aussi exclure complètement des fichiers ou motifs
omit =
    */tests/*
    */.venv/*
    */site-packages/*
    */migrations/*

[report]
show_missing = True
skip_covered = False            # mettez True si vous voulez un rapport plus court
fail_under = 90                 # fait échouer l'IC si la couverture est inférieure à 90 %
exclude_lines =
    pragma: no cover            # pragma standard pour ignorer des lignes
    if TYPE_CHECKING:
    raise NotImplementedError

[html]
directory = htmlcov
title = Coverage Report

[xml]
output = coverage.xml

[json]
output = coverage.json

[paths]
# Utile pour combiner des données de différentes machines/conteneurs
source =
    src
    */workspace/src
    */checkouts/your_repo/src
```

# Mesurer les sous-processus et les exécutions parallèles

Si votre code lance des sous-processus (multiprocessing, outils CLI), configurez la **couverture des sous-processus** :

1. Dans `[run]`, gardez `parallel = True`.
2. Exportez une variable d'environnement pour que les sous-processus démarrent automatiquement coverage avec la même configuration :

```bash
export COVERAGE_PROCESS_START=$(pwd)/.coveragerc
```

3. Exécutez votre programme/tests normalement (ou toujours via `coverage run -m ...`).
4. Une fois toutes les exécutions terminées, fusionnez les données et générez le rapport :

```bash
coverage combine
coverage report -m
```

> Astuce : `concurrency = multiprocessing, thread, gevent, eventlet, greenlet` permet à coverage de s'accrocher à différents modèles asynchrones.

# Couverture de branches et pragmas

* Activez `branch = True` dans `[run]`. Cela détecte les branches `else` manquées, les courts-circuits, les chemins d'exception, etc.
* Ignorez les lignes non testables avec un commentaire de fin de ligne :

  * `# pragma: no cover` — exclut cette ligne de la couverture.
  * Pour les branches délicates, refactorisez plutôt que de surutiliser les pragmas.

# Contextes (segmentez la couverture par test ou tâche)

Les contextes attachent des labels aux lignes exécutées pour que vous puissiez répondre à : « Quels tests couvrent ce code ? »

* Le plus simple avec pytest :

  * Dans `.coveragerc` ajoutez `dynamic_context = test_function`.
  * Puis `coverage html --show-contexts` ou inspectez les données par contexte pour voir quel test a touché une ligne.
* Vous pouvez aussi définir `dynamic_context = test` (test nodeid) ou `dynacontext` via une variable d'environnement dans des lanceurs personnalisés.

# Intégration avec Pytest

Deux modèles courants :

**A. CLI coverage native (simple et rapide)**

```bash
coverage run -m pytest -q
coverage report -m
```

**B. Plugin pytest-cov (ajoute du sucre syntaxique en CLI)**

```bash
pip install pytest-cov
pytest --cov=your_package --cov-branch --cov-report=term-missing --cov-report=html
```

Les deux utilisent coverage.py en arrière-plan ; utilisez celui qui correspond aux conventions de votre équipe.

# Câblage typique en IC (ébauche GitHub Actions)

```yaml
- name: Installer
  run: pip install -U pip coverage pytest

- name: Tester avec coverage
  run: |
    coverage run -m pytest -q
    coverage report -m
    coverage xml
- name: Appliquer le seuil
  run: coverage report --fail-under=90
- name: Téléverser le HTML
  if: always()
  uses: actions/upload-artifact@v4
  with:
    name: htmlcov
    path: htmlcov/
```

# Pièges courants et correctifs

* **Rapports énormes/lents** : Restreignez `source=` et utilisez `omit=` pour ignorer venv, tests, code généré.
* **Chemins différents en IC vs local** : Ajoutez une section `[paths]` pour que `coverage combine` fusionne les jeux de données.
* **Sous-processus non mesurés** : Définissez `COVERAGE_PROCESS_START` et gardez `parallel = True`, puis `coverage combine`.
* **Frameworks async** : Ajoutez l'entrée pertinente à `concurrency = ...`.
* **Extensions C** : coverage.py mesure le Python, pas le code natif — écrivez des tests de harness autour de la frontière Python.
* **Faux négatifs sur le code inaccessible** : Marquez avec `# pragma: no cover`, mais envisagez une refactorisation pour rendre le comportement testable.

# Commandes utiles que vous utiliserez vraiment

```bash
coverage erase                       # nettoie les données précédentes
coverage run -m pytest               # collecte
coverage report -m                   # résumé texte avec les lignes manquantes
coverage html                        # ouvre htmlcov/index.html
coverage xml                         # analyseurs d'IC
coverage json                        # scripts/automatisation
coverage combine                     # fusionne les données parallèles/sous-processus
coverage annotate                    # par ligne .py, montrant quelles lignes ont été exécutées
```

# Quand arrêter de régler

Visez un **seuil significatif** (par exemple, 80–95 %), appliquez-le avec `fail_under`, et concentrez les revues sur la **couverture des diffs** (les lignes nouvelles/modifiées sont-elles testées ?). Ne cherchez pas à atteindre 100 % sur du code difficile à exercer (feature flags, gardes défensives) — utilisez les pragmas avec parcimonie et privilégiez une conception plus simple et testable.
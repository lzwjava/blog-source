---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Guide du Formateur de Code Python Black
translated: true
type: note
---

Black est un formateur de code Python partial et intransigeant développé par la Python Software Foundation (PSF). Il reformate automatiquement le code Python pour qu'il respecte un style cohérent, principalement basé sur un sous-ensemble strict de PEP 8, tout en mettant l'accent sur la lisibilité, la cohérence et la minimisation des diffs dans le contrôle de version. En utilisant Black, les développeurs acceptent de renoncer au contrôle des détails de formatage mineurs en échange de la vitesse, du déterminisme et de la réduction des débats sur le style pendant les revues de code. Black garantit que le code formaté ("noirci") ait un aspect uniforme d'un projet à l'autre, ce qui permet d'économiser du temps et de l'énergie mentale pour des aspects plus critiques du développement. Il prend en charge Python 3.8 et versions ultérieures, la dernière version stable étant la 25.1.0 (publiée le 29 janvier 2025), qui introduit le style stable 2025 avec des améliorations comme la normalisation de la casse des séquences d'échappement Unicode et une meilleure gestion des virgules finales.

La philosophie de Black privilégie :
- **Cohérence** : Les constructions similaires sont formatées de manière identique.
- **Généralité** : Les règles s'appliquent largement sans cas particuliers.
- **Lisibilité** : Se concentre sur un code facile à lire.
- **Minimisation des Diffs** : Réduit les changements dans les diffs Git pour accélérer les revues.

Il est largement utilisé dans les projets open source et professionnels pour sa fiabilité et ses capacités d'intégration.

## Installation

Black est disponible sur PyPI et peut être installé en utilisant pip. Il est recommandé de l'installer dans un environnement virtuel pour isoler le projet.

- Installation de base :
  ```
  pip install black
  ```

- Pour des fonctionnalités supplémentaires comme la prise en charge de Jupyter Notebook ou les diffs colorés :
  ```
  pip install 'black[jupyter,colorama]'
  ```
  (L'extra `d` est pour blackd, un démon pour les intégrations d'éditeur.)

Sur Arch Linux, vous pouvez l'installer via le gestionnaire de paquets : `pacman -S python-black`.

Black peut également être installé via conda ou d'autres gestionnaires de paquets. Après l'installation, vérifiez avec `black --version`.

Pour le développement ou les tests, vous pouvez cloner le dépôt GitHub et l'installer en mode modifiable :
```
git clone https://github.com/psf/black.git
cd black
pip install -e .
```

## Utilisation

Black est principalement un outil en ligne de commande. La commande de base formate les fichiers ou répertoires sur place :

```
black {fichier_ou_répertoire_source}
```

Si l'exécution de Black en tant que script ne fonctionne pas (par exemple, à cause de problèmes d'environnement), utilisez :
```
python -m black {fichier_ou_répertoire_source}
```

### Options principales en ligne de commande

Black offre divers drapeaux pour la personnalisation et le contrôle. Voici un résumé des principaux :

- `-h, --help` : Afficher l'aide et quitter.
- `-c, --code <code>` : Formater une chaîne de code (par exemple, `black --code "print ( 'hello, world' )"` affiche la version formatée).
- `-l, --line-length <int>` : Définir la longueur de ligne (par défaut : 88).
- `-t, --target-version <version>` : Spécifier les versions Python pour la compatibilité (par exemple, `py38`, peut en spécifier plusieurs comme `-t py311 -t py312`).
- `--pyi` : Traiter les fichiers comme des stubs de typage (style `.pyi`).
- `--ipynb` : Traiter les fichiers comme des Jupyter Notebooks.
- `--python-cell-magics <magic>` : Reconnaître les magies Jupyter personnalisées.
- `-x, --skip-source-first-line` : Ignorer le formatage de la première ligne (utile pour les shebangs).
- `-S, --skip-string-normalization` : Ne pas normaliser les chaînes en guillemets doubles ou les préfixes.
- `-C, --skip-magic-trailing-comma` : Ignorer les virgules finales pour les sauts de ligne.
- `--preview` : Activer les changements de style expérimentaux pour la prochaine version.
- `--unstable` : Activer tous les changements d'aperçu plus les fonctionnalités instables (nécessite `--preview`).
- `--enable-unstable-feature <feature>` : Activer des fonctionnalités instables spécifiques.
- `--check` : Vérifier si les fichiers ont besoin d'être reformatés sans les modifier (code de sortie 1 si des changements sont nécessaires).
- `--diff` : Afficher un diff des changements sans écrire dans les fichiers.
- `--color / --no-color` : Coloriser la sortie du diff.
- `--line-ranges <ranges>` : Formater des plages de lignes spécifiques (par exemple, `--line-ranges=1-10`).
- `--fast / --safe` : Ignorer (`--fast`) ou forcer (`--safe`) les vérifications de sécurité AST (par défaut : safe).
- `--required-version <version>` : Exiger une version spécifique de Black.
- `--exclude <regex>` : Exclure les fichiers/répertoires via une regex.
- `--extend-exclude <regex>` : Ajouter aux exclusions par défaut.
- `--force-exclude <regex>` : Exclure même si passé explicitement.
- `--include <regex>` : Inclure les fichiers/répertoires via une regex.
- `-W, --workers <int>` : Définir le nombre de workers parallèles (par défaut : nombre de CPU).
- `-q, --quiet` : Supprimer les messages non-erreurs.
- `-v, --verbose` : Afficher une sortie détaillée.
- `--version` : Afficher la version de Black.
- `--config <file>` : Charger la configuration depuis un fichier.

### Exemples

- Formater un seul fichier : `black example.py`
- Vérifier sans formater : `black --check .`
- Afficher le diff : `black --diff example.py`
- Formater l'entrée standard : `echo "print('hello')" | black -`
- Formater avec une longueur de ligne personnalisée : `black -l 79 example.py`
- Formater un Jupyter Notebook : `black notebook.ipynb`

### Conseils et Notes

- Black formate les fichiers entiers ; utilisez `# fmt: off` / `# fmt: on` pour ignorer des blocs ou `# fmt: skip` pour des lignes.
- Pour l'entrée standard, utilisez `--stdin-filename` pour respecter les exclusions.
- Black est déterministe : la même entrée produit toujours la même sortie.
- Utilisez `--preview` pour tester les styles à venir, mais notez qu'ils peuvent changer.

## Configuration

Black peut être configuré via des drapeaux en ligne de commande ou un fichier `pyproject.toml` (préféré pour les projets). La configuration dans `pyproject.toml` se place dans une section `[tool.black]`.

### Utilisation de pyproject.toml

Exemple :
```
[tool.black]
line-length = 79
target-version = ['py311']
include = '\.pyi?$'
exclude = '''
/(
    \.git
  | \.hg
  | \.mypy_cache
  | \.tox
  | \.venv
  | _build
  | buck-out
  | build
  | dist
)/
'''
skip-string-normalization = true
```

Les options prises en charge reflètent les drapeaux CLI (par exemple, `line-length`, `skip-string-normalization`). Les options multi-valeurs comme `target-version` utilisent des tableaux.

### Priorité

- Les drapeaux en ligne de commande écrasent les paramètres du fichier de configuration.
- Si aucun `pyproject.toml` n'est trouvé, Black utilise les paramètres par défaut et recherche dans les répertoires parents.
- Utilisez `--config` pour spécifier un fichier de configuration personnalisé.

### Découverte et Ignorance de Fichiers

Black découvre automatiquement les fichiers Python dans les répertoires, en respectant `.gitignore` par défaut. Utilisez `--include`/`--exclude` pour personnaliser. Il ignore les répertoires communs comme `.git`, `.venv`, etc., sauf indication contraire.

Pour le contrôle de version, intégrez avec des outils comme pre-commit pour imposer le formatage.

## Le Style de Code Black

Black impose un style spécifique avec une configurabilité limitée. Règles clés :

### Longueur de Ligne
- Par défaut : 88 caractères. Peut dépasser si incassable (par exemple, longues chaînes).

### Chaînes de Caractères
- Préfère les guillemets doubles ; normalise les préfixes en minuscules (par exemple, `r` avant `f`).
- Met en minuscules les séquences d'échappement (sauf les noms `\N`).
- Traite les docstrings : corrige l'indentation, supprime les espaces supplémentaires/sauts de ligne, préserve les tabulations dans le texte.

### Littéraux Numériques
- Parties syntaxiques en minuscules (par exemple, `0xAB`), chiffres en majuscules.

### Sauts de Ligne et Opérateurs
- Sauts de ligne avant les opérateurs binaires.
- Espaces simples autour de la plupart des opérateurs ; pas d'espaces pour les opérateurs unaires/puissance avec des opérandes simples.

### Virgules Finales
- Les ajoute aux collections multi-lignes/arguments de fonction (si Python 3.6+).
- La virgule finale "magique" explose les listes si elle est présente.

### Commentaires
- Deux espaces avant les commentaires en ligne ; un espace avant le texte.
- Préserve l'espacement spécial pour les shebangs, les commentaires de doc, etc.

### Indentation
- 4 espaces ; correspond aux crochets avec des fermetures désindentées.

### Lignes Vides
- Espace blanc minimal : simple dans les fonctions, double au niveau du module.
- Règles spécifiques pour les docstrings, les classes et les fonctions.

### Imports
- Sépare les imports longs ; compatible avec le profil `black` d'isort.

### Autres Règles
- Préfère les parenthèses aux barres obliques inverses.
- Normalise les fins de ligne en fonction du fichier.
- Style concis pour les fichiers `.pyi` (par exemple, pas de lignes supplémentaires entre les méthodes).
- Réduit les lignes vides après les imports en mode aperçu.

Black vise à réduire les diffs et à améliorer la lisibilité, avec des changements principalement pour les corrections de bogues ou la prise en charge de nouvelles syntaxes.

## Intégrations

Black s'intègre parfaitement avec les éditeurs et le contrôle de version pour un formatage automatisé.

### Éditeurs

- **VS Code** : Utilisez l'extension Python avec Black comme formateur. Définissez `"python.formatting.provider": "black"` dans settings.json. Pour LSP, installez python-lsp-server et python-lsp-black.
- **PyCharm/IntelliJ** :
  - Intégré (2023.2+) : Paramètres > Outils > Black, configurez le chemin.
  - Outil Externe : Paramètres > Outils > Outils externes, ajoutez Black avec l'argument `$FilePath$`.
  - File Watcher : Pour le formatage automatique à l'enregistrement.
  - Plugin BlackConnect pour le formatage basé sur le démon.
- **Vim** : Utilisez le plugin officiel (via vim-plug : `Plug 'psf/black', { 'branch': 'stable' }`). Commandes : `:Black` pour formater. Auto-enregistrement : Ajoutez autocmd au vimrc. Variables de config comme `g:black_linelength`.
- **Emacs** : Utilisez reformatter.el ou le package python-black pour le formatage à l'enregistrement.
- **Autres** : Prend en charge Sublime Text, JupyterLab, Spyder, etc., via des plugins ou des extensions.

### Contrôle de Version

- **Hooks Pre-commit** : Ajoutez à `.pre-commit-config.yaml` :
  ```
  repos:
    - repo: https://github.com/psf/black-pre-commit-mirror
      rev: 25.1.0
      hooks:
        - id: black
          language_version: python3.11
  ```
  Pour Jupyter : Utilisez `id: black-jupyter`.
- **GitHub Actions** : Utilisez des actions comme `psf/black-action` dans les workflows pour les vérifications CI.
- **Git** : Exécutez Black dans des scripts pre-commit ou husky pour l'application.

## Sujets Avancés

- **Styles Aperçu et Instables** : Utilisez `--preview` pour les changements futurs (par exemple, meilleure gestion des parenthèses). `--unstable` pour les fonctionnalités expérimentales.
- **Blackd** : Serveur HTTP pour les intégrations (`blackd --bind-host 127.0.0.1 --bind-port 45484`).
- **Prise en charge de Jupyter** : Formate les notebooks, en préservant les magies.
- **Stubs de Typage** : Formatage spécial concis pour les fichiers `.pyi`.
- **Compatibilité** : Cible Python 3.8+ ; utilisez `--target-version` pour le code plus ancien.
- **Alternatives** : Comparé à autopep8 (plus flexible mais moins partial) ou Ruff (plus rapide, inclut le linting).

Pour le dépannage, consultez la FAQ de la documentation officielle ou les issues GitHub.

## Références

- [Documentation Black 25.1.0](https://black.readthedocs.io/en/stable/)
- [Dépôt GitHub psf/black](https://github.com/psf/black)
- [Le Style de Code Black](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html)
- [Utilisation et Configuration](https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html)
- [Intégrations d'Éditeurs](https://black.readthedocs.io/en/stable/integrations/editors.html)
- [Intégration du Contrôle de Version](https://black.readthedocs.io/en/stable/integrations/source_version_control.html)
- [Python Code Formatting Using Black - GeeksforGeeks](https://www.geeksforgeeks.org/python/python-code-formatting-using-black/)
- [How to Auto-Format Your Python Code with Black - freeCodeCamp](https://www.freecodecamp.org/news/auto-format-your-python-code-with-black/)
- [Black - PyPI](https://pypi.org/project/black/)
- [Introduction to Python Black Module - GeeksforGeeks](https://www.geeksforgeeks.org/introduction-to-python-black-module/)
- [Python Auto Formatter: Autopep8 vs. Black - Built In](https://builtin.com/data-science/autopep8-vs-black)
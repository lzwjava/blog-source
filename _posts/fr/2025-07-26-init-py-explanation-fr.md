---
audio: false
generated: true
lang: fr
layout: post
title: Pourquoi Python a besoin de `__init__.py`
translated: true
type: note
---

### Correction de la faute de frappe
Il semble que vous vouliez dire `__init__.py` (où "init" est l'abréviation de "initialization") plutôt que `__int__.py`. Si ce n'est pas le cas, n'hésitez pas à clarifier ! En supposant qu'il s'agit bien de `__init__.py`, voici l'explication.

### Pourquoi Python a besoin de `__init__.py` dans un répertoire
En Python, un répertoire n'est pas automatiquement traité comme un module ou un package simplement parce qu'il contient des fichiers Python. Pour organiser le code en packages réutilisables (qui sont essentiellement des répertoires de modules associés), Python nécessite un fichier `__init__.py` dans ce répertoire. Voici pourquoi :

- **Marquer le répertoire comme un package** : La présence de `__init__.py` indique à Python que le répertoire doit être considéré comme un package. Cela vous permet d'importer des modules depuis celui-ci en utilisant la notation pointée, comme `import monpackage.monmodule`. Sans ce fichier (dans les cas standard), Python traiterait le répertoire comme un dossier ordinaire et n'autoriserait pas les imports depuis celui-ci.

- **Éviter les conflits de noms** : Cela empêche la dissimulation accidentelle de modules. Par exemple, si vous avez un répertoire nommé `string` (un nom courant), sans `__init__.py`, il pourrait masquer involontairement le module `string` intégré de Python dans le chemin d'import.

- **Initialisation et personnalisation** : Le fichier peut être vide (ce qui est courant pour les packages simples), mais il peut également contenir du code qui s'exécute lors de l'import du package. Ceci est utile pour les tâches de configuration, comme l'import automatique de sous-modules. De plus, vous pouvez définir une variable spéciale appelée `__all__` dans `__init__.py` pour contrôler ce qui est importé lorsque quelqu'un utilise `from monpackage import *` (par exemple, `__all__ = ['module1', 'module2']`).

### Contexte historique et spécifique aux versions
- Cette exigence fait partie de Python depuis ses débuts pour garder le système de modules explicite et organisé.
- À partir de Python 3.3, les "namespace packages" (packages d'espace de noms) ont été introduits ; ils ne nécessitent pas de `__init__.py`. Ils permettent aux packages d'être répartis sur plusieurs répertoires (par exemple, à des fins de distribution) sans ce fichier, en utilisant des outils comme `pkgutil` ou `importlib`. Cependant, cela est considéré comme une fonctionnalité avancée, et pour la plupart des cas d'utilisation quotidiens, `__init__.py` est toujours recommandé et largement utilisé pour les packages réguliers.

Si vous travaillez avec Python 3.3 ou supérieur, vous pouvez expérimenter avec les namespace packages, mais rester avec `__init__.py` est plus simple et plus direct pour les débutants.

[Tutoriel Python : Modules](https://docs.python.org/3/tutorial/modules.html#packages)
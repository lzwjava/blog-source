---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Corriger les chemins d'importation des modules Python
translated: true
type: note
---

La réponse courte : vous avez besoin de `sys` ici pour pouvoir modifier le chemin de recherche des modules Python (`sys.path`) avant de faire `from scripts.create.delete import delete_md`.

---

### Pourquoi `sys` est nécessaire

* Python cherche les modules/paquets à importer dans une liste de répertoires stockée dans `sys.path`.
* Par défaut, il contient :

  * Le répertoire du script actuel.
  * Les répertoires de la bibliothèque standard.
  * Les site-packages installés.
* Si votre fichier `scripts/create/delete.py` ne se trouve pas dans l'un de ces emplacements par défaut, l'importation échouera avec `ModuleNotFoundError`.

Donc le code fait :

```python
sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)
```

Ce qui signifie :

* Prendre le chemin absolu du fichier actuel (`__file__`).
* Remonter de trois répertoires.
* Ajouter ce répertoire à `sys.path`.

Après cela, Python peut résoudre `scripts.create.delete` comme s'il était installé ou dans la racine du projet.

---

### Sans `sys`

Si votre projet est structuré comme :

```
project/
├── scripts/
│   └── create/
│       └── delete.py
└── tools/
    └── myscript.py   <-- vous exécutez celui-ci
```

et que vous exécutez `myscript.py` directement, Python ne saura pas automatiquement que `project/` est la racine. L'importation échouera à moins que vous ne :

* L'exécutiez avec `PYTHONPATH=...` (par exemple, `PYTHONPATH=.. python myscript.py`), ou
* Empaquetiez le projet et l'installiez (`pip install -e .`), ou
* Ajoutiez dynamiquement le chemin dans le code avec `sys.path.append(...)` (comme fait ici).

---

👉 Donc `sys` est nécessaire uniquement pour **manipuler le chemin d'importation à l'exécution**, vous permettant d'importer des modules relatifs à la racine de votre projet.

Voulez-vous que je vous montre aussi **des alternatives plus propres** pour éviter de manipuler manuellement `sys.path` ?
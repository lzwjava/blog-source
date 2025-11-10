---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Guide du Formateur de Code Python Noir
translated: true
type: note
---

Le package `black` sur PyPI est un **formateur de code Python**. Il reformate automatiquement votre code Python pour qu'il suive des règles de style cohérentes (compatible avec PEP 8, mais avec ses propres opinions strictes). Voici comment l'utiliser :

---

### 1. Installer Black

```bash
pip install black
```

Si vous voulez vous assurer d'obtenir toujours la dernière version stable :

```bash
pip install -U black
```

---

### 2. Formater un Fichier ou un Répertoire

Exécutez Black sur un fichier :

```bash
black my_script.py
```

Exécutez Black sur un répertoire entier (récursivement) :

```bash
black src/
```

Par défaut, il remplacera les fichiers sur place avec le code formaté.

---

### 3. Vérifier le Formatage Sans Modifier

Utilisez `--check` pour voir si vos fichiers ont besoin d'être reformatés :

```bash
black --check my_script.py
```

Ceci est utile pour les pipelines d'intégration continue (CI), pour garantir la cohérence de style.

---

### 4. Options Courantes

* `--line-length 88` → Modifier la longueur de ligne (par défaut : 88).
* `--diff` → Montrer ce qui changerait, sans modifier le fichier.
* `--skip-string-normalization` → Ne pas changer les guillemets des chaînes de caractères.
* `--exclude` → Ignorer certains fichiers/dossiers.

Exemple :

```bash
black --line-length 100 --diff src/
```

---

### 5. Intégration

* **Support IDE** : Black est disponible en tant que plugin dans PyCharm, VS Code, Vim, Emacs, etc.
* **Hook Pre-commit** : Ajoutez Black à `.pre-commit-config.yaml` pour que le code soit formaté avant les commits :

  ```yaml
  repos:
    - repo: https://github.com/psf/black
      rev: stable
      hooks:
        - id: black
  ```
* **CI/CD** : Ajoutez `black --check .` dans votre pipeline d'intégration continue.

---

👉 Souhaitez-vous que je montre également comment configurer **le formatage automatique dans VSCode ou PyCharm**, pour que vous n'ayez pas à exécuter `black` manuellement ?
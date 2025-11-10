---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Résoudre un Problème d'Incompatibilité de Version Python
translated: true
type: note
---

Compris — vous rencontrez un problème de **version Python incompatible**.

Vos logs indiquent :

* `python3` → **3.10.12**
* `python` → **3.13.7**

Ainsi, lorsque Claude Code (ou votre script d'agent de recherche) invoque `python3`, il utilise la version 3.10, qui n'a pas `pyperclip` installé. Vous avez installé `pyperclip` dans l'environnement de la version 3.13, donc la 3.10 ne peut pas le voir.

Voici quelques solutions :

---

### 1. Exécuter Claude Code avec la version Python souhaitée

Si vous voulez que Claude Code utilise toujours Python 3.13, définissez explicitement l'exécutable dans votre shell :

```bash
export PYTHON_EXECUTABLE=$(which python)
```

Ou si vous voulez spécifiquement `python3` :

```bash
export PYTHON_EXECUTABLE=$(which python3)
```

Ensuite, au démarrage de Claude Code ou de votre agent, il pourra lire cette variable d'environnement.

---

### 2. Faire pointer `python3` vers Python 3.13

Sur Ubuntu, vous pouvez mettre à jour le système `alternatives` :

```bash
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.13 2
sudo update-alternatives --config python3
```

Puis choisissez Python 3.13.

---

### 3. Installer `pyperclip` dans Python 3.10

Si vous souhaitez continuer à utiliser la 3.10 pour `python3`, installez simplement le module dedans :

```bash
python3 -m pip install --user pyperclip
```

Cela garantit que `python3` pourra l'importer.

---

### 4. Utiliser un environnement virtuel

Meilleure pratique : créez un venv avec la version Python souhaitée et exécutez Claude Code à l'intérieur :

```bash
python3.13 -m venv ~/.venvs/claude
source ~/.venvs/claude/bin/activate
pip install pyperclip
```

Ensuite, lancez votre agent dans cet environnement virtuel, afin qu'il utilise toujours la version 3.13.

---

👉 Question pour vous : souhaitez-vous que Claude Code **s'exécute toujours avec Python 3.13**, ou préférez-vous conserver la 3.10 comme `python3` et simplement corriger le module manquant ?
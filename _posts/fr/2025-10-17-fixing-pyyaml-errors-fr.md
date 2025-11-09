---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Résoudre les erreurs d'installation de PyYAML
translated: true
type: note
---

### Comprendre l'erreur

Cette sortie semble provenir d'une commande `python setup.py install` ou `pip install pyyaml` (à partir des sources) sur un système Linux avec Python 3.13. Il y a deux problèmes principaux :

1. **Échec de compilation de l'extension C** :
   - Le processus de compilation essaie de compiler l'extension C (`yaml._yaml`) mais ne trouve pas le fichier source `yaml/_yaml.c`.
   - Cela se produit car les versions récentes de PyYAML (à partir d'environ la version 4.x) génèrent le fichier `_yaml.c` dynamiquement en utilisant Cython pendant la compilation. La distribution source sur PyPI n'inclut pas le fichier `.c` pré-généré, donc Cython doit être installé au préalable pour le créer.
   - Par conséquent, le processus revient à la version pure Python (qui fonctionne mais est plus lente et manque certaines fonctionnalités comme le support de libyaml).

2. **Permission refusée pendant l'installation** :
   - L'installation tente d'écrire dans le répertoire Python système (`/usr/local/lib/python3.13/dist-packages`), ce qui nécessite des privilèges d'administrateur.
   - Ceci est courant lors de l'exécution sans `sudo` ou sans l'option `--user`.

### Solutions

#### Corriger le problème de compilation
Installez d'abord Cython, puis réessayez l'installation de PyYAML. Cela générera le fichier `_yaml.c` manquant et permettra la compilation de l'extension C.

- **En utilisant pip (recommandé)** :
  ```
  pip install cython
  pip install pyyaml
  ```
  - Si vous voulez l'extension C plus rapide avec le support de libyaml (nécessite l'installation de libyaml-dev via votre gestionnaire de paquets, par exemple `sudo apt install libyaml-dev` sur Ubuntu/Debian) :
    ```
    pip install cython libyaml
    pip install --upgrade --force-reinstall --no-cache-dir pyyaml
    ```

- **Si vous utilisez setup.py directement** (non recommandé, préférez pip) :
  ```
  pip install cython
  python setup.py build_ext --inplace
  python setup.py install
  ```

Note : Python 3.13 étant relativement nouveau, assurez-vous d'utiliser la dernière version de Cython (par exemple, 3.0.11 ou plus récent) pour la compatibilité. Si vous utilisez une version de Python avec le "free-threaded" build, des ajustements de compilation supplémentaires peuvent être nécessaires — vérifiez les issues sur le GitHub de PyYAML pour les mises à jour.

#### Corriger le problème de permission
- **Installer dans le répertoire utilisateur** (plus sûr, ne nécessite pas sudo) :
  ```
  pip install --user cython pyyaml
  ```
  - Ceci installe dans `~/.local/lib/python3.13/site-packages`.

- **Utiliser sudo pour une installation système** (à utiliser avec prudence, car cela peut entrer en conflit avec les gestionnaires de paquets) :
  ```
  sudo pip install cython pyyaml
  ```

- **Meilleure pratique : Utiliser un environnement virtuel** :
  Pour éviter complètement les problèmes de permission :
  ```
  python -m venv myenv
  source myenv/bin/activate  # Sur Linux/Mac
  pip install cython pyyaml
  ```
  Cela garde tout isolé.

Après l'installation, testez avec `python -c "import yaml; print(yaml.__version__)"`. Si l'importation se fait sans erreur, c'est bon.

Si ces solutions ne résolvent pas le problème (par exemple, à cause d'un problème spécifique à Python 3.13), fournissez plus de détails comme votre commande exacte et la version de votre OS.

[Building on Mac - _yaml.c not found](https://github.com/yaml/pyyaml/issues/122)  
[extension _yaml is not built](https://github.com/yaml/pyyaml/issues/179)  
[Installing Pyyaml with libyaml support on MacOS](https://akasurde.github.io/installing-pyyaml-with-libyaml-on-macos.html)
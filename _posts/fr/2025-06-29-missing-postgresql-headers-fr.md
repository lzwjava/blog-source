---
audio: false
generated: true
lang: fr
layout: post
title: Erreur de libpq-fe.h pour psycopg2
translated: true
type: note
---

Lorsque vous essayez d'installer le package Python `psycopg2`, vous avez rencontré une erreur indiquant que la wheel n'a pas pu être construite avec succès. La partie clé du message d'erreur est :

```
In file included from psycopg/adapter_asis.c:28:
./psycopg/psycopg.h:36:10: fatal error: libpq-fe.h: No such file or directory
   36 | #include <libpq-fe.h>
      |          ^~~~~~~~~~~~
compilation terminated.
```

Cette erreur se produit car le fichier `libpq-fe.h`, un fichier d'en-tête de la bibliothèque cliente PostgreSQL, est manquant sur votre système. Le package `psycopg2` a besoin de ce fichier pour être compilé à partir des sources, car il fournit l'interface pour connecter Python aux bases de données PostgreSQL. Ci-dessous, j'expliquerai pourquoi cela se produit et je fournirai une solution étape par étape pour la corriger.

---

### Pourquoi cette erreur se produit
Le package `psycopg2` est un adaptateur PostgreSQL pour Python, et lorsque vous l'installez en utilisant `pip`, il tente de compiler ses extensions C. Ces extensions dépendent de la bibliothèque cliente PostgreSQL, en particulier des en-têtes de développement comme `libpq-fe.h`. Le message d'erreur le confirme :

```
It appears you are missing some prerequisite to build the package from source.
```

Votre système, qui semble être une distribution Linux basée sur Debian (d'après l'utilisation de `x86_64-linux-gnu-gcc`), ne possède pas les fichiers de développement PostgreSQL nécessaires. Sans ceux-ci, la compilation échoue, empêchant la construction de la wheel pour `psycopg2`.

L'erreur suggère également deux options :
1. Installer le package binaire pré-construit `psycopg2-binary` via PyPI.
2. Installer les prérequis manquants et compiler `psycopg2` à partir des sources.

Étant donné que votre projet spécifie `psycopg2` (et non `psycopg2-binary`) dans le fichier des exigences, et que la compilation à partir des sources peut être nécessaire pour des raisons de compatibilité ou de personnalisation, nous nous concentrerons sur la correction du processus de compilation. Cependant, je mentionnerai également l'option binaire plus tard pour être complet.

---

### Comment corriger l'erreur
Pour résoudre ce problème, vous devez installer le package de développement du client PostgreSQL, qui fournit `libpq-fe.h` et les autres fichiers nécessaires. Voici comment procéder :

#### Étape 1 : Identifier votre système
Votre sortie de compilation inclut `x86_64-linux-gnu-gcc`, ce qui indique que vous utilisez probablement un système basé sur Debian comme Ubuntu. La solution sera adaptée à ce cas, mais je noterai des alternatives pour d'autres distributions plus tard.

#### Étape 2 : Installer le package de développement PostgreSQL
Sur les systèmes basés sur Debian (par exemple, Ubuntu), le package `libpq-dev` contient les en-têtes de la bibliothèque cliente PostgreSQL, y compris `libpq-fe.h`. Installez-le avec la commande suivante :

```bash
sudo apt-get update
sudo apt-get install libpq-dev
```

- **`sudo apt-get update`** : Assure que votre liste de packages est à jour.
- **`sudo apt-get install libpq-dev`** : Installe les fichiers de développement pour la bibliothèque cliente PostgreSQL.

Ce package place `libpq-fe.h` dans un emplacement standard (généralement `/usr/include/postgresql`), que le processus de compilation recherche (comme on peut le voir dans votre chemin d'inclusion : `-I/usr/include/postgresql`).

#### Étape 3 : Réessayer l'installation
Une fois `libpq-dev` installé, réessayez d'installer vos exigences :

```bash
pip install -r scripts/requirements/requirements.local.txt
```

Cela devrait maintenant fonctionner, car le fichier manquant `libpq-fe.h` sera disponible, permettant à `psycopg2` de construire sa wheel.

---

### Vérification de la correction
Si l'installation échoue toujours, vérifiez que les en-têtes PostgreSQL sont correctement installés :
- Exécutez `pg_config --includedir` pour voir où les en-têtes sont situés (par exemple, `/usr/include/postgresql`).
- Assurez-vous que cela correspond au chemin d'inclusion dans la commande de compilation (`-I/usr/include/postgresql`).

Votre sortie de compilation montre `-DPG_VERSION_NUM=140018`, indiquant qu'elle cible PostgreSQL 14. Le package `libpq-dev` est indépendant de la version et devrait fonctionner avec les en-têtes PostgreSQL 14.

---

### Alternative : Utiliser le package binaire
Si vous n'avez pas besoin de compiler `psycopg2` à partir des sources (par exemple, pour des optimisations ou une compatibilité spécifique), vous pouvez installer le package pré-construit `psycopg2-binary` à la place :

```bash
pip install psycopg2-binary
```

Pour l'utiliser dans votre projet, mettez à jour `scripts/requirements/requirements.local.txt` pour remplacer `psycopg2` par `psycopg2-binary`. Cependant, notez que `psycopg2-binary` peut avoir des limitations (par exemple, des problèmes de compatibilité potentiels avec certaines versions de PostgreSQL), donc la compilation à partir des sources est préférable si votre projet l'exige.

---

### Pour les autres distributions
Si vous n'êtes pas sur un système basé sur Debian, installez le package équivalent :
- **Red Hat/CentOS/Fedora** : `sudo yum install postgresql-devel` ou `sudo dnf install postgresql-devel`
- **Arch Linux** : `sudo pacman -S postgresql-libs`
- **macOS (avec Homebrew)** : `brew install libpq`

Ensuite, réexécutez la commande `pip install`.

---

### Résumé
L'erreur se produit car `libpq-fe.h` est manquant, ce fichier faisant partie des fichiers de développement du client PostgreSQL. Pour votre système basé sur Debian, l'installation de `libpq-dev` avec `sudo apt-get install libpq-dev` devrait résoudre le problème. Après cela, relancez votre commande `pip install`, et `psycopg2` devrait se compiler avec succès. Si vous préférez une solution plus rapide et n'avez pas besoin de la compilation à partir des sources, utilisez `psycopg2-binary` à la place.
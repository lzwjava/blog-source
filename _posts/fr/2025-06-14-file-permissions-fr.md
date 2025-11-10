---
audio: false
generated: true
lang: fr
layout: post
title: Permissions des fichiers
translated: true
type: note
---

Le `crw-rw----` dans la sortie de `ls -alrt /dev/ttyUSB0` représente le **type de fichier et les permissions** pour le fichier de périphérique `/dev/ttyUSB0`. Voici une explication détaillée :

- **c** : Le premier caractère indique le type de fichier. `c` signifie qu'il s'agit d'un **périphérique caractère** (par opposition à `b` pour un périphérique bloc, `d` pour un répertoire, ou `-` pour un fichier standard). `/dev/ttyUSB0` est un périphérique de port série, typiquement utilisé pour les adaptateurs USB-série.

- **rw-rw----** : Les neuf caractères suivants représentent les **permissions** pour le fichier, divisées en trois groupes :
  - **rw-** (positions 2-4) : Permissions pour le **propriétaire** (root). Le propriétaire peut **lire** (`r`) et **écrire** (`w`), mais pas exécuter (`-`).
  - **rw-** (positions 5-7) : Permissions pour le **groupe** (dialout). Les membres du groupe `dialout` peuvent aussi **lire** et **écrire**, mais pas exécuter.
  - **---** (positions 8-10) : Permissions pour les **autres** (utilisateurs n'étant ni le propriétaire ni dans le groupe). Les autres n'ont **aucune permission** (pas de lecture, d'écriture ou d'exécution).

### Résumé
- `/dev/ttyUSB0` est un fichier de périphérique caractère.
- Le propriétaire (`root`) et le groupe (`dialout`) peuvent lire et écrire sur le périphérique.
- Les autres utilisateurs n'ont aucun accès.
- Pour interagir avec ce périphérique (par exemple, pour une communication série), votre compte utilisateur doit typiquement être dans le groupe `dialout`. Vous pouvez vérifier avec la commande `groups` et vous ajouter avec `sudo usermod -a -G dialout <nom_utilisateur>` si nécessaire (puis déconnectez-vous et reconnectez-vous).
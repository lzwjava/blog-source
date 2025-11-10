---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Guide de Contrôle des Fins de Ligne Git
translated: true
type: note
---

`git config core.autocrlf` contrôle la façon dont Git gère les fins de ligne lorsque vous extrayez des fichiers du dépôt et lorsque vous les validez. C'est important car Windows utilise **CRLF** (`\r\n`) pour les fins de ligne, tandis que Linux et macOS utilisent **LF** (`\n`). Sans gestion appropriée, les fichiers peuvent alterner entre les formats selon la personne qui les modifie, entraînant des différences "sales" et des modifications inutiles.

---

### Fonctionnement

* **Lors de l'extraction (lecture)** d'un fichier, Git peut convertir les fins de ligne pour correspondre à la convention de votre système d'exploitation (afin qu'elles apparaissent naturellement dans votre éditeur).
* **Lors de la validation (écriture)** d'un fichier, Git peut reconvertir les fins de ligne en LF (la norme multiplateforme dans les dépôts).

---

### Paramètres

Vous le configurez avec :

```bash
git config --global core.autocrlf <valeur>
```

Les valeurs courantes :

* `true`
  Convertit **LF → CRLF** à l'extraction, et **CRLF → LF** à la validation.
  Idéal pour les **développeurs Windows** modifiant du code avec des éditeurs Windows.

* `input`
  Ne **modifie pas** les fichiers à l'extraction, mais convertit **CRLF → LF** à la validation.
  Idéal pour les **développeurs Linux/macOS** afin de garantir des dépôts avec uniquement des LF.

* `false`
  Aucune conversion. Git stocke et extrait les fichiers exactement tels quels.
  Idéal si votre équipe/éditeur gère les fins de ligne de manière cohérente.

---

### Recommandations typiques

* **Windows** :

  ```bash
  git config --global core.autocrlf true
  ```
* **Linux/macOS** :

  ```bash
  git config --global core.autocrlf input
  ```

Pour les équipes mixtes, il est également conseillé d'ajouter un fichier `.gitattributes` dans le dépôt pour imposer des fins de ligne cohérentes, par exemple :

```
* text=auto
```

---

Souhaitez-vous que je vous montre également une **configuration `.gitattributes` recommandée** qui fonctionne bien pour les équipes multiplateformes (afin de ne pas dépendre uniquement de `core.autocrlf`) ?
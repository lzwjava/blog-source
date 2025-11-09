---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Correction des Erreurs de Liaison de Définitions Multiples
translated: true
type: note
---

C'est une **erreur de liaison par définition multiple** — une erreur classique en C lorsque **des variables globales sont définies dans un fichier d'en-tête (`variables.h`)** au lieu d'y être seulement *déclarées*.

Voyons ce qui se passe et comment le corriger.

---

### 🔍 Le problème

Votre erreur indique :

```
multiple definition of `curl' ...
multiple definition of `nec' ...
multiple definition of `contador' ...
multiple definition of `descargadas' ...
```

Cela signifie que votre fichier d'en-tête `variables.h` ressemble probablement à ceci :

```c
// variables.h (problématique)
#include <curl/curl.h>

CURL *curl;
int nec;
int contador;
int descargadas;
```

Chaque fichier `.c` qui inclut `variables.h` obtient sa **propre copie** de ces variables.
Au moment de l'édition des liens, l'éditeur de liens trouve des *définitions multiples* des mêmes symboles globaux, une provenant de chaque fichier objet.

---

### ✅ Le modèle correct

Vous devez **déclarer** les variables globales dans l'en-tête, et les **définir** une seule fois dans un seul fichier `.c`.

#### Étape 1 : Corriger `variables.h`

Modifiez-le ainsi :

```c
// variables.h
#ifndef VARIABLES_H
#define VARIABLES_H

#include <curl/curl.h>

extern CURL *curl;
extern int nec;
extern int contador;
extern int descargadas;

#endif
```

#### Étape 2 : Définissez-les une seule fois (par exemple, dans `variables.c`)

Créez ou mettez à jour `variables.c` :

```c
#include "variables.h"

CURL *curl = NULL;
int nec = 0;
int contador = 0;
int descargadas = 0;
```

#### Étape 3 : Recompilez

Nettoyez et recompilez :

```bash
make clean
make
```

---

### 🧠 Pourquoi cela fonctionne

* `extern` indique au compilateur que la variable *existe ailleurs*.
* Un seul fichier `.c` la définit réellement (alloue de la mémoire pour elle).
* L'éditeur de liens a alors une seule définition et de multiples références → aucun conflit.

---

Si vous le souhaitez, je peux vous montrer un exemple minimal de code avant/après pour clarifier cela. Voulez-vous que je le fasse ?
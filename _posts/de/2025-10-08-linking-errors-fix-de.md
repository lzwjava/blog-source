---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Beheben von Linking-Fehlern durch Mehrfachdefinitionen
translated: true
type: note
---

Dies ist ein **Multiple-Definition-Linking-Fehler** – ein klassischer C-Fehler, der auftritt, wenn **globale Variablen in einer Header-Datei (`variables.h`)** *definiert* werden, anstatt dort nur *deklariert* zu werden.

Lassen Sie uns aufschlüsseln, was passiert und wie man es behebt.

---

### 🔍 Das Problem

Ihre Fehlermeldung lautet:

```
multiple definition of `curl' ...
multiple definition of `nec' ...
multiple definition of `contador' ...
multiple definition of `descargadas' ...
```

Das bedeutet, dass Ihre Header-Datei `variables.h` wahrscheinlich so aussieht:

```c
// variables.h (problematisch)
#include <curl/curl.h>

CURL *curl;
int nec;
int contador;
int descargadas;
```

Jede `.c`-Datei, die `variables.h` einbindet, erhält ihre **eigene Kopie** dieser Variablen.
Beim Linken findet der Linker *mehrere Definitionen* der gleichen globalen Symbole, eine aus jeder Objektdatei.

---

### ✅ Das korrekte Muster

Sie müssen die Globalvariablen im Header **deklarieren** und sie nur einmal in einer einzelnen `.c`-Datei **definieren**.

#### Schritt 1: Korrigieren Sie `variables.h`

Ändern Sie sie zu:

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

#### Schritt 2: Definieren Sie sie einmal (z.B. in `variables.c`)

Erstellen oder aktualisieren Sie `variables.c`:

```c
#include "variables.h"

CURL *curl = NULL;
int nec = 0;
int contador = 0;
int descargadas = 0;
```

#### Schritt 3: Bauen Sie neu

Bereinigen und neu bauen:

```bash
make clean
make
```

---

### 🧠 Warum das funktioniert

* `extern` teilt dem Compiler mit, dass die Variable *anderswo existiert*.
* Nur eine `.c`-Datei definiert sie tatsächlich (weist Speicher für sie zu).
* Der Linker hat dann eine Definition und mehrere Referenzen → kein Konflikt.

---

Falls Sie möchten, kann ich Ihnen ein minimales Beispiel für Vorher/Nachher-Code zeigen, um dies zu verdeutlichen. Möchten Sie das?
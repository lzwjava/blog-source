---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Corrección de Errores de Enlace por Múltiples Definiciones
translated: true
type: note
---

Este es un **error de enlace por definición múltiple** — un error clásico en C cuando **las variables globales se definen en un archivo de cabecera (`variables.h`)** en lugar de solo *declararse* allí.

Desglosemos lo que está sucediendo y cómo solucionarlo.

---

### 🔍 El problema

Tu error dice:

```
multiple definition of `curl' ...
multiple definition of `nec' ...
multiple definition of `contador' ...
multiple definition of `descargadas' ...
```

Eso significa que tu archivo de cabecera `variables.h` probablemente se ve así:

```c
// variables.h (problemático)
#include <curl/curl.h>

CURL *curl;
int nec;
int contador;
int descargadas;
```

Cada archivo `.c` que incluye `variables.h` obtiene su **propia copia** de esas variables.
En el momento del enlace, el linker encuentra *definiciones múltiples* de los mismos símbolos globales, una de cada archivo objeto.

---

### ✅ El patrón correcto

Debes **declarar** las globales en el encabezado y **definirlas** solo una vez en un único archivo `.c`.

#### Paso 1: Corrige `variables.h`

Cámbialo a:

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

#### Paso 2: Defínelas una vez (por ejemplo, en `variables.c`)

Crea o actualiza `variables.c`:

```c
#include "variables.h"

CURL *curl = NULL;
int nec = 0;
int contador = 0;
int descargadas = 0;
```

#### Paso 3: Recompila

Limpia y recompila:

```bash
make clean
make
```

---

### 🧠 Por qué esto funciona

* `extern` le dice al compilador que la variable *existe en otro lugar*.
* Solo un archivo `.c` la define realmente (asigna memoria para ella).
* El linker entonces tiene una definición y múltiples referencias → sin conflicto.

---

Si lo deseas, puedo mostrarte un ejemplo mínimo de código antes/después para hacer esto más claro. ¿Te gustaría eso?
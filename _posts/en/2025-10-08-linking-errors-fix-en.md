---
audio: false
generated: true
image: false
lang: en
layout: post
model: x-ai/grok-4-fast
title: Fixing Multiple Definition Linking Errors
translated: false
type: note
---

This is a **multiple definition linking error** — a classic C mistake when **global variables are defined in a header file (`variables.h`)** instead of just being *declared* there.

Let’s break down what’s happening and how to fix it.

---

### 🔍 The problem

Your error says:

```
multiple definition of `curl' ...
multiple definition of `nec' ...
multiple definition of `contador' ...
multiple definition of `descargadas' ...
```

That means your header file `variables.h` probably looks like this:

```c
// variables.h (problematic)
#include <curl/curl.h>

CURL *curl;
int nec;
int contador;
int descargadas;
```

Every `.c` file that includes `variables.h` gets its **own copy** of those variables.
At link time, the linker finds *multiple definitions* of the same global symbols, one from each object file.

---

### ✅ The correct pattern

You must **declare** the globals in the header, and **define** them only once in a single `.c` file.

#### Step 1: Fix `variables.h`

Change it to:

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

#### Step 2: Define them once (e.g., in `variables.c`)

Create or update `variables.c`:

```c
#include "variables.h"

CURL *curl = NULL;
int nec = 0;
int contador = 0;
int descargadas = 0;
```

#### Step 3: Rebuild

Clean and rebuild:

```bash
make clean
make
```

---

### 🧠 Why this works

* `extern` tells the compiler that the variable *exists elsewhere*.
* Only one `.c` file actually defines it (allocates memory for it).
* The linker then has one definition and multiple references → no conflict.

---

If you’d like, I can show you a minimal example of before/after code to make this clearer. Would you like that?
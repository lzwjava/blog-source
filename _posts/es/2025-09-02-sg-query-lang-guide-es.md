---
audio: false
generated: true
image: false
lang: es
layout: post
title: Guía del Lenguaje de Consulta de Sourcegraph
translated: true
type: note
---

La búsqueda de Sourcegraph tiene su propio lenguaje de consulta que es flexible y potente. Aquí tienes un desglose de la sintaxis común que puedes usar:

---

### 1. **Búsqueda Básica por Palabra Clave**

* Simplemente escribe términos:

  ```
  http client
  ```

  Encuentra archivos o código que contengan ambas palabras.

---

### 2. **Operadores Lógicos**

* `AND`, `OR`, `NOT` (deben ir en mayúsculas):

  ```
  React AND useEffect
  React OR Vue
  logger NOT debug
  ```

---

### 3. **Filtros**

* `repo:` → limitar por repositorio

  ```
  repo:github.com/myorg/myrepo
  ```
* `file:` → coincidir con la ruta del archivo (admite regex)

  ```
  file:\.java$
  ```
* `lang:` → restringir a un lenguaje de programación

  ```
  lang:python requests
  ```
* `content:` → forzar una búsqueda de texto (ignora coincidencias estructurales)

  ```
  content:"SELECT * FROM"
  ```
* `case:yes` → hacer la búsqueda sensible a mayúsculas y minúsculas

---

### 4. **Coincidencia con Regex**

* Por defecto, Sourcegraph admite regex.

  ```
  foo(bar|baz)
  ^class\s+\w+
  ```

---

### 5. **Búsqueda Estructural**

Usa espacios para patrones como `:[var]` para coincidir con estructuras de código:

```
if (:[cond]) { :[body] }
```

---

### 6. **Búsqueda por Revisión / Rama**

* Añade `@branch`, `@commit` o `@tag`:

  ```
  repo:myrepo@main lang:go fmt.Println
  ```

---

### 7. **Símbolos y Definiciones**

* `type:symbol` → buscar nombres de símbolos
* `type:commit` → buscar mensajes de commit
* `type:diff` → buscar diferencias de código (diffs)

---

### 8. **Ejemplos**

* Encontrar todos los comentarios `TODO` en archivos Go:

  ```
  TODO lang:go
  ```
* Buscar solo en la carpeta `src/` para métodos Java:

  ```
  file:^src/ lang:java "public static"
  ```
* Buscar en múltiples repositorios:

  ```
  repo:github.com/org/.* file:\.ts$ "useState"
  ```

---

👉 ¿Quieres que prepare una **guía rápida de las consultas más usadas de Sourcegraph** (como frases de una línea que puedes reutilizar a diario), o una **inmersión profunda con patrones avanzados**?
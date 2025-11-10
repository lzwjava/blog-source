---
audio: false
generated: true
image: false
lang: en
layout: post
title: Sourcegraph Query Language Guide
translated: false
type: note
---

Sourcegraph search has its own query language that’s flexible and powerful. Here’s a breakdown of the common syntax you can use:

---

### 1. **Basic Keyword Search**

* Just type terms:

  ```
  http client
  ```

  Finds files or code containing both words.

---

### 2. **Logical Operators**

* `AND`, `OR`, `NOT` (must be uppercase):

  ```
  React AND useEffect
  React OR Vue
  logger NOT debug
  ```

---

### 3. **Filters**

* `repo:` → limit by repository

  ```
  repo:github.com/myorg/myrepo
  ```
* `file:` → match file path (regex supported)

  ```
  file:\.java$
  ```
* `lang:` → restrict to a programming language

  ```
  lang:python requests
  ```
* `content:` → force a text search (ignores structural matches)

  ```
  content:"SELECT * FROM"
  ```
* `case:yes` → make search case-sensitive

---

### 4. **Regex Matching**

* By default, Sourcegraph supports regex.

  ```
  foo(bar|baz)
  ^class\s+\w+
  ```

---

### 5. **Structural Search**

Use pattern holes like `:[var]` to match code structures:

```
if (:[cond]) { :[body] }
```

---

### 6. **Revision / Branch Search**

* Append `@branch`, `@commit`, or `@tag`:

  ```
  repo:myrepo@main lang:go fmt.Println
  ```

---

### 7. **Symbols and Definitions**

* `type:symbol` → search for symbol names
* `type:commit` → search commit messages
* `type:diff` → search code diffs

---

### 8. **Examples**

* Find all `TODO` comments in Go files:

  ```
  TODO lang:go
  ```
* Search only in `src/` folder for Java methods:

  ```
  file:^src/ lang:java "public static"
  ```
* Search across multiple repos:

  ```
  repo:github.com/org/.* file:\.ts$ "useState"
  ```

---

👉 Do you want me to prepare a **quick cheat sheet of the most used Sourcegraph queries** (like one-liners you can reuse daily), or a **deep-dive with advanced patterns**?
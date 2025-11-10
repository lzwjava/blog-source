---
audio: false
generated: true
image: false
lang: de
layout: post
title: Sourcegraph-Abfragesprache Leitfaden
translated: true
type: note
---

Die Sourcegraph-Suche verfügt über eine eigene flexible und leistungsstarke Abfragesprache. Hier ist eine Übersicht der gängigen Syntax, die Sie verwenden können:

---

### 1. **Einfache Schlüsselwortsuche**

* Geben Sie einfach Begriffe ein:

  ```
  http client
  ```

  Findet Dateien oder Code, die beide Wörter enthalten.

---

### 2. **Logische Operatoren**

* `AND`, `OR`, `NOT` (müssen in Großbuchstaben sein):

  ```
  React AND useEffect
  React OR Vue
  logger NOT debug
  ```

---

### 3. **Filter**

* `repo:` → Auf Repository beschränken

  ```
  repo:github.com/myorg/myrepo
  ```
* `file:` → Dateipfad abgleichen (Regex unterstützt)

  ```
  file:\.java$
  ```
* `lang:` → Auf eine Programmiersprache beschränken

  ```
  lang:python requests
  ```
* `content:` → Erzwingt eine Textsuche (ignoriert strukturelle Treffer)

  ```
  content:"SELECT * FROM"
  ```
* `case:yes` → Suche case-sensitiv machen

---

### 4. **Regex-Abgleich**

* Standardmäßig unterstützt Sourcegraph Regex.

  ```
  foo(bar|baz)
  ^class\s+\w+
  ```

---

### 5. **Strukturelle Suche**

Verwenden Sie Platzhalter wie `:[var]`, um Codestrukturen abzugleichen:

```
if (:[cond]) { :[body] }
```

---

### 6. **Revisions- / Branch-Suche**

* Hängen Sie `@branch`, `@commit` oder `@tag` an:

  ```
  repo:myrepo@main lang:go fmt.Println
  ```

---

### 7. **Symbole und Definitionen**

* `type:symbol` → Nach Symbolnamen suchen
* `type:commit` → Commit-Nachrichten durchsuchen
* `type:diff` → Code-Diffs durchsuchen

---

### 8. **Beispiele**

* Finde alle `TODO`-Kommentare in Go-Dateien:

  ```
  TODO lang:go
  ```
* Suche nur im `src/`-Ordner nach Java-Methoden:

  ```
  file:^src/ lang:java "public static"
  ```
* Suche über mehrere Repositories hinweg:

  ```
  repo:github.com/org/.* file:\.ts$ "useState"
  ```

---

👉 Soll ich eine **kurze Spickzettel der am häufigsten verwendeten Sourcegraph-Abfragen** erstellen (zum Beispiel einzeilige Abfragen, die Sie täglich wiederverwenden können) oder einen **tiefgehenden Einblick mit erweiterten Mustern**?
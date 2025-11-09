---
audio: false
date: 2025-09-12
generated: true
image: false
lang: de
layout: post
model: mistralai/mistral-medium-3.1
title: Sourcegraph Code-Suche Anleitung
translated: true
type: note
---

Sourcegraph ist ein leistungsstarkes Tool zur Code-Suche und Navigation, das Entwicklern ermöglicht, über mehrere Repositories hinweg zu suchen, Code-Abhängigkeiten zu verstehen und große Codebasen effizient zu navigieren. Dieser Leitfaden behandelt **Suchsyntax, Best Practices und sprachspezifische Suchen (Java & Python)**.

---

## **1. Grundlegende Suchsyntax**
Sourcegraph unterstützt **Literal-, Regex- und Struktursuche** mit Filtern.

### **1.1. Literale Suche**
Suche nach exaktem Text:
```
"def calculate_sum"
```

### **1.2. Regex-Suche**
Verwende `/.../` für Regex:
```
/def \w+_sum\(/
```

### **1.3. Struktursuche (Beta)**
Suche nach Codemustern (z.B. Funktionsdefinitionen):
```
type:func def calculate_sum
```

### **1.4. Filter**
Verfeinere Suchen mit Filtern:
- `repo:` – Suche in einem bestimmten Repo
  ```
  repo:github.com/elastic/elasticsearch "def search"
  ```
- `file:` – Suche in bestimmten Dateien
  ```
  file:src/main/java "public class"
  ```
- `lang:` – Suche in einer bestimmten Sprache
  ```
  lang:python "def test_"
  ```
- `type:` – Suche nach Symbolen (Funktionen, Klassen, etc.)
  ```
  type:func lang:go "func main"
  ```

---

## **2. Erweiterte Suchtechniken**
### **2.1. Boolesche Operatoren**
- `AND` (Standard): `def calculate AND sum`
- `OR`: `def calculate OR def sum`
- `NOT`: `def calculate NOT def subtract`

### **2.2. Wildcards**
- `*` – Entspricht einer beliebigen Zeichenfolge
  ```
  "def calculate_*"
  ```
- `?` – Entspricht einem einzelnen Zeichen
  ```
  "def calculate_?"
  ```

### **2.3. Groß-/Kleinschreibung**
- Standardmäßig case-insensitive
- Erzwinge case-sensitive mit `case:yes`
  ```
  case:yes "Def Calculate"
  ```

### **2.4. Suche in Kommentaren**
Verwende `patternType:literal`, um in Kommentaren zu suchen:
```
patternType:literal "// TODO:"
```

---

## **3. Suchen in Java-Code**
### **3.1. Klassen finden**
```
type:symbol lang:java "public class"
```
### **3.2. Methoden finden**
```
type:func lang:java "public void"
```
### **3.3. Annotationen finden**
```
lang:java "@Override"
```
### **3.4. Imports finden**
```
lang:java "import org.springframework"
```
### **3.5. Exception-Handling finden**
```
lang:java "try {" AND "catch (Exception"
```

---

## **4. Suchen in Python-Code**
### **4.1. Funktionen finden**
```
type:func lang:python "def calculate"
```
### **4.2. Klassen finden**
```
type:symbol lang:python "class Calculator"
```
### **4.3. Imports finden**
```
lang:python "import pandas"
```
### **4.4. Dekoratoren finden**
```
lang:python "@app.route"
```
### **4.5. Docstrings finden**
```
lang:python '"""'
```

---

## **5. Best Practices**
1. **Verwende `lang:`**, um Ergebnisse einzugrenzen.
2. **Kombiniere Filter** (`repo:`, `file:`, `type:`) für Präzision.
3. **Verwende Regex** für flexible Mustersuche.
4. **Speichere Suchen** für häufige Abfragen.
5. **Verwende `case:yes`**, wenn nötig.

---

## **6. Beispielabfragen**

| **Ziel** | **Abfrage** |
|----------|-----------|
| Finde alle Java-`main`-Methoden | `lang:java "public static void main"` |
| Finde Python-Testfunktionen | `lang:python "def test_"` |
| Finde TODO-Kommentare in Go | `lang:go "// TODO:"` |
| Finde Spring Boot Controller | `lang:java "@RestController"` |
| Finde alle `if`-Anweisungen in JS | `lang:javascript "if ("` |

---

## **7. Fazit**
Die Sourcegraph-Suche ist **leistungsstark und flexibel** und unterstützt **Literal-, Regex- und Struktursuchen** über mehrere Sprachen hinweg. Durch das Beherrschen von Filtern (`lang:`, `repo:`, `type:`) kannst du große Codebasen effizient navigieren.

### **Nächste Schritte**
- Probiere **gespeicherte Suchen** für wiederkehrende Abfragen aus.
- Erkunde **Code Intelligence** (Hover-Tooltips, Cross-Repo-Navigation).
- Verwende **Sourcegraph-Erweiterungen** (VS Code, JetBrains).

Möchtest du einen tieferen Einblick in eine bestimmte Funktion? 🚀
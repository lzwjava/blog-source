---
audio: false
generated: true
image: false
lang: de
layout: post
title: Regeln für die Spring-Eigenschaftsreihenfolge erklärt
translated: true
type: note
---

Im Frühjahr, wenn Sie **doppelte Eigenschaftsschlüssel** in Ihren Konfigurationsquellen haben (z. B. `application.properties`, `application.yml`, Umgebungsvariablen, Kommandozeilenargumente usw.), gewinnt der **letzte mit der höchsten Priorität**.

Hier ist die detaillierte Funktionsweise:

### 1. Reihenfolge der Eigenschaftsquellen

Spring Boot wendet eine wohldefinierte **Reihenfolge der Eigenschaftsquellen** an. Zum Beispiel:

* Kommandozeilenargumente
* `application.properties` / `application.yml` (profilspezifische zuerst, dann Standard)
* Umgebungsvariablen
* Systemeigenschaften
* Standardwerte im Code (`@Value("${...:default}")`)

Wenn derselbe Eigenschaftsschlüssel in mehreren Quellen erscheint, wählt Spring den aus der **Quelle mit der höchsten Priorität**.

### 2. Innerhalb derselben Datei

Wenn Sie denselben Eigenschaftsschlüssel **wiederholt in einer einzelnen Datei** haben (wie `application.properties`), verwendet Spring das **zuletzt deklarierte Vorkommen**.
Beispiel (`application.properties`):

```properties
server.port=8080
server.port=9090
```

Hier wird `server.port=9090` wirksam.

### 3. Über mehrere Dateien hinweg

Wenn Sie dieselbe Eigenschaft in `application.properties` und `application-dev.properties` definieren und Sie das `dev`-Profil aktivieren, überschreibt der Wert aus `application-dev.properties` den Standardwert.

### 4. Mit `@PropertySource`

Wenn Sie mehrere Eigenschaftsdateien über `@PropertySource` laden, ist die Reihenfolge der Deklaration wichtig. Die spätere kann frühere Werte überschreiben, es sei denn, Sie markieren sie mit `ignoreResourceNotFound` oder steuern die Priorität explizit.

---

✅ **Zusammenfassung:**

* Spring löst Eigenschaften nach der **Priorität der Quellen** auf.
* Innerhalb **derselben Datei** gewinnt die **letzte Schlüsseldefinition**.
* Über Dateien/Profile hinweg überschreibt die **Eigenschaft des aktiven Profils oder der später geladenen Datei** die früheren.

Möchten Sie, dass ich Ihnen auch die **genaue Spring Boot Eigenschafts-Prioritätshierarchie (von höchster zu niedrigster)** zeige? Das gibt ein sehr klares Bild davon, wo Überschreibungen stattfinden.
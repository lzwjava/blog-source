---
audio: false
generated: true
image: false
lang: de
layout: post
title: Jackson Standard-Typisierung Erklärt und Deaktiviert
translated: true
type: note
---

In Jackson (der `com.fasterxml.jackson.databind`-Bibliothek) ist **Default Typing** (Standard-Typisierung) eine Funktion des `ObjectMapper`, die automatisch Typ-Metadaten (wie `@class` oder `@type`) in serialisiertes JSON einfügt, damit Objekte wieder in ihre ursprünglichen polymorphen Typen deserialisiert werden können.

Zum Beispiel: Wenn Sie eine `List<Animal>` serialisieren, die sowohl `Dog` als auch `Cat` enthält, fügt die Standard-Typisierung zusätzliche JSON-Felder hinzu, damit Jackson später weiß, welche Unterklasse instanziiert werden muss.

---

### Wie das Deaktivieren funktioniert

Wenn Sie **Default Typing deaktivieren**, hört Jackson auf, diese zusätzlichen Typ-Metadaten-Felder einzufügen. Das bedeutet:

* Die JSON-Ausgabe wird "sauberer" sein, ohne `@class`/`@type`-Hinweise.
* Bei der Deserialisierung kann Jackson Objekte nur unter Verwendung deklarierter statischer Typen (dem Zieltyp, den Sie übergeben) rekonstruieren, nicht die ursprünglichen Laufzeittypen.
* Alle polymorphen Anwendungsfälle werden brechen, es sei denn, Sie konfigurieren explizit `@JsonTypeInfo`, `@JsonSubTypes` oder benutzerdefinierte Module.

---

### Relevante Methoden

* **Aktivieren** (Pre-2.10-Stil):

  ```java
  objectMapper.enableDefaultTyping();
  ```

  (veraltet, weil es zu freizügig war und Sicherheitsrisiken einführte.)

* **Deaktivieren**:

  ```java
  objectMapper.disableDefaultTyping();
  ```

  oder in neueren Versionen (2.10+), rufen Sie auf:

  ```java
  objectMapper.activateDefaultTyping(PolymorphicTypeValidator, ObjectMapper.DefaultTyping.NON_FINAL);
  ```

  Um es zu *deaktivieren*, rufen Sie diese Methode einfach **nicht auf** (es gibt keine Standard-Typisierung, es sei denn, Sie aktivieren sie), oder Sie können aufrufen:

  ```java
  objectMapper.deactivateDefaultTyping();
  ```

---

### Sicherheit und Begründung

* **Default Typing ist in modernen Jackson-Versionen standardmäßig deaktiviert**, weil es ausgenutzt werden kann (Angreifer könnten JSON konstruieren, das gefährliche Klassen instanziiert).
* Wenn Sie es deaktivieren, verhält sich Jackson in einem "sicheren" Modus, bei dem die Deserialisierung nur für Typen funktioniert, die Sie explizit binden, nicht für beliebige Laufzeittypen.
* Wenn Sie polymorphe Unterstützung benötigen, sollten Sie Ihre Klassen mit `@JsonTypeInfo` annotieren, anstatt sich auf globale Standard-Typisierung zu verlassen.

---

✅ **Kurz gesagt:**
Das Deaktivieren der Standard-Typisierung weist Jackson an, **keine** Typ-Metadaten in JSON aufzunehmen, was bedeutet, dass es polymorphe Untertypen bei der Deserialisierung nicht automatisch rekonstruiert. Dies verringert die Flexibilität, ist aber sicherer und hält das JSON sauber.

Möchten Sie, dass ich Ihnen ein **Vorher/Nachher-JSON-Beispiel** mit aktivierter vs. deaktivierter Standard-Typisierung zeige?
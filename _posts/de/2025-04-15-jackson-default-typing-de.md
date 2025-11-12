---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Jackson Standard-Typisierung erklärt
translated: true
type: note
---

### Was ist Default Typing in Jacksons ObjectMapper?

Jacksons `ObjectMapper` ist eine Kernklasse in der Jackson-JSON-Bibliothek für Java, die für die Serialisierung von Java-Objekten zu JSON und die Deserialisierung von JSON zurück zu Objekten verantwortlich ist. "Default Typing" ist ein Feature, das den Umgang mit polymorphen Typen verbessert (z. B. wenn ein Feld verschiedene Unterklassen halten kann). Es funktioniert, indem Typinformationen in die JSON-Ausgabe während der Serialisierung eingebettet werden, die der Mapper während der Deserialisierung verwendet, um die korrekte konkrete Klasse zu instanziieren.

Ohne Default Typing verlässt sich Jackson auf den deklarierten Typ (z. B. eine abstrakte Basisklasse oder ein Interface), und Sie benötigen möglicherweise eine benutzerdefinierte Konfiguration wie `@JsonTypeInfo`-Annotationen, um Untertypen anzugeben. Das Aktivieren von Default Typing bietet einen globalen oder semi-globalen Fallback für Polymorphie, was besonders nützlich für Sammlungen oder Maps mit gemischten Typen ist.

### Wie funktioniert es?

Das Aktivieren von Default Typing verändert den Serialisierungsprozess:
1.  **Serialisierung**: Wenn ein Objektgraph serialisiert wird, fügt Jackson ein spezielles `@class`-Feld oder ähnliche Metadaten zum JSON hinzu, um den Laufzeittyp polymorpher Objekte anzuzeigen. Dies geschieht nur für Typen, bei denen der deklarierte Typ die konkrete Klasse nicht vollständig spezifiziert (z. B. eine `List`, die `String`- und `Integer`-Objekte enthält, oder abstrakte Klassenfelder).

2.  **Deserialisierung**: Während der Deserialisierung verwendet der Mapper diese eingebetteten Typinformationen, um die genaue Klasse nachzuschlagen und zu instanziieren. Dabei nutzt er Jacksons `TypeFactory`, um Typen dynamisch aufzulösen.

Um es zu aktivieren, rufen Sie eine dieser Methoden auf einer `ObjectMapper`-Instanz auf:
-   `mapper.enableDefaultTyping()`: Eine veraltete Methode, die die Aufnahme von Polymorphie-Typinformationen zur Laufzeit aktiviert (anfällig für Sicherheitsprobleme).
-   `mapper.activateDefaultTyping(ObjectMapper.DefaultTyping policy)`: Eine sicherere, empfohlene Alternative, eingeführt in Jackson 2.10. Sie erlaubt die Angabe eines `DefaultTyping`-Enum-Werts, wie z. B.:
    -   `JAVA_LANG_OBJECT`: Schließt Typisierung für alle `Object`-Referenzen ein.
    -   `NON_CONCRETE_AND_ARRAYS`: Schließt Typisierung für abstrakte/nicht-konkrete Typen und Arrays ein.
    -   `NON_FINAL`: Schließt Typisierung für nicht-finale Klassen ein.

Beispiel zur Verwendung:
```java
import com.fasterxml.jackson.databind.ObjectMapper;
import static com.fasterxml.jackson.databind.ObjectMapper.DefaultTyping;

ObjectMapper mapper = new ObjectMapper();
mapper.activateDefaultTyping(DefaultTyping.NON_CONCRETE_AND_ARRAYS);
```

Ohne Aktivierung könnte die JSON-Ausgabe für eine `List<Object>` mit gemischten Typen die Typdetails weglassen, was zu Deserialisierungsfehlern führt. Wenn es aktiviert ist, enthält das JSON Typ-Hinweise, z. B. `[{"@class": "java.lang.String", "value": "hallo"}, {"@class": "java.lang.Integer", "value": 42}]`.

### Sicherheitsüberlegungen und Einschränkungen

-   **Schwachstellen**: Das blinde Aktivieren von Default Typing (insbesondere der alten `enableDefaultTyping()`-Methode) kann Systeme Angriffen wie Datenextraktion aussetzen, da es die Deserialisierung beliebiger Klassen über manipuliertes JSON erlaubt. Jackson schränkt dies in neueren Versionen standardmäßig ein und erlaubt nur gängige Typen, sofern nicht angepasst.
-   **Eignung für den Anwendungsfall**: Es eignet sich am besten für vertrauenswürdige Umgebungen mit polymorphen Daten (z. B. interne APIs). Für öffentliche APIs sind explizite Typ-Annotationen oder benutzerdefinierte Serializer/Deserializer aus Sicherheitsgründen vorzuziehen.
-   **Leistung**: Fügt einen geringen Overhead aufgrund der eingebetteten Typinformationen hinzu, was die JSON-Größe erhöht.

Wenn dies sich auf einen anderen "Object Mapper" bezieht (z. B. den von Elasticsearch oder eine andere Bibliothek), geben Sie bitte mehr Kontext für eine maßgeschneiderte Erklärung. Für vollständige Details lesen Sie bitte die offizielle Dokumentation von Jackson.
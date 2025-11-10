---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Übersicht zur Jackson-Polymorphie-Deserialisierung
translated: true
type: note
---

### Überblick über Jackson Polymorphic Deserialization

Jackson ist eine Java-Bibliothek für JSON-Serialisierung und -Deserialisierung. Polymorphic Deserialization ermöglicht es Jackson, während der Deserialisierung automatisch die richtige Unterklasse einer Basisklasse zu instanziieren, basierend auf Typinformationen, die im JSON eingebettet sind. Dies ist nützlich, wenn man mit Vererbungshierarchien arbeitet, um sicherzustellen, dass der richtige Objekttyp aus JSON-Daten erstellt wird.

Wichtige Komponenten:
- **@JsonTypeInfo**: Annotationen, die steuern, wo und wie Typinformationen im JSON gespeichert werden.
- **@JsonSubTypes**: Annotationen, die Unterklassen (Subtypen) und ihre Identifikatoren auflisten.
- Jacksons Subtyp-Auflösung übernimmt das Mapping.

Ohne diese würde Jackson standardmäßig alle Objekte als Basisklasse deserialisieren, was möglicherweise zu einem Verlust von unterklassenspezifischen Daten führt.

### Schritt-für-Schritt-Funktionsweise

1. **Annotationen auf der Basisklasse**:
   - Verwende `@JsonTypeInfo`, um anzugeben, wo Typinformationen eingebettet sind (z. B. als Eigenschaft im JSON-Objekt).
   - Beispiel:
     ```java
     @JsonTypeInfo(use = JsonTypeInfo.Id.NAME, include = JsonTypeInfo.As.PROPERTY, property = "@type")
     @JsonSubTypes({
         @JsonSubType(value = Cat.class, name = "cat"),
         @JsonSubType(value = Dog.class, name = "dog")
     })
     public abstract class Animal {
         public String name;
     }
     ```
     - `use = JsonTypeInfo.Id.NAME`: Verwendet einen Namen (String-Identifikator) für den Typ.
     - `include = JsonTypeInfo.As.PROPERTY`: Fügt die Typinformation als Eigenschaft ("@type") im JSON-Objekt hinzu.
     - `@JsonSubTypes`: Ordnet Unterklassennamen ihren Java-Klassen zu (z. B. "cat" → Cat.class).

2. **Serialisierungsprozess**:
   - Beim Serialisieren eines Cat- oder Dog-Objekts fügt Jackson den Typidentifikator zum JSON hinzu.
   - Beispielausgabe: `{"@type": "cat", "name": "Whiskers", "purr": true}` (wenn Cat ein "purr"-Feld hat).

3. **Deserialisierungsprozess**:
   - Jackson liest das JSON und prüft die Typinformation (z. B. die "@type"-Eigenschaft).
   - Es ordnet den Identifikator ("cat") über `@JsonSubTypes` der registrierten Unterklasse (Cat.class) zu.
   - Instanziiert die korrekte Unterklasse und füllt ihre Felder aus.
   - Wenn keine Übereinstimmung vorliegt oder Typinformationen fehlen, wird standardmäßig auf die Basisklasse zurückgegriffen oder es werden Ausnahmen ausgelöst (konfigurierbar über `defaultImpl`).

4. **Unterstützte Typinformationsformate**:
   - `@JsonTypeInfo.As.PROPERTY`: Typ als Feld (z. B. `{"@type": "cat", ...}`).
   - `@JsonTypeInfo.As.WRAPPER_OBJECT`: Umschließt das Objekt in einen Wrapper mit dem Typ als Schlüssel (z. B. `{"cat": {...}}`).
   - `@JsonTypeInfo.As.WRAPPER_ARRAY`: Verwendet ein Array-Format.
   - `@JsonTypeInfo.As.EXTERNAL_PROPERTY`: Typinformation in einem separaten Feld (fortgeschritten, für XML-ähnliche Strukturen).

### Erweiterte Konfiguration und Grenzfälle

- **Benutzerdefinierte Name Mapper**: Verwende `@JsonTypeInfo(use = JsonTypeInfo.Id.CLASS)`, um den vollständig qualifizierten Klassennamen direkt im JSON einzubetten (z. B. `{"@class": "com.example.Cat", ...}`), was bei Refactorings problematisch sein kann.
- **Default Implementation**: Füge `defaultImpl = Animal.class` hinzu, um bei fehlenden Typinformationen einen Fallback zu haben.
- **Visibility und Mix-Ins**: Wende Annotationen über Mix-In-Klassen an, wenn die Quellklassen nicht modifiziert werden können.
- **Error Handling**: Wenn Typinformationen nicht mit einem registrierten Subtyp übereinstimmen, wirft Jackson eine `JsonMappingException`. Dies kann mit benutzerdefinierten Deserializern behandelt werden.
- **Performance**: Geringer Overhead während der Deserialisierung aufgrund effizienter Lookups, aber das Einbetten von Typinformationen erhöht die JSON-Nutzlast.

Die vollständige Dokumentation findest du im offiziellen Jackson-Guide: [Polymorphic Type Handling](https://github.com/FasterXML/jackson-docs/wiki/JacksonPolymorphicDeserialization). Diese Funktion ist seit Jackson 2.x stabil, mit ähnlichen Konzepten in anderen JSON-Bibliotheken wie Gson. Für weitere Anpassungen erweitere `PolymorphicTypeValidator` für die Sicherheit bei nicht vertrauenswürdigen Eingaben.
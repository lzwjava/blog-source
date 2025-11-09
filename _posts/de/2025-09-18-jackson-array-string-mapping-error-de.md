---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Jackson-Array-zu-String-Zuordnungsfehler
translated: true
type: note
---

### Problemübersicht

Wenn Sie Jackson (eine beliebte Java-Bibliothek für JSON-Serialisierung/Deserialisierung) verwenden und versuchen, ein JSON-Array (z. B. `[1, 2, 3]` oder `["a", "b"]`) direkt auf ein Java-Feld abzubilden, das als `String` deklariert ist, schlägt dies bei der Deserialisierung fehl. Jackson bietet keine Standardkonvertierung von JSON-Arrays zu Strings, da es sich um grundlegend verschiedene Datentypen handelt. Dies führt zu einem Laufzeitfehler.

### Erwarteter Fehler

Jackson wirft typischerweise eine `JsonMappingException` mit einer Meldung, die auf die Typinkompatibilität hinweist. Zum Beispiel:
- Beim Deserialisieren von `[1, 2, 3]` in ein `String`-Feld würden Sie etwa Folgendes sehen:  
  `Cannot deserialize instance of 'java.lang.String' out of START_ARRAY token`

Die genaue Meldung kann je nach Jackson-Version (häufig in 2.x) leicht variieren, hat ihre Ursache aber in `com.fasterxml.jackson.core.JsonMappingException`.

### Warum das passiert

- Jackson verwendet Typ-Hinweise oder Feldsignaturen, um zu bestimmen, wie JSON geparst werden soll. Ein JSON-Array beginnt mit `[` (START_ARRAY), was Jackson erwartet, um es auf Array-/Listentypen wie `List<String>`, `int[]` oder Arrays abzubilden.
- Ein `String`-Feld erwartet ein JSON-Primitive (z. B. `"hello"`) oder null, kein Array.
- Es gibt keinen eingebauten Coercer in Jackson, der diese Art von Fehlanpassung aus Sicherheitsgründen zulässt, anders als bei leichteren Typkonvertierungen für Zahlen/Strings.

### Lösung oder Workaround

- **Ändern Sie den Java-Feldtyp**: Verwenden Sie einen kompatiblen Array- oder Collection-Typ, z. B. `List<String>`, `String[]` oder `Object`, wenn Sie Flexibilität benötigen.
- **Benutzerdefinierte Deserialisierung**: Versehen Sie das Feld mit der Annotation `@JsonDeserialize(using = CustomDeserializer.class)` und definieren Sie einen Deserialisierer, um das Array nach Bedarf zu konvertieren (z. B. durch Verkettung).
- **Wenn eine String-Darstellung erwartet wird**: Stellen Sie sicher, dass das JSON einen String sendet (z. B. `"[1, 2, 3]"`) und deserialisieren Sie entsprechend.
- **Testtipp**: Verwenden Sie Jacksons `ObjectMapper` mit try-catch, um solche Fehler elegant abzufangen und auf Standardwerte zurückzufallen.

Weitere Details finden Sie in der Jackson-Dokumentation zu Deserialisierungsausnahmen. Wenn dies nicht genau auf Ihr Szenario zutrifft, teilen Sie bitte Code-Snippets für eine bessere Hilfe mit!
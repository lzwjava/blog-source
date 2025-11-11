---
audio: false
generated: true
lang: de
layout: post
title: XML-Leitfaden
translated: true
type: note
---

Okay, tauchen wir ein in einen umfassenden Leitfaden über XML (Extensible Markup Language), der seine Spezifikationen, die Funktionsweise des `<sequence>`-Elements und die Bedeutung von `minOccurs` und `maxOccurs` abdeckt.

## Ein umfassender Leitfaden zu XML

**Was ist XML?**

XML ist eine Auszeichnungssprache, die zum Transportieren von Daten entwickelt wurde. Sie ist sowohl menschenlesbar als auch maschinenlesbar. Ihr Hauptzweck ist es, Daten zu strukturieren, zu speichern und zu transportieren. Im Gegensatz zu HTML, das zur Anzeige von Daten entwickelt wurde, konzentriert sich XML darauf, die Daten selbst zu beschreiben.

**Wesentliche Merkmale von XML:**

* **Erweiterbar:** Sie können Ihre eigenen Tags definieren, um Ihre Daten zu beschreiben.
* **Selbstbeschreibend:** Die verwendeten Tags beschreiben die Bedeutung der Daten.
* **Hierarchische Struktur:** XML-Dokumente haben eine baumartige Struktur mit einem einzelnen Wurzelelement.
* **Plattformunabhängig:** XML kann von jedem System verarbeitet werden, das das XML-Format versteht.
* **Textbasiert:** XML-Dokumente sind reine Textdateien, was ihre Erstellung, Lektüre und Bearbeitung erleichtert.
* **Wohlgeformt:** XML-Dokumente müssen strenge Syntaxregeln einhalten, um als wohlgeformt zu gelten.

**Grundlegende XML-Konzepte:**

* **Elemente:** Die grundlegenden Bausteine eines XML-Dokuments. Sie werden durch Start- und End-Tags definiert (z.B. `<book>`, `</book>`). Elemente können Textinhalte, andere Elemente oder eine Mischung aus beidem enthalten.
* **Attribute:** Stellen zusätzliche Informationen über ein Element bereit. Sie erscheinen innerhalb des Start-Tags und bestehen aus einem Name-Wert-Paar (z.B. `<book genre="fiction">`).
* **Tags:** Schlüsselwörter in spitzen Klammern (`<>`). Start-Tags markieren den Beginn eines Elements, und End-Tags (mit einem Schrägstrich) markieren das Ende.
* **Wurzelelement:** Jedes XML-Dokument muss ein einzelnes, übergeordnetes Element haben, das alle anderen Elemente enthält.
* **Geschachtelte Elemente:** Elemente können innerhalb anderer Elemente geschachtelt werden, um eine hierarchische Struktur zu erstellen.
* **Leere Elemente:** Elemente ohne Inhalt können mit einem einzelnen Tag (z.B. `<br />`) oder mit einem Start- und End-Tag ohne Inhalt dazwischen (`<br></br>`) dargestellt werden.
* **XML-Deklaration (Optional, aber empfohlen):** Die erste Zeile eines XML-Dokuments kann eine XML-Deklaration sein, die die XML-Version und Kodierung angibt (z.B. `<?xml version="1.0" encoding="UTF-8"?>`).
* **Kommentare:** Werden verwendet, um erläuternde Anmerkungen innerhalb des XML-Dokuments hinzuzufügen. Sie sind in `` eingeschlossen.
* **Entities:** Stellen Sonderzeichen oder wiederverwendbare Textblöcke dar. Vordefinierte Entities umfassen `&lt;` (<), `&gt;` (>), `&amp;` (&), `&apos;` (') und `&quot;` (").

**XML-Spezifikationen:**

Das World Wide Web Consortium (W3C) pflegt die Spezifikationen für XML und verwandte Technologien. Einige wichtige XML-Spezifikationen sind:

* **XML 1.0 (und XML 1.1):** Die Kernspezifikation, die die Syntax und Struktur von XML-Dokumenten definiert. XML 1.0 ist die am weitesten verbreitete Version.
* **XML Schema (XSD):** Eine Sprache zur Definition der Struktur und Datentypen von XML-Dokumenten. Sie bietet eine leistungsfähigere und ausdrucksstärkere Möglichkeit zur Validierung von XML als Document Type Definitions (DTDs).
* **Document Type Definition (DTD):** Eine ältere Schemasprache, die zur Definition der Struktur von XML-Dokumenten verwendet wird. Obwohl sie manchmal noch anzutreffen ist, wird XSD aufgrund seiner erweiterten Funktionen generell bevorzugt.
* **XPath:** Eine Sprache zum Abfragen und Auswählen von Knoten innerhalb eines XML-Dokuments.
* **XSLT (Extensible Stylesheet Language Transformations):** Eine Sprache zum Transformieren von XML-Dokumenten in andere Formate (z.B. HTML, Klartext, andere XML-Formate).
* **Namespaces in XML:** Bieten eine Möglichkeit, Namenskonflikte zu vermeiden, wenn XML-Dokumente aus verschiedenen Quellen kombiniert werden.

**XML Schema (XSD) und das Definieren von Struktur:**

XML Schema ist entscheidend für die Definition der gültigen Struktur und des gültigen Inhalts von XML-Dokumenten. Es ermöglicht Ihnen festzulegen:

* Die Elemente, die im Dokument erscheinen können.
* Die Attribute, die Elemente haben können.
* Die Reihenfolge und Anzahl der untergeordneten Elemente innerhalb eines übergeordneten Elements.
* Die Datentypen von Elementen und Attributen.
* Einschränkungen für die Werte von Elementen und Attributen.

**`<sequence>` in XML Schema:**

Das `<sequence>`-Element ist ein Kompositor, der innerhalb von Complex-Type-Definitionen in XML Schema verwendet wird. Es gibt an, dass die darin enthaltenen untergeordneten Elemente **in der angegebenen Reihenfolge erscheinen müssen**.

**Syntax:**

```xml
<xs:complexType name="TypeName">
  <xs:sequence>
    <xs:element name="element1" type="xs:string" minOccurs="1" maxOccurs="1"/>
    <xs:element name="element2" type="xs:integer" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="element3" type="xs:date" minOccurs="1" maxOccurs="1"/>
  </xs:sequence>
</xs:complexType>
```

In diesem Beispiel muss jedes XML-Element, das dem Complex Type `TypeName` entspricht, Folgendes haben:

1.  Ein `<element1>`-Element (vom Typ string), das genau einmal erscheint.
2.  Null oder mehr `<element2>`-Elemente (vom Typ integer), die in Sequenz nach `<element1>` erscheinen.
3.  Ein `<element3>`-Element (vom Typ date), das genau einmal nach allen `<element2>`-Elementen erscheint.

**`minOccurs`- und `maxOccurs`-Attribute:**

Die Attribute `minOccurs` und `maxOccurs` werden innerhalb von Elementdeklarationen (normalerweise innerhalb eines `<sequence>`, `<choice>` oder `<all>` Kompositors) in XML Schema verwendet, um die minimale und maximale Anzahl anzugeben, wie oft ein Element erscheinen kann.

* **`minOccurs`:**
    * Gibt die Mindestanzahl an, wie oft das Element erscheinen muss.
    * Der Standardwert ist `1`.
    * Ein Wert von `0` zeigt an, dass das Element optional ist.
    * Eine positive Ganzzahl gibt die mindestens erforderlichen Vorkommen an.

* **`maxOccurs`:**
    * Gibt die maximale Anzahl an, wie oft das Element erscheinen kann.
    * Der Standardwert ist `1`.
    * Eine positive Ganzzahl gibt die maximal erlaubten Vorkommen an.
    * Der Wert `unbounded` zeigt an, dass das Element beliebig oft erscheinen kann (null oder mehr, wenn `minOccurs` 0 ist, eins oder mehr, wenn `minOccurs` 1 ist, usw.).

**Wie Sequence mit `minOccurs` und `maxOccurs` funktioniert:**

Wenn sich Elemente innerhalb einer `<sequence>` befinden, definieren die `minOccurs`- und `maxOccurs`-Attribute für jedes einzelne Element die zulässige Anzahl von Vorkommen *für dieses spezifische Element an dieser spezifischen Position innerhalb der Sequenz*. Die Reihenfolge der Elemente, wie in der `<sequence>` definiert, muss im XML-Instanzdokument eingehalten werden.

**Beispiel:**

Betrachten Sie den folgenden XML-Schema-Ausschnitt:

```xml
<xs:complexType name="OrderType">
  <xs:sequence>
    <xs:element name="orderId" type="xs:ID" minOccurs="1" maxOccurs="1"/>
    <xs:element name="customer" type="xs:string" minOccurs="1" maxOccurs="1"/>
    <xs:element name="item" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="orderDate" type="xs:date" minOccurs="1" maxOccurs="1"/>
  </xs:sequence>
</xs:complexType>
```

Ein XML-Dokument, das diesem Schema entspricht, hätte die folgende Struktur:

1.  **Genau ein** `<orderId>`-Element.
2.  **Genau ein** `<customer>`-Element, das unmittelbar nach `<orderId>` erscheint.
3.  **Null oder mehr** `<item>`-Elemente, die in Sequenz nach `<customer>` erscheinen.
4.  **Genau ein** `<orderDate>`-Element, das nach allen `<item>`-Elementen erscheint.

**Gültige XML-Instanz:**

```xml
<order>
  <orderId>ORD123</orderId>
  <customer>John Doe</customer>
  <item>Product A</item>
  <item>Product B</item>
  <orderDate>2025-03-29</orderDate>
</order>
```

**Eine weitere gültige XML-Instanz:**

```xml
<order>
  <orderId>ORD456</orderId>
  <customer>Jane Smith</customer>
  <orderDate>2025-03-28</orderDate>
</order>
```

**Ungültige XML-Instanz (Reihenfolge ist falsch):**

```xml
<order>
  <customer>John Doe</customer>
  <orderId>ORD123</orderId>
  <orderDate>2025-03-29</orderDate>
</order>
```

**Ungültige XML-Instanz (`orderId` fehlt):**

```xml
<order>
  <customer>John Doe</customer>
  <item>Product A</item>
  <orderDate>2025-03-29</orderDate>
</order>
**Zusammenfassend:**

* XML ist eine vielseitige Auszeichnungssprache zum Strukturieren und Transportieren von Daten.
* Sie beruht auf einer wohldefinierten Syntax und einer hierarchischen Struktur.
* XML Schema (XSD) bietet eine leistungsstarke Möglichkeit, die Struktur und den Inhalt von XML-Dokumenten zu definieren.
* Der `<sequence>`-Kompositor in XSD erzwingt eine bestimmte Reihenfolge für untergeordnete Elemente.
* Die Attribute `minOccurs` und `maxOccurs` legen die minimale und maximale Anzahl fest, wie oft ein Element in seinem definierten Kontext (oft innerhalb einer `<sequence>`) erscheinen kann.

Dieser Leitfaden bietet eine solide Grundlage für das Verständnis von XML und seinen Kernkonzepten, insbesondere der Rolle von `<sequence>`, `minOccurs` und `maxOccurs` bei der Definition der XML-Dokumentstruktur mit XML Schema. Denken Sie daran, für die detailliertesten und aktuellsten Informationen die offiziellen W3C-Spezifikationen zu konsultieren.
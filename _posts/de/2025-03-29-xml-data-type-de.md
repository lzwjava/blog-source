---
audio: false
generated: true
lang: de
layout: post
title: XML-Schema-Datentypen
translated: true
type: note
---

XML Schema definiert einen umfangreichen Satz integrierter Datentypen, die verwendet werden können, um die Art der in Elementen und Attributen zulässigen Daten festzulegen. Diese Datentypen stellen sicher, dass der XML-Inhalt dem beabsichtigten Format und den beabsichtigten Einschränkungen entspricht.

Die integrierten Datentypen in XML Schema werden grob in **primitive** und **abgeleitete** Typen kategorisiert. Abgeleitete Typen basieren auf primitiven Typen und werden durch das Anwenden von Einschränkungen oder anderen Modifikationen erstellt.

**Primitive Datentypen (19 integrierte):**

Dies sind die grundlegenden, unteilbaren Datentypen, von denen alle anderen integrierten und benutzerdefinierten einfachen Typen abgeleitet werden.

*   **String:** Stellt Zeichenketten dar.
*   **Boolean:** Stellt logische Werte dar (true oder false, kann auch als 1 oder 0 dargestellt werden).
*   **Decimal:** Stellt Dezimalzahlen mit beliebiger Genauigkeit dar.
*   **Float:** Stellt Gleitkommazahlen mit einfacher Genauigkeit (32-Bit) dar.
*   **Double:** Stellt Gleitkommazahlen mit doppelter Genauigkeit (64-Bit) dar.
*   **Duration:** Stellt ein Zeitintervall dar.
*   **DateTime:** Stellt einen bestimmten Zeitpunkt, inklusive Datum und Uhrzeit, dar.
*   **Time:** Stellt einen bestimmten Zeitpunkt innerhalb eines 24-Stunden-Zeitraums dar.
*   **Date:** Stellt ein Kalenderdatum dar.
*   **gYearMonth:** Stellt ein bestimmtes Jahr und einen bestimmten Monat dar.
*   **gYear:** Stellt ein bestimmtes Jahr dar.
*   **gMonthDay:** Stellt einen bestimmten Monat und Tag dar.
*   **gDay:** Stellt einen bestimmten Tag des Monats dar.
*   **gMonth:** Stellt einen bestimmten Monat des Jahres dar.
*   **HexBinary:** Stellt Binärdaten als Hexadezimalwerte dar.
*   **Base64Binary:** Stellt in Base64 kodierte Binärdaten dar.
*   **AnyURI:** Stellt einen Uniform Resource Identifier (URI) dar.
*   **QName:** Stellt einen qualifizierten Namen (einen Namen mit einem Namensraum-Präfix) dar.
*   **NOTATION:** Stellt den Namen einer im Schema deklarierten Notation dar.

**Abgeleitete Datentypen (etwa 25 integrierte):**

Diese Datentypen werden von den primitiven Typen abgeleitet, indem Einschränkungen (Facets) wie Länge, Bereich, Muster usw. angewendet werden.

**Abgeleitet von `string`:**

*   `normalizedString`: Stellt Zeichenketten dar, bei denen Zeilenumbrüche, Tabulatoren und Wagenrückläufe durch Leerzeichen ersetzt wurden und die keine führenden oder nachgestellten Leerzeichen haben.
*   `token`: Stellt normalisierte Zeichenketten ohne führende oder nachgestellte Leerzeichen und ohne interne Sequenzen von zwei oder mehr Leerzeichen dar.
*   `language`: Stellt eine Sprachkennung gemäß RFC 3066 dar.
*   `NMTOKEN`: Stellt ein Name Token dar (kann Buchstaben, Ziffern, Punkte, Bindestriche und Unterstriche enthalten).
*   `NMTOKENS`: Stellt eine durch Leerzeichen getrennte Liste von `NMTOKEN`s dar.
*   `Name`: Stellt einen XML-Namen dar (muss mit einem Buchstaben oder Unterstrich beginnen, gefolgt von Buchstaben, Ziffern, Punkten, Bindestrichen oder Unterstrichen).
*   `NCName`: Stellt einen nicht-kolonisierten Namen dar (wie `Name`, darf aber keinen Doppelpunkt enthalten).
*   `ID`: Stellt einen eindeutigen Bezeichner innerhalb eines XML-Dokuments dar.
*   `IDREF`: Stellt eine Referenz auf einen `ID`-Wert im selben Dokument dar.
*   `IDREFS`: Stellt eine durch Leerzeichen getrennte Liste von `IDREF`-Werten dar.
*   `ENTITY`: Stellt eine Referenz auf eine unparsed Entity dar, die in einer DTD deklariert ist (weniger gebräuchlich in XML Schema).
*   `ENTITIES`: Stellt eine durch Leerzeichen getrennte Liste von `ENTITY`-Werten dar (weniger gebräuchlich in XML Schema).

**Abgeleitet von `decimal`:**

*   `integer`: Stellt ganze Zahlen dar (kein Nachkommateil).
*   `nonPositiveInteger`: Stellt ganze Zahlen kleiner oder gleich 0 dar.
*   `negativeInteger`: Stellt ganze Zahlen strikt kleiner als 0 dar.
*   `long`: Stellt 64-Bit Ganzzahlen mit Vorzeichen dar.
*   `int`: Stellt 32-Bit Ganzzahlen mit Vorzeichen dar.
*   `short`: Stellt 16-Bit Ganzzahlen mit Vorzeichen dar.
*   `byte`: Stellt 8-Bit Ganzzahlen mit Vorzeichen dar.
*   `nonNegativeInteger`: Stellt ganze Zahlen größer oder gleich 0 dar.
*   `unsignedLong`: Stellt 64-Bit Ganzzahlen ohne Vorzeichen dar.
*   `unsignedInt`: Stellt 32-Bit Ganzzahlen ohne Vorzeichen dar.
*   `unsignedShort`: Stellt 16-Bit Ganzzahlen ohne Vorzeichen dar.
*   `unsignedByte`: Stellt 8-Bit Ganzzahlen ohne Vorzeichen dar.
*   `positiveInteger`: Stellt ganze Zahlen strikt größer als 0 dar.

**Andere abgeleitete Typen:**

*   `dateTimeStamp` (in XML Schema 1.1): Ähnlich wie `dateTime`, beinhaltet aber auch Zeitzoneninformationen.
*   `yearMonthDuration` (in XML Schema 1.1): Stellt eine Dauer in Jahren und Monaten dar.
*   `dayTimeDuration` (in XML Schema 1.1): Stellt eine Dauer in Tagen, Stunden, Minuten und Sekunden dar.
*   `precisionDecimal` (in XML Schema 1.1): Stellt Dezimalzahlen mit erhaltener Genauigkeit dar.

**Benutzerdefinierte Datentypen:**

Zusätzlich zu den integrierten Typen ermöglicht XML Schema die Definition eigener einfacher und komplexer Datentypen mithilfe von Mechanismen wie:

*   **Restriction:** Erstellen eines neuen Typs durch Einschränken des Bereichs oder Formats eines vorhandenen Typs (entweder integriert oder benutzerdefiniert).
*   **List:** Definieren eines Typs, dessen Werte Sequenzen von Werten eines anderen einfachen Typs sind.
*   **Union:** Definieren eines Typs, dessen Werte aus den Wertebereichen von zwei oder mehr anderen einfachen Typen stammen können.

Bei der Definition von Elementen und Attributen in einem XML Schema verwenden Sie das `type`-Attribut, um anzugeben, welchem Datentyp der Inhalt entsprechen soll. Dies gewährleistet die Datenvalidität und erleichtert die Datenverarbeitung.

Zum Beispiel:

```xml
<xs:element name="age" type="xs:positiveInteger"/>
<xs:element name="name" type="xs:string"/>
<xs:attribute name="status" type="xs:token"/>
```

In diesem Ausschnitt ist das `age`-Element so definiert, dass es eine positive Ganzzahl enthält, das `name`-Element eine Zeichenkette und das `status`-Attribut ein Token (eine normalisierte Zeichenkette mit spezifischer Behandlung von Leerzeichen).

Das Verständnis dieser Datentypen ist grundlegend für die Erstellung effektiver und wohldefinierter XML Schemas. Die vollständigen Details und formalen Definitionen finden Sie in der W3C XML Schema Part 2: Datatypes-Spezifikation.
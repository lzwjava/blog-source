---
audio: false
generated: true
lang: de
layout: post
title: Reguläre Ausdrücke
translated: true
type: note
---

Reguläre Ausdrücke, oft abgekürzt als "Regex" oder "Regexp", sind ein leistungsstarkes und vielseitiges Werkzeug für die Mustererkennung in Texten. Sie bieten eine prägnante und flexible Möglichkeit, Zeichenketten basierend auf definierten Mustern zu suchen, zu manipulieren und zu validieren. Auch wenn die Syntax zunächst entmutigend wirken kann, kann die Beherrschung von Regex Ihre Textverarbeitungsfähigkeiten in verschiedenen Programmiersprachen, Texteditoren und Kommandozeilen-Tools erheblich verbessern.

Dieser Leitfaden führt Sie von den Grundlagen zu fortgeschritteneren Konzepten der regulären Ausdrücke.

**I. Die Grundlagen: Bausteine von Regex**

Im Kern ist ein Regex eine Sequenz von Zeichen, die ein Suchmuster definiert. Diese Zeichen können literal (entsprechen sich selbst) oder speziell (haben spezifische Bedeutungen) sein.

**A. Literale Zeichen:**

Die meisten Zeichen in einem Regex entsprechen sich selbst wörtlich. Zum Beispiel:

* `abc` entspricht der exakten Sequenz "abc" in einer Zeichenkette.
* `123` entspricht der exakten Sequenz "123".
* `hello` entspricht der exakten Sequenz "hello".

**B. Metazeichen: Die besonderen Fähigkeiten**

Metazeichen sind die Bausteine, die Regex seine Kraft verleihen. Sie haben spezielle Bedeutungen und entsprechen nicht sich selbst wörtlich. Hier sind die gebräuchlichsten:

1.  **`.` (Punkt):** Entspricht einem beliebigen einzelnen Zeichen *außer* einem Zeilenumbruchzeichen (standardmäßig `\n`).
    * `a.c` entspricht "abc", "adc", "a1c", "a c", aber nicht "ac" oder "abbc".

2.  **`^` (Zirkumflex):**
    * **Innerhalb einer Zeichenklasse (siehe unten):** Negiert die Menge, entspricht jedem Zeichen, das *nicht* in der Menge ist.
    * **Außerhalb einer Zeichenklasse:** Entspricht dem Anfang einer Zeichenkette (oder dem Anfang einer Zeile im Multiline-Modus).
        * `^hello` entspricht "hello world", aber nicht "say hello".

3.  **`$` (Dollarzeichen):** Entspricht dem Ende einer Zeichenkette (oder dem Ende einer Zeile im Multiline-Modus).
    * `world$` entspricht "hello world", aber nicht "world hello".

4.  **`*` (Sternchen):** Entspricht dem vorhergehenden Zeichen oder der Gruppe null oder mehr Mal.
    * `ab*c` entspricht "ac", "abc", "abbc", "abbbc" und so weiter.

5.  **`+` (Pluszeichen):** Entspricht dem vorhergehenden Zeichen oder der Gruppe ein oder mehr Mal.
    * `ab+c` entspricht "abc", "abbc", "abbbc", aber nicht "ac".

6.  **`?` (Fragezeichen):**
    * Entspricht dem vorhergehenden Zeichen oder der Gruppe null oder ein Mal (macht es optional).
        * `ab?c` entspricht "ac" und "abc", aber nicht "abbc".
    * Wird als Quantifizierer-Modifikator verwendet, um eine Übereinstimmung nicht-gierig zu machen (siehe Abschnitt Quantifizierer).

7.  **`{}` (Geschweifte Klammern):** Gibt die exakte Anzahl oder den Bereich der Vorkommen des vorhergehenden Zeichens oder der Gruppe an.
    * `a{3}` entspricht genau drei "a"s (z.B. "aaa").
    * `a{2,4}` entspricht zwischen zwei und vier "a"s (z.B. "aa", "aaa", "aaaa").
    * `a{2,}` entspricht zwei oder mehr "a"s (z.B. "aa", "aaa", "aaaa", ...).

8.  **`[]` (Eckige Klammern):** Definiert eine Zeichenmenge, entspricht einem beliebigen einzelnen Zeichen innerhalb der Klammern.
    * `[abc]` entspricht entweder "a", "b" oder "c".
    * `[a-z]` entspricht einem beliebigen Kleinbuchstaben von "a" bis "z" (Bereich).
    * `[0-9]` entspricht einer beliebigen Ziffer von "0" bis "9".
    * `[A-Za-z0-9]` entspricht einem beliebigen alphanumerischen Zeichen.
    * `[^abc]` (mit `^` am Anfang) entspricht jedem Zeichen *außer* "a", "b" oder "c".

9.  **`\` (Backslash):** Maskiert das nächste Zeichen, behandelt ein Metazeichen als literales Zeichen oder führt eine spezielle Zeichensequenz ein.
    * `\.` entspricht einem wörtlichen Punkt ".".
    * `\*` entspricht einem wörtlichen Sternchen "*".
    * `\d` entspricht einer beliebigen Ziffer (äquivalent zu `[0-9]`).
    * `\D` entspricht einem beliebigen Nicht-Ziffer-Zeichen (äquivalent zu `[^0-9]`).
    * `\s` entspricht einem beliebigen Leerzeichen (Leerzeichen, Tabulator, Zeilenumbruch usw.).
    * `\S` entspricht einem beliebigen Nicht-Leerzeichen-Zeichen.
    * `\w` entspricht einem beliebigen Wortzeichen (alphanumerisch und Unterstrich, äquivalent zu `[a-zA-Z0-9_]`).
    * `\W` entspricht einem beliebigen Nicht-Wort-Zeichen (äquivalent zu `[^a-zA-Z0-9_]`).
    * `\b` entspricht einer Wortgrenze (die Position zwischen einem Wortzeichen und einem Nicht-Wort-Zeichen).
    * `\B` entspricht einer Nicht-Wortgrenze.
    * `\n` entspricht einem Zeilenumbruchzeichen.
    * `\r` entspricht einem Wagenrücklaufzeichen.
    * `\t` entspricht einem Tabulatorzeichen.

10. **`|` (Pipe-Symbol):** Fungiert als "ODER"-Operator, entspricht entweder dem Ausdruck vor oder dem Ausdruck nach der Pipe.
    * `cat|dog` entspricht entweder "cat" oder "dog".

11. **`()` (Runde Klammern):**
    * **Gruppierung:** Fasst Teile eines Regex zusammen, sodass Sie Quantifizierer oder den ODER-Operator auf die gesamte Gruppe anwenden können.
        * `(ab)+c` entspricht "abc", "ababc", "abababc" und so weiter.
        * `(cat|dog) food` entspricht "cat food" oder "dog food".
    * **Erfassungsgruppen:** Erfasst den Text, der durch den Ausdruck innerhalb der Klammern abgeglichen wurde. Diese erfassten Gruppen können später referenziert werden (z.B. für Ersetzung oder Extraktion).

**II. Quantifizierer: Steuerung der Wiederholung**

Quantifizierer geben an, wie oft ein vorhergehendes Element (Zeichen, Gruppe oder Zeichenmenge) vorkommen kann.

* `*`: Null oder mehr Mal
* `+`: Ein oder mehr Mal
* `?`: Null oder ein Mal
* `{n}`: Genau `n` Mal
* `{n,}`: `n` oder mehr Mal
* `{n,m}`: Zwischen `n` und `m` Mal (inklusive)

**Gierige vs. Nicht-Gierige Übereinstimmung:**

Standardmäßig sind Quantifizierer **gierig**, was bedeutet, dass sie versuchen, so viel wie möglich von der Zeichenkette zu erfassen. Sie können einen Quantifizierer **nicht-gierig** (oder faul) machen, indem Sie ein `?` dahinter setzen. Nicht-gierige Quantifizierer versuchen, die kürzestmögliche Zeichenkette zu erfassen.

* `a.*b` (gierig) auf "axxbxb" wird "axxbxb" entsprechen.
* `a.*?b` (nicht-gierig) auf "axxbxb" wird "axb" und dann "xb" entsprechen.

**III. Anker: Angeben der Position**

Anker entsprechen selbst keinen Zeichen, sondern bestätigen eine Position innerhalb der Zeichenkette.

* `^`: Entspricht dem Anfang der Zeichenkette (oder Zeile).
* `$`: Entspricht dem Ende der Zeichenkette (oder Zeile).
* `\b`: Entspricht einer Wortgrenze.
* `\B`: Entspricht einer Nicht-Wortgrenze.

**IV. Zeichenklassen: Vordefinierte Mengen**

Zeichenklassen bieten Kurzschreibweisen für häufig verwendete Zeichenmengen.

* `\d`: Entspricht einer beliebigen Ziffer (0-9).
* `\D`: Entspricht einem beliebigen Nicht-Ziffer-Zeichen.
* `\s`: Entspricht einem beliebigen Leerzeichen (Leerzeichen, Tabulator, Zeilenumbruch, Wagenrücklauf, Seitenvorschub).
* `\S`: Entspricht einem beliebigen Nicht-Leerzeichen-Zeichen.
* `\w`: Entspricht einem beliebigen Wortzeichen (alphanumerisch und Unterstrich: a-zA-Z0-9_).
* `\W`: Entspricht einem beliebigen Nicht-Wort-Zeichen.

**V. Gruppierung und Erfassung**

Runde Klammern `()` dienen zwei Hauptzwecken:

* **Gruppierung:** Ermöglicht es Ihnen, Quantifizierer oder den ODER-Operator auf eine Sequenz von Zeichen anzuwenden.
* **Erfassung:** Erstellt eine Erfassungsgruppe, die den Teil der Zeichenkette speichert, der dem Ausdruck innerhalb der Klammern entspricht. Diese erfassten Gruppen können für Backreferences oder Ersetzungen abgerufen und verwendet werden.

**Backreferences:**

Sie können innerhalb desselben Regex mit `\1`, `\2`, `\3` usw. auf zuvor erfasste Gruppen verweisen, wobei die Zahl der Reihenfolge der öffnenden Klammer der Erfassungsgruppe entspricht.

* `(.)\1` entspricht einem beliebigen Zeichen, gefolgt vom selben Zeichen (z.B. "aa", "bb", "11").
* `(\w+) \1` entspricht einem Wort, gefolgt von einem Leerzeichen und dann demselben Wort (z.B. "hello hello").

**Nicht-Erfassende Gruppen:**

Wenn Sie Teile eines Regex gruppieren müssen, ohne eine Erfassungsgruppe zu erstellen, können Sie `(?:...)` verwenden. Dies ist nützlich für Übersichtlichkeit oder Leistungsgründe.

* `(?:ab)+c` entspricht "abc", "ababc" usw., erfasst aber nicht "ab".

**VI. Lookarounds: Assertions ohne Konsumierung**

Lookarounds sind Null-Breiten-Assertions, die auf ein Muster vor oder nach der aktuellen Position in der Zeichenkette prüfen, ohne den übereinstimmenden Lookaround-Teil in die Gesamtübereinstimmung einzuschließen.

* **Positiver Lookahead `(?=...)`:** Stellt sicher, dass das Muster innerhalb der Klammern der aktuellen Position folgen muss.
    * `\w+(?=:)` entspricht jedem Wort, dem ein Doppelpunkt folgt, aber der Doppelpunkt selbst ist nicht Teil der Übereinstimmung (z.B. in "name:" entspricht es "name").

* **Negativer Lookahead `(?!...)`:** Stellt sicher, dass das Muster innerhalb der Klammern der aktuellen Position *nicht* folgen darf.
    * `\w+(?!:)` entspricht jedem Wort, dem kein Doppelpunkt folgt (z.B. in "name value" entspricht es "name" und "value").

* **Positiver Lookbehind `(?<=...)`:** Stellt sicher, dass das Muster innerhalb der Klammern der aktuellen Position vorausgehen muss. Das Muster innerhalb des Lookbehind muss eine feste Breite haben (keine variablen Quantifizierer wie `*` oder `+`).
    * `(?<=\$)\d+` entspricht einer oder mehreren Ziffern, denen ein Dollarzeichen vorausgeht, aber das Dollarzeichen selbst ist nicht Teil der Übereinstimmung (z.B. in "$100" entspricht es "100").

* **Negativer Lookbehind `(?<!...)`:** Stellt sicher, dass das Muster innerhalb der Klammern der aktuellen Position *nicht* vorausgehen darf. Das Muster innerhalb des Lookbehind muss eine feste Breite haben.
    * `(?<!\$)\d+` entspricht einer oder mehreren Ziffern, denen kein Dollarzeichen vorausgeht (z.B. in "100$" entspricht es "100").

**VII. Flags (Modifikatoren): Steuerung des Regex-Verhaltens**

Flags (oder Modifikatoren) werden verwendet, um das Verhalten der Regex-Engine zu ändern. Sie werden je nach Implementierung normalerweise am Anfang oder Ende des Regex-Musters angegeben. Häufige Flags sind:

* **`i` (Groß-/Kleinschreibung ignorieren):** Macht die Übereinstimmung unabhängig von Groß-/Kleinschreibung. `[a-z]` entspricht sowohl Klein- als auch Großbuchstaben.
* **`g` (Global):** Findet alle Übereinstimmungen in der Zeichenkette, nicht nur die erste.
* **`m` (Multiline):** Bewirkt, dass `^` und `$` den Anfang und das Ende jeder Zeile (begrenzt durch `\n` oder `\r`) entsprechen, anstatt nur dem Anfang und Ende der gesamten Zeichenkette.
* **`s` (Dotall/Single line):** Bewirkt, dass das Metazeichen `.` jedem Zeichen entspricht, einschließlich Zeilenumbruchzeichen.
* **`u` (Unicode):** Aktiviert die vollständige Unicode-Unterstützung für Zeichenklassen und andere Funktionen.
* **`x` (Erweitert/Ausführlich):** Ermöglicht das Schreiben von besser lesbaren Regex, indem Leerzeichen und Kommentare innerhalb des Musters ignoriert werden (nützlich für komplexe Regex).

**VIII. Praktische Anwendungen von Regex**

Regex wird in verschiedenen Bereichen umfassend eingesetzt:

* **Texteditoren (z.B. Notepad++, Sublime Text, VS Code):** Suchen und Ersetzen von Text basierend auf Mustern.
* **Programmiersprachen (z.B. Python, JavaScript, Java, C#):**
    * Validieren von Benutzereingaben (z.B. E-Mail-Adressen, Telefonnummern, URLs).
    * Extrahieren spezifischer Informationen aus Text (z.B. Daten, Zahlen, Tags).
    * Ersetzen von Teilen einer Zeichenkette basierend auf einem Muster.
    * Parsen von Logdateien oder anderen strukturierten Textdaten.
* **Kommandozeilen-Tools (z.B. `grep`, `sed`, `awk`):** Durchsuchen und Manipulieren von Textdateien.
* **Webentwicklung:** Formularvalidierung, URL-Routing, Inhaltsverarbeitung.
* **Data Science:** Datenbereinigung, Datenextraktion, Mustererkennung.
* **Sicherheit:** Eindringlingserkennung, Loganalyse.

**IX. Regex in verschiedenen Programmiersprachen**

Die meisten modernen Programmiersprachen haben eingebaute Unterstützung für reguläre Ausdrücke, obwohl die spezifische Syntax und die Funktionen leicht variieren können. Sie finden die Regex-Funktionalität typischerweise in Standardbibliotheken oder Modulen.

* **Python:** Das `re`-Modul.
* **JavaScript:** Eingebautes `RegExp`-Objekt und String-Methoden wie `match()`, `replace()`, `search()`, `split()`.
* **Java:** Das Paket `java.util.regex`.
* **C# (.NET):** Der Namensraum `System.Text.RegularExpressions`.
* **PHP:** Funktionen wie `preg_match()`, `preg_replace()`, `preg_match_all()`.

**X. Tipps zum Schreiben effektiver Regex**

* **Fangen Sie einfach an:** Beginnen Sie mit einem grundlegenden Muster und fügen Sie schrittweise Komplexität hinzu.
* **Testen Sie häufig:** Verwenden Sie Online-Regex-Tester oder die Regex-Tools Ihrer Programmiersprache, um Ihre Muster anhand von Beispieldaten zu testen.
* **Seien Sie spezifisch:** Vermeiden Sie zu breite Muster, die unbeabsichtigten Text erfassen könnten.
* **Verwenden Sie Zeichenklassen und Quantifizierer mit Bedacht:** Sie sind leistungsstark, können aber bei falscher Anwendung zu unerwartetem Verhalten führen.
* **Verstehen Sie gierige vs. nicht-gierige Übereinstimmung:** Wählen Sie das geeignete Verhalten für Ihre Bedürfnisse.
* **Verwenden Sie Gruppierung und Erfassung umsichtig:** Erfassen Sie nur das, was Sie benötigen. Verwenden Sie nicht-erfassende Gruppen, wenn keine Erfassung erforderlich ist.
* **Dokumentieren Sie Ihren Regex:** Fügen Sie für komplexe Muster Kommentare hinzu (insbesondere bei Verwendung des `x`-Flags), um deren Zweck zu erklären.
* **Berücksichtigen Sie Randfälle:** Denken Sie über verschiedene Variationen des Eingabetextes nach und stellen Sie sicher, dass Ihr Regex diese korrekt verarbeitet.
* **Brechen Sie komplexe Probleme auf:** Wenn Sie eine sehr komplexe Abgleichsaufgabe haben, ziehen Sie in Betracht, sie in mehrere einfachere Regex-Muster aufzuteilen.

**XI. Lernressourcen**

* **Online-Regex-Tester:** regex101.com, regexr.com, regextester.com
* **Sprachspezifische Dokumentation:** Konsultieren Sie die Regex-Dokumentation für Ihre gewählte Programmiersprache.
* **Online-Tutorials und Kurse:** Plattformen wie Coursera, Udemy und YouTube bieten umfassende Regex-Kurse an.
* **Bücher:** "Mastering Regular Expressions" von Jeffrey Friedl ist eine sehr empfehlenswerte Ressource.

**Schlussfolgerung**

Reguläre Ausdrücke sind ein unverzichtbares Werkzeug für alle, die mit Textdaten arbeiten. Auch wenn die anfängliche Lernkurve steil erscheinen mag, ist die Fähigkeit, Text basierend auf komplexen Mustern effizient zu suchen, zu manipulieren und zu validieren, eine wertvolle Fertigkeit. Durch das Verständnis der grundlegenden Konzepte, Metazeichen, Quantifizierer und anderer Funktionen von Regex können Sie Ihre Produktivität und Problemlösungsfähigkeiten in einer Vielzahl von Anwendungen erheblich steigern. Übung ist der Schlüssel zur Beherrschung von Regex, also zögern Sie nicht, verschiedene Muster für verschiedene Textverarbeitungsaufgaben zu experimentieren und zu erkunden.
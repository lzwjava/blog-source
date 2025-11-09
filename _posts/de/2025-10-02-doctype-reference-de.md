---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: CodeIgniter DOCTYPE-Deklarationsreferenz
translated: true
type: note
---

### Übersicht
Dies ist ein PHP-Array aus dem CodeIgniter-Framework (einem Open-Source-Webanwendungs-Framework), das DOCTYPE-Deklarationen für verschiedene Auszeichnungssprachen definiert. Eine DOCTYPE ist eine Dokumenttyp-Deklaration, die Browser und Validatoren über die Version und den Standard der in einem HTML-Dokument verwendeten Auszeichnungssprache informiert. Sie stellt ein korrektes Rendering und eine korrekte Validierung sicher. Diese Deklarationen basieren auf offiziellen W3C-Standards. Im Folgenden werde ich sie thematisch gruppiert erklären, einschließlich ihres Zwecks und typischer Anwendungsfälle.

### XHTML-Doctypes
XHTML (Extensible HyperText Markup Language) ist HTML, das als XML neu formuliert wurde und eine strengere Syntax erzwingt (z.B. erforderliche schließende Tags und Kleinbuchstaben für Elemente).
- **xhtml11**: Deklariert XHTML 1.1, die neueste XHTML-Version mit modularen Funktionen für fortgeschrittene Web-Apps. Streng, XML-konform; verwendet für moderne, semantische Webseiten ohne Frames oder veraltete Elemente.
- **xhtml1-strict**: XHTML 1.0 Strict; erzwingt sauberes, semantisches Markup ohne veraltete Elemente (z.B. kein `<font>`). Ideal für standardkonforme Seiten, die Abwärtskompatibilität benötigen.
- **xhtml1-trans**: XHTML 1.0 Transitional; erlaubt einige Legacy-HTML-Elemente für eine einfachere Migration von HTML 3.2/4.0. Nützlich für bestehende Seiten, die altes und neues Markup mischen.
- **xhtml1-frame**: XHTML 1.0 Frameset; unterstützt Framed-Layouts mit `<frameset>`. Veraltet im modernen Webdesign aufgrund von Usability-Problemen und SEO-Nachteilen.
- **xhtml-basic11**: XHTML Basic 1.1; ein schlankes Profil für mobile Geräte und einfache Anwendungen, das fortgeschrittene Funktionen wie Formulare oder Stylesheets ausschließt.

### HTML-Doctypes
HTML ist die Standard-Auszeichnungssprache für Webseiten, die sich von lockeren zu strengen Standards entwickelt hat.
- **html5**: Der moderne HTML5-DOCTYPE; einfach und zukunftssicher, wird von allen Browsern im Standards-Modus geparst. Unterstützt Multimedia, APIs und semantische Elemente (z.B. `<article>`, `<header>`). Empfohlen für neue Websites.
- **html4-strict**: HTML 4.01 Strict; erzwingt semantische Strenge ohne veraltete Elemente. Wird in Legacy-Projekten verwendet, die strikte Compliance erfordern.
- **html4-trans**: HTML 4.01 Transitional; permissiv, erlaubt Legacy-Tags für schrittweise Updates. Üblich in älteren Seiten, die auf Standards umgestellt werden.
- **html4-frame**: HTML 4.01 Frameset; für Seiten mit Frames, jetzt veraltet aufgrund langsamer Ladezeiten und Barrierefreiheitsproblemen.

### MathML-Doctypes
MathML (Mathematical Markup Language) ermöglicht die Darstellung mathematischer Notationen im Web.
- **mathml1**: MathML 1.0; grundlegendes Math-Rendering im XML-Format. Wird in Bildungstools oder Dokumenten mit einfachen Gleichungen verwendet.
- **mathml2**: MathML 2.0; erweiterte Unterstützung für komplexe Mathematik, besser integriert mit anderen Auszeichnungssprachen. Grundlage für die moderne mathematische Darstellung im Web.

### SVG-Doctypes
SVG (Scalable Vector Graphics) definiert Vektorgrafiken in XML für Webgrafiken.
- **svg10**: SVG 1.0; grundlegende 2D-Vektorgrafiken. Wird für statische Illustrationen verwendet.
- **svg11**: SVG 1.1; vollständige 2D-Grafiken mit Animationen und Filtern. Standard für dynamische Webgrafiken.
- **svg11-basic**: SVG 1.1 Basic; mobiles Subset mit weniger Funktionen. Für schlankes SVG auf Geräten.
- **svg11-tiny**: SVG 1.1 Tiny; minimales Profil für Geräte mit geringer Leistung wie Telefone. Unterstützt grundlegende Formen und Animationen.

### Zusammengesetzte Doctypes
Diese kombinieren mehrere Standards für umfangreiche Multimedia-Inhalte.
- **xhtml-math-svg-xh**: XHTML 1.1 mit MathML 2.0 und SVG 1.1; für Dokumente, die Text, Mathematik und Grafiken mischen (z.B. wissenschaftliche Arbeiten).
- **xhtml-math-svg-sh**: Ähnlich dem obigen, aber in SVG verwurzelt (`<svg:svg>`), für SVG-dominierte Dokumente mit eingebettetem XHTML und MathML.
- **xhtml-rdfa-1**: XHTML mit RDFa 1.0 (Resource Description Framework in Attributen); verbessert das Einbetten semantischer Webdaten für metadata-reiche Seiten.
- **xhtml-rdfa-2**: XHTML mit RDFa 1.1; verbessertes RDFa zum Verknüpfen von Daten in HTML-Attributen, verwendet in Web-of-Data-Anwendungen.

### Verwendungshinweise
- Diese sind in CodeIgniter vordefiniert für eine einfache Einfügung über seine `doctype()`-Hilfsfunktion.
- Moderne Webentwicklung bevorzugt HTML5 (`html5`) aufgrund seiner Flexibilität und Browserunterstützung. Ältere Doctypes (z.B. HTML 4 oder Versionen mit Frames) sind größtenteils veraltet.
- Belegt durch W3C-Spezifikationen (z.B. w3.org/TR/html5/, w3.org/TR/xhtml11/) stellen diese ein konsistentes Parsing sicher: Browser verwenden sie, um den Standards- oder Quirks-Modus auszulösen, was Layout und Skripte beeinflusst. Wählen Sie basierend auf den Markup-Anforderungen Ihres Projekts für die beste Validierung (über Tools wie den W3C-Validator). Wenn Sie in CodeIgniter arbeiten, verwenden Sie den Array-Schlüssel in Ihren Views, um die Deklaration auszugeben.
---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Konfigurationsdateien entwickeln sich zu schlechten Sprachen
translated: true
type: note
---

### Die Erklärung des "Gesetzes der unzerstörbaren Logik" und warum Konfigurationsdateien zu schlechten Programmiersprachen werden

Der Beitrag, auf den Sie sich beziehen, stammt von Yining Wang (auch bekannt als Yin Wang), einem Informatiker und Blogger. Es ist ein durchdachter Artikel, der auf einer Beobachtung der Programmierlegende Guy Steele aufbaut: **Wenn Konfigurationsdateien komplexer werden, entwickeln sie sich unweigerlich zu einer schlechten Programmiersprache**. Wang verwendet ein von ihm geprägtes Konzept – das "Gesetz der unzerstörbaren Logik" –, um zu erklären, *warum* dies fast jedes Mal passiert. Es ist eine kluge Analogie zur Energieerhaltung in der Physik: Logik verschwindet nicht; sie verlagert sich nur.

#### Was ist das "Gesetz der unzerstörbaren Logik"?
Wang definiert es einfach: **Die Logik, die Menschen ausdrücken müssen, wird immer irgendwo auftauchen, und zwar in im Wesentlichen derselben Form.**

- Im Grunde genommen bedeutet das: Wenn es eine Entscheidungsfindung oder regelbasierte Denkweise gibt (z. B. "Wenn diese Bedingung wahr ist, dann mache das"), *muss* diese in Ihrem System auftauchen. Sie wird nicht einfach verschwinden, nur weil Sie versuchen, sie zu verstecken oder auszulagern.
- Diese Logik könnte in Ihrem Hauptprogrammcode, einer Konfigurationsdatei, einer Tabellenkalkulation oder sogar einer Skizze auf einem Whiteboard landen – aber sie bleibt bestehen, unverändert in ihrer Kernstruktur.
- Sie ist "unzerstörbar", weil menschliche Bedürfnisse (wie die Anpassung von Verhalten) sie erfordern. Wenn man dies ignoriert, führt das zu umständlichen Workarounds.

Stellen Sie es sich wie Wasser vor, das sein Niveau findet: Die Logik fließt dorthin, wo sie gebraucht wird, egal wie sehr man versucht, sie einzudämmen.

#### Wie erklärt das, warum Konfigurationsdateien zu "schlechten Sprachen" werden?
Konfigurationsdateien beginnen harmlos – als eine Möglichkeit, Einstellungen anzupassen, ohne den Kerncode zu berühren. Aber wenn die Anforderungen wachsen, blähen sie sich zu etwas Bösartigerem auf. Hier ist die schrittweise Aufschlüsselung, bezogen auf das Gesetz:

1.  **Der einfache Start: Nur Variablen**
    Zunächst sind Konfigurationen einfache Schlüssel-Wert-Paare:
    - `enable_optimization = true`
    - `max_requests = 1000`
    Diese sind wie "Variablen" in der Programmierung (z. B. `let x = 5;`). Das Programm liest sie und setzt die Werte in seine eigene Logik ein.
    *Warum?* Noch keine tiefgreifende Logik – nur Platzhalter. Aber Variablen sind ein grundlegender Baustein *jeder* Programmiersprache. Dem Gesetz nach hat sich diese Logik (das Zuweisen und Verwenden von Werten) bereits in die Konfiguration eingeschlichen.

2.  **Die schleichende Entwicklung: Hinzufügen von Verzweigungen**
    Wenn Benutzer mehr Flexibilität verlangen (z. B. "Aktiviere Funktion X nur für Premium-Benutzer"), beginnen Entwickler, *bedingte Logik* in die Konfiguration einzubetten:
    - So etwas wie: `if user_type == "premium" then enable_feature_X else disable`.
    Das ist eindeutig "if-then-else"-Verzweigung – ein weiterer Kernbestandteil der Programmierung.
    *Warum?* Entwickler verlagern die Logik unbewusst vom Hauptcode in die Konfiguration, um sie leichter anpassen zu können. Aber das Gesetz greift: Die Logik verschwindet nicht aus dem Programm; sie wandert nur aus. Jetzt ist die Konfiguration nicht mehr nur Daten – sie trifft Entscheidungen.

3.  **Der Wendepunkt: Voll ausgereizte Logik**
    Mit der Zeit sammeln Konfigurationen Schleifen, Funktionen, Fehlerbehandlung und benutzerdefinierte Regeln. Was als flache Datei (YAML, JSON, etc.) begann, endet mit einer Syntax, die Turing-vollständig ist (in der Lage, jede Berechnung auszudrücken).
    - Ergebnis: Eine "Sprache", die mächtig, aber furchtbar ist – es fehlen gute Tools, Fehlermeldungen, Debugging-Möglichkeiten oder Bibliotheken. Es ist, als würde man in einem halbgar programmierten Code-Dialekt programmieren.
    *Warum unvermeidlich?* Die Unzerstörbarkeit der Logik. Wenn die Logik existiert (und das muss sie, um reale Probleme zu lösen), wird sie sich *irgendwo* manifestieren. Sie aus dem Hauptcode zu verbannen, schiebt sie in die Konfiguration, wo sie vor sich hin gärt.

Steeles Spott bringt es auf den Punkt: Konfigurationen *wollen* keine Sprachen sein, aber die Komplexität zwingt sie dazu. Und sie sind immer "schlecht", weil sie für Einfachheit und nicht für Ausdrucksstärke designed wurden.

#### Bezug zu domänenspezifischen Sprachen (DSLs)
Wang bezieht sich auf seinen früheren Essay ["The Pitfalls of DSLs"](https://yinwang1.substack.com/p/dsl-misconceptions) (insbesondere den Abschnitt "Dynamic Logic Loading"), um dies zu erweitern. Viele DSLs (benutzerdefinierte Mini-Sprachen für bestimmte Aufgaben) entstehen aus demselben Drang heraus: Regeln oder Verhalten zur Laufzeit zu laden, ohne neu kompilieren zu müssen.

- **Der Fehler:** Teams denken, sie bräuchten eine maßgeschneiderte Sprache für "dynamische Logik", also erfinden sie eine – und erfinden "if-then-else" in einer umständlichen Hülle neu.
- **Die Lösung:** Meistens läuft dies auf einfache Bedingungen hinaus. Bettet man einfach Code-Snippets einer bestehenden Sprache (z. B. JavaScripts `if`-Anweisungen) in die Konfiguration ein. Es ist nicht nötig, eine ganz neue DSL zu erfinden – das ist übertrieben und führt in dieselbe "schlechte Sprache"-Falle.
- *Das Gesetz in Aktion:* Die Logik (z. B. "prüfe ob X, dann Y") musste irgendwo hin. Ein Snippet in JS belässt sie in einer *guten* Sprache und vermeidet so aufgeblähte Konfigurationen.

#### Warum ist das wichtig?
Das ist nicht nur Theorie – es ist eine Warnung für das Software-Design. Es erklärt, warum sich Tools wie Kubernetes YAML oder Webpack-Konfigurationen wie Programmier-Albträume anfühlen. Die Lehre? Man sollte die Logik dort willkommen heißen, wo sie gedeiht (in richtigen Sprachen), anstatt sie in Konfigurationen zu verbannen. Man sollte Systeme so gestalten, dass Logik *sichtbar und handhabbar* ist, sonst wird sie einen in spektraler Form heimsuchen.

Wenn Sie mehr erfahren möchten, ist der vollständige Beitrag eine kurze Lektüre mit mehr Nuancen.

[Originalbeitrag: Configuration Files and the Logic Indestructibility Law](https://yinwang1.substack.com/p/224)
[Verwandter Beitrag: The Pitfalls of DSLs](https://yinwang1.substack.com/p/dsl-misconceptions)
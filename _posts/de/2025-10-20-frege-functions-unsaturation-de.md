---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Frege über Funktionen und Ungesättigtheit
translated: true
type: note
---

### Was sagt Freges Aufsatz „Was ist eine Funktion?“ aus dem Jahr 1904?

Gottlob Freges kurzer Aufsatz, ursprünglich mit dem Titel *Was ist eine Funktion?* veröffentlicht in einer Festschrift für den Physiker Ludwig Boltzmann, ist eine prägnante Klärung der logischen Natur von Funktionen in der Mathematik. Verfasst in einer späten Phase von Freges Karriere (nach seinen Hauptwerken wie *Grundlagen der Arithmetik* und *Grundgesetze der Arithmetik*), reagiert er auf anhaltende Verwirrungen in der mathematischen Praxis und Didaktik – ähnlich den von Ihnen beschriebenen Problemen mit Studierenden, die grafische Gleichungen (y = x² + 3x) und Funktionsnotation (f(x) = x² + 3x) vermischen. Frege schreibt hier keine Mathematiklehrbücher um, sondern seziert, warum diese Notationen in die Irre führen, und bietet eine präzise logische Grundlage dafür, was Funktionen *wirklich* sind. Der Aufsatz ist im Deutschen nur etwa 8 Seiten lang, und seine englische Übersetzung (von Peter Geach) erscheint in Sammelbänden wie *Collected Papers on Mathematics, Logic, and Philosophy*.

#### Wichtige Argumente und Struktur
Frege beginnt damit, den intuitiven Erfolg der Funktionsnotation in der Mathematik (z.B. sin x, log x oder x²) anzuerkennen, argumentiert aber, dass nachlässiger Gebrauch tiefere logische Probleme verbirgt. Er baut auf seinen früheren Ideen aus „Funktion und Begriff“ (1891) auf, wo er Funktionen erstmals als Bausteine der Logik behandelte und nicht nur als arithmetische Werkzeuge. Der Aufsatz hat drei Hauptstränge:

1.  **Die ungesättigte Natur von Funktionen**:
    - Frege besteht darauf, dass eine Funktion kein vollständiges „Ding“ wie eine Zahl oder ein Objekt ist – sie ist *ungesättigt* (oder „unvollständig“). Man kann sie sich als eine Lücke vorstellen, die gefüllt werden muss: Der Ausdruck ξ² + 3ξ (mit ξ als Platzhalter) bezeichnet die Funktion selbst, kann aber nicht allein als sinnvolle Entität stehen. Erst wenn man ein Argument einsetzt (z.B. ξ durch 2 ersetzt), „sättigt“ sie sich und liefert einen Wert (wie 2² + 3·2 = 10).
    - Dies steht im Gegensatz zum alltäglichen Mathematikunterricht, wo y = x² + 3x als „die Funktion“ präsentiert wird, die y gleichgesetzt wird (einem vollständigen Wert). Frege sagt, dass dies die Grenzen verwischt: Die linke Seite (y) ist gesättigt (ein Objekt), aber die rechte Seite ist ungesättigt, bis x spezifiziert ist. Die Notation verleitet uns dazu, die Funktion wie eine statische Formel zu behandeln und ihre dynamische, logische Rolle zu ignorieren.

2.  **Kritik am traditionellen mathematischen Gebrauch**:
    - Frege zielt auf den von Ihnen erwähnten historischen Wandel ab – von grafischem y = f(x) zu abstraktem f(x) – als Symptom tieferer Fehler. Die frühe Mathematik (z.B. in Eulers Zeit) sah Funktionen als Kurven oder Regeln, aber zu Freges Zeit hatte sich Dirichlets Definition (eine Funktion als beliebige Zuordnung zwischen Definitionsbereich und Wertebereich) durchgesetzt. Frege stimmt der extensionellen Idee zu (Funktionen werden durch ihr Eingabe-Ausgabe-Verhalten definiert), kritisiert aber, wie mit Variablen unsauber umgegangen wird.
    - Variablen sind keine „veränderlichen Größen“ (eine gängige pädagogische Legende); sie sind Platzhalter in Ausdrücken. Das Entfernen einer Variablen aus 2x³ + x, um „die Funktion zu erhalten“ (wie 2( )³ + ( )), scheitert bei Fällen mit mehreren Argumenten, wo die Stellen das *gleiche* Argument (wie in x³ + x) oder *verschiedene* Argumente (x³ + y) benötigen können. Dies führt zu Verwirrung bei der Bindung von Variablen und der Darstellung komplexer Funktionen.
    - Er erwähnt auch das „Begriffs-Pferd“-Paradoxon (aus seinem Aufsatz von 1892): So wie man keinen eigentlichen Namen wie „der Begriff Pferd“ bilden kann (indem man einen prädikativen Begriff als Objekt behandelt), kann man Funktionen nicht direkt als vollständige Entitäten benennen. Der Versuch, dies zu tun, zerstört die logische Struktur.

3.  **Implikationen für Logik und Mathematik**:
    - Funktionen sind primitiv in Freges Logizismus (die Reduktion von Mathematik auf Logik): Sie sind der Kitt zum Aufbau von Aussagen, Begriffen (speziellen Funktionen erster Stufe, die Wahrheitswerte zurückgeben) und sogar Zahlen (als Wertverläufe von Funktionen). Dies bindet sich in seine breitere Philosophie ein – Funktionen ermöglichen präzise Schlussfolgerungen ohne Mehrdeutigkeit.
    - Frege endet optimistisch: Eine klare Funktionsanalyse wird die Mathematik verfeinern und Paradoxien vermeiden (eine Vorwegnahme von Russells Brief von 1902 über sein eigenes Paradoxon, das um diese Zeit herum den zweiten Band der *Grundgesetze* zum Scheitern brachte).

Der Aufsatz ist keine Polemik; er ist diagnostisch, wie ein Philosoph-Logiker, der die Sprache der Mathematik debuggt. Er beeinflusste die analytische Philosophie (z.B. Wittgenstein, Russell) und die moderne Typentheorie in Logik/Informatik, wo Funktionen tatsächlich „ungesättigte“ Operationen sind.

#### Was ist eine Funktion laut Frege?
In Freges Sicht ist eine Funktion **eine ungesättigte logische Entität (oder ein Ausdruck), die Argumente auf Werte abbildet, indem sie ihre unvollständige Struktur vervollständigt**. Formal:
- Es ist nicht die Gleichung (y = f(x)), der Graph oder sogar die Menge der Ausgaben – diese sind abgeleitet.
- Es ist die „Lücke“ in einem Ausdruck, wie f(ξ) = ξ² + 3ξ, wobei ξ die Unvollständigkeit signalisiert.
- Eigenschaften: Extensionell (gleiche Eingaben → gleiche Ausgaben definieren die Identität); hierarchisch (Funktionen erster Stufe nehmen Objekte als Argumente, geben Objekte zurück; Funktionen zweiter Stufe nehmen Funktionen); und prädikativ (Begriffe/Relationen als Sonderfälle).
- Beispiel: Für f(x) = x² + 3x ist die Funktion die Regel/der Ausdruck mit einer Lücke; f(2) = 10 ist der gesättigte Wert.

Dies löst die Verwirrung Ihrer Studierenden: Die „Funktion“ ist nicht die ganze Gleichung y = x² + 3x (die vollständige und unvollständige Teile vermischt) oder nur f(x) = x² + 3x (die immer noch eine Variablen-Lücke hat). Es ist der reine, ungesättigte Abbildungsmechanismus darunter. Dies so zu lehren – ausgehend von der Logik, nicht nur von der Algebra – vermeidet die von Ihnen festgestellte Interferenz.

Wenn Sie möchten, kann ich Vorschläge machen, wie man dies in einer Anfängerklasse erklären oder in verwandte Frege-Aufsätze eintauchen kann.

**Referenzen**
- [Russell and Frege on the Logic of Functions (PDF summary/discussion)](https://newprairiepress.org/cgi/viewcontent.cgi?article=1023&context=biyclc)
- [The Philosophy of Gottlob Frege (excerpt on functions)](https://assets.cambridge.org/052183/6697/excerpt/0521836697_excerpt.htm)
- [Stanford Encyclopedia of Philosophy: Gottlob Frege](https://plato.stanford.edu/entries/frege/)
- [Collected Papers on Mathematics, Logic, and Philosophy (contains English translation)](https://www.oxfordbibliographies.com/display/document/obo-9780195396577/obo-9780195396577-0065.xml)
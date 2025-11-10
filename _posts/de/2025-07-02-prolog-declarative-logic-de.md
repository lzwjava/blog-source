---
audio: false
generated: true
lang: de
layout: post
title: 'Prolog: Logikbasierte deklarative Programmierung'
translated: true
type: note
---

Prolog, kurz für "Programming in Logic", ist eine **deklarative Programmiersprache**, die sich stark von imperativen Sprachen wie Python, Java oder C++ unterscheidet. Anstatt dem Computer Schritt für Schritt *zu erklären, wie* er ein Problem lösen soll, beschreibst du *was* das Problem ist, und Prolog verwendet seine eingebaute Inferenz-Engine, um Lösungen zu finden.

Es ist besonders gut geeignet für Probleme, die **Logik, symbolisches Schließen und Wissensrepräsentation** betreffen, was es zu einem Grundpfeiler auf den Gebieten der Künstlichen Intelligenz (KI), der natürlichen Sprachverarbeitung und von Expertensystemen macht.

### Schlüsselkonzepte von Prolog:

1.  **Fakten:**
    Fakten sind grundlegende Wahrheiten über die Welt, die du Prolog zur Verfügung stellst. Sie stellen unbedingte Aussagen dar.

      * **Syntax:** `prädikat(argument1, argument2, ...).`
      * **Beispiele:**
          * `mann(john).` (John ist ein Mann)
          * `frau(mary).` (Mary ist eine Frau)
          * `elternteil(john, mary).` (John ist ein Elternteil von Mary)
          * `hauptstadt_von(frankreich, paris).` (Paris ist die Hauptstadt von Frankreich)

2.  **Regeln:**
    Regeln definieren Beziehungen zwischen Fakten. Sie stellen fest, dass eine bestimmte Tatsache wahr ist, wenn eine oder mehrere andere Fakten (oder Bedingungen) wahr sind.

      * **Syntax:** `kopf :- körper.` (Zu lesen als "kopf ist wahr, wenn körper wahr ist")
          * Der `kopf` ist ein einzelnes Prädikat.
          * Der `körper` ist eine Konjunktion von einem oder mehreren Prädikaten, getrennt durch Kommata (`,`), was "UND" bedeutet.
      * **Beispiele:**
          * `glücklich(X) :- mag(X, pizza).` (X ist glücklich, wenn X Pizza mag)
          * `vater(X, Y) :- elternteil(X, Y), männlich(X).` (X ist der Vater von Y, wenn X ein Elternteil von Y ist UND X männlich ist)
          * `großelternteil(G, C) :- elternteil(G, P), elternteil(P, C).` (G ist ein Großelternteil von C, wenn G ein Elternteil von P ist UND P ein Elternteil von C ist)

3.  **Abfragen:**
    Sobald du deine Fakten und Regeln (deine "Wissensbasis") definiert hast, kannst du Prolog Fragen stellen, sogenannte Abfragen, um Informationen abzurufen oder Beziehungen zu überprüfen.

      * **Syntax:** `?- abfrage.`
      * Prolog versucht, die Abfrage zu erfüllen, indem es Variablen findet, die die Abfrage basierend auf den etablierten Fakten und Regeln wahr machen. Wenn mehrere Lösungen existieren, kannst du Prolog oft durch Eingabe eines Semikolons (`;`) dazu auffordern, weitere zu suchen.
      * **Beispiele:**
          * `?- mann(john).` (Ist John ein Mann?)
          * `?- elternteil(john, X).` (Von wem ist John ein Elternteil? - `X` ist eine Variable)
          * `?- großelternteil(elizabeth, william).` (Ist Elizabeth ein Großelternteil von William?)

4.  **Variablen:**
    Variablen in Prolog werden verwendet, um unbekannte Werte darzustellen. Sie beginnen immer mit einem Großbuchstaben oder einem Unterstrich (`_`). Im Gegensatz zu Variablen in imperativen Sprachen sind sie keine Speicherplätze, denen neue Werte zugewiesen werden können; vielmehr sind sie Platzhalter, die Prolog versucht durch Werte zu ersetzen (zu unifizieren), um eine Abfrage zu erfüllen.

5.  **Unifikation:**
    Dies ist der Kernmechanismus von Prolog. Unifikation ist ein Musterabgleichsprozess, der versucht, zwei Terme identisch zu machen, indem Werte an Variablen gebunden werden. Wenn eine Übereinstimmung gefunden wird, werden die Variablen an diese Werte "gebunden". Wenn keine Übereinstimmung möglich ist, schlägt die Unifikation fehl.

6.  **Backtracking (Rücksetzverfahren):**
    Wenn Prolog versucht, eine Abfrage zu erfüllen, arbeitet es die Fakten und Regeln auf Tiefensuche ab. Wenn ein Pfad in eine Sackgasse führt (ein Ziel nicht erfüllt werden kann), "backtracked" Prolog zu einem früheren Entscheidungspunkt und versucht einen alternativen Pfad. Diese systematische Suche ermöglicht es ihm, alle möglichen Lösungen für eine Abfrage zu finden.

### Wie Prolog funktioniert (vereinfacht):

1.  Du lädst ein Prolog-Programm (eine Sammlung von Fakten und Regeln) in den Interpreter.
2.  Du stellst eine Abfrage.
3.  Prolog versucht, die Abfrage zu beweisen, indem es sie mit seinen Fakten und den Köpfen seiner Regeln abgleicht.
4.  Wenn ein Regelkopf übereinstimmt, versucht Prolog dann, die Bedingungen im Regelkörper zu beweisen (diese werden zu Teilzielen).
5.  Dieser Prozess setzt sich rekursiv fort, bis alle Teilziele durch Fakten oder erfolgreich bewiesene Regeln erfüllt sind.
6.  Wenn eine Lösung gefunden wird, präsentiert Prolog die Variablenbindungen. Wenn mehrere Lösungen existieren, kann es backtracken, um sie zu finden.

### Vorteile von Prolog:

  * **Deklarative Natur:** Fokus auf *was* zu lösen ist, nicht *wie*. Dies kann für bestimmte Probleme zu prägnanterem und lesbarerem Code führen.
  * **Eingebaute Logik und Inferenz:** Leistungsstarke Mechanismen für logisches Schließen und Suchen.
  * **Hervorragend für symbolische KI:** Ideal für Expertensysteme, natürliche Sprachverarbeitung, Wissensrepräsentation und Theorembeweiser.
  * **Musterabgleich und Unifikation:** Vereinfacht komplexe Datenmanipulation.
  * **Backtracking:** Automatisiert die Suche nach Lösungen, die in anderen Sprachen manuell programmiert werden müssten.

### Nachteile von Prolog:

  * **Lernkurve:** Das deklarative Paradigma kann für Personen, die an imperative Programmierung gewöhnt sind, eine Herausforderung sein.
  * **Leistung:** Kann für numerische Berechnungen oder E/A-intensive Aufgaben im Vergleich zu imperativen Sprachen weniger effizient sein.
  * **Begrenzte E/A und Grafik:** Nicht für komplexe Benutzeroberflächen oder grafische Anwendungen konzipiert.
  * **Debugging:** Die Verfolgung des Ablaufsteuerung in Prolog kann aufgrund des Backtrackings manchmal schwierig sein.

-----

### Prolog-Code-Beispiele:

Um diese Beispiele auszuführen, benötigst du einen Prolog-Interpreter (wie SWI-Prolog, der kostenlos und weit verbreitet ist). Typischerweise speicherst du deinen Code in einer Datei mit der Endung `.pl` (z.B. `family.pl`) und lädst sie dann in den Interpreter.

**Beispiel 1: Familienbeziehungen**

Definieren wir einige grundlegende Familienbeziehungen.

**`family.pl`:**

```prolog
% Fakten: Definiere grundlegende Beziehungen
männlich(john).
männlich(jim).
männlich(george).
weiblich(mary).
weiblich(lisa).
weiblich(susan).

elternteil(john, lisa).   % John ist ein Elternteil von Lisa
elternteil(john, jim).    % John ist ein Elternteil von Jim
elternteil(mary, lisa).   % Mary ist ein Elternteil von Lisa
elternteil(mary, jim).    % Mary ist ein Elternteil von Jim
elternteil(lisa, george). % Lisa ist ein Elternteil von George
elternteil(jim, susan).   % Jim ist ein Elternteil von Susan

% Regeln: Definiere abgeleitete Beziehungen
vater(X, Y) :- elternteil(X, Y), männlich(X).         % X ist der Vater von Y, wenn X ein Elternteil von Y ist UND X männlich ist.
mutter(X, Y) :- elternteil(X, Y), weiblich(X).        % X ist die Mutter von Y, wenn X ein Elternteil von Y ist UND X weiblich ist.
kind(X, Y) :- elternteil(Y, X).                       % X ist ein Kind von Y, wenn Y ein Elternteil von X ist.
großelternteil(G, C) :- elternteil(G, P), elternteil(P, C). % G ist ein Großelternteil von C, wenn G ein Elternteil von P ist UND P ein Elternteil von C ist.
geschwister(X, Y) :- elternteil(P, X), elternteil(P, Y), X \= Y. % X und Y sind Geschwister, wenn sie ein Elternteil P teilen, und X nicht dasselbe wie Y ist.
```

**Ausführung in einem Prolog-Interpreter (z.B. SWI-Prolog):**

```prolog
?- consult('family.pl').
% family.pl compiled 0.00 sec, 7 clauses
true.

% Abfragen:

?- männlich(john).
true.

?- weiblich(jim).
false.

?- elternteil(john, lisa).
true.

?- elternteil(X, jim). % Wer ist ein Elternteil von Jim?
X = john ;           % Tippe ';' für weitere Lösungen
X = mary.
false.

?- vater(john, lisa).
true.

?- mutter(mary, jim).
true.

?- großelternteil(john, george).
true.

?- großelternteil(X, susan). % Wer ist ein Großelternteil von Susan?
X = john ;
X = mary.
false.

?- geschwister(lisa, jim).
true.

?- geschwister(lisa, george).
false. % Weil sie nicht *alle* Eltern teilen
```

**Beispiel 2: Einfache Wissensbasis (Tiere)**

**`animals.pl`:**

```prolog
% Fakten über Tiere und ihre Eigenschaften
tier(hund).
tier(katze).
tier(vogel).
tier(fisch).

hat_fell(hund).
hat_fell(katze).
fliegt(vogel).
schwimmt(fisch).

frisst(hund, knochen).
frisst(katze, fisch).
frisst(vogel, samen).
frisst(fisch, plankton).

% Regeln
ist_säugetier(X) :- tier(X), hat_fell(X). % Ein Säugetier ist ein Tier, das Fell hat.
kann_fliegen(X) :- tier(X), fliegt(X).     % Etwas kann fliegen, wenn es ein Tier ist und fliegt.
```

**Ausführung in einem Prolog-Interpreter:**

```prolog
?- consult('animals.pl').
% animals.pl compiled 0.00 sec, 10 clauses
true.

% Abfragen:

?- tier(katze).
true.

?- hat_fell(hund).
true.

?- frisst(katze, X). % Was frisst eine Katze?
X = fisch.

?- ist_säugetier(hund).
true.

?- ist_säugetier(vogel).
false.

?- kann_fliegen(X). % Welche Tiere können fliegen?
X = vogel.
false.
```

Diese Beispiele veranschaulichen die deklarative Natur von Prolog, bei der du die Beziehungen und Eigenschaften definierst und das System Antworten auf deine Abfragen ableitet.
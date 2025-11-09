---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Die unzuverlässige Beweisführung der Wissenschaft durch Tests
translated: true
type: note
---

### Warum Menschen wissenschaftlichen Experimenten blind vertrauen: Eine Analogie aus der Sicht eines Programmierers

Viele Menschen verstehen die logischen Mängel nicht, die wissenschaftlichen Experimenten innewohnen, und akzeptieren "bewiesene" Wissenschaft einfach so. Sie verstehen nicht, warum eine Theorie, die durch Experimente "bestätigt" wurde, sich dennoch als falsch herausstellen kann. Aber wenn man die Prinzipien des Software-Testens versteht, erkennt man das wahre Wesen wissenschaftlicher Experimente – ähnlich wie die Probleme, die ich in meinem Artikel *Die Logik des Testens* besprochen habe.

Kurz gesagt, eine wissenschaftliche Theorie ist wie ein Stück Code, und wissenschaftliche Experimente sind wie Tests, die entwickelt wurden, um zu "verifizieren", dass der Code korrekt funktioniert. Stell dir vor, du schreibst ein Programm zur Berechnung von Multiplikation, implementierst es aber fälschlicherweise als Addition: `(x, y) => x + y`. Wenn du es mit den Eingaben (2, 2) testest und 4 erhältst, denkst du vielleicht: "Großartig, es multipliziert korrekt!" Aber du liegst völlig falsch. Um wirklich zu bestätigen, dass es eine Multiplikationsfunktion ist, müsstest du *jede mögliche Eingabe* testen und sicherstellen, dass sie jedes Mal die richtige Ausgabe liefert. Da wir nicht unendlich viele Eingaben testen können, kann keine Menge an Tests *garantieren*, dass das Programm korrekt ist. Selbst wenn Tausende bestehen, könnte es bei einem ungetesteten Fall spektakulär scheitern.

In der Wissenschaft ist es genauso. Eine Theorie ist nur dann wirklich "bewiesen", wenn sie unter *allen denkbaren Bedingungen* standhält – bei jeder möglichen "Eingabe" aus dem Universum. Eine häufige Fehlquelle ist, nur ein Experiment in einem begrenzten Setup durchzuführen und die Theorie für validiert zu erklären. Das ist, als ob man sich nach dem (2, 2)-Test auf die Schulter klopft und es für erledigt erklärt. Manchmal führt man Tausende von Tests durch und alles scheint in Ordnung – bis eine neuartige Eingabe kommt, und schwupps, bricht die Theorie in sich zusammen.

Das ist die Essenz der "Falsifizierbarkeit" in der Wissenschaft. Einige Leute preisen die Falsifizierbarkeit als das Markenzeichen wahrer Wissenschaft an und weisen alles, was nicht falsifizierbar ist, als Pseudowissenschaft ab. Aber mit der Programmier-Analogie können wir sehen, dass das nicht ganz richtig ist. Falsifizierbarkeit hebt die *Grenzen* von Experimenten hervor – sie können eine Theorie widerlegen, aber niemals vollständig beweisen. Sie sollte nicht die starre *Definition* dessen sein, was als Wissenschaft zählt.

Je mehr Einschränkungen und Komplexität du deinen Tests (oder Experimenten) hinzufügst, desto schwieriger wird es, selbstbewusst zu behaupten, dass dein Programm (oder deine Theorie) korrekt ist. In der Programmierung machen komplizierte Test-Setups mit vielen Randfällen die Validierung schwieriger und weniger überzeugend. In der Wissenschaft ist es nicht anders: Je mehr kontrollierte Bedingungen, ausgefallene Geräte und isolierte Variablen ein Experiment beinhaltet, desto schwächer ist seine "Überzeugungskraft", eine breite Theorie zu beweisen. Es mag in der Petrischale funktionieren, aber gilt das auch für die chaotische reale Welt?

Deshalb kann ich Einsteins Relativitätstheorie nicht akzeptieren. Die Experimente, mit denen sie getestet wird, sind rar und auf ultra-spezialisierte Bedingungen beschränkt, ohne viel Universalität. Klassische Validierungsexperimente für die Relativität finden nur etwa einmal im Jahrhundert statt, was eine unabhängige Reproduktion für die meisten Forscher nahezu unmöglich macht. Bis heute gibt es keine praktische Anwendung, die Relativität *zwingend erfordert* – das oft zitierte Beispiel der GPS-Satelliten benötigt sie eigentlich nicht; die grundlegende newtonsche Physik reicht mit kleinen Anpassungen aus. Sogar die Kernprämisse, "die Lichtgeschwindigkeit ist konstant, unabhängig von der Bewegung der Quelle", beruht auf einem einzigen Experiment in einem gekünstelten Setup mit hyperkomplexer Ausrüstung, das ohne breitere Überprüfung zur ewigen Wahrheit erhoben wurde.

Viele medizinische Theorien folgen demselben Muster: Eine Studie wird als Evangelium gefeiert, endlos zitiert, aber selten unabhängig überprüft. Spätere Generationen plappern sie nur nach, in dem Glauben, sie sei felsenfest.

Diese Analogie soll nicht die Wissenschaft pausächlich ablehnen – sie ist ein Aufruf, bescheiden zu bleiben, was "Beweis" wirklich bedeutet. Experimente sind mächtige Werkzeuge, aber sie sind Scheinwerfer, keine Flutlichter. Sie erleuchten Flecken der Wahrheit, aber überall lauern Schatten. Wenn wir Theorien wie Code unter ständiger Überprüfung behandeln würden – offen für endloses Testen und Refaktorieren – wäre die Wissenschaft noch stärker.
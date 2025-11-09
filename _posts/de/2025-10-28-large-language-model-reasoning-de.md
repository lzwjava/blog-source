---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Große Sprachmodell-Verfahren für das logische Denken
translated: true
type: note
---

### Überblick
Denny Zhou (vermutlich die beabsichtigte Person "Danny Zhou") hielt einen Vortrag mit dem Titel "Large Language Model Reasoning" im Rahmen von Stanfords CS25: Transformers United Kurs (Version 5). Darin gibt er einen umfassenden Überblick über das Reasoning in Large Language Models (LLMs), wobei er praktische Techniken, theoretische Grundlagen und laufende Herausforderungen betont. Im Folgenden finden Sie eine strukturierte Zusammenfassung seiner Kernaussagen, die direkt seinen Folien und begleitenden Notizen entnommen ist.

### Definition von Reasoning in LLMs
- Beim Reasoning in LLMs geht es grundlegend darum, **zwischengeschaltete Tokens** (oder Schritte) zwischen der Eingabeaufforderung und der endgültigen Ausgabe zu generieren, anstatt direkt zu einer Antwort zu springen. Dieser Prozess ermöglicht es dem Modell, komplexe Probleme aufzuschlüsseln.
- Es muss nicht genau das menschliche Denken nachahmen – das Ziel ist eine effektive Problemlösung. Beispiel: Die Frage "Was sind die letzten beiden Buchstaben von 'artificial intelligence'?" wird gelöst, indem schrittweise die Wortenden verkettet werden, was "le" ergibt. Dies zeigt, wie Zwischenschritte die Berechnung unterstützen.
- Theoretische Untermauerung: Für Probleme, die durch boolesche Schaltkreise der Größe *T* lösbar sind, können Transformer konstanter Größe sie bewältigen, indem sie *O(T)* Zwischentokens erzeugen, was die Notwendigkeit einer massiven Skalierung des Modells vermeidet.

### Motivationen
- Vortrainierte LLMs sind von Haus aus fähig zum Reasoning, ohne spezielles Prompting oder Fine-Tuning; das Gerücht, dass sie es nicht können, ist widerlegt – Probleme entstehen durch Decoding-Methoden, die die durchdachten Ausgaben nicht zutage fördern.
- Dieser Ansatz folgt "The Bitter Lesson": Rechenleistung nutzen (durch Token-Generierung) statt menschenähnlicher Abkürzungen, wodurch sich menschenähnliche Verhaltensweisen durch die Vorhersage des nächsten Tokens emergent ergeben.
- Fokus auf die Optimierung von Endziel-Metriken wie Korrektheit, unter Verwendung von modellgenerierten Daten statt teurer menschlicher Annotationen.

### Kernideen
- **Chain-of-Thought (CoT) Decoding**: Generiere mehrere Kandidatenantworten und wähle diejenige mit der höchsten Konfidenz für die endgültige Antwort. Durchdachte Pfade haben oft eine höhere Konfidenz als direkte Schätzungen (z.B. das Zählen von Äpfeln in einem Szenario).
- **Skalierung über Länge, nicht Tiefe**: Trainiere Modelle dazu, längere Sequenzen (*O(T)* Tokens) für serielle Probleme zu generieren, wodurch sie beliebig leistungsfähig werden, ohne die Modellgröße aufzublähen.
- **Aggregation gegenüber Einzelantworten**: Das Generieren und Kombinieren mehrerer Antworten (z.B. durch Mehrheitsentscheid) übertrifft Einzelausgaben; das Retrieval ähnlicher Probleme + Reasoning schlägt Reasoning allein.
- Beispiel: Gemini 2.0s "Denkmodus" löst Rätsel, wie man 2025 mit den Zahlen 1-10 bildet, indem Operationen priorisiert werden (z.B. 45 × 45 = 2025).

### Wichtige Techniken
- **Prompting**: Verwende Few-Shot-Beispiele oder Phrasen wie "Lass uns Schritt für Schritt denken", um Zwischenschritte hervorzurufen (z.B. für Textaufgaben). Zero-Shot funktioniert, ist aber weniger zuverlässig.
- **Supervised Fine-Tuning (SFT)**: Trainiere mit menschlich annotierten Schritt-für-Schritt-Lösungen, um die Wahrscheinlichkeit von durchdachten Pfaden zu erhöhen.
- **Selbstverbesserung**: Generiere eigene Trainingsdaten, indem korrekte, durchdachte Lösungen aus Modellausgaben gefiltert werden.
- **RL Fine-Tuning (ReFT)**: Belohne iterativ korrekte vollständige Antworten (Reasoning + Antwort) und bestrafe falsche, unter Verwendung eines Verifizierers. Dies verallgemeinert am besten für überprüfbare Aufgaben; Dank an Teammitglieder wie Jonathan Lai.
- **Self-Consistency**: Sample mehrere Pfade und aggregiere sie dann (z.B. häufigste Antwort). Universelle Variante für offene Aufgaben lässt das Modell selbst auswählen.
- **Retrieval + Reasoning**: Hole ähnliche Beispiele herein, um den Prozess zu starten (z.B. das Abrufen von Entfernungsformeln für Flächenanfragen).
- **Andere Verbesserer**: "Take a Step Back" für Abstraktion; Marginalisierung, um probabilistische Decoding-Biases zu korrigieren.

### Einschränkungen
- **Prompting**: Einfach, aber spröde – benötigt aufgabenspezifische Beispiele; generische Prompts schneiden schlechter ab.
- **SFT**: Verallgemeinert nicht gut auf Out-of-Distribution-Probleme (z.B. scheitert bei neuartiger "Erdbeer"-Buchstabenzählung trotz Training).
- **RL**: Basiert auf zuverlässigen Verifizierern, die nicht für alle Aufgaben verfügbar sind (z.B. kreatives Schreiben).
- **Allgemeine Herausforderungen**: LLMs sind probabilistische Prädiktoren, daher begünstigt gieriges Decoding flüssige, aber falsche Antworten. Aggregation hilft, löst aber nicht nicht-verifizierbare Domänen.
- Decoding-Fehlausrichtung: Selbst starke Modelle ordnen durchdachte Ausgaben ohne Intervention möglicherweise nicht höchste Priorität zu.

### Zukünftige Richtungen
- Über Benchmarks hinaus zu realen Anwendungen vordringen, insbesondere bei nicht-verifizierbaren Aufgaben (z.B. Übersetzungsoptimierung ohne perfekte Metriken).
- Skalierung von Aggregation und Retrieval für größere Gewinne.
- Verbesserung des Decodings (z.B. durch Marginalisierung), um probabilistische Ausgaben besser mit der Korrektheit in Einklang zu bringen.
- Hin zu Systemen arbeiten, die sich erfolgreiche Reasoning-Pfade über Sitzungen hinweg "merken".

Dieser Vortrag hebt RL Fine-Tuning als derzeitige Kraftpakete hervor, mit einem Wandel hin zur Betrachtung von Reasoning als ein skalierbares Generierungsproblem.

### Referenzen
- [LLM Reasoning Slides (PDF)](https://dennyzhou.github.io/LLM-Reasoning-Stanford-CS-25.pdf)
- [Denny Zhous X-Post zu den Kernpunkten](https://x.com/denny_zhou/status/1948499173986201915)
- [Vortragsvideo auf YouTube](https://www.youtube.com/watch?v=ebnX5Ur1hBk)
- [CS25 Kursseite](https://web.stanford.edu/class/cs25/)
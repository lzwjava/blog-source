---
audio: false
generated: true
image: false
lang: de
layout: post
title: Bittere Lehre treibt die Evolution von Transformatoren voran
translated: true
type: note
---

In seinem Vortrag bei der Stanford CS25-Veranstaltung liefert Hyung Won Chung eine detaillierte historische und vorausschauende Analyse der **Transformer-Architekturen** und argumentiert, dass das Verständnis der treibenden Kräfte hinter ihrer Entwicklung der Schlüssel zur Antizipation der Zukunft der KI ist. Der Kern seiner Argumentation dreht sich um die "Bittere Lektion" der KI-Entwicklung, die er anhand der Evolution der Transformer-Modelle veranschaulicht.

***

### Die treibende Kraft des KI-Fortschritts

Chung stellt die These auf, dass der bedeutendste Faktor, der die KI-Forschung vorantreibt, die **exponentiell sinkenden Kosten für Compute** sind, was eine entsprechende Steigerung des Umfangs von Modellen und Daten ermöglicht hat. Er argumentiert, dass man, um das rasante Tempo des Wandels in diesem Bereich zu verstehen, sich auf diese dominierende treibende Kraft konzentrieren muss, anstatt sich in den Details einzelner architektonischer Innovationen zu verlieren.

Er führt das Konzept der **"Bitteren Lektion"** ein, das besagt, dass langfristiger KI-Fortschritt einfachere, allgemeinere Methoden mit weniger eingebauten Annahmen (induktiven Verzerrungen) begünstigt. Während hochstrukturierte, domänenspezifische Modelle kurzfristige Gewinne bringen mögen, werden sie letztendlich zu Engpässen, wenn Compute und Daten skaliert werden. Er ermutigt Forscher, die zugrundeliegenden Strukturen ihrer Modelle ständig zu hinterfragen und zu vereinfachen.

***

### Die Evolution der Transformer-Architekturen

Chung veranschaulicht seine Punkte anhand drei großer Transformer-Architekturen:

1.  **Encoder-Decoder (Original Transformer):** Diese Architektur, die ursprünglich für Aufgaben wie maschinelle Übersetzung verwendet wurde, hat eine inherent stärkere Struktur. Sie verwendet separate Parameter für Encoder und Decoder sowie spezifische Cross-Attention-Muster. Obwohl effektiv für Aufgaben mit klaren Eingabe-/Ausgabestrukturen, verliert diese Struktur im Zeitalter großer, allgemeiner Modelle an Relevanz.

2.  **Encoder-Only (z.B. BERT):** Eine einfachere Architektur, die auf Generierung verzichtet und sich auf Aufgaben wie Klassifizierung konzentriert. Obwohl leistungsstark für spezifische Benchmarks, macht ihr enger Fokus sie weniger verallgemeinerbar für eine breite Palette moderner Anwendungen.

3.  **Decoder-Only (z.B. GPT-3):** Dies ist die allgemeinste und am wenigsten strukturierte der drei Architekturen. Sie verwendet einen einzigen Stapel von Layern und gemeinsame Parameter, was sie hochgradig geeignet für moderne Large Language Models macht, die vielfältige Aufgaben bewältigen, allgemeines Wissen erlernen und lange Texte generieren.

***

### Wichtige Erkenntnisse und Vorhersagen

Laut Chung ist der Trend klar: Die KI bewegt sich hin zu **einfacheren, allgemeineren Architekturen mit weniger auferlegter Struktur**. Dies gibt Modellen die Freiheit, komplexe Muster und Beziehungen aus riesigen Datenmengen zu erlernen, ohne durch feste Annahmen eingeschränkt zu werden.

Er deutet an, dass der nächste Engpass in der KI möglicherweise nicht die Architektur selbst, sondern das **Lernziel** sein könnte. Er betrachtet Methoden wie Reinforcement Learning from Human Feedback (RLHF) als einen Schritt hin zu weniger strukturierten, gelernten Zielfunktionen, die besser für offene und komplexe Generierungsaufgaben geeignet sind. Er ermutigt das Publikum, kritisch über diese Prinzipien nachzudenken, um die Zukunft der KI mitzugestalten.

Sie können den vollständigen Vortrag unter [https://www.youtube.com/watch?v=3gb-ZkVRemQ&pp=0gcJCfwAo7VqN5tD](https://www.youtube.com/watch?v=3gb-ZkVRemQ&pp=0gcJCfwAo7VqN5tD) ansehen.
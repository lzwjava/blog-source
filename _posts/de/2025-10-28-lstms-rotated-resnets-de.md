---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: LSTMs waren nur rotierte ResNets
translated: true
type: note
---

In seiner NeurIPS 2024 Test of Time Award-Rede über die Arbeit "Sequence to Sequence Learning with Neural Networks" aus dem Jahr 2014 reflektierte Ilya Sutskever über wichtige Erkenntnisse und Fehleinschätzungen aus jener Zeit. Ein zentraler Punkt, den er unter "was wir falsch gemacht haben" ansprach, war die zu große Komplexität und die daraus resultierenden Grenzen von LSTMs (Long Short-Term Memory Networks), die frühe Durchbrüche im Bereich der Sequenzmodellierung, wie z.B. maschinelle Übersetzung, ermöglichten.

### Das grundlegende Missverständnis über LSTMs
Wir betrachteten LSTMs als eine grundlegend neuartige, komplizierte Architektur, die speziell für sequentielle Daten maßgeschneidert war – als etwas "Besonderes", das Deep-Learning-Forscher mühsam entwickeln mussten, um Zeitabhängigkeiten, verschwindende Gradienten und Rekurrenz zu handhaben. In Wirklichkeit, so erklärte Sutskever, waren LSTMs viel simpler: **Im Wesentlichen sind sie ein ResNet (Residual Network), das um 90 Grad gedreht ist**.

- **ResNets** (eingeführt 2015) revolutionierten die Bildverarbeitung, indem sie Skip Connections (Residuals) hinzufügten, die es Informationen ermöglichen, direkt über Schichten hinweg zu fließen, und so viel tiefere Netzwerke ohne Trainingsinstabilität ermöglichten.
- LSTMs (von 1997) machten etwas Analoges, aber in der *zeitlichen Dimension*: Ihre Gates und der Zellzustand wirken wie Residuals, die es Gradienten und Informationen erlauben, über lange Sequenzen hinweg zu propagieren, ohne zu verblassen. Es ist das gleiche Prinzip – nur "gedreht" von der räumlichen Stapelung (z.B. Pixel in einem Bild) zur zeitlichen Stapelung (z.B. Wörter in einem Satz).

Sutskever bemerkte scherzhaft: "Für diejenigen, die nicht damit vertraut sind, ist ein LSTM etwas, was arme Deep-Learning-Forscher taten, bevor es Transformer gab. Es ist im Grunde ein ResNet, aber um 90 Grad gedreht... Und es kam früher; es ist wie ein etwas komplexeres ResNet, mit einem Integrator und ein paar Multiplikationen." Diese Analogie unterstreicht, dass LSTMs keine radikale Abweichung waren; sie waren eine frühe, elegante Anwendung von Residual-Ideen auf die Rekurrenz.

### Warum das wichtig war (und was schiefging)
- **Was brillant funktionierte**: LSTMs skalierten für ihre Zeit überraschend gut und ermöglichten es dem Seq2Seq-Modell, traditionelle statistische Methoden bei Übersetzungsaufgaben zu übertreffen. Die Residuals machten tiefe rekurrente Netze trainierbar, ähnlich wie sie es später für feedforward Netze taten.
- **Was wir falsch machten (und warum LSTMs verblassten)**: Wir unterschätzten, wie die sequentielle Natur von LSTMs die Skalierbarkeit behindern würde. Im Gegensatz zu parallelisierbaren ResNets oder Transformern verarbeiten LSTMs Daten Schritt für Schritt, was sie ineffizient für massive Datensätze oder lange Kontexte macht. Sie fügten auch unnötige Komplexität hinzu (z.B. mehrere Gates), die die Aufmerksamkeitsmechanismen in Transformern vereinfacht beseitigten. Bis 2017 machten Transformer diese Grenzen deutlich und verlagerten den Fokus auf Self-Attention für bessere Parallelität und längerreichweitige Abhängigkeiten.

Im Nachhinein war der "falsche" Teil nicht die Erfindung der LSTMs – sie waren eine heroische Zwischenlösung – sondern das Festhalten an ihnen als Endziel für Sequenzen, anstatt Residuals als ein allgemeines Werkzeug zu erkennen und schneller auf parallelere Architekturen zu drängen.

Diese Perspektive stellt LSTMs nicht als Relikt dar, sondern als einen grundlegenden Schritt zum Verständnis davon, wie Skip Connections Tiefe über Dimensionen hinweg freischalten.

[Sequence to Sequence Learning with Neural Networks: What a Decade – Transcript & Video](https://kingy.ai/news/sequence-to-sequence-learning-with-neural-networks-what-a-decade-transcript-video/)  
[Ilya Sutskever NeurIPS 2024 full talk](https://www.youtube.com/watch?v=1yvBqasHLZs)  
[Reflections from Ilya's Full Talk at NeurIPS 2024](https://dlyog.com/papers/one_internet_v1)
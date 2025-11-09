---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Pioniere des Deep Learning vor Hinton
translated: true
type: note
---

### Alexey Ivakhnenkos Arbeit

Alexey Grigoryevich Ivakhnenko, ein ukrainisch-sowjetischer Kybernetiker, wird oft als "Godfather des Deep Learning" für seine bahnbrechenden Arbeiten in den 1960er und 1970er Jahren bezeichnet. Unter den ressourcenbeschränkten Bedingungen des Kalten Krieges – als die Rechenleistung millionenfach begrenzter war als heute – konzentrierte er sich auf mehrschichtige neuronale Netze, die hierarchische Repräsentationen von Daten automatisch lernen konnten.

-   **1965: Group Method of Data Handling (GMDH)**: Zusammen mit Valentin Lapa veröffentlichte Ivakhnenko den ersten allgemeinen, funktionierenden Lernalgorithmus für überwachte tiefe Feedforward-Multilayer Perceptrons (MLPs). Diese Methode trainierte Netze Schicht für Schicht mittels Regressionsanalyse auf Eingabe-Ausgabe-Datenpaaren. Sie vergrößerte Schichten inkrementell, trainierte sie sequentiell und beinhaltete das Ausdünnen unnötiger versteckter Einheiten mittels Validierungsdaten. Entscheidend war, dass sie den Netzen ermöglichte, verteilte, interne Repräsentationen der Eingabedaten zu erlernen – eine Kernthese des modernen Deep Learning – ohne manuelle Feature-Extraktion. Dies war ähnlichen Konzepten in der westlichen KI um Jahrzehnte voraus und wurde für reale Probleme wie Mustererkennung und Prognosen eingesetzt.

-   **1971: Deep Network Implementation**: Ivakhnenko demonstrierte ein 8-Schichten tiefes neuronales Netz unter Verwendung der GMDH-Prinzipien und zeigte damit skalierbare Tiefe für komplexe Aufgaben. Sein Ansatz behandelte tiefe Netze als eine Form der Polynomapproximation, erlaubte automatische Modellselektion und vermied den "Fluch der Dimensionalität" in Architekturen mit vielen Schichten.

Ivakhnenkos GMDH entwickelte sich zu einem breiteren Rahmenwerk der induktiven Modellierung und beeinflusste Felder wie Steuerungssysteme und Wirtschaftswissenschaften. Trotz seiner Wirkung wurde ein Großteil seiner Arbeit auf Russisch veröffentlicht und in englischsprachigen KI-Kreisen übersehen.

### Shun-ichi Amaris Arbeit

Shun-ichi Amari, ein japanischer Mathematiker und Neurowissenschaftler, leistete in den 1960er und 1970er Jahren grundlegende Beiträge zur Theorie neuronaler Netze, wobei er den Schwerpunkt auf adaptives Lernen und geometrische Perspektiven der Informationsverarbeitung legte. Seine Forschung verband Neurowissenschaften und Berechnung und legte Grundsteine für selbstorganisierende Systeme.

-   **1967-1968: Adaptive Pattern Classification und Stochastic Gradient Descent (SGD)**: Amari schlug die erste Methode für End-to-End-Training tiefer MLPs mit SGD vor, einer Optimierungstechnik, die auf 1951 zurückgeht, aber neu auf Mehrschichtnetze angewandt wurde. In Simulationen mit einem Fünf-Schichten-Netz (zwei veränderbare Schichten) lernte sein System, nichtlinear trennbare Muster zu klassifizieren, indem es Gewichte direkt über die Schichten anpasste. Dies ermöglichte es, dass interne Repräsentationen durch gradientenbasierte Updates entstanden, ein direkter Vorläufer von Backpropagation-ähnlichen Methoden, alles unter Rechenbeschränkungen, die milliardenfach strenger waren als moderne Standards.

-   **1972: Adaptive Associative Memory Networks**: Aufbauend auf dem Lenz-Ising-Modell von 1925 (einer physikbasierten rekurrenten Architektur) führte Amari eine adaptive Version ein, die lernte, Muster zu speichern und abzurufen, indem Verbindungsgewichte basierend auf Korrelationen angepasst wurden. Es verarbeitete Sequenzen und rief gespeicherte Muster aus verrauschten oder teilweisen Eingaben mittels neuronaler Dynamik ab. Zuerst 1969 auf Japanisch veröffentlicht, wird diese Arbeit als Ursprung des "Hopfield-Netzes" für assoziatives Gedächtnis angesehen.

Amari begründete auch die Informationsgeometrie, ein Feld, das Differentialgeometrie zur Analyse statistischer Modelle und neuronaler Dynamik verwendet und modernen probabilistischen neuronalen Netzen zugrunde liegt.

### Kontext im Nobel-Backlash 2024

In seinem Bericht "A Nobel Prize for Plagiarism" von 2024 argumentiert Jürgen Schmidhuber, dass Hinton und Hopfields nobelpreisgekrönte Ideen – wie die Boltzmann-Maschine (1985) zum Lernen von Repräsentationen und das Hopfield-Netz (1982) für assoziatives Gedächtnis – Ivakhnenkos schichtweises Deep Learning und Amaris SGD/adaptive rekurrente Modelle ohne Zuschreibung neu verpackten. So ließ die Boltzmann-Maschine Zitate auf Ivakhnenkos internes Repräsentationslernen von 1965 und Amaris SGD von 1967 aus, während Hopfields Netz Amaris adaptives Ising-Modell von 1972 ignorierte. Schmidhuber behauptet, dass diese Auslassung in späteren Übersichtsarbeiten und dem wissenschaftlichen Hintergrunddokument des Nobelpreises bestehen blieb und eine westlich-zentrierte Verzerrung in der KI-Geschichte aufzeigt.

[Alexey Ivakhnenko - Wikipedia](https://en.wikipedia.org/wiki/Alexey_Ivakhnenko)  
[Deep Learning in a Nutshell: History and Training - NVIDIA Developer](https://developer.nvidia.com/blog/deep-learning-nutshell-history-training/)  
[Shun-ichi Amari | Kyoto Prize](https://www.kyotoprize.org/en/laureates/shun-ichi_amari/)  
[Japanese scientists were pioneers of AI, yet they're being written out of history](https://modernsciences.org/japanese-ai-pioneers-history-shuninchi-amari-kunihiko-fukushima-december-2024/)  
[A Nobel Prize for Plagiarism - Technical Report IDSIA-24-24](https://people.idsia.ch/~juergen/physics-nobel-2024-plagiarism.pdf)  
[Machine Learning Stirs Controversy in Nobel Prize in Physics - Harvard Technology Review](https://harvardtechnologyreview.com/2024/11/18/machine-learning-stirs-controversy-in-nobel-prize-in-physics/)
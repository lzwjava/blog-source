---
audio: false
generated: false
image: false
lang: de
layout: post
title: KQV, Transformer und GPT
translated: true
---

## Wie ich den KQV-Mechanismus in Transformern gelernt habe

*2025.07.16*

Nach dem Lesen von [K, Q, V Mechanism in Transformers](https://lzwjava.github.io/notes/2025-06-02-attention-kqv-en) habe ich irgendwie verstanden, wie K, Q und V funktionieren.

Q steht für Query, K für Key und V für Value. Bei einem Satz ist die Query eine Matrix, die den Wert eines Tokens speichert, über das es andere Token befragen muss. Der Key steht für die Beschreibung der Token, und der Value steht für die eigentliche Bedeutungsmatrix der Token.

Sie haben spezifische Formen, daher muss man ihre Dimensionen und Details kennen.

Ich habe das etwa Anfang Juni 2025 verstanden. Zum ersten Mal davon gehört habe ich Ende 2023. Damals las ich Artikel wie [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/), verstand aber nicht viel.

Nach etwa zwei Jahren fällt mir das Verständnis nun leichter. In diesen zwei Jahren konzentrierte ich mich auf Backend-Arbeit und die Vorbereitung auf meine Abschlussprüfungen und las oder lernte nicht viel über maschinelles Lernen. Dennoch dachte ich ab und zu über diese Konzepte nach, zum Beispiel beim Autofahren oder bei anderen Tätigkeiten.

Das erinnert mich an die Wirkung von Zeit. Wir lernen vielleicht viele Dinge auf den ersten Blick, auch wenn wir sie nicht vollständig begreifen. Aber irgendwie löst es einen Denkprozess aus.

Mit der Zeit stellte ich fest, dass es bei Wissen und Entdeckungen schwer ist, Dinge beim ersten Mal zu verstehen oder zu durchdenken. Später scheint das Lernen und Verstehen jedoch einfacher zu werden.

Ein Grund dafür ist, dass es im Zeitalter der KI einfacher ist zu lernen, weil man sich in jeden Detailaspekt vertiefen kann, um seine Fragen zu klären. Es gibt auch mehr verwandte KI-Videos. Noch wichtiger ist, dass man sieht, wie viele Menschen damit lernen und Projekte darauf aufbauen, wie zum Beispiel [llama.cpp](https://github.com/ggml-org/llama.cpp).

Die Geschichte von Georgi Gerganov ist inspirierend. Als neuer Lernender im Bereich maschinelles Lernen, der etwa 2021 begann, hat er einen starken Einfluss in der KI-Community hinterlassen.

Solche Dinge werden sich immer wieder wiederholen. Daher glaube ich, dass ich für bestärkendes Lernen und das neueste KI-Wissen, auch wenn ich nicht viel Zeit investieren kann, trotzdem etwas Zeit finden kann, um schnell zu lernen und viel darüber nachzudenken. Das Gehirn wird seine Arbeit tun.

---

## Vom neuronalen Netzwerk zu GPT

*2023.09.28*

### YouTube-Videos

Andrej Karpathy - Let's build GPT: from scratch, in code, spelled out.

Umar Jamil - Attention is all you need (Transformer) - Modell-Erklärung (inkl. Mathematik), Inferenz und Training

StatQuest mit Josh Starmer - Transformer Neural Networks, ChatGPTs Grundlage, klar erklärt!!!

Pascal Poupart - CS480/680 Lecture 19: Attention und Transformer-Netzwerke

The A.I. Hacker - Michael Phi - Illustrierte Anleitung zu Transformers Neural Network: Eine Schritt-für-Schritt-Erklärung

### Wie ich lerne

Nachdem ich die Hälfte des Buches "Neural Networks and Deep Learning" gelesen hatte, begann ich, das Beispiel eines neuronalen Netzwerks zur Erkennung handgeschriebener Ziffern nachzubauen. Ich erstellte ein Repository auf GitHub, https://github.com/lzwjava/neural-networks-and-zhiwei-learning.

Das ist der wirklich schwierige Teil. Wenn man es von Grund auf schreiben kann, ohne Code zu kopieren, versteht man es sehr gut.

Mein nachgebauter Code enthält noch nicht die Implementierung von update_mini_batch und Backpropagation. Durch das sorgfältige Beobachten der Variablen in den Phasen des Ladens der Daten, des Feed-Forwardings und der Bewertung habe ich jedoch ein viel besseres Verständnis für Vektoren, Dimensionalität, Matrizen und die Formen der Objekte entwickelt.

Und ich begann, die Implementierung von GPT und Transformern zu lernen. Durch Wort-Einbettung und Positionskodierung wird der Text in Zahlen umgewandelt. Im Grunde gibt es dann keinen Unterschied mehr zu einem einfachen neuronalen Netzwerk, das handgeschriebene Ziffern erkennt.

Andrej Karpathys Vortrag "Let's build GPT" ist sehr gut. Er erklärt die Dinge gut.

Der erste Grund ist, dass es wirklich von Grund auf ist. Zuerst sehen wir, wie Text generiert wird. Es ist irgendwie unscharf und zufällig. Der zweite Grund ist, dass Andrej Dinge sehr intuitiv erklären kann. Andrej arbeitete mehrere Monate am Projekt nanoGPT.

Ich hatte gerade eine neue Idee, um die Qualität eines Vortrags zu beurteilen. Kann der Autor diesen Code wirklich schreiben? Warum verstehe ich etwas nicht und welches Thema hat der Autor ausgelassen? Neben diesen eleganten Diagrammen und Animationen, was sind ihre Mängel und Defekte?

Zurück zum Thema maschinelles Lernen selbst. Wie Andrej erwähnt, gibt es Dropout, Residual Connections, Self-Attention, Multi-Head Attention, Masked Attention.

Durch das Ansehen weiterer Videos begann ich, ein bisschen zu verstehen.

Durch Positionskodierung mit Sinus- und Kosinusfunktionen erhalten wir einige Gewichte. Durch Wort-Einbettung wandeln wir Wörter in Zahlen um.

$$
    PE_{(pos,2i)} = sin(pos/10000^{2i/d_{model}}) \\
    PE_{(pos,2i+1)} = cos(pos/10000^{2i/d_{model}})
$$

> The pizza came out of the oven and it tasted good.

In diesem Satz, wie erkennt der Algorithmus, ob es sich auf Pizza oder Ofen bezieht? Wie berechnen wir die Ähnlichkeiten für jedes Wort im Satz?

Wir möchten eine Reihe von Gewichten. Wenn wir das Transformer-Netzwerk für die Aufgabe der Übersetzung verwenden, gibt es bei der Eingabe eines Satzes den entsprechenden Satz in einer anderen Sprache aus.

Zum Skalarprodukt hier. Ein Grund, warum wir das Skalarprodukt verwenden, ist, dass es jede Zahl im Vektor berücksichtigt. Was wäre, wenn wir das quadrierte Skalarprodukt verwenden? Wir würden zuerst das Quadrat der Zahlen berechnen und dann das Skalarprodukt bilden. Was wäre, wenn wir ein umgekehrtes Skalarprodukt durchführen?

Bei der Maskierung hier ändern wir die Zahlen der Hälfte der Matrix in negative Unendlich. Dann verwenden wir Softmax, um die Werte im Bereich von 0 bis 1 zu halten. Wie wäre es, wenn wir die Zahlen in der linken unteren Hälfte in negative Unendlich ändern?

### Plan

Weiterhin Code und Forschungsarbeiten lesen und Videos anschauen. Einfach Spaß haben und meiner Neugier folgen.

https://github.com/karpathy/nanoGPT

https://github.com/jadore801120/attention-is-all-you-need-pytorch
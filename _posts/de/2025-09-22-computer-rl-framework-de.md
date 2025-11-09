---
audio: false
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: ComputerRL-Framework für Desktop-Automatisierungsagenten
translated: true
type: note
---

Die „ComputerRL“-Arbeit ist eine aktuelle Forschungsarbeit mit dem Titel *„ComputerRL: Scaling End-to-End Online Reinforcement Learning for Computer Use Agents“*. ([arXiv][1])

Hier sind die wesentlichen Ideen und Beiträge in Kürze:

---

### Was ist ComputerRL?

* Es ist ein Framework, das darauf abzielt, autonomen Agenten zu ermöglichen, mit Desktop-Umgebungen (Apps, GUIs, APIs) zu interagieren, wie ein Mensch es tun würde – durch Klicken, Tippen, Nutzen von Menüs etc. – aber auch über APIs, wenn möglich. ([arXiv][1])
* Die Idee ist, sowohl **GUI-basierte Interaktionen** (für den Fall, dass keine API verfügbar ist oder es für einen Menschen natürlicher ist) als auch **programmatische API-Aufrufe** (präziser, robuster, effizienter) in dem zu kombinieren, was sie das **API-GUI-Paradigma** nennen. ([arXiv][1])

---

### Warum es anders ist / Welche Probleme es löst

* Eine der großen Herausforderungen beim Training von RL-Agenten für Desktop-/GUI-Aufgaben ist die Ineffizienz und Instabilität beim Starten vieler virtueller Maschinen / Simulieren von Umgebungen über lange Zeiträume. ComputerRL bewältigt die Skalierung, indem es viele parallele Desktop-Umgebungen ausführt. ([arXiv][1])
* Außerdem neigen lange RL-Läufe zu einem **Entropie-Kollaps** (bei dem die Policy zu früh zu deterministisch wird und die Exploration reduziert). Sie schlagen eine Trainingsstrategie namens **Entropulse** vor, die zwischen Reinforcement-Learning-Phasen und supervised Fine-Tuning abwechselt, um die Exploration der Policy aufrechtzuerhalten. ([arXiv][1])

---

### Experimente & Ergebnisse

* Sie wandten es auf Open-Models wie **GLM-4-9B-0414** und **Qwen2.5-14B** an. ([arXiv][1])
* Der Evaluierungs-Benchmark ist **OSWorld**, der Agenten in Ubuntu-ähnlichen Desktop-Umgebungen testet. ([arXiv][1])
* Ihr Agent „AutoGLM-OS-9B“ (basierend auf GLM-4-9B-0414) erreicht eine neue State-of-the-Art-Genauigkeit (ca. 48,1 %) in diesen Desktop-Automatisierungsaufgaben. ([arXiv][1])

---

Wenn du möchtest, kann ich dir eine Zusammenfassung schicken, wie sich dies beispielsweise mit AgentBench oder den Agenten von Anthropic vergleichen lassen könnte (in Bezug auf Stabilität, TPS etc.), falls du neugierig bist.

[1]: https://arxiv.org/abs/2508.14040?utm_source=chatgpt.com "ComputerRL: Scaling End-to-End Online Reinforcement Learning for Computer Use Agents"
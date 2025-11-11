---
audio: false
generated: true
lang: de
layout: post
title: Transistoren als Schalter
translated: true
type: note
---

### Transistoren als Schalter: Ein Tutorial

Dieses Tutorial erklärt, wie ein Transistor, speziell ein Bipolartransistor (BJT), als ein durch elektrischen Strom gesteuerter Schalter fungieren kann.

**1. Stromverstärkung für die Schaltfunktion**

* Wie bereits gesehen, kann ein Transistor einen kleinen Basisstrom verstärken, um einen größeren Kollektor-Emitter-Strom zu steuern.
* Diese Verstärkung ist grundlegend für seine Verwendung als Schalter. Ein kleiner Steuerstrom kann einen viel größeren Strom steuern, der benötigt wird, um Komponenten wie eine LED mit Strom zu versorgen.

**2. Der "Ein"-Zustand: Sättigung**

* Wenn der Transistor den maximal möglichen Strom zwischen Kollektor und Emitter fließen lässt, befindet er sich in einem Zustand, der **Sättigung** genannt wird.
* Dies tritt auf, wenn der gewünschte Strom für die Schaltung geringer ist als der maximale Strom, den der Transistor basierend auf seiner Verstärkung liefern kann.
* In der Sättigung verhält sich der Transistor ähnlich wie ein **geschlossener Schalter** oder ein Kurzschluss und lässt den Strom frei passieren.

**3. Der "Aus"-Zustand: Sperrbereich**

* Wenn kein Basisstrom fließt, schränkt der Transistor den Stromfluss zwischen Kollektor und Emitter erheblich ein oder unterbricht ihn vollständig. Dieser Zustand wird **Sperrbereich** genannt.
* Im Sperrbereich verhält sich der Transistor wie ein **offener Schalter** und blockiert den Stromfluss vollständig.

**4. Wie er als Schalter funktioniert**

* Durch den Wechsel zwischen dem **Sättigungs-** (Ein-) Zustand und dem **Sperrbereich-** (Aus-) Zustand funktioniert ein Transistor effektiv als ein **stromgesteuerter Schalter**.
* Ein kleiner Steuerstrom an der Basis bestimmt, ob der Schalter "ein" (gesättigt) oder "aus" (Sperrbereich) ist, und steuert so einen größeren Strompfad.

**5. Schaltungsanwendungen**

* Das Verständnis dieser Schaltzustände ist entscheidend für den Aufbau elektronischer Schaltungen, in denen Transistoren verwendet werden, um den Stromfluss zu anderen Komponenten zu steuern.

Im Wesentlichen können wir, indem wir einen kleinen Basisstrom verwenden, um den Transistor entweder in die Sättigung oder den Sperrbereich zu treiben, ihn nutzen, um einen größeren Stromfluss ein- oder auszuschalten. Dies ermöglicht seine Verwendung als grundlegender Baustein in der Digitalelektronik und für Schaltanwendungen.
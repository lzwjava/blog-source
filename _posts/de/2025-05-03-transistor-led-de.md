---
audio: false
generated: true
lang: de
layout: post
title: LED-Schaltung mit einem Transistor
translated: true
type: note
---

Hier ist ein Tutorial basierend auf dem von Ihnen bereitgestellten YouTube-Video, das erklärt, wie man einen Transistor zur Steuerung einer LED-Schaltung verwendet.

**Ziel:** Lernen, wie man einen Transistor als Schalter verwendet, um eine LED mit einem Niedrigstrom-Signal ein- und auszuschalten.

**Hintergrundinformationen:**

* Transistoren ermöglichen es, dass ein größerer Strom zwischen ihrem Kollektor und Emitter fließt, gesteuert durch einen kleineren Strom, der von der Basis zum Emitter fließt.
* Der Kollektorstrom kann erheblich größer sein als der Basisstrom (z.B. 100 Mal).
* LEDs benötigen typischerweise eine bestimmte Stromstärke (z.B. 20mA), um korrekt zu leuchten.

**Schritte:**

1.  **Grundlegende LED-Schaltung aufbauen:** Schließen Sie eine 5V-Stromversorgung, eine LED, einen Widerstand (z.B. 220 Ohm) und den Transistor in einer Reihenschaltung an. Der Widerstand ist entscheidend, um den zur LED fließenden Strom zu begrenzen. Der Transistor fungiert als Schalter innerhalb dieser Schaltung.
2.  **Transistor anschließen:** Identifizieren Sie die Emitter-, Basis- und Kollektor-Pins Ihres Transistors. Schließen Sie den Emitter-Pin an Masse (Ground) an. Schließen Sie den Kollektor-Pin in der Schaltung zwischen den Widerstand (und die LED) und den Emitter.
3.  **Steuersignal anschließen:** Schließen Sie den positiven Pol Ihres Steuersignals an den Basis-Pin des Transistors an. Schließen Sie die Masse des Steuersignals an den Emitter-Pin an (der auch mit der Masse der Hauptschaltung verbunden ist).
4.  **Ergebnis beobachten:** Wenn das Steuersignal aktiv (ein) ist, fließt ein kleiner Strom von der Basis zum Emitter. Dieser kleine Basisstrom ermöglicht es, dass ein viel größerer Strom vom Kollektor zum Emitter fließt, wodurch die LED hell aufleuchtet. Wenn das Steuersignal inaktiv (aus) ist, fließt kein Strom von der Basis zum Emitter, der Transistor schaltet sich aus und die LED erlischt.

**Wichtige Konzepte:**

* **Stromverstärkung:** Transistoren können einen kleinen Basisstrom verstärken, um einen viel größeren Kollektorstrom zu steuern.
* **Stromgesteuerter Schalter:** Transistoren fungieren als Schalter, bei denen ein kleiner Eingangsstrom den Fluss eines größeren Stroms steuert.

Durch den Aufbau dieser Schaltung können Sie effektiv ein kleines Steuersignal verwenden, um eine Schaltung zu steuern, die einen höheren Strom benötigt, wie z.B. eine, die eine LED mit Strom versorgt.
http://googleusercontent.com/youtube_content/0
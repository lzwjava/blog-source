---
audio: false
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Grundlagen und Vergleiche des D-Flip-Flops
translated: true
type: note
---

Antwort: D-Flip-Flop

Warum es die richtige Wahl ist
- Funktion: Ein D-Flip-Flop (Daten- oder Verzögerungs-Flip-Flop) speichert exakt ein Bit. Bei der aktiven Taktflanke (steigend oder fallend, abhängig vom Design) tastet es den D-Eingang ab und aktualisiert Q auf diesen Wert. Zwischen den Taktflanken behält Q seinen vorherigen Wert bei.
- Verhaltensregel: Q_next = D bei der Taktflanke; ansonsten bleibt Q unverändert. Dieses "Sample-and-Hold"-Verhalten ist genau das, was man für Register und Pipelines benötigt.

Wie es sich von den anderen unterscheidet
- RS-Flip-Flop: Hat separate Set- und Reset-Eingänge und einen ungültigen Zustand (S=R=1). Nicht ideal für allgemeine Datenspeicherung in synchronen Schaltungen.
- JK-Flip-Flop: Verallgemeinert den RS-Flip-Flop; J=K=1 bewirkt ein Toggeln. Flexibler, aber komplexer und selten für Standard-Datenregister verwendet.
- T-Flip-Flop: Toggelt bei T=1 an der Taktflanke, hält den Zustand bei T=0. Ideal für Teiler-Zähler, nicht für die Speicherung beliebiger Daten.

Wichtige Details zu D-Flip-Flops
- Flankengesteuert vs. Latch: Ein D-Flip-Flop ist flankengesteuert (aktualisiert nur bei der Taktflanke). Ein D-Latch ist pegelgesteuert (durchlässig, solange Enable aktiviert ist). Wenn man sagt, dass die Eingabe "bei Takten direkt auf den Ausgang durchgeschaltet" wird, ist typischerweise gemeint, dass der D-Flip-Flop D bei der Taktflanke erfasst.
- Timing-Anforderungen: Für einen korrekten Betrieb müssen die Set-up-Zeit (D stabil vor der Flanke) und die Hold-Zeit (D stabil nach der Flanke) eingehalten werden. Eine Verletzung kann zu Metastabilität führen.
- Varianten: Oft mit asynchronen Preset- (Set) und Clear- (Reset) Eingängen zum Initialisieren von Q.
- Häufige Anwendungen: Aufbau von n-Bit-Registern (n DFFs parallel), Pipelinestufen, Zustandsregister, Schieberegister (oft mit einem MUX für serielles/paralleles Laden), Synchronisierer (in Paaren) für Clock-Domain-Crossings.

Faustregel
- Wenn Sie ein Speicherelement benötigen, das "einfach das Bit speichert, das Sie beim Takt anlegen", verwenden Sie einen D-Flip-Flop.
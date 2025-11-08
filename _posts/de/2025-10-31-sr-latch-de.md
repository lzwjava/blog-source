---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Grundlagen des SR-Latch
translated: true
type: note
---

### Was ist ein SR-Latch?
Ein **SR-Latch** (Set-Reset-Latch) ist ein grundlegender Baustein in der Digitaltechnik und Computerarchitektur. Es ist eine Art **Flip-Flop**, das ein einzelnes Bit an Information (0 oder 1) speichert und sich daran "erinnert", bis es explizit durch Eingangssignale geändert wird. Das "SR" steht für **Set** (um den Ausgang auf 1 zu setzen) und **Reset** (um den Ausgang auf 0 zu setzen).

Ein grundlegender SR-Latch wird typischerweise mit zwei **NOR-Gattern** (oder NAND-Gattern in einer Variante) aufgebaut, die kreuzgekoppelt sind. Hier ist ein einfaches textuelles Diagramm der NOR-basierten Version:

```
   S ───┐
        │ NOR1 ── Q
        │    │
   R ───┘    │
             │
             └─ NOR2 ── Q' (Komplement von Q)
                  │
                  └────── Rückkopplung zu NOR1
```

- **S** (Set): Wenn hoch (1), setzt es Q auf 1.
- **R** (Reset): Wenn hoch (1), setzt es Q auf 0.
- **Q**: Der gespeicherte Ausgang (der "Speicher").
- Die Rückkopplungsschleife zwischen den Gattern bewirkt, dass die Schaltung den Zustand "verriegelt", selbst nachdem S und R auf 0 zurückgehen.

### Was bedeutet "Latch" hier?
Der Begriff **Latch** bezieht sich auf die Fähigkeit der Schaltung, **einen stabilen Zustand über die Zeit zu halten (oder "festzuhalten")**, ohne dass dazu eine kontinuierliche Eingangsversorgung erforderlich ist. Es ist wie ein Schalter, der in seiner Position bleibt, nachdem man ihn umgelegt hat – bis man ihn erneut umlegt.

- **Nicht nur abstrakt**: Während "Latch" eine konzeptionelle Idee im Logikentwurf ist (eine Abstraktion für Speicherverhalten), wird es als **echte elektrische Schaltung** implementiert. Man kann sie mit physischen Komponenten wie Transistoren oder Logikgattern auf einem Chip aufbauen (z.B. in ICs der 7400er Serie).

- **Logik vs. Schaltung**: Es ist beides!
  - **Logikaufbau**: In der Theorie ist es ein boolesches Logikmodell, bei dem die Ausgänge von Eingängen und Rückkopplung abhängen (z.B. Q = ¬(S ∨ ¬Q) in der NOR-Version).
  - **Elektrische Schaltung**: In der Praxis ist es verdrahtete Hardware, die mit Spannungspegeln arbeitet (z.B. 5V-Logik). Die Gatter werden mit Strom versorgt, und Signale breiten sich als Ströme/Spannungen aus.

### Ist es ein abstraktes Konzept?
Ja, teilweise – **Latch** ist ein **abstraktes Modell** in der Informatik und im Digitalentwurf, das die einfachste Form von bistabilem Speicher (zwei stabile Zustände) repräsentiert. Aber es ist in der Physik verankert: Die Schaltung nutzt elektronische Hysterese (Rückkopplung), um den Zustand zu speichern. Ohne die physische Schaltung würde die Abstraktion nicht funktionieren.

Wenn Sie es simulieren oder studieren:
- Verwenden Sie Tools wie Logisim oder Tinkercad für eine virtuelle Schaltung.
- Wahrheitstabelle für den SR-Latch (NOR-Version):

| S | R | Q (nächster) | Q' (nächster) | Beschreibung    |
|---|----|--------------|---------------|-----------------|
| 0 | 0 | Q (vorher)   | Q' (vorher)   | Halten (Latch)  |
| 0 | 1 | 0            | 1             | Reset           |
| 1 | 0 | 1            | 0             | Set             |
| 1 | 1 | ?            | ?             | Ungültig (Race) |

Dieses "Halte"-Verhalten, wenn S=R=0 ist, macht es zu einem Latch – es ist ein Speicher!

Für vertiefende Einblicke sehen Sie sich Ressourcen wie "Digital Design" von Morris Mano an. Wenn Sie ein bestimmtes Diagramm oder eine Simulation im Sinn haben, teilen Sie weitere Details!
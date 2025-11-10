---
audio: false
generated: true
lang: de
layout: post
title: Googles Echtzeit-Kollaborationstechnologie in Docs
translated: true
type: note
---

Google Docs verwendet einen ausgeklügelten **Echtzeit-Kollaborationsalgorithmus**, um mehreren Benutzern die gleichzeitige Bearbeitung eines Dokuments zu ermöglichen. Die zugrunde liegende Kerntechnologie basiert auf **Operational Transformation (OT)** und entwickelte sich später weiter, um in einigen Systemen auch **Conflict-Free Replicated Data Types (CRDTs)** einzubeziehen. Hier ist eine Aufschlüsselung der wichtigsten Komponenten:

### 1. **Operational Transformation (OT)**
   - **Grundprinzip**: OT löst Konflikte, indem eingehende Operationen gegen bereits angewandte Operationen transformiert (angepasst) werden.
   - **Funktionsweise**:
     1. Wenn ein Benutzer eine Bearbeitung vornimmt (z. B. Text einfügt), generiert der Client eine **Operation** (z. B. `insert("hallo", pos=5)`).
     2. Die Operation wird an den Server gesendet, der sie gegen gleichzeitige Bearbeitungen anderer Benutzer **transformiert**, um Konsistenz zu gewährleisten.
     3. Alle Clients wenden die Operationen so an, dass letztendliche Konsistenz sichergestellt ist.
   - **Beispiel**: Wenn Benutzer A "abc" an Position 5 einfügt, während Benutzer B Position 5 löscht, passt OT die Operation von B an, um Position 8 (nach A's Einfügung) zu löschen.
   - **Herausforderungen**: OT erfordert einen Zentral-Server, um die Transformationen zu verwalten, was die Implementierung komplex macht.

### 2. **Conflict-Free Replicated Data Types (CRDTs)**
   - **Grundprinzip**: CRDTs ermöglichen es verteilten Systemen, Bearbeitungen ohne einen zentralen Server zusammenzuführen, indem Datenstrukturen entworfen werden, die immer konvergieren.
   - **Funktionsweise**:
     1. Bearbeitungen werden mit eindeutigen Identifikatoren versehen (wie Zeitstempel oder Vektoruhren).
     2. Das System führt Bearbeitungen mithilfe mathematischer Eigenschaften zusammen (z. B. kommutative, assoziative Operationen).
   - **Vorteile gegenüber OT**:
     - Kein zentraler Server erforderlich (funktioniert Peer-to-Peer).
     - Robuster für die Offline-Bearbeitung.
   - **Beispiel**: Anstatt Positionen durch Zahlen zu verfolgen, können CRDTs gebrochene Indizierung verwenden (z. B. "A" < "A1" < "B"), um Konflikte zu vermeiden.

### 3. **Googles Implementierung (Wave/OT-Hybrid)**
   - Google Docs basierte ursprünglich auf **Google Waves OT-Algorithmus**, der die klassische OT erweiterte mit:
     - **Zentralisiertem Server**: Stellt sicher, dass alle Operationen korrekt transformiert werden.
     - **Differenzieller Synchronisierung**: Minimiert die über das Netzwerk gesendeten Daten.
   - Im Laufe der Zeit hat Google wahrscheinlich **CRDT-ähnliche Optimierungen** für eine bessere Offline-Unterstützung integriert.

### 4. **Andere Schlüsseltechnologien**
   - **Frontend/Backend-Synchronisierung**: Verwendet **WebSockets/Long-Polling** für Echtzeit-Updates.
   - **Versionsvektoren/Logische Uhren**: Verfolgen die Kausalität von Bearbeitungen.
   - **Konfliktlösung**: Wenn zwei Benutzer gleichzeitig denselben Text bearbeiten, löst das System Konflikte mittels OT/CRDT-Regeln.

### **Vergleich: OT vs. CRDT**

| Merkmal               | OT (Google Docs Classic) | CRDT (z.B. Figma, Notion) |
|-----------------------|--------------------------|---------------------------|
| Zentraler Server nötig | Ja                      | Nein (Peer-to-Peer möglich) |
| Offline-Unterstützung | Eingeschränkt            | Besser                    |
| Komplexität           | Hoch (Transformationslogik) | Hoch (Datenstrukturentwurf) |
| Latenz                | Niedrig (serververwaltet) | Hängt von der Implementierung ab |

### **Warum Google wahrscheinlich OT verwendet (mit CRDT-Einflüssen)**
- OT eignet sich gut für **zentralisierte** Dienste wie Google Docs.
- CRDTs gewinnen in dezentralen Apps an Beliebtheit (z. B. **Figma, Apple Notes**), aber Googles Infrastruktur ist für OT optimiert.

### **Weiterführende Literatur**
- **OT-Papier**: [Operational Transformation in Real-Time Group Editors](https://dl.acm.org/doi/10.1145/146486.146487) (Cormack et al.)
- **CRDTs**: [A Comprehensive Study of CRDTs](https://arxiv.org/abs/1805.06358)
- **Google Wave Protocol**: [Wave Protocol](https://wave-protocol.google.com/)

Möchten Sie einen tieferen Einblick in einen bestimmten Aspekt?
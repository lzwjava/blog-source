---
audio: false
generated: true
lang: de
layout: post
title: Discords Rust-Leistungssteigerung
translated: true
type: note
---

Discords Umstellung auf Rust wurde durch Leistungsengpässe in ihrem Go-basierten „Read States“-Service veranlasst, der die Nachrichten-Lesestände von Nutzern über Kanäle hinweg verfolgt. Der Wechsel zu Rust brachte signifikante Verbesserungen bei der Latenz, beseitigte Garbage Collection-Spitzen und zeigte die Stärken von Rust im Bereich Speicherverwaltung und Nebenläufigkeit. Hier eine detaillierte Aufschlüsselung:

---

### **Warum Discord zu Rust gewechselt hat**
1.  **Garbage Collection (GC)-Probleme in Go**
    - Discords Go-Service erlebte alle ~2 Minuten Latenzspitzen aufgrund von Gos konservativer, nicht-generationaler GC, die *den gesamten LRU-Cache (mit Millionen von Objekten) scannen musste*, selbst bei minimaler Garbage-Produktion.
    - Die Feinabstimmung der Go-GC (z.B. durch Anpassen der Cache-Größe) konnte die Spitzen entweder nicht beheben oder verschlechterte die Latenz im 99. Perzentil.

2.  **Speicherverwaltung von Rust**
    - Rusts Ownership-Modell *gibt Speicher sofort frei* nach dem Entfernen aus dem LRU-Cache und vermeidet so GC-bedingte Pausen. Dieser deterministische Ansatz beseitigte Latenzspitzen.
    - Keine Laufzeit-GC-Overheads bedeuteten eine konsistente Leistung unter hoher Last (Hunderttausende Updates/Sekunde).

3.  **Leistungsoptimierung**
    - Selbst eine naive Rust-Implementierung erreichte die Leistung von Go. Weitere Optimierungen (z.B. die Verwendung von `BTreeMap` statt `HashMap`, Reduzierung von Speicherkopien) *senkten die CPU-Auslastung um 70 %* und drückten die durchschnittlichen Antwortzeiten auf Mikrosekunden.

4.  **Ökosystem und Async-Unterstützung**
    - Discord setzte früh auf Rusts Nightly-Async-Features (später stabilisiert), was effiziente vernetzte Dienste ohne GC-Kompromisse ermöglichte.

---

### **Ergebnisse des Wechsels**
-   **Latenz**: Beseitigung der 2-minütigen GC-Spitzen, Erreichen von Antwortzeiten im Sub-Millisekundenbereich.
-   **Ressourceneffizienz**: Geringere CPU- und Speichernutzung, Ermöglichung der Skalierung der Cache-Kapazität auf 8 Millionen Read States ohne Leistungseinbußen.
-   **Zuverlässigkeit**: Weniger Laufzeitfehler aufgrund von Rusts Compile-Time-Sicherheitsprüfungen.

---

### **Vorteile von Rust für Discord**
1.  **Leistung**
    - Vorhersehbare niedrige Latenz, ideal für Echtzeit-Services.
    - Fein granulierte Speicherkontrolle übertrifft GC-abhängige Sprachen.

2.  **Sicherheit**
    - Ownership-Modell verhindert Memory Leaks, Nullpointer und Data Races.
    - Nebenläufigkeitssicherheit ohne manuelle Synchronisierung.

3.  **Moderne Werkzeuge**
    - Cargo (Package Manager) und reiche Generics reduzierten Boilerplate-Code im Vergleich zu Go.

4.  **Wachsendes Ökosystem**
    - Upgrades (z.B. Tokio Async Runtime) brachten kostenlose Leistungssteigerungen.

---

### **Nachteile & Herausforderungen**
1.  **Lernkurve**
    - Rusts Ownership und Lifetimes erfordern anfänglichen Invest.

2.  **Frühe Async-Einschränkungen**
    - Anfängliche Abhängigkeit von instabilen Nightly-Features barg Wartungsrisiken.

3.  **Kleineres Ökosystem**
    - Weniger Bibliotheken im Vergleich zu Go oder C++, wächst aber schnell.

---

### **Wichtige Erkenntnisse**
Discords Erfolg mit Rust unterstreicht seine Eignung für *latenzkritische, hochskalierbare Dienste*, bei denen GC-Pausen inakzeptabel sind. Während der Übergang das Überwinden von Rusts steiler Lernkurve erforderte, brachte die Umstellung **schnellere Leistung, geringeren Ressourcenverbrauch und weniger Laufzeitfehler**. Für Teams, die langfristige Wartbarkeit und Leistung priorisieren, bietet Rust überzeugende Vorteile gegenüber GC-abhängigen Sprachen wie Go.

Für tiefergehende technische Einblicke siehe Discords [ursprünglichen Blog-Beitrag](https://discord.com/blog/why-discord-is-switching-from-go-to-rust).
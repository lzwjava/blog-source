---
audio: false
generated: true
lang: de
layout: post
title: Vorteile des JDK 24-Upgrades erklärt
translated: true
type: note
---

Ein Upgrade von JDK 11 auf JDK 24 bietet erhebliche Vorteile in verschiedenen Bereichen, einschließlich Leistung, neuen Funktionen und Sicherheit. Hier eine Aufschlüsselung:

**1. Leistungsverbesserungen:**

*   **Virtuelle Threads (Project Loom):** Obwohl in JDK 21 eingeführt, verfeinert JDK 24 virtuelle Threads weiter (JEP 491: Synchronize Virtual Threads Without Pinning). Dies ist ein Wendepunkt für hochgradig nebenläufige Anwendungen, da Millionen von leichtgewichtigen Threads ohne den Overhead traditioneller Plattform-Threads ermöglicht werden. Dies kann die Skalierbarkeit und Reaktionsfähigkeit dramatisch verbessern, besonders für server-seitige Anwendungen.
*   **Schnellerer Start:** JDK 24 beinhaltet "Ahead-of-Time Class Loading and Linking" (JEP 483), das Anwendungsklassen sofort verfügbar macht, wenn die JVM startet, und so die Startzeiten reduziert. Dies ist besonders vorteilhaft für Microservices und Cloud-native Anwendungen, bei denen ein schneller Start entscheidend ist.
*   **Kompakte Objekt-Header (Experimentell):** JEP 450 zielt darauf ab, die Größe von Objekt-Headern auf 64-Bit-Architekturen zu reduzieren, was zu erheblichen Speichereinsparungen (10-20 %) und einer verbesserten Cache-Lokalität führen kann, besonders für Anwendungen mit vielen kleinen Objekten.
*   **ZGC Generational Mode (Standard):** Der Z Garbage Collector (ZGC) verwendet nun standardmäßig einen Generational Mode (JEP 490), der die Garbage Collection für kurzlebige Objekte optimiert. Dies kann zu reduzierten Pausenzeiten und verbesserter Speichereffizienz für große Heaps führen.
*   **Stream Gatherers (JEP 485):** Diese neue API ermöglicht benutzerdefinierte Intermediate Operations in Stream Pipelines, was mehr Flexibilität und potenziell effizientere Datentransformationen bietet.
*   **Optimierte Foreign Function & Memory API Bulk Operations:** Bulk-Speicheroperationen verwenden nun Java-Code anstelle von nativen Methoden, was auf bestimmten Architekturen (z.B. Linux x64/AArch64) zu schnellerer Leistung führt, besonders für kleinere Datengrößen.
*   **String Concatenation Startup Boost:** Interne Optimierungen der String-Verkettung führen zu schnellerem Start und geringerem Code-Generation-Overhead.

**2. Neue Sprachfunktionen und APIs:**

*   **Pattern Matching Enhancements (JEP 488):** Weitere Verbesserungen am Pattern Matching, die primitive Typen in Patterns erlauben und `instanceof` sowie `switch` erweitern, um mit allen primitiven Typen zu arbeiten, was Code prägnanter und lesbarer macht.
*   **Scoped Values (JEP 487):** Eine Preview-API, die eine sicherere und effizientere Möglichkeit bietet, unveränderliche Daten innerhalb eines Threads und mit Kind-Threads zu teilen, was besonders bei virtuellen Threads vorteilhaft ist.
*   **Structured Concurrency (JEP 499):** Eine Preview-API, die die nebenläufige Programmierung vereinfacht, indem sie Gruppen verwandter Tasks als eine einzelne Einheit behandelt, was die Fehlerbehandlung, Abbruchmöglichkeit und Beobachtbarkeit verbessert.
*   **Class-File API (JEP 484):** Eine Standard-API zum Parsen, Generieren und Transformieren von Java-Class-Dateien.
*   **Vector API (JEP 489):** (Weiterhin im Incubator-Stadium) Diese API ermöglicht die Formulierung von Vektorberechnungen, die zu optimalen Vektorbefehlen auf unterstützten CPUs kompiliert werden, was zu überlegener Leistung für bestimmte numerische Operationen führt.
*   **Key Derivation Function API (JEP 478):** Eine Preview-API für kryptographische Algorithmen, die verwendet werden, um zusätzliche Schlüssel aus einem geheimen Schlüssel abzuleiten.

**3. Sicherheitsverbesserungen:**

*   **Quantenresistente Kryptographie:** JDK 24 führt Implementierungen der quantenresistenten Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM) (JEP 496) und Module-Lattice-Based Digital Signature Algorithm (ML-DSA) (JEP 497) ein und bereitet Java so auf zukünftige kryptographische Herausforderungen vor.
*   **TLS-Verbesserungen:** Verbesserungen wie konfigurierbare New Session Tickets Count für TLSv1.3 und ein Mechanismus zum Deaktivieren von TLS-Cipher-Suites durch Pattern Matching. TLS_RSA-Cipher-Suites sind nun standardmäßig deaktiviert, um Forward Secrecy zu verbessern.
*   **Entfernung des Security Manager (JEP 486):** Der Security Manager, eine veraltete Funktion, ist permanent deaktiviert. Dies vereinfacht das JVM-Sicherheitsmodell und fördert die Verwendung moderner Sicherheitspraktiken wie Container-basierter Sandboxing.
*   **Warnungen für `sun.misc.Unsafe`:** JDK 24 gibt Laufzeitwarnungen aus, wenn Speicherzugriffsmethoden in `sun.misc.Unsafe` verwendet werden, um die Migration zu sichereren Alternativen wie der VarHandle API und der Foreign Function & Memory API zu fördern.

**4. Veraltungen und Entfernungen:**

*   Während diese Codeänderungen erfordern können, tragen sie zu einer saubereren, sichereren und besser wartbaren Plattform bei. Die permanente Deaktivierung des Security Managers und die Warnungen für `sun.misc.Unsafe` sind Beispiele hierfür.

**5. Überlegungen zur Langzeitunterstützung (LTS):**

*   JDK 11 ist ein LTS-Release, mit erweiterter Unterstützung von Oracle bis mindestens Januar 2032.
*   JDK 24 ist *kein* LTS-Release. Das nächste LTS-Release nach JDK 21 ist voraussichtlich JDK 25 im September 2025.
*   Das bedeutet, dass bei einem Upgrade auf JDK 24 ein weiteres Upgrade auf JDK 25 (oder ein späteres LTS) relativ bald geplant werden muss, um fortgesetzte Langzeitunterstützung und Sicherheitsupdates zu gewährleisten.

**Zusammenfassend:**

Ein Upgrade auf JDK 24 von JDK 11 bietet eine Fülle neuer Funktionen, erhebliche Leistungssteigerungen (besonders durch virtuelle Threads und schnelleren Start) und entscheidende Sicherheitsverbesserungen. Es ist jedoch wichtig, den Support-Lebenszyklus zu berücksichtigen, da JDK 24 ein Non-LTS-Release ist, was ein nachfolgendes Upgrade auf JDK 25 (das nächste LTS) für langfristige Stabilität und Unterstützung notwendig macht.
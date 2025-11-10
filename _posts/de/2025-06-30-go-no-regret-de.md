---
audio: false
generated: true
lang: de
layout: post
title: PingCAP und Cloudflare loben Go
translated: true
type: note
---

Weder PingCAP noch Cloudflare haben "Bedauern" über die Verwendung von Go geäußert. Tatsächlich haben beide Unternehmen die Stärken von Go öffentlich gelobt und setzen es weiterhin umfassend in ihren Kernprodukten ein. Sie sind jedoch auch pragmatisch bei der Wahl der Programmiersprache und verwenden andere Sprachen, wenn diese für bestimmte Probleme besser geeignet sind.

Hier eine Aufschlüsselung:

### PingCAP (TiDB) und Go

*   **Kein Bedauern:** PingCAP wählte Go für die SQL-Schicht (`tidb-server`) von TiDB aufgrund seines ausgezeichneten Nebenläufigkeitsmodells (Goroutinen und Channels), der einfachen Entwicklung und der starken Standardbibliothek. Diese Funktionen ermöglichten es ihnen, eine komplexe verteilte Datenbank relativ schnell zu bauen.
*   **Anerkannte Herausforderungen:** Obwohl Go zentral für TiDB ist, ist PingCAP sehr transparent bezüglich der Herausforderungen, insbesondere in Bezug auf den Garbage Collector von Go. Ihre Dokumentation und Blogbeiträge diskutieren häufig:
    *   **GC-Pausen:** Sie räumen ein, dass GC-Pausen, selbst wenn sie kurz sind, Latenzschwankungen in einer Hochleistungsdatenbank verursachen können. Sie arbeiten aktiv daran, dies durch Optimierung von `GOGC`, `GOMEMLIMIT` und die Implementierung einer adaptiven GC-Auslösung zu mildern.
    *   **Speicherverwaltung:** Sie bieten detaillierte Anleitungen zur Überwachung der Speichernutzung und zur Fehlerbehebung bei OOM-Problemen, in der Erkenntnis, dass ineffiziente Speichernutzungsmuster in Go zu Problemen führen können.
*   **Strategischer Einsatz von Rust:** PingCAP wählte **Rust** für TiKV, ihre verteilte Key-Value-Speicher-Engine. Dies war kein "Bedauern" über Go, sondern eine **strategische Entscheidung** für die Speicherschicht, in der extrem niedrige Latenzzeiten, vorhersehbare Leistung und fein granulierte Speicherkontrolle von größter Bedeutung sind.
    *   Rusts Ownership- und Borrowing-Modell sowie das Fehlen eines Garbage Collectors sind ideal für die Systemprogrammierung, wo jede Mikrosekunde und jedes Byte zählt.
    *   Sie erkannten, dass der Kompromiss aus Rusts steilerer Lernkurve und längeren Kompilierzeiten für die kritische Speicher-Engine akzeptabel war, für die sich schnell entwickelnde SQL-Schicht jedoch weniger wünschenswert.
*   **Schlussfolgerung für PingCAP:** Sie sehen Go und Rust eindeutig als sich ergänzende Werkzeuge. Go für die höhere Logik und schnelle Iteration, Rust für die Low-Level, leistungskritischen Komponenten.

### Cloudflare und Go

*   **Umfassende Go-Adaption:** Cloudflare war ein früher und begeisterter Anwender von Go. Sie verwenden Go für eine Vielzahl ihrer Dienste, einschließlich DNS-Infrastruktur, SSL-Abwicklung, Lasttest-Tools und viele interne Systeme. Sie haben konsequent positiv über die Nebenläufigkeit, die einfache Bereitstellung und die Entwicklerproduktivität von Go gesprochen.
*   **Evolution, kein Bedauern:** Cloudflare hat seine Sprachverwendung sicherlich diversifiziert, mit einer bemerkenswerten Verschiebung hin zu **Rust** in bestimmten kritischen Bereichen. Dies wird durch Leistungs-, Sicherheits- und Ressourceneffizienzanforderungen getrieben, nicht durch ein "Bedauern" über Go.
    *   **Pingora (Rust):** Ein Paradebeispiel ist die Entwicklung von **Pingora** durch Cloudflare, ein neuer HTTP-Proxy, der in Rust gebaut wurde, um Teile ihrer NGINX-Infrastruktur (die in C geschrieben war) zu ersetzen. Dieser Wechsel zu Rust geschah hauptsächlich aufgrund von:
        *   **Speichersicherheit:** Rusts Garantien gegen häufige Speicherfehler (Pufferüberläufe, Use-after-free), die in C/C++ (wie bei NGINX) weit verbreitet sind. Dies verbessert die Sicherheit und Stabilität erheblich.
        *   **Extreme Leistung:** Für eine Kernkomponente, die Billionen von Anfragen verarbeitet, ermöglichen Rusts "Zero-Cost Abstractions" und die feingranulierte Kontrolle eine noch höhere Leistung und einen geringeren Ressourcenverbrauch, als sie in Go (aufgrund des GC-Overheads) leicht erreichbar sind.
        *   **Verbessertes Developer Experience für Systemprogrammierung:** Obwohl Rust anfangs eine steilere Lernkurve hat, kann seine Strenge und das mächtige Typsystem für Systemingenieure, die an extrem Low-Level-Netzwerkkomponenten arbeiten, langfristig zu robusterem und leichter verständlichem Code führen.
    *   **Go bleibt stark:** Selbst mit Pingora entwickelt und wartet Cloudflare weiterhin viele Dienste in Go. Sie betrachten Go für die meisten ihrer Workloads als "schnell genug" und schätzen seine Entwicklungsgeschwindigkeit und betriebliche Einfachheit.
*   **Schlussfolgerung für Cloudflare:** Cloudflare verfolgt eine Multi-Sprachen-Strategie und wählt das beste Werkzeug für die Aufgabe. Go bleibt eine grundlegende Sprache für sie, insbesondere für Dienste, die von seiner schnellen Entwicklung und Nebenläufigkeit profitieren. Rust wird zunehmend für System-Level-Komponenten verwendet, bei denen maximale Leistung, Speichersicherheit und feingranulierte Kontrolle von größter Bedeutung sind.

Im Wesentlichen sind beide Unternehmen anspruchsvolle Engineering-Organisationen, die die Kompromisse verschiedener Programmiersprachen verstehen. Sie äußern kein "Bedauern" über die Wahl von Go, sondern demonstrieren einen pragmatischen Ansatz, andere Sprachen wie Rust für bestimmte Problemdomänen einzusetzen, in denen ihre Stärken (z. B. das Fehlen eines GC, Speichersicherheit) signifikante Vorteile für kritische Infrastrukturen bieten.
---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Übersicht des Memcached-In-Memory-Caching-Systems
translated: true
type: note
---

### Was ist Memcached?

Memcached ist ein Open-Source, hochleistungsfähiges, verteiltes Speicherobjekt-Caching-System. Es wird hauptsächlich verwendet, um dynamische Webanwendungen (wie solche, die mit PHP-Frameworks wie CodeIgniter erstellt wurden) zu beschleunigen, indem Datenbankabfrageergebnisse, API-Antworten oder andere rechenintensive Daten im RAM zwischengespeichert werden. Dies verringert die Last auf Datenbanken und verbessert die Antwortzeiten der Anwendung. Es ist keine vollwertige Datenbank, sondern ein einfacher Schlüssel-Wert-Speicher, der für die temporäre Datenspeicherung konzipiert ist.

### Wie funktioniert Memcached?

Memcached arbeitet als Daemon (Hintergrundprozess), der auf einem oder mehreren Servern läuft, typischerweise gestartet mit Befehlen wie `memcached -p 11211 -m 64` (Angabe von Port und Speicherlimit). Hier ist eine vereinfachte Übersicht:

1.  **In-Memory-Speicherung**: Es speichert Daten als Schlüssel-Wert-Paare vollständig im RAM für schnellen Zugriff. Jeder Wert kann bis zu 1 MB groß sein, und Schlüssel sind Zeichenketten mit bis zu 250 Zeichen. Daten sind flüchtig – startet der Server neu, gehen die zwischengespeicherten Daten verloren.

2.  **Client-Server-Modell**: Anwendungen (Clients) verbinden sich über TCP- oder UDP-Protokolle mit Memcached. Das bereitgestellte CodeIgniter-Konfigurationssnippet zeigt einen PHP-Setup, der sich mit einer lokalen Memcached-Instanz verbindet:
    *   **Hostname**: '127.0.0.1' (localhost, bedeutet derselbe Server wie Ihre App).
    *   **Port**: '11211' (Der Standardport von Memcached).
    *   **Gewichtung**: '1' (Definiert die Serverpriorität in einem Cluster; höhere Werte bedeuten mehr Last).

3.  **Operationen**:
    *   Set: Speichert ein Schlüssel-Wert-Paar mit einer optionalen Ablaufzeit (z. B. `set app_name 0 3600 13\n"cached_data"` via Telnet).
    *   Get: Ruft einen Wert anhand des Schlüssels ab.
    *   Delete: Entfernt einen Wert anhand des Schlüssels.
    Es verwendet einen einfachen Hashing-Algorithmus, um Schlüssel über Server in einem Cluster-Setup zu verteilen (z. B. konsistentes Hashing, um Serverhinzufügungen/-entfernungen zu handhaben).

4.  **Verdrängung und Skalierung**: Wenn der Speicher voll wird, verwendet es eine LRU-Richtlinie (Least Recently Used), um alte Daten zu verdrängen. Skalierung beinhaltet mehrere Serverinstanzen, die oft automatisch über Tools wie moxi oder externes Sharding ermittelt werden.

Die Leistungsspitze liegt bei Millionen von Operationen pro Sekunde, aber es ist für leseintensive Workloads optimiert. Überwachungstools wie memcached-top können die Nutzung verfolgen.

### Vergleich mit Redis

Während sowohl Memcached als auch Redis In-Memory-Schlüssel-Wert-Datenspeicher sind, die für Caching und Hochgeschwindigkeitsdatenzugriff verwendet werden, unterscheiden sie sich in Funktionen, Architektur und Anwendungsfällen:

| Aspekt                   | Memcached                                                              | Redis                                                                                                                               |
|--------------------------|------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| **Datentypen**           | Einfache Zeichenketten (nur Schlüssel/Werte).                          | Unterstützt Zeichenketten, Hashes, Listen, Sets, Sorted Sets, Bitmaps, Hyperloglogs und mehr. Ermöglicht komplexe Datenstrukturen.  |
| **Persistenz**           | Keine – Daten sind reiner RAM; gehen bei Neustart verloren.            | Optionale Persistenz (AOF oder RDB-Snapshots) auf die Festplatte, ermöglicht Datenwiederherstellung.                                |
| **Verdrängung**          | Nur LRU.                                                               | LRU, LFU (Least Frequently Used) oder volatile TTL-basierte Verdrängung.                                                            |
| **Operationen**          | Einfache set/get/delete/multiget.                                      | Tausende von Befehlen (z. B. Pub/Sub, Transaktionen, Lua-Skripting, geospatiale Abfragen). Unterstützt atomare Operationen.          |
| **Leistung**             | Etwas schneller für einfaches Lesen/Schreiben (multigets helfen).      | Exzellent insgesamt, aber etwas Overhead für komplexe Strukturen. Benchmarks zeigen Memcached bei reinem Caching in einfachen Szenarien leicht vorn. |
| **Skalierung & Clustering** | Eingebaut via konsistentem Hashing; kein natives Clustering (externe Partitionierung verwenden). | Unterstützt natives Clustering, Replikation (Master-Slave) und Redis Cluster für automatische Partitionierung.                       |
| **Anwendungsfälle**      | Ideal für Web-App-Caching (z. B. Sitzungs- oder Abfrage-Caches), wie in CodeIgniter-Setups. Einfach und leichtgewichtig. | Breiter: Caching, Sitzungsspeicher, Nachrichtenwarteschlangen, Echtzeit-Analytik oder sogar als vollwertige Datenbankalternative.    |
| **Speichereffizienz**    | Effizient für Daten fester Größe; keine Komprimierung.                 | Besser für große Datensätze mit Komprimierungsoptionen (Redis 5+).                                                                  |
| **Protokoll**            | Eigene binäre/Text-Protokolle.                                         | RESP (Redis Serialization Protocol) mit besserer Fehlerbehandlung.                                                                  |
| **Lizenz & Ökosystem**   | Open-Source (BSD), weit verbreitet in LAMP-Stacks.                     | Open-Source (BSD), größere Community mit Tools wie RedisInsight.                                                                    |

Zusammenfassend sollte Memcached für Einfachheit und Geschwindigkeit beim grundlegenden Caching (wie in Ihrer CodeIgniter-Konfiguration gezeigt) gewählt werden. Entscheiden Sie sich für Redis, wenn Sie Persistenz, erweiterte Datentypen oder Funktionen wie Pub/Sub-Messaging benötigen. Beim Migrieren von Memcached bieten Projekte wie redis-memcached Kompatibilitätsschichten, aber Redis ersetzt Memcached oft aufgrund seiner Vielseitigkeit. Für CodeIgniter speziell erlaubt die Konfiguration ein nahtloses Wechseln zwischen Treibern.
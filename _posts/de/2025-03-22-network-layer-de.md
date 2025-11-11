---
audio: false
generated: true
lang: de
layout: post
title: Netzwerkschicht
translated: true
type: note
---

Okay, tauchen wir ein in ein detailliertes Tutorial zur Vermittlungsschicht, speziell zugeschnitten für den Kurs Computernetzwerktechnologie im chinesischen Selbststudiumsexamenssystem (自考). Dieses Kapitel ist entscheidend für das Verständnis, wie Daten über Netzwerke reisen.

## Vermittlungsschicht Tutorial

Die Vermittlungsschicht ist die dritte Schicht im OSI-Modell und im TCP/IP-Modell. Ihre Hauptaufgabe ist es, die Bewegung von Datenpaketen von einem Quellhost zu einem Zielhost über ein oder mehrere Netzwerke hinweg zu ermöglichen. Man kann sie sich wie den Postdienst für das Internet vorstellen – sie findet die beste Route und stellt sicher, dass Ihr "Paket" (Datenpaket) die richtige Adresse erreicht.

Hier ist eine Aufschlüsselung der Schlüsselthemen in diesem Kapitel:

### 1. Funktionen der Vermittlungsschicht

Die Vermittlungsschicht erfüllt drei Hauptfunktionen:

#### a) Logische Adressierung

*   **Zweck:** Jeden Host in einem Netzwerk eindeutig zu identifizieren. Dies unterscheidet sich von der physikalischen Adresse (MAC-Adresse), die ein Gerät innerhalb eines lokalen Netzwerks identifiziert. Logische Adressen sind hierarchisch und ermöglichen ein effizientes Routing.
*   **Schlüsselkonzept:** IP-Adressen (Internet Protocol Adressen) sind die primäre Form der logischen Adressierung, die in der Vermittlungsschicht verwendet wird.
*   **Analogie:** Denken Sie an Ihre Hausadresse. Es ist eine logische Adresse, die dem Postdienst hilft, Ihr spezifisches Haus innerhalb einer Stadt und eines Landes zu finden, unabhängig vom physischen Standort der Postfiliale.

#### b) Routing

*   **Zweck:** Den besten Pfad für ein Datenpaket zu bestimmen, um von der Quelle zum Ziel zu gelangen. Dies beinhaltet die Auswahl einer Abfolge von Netzwerkgeräten (Router), die das Paket durchlaufen wird.
*   **Schlüsselkonzept:** Routing-Algorithmen werden von Routern verwendet, um Routing-Tabellen zu erstellen und zu pflegen, die Informationen über die besten Pfade zu verschiedenen Netzwerken enthalten.
*   **Analogie:** Stellen Sie sich vor, Sie planen eine Autoreise. Sie schauen auf eine Karte oder verwenden ein GPS, um die beste Route zu Ihrem Ziel zu finden, unter Berücksichtigung von Faktoren wie Entfernung und Verkehr. Router machen etwas Ähnliches für Datenpakete.

#### c) Weiterleitung (Forwarding)

*   **Zweck:** Der tatsächliche Prozess, ein Datenpaket von einem Eingangsport eines Routers zum entsprechenden Ausgangsport zu bewegen, basierend auf der Routing-Entscheidung.
*   **Schlüsselkonzept:** Wenn ein Router ein Paket empfängt, prüft er die Ziel-IP-Adresse und konsultiert seine Routing-Tabelle, um den nächsten Hop (einen anderen Router oder den Zielhost) zu bestimmen.
*   **Analogie:** Sobald Sie Ihre Route geplant haben, ist das Weiterlegen wie das tatsächliche Fahren Ihres Autos entlang dieser Route, von einem Punkt zum nächsten.

### 2. IP-Adressierung

IP-Adressen sind grundlegend für die Vermittlungsschicht. Es gibt zwei Hauptversionen: IPv4 und IPv6.

#### a) IPv4-Struktur

*   **Format:** Eine 32-Bit numerische Adresse, geschrieben in punktierter Dezimalnotation (z.B. 192.168.1.10). Sie ist in vier 8-Bit-Oktette unterteilt.
*   **Adressklassen (historisch):** Während sie heute aufgrund von Classless Inter-Domain Routing (CIDR) größtenteils veraltet sind, kann das Verständnis der historischen Klassen (A, B, C, D, E) für das Grundlagenwissen hilfreich sein.
    *   **Klasse A:** Große Netzwerke (erstes Oktett 1-126).
    *   **Klasse B:** Mittelgroße Netzwerke (erstes Oktett 128-191).
    *   **Klasse C:** Kleine Netzwerke (erstes Oktett 192-223).
    *   **Klasse D:** Multicast-Adressen (erstes Oktett 224-239).
    *   **Klasse E:** Reserviert für experimentelle Nutzung (erstes Oktett 240-255).
*   **Netzwerk-ID und Host-ID:** Eine IPv4-Adresse besteht aus einer Netzwerk-ID (identifiziert das Netzwerk) und einer Host-ID (identifiziert ein bestimmtes Gerät innerhalb dieses Netzwerks). Die Trennung zwischen diesen IDs hängt von der Adressklasse (oder der Subnetzmaske bei CIDR) ab.
*   **Spezielle IPv4-Adressen:**
    *   **0.0.0.0:** Repräsentiert das aktuelle Netzwerk.
    *   **127.0.0.1 (Loopback-Adresse):** Wird zum Testen des Netzwerkstacks des lokalen Rechners verwendet.
    *   **Private IP-Adressen:** Bereiche, die für die Verwendung in privaten Netzwerken reserviert sind (z.B. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16). Diese Adressen sind nicht über das öffentliche Internet routbar.
    *   **Öffentliche IP-Adressen:** Adressen, die über das öffentliche Internet routbar sind.

#### b) IPv6-Struktur

*   **Format:** Eine 128-Bit numerische Adresse, geschrieben im Hexadezimalformat, gruppiert in acht 16-Bit-Segmente, die durch Doppelpunkte getrennt sind (z.B. 2001:0db8:85a3:0000:0000:8a2e:0370:7334).
*   **Vorteile gegenüber IPv4:** Größerer Adressraum (löst die IPv4-Adressknappheit), verbesserte Sicherheit (IPsec ist oft integriert), vereinfachtes Header-Format, bessere Unterstützung für mobile Geräte.
*   **Adressdarstellung:**
    *   **Führende Nullen:** Führende Nullen innerhalb eines Segments können weggelassen werden (z.B. kann 0000 als 0 geschrieben werden).
    *   **Doppelter Doppelpunkt:** Ein einzelner doppelter Doppelpunkt (::) kann verwendet werden, um ein oder mehrere aufeinanderfolgende Segmente mit lauter Nullen darzustellen. Dies kann nur einmal in einer Adresse verwendet werden.
*   **Arten von IPv6-Adressen:**
    *   **Unicast:** Identifiziert eine einzelne Schnittstelle.
    *   **Multicast:** Identifiziert eine Gruppe von Schnittstellen.
    *   **Anycast:** Identifiziert eine Menge von Schnittstellen, wobei Pakete an die nächstgelegene Schnittstelle in der Menge geliefert werden.
*   **Link-Local-Adressen (fe80::/10):** Werden für die Kommunikation innerhalb eines einzelnen Netzwerk-Links verwendet.
*   **Globale Unicast-Adressen:** Global routbare Adressen im Internet.

#### c) Subnetting

*   **Zweck:** Ein größeres Netzwerk in kleinere, besser handhabbare Teilnetzwerke (Subnetze) aufzuteilen. Dies hilft bei der Organisation von Netzwerken, verbessert die Sicherheit und optimiert die Netzwerkleistung.
*   **Mechanismus:** Subnetting wird erreicht, indem Bits vom Host-Teil einer IP-Adresse "geliehen" und zur Erstellung von Subnetz-IDs verwendet werden. Dies geschieht mit einer **Subnetzmaske**.
*   **Subnetzmaske:** Eine 32-Bit-Zahl (für IPv4), die den Netzwerk- und Subnetz-Teil einer IP-Adresse identifiziert. Sie hat eine fortlaufende Folge von 1en für die Netzwerk- und Subnetz-Bits, gefolgt von einer fortlaufenden Folge von 0en für die Host-Bits.
*   **CIDR-Notation (Classless Inter-Domain Routing):** Eine flexiblere Art, Netzwerkpräfixe darzustellen, unter Verwendung eines Schrägstrichs gefolgt von der Anzahl der Netzwerk-Bits (z.B. 192.168.1.0/24 zeigt an, dass die ersten 24 Bits das Netzwerk repräsentieren). Dies ist die heute verwendete Standardmethode.
*   **Subnetting-Berechnung (IPv4):**
    1.  Bestimmen Sie die Anzahl der benötigten Subnetze.
    2.  Bestimmen Sie die Anzahl der benötigten Hosts pro Subnetz.
    3.  Berechnen Sie die Anzahl der benötigten Bits für die Subnetze und Hosts.
    4.  Bestimmen Sie die Subnetzmaske.
    5.  Identifizieren Sie die gültigen Subnetzadressen, Broadcast-Adressen und nutzbare Host-Bereiche für jedes Subnetz.
*   **Subnetting in IPv6:** Während das Konzept des Subnettings in IPv6 existiert, macht der riesige Adressraum es weniger zu einer Frage der Adresseinsparung und mehr zu einer Frage der Netzwerkorganisation. IPv6-Subnetze sind typischerweise eine feste Größe (/64).

### 3. Routing-Algorithmen

Routing-Algorithmen werden von Routern verwendet, um den besten Pfad für Datenpakete zu bestimmen. Sie können grob klassifiziert werden in:

#### a) Statisches vs. Dynamisches Routing

*   **Statisches Routing:**
    *   Routing-Tabellen werden manuell vom Netzwerkadministrator konfiguriert.
    *   Einfach zu implementieren für kleine, stabile Netzwerke.
    *   Nicht anpassungsfähig an Netzwerkänderungen oder -ausfälle.
    *   Geeignet für spezifische Szenarien wie die Verbindung zu einem einzelnen entfernten Netzwerk.
*   **Dynamisches Routing:**
    *   Router lernen automatisch über die Netzwerktopologie und aktualisieren ihre Routing-Tabellen, indem sie Informationen mit anderen Routern austauschen.
    *   Anfänglich komplexer zu konfigurieren, aber hochgradig anpassungsfähig an Netzwerkänderungen und -ausfälle.
    *   Skalierbar für größere und komplexere Netzwerke.

#### b) Distance-Vector-Routing

*   **Prinzip:** Jeder Router verwaltet eine Routing-Tabelle, die die beste bekannte Entfernung (z.B. Anzahl der Hops) und die Richtung (nächster Hop-Router) zu jedem Zielnetzwerk auflistet.
*   **Informationsaustausch:** Router tauschen periodisch ihre gesamten Routing-Tabellen mit ihren direkt verbundenen Nachbarn aus.
*   **Algorithmus-Beispiel:** Der **Bellman-Ford-Algorithmus** ist ein häufig verwendeter Algorithmus in Distance-Vector-Routing-Protokollen.
*   **Protokolle:** RIP (Routing Information Protocol) ist ein bekanntes Beispiel für ein Distance-Vector-Routing-Protokoll.
*   **Einschränkungen:** Kann unter langsamer Konvergenz leiden (es dauert eine Weile, bis sich das Netzwerk an Änderungen anpasst) und dem "Count-to-Infinity"-Problem (Routing-Schleifen können auftreten).

#### c) Link-State-Routing

*   **Prinzip:** Jeder Router verwaltet eine vollständige Karte der Netzwerktopologie. Er kennt alle Router und die Verbindungen zwischen ihnen, zusammen mit den Kosten jeder Verbindung.
*   **Informationsaustausch:** Router tauschen Informationen über den Zustand ihrer direkt verbundenen Links mit allen anderen Routern im Netzwerk aus. Diese Information wird Link State Advertisement (LSA) genannt.
*   **Algorithmus-Beispiel:** Der **Dijkstra-Algorithmus** (Shortest Path First - SPF) wird von jedem Router verwendet, um den kürzesten Pfad zu allen anderen Zielen basierend auf den gesammelten Link-State-Informationen zu berechnen.
*   **Protokolle:** OSPF (Open Shortest Path First) und IS-IS (Intermediate System to Intermediate System) sind beliebte Link-State-Routing-Protokolle.
*   **Vorteile:** Schnellere Konvergenz, weniger anfällig für Routing-Schleifen im Vergleich zu Distance-Vector-Routing.

### 4. Protokolle

Mehrere Schlüsselprotokolle arbeiten auf der Vermittlungsschicht:

#### a) IP (Internet Protocol)

*   **Kernprotokoll:** Das grundlegende Protokoll, das für die Adressierung und das Routing von Paketen über Netzwerke hinweg verantwortlich ist.
*   **Verbindungslos und unzuverlässig:** IP bietet einen verbindungslosen Dienst (keine vorherige Verbindungsherstellung) und ist unzuverlässig (keine Zustellgarantie). Fehlererkennung wird durchgeführt, aber die Fehlerbehebung ist die Verantwortung von Protokollen höherer Schichten (wie TCP).
*   **Paketformat:** IP definiert die Struktur von IP-Paketen (Datagrammen), einschließlich Quell- und Ziel-IP-Adressen, Header-Informationen (z.B. Time-to-Live - TTL) und der Nutzlast (Daten von höheren Schichten).

#### b) ICMP (Internet Control Message Protocol)

*   **Zweck:** Wird zum Senden von Fehlermeldungen und Steuer-/Informationsnachrichten zwischen Netzwerkgeräten verwendet.
*   **Funktionalität:** ICMP-Nachrichten werden verwendet, um Fehler zu melden (z.B. Ziel nicht erreichbar, Zeit überschritten), Informationen anzufordern (z.B. Echo-Request/Reply, verwendet vom `ping`-Befehl) und andere Netzwerkdiagnosen durchzuführen.
*   **Beispiele:** Das `ping`-Utility verwendet ICMP Echo-Requests und -Replies, um die Netzwerkverbindung zu testen. `traceroute` (oder `tracert` unter Windows) verwendet ICMP-Zeit-überschritten-Nachrichten, um den Pfad eines Pakets nachzuverfolgen.

#### c) ARP (Address Resolution Protocol)

*   **Zweck:** Wird verwendet, um eine logische Adresse (IP-Adresse) in eine physikalische Adresse (MAC-Adresse) innerhalb desselben lokalen Netzwerksegments aufzulösen.
*   **Prozess:** Wenn ein Host ein Paket an einen anderen Host im selben Netzwerk senden muss, kennt er die Ziel-IP-Adresse, benötigt aber die Ziel-MAC-Adresse, um das Paket auf der Sicherungsschicht zu framen. Der sendende Host sendet eine ARP-Anfrage (Broadcast) mit der Ziel-IP-Adresse. Der Host mit dieser IP-Adresse antwortet mit einer ARP-Antwort, die seine MAC-Adresse enthält.
*   **ARP-Cache:** Hosts pflegen einen ARP-Cache, um kürzlich aufgelöste IP-zu-MAC-Adresszuordnungen zu speichern, um ARP-Anfragen für jede Kommunikation zu vermeiden.

### 5. Netzwerkgeräte

Die Vermittlungsschicht umfasst primär zwei Schlüsseltypen von Netzwerkgeräten:

#### a) Router

*   **Primärfunktion:** Datenpakete zwischen verschiedenen Netzwerken basierend auf ihren Ziel-IP-Adressen weiterzuleiten.
*   **Schlüsselmerkmale:**
    *   Pflegen Routing-Tabellen, um den besten Pfad für Pakete zu bestimmen.
    *   Verbinden verschiedene Netzwerksegmente (können unterschiedliche Netzwerktechnologien sein).
    *   Führen Paketweiterleitung basierend auf Routing-Entscheidungen durch.
    *   Können Sicherheitsfunktionen wie Firewalls und Zugriffssteuerungslisten (ACLs) implementieren.

#### b) Gateways

*   **Weiterer Begriff:** Ein Gateway ist ein Gerät, das als Eintrittspunkt zu einem anderen Netzwerk dient. Es kann ein Router, eine Firewall oder eine andere Art von Gerät sein.
*   **Standardgateway:** Im Kontext der IP-Netzwerke ist das Standardgateway ein Router im lokalen Netzwerk, den ein Host verwendet, um Datenverkehr an Ziele außerhalb seines eigenen Netzwerks zu senden.
*   **Protokollkonvertierung:** Gateways können auch Protokollkonvertierung zwischen verschiedenen Netzwerkarchitekturen oder Protokollen durchführen, obwohl dies für einfaches IP-Routing weniger üblich ist.

## Wichtige Erkenntnisse für die Selbststudiumsprüfung

*   **Verstehen Sie die Kernfunktionen:** Logische Adressierung (IP-Adressen), Routing (Pfadauswahl) und Weiterleitung (Paketbewegung).
*   **Beherrschen Sie die IP-Adressierung:** Seien Sie in der Lage, die Struktur von IPv4- und IPv6-Adressen zu erklären, Subnetting-Konzepte und -Berechnungen zu verstehen (insbesondere für IPv4) und die verschiedenen Arten von IP-Adressen zu kennen.
*   **Unterscheiden Sie Routing-Algorithmen:** Verstehen Sie die Unterschiede zwischen statischem und dynamischem Routing und seien Sie in der Lage, die grundlegenden Prinzipien von Distance-Vector- und Link-State-Routing-Algorithmen zu erklären. Kennen Sie die gängigen Protokolle, die mit jedem verbunden sind.
*   **Kennen Sie die wichtigsten Vermittlungsschicht-Protokolle:** Verstehen Sie den Zweck und den grundlegenden Betrieb von IP, ICMP und ARP.
*   **Identifizieren Sie die Rolle von Netzwerkgeräten:** Verstehen Sie klar die Funktion von Routern und Gateways in der Vermittlungsschicht.

## Übung und Wiederholung

*   **Arbeiten Sie Beispiele durch:** Üben Sie Subnetting-Berechnungen für IPv4.
*   **Vergleichen und kontrastieren Sie:** Erstellen Sie Tabellen, um verschiedene Routing-Algorithmen und IP-Adressversionen zu vergleichen.
*   **Beziehen Sie es auf reale Szenarien:** Denken Sie darüber nach, wie diese Konzepte auf Ihre eigene Internetnutzung und Netzwerkeinrichtungen zutreffen.
*   **Überprüfen Sie alte Prüfungsunterlagen:** Verstehen Sie die Arten von Fragen, die typischerweise zu diesem Thema in der chinesischen Selbststudiumsprüfung gestellt werden.

Durch ein gründliches Verständnis dieser Konzepte werden Sie eine starke Grundlage in der Vermittlungsschicht aufbauen, die für weiterführende Studien in der Computernetzwerktechnik unerlässlich ist. Viel Erfolg bei Ihren Studien!
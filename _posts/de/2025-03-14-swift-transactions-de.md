---
audio: false
generated: true
lang: de
layout: post
title: Wie SWIFT-Transaktionen funktionieren
translated: true
type: note
---

### Wie funktionieren SWIFT-Transaktionen über mehrere Banken hinweg?

SWIFT, was für **Society for Worldwide Interbank Financial Telecommunication** steht, ist ein globales Netzwerk, das es Banken ermöglicht, Informationen über Finanztransaktionen sicher und effizient auszutauschen. Es ist wichtig zu verstehen, dass SWIFT selbst kein Geld bewegt; vielmehr ermöglicht es die Kommunikation von Anweisungen zwischen Banken, um diese Überweisungen durchzuführen. Hier ist eine detaillierte Erklärung, wie SWIFT-Transaktionen funktionieren, einschließlich der Rolle von SWIFT-Codes und wie Banken sich in das SWIFT-System integrieren, insbesondere über mehrere Banken hinweg.

---

#### **Was ist eine SWIFT-Transaktion?**
Eine SWIFT-Transaktion bezieht sich auf den Prozess, standardisierte Nachrichten über das SWIFT-Netzwerk zu senden, um Banken anzuweisen, wie Gelder von einem Konto auf ein anderes übertragen werden sollen. Diese Nachrichten enthalten kritische Details wie den Betrag, die Währung, Informationen zu den Konten von Absender und Empfänger sowie die beteiligten Banken. Die tatsächliche Bewegung des Geldes erfolgt separat über Bankenabwicklungssysteme, die wir später betrachten werden.

Wenn Sie beispielsweise Geld von einer Bank in den USA an eine Bank in Deutschland senden möchten, stellt SWIFT sicher, dass die Anweisungen genau und sicher zwischen den beiden Banken kommuniziert werden, selbst wenn diese keine direkte Beziehung zueinander haben.

---

#### **Die Rolle von SWIFT-Codes**
Jede Bank, die am SWIFT-Netzwerk teilnimmt, hat eine eindeutige Kennung, die **SWIFT-Code** (auch bekannt als **Bank Identifier Code** oder **BIC**) genannt wird. Dieser Code, typischerweise 8 oder 11 Zeichen lang, identifiziert die spezifische Bank und oft auch ihre Filiale in einer Transaktion. Zum Beispiel:
- **Bank A in den USA** könnte einen SWIFT-Code wie `BOFAUS3N` haben.
- **Bank B in Deutschland** könnte einen Code wie `DEUTDEFF` haben.

Wenn Sie eine Überweisung initiieren, geben Sie den SWIFT-Code der Empfängerbank an, um sicherzustellen, dass die Anweisungen die richtige Institution erreichen.

---

#### **Wie SWIFT-Transaktionen Schritt für Schritt funktionieren**
Lassen Sie uns den Ablauf einer SWIFT-Transaktion über mehrere Banken hinweg anhand eines einfachen Beispiels aufschlüsseln: Senden von 1.000 US-Dollar von Bank A (in den USA) an Bank B (in Deutschland).

1. **Initiierung**  
   Sie übermitteln Bank A die Überweisungsdetails:
   - Betrag: 1.000 US-Dollar
   - Kontonummer des Empfängers bei Bank B
   - SWIFT-Code der Bank B (z.B. `DEUTDEFF`)
   Bank A könnte die 1.000 US-Dollar basierend auf dem Wechselkurs in Euro umtauschen (z.B. 850 Euro), dies kann jedoch je nach den Richtlinien der Banken variieren.

2. **Nachrichtenerstellung**  
   Bank A erstellt eine standardisierte SWIFT-Nachricht, wie z.B. eine **MT103** (verwendet für einzelne Kundengutschriften). Diese Nachricht enthält:
   - Absenderdetails (Bank A und Ihr Konto)
   - Empfängerdetails (Bank B und das Konto Ihres Freundes)
   - Betrag und Währung (z.B. 850 Euro)
   - Anweisungen für die Bearbeitung der Zahlung

3. **Senden der Nachricht**  
   Bank A überträgt die MT103-Nachricht über das SWIFT-Netzwerk. Das Netzwerk stellt eine sichere Zustellung durch Verschlüsselungs- und Authentifizierungsmaßnahmen sicher.

4. **Weiterleitung über Banken**  
   - **Direkte Beziehung**: Wenn Bank A und Bank B Konten bei einander unterhalten, sendet Bank A die Nachricht direkt an Bank B.
   - **Zwischenbanken**: Wenn keine direkte Beziehung besteht, wird die Nachricht über eine oder mehrere **Korrespondenzbanken** (z.B. Bank C) weitergeleitet. Zum Beispiel:
     - Bank A sendet die Nachricht an Bank C und weist sie an, das Konto von Bank A bei Bank C zu belasten und das Konto von Bank B bei Bank C zu gutschreiben.
     - Bank C leitet die Anweisungen an Bank B weiter und teilt mit, dass die Gelder für das Konto Ihres Freundes bestimmt sind.
   Zwischenbanken sind bei internationalen Überweisungen üblich, wenn keine direkten Beziehungen bestehen.

5. **Empfang und Verarbeitung**  
   Bank B empfängt die SWIFT-Nachricht, prüft die Details und bereitet vor, das Konto Ihres Freundes mit 850 Euro zu gutschreiben.

6. **Abrechnung der Gelder**  
   Da SWIFT nur die Nachrichtenübermittlung abwickelt, erfolgt die tatsächliche Geldbewegung über Abwicklungsmechanismen:
   - **Direkte Konten**: Wenn Bank A ein **Nostro-Konto** (ein Konto in Euro bei Bank B) unterhält, belastet Bank B dieses und schreibt das Konto Ihres Freundes gut.
   - **Korrespondenzbankgeschäft**: Wenn eine Zwischenbank (Bank C) beteiligt ist, gleicht Bank A die Beträge mit Bank C ab, und Bank C gleicht sie mit Bank B über ihre jeweiligen Konten ab.
   - **Zentrale Clearing-Systeme**: Für einige Währungen (z.B. Euro in der Eurozone) kann die Abwicklung über Systeme wie **TARGET2** erfolgen.

7. **Abschluss**  
   Das Konto Ihres Freundes bei Bank B wird mit 850 Euro gutgeschrieben. Gebühren können in verschiedenen Phasen abgezogen werden (von Bank A, Zwischenbanken oder Bank B), und der Prozess kann je nach beteiligten Banken und Zwischenstellen einige Stunden bis mehrere Tage dauern.

---

#### **Wie Banken sich in das SWIFT-System integrieren**
Um an SWIFT-Transaktionen teilzunehmen, müssen Banken sich in das Netzwerk integrieren. So machen sie das:

- **Mitgliedschaft**: Banken werden Mitglieder bei SWIFT und verpflichten sich, deren Regeln und Standards einzuhalten.
- **Infrastruktur**: Sie installieren SWIFT-zugelassene Software und Hardware, um eine Verbindung zum SWIFT-Netzwerk herzustellen, einem privaten, sicheren System, das vom öffentlichen Internet getrennt ist.
- **SWIFT-Codes**: Jeder Bank wird ein eindeutiger SWIFT-Code zugewiesen, um sie in Transaktionen zu identifizieren.
- **Nachrichtenstandards**: Banken verwenden standardisierte Nachrichtenformate (z.B. MT103) mit spezifischen Feldern, um Kompatibilität im gesamten Netzwerk sicherzustellen.
- **Sicherheit**: SWIFT schreibt Verschlüsselung, digitale Signaturen und die Einhaltung von Sicherheitsprotokollen vor, um vor Betrug und Manipulation zu schützen.
- **Zusätzliche Dienstleistungen**: Über Zahlungen hinaus nutzen Banken SWIFT für Handelsfinanzierung, Wertpapiergeschäfte und administrative Nachrichten, was eine weitere Integration für diese Funktionen erfordert.

---

#### **Wichtige Merkmale und Überlegungen**
- **Standardisierung**: Die Verwendung strukturierter Nachrichten (wie MT103) durch SWIFT stellt sicher, dass alle Banken Anweisungen gleich interpretieren.
- **Sicherheit**: Das Netzwerk setzt robuste Maßnahmen ein, um Transaktionsdaten zu schützen.
- **Gebühren und Dauer**: Zwischenbanken können Gebühren erheben, und die Bearbeitungszeiten variieren je nach Anzahl der beteiligten Banken.
- **Moderne Verbesserungen**: Initiativen wie **SWIFT gpi** (Global Payments Innovation) verbessern Transparenz und Geschwindigkeit durch End-to-End-Verfolgung und schnellere Abwicklung.

---

#### **Zusammenfassung**
SWIFT-Transaktionen funktionieren, indem sie Banken ermöglichen, sichere, standardisierte Nachrichten (über SWIFT-Codes) zu senden, um grenzüberschreitende Geldtransfers anzuweisen. Der Prozess umfasst das Erstellen und Weiterleiten von Nachrichten – manchmal über Zwischenbanken – und die separate Abwicklung der Gelder über direkte Konten, Korrespondenzbeziehungen oder Clearing-Systeme. Banken integrieren sich in SWIFT, indem sie Mitglieder werden, die notwendige Infrastruktur aufbauen und sich an deren Protokolle halten. Dieses System stellt sicher, dass Geld zuverlässig zwischen Konten bewegt wird, selbst über mehrere Banken weltweit hinweg.
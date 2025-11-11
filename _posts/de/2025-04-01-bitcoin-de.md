---
audio: false
generated: true
lang: de
layout: post
title: Wie Bitcoin funktioniert
translated: true
type: note
---

Technisch funktioniert Bitcoin durch eine Kombination aus Kryptografie, einem Peer-to-Peer-Netzwerk und einem Konsensmechanismus namens Proof-of-Work (PoW). Hier ist eine Aufschlüsselung der wichtigsten Komponenten und Prozesse:

**1. Kryptografische Grundlagen:**

*   **Hashing (SHA-256):** Bitcoin ist stark auf die kryptografische Hash-Funktion SHA-256 angewiesen. Diese Funktion nimmt beliebige Eingabedaten und erzeugt eine feste 256-Bit-Ausgabe (den Hash). Wichtige Eigenschaften von SHA-256, die in Bitcoin verwendet werden, sind:
    *   **Deterministisch:** Die gleiche Eingabe erzeugt immer die gleiche Ausgabe.
    *   **Einwegfunktion:** Es ist rechnerisch nicht praktikabel, den Prozess umzukehren und die Eingabe aus der Ausgabe zu ermitteln.
    *   **Kollisionsresistent:** Es ist extrem schwierig, zwei verschiedene Eingaben zu finden, die die gleiche Ausgabe erzeugen.
*   **Digitale Signaturen (ECDSA):** Bitcoin verwendet den Elliptic Curve Digital Signature Algorithm (ECDSA) zur Absicherung von Transaktionen. Jeder Bitcoin-Nutzer hat ein Paar kryptografischer Schlüssel:
    *   **Privater Schlüssel:** Ein geheimer Schlüssel, der es dem Nutzer ermöglicht, Transaktionen zu autorisieren (zu signieren).
    *   **Öffentlicher Schlüssel:** Ein aus dem privaten Schlüssel abgeleiteter Schlüssel, der mit anderen geteilt werden kann. Er wird verwendet, um die Authentizität von Transaktionen zu überprüfen, die mit dem entsprechenden privaten Schlüssel signiert wurden.
*   **Bitcoin-Adressen:** Diese werden aus öffentlichen Schlüsseln durch eine Reihe von Hashing- und Codierungsschritten abgeleitet. Sie sind die "Adressen", die Nutzer teilen, um Bitcoin zu empfangen.

**2. Die Blockchain:**

*   **Verteiltes Hauptbuch (Distributed Ledger):** Bitcoin führt ein öffentliches, dezentrales Hauptbuch, die sogenannte Blockchain. Dieses Hauptbuch zeichnet jede Bitcoin-Transaktion in chronologischer und transparenter Weise auf.
*   **Blöcke:** Transaktionen werden in Blöcken gruppiert. Jeder Block enthält:
    *   Eine Reihe verifizierter Transaktionen.
    *   Eine Referenz auf den Hash des **vorherigen Blocks** in der Kette. Dies erzeugt die kettenartige Struktur.
    *   Einen **Nonce**: Eine Zufallszahl, die im Mining-Prozess verwendet wird.
    *   Einen **Zeitstempel**.
    *   Den Hash des aktuellen Blocks selbst.
*   **Unveränderbarkeit:** Sobald ein Block der Blockchain hinzugefügt wurde, ist es extrem schwierig, ihn zu verändern, da dies die Neuberechnung der Hashes dieses Blocks und aller nachfolgenden Blöcke erfordern würde. Dies wäre für einen Angreifer, der weniger als 51 % der Rechenleistung des Netzwerks kontrolliert, rechnerisch nicht praktikabel.

**3. Transaktionen:**

*   **Struktur:** Eine Bitcoin-Transaktion enthält typischerweise:
    *   **Inputs:** Verweise auf frühere Transaktionen, bei denen der Absender die Bitcoin erhalten hat, die er jetzt ausgibt. Dies sind im Wesentlichen Verweise auf bestimmte "unverbrauchte Transaktionsausgaben" (UTXOs).
    *   **Outputs:** Geben die Bitcoin-Adresse(n) des Empfängers und den Betrag an, der an jede Adresse gesendet wird. Eine Transaktion kann mehrere Outputs haben.
    *   **Signatur:** Eine digitale Signatur, die mit dem privaten Schlüssel des Absenders erstellt wurde. Dies beweist, dass der Eigentümer der Bitcoin die Transaktion autorisiert hat.
*   **Broadcasting:** Sobald eine Transaktion erstellt und signiert ist, wird sie an das Bitcoin-Peer-to-Peer-Netzwerk gesendet.

**4. Mining und Proof-of-Work:**

*   **Miner:** Dies sind Knoten im Bitcoin-Netzwerk, die die Arbeit der Verifizierung und Hinzufügung neuer Transaktionen zur Blockchain übernehmen.
*   **Transaktionsverifizierung:** Miner sammeln ausstehende, unbestätigte Transaktionen aus dem Netzwerk und überprüfen deren Gültigkeit (z. B. ob der Absender genug Bitcoin zum Ausgeben hat und ob die digitalen Signaturen gültig sind).
*   **Erstellen eines Blocks:** Miner bündeln diese verifizierten Transaktionen in einem neuen Block. Sie fügen auch eine spezielle Transaktion hinzu, die "Coinbase-Transaktion", die sie mit neu geschürften Bitcoin und allen Transaktionsgebühren belohnt, die von den Absendern der im Block enthaltenen Transaktionen gezahlt wurden.
*   **Proof-of-Work (PoW):** Um einen neuen Block zur Blockchain hinzuzufügen, müssen Miner ein rechnerisch schwieriges Rätsel mit dem SHA-256-Algorithmus lösen. Dieser Prozess wird "Mining" genannt.
    *   Miner verändern wiederholt den **Nonce** (eine Zufallszahl) im Block-Header.
    *   Für jeden Nonce berechnen sie den SHA-256-Hash des gesamten Block-Headers.
    *   Das Ziel ist es, einen Nonce zu finden, der zu einem Hash führt, der mit einer bestimmten Anzahl von führenden Nullen beginnt. Die Anzahl der erforderlichen führenden Nullen wird durch die **Schwierigkeit** des Bitcoin-Netzwerks bestimmt.
    *   Das Finden eines solchen Hashs ist eine Frage von Trial-and-Error und erfordert erhebliche Rechenleistung.
*   **Blockvalidierung und Konsens:** Sobald ein Miner einen gültigen Hash (den "Proof-of-Work") gefunden hat, sendet er den neuen Block an den Rest des Netzwerks. Andere Knoten im Netzwerk überprüfen dann:
    *   Ob die Transaktionen im Block gültig sind.
    *   Ob der Hash des Blocks korrekt ist.
    *   Ob der Hash dem aktuellen Schwierigkeitsziel entspricht.
    *   Ob die Referenz auf den Hash des vorherigen Blocks korrekt ist.
*   **Hinzufügen zur Blockchain:** Wenn der Block gültig ist, akzeptieren ihn andere Knoten und fügen ihn ihrer Kopie der Blockchain hinzu, wodurch die Kette erweitert wird. Dieser Prozess stellt sicher, dass alle Knoten die Reihenfolge und Gültigkeit der Transaktionen gemeinsam bestätigen. Die längste Kette gilt als die autoritative Version.

**5. Anreize:**

*   **Blockbelohnung:** Miner, die erfolgreich einen neuen Block minen, werden mit einer bestimmten Menge neu geschaffener Bitcoin belohnt (derzeit 3,125 BTC, die sich ungefähr alle vier Jahre in einem Ereignis namens "Halving" halbiert).
*   **Transaktionsgebühren:** Miner sammeln auch die Transaktionsgebühren ein, die Nutzer freiwillig beim Senden von Bitcoin hinzufügen. Diese Gebühren incentivieren Miner, bestimmte Transaktionen zu priorisieren.

**6. Dezentralisierung und Sicherheit:**

*   **Peer-to-Peer-Netzwerk:** Bitcoin operiert in einem dezentralen Peer-to-Peer-Netzwerk, was bedeutet, dass es keine zentrale Kontrollinstanz gibt. Transaktionen und Blöcke werden über viele Computer auf der ganzen Welt verbreitet.
*   **Zensurresistenz:** Da die Blockchain verteilt ist und eine erhebliche Rechenleistung zur Veränderung erfordert, ist es für eine einzelne Entität sehr schwierig, Transaktionen zu zensieren oder das Netzwerk zu kontrollieren.
*   **Sicherheit durch Kryptografie:** Der Einsatz starker Kryptografie gewährleistet die Sicherheit und Integrität von Transaktionen und der Blockchain. Private Schlüssel ermöglichen es Nutzern, ihre Bitcoin zu kontrollieren, und digitale Signaturen verhindern die Manipulation von Transaktionen. Der Proof-of-Work-Mechanismus macht es für böswillige Akteure rechnerisch sehr teuer, die Transaktionshistorie umzuschreiben.

**Zusammenfassend lässt sich sagen, dass der technische Betrieb von Bitcoin auf einem ausgeklügelten Zusammenspiel kryptografischer Techniken, eines verteilten und transparenten Hauptbuchs und eines rechenintensiven Konsensmechanismus beruht, um Sicherheit, Unveränderbarkeit und Dezentralisierung zu gewährleisten.**
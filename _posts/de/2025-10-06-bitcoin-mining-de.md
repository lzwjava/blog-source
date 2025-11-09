---
audio: false
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Bitcoin-Hash-Berechnung und Mining
translated: true
type: note
---

### Wie Bitcoin Hashes berechnet

Bitcoin verwendet eine kryptografische Hash-Funktion namens **SHA-256** (Secure Hash Algorithm 256-bit), um Hashes zu berechnen. Dies ist eine Einwegfunktion, die Eingabedaten (wie den Header eines Blocks) nimmt und eine feste 256-Bit (32-Byte) Ausgabe erzeugt, die einzigartig und unvorhersehbar ist.

-   **Was wird gehasht?** In erster Linie der Block-Header, der Folgendes enthält:
    -   Versionsnummer
    -   Hash des vorherigen Blocks
    -   Merkle-Root (eine Zusammenfassung aller Transaktionen im Block)
    -   Zeitstempel
    -   Schwierigkeitsziel (Bits)
    -   Nonce (eine Zahl, die Miner anpassen)

-   **Der Prozess:**
    1.  Der Miner stellt den Block-Header zusammen.
    2.  Wendet SHA-256 zweimal an: `hash = SHA256(SHA256(header))`.
    3.  Prüft, ob der resultierende Hash unter dem aktuellen Ziel liegt (z. B. mit genügend führenden Nullen beginnt, wie 000000...).
    4.  Wenn nicht, wird die Nonce erhöht und der Vorgang wiederholt. Dies ist der "Trial-and-Error"-Teil von Proof of Work (PoW).

Hashes sind deterministisch – die gleiche Eingabe ergibt immer die gleiche Ausgabe – aber winzige Änderungen (wie +1 zur Nonce) erzeugen völlig andere Ausgaben. Dies macht es unpraktikabel, Eingaben aus Ausgaben zurückzuberechnen.

### Warum Bitcoin minen? (Und wie es die Obergrenze von 21 Millionen sicherstellt)

Ich denke, Sie meinten "warum minen" anstelle von "warum prägen" – Mining ist der Prozess der Validierung von Transaktionen und des Hinzufügens von Blöcken zur Blockchain, der mit neuen Bitcoins belohnt wird.

-   **Warum minen?**
    -   **Sicherheit:** Miner sichern das Netzwerk, indem sie um die Lösung von PoW-Rätseln konkurrieren und so Angriffe wie Double-Spending (dasselbe BTC zweimal ausgeben) verhindern.
    -   **Dezentralisierung:** Jeder kann minen, was die Kontrolle verteilt – keine zentrale Autorität.
    -   **Anreiz:** Miner verdienen **Block Rewards** (neu geschaffene BTC) + Transaktionsgebühren. Dies bootstrappt das Netzwerk und kompensiert die Energiekosten.

-   **Sicherstellung der Angebotsobergrenze (es sind tatsächlich 21 Millionen, nicht 10 Millionen):**
    Das Protokoll von Bitcoin legt eine Gesamtmenge von **21 Millionen BTC** fest, die durch Mining-Belohnungen geschaffen wird, die sich alle 210.000 Blöcke (~4 Jahre) **halbiert**.
    -   Begann 2009 mit 50 BTC pro Block.
    -   Halbierte sich 2012 auf 25, 2016 auf 12,5, 2020 auf 6,25, 2024 auf 3,125 und so weiter.
    -   Der letzte Bitcoin wird um 2140 herum gemint; danach bleiben nur noch Gebühren.
    -   Dies wird durch Code erzwungen: Die Belohnungsformel lautet `reward = 50 * 0.5^(floor(block_height / 210000))`. Niemand kann dies ohne 95% Netzwerk-Konsens ändern, was die Inflation vorhersehbar und gedeckelt macht.

Diese Knappheit imitiert Gold und treibt den Wert.

### Wie Proof of Work (PoW) funktioniert

PoW ist der Konsensmechanismus von Bitcoin – ein Rechenrätsel, das beweist, dass ein Miner "Arbeit" (CPU/GPU/ASIC-Leistung) investiert hat, um einen Block hinzuzufügen.

-   **Schritt für Schritt:**
    1.  **Transaktionen sammeln:** Miner sammeln ausstehende Transaktionen in einem Block (bis zu ~1-4 MB, abhängig von SegWit).
    2.  **Header erstellen:** Schließen Sie den Merkle-Root der Transaktionen ein, verlinken Sie zum vorherigen Block usw.
    3.  **Ziel setzen:** Das Netzwerk passt die Schwierigkeit alle 2016 Blöcke an, um die durchschnittliche Blockzeit bei 10 Minuten zu halten. Ziel = eine sehr kleine Zahl (z. B. muss der Hash < 0x00000000FFFF... sein).
    4.  **Nonce finden:** Raten Sie Nonces per Brute-Force (0 bis 2^32-1). Hashen Sie für jede den Header. Wenn der Hash < Ziel ist, ist er gültig!
    5.  **Block verbreiten:** Andere Nodes verifizieren (einfach – nur einmal neu hashen). Wenn gültig, wird er zur Chain hinzugefügt; Miner beginnen mit dem nächsten Block.
    6.  **Chain-Regel:** Die längste gültige Kette gewinnt (löst Forks auf).

PoW macht es billig, Blöcke zu verifizieren, aber teuer, sie zu erstellen, und schützt so vor 51%-Angriffen (Kontrolle von >50% der Hash-Rate, um die Historie umzuschreiben).

### Warum so viele Berechnungen für eine Transaktion?

Transaktionen erfordern nicht direkt massive Berechnungen von Benutzern – nur das Signieren mit Ihrem privaten Schlüssel (elliptische Kurven-Kryptographie, schnell). Die schwere Arbeit steckt im **Mining**:

-   **Pro Block, nicht pro Transaktion:** Ein Block bündelt ~2.000-3.000 Transaktionen. Miner hashen Billionen Mal pro Block, um PoW zu lösen.
-   **Schwierigkeitsanpassung:** Wenn mehr Miner beitreten (höhere Gesamt-Hash-Rate), steigt die Schwierigkeit exponentiell, um 10-Minuten-Blöcke beizubehalten. Die aktuelle globale Hash-Rate beträgt ~600 EH/s (Exahashes pro Sekunde) – das sind 600 Trillionen Hashes pro Sekunde!
-   **Warum die Verschwendung?**
    -   **Sicherheitskosten:** Hohe Rechenleistung macht Angriffe unwirtschaftlich. Das Umschreiben eines Blocks kostet die Wiederholung aller nachfolgenden PoW.
    -   **Sybil-Resistenz:** Verhindert das Überfluten des Netzwerks mit gefälschten Identitäten.
    -   **Kompromiss:** Energieintensiv (Bitcoin verbraucht ~150 TWh/Jahr, wie ein mittelgroßes Land), aber Befürworter argumentieren, dass es ein Feature für vertrauensloses Geld ist.

Benutzer zahlen Gebühren, um Transaktionen in Blöcken zu priorisieren; Transaktionen mit niedrigen Gebühren warten.

Wenn Sie etwas Bestimmtes meinten (wie Hardware für das Mining), lassen Sie es mich wissen!

**Referenzen:**  
[Bitcoin Whitepaper](https://bitcoin.org/bitcoin.pdf)  
[Bitcoin Wiki: Proof of Work](https://en.bitcoin.it/wiki/Proof_of_work)  
[Blockchain.com: Bitcoin Halving](https://www.blockchain.com/learning-crypto/bitcoin-halving)
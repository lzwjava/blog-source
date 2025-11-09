---
audio: false
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Bitcoin-Automat zu Binance Überweisungsanleitung
translated: true
type: note
---

### Verständnis Ihrer Anfrage
Es scheint, als würden Sie sich nach der Nutzung von CoinUnit.io (einem Bitcoin ATM-Service) erkundigen, um BTC "aufzuladen" oder einzuzahlen, das entsprechende Netzwerk auszuwählen und dann diesen BTC an Ihr Binance-Konto zu senden (abzuheben) – insbesondere, ob Sie das standardmäßige "Bitcoin"-Netzwerk oder "BTC SegWit" auf Binance wählen sollen. Ich werde dies Schritt für Schritt aufschlüsseln, basierend auf der Funktionsweise dieser Dienste, um Ihnen zu helfen, Risiken wie den Verlust von Geldern zu vermeiden.

### Schritt 1: "Aufladen" von BTC auf CoinUnit.io
- CoinUnit.io betreibt Bitcoin-Automaten, an denen Sie **BTC durch Einzahlung von Bargeld kaufen** können (das ist wahrscheinlich die Bedeutung von "aufladen" in diesem Kontext – Ihr Wallet mit BTC aufzufüllen).
- Der Prozess an ihren Automaten ist unkompliziert (Standorte hauptsächlich in Hongkong, mit einigen internationalen Spots):
  1. Suchen Sie einen Automaten über ihre Website oder App.
  2. Wählen Sie "Bitcoin kaufen".
  3. Scannen Sie Ihren Bitcoin-Wallet-QR-Code (verwenden Sie ein Mobile Wallet wie Electrum, Trust Wallet oder die eigene Wallet-App von Binance).
  4. Werfen Sie Bargeld ein (unterstützt verschiedene Stückelungen; Gebühren liegen typischerweise bei 5-10 %, prüfen Sie dies vor Ort).
  5. Der Automat sendet die BTC direkt an **Ihre Bitcoin-Adresse in Ihrem Wallet**.
- **Wichtig**: CoinUnit.io-Automaten senden BTC ausschließlich über die **native Bitcoin-Blockchain**. Es gibt hier keine "Netzwerkauswahl" wie auf Börsen – es ist immer das standardmäßige BTC-Netzwerk. Ihr Wallet empfängt es als eine standardmäßige Bitcoin-Transaktion (kompatibel mit allen Adresstypen: Legacy beginnend mit "1", P2SH-SegWit mit "3" oder Native SegWit mit "bc1").
- Es gibt keine Anleitungen auf ihrer Website zum Senden an Binance, aber sobald Sie die BTC in Ihrem Wallet haben, können Sie sie transferieren.

Falls Sie mit dem Verkauf von BTC gegen Bargeld an ihren Automaten gemeint haben, ist das der umgekehrte Vorgang ("Bitcoin verkaufen" Option), aber Ihre Anfrage scheint sich auf den Erwerb und das Senden an Binance zu konzentrieren.

### Schritt 2: Senden von BTC von Ihrem Wallet zu Binance
- Nach dem Kauf bei CoinUnit.io haben Sie BTC in Ihrem persönlichen Wallet. Um sie zu Binance zu transferieren:
  1. Loggen Sie sich bei Binance ein > Wallet > Einzahlung > Wählen Sie "BTC" (Bitcoin).
  2. Binance generiert eine Einzahlungsadresse und fordert Sie auf, **ein Netzwerk auszuwählen**. Hier kommt Ihre Frage ins Spiel.
- **Wichtige Warnung**: Das Netzwerk, das Sie auf Binance auswählen, **muss mit** dem Netzwerk übereinstimmen, das Ihr Wallet zum Senden der BTC verwendet. Nichtübereinstimmungen können zu dauerhaftem Verlust der Gelder führen (Binance kann sie nicht wiederherstellen). Da CoinUnit.io das native Bitcoin-Netzwerk verwendet, bleiben Sie bei den Bitcoin-basierten Optionen auf Binance.

### Schritt 3: "Bitcoin" oder "BTC SegWit" auf Binance wählen?
- Binance unterstützt mehrere Netzwerke für BTC-Einzahlungen, aber nur **Bitcoin-native** sind sicher für Transfers von einem Standard-Wallet, wie Sie es an einem CoinUnit.io-Automaten verwenden würden. Hier ein kurzer Vergleich:

| Netzwerk-Option auf Binance | Beschreibung | Adresse beginnt mit | Empfohlen? | Warum? |
|---------------------------|-------------|---------------------|--------------|------|
| **Bitcoin (BTC)** | Standard Bitcoin-Netzwerk (oft Legacy oder P2SH). | "1" oder "3" | ✅ **Ja, sicherste Standardwahl** | Entspricht genau dem, was CoinUnit.io sendet. Geringstes Fehlerrisiko; weitgehende Kompatibilität. Gebühren sind Standard-Bitcoin-Gebühren. |
| **BTC (SegWit)** | Native SegWit (bech32) im Bitcoin-Netzwerk. | "bc1" | ✅ Ja, falls Ihr Wallet es unterstützt | Befindet sich ebenfalls auf der Bitcoin-Blockchain – voll kompatibel. Etwas niedrigere Gebühren und schnellere Bestätigungen aufgrund der SegWit-Effizienz. Verwenden Sie dies, wenn Ihr Wallet "bc1"-Adressen generiert (z.B. moderne Wallets wie Electrum). |
| **BEP20 (BSC)** | Binance Smart Chain (wrapped BTC). | Verschiedene (BEP20) | ❌ Nein | Falsche Blockchain – Ihre BTC wären verloren. |
| **BEP2** | Binance Chain (wrapped BTC). | "bnb" | ❌ Nein | Falsche Blockchain – Gelder verloren. |
| **ERC20** | Ethereum-Netzwerk (wrapped BTC wie WBTC). | "0x" | ❌ Nein | Falsche Blockchain – Gelder verloren. |

- **Empfehlung**: Wählen Sie **Bitcoin (BTC)**, es sei denn, Ihr Wallet verwendet speziell Native SegWit-Adressen (prüfen Sie dies, indem Sie eine Empfangsadresse in Ihrer Wallet-App generieren). Beide sind für diese Überweisung sicher, aber "Bitcoin" ist die unkomplizierteste und nachsichtigste Option für Anfänger.
  - Einzahlungen in diesen Netzwerken bestätigen sich in 1-3 Blöcken (typischerweise 10-30 Minuten), abhängig von der Netzwerkauslastung.
  - Mindesteinzahlung: Normalerweise 0,0005 BTC (prüfen Sie die aktuellen Limits auf Binance).
- Profi-Tipp: Führen Sie immer zuerst eine kleine Testtransaktion durch (z.B. 0,001 BTC), um zu bestätigen, dass alles funktioniert, bevor Sie den vollen Betrag senden.

### Zusätzliche Tipps
- **Gebühren**: CoinUnit.io berechnet ~5-8 % für Käufe (variiert je nach Standort). Bitcoin-Netzwerkgebühren für die Überweisung zu Binance betragen ~1-5 USD (werden von Ihrem Wallet bezahlt). Einzahlungen bei Binance sind kostenlos.
- **Sicherheit**: Aktivieren Sie die 2FA auf Binance. Verwenden Sie ein seriöses Wallet für den ATM-Scan. Vermeiden Sie öffentliche WLANs.
- **Bei Problemen**: Wenden Sie sich an den CoinUnit.io-Support (E-Mail/Telefon über ihre FAQ) für Hilfe mit den Automaten, oder an den Binance-Support für Einzahlungsfragen.
- Weitere Details finden Sie im offiziellen Einzahlungsleitfaden von Binance.

Falls dies nicht dem entspricht, was Sie gemeint haben (z.B. wenn sich "aufladen" auf etwas anderes bezieht), geben Sie bitte mehr Details für eine bessere Hilfe an!
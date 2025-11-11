---
audio: false
generated: true
lang: de
layout: post
title: Anschluss von Lautsprechern an den PC
translated: true
type: note
---

Um Audio-Lautsprecher über den RCA-Ausgang (oder "RS out") Ihres Motherboards an Ihren Computer anzuschließen, befolgen Sie diese Schritte. Beachten Sie, dass das MSI MAG B760M Mortar WiFi Motherboard normalerweise keine direkten RCA-Ausgänge hat, da die meisten modernen Motherboards 3,5-mm-Audioanschlüsse oder HDMI für die Audioausgabe verwenden. Ich gehe jedoch davon aus, dass Sie sich auf den Audioausgang des Motherboards (wahrscheinlich einen 3,5-mm-Anschluss, der für hintere Lautsprecher oder Line-Out gekennzeichnet ist) oder einen RCA-Adapter/Konverter beziehen.

### Schritte zum Anschließen von Audio-Lautsprechern mit RCA-Eingang:

1.  **Identifizieren Sie den Audioausgang auf dem Motherboard**:
    - Überprüfen Sie die hintere I/O-Blende Ihres MSI MAG B760M Mortar WiFi Motherboards. Sie hat typischerweise mehrere 3,5-mm-Audioanschlüsse, einschließlich eines grünen (Line-Out) für Stereo-Lautsprecher oder eines orangefarbenen Ausgangs (Center/Subwoofer) für Surround-Sound-Setups.
    - Wenn Ihre Lautsprecher RCA-Eingänge (rote und weiße Stecker) haben, benötigen Sie wahrscheinlich einen Adapter oder Konverter.

2.  **Überprüfen Sie die Lautsprecheranforderungen**:
    - Bestätigen Sie, ob Ihre Lautsprecher **aktiv** (mit eingebautem Verstärker) oder **passiv** (erfordern einen externen Verstärker) sind.
      - **Aktive Lautsprecher**: Können direkt mit dem richtigen Kabel oder Adapter an den Audioausgang des Motherboards angeschlossen werden.
      - **Passive Lautsprecher**: Erfordern einen externen Verstärker oder Receiver mit RCA-Eingängen.

3.  **Besorgen Sie sich das richtige Kabel/den richtigen Adapter**:
    - Wenn Ihre Lautsprecher RCA-Eingänge haben, benötigen Sie ein **3,5-mm-auf-RCA-Kabel** oder einen Adapter:
      - **3,5-mm-Stecker auf RCA-Stecker Kabel**: Verbindet den grünen 3,5-mm-Line-Out-Anschluss des Motherboards (oder einen anderen dafür vorgesehenen Audioausgang) mit den RCA-Eingängen an Ihren Lautsprechern oder Ihrem Verstärker.
      - **3,5-mm-Buchse auf RCA-Stecker Adapter**: Wenn Sie bereits ein RCA-Kabel haben, können Sie einen 3,5-mm-Buchse-auf-RCA-Stecker-Adapter verwenden.
    - Beispielprodukt: Ein 3,5-mm-auf-RCA-Kabel (ähnlich dem von Ihnen gelisteten Cable Matters SATA-Kabel, aber für Audio). Diese sind weit verbreitet für 10-50 CNY auf JD.com erhältlich.

4.  **Schließen Sie die Lautsprecher an**:
    - **Für aktive Lautsprecher**:
      - Stecken Sie das 3,5-mm-Ende des Kabels in den grünen Line-Out-Anschluss auf der hinteren I/O-Blende des Motherboards.
      - Verbinden Sie die RCA-Enden (rot und weiß) mit den entsprechenden RCA-Eingängen an Ihren Lautsprechern.
      - Schalten Sie die Lautsprecher ein und stellen Sie sicher, dass ihre Lautstärke aufgedreht ist.
    - **Für passive Lautsprecher**:
      - Schließen Sie das 3,5-mm-Ende an den Line-Out-Anschluss des Motherboards an.
      - Stecken Sie die RCA-Enden in die RCA-Eingänge eines externen Verstärkers oder Receivers.
      - Verbinden Sie die passiven Lautsprecher mit den Lautsprecherklemmen des Verstärkers (normalerweise über Lautsprecherkabel, nicht RCA).
      - Schalten Sie den Verstärker ein und passen Sie seine Einstellungen an.

5.  **Konfigurieren Sie die Audioeinstellungen**:
    - Fahren Sie Ihren Computer hoch und stellen Sie sicher, dass die Lautsprecher eingeschaltet sind.
    - In Windows:
      - Klicken Sie mit der rechten Maustaste auf das Lautsprechersymbol im Systembereich und wählen Sie **Sounds** oder **Soundeinstellungen**.
      - Wählen Sie im Tab **Wiedergabe** das Ausgabegerät (z. B. "Lautsprecher" oder "Realtek Audio") aus und setzen Sie es als Standard.
      - Wenn Sie Surround Sound verwenden, gehen Sie zu **Eigenschaften > Erweitert** und konfigurieren Sie das Lautsprechersetup (z. B. Stereo oder 5.1 Surround).
    - Installieren Sie die neuesten **Realtek Audio-Treiber** für Ihr MSI-Motherboard von der offiziellen MSI-Website oder von JD.com, falls noch nicht geschehen, um eine optimale Audioleistung zu gewährleisten.

6.  **Testen Sie die Audioausgabe**:
    - Spielen Sie Audio ab (z. B. Musik oder ein Video), um die Tonausgabe zu überprüfen.
    - Passen Sie die Lautstärke an den Lautsprechern, dem Verstärker (falls verwendet) und in Windows an.
    - Wenn kein Ton zu hören ist, überprüfen Sie:
      - Ob die Kabelverbindungen sicher sind.
      - Ob das richtige Wiedergabegerät in Windows ausgewählt ist.
      - Ob der Audioausgang des Motherboards im BIOS aktiviert ist (selten deaktiviert, aber überprüfen Sie bei Bedarf die BIOS-Einstellungen von MSI unter **Erweitert > Integrierte Peripheriegeräte**).

### Hinweise:
-   **Motherboard-Audio**: Das MSI MAG B760M Mortar WiFi verwendet einen Realtek Audio-Chip, der hochwertige Audioausgabe über 3,5-mm-Anschlüsse unterstützt. RCA-Ausgänge sind nicht Standard, daher verwenden Sie wahrscheinlich einen Adapter oder beziehen sich auf den Line-Out-Anschluss.
-   **Alternative Ausgänge**:
    - Wenn Ihre Lautsprecher HDMI oder Optical (S/PDIF) unterstützen, hat Ihr Motherboard auch einen S/PDIF Optical-Ausgang oder HDMI (über die GPU für Video+Audio). Prüfen Sie, ob Ihre Lautsprecher oder Ihr Verstärker diese unterstützen, um möglicherweise eine bessere Audioqualität zu erzielen.
    - Die HDMI/DisplayPort-Ausgänge der RTX 4070 GPU können Audio an einen Monitor oder Receiver mit Lautsprechern übertragen, falls bevorzugt.
-   **Kosten**: Ein 3,5-mm-auf-RCA-Kabel oder Adapter ist preiswert (10-50 CNY auf JD.com). Stellen Sie sicher, dass es Audio unterstützt (nicht nur Daten, wie Ihr SATA-Kabel).
-   **Surround Sound**: Wenn Ihre Lautsprecher Teil eines 5.1- oder 7.1-Setups sind, verwenden Sie die zusätzlichen 3,5-mm-Anschlüsse (z. B. orange für Center/Subwoofer, schwarz für hinten) und konfigurieren Sie diese in Windows.

Wenn Sie das Lautsprechermodell angeben oder ob Sie einen Verstärker verwenden, kann ich spezifischere Anleitung geben. Wenn Sie einen anderen "RS out" meinten (z. B. einen bestimmten Anschluss oder ein Gerät), geben Sie bitte Details an, und ich werde die Anweisungen anpassen.
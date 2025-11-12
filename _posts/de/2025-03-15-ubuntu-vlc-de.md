---
audio: false
generated: true
lang: de
layout: post
title: Installieren Sie VLC Media Player auf Ubuntu
translated: true
type: note
---

Um VLC Media Player auf Ihrem Ubuntu-System zu installieren, können Sie entweder das Terminal (Befehlszeile) oder das Ubuntu Software Center (grafische Oberfläche) verwenden. Nachfolgend finden Sie detaillierte Anleitungen für beide Methoden.

---

### **Methode 1: VLC über das Terminal installieren**

Diese Methode ist schnell und effizient, besonders wenn Sie mit der Befehlszeile vertraut sind. Gehen Sie folgendermaßen vor:

1.  **Öffnen Sie das Terminal**
    *   Suchen Sie im Ubuntu-Anwendungsmenü nach "Terminal" oder drücken Sie `Strg + Alt + T`, um es zu öffnen.

2.  **Aktualisieren Sie die Paketliste**
    *   Bevor Sie Software installieren, ist es eine gute Praxis, sicherzustellen, dass Ihre Paketliste auf dem neuesten Stand ist. Führen Sie diesen Befehl aus:
        ```bash
        sudo apt update
        ```
    *   Geben Sie Ihr Passwort ein, wenn Sie dazu aufgefordert werden. Dieser Befehl aktualisiert die Liste der verfügbaren Softwarepakete.

3.  **Installieren Sie VLC**
    *   Sobald die Paketliste aktualisiert ist, installieren Sie VLC mit:
        ```bash
        sudo apt install vlc
        ```
    *   Sie müssen erneut Ihr Passwort eingeben. Das System kann Sie bitten, die Installation durch Eingabe von `y` und Drücken der Eingabetaste zu bestätigen. Dadurch wird VLC zusammen mit seinen notwendigen Abhängigkeiten heruntergeladen und installiert.

4.  **Überprüfen Sie die Installation**
    *   Überprüfen Sie nach der Installation, ob VLC installiert ist, indem Sie eingeben:
        ```bash
        vlc
        ```
    *   Dies sollte den VLC Media Player starten. Wenn er sich öffnet, war die Installation erfolgreich.
    *   Alternativ können Sie die Version von VLC überprüfen, indem Sie ausführen:
        ```bash
        vlc --version
        ```
    *   Dies zeigt etwas wie "VLC media player 3.0.11.1 Vetinari" an (die Versionsnummer kann variieren).

5.  **Optional: Testen Sie VLC**
    *   Um sicherzustellen, dass VLC ordnungsgemäß funktioniert, versuchen Sie, eine Mediendatei abzuspielen. Wenn Sie beispielsweise eine MP4-Datei auf Ihrem Desktop haben, klicken Sie mit der rechten Maustaste darauf und wählen Sie "Öffnen mit VLC Media Player". Wenn sie abgespielt wird, ist VLC voll funktionsfähig.

---

### **Methode 2: VLC über das Ubuntu Software Center installieren**

Wenn Sie eine grafische Oberfläche dem Terminal vorziehen, verwenden Sie das Ubuntu Software Center:

1.  **Öffnen Sie das Ubuntu Software Center**
    *   Suchen Sie im Anwendungsmenü nach "Ubuntu Software" und klicken Sie es zum Öffnen an.

2.  **Suchen Sie nach VLC**
    *   Klicken Sie im Software Center auf das Suchsymbol (normalerweise eine Lupe) und geben Sie "VLC" in die Suchleiste ein.

3.  **Installieren Sie VLC**
    *   Finden Sie "VLC media player" in den Suchergebnissen, klicken Sie darauf und dann auf die Schaltfläche "Installieren". Möglicherweise müssen Sie Ihr Passwort eingeben, um die Installation zu autorisieren.

4.  **Starten Sie VLC**
    *   Nach der Installation können Sie VLC direkt aus dem Software Center starten, indem Sie auf "Öffnen" klicken (falls verfügbar), oder indem Sie im Anwendungsmenü nach "VLC" suchen.

---

### **Zusätzliche Hinweise**

*   **VLC aktuell halten**
    *   Wenn Sie VLC über das Terminal installiert haben, können Sie es aktuell halten, indem Sie regelmäßig ausführen:
        ```bash
        sudo apt update
        sudo apt upgrade
        ```
    *   Dies aktualisiert VLC zusammen mit anderen Systempaketen. Wenn Sie das Software Center verwendet haben, werden Updates normalerweise über dieselbe Oberfläche verwaltet.

*   **Plugins und Codecs**
    *   Die Standard-VLC-Installation über `sudo apt install vlc` beinhaltet essentielle Plugins (wie `vlc-plugin-base`) und Codecs, sodass die meisten gängigen Medienformate (z.B. MP4, AVI) sofort abgespielt werden sollten. Wenn Sie Probleme mit bestimmten Dateitypen haben, können Sie später zusätzliche Codecs installieren, wie z.B. `ubuntu-restricted-extras`, mit:
        ```bash
        sudo apt install ubuntu-restricted-extras
        ```

*   **Alternative Installation via Snap**
    *   VLC ist auch als Snap-Paket verfügbar. Wenn Sie diese Methode bevorzugen, führen Sie aus:
        ```bash
        sudo snap install vlc
        ```
    *   Dennoch wird die `apt`-Methode für die meisten Benutzer empfohlen, da sie sich gut in das System integriert.

---

Indem Sie eine der beiden Methoden befolgen, haben Sie VLC installiert und einsatzbereit auf Ihrem Ubuntu-System. Die Terminal-Methode ist schneller für Befehlszeilen-Benutzer, während das Software Center ideal für diejenigen ist, die einen grafischen Ansatz bevorzugen. Viel Spaß beim Medienabspielen!

---

Um den Fehler zu beheben, den Sie beim Abspielen einer MKV-Datei in VLC unter Ubuntu erhalten – speziell die Meldung über fehlende MPEG-4 AAC und H.265 Decoder – befolgen Sie die nachfolgenden Schritte. Dieses Problem tritt typischerweise auf, weil Ubuntu bestimmte proprietäre Codecs standardmäßig aufgrund von Lizenzbeschränkungen nicht enthält. Die Installation zusätzlicher Codec-Pakete sollte das Problem beheben.

---

### **Lösung**

#### **Schritt 1: Installieren Sie das Paket `ubuntu-restricted-extras`**
Dieses Paket bietet Unterstützung für eine Vielzahl von Codecs, einschließlich MPEG-4 AAC (Audio) und H.265 (HEVC) Video, die wahrscheinlich in Ihrer VLC-Installation fehlen.

1.  **Öffnen Sie das Terminal**
    *   Suchen Sie im Ubuntu-Anwendungsmenü nach "Terminal" oder drücken Sie `Strg + Alt + T`.

2.  **Aktualisieren Sie die Paketliste**
    *   Führen Sie diesen Befehl aus, um sicherzustellen, dass die Paketliste Ihres Systems auf dem neuesten Stand ist:
        ```bash
        sudo apt update
        ```

3.  **Installieren Sie `ubuntu-restricted-extras`**
    *   Führen Sie den folgenden Befehl aus:
        ```bash
        sudo apt install ubuntu-restricted-extras
        ```
    *   Möglicherweise müssen Sie Ihr Passwort eingeben. Während der Installation werden Sie möglicherweise aufgefordert, die Endbenutzer-Lizenzvereinbarung (EULA) für bestimmte Komponenten zu akzeptieren – befolgen Sie die Anweisungen auf dem Bildschirm, um zuzustimmen und fortzufahren.

4.  **Starten Sie VLC neu**
    *   Schließen Sie VLC, falls es geöffnet ist, öffnen Sie es dann erneut und versuchen Sie, die MKV-Datei erneut abzuspielen.

---

#### **Schritt 2: Installieren Sie zusätzliche Codec-Pakete (falls nötig)**
Wenn der Fehler nach Schritt 1 weiterhin besteht, installieren Sie spezifische Pakete, die zusätzliche Unterstützung für H.265 und andere Codecs bieten.

1.  **Installieren Sie `libde265-0` und `libavcodec-extra`**
    *   Führen Sie diesen Befehl aus, um Bibliotheken für H.265-Decodierung und zusätzliche Codec-Unterstützung zu installieren:
        ```bash
        sudo apt install libde265-0 libavcodec-extra
        ```

2.  **Starten Sie VLC neu**
    *   Schließen und öffnen Sie VLC erneut und versuchen Sie dann, die MKV-Datei erneut abzuspielen.

---

#### **Schritt 3: Zusätzliche Fehlerbehebung (falls erforderlich)**
Wenn das Problem immer noch nicht behoben ist, versuchen Sie diese zusätzlichen Schritte:

*   **Überprüfen Sie die VLC-Version**
    *   Stellen Sie sicher, dass Sie die neueste VLC-Version verwenden. Überprüfen Sie Ihre aktuelle Version mit:
        ```bash
        vlc --version
        ```
    *   Wenn sie veraltet ist, aktualisieren Sie sie durch Ausführen von:
        ```bash
        sudo apt update
        sudo apt upgrade vlc
        ```

*   **Testen Sie eine andere MKV-Datei**
    *   Spielen Sie eine andere MKV-Datei ab, um zu sehen, ob das Problem dateispezifisch ist. Wenn andere Dateien funktionieren, könnte die problematische Datei beschädigt sein oder eine nicht unterstützte Kodierung verwenden.

*   **Sehen Sie sich die VLC-Protokolle für weitere Details an**
    *   Für eine erweiterte Fehlerbehebung führen Sie VLC mit ausführlicher Ausgabe aus dem Terminal aus:
        ```bash
        vlc --verbose 2
        ```
    *   Versuchen Sie, die Datei abzuspielen, und suchen Sie nach detaillierten Fehlermeldungen über die fehlenden Codecs.

---

### **Zusätzliche Hinweise**

*   **Warum das passiert**: MKV ist ein Containerformat, das verschiedene Codecs wie MPEG-4 AAC für Audio und H.265 für Video verwenden kann. Die Standard-VLC-Installation von Ubuntu könnte diese aufgrund rechtlicher Beschränkungen für proprietäre Software nicht enthalten.
*   **Hardware-Beschleunigung**: Wenn Ihr System H.265-Hardware-Decodierung unterstützt (z.B. über eine moderne GPU), stellen Sie sicher, dass Ihre Grafiktreiber aktualisiert sind. Dieser Fehler deutet jedoch auf einen fehlenden Software-Decoder hin, daher ist Hardware-Beschleunigung wahrscheinlich nicht das Hauptproblem.
*   **Nächste Schritte**: Wenn nichts davon funktioniert, ziehen Sie eine Neuinstallation von VLC in Betracht oder suchen Sie Hilfe in Ubuntu- oder VLC-Foren mit Details zu Ihrem System und der spezifischen MKV-Datei.

---

Indem Sie diese Schritte befolgen, sollten Sie in der Lage sein, die Fehler wegen fehlender Decoder zu beheben und Ihre MKV-Dateien in VLC erfolgreich abzuspielen. Beginnen Sie mit Schritt 1, da dies die einfachste und wahrscheinlichste Lösung ist.
---
audio: false
generated: true
lang: de
layout: post
title: Git Credential Manager Diagnose
translated: true
type: note
---

Die Ausgabe von `git credential-manager diagnose` zeigt nun eindeutig einen **Netzwerkfehler** an, zusätzlich zur TLS-Zertifikatsverifikationswarnung. Lassen Sie uns den Fehler und seine Behebung aufschlüsseln:

**Wichtige Erkenntnisse:**

*   **Netzwerkfehler:**
    *   Der Diagnosetest schlug mit folgendem Fehler fehl: `System.Net.Http.HttpRequestException: nodename nor servname provided, or not known (example.com:443)`.
    *   Dieser Fehler bedeutet, dass der Git Credential Manager den Hostnamen `example.com` nicht in eine IP-Adresse auflösen konnte oder keine Verbindung zu Port 443 auf diesem Host herstellen konnte.
    *   Das Diagnoseprotokoll zeigt, dass die HEAD-Anfrage an `https://example.com` fehlgeschlagen ist.
*   **Proxy-Interferenz (wahrscheinliche Ursache):**
    *   Das Vorhandensein von `HTTP_PROXY: http://127.0.0.1:7890` und `HTTPS_PROXY: http://127.0.0.1:7890` deutet stark darauf hin, dass der Proxy die Grundursache des Netzwerkfehlers ist.
    *   Die Tatsache, dass die Diagnose [http://httpforever.com](http://httpforever.com) erreichen kann, aber nicht [https://example.com](https://example.com), deutet darauf hin, dass der Proxy Probleme mit HTTPS-Anfragen hat.
*   **TLS-Zertifikatsverifikation deaktiviert (Sicherheitsrisiko):**
    *   Wie zuvor ist die TLS-Zertifikatsverifikation deaktiviert, was ein großes Sicherheitsrisiko darstellt.

**Schritte zur Fehlerbehebung:**

1.  **Proxy-Überprüfung:**
    *   **Proxy testen:** Öffnen Sie einen Webbrowser und versuchen Sie, direkt auf `https://example.com` zuzugreifen. Wenn Sie einen "Verbindungsfehler" oder "Hostname nicht gefunden" Fehler erhalten, ist Ihr Proxy wahrscheinlich fehlkonfiguriert.
    *   **Proxy-Software-Probleme:**
        *   Starten Sie Ihre Proxy-Software (Shadowsocks, Clash, etc.) neu.
        *   Überprüfen Sie die Protokolle der Proxy-Software auf Fehlermeldungen.
        *   Stellen Sie sicher, dass der Proxy für die korrekte Verarbeitung von HTTPS-Datenverkehr konfiguriert ist.
        *   Stellen Sie sicher, dass die Proxy-Software läuft.
    *   **Proxy-Konfiguration:**
        *   Überprüfen Sie Ihre Proxy-Einstellungen in den Netzwerkeinstellungen Ihres Betriebssystems und in allen Git-Konfigurationsdateien.
        *   Verifizieren Sie, dass die Proxy-Adresse (`127.0.0.1`) und der Port (`7890`) korrekt sind.
        *   Deaktivieren Sie den Proxy vorübergehend in den Netzwerkeinstellungen Ihres Betriebssystems und führen Sie den `git credential-manager diagnose` Befehl erneut aus.
2.  **DNS-Auflösung:**
    *   Obwohl die Fehlermeldung auf ein Hostnamen-Auflösungsproblem hindeutet, ist der Proxy der wahrscheinlichste Schuldige. Es ist dennoch ratsam, Ihre DNS-Einstellungen zu überprüfen.
    *   Versuchen Sie, einen öffentlichen DNS-Server zu verwenden (z.B. 8.8.8.8, 1.1.1.1).
3.  **TLS-Zertifikatsverifikation:**
    *   **Zertifikatsverifikation wieder aktivieren:** Dies ist entscheidend für die Sicherheit. Befolgen Sie die Anweisungen im Link `https://aka.ms/gcm/tlsverify`.
    *   Wenn Ihre Proxy-Software dafür ausgelegt ist, HTTPS-Datenverkehr abzufangen, stellen Sie sicher, dass Sie das Stammzertifikat des Proxys in den vertrauenswürdigen Stammzertifikatspeicher Ihres Betriebssystems installieren. Dies ist der sichere Weg, um die Funktion des Proxys zu ermöglichen.
4.  **Git-Konfiguration:**
    *   Führen Sie `git config --global --list` aus, um Ihre Git-Konfiguration zu überprüfen.
    *   Entfernen Sie vorübergehend die Proxy-Einstellungen aus Git, um das Problem zu isolieren:
        ```bash
        git config --global --unset http.proxy
        git config --global --unset https.proxy
        ```
    *   Nach dem Entfernen der Proxy-Einstellungen führen Sie den Befehl `git credential-manager diagnose` erneut aus.
5.  **Firewall:**
    *   Deaktivieren Sie vorübergehend alle Firewalls auf Ihrem Computer, um eine Firewall-Interferenz auszuschließen.
6.  **Netzwerkverbindung:**
    *   Testen Sie Ihre Netzwerkverbindung mit anderen Netzwerkanwendungen, um sicherzustellen, dass das Netzwerk selbst stabil ist.
    *   Wenn Sie einen mobilen Hotspot verwenden, wechseln Sie an einen Ort mit besserer Signalstärke.

**Wichtigste Erkenntnis:** Der Proxy verursacht mit hoher Sicherheit die Netzwerkfehler. Die korrekte Konfiguration des Proxys und die erneute Aktivierung der TLS-Zertifikatsverifikation sind die wichtigsten Schritte.
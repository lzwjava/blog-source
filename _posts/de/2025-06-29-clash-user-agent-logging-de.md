---
audio: false
generated: true
lang: de
layout: post
title: Benutzer-Agent in Clash Proxy protokollieren
translated: true
type: note
---

Es scheint, dass Sie sich auf **Clash** beziehen, ein regelbasiertes Proxy-Utility, und es so konfigurieren möchten, dass es den **User-Agent** seiner HTTP-Anfragen ausgibt oder protokolliert. Nach den verfügbaren Informationen verfügt Clash (oder sein Kern, oft als `clash-core` bezeichnet) nicht über eine eingebaute Funktion, um den User-Agent ausgehender Anfragen auf einfache Weise direkt auszugeben. Sie können dies jedoch erreichen, indem Sie die Konfigurationsoptionen von Clash, externe Tools oder Debugging-Methoden nutzen. Im Folgenden finden Sie eine Schritt-für-Schritt-Anleitung, die Ihnen hilft, den User-Agent von Anfragen, die über Clash gestellt werden, zu protokollieren oder zu inspizieren.

---

### Kontext verstehen
- **Clash** ist ein Proxy-Utility, das Datenverkehr basierend auf Regeln routet und Protokolle wie HTTP, SOCKS5, Shadowsocks, V2Ray und mehr unterstützt. Es operiert auf der Netzwerk- und Anwendungsschicht.
- Der **User-Agent** ist ein HTTP-Header, der typischerweise von der Client-Anwendung (z.B. einem Browser oder einem Tool wie `curl`) gesetzt wird, die die Anfrage stellt, und nicht von Clash selbst. Clash leitet diese Anfragen als Proxy weiter und protokolliert oder modifiziert den User-Agent standardmäßig nicht, es sei denn, es ist explizit dafür konfiguriert.
- Um den User-Agent auszugeben, müssen Sie entweder:
  1. Clash so konfigurieren, dass es HTTP-Header (einschließlich User-Agent) für Debugging-Zwecke protokolliert.
  2. Ein externes Tool (z.B. einen Proxy-Debugger oder Network Sniffer) verwenden, um die Anfragen zu inspizieren.
  3. Die Clash-Konfiguration modifizieren, um benutzerdefinierte Header hinzuzufügen oder ein Skript zu verwenden, um sie zu protokollieren.

Da Clash selbst keine direkte Konfiguration zum Protokollieren von User-Agent-Headern hat, müssen Sie Clash möglicherweise mit anderen Tools kombinieren oder spezifische Konfigurationen verwenden. Im Folgenden sind die Methoden beschrieben, um dies zu erreichen.

---

### Methode 1: Detaillierte Protokollierung in Clash aktivieren und Logs inspizieren
Clash kann Anfragen auf verschiedenen Ebenen protokollieren, protokolliert aber von Haus aus keine HTTP-Header wie den User-Agent, es sei denn, es ist explizit konfiguriert oder wird mit einem Tool verwendet, das den Datenverkehr inspizieren kann. Sie können eine detaillierte Protokollierung aktivieren und ein Tool verwenden, um den User-Agent zu erfassen.

#### Schritte:
1. **Clash Log-Level auf Debug setzen**:
   - Bearbeiten Sie Ihre Clash-Konfigurationsdatei (`config.yaml`, typischerweise located unter `~/.config/clash/config.yaml` oder einem benutzerdefinierten Verzeichnis, das mit dem `-d`-Flag angegeben wird).
   - Setzen Sie `log-level` auf `debug`, um detaillierte Informationen über Anfragen zu erfassen:
     ```yaml
     log-level: debug
     ```
   - Speichern Sie die Konfiguration und starten Sie Clash neu:
     ```bash
     clash -d ~/.config/clash
     ```
   - Clash protokolliert nun detailliertere Informationen nach `STDOUT` oder in eine spezifizierte Log-Datei. Dies könnte jedoch den User-Agent-Header nicht direkt enthalten, da Clash sich auf Routing- und Verbindungsdetails konzentriert.

2. **Logs inspizieren**:
   - Überprüfen Sie die Log-Ausgabe im Terminal oder in der Log-Datei (falls konfiguriert). Suchen Sie nach HTTP-Anfragedetails, aber beachten Sie, dass die Standardprotokollierung von Clash möglicherweise keine vollständigen HTTP-Header wie User-Agent enthält.
   - Wenn Sie keine User-Agent-Informationen sehen, fahren Sie mit der Verwendung eines Debugging-Proxys (siehe Methode 2) oder Network Sniffers (Methode 3) fort.

3. **Optional: Clash Dashboard verwenden**:
   - Clash bietet ein webbasiertes Dashboard (z.B. YACD unter `https://yacd.haishan.me/` oder das offizielle Dashboard unter `https://clash.razord.top/`), um Verbindungen und Logs zu überwachen.
   - Konfigurieren Sie `external-controller` und `external-ui` in Ihrer `config.yaml`, um das Dashboard zu aktivieren:
     ```yaml
     external-controller: 127.0.0.1:9090
     external-ui: folder
     ```
   - Greifen Sie auf das Dashboard über `http://127.0.0.1:9090/ui` zu und überprüfen Sie den Tab "Logs" oder "Connections". Dies zeigt möglicherweise Verbindungsdetails an, aber wahrscheinlich nicht direkt den User-Agent.

#### Einschränkungen:
- Die Debug-Logs von Clash konzentrieren sich auf Routing- und Proxy-Entscheidungen, nicht auf vollständige HTTP-Header. Um den User-Agent zu erfassen, müssen Sie den HTTP-Datenverkehr abfangen, was zusätzliche Tools erfordert.

---

### Methode 2: Einen Debugging-Proxy verwenden, um den User-Agent zu erfassen
Da Clash selbst keine HTTP-Header wie User-Agent direkt protokolliert, können Sie den Datenverkehr von Clash durch einen Debugging-Proxy wie **mitmproxy**, **Charles Proxy** oder **Fiddler** routen. Diese Tools können die vollständige HTTP-Anfrage abfangen und anzeigen, einschließlich des User-Agent.

#### Schritte:
1. **mitmproxy installieren**:
   - Installieren Sie `mitmproxy`, ein beliebtes Open-Source-Tool zum Abfangen von HTTP/HTTPS-Datenverkehr:
     ```bash
     sudo apt install mitmproxy  # Auf Debian/Ubuntu
     brew install mitmproxy      # Auf macOS
     ```
   - Alternativ können Sie ein anderes Proxy-Tool wie Charles oder Fiddler verwenden.

2. **Clash konfigurieren, um Datenverkehr durch mitmproxy zu routen**:
   - Standardmäßig agiert Clash als HTTP/SOCKS5-Proxy. Sie können es an `mitmproxy` kaskadieren, indem Sie `mitmproxy` als Upstream-Proxy setzen.
   - Bearbeiten Sie Ihre Clash `config.yaml`, um einen HTTP-Proxy einzufügen, der auf `mitmproxy` zeigt:
     ```yaml
     proxies:
       - name: mitmproxy
         type: http
         server: 127.0.0.1
         port: 8080  # Standard mitmproxy Port
     proxy-groups:
       - name: Proxy
         type: select
         proxies:
           - mitmproxy
     ```
   - Speichern Sie die Konfiguration und starten Sie Clash neu.

3. **mitmproxy starten**:
   - Führen Sie `mitmproxy` aus, um auf Port 8080 zu lauschen:
     ```bash
     mitmproxy
     ```
   - `mitmproxy` zeigt alle HTTP-Anfragen an, die durch es hindurchgehen, einschließlich des User-Agent-Headers.

4. **Eine Test-Anfrage senden**:
   - Verwenden Sie einen Client (z.B. `curl`, einen Browser oder ein anderes Tool), der so konfiguriert ist, dass er Clash als Proxy verwendet.
   - Beispiel mit `curl`:
     ```bash
     curl --proxy http://127.0.0.1:7890 http://example.com
     ```
   - In `mitmproxy` sehen Sie die vollständige HTTP-Anfrage, einschließlich des User-Agent (z.B. `curl/8.0.1` oder der User-Agent des Browsers).

5. **User-Agent inspizieren**:
   - Navigieren Sie in der `mitmproxy`-Oberfläche durch die erfassten Anfragen. Der User-Agent-Header wird in den Anfragedetails sichtbar sein.
   - Sie können die Logs auch in einer Datei speichern für weitere Analysen:
     ```bash
     mitmproxy -w mitmproxy.log
     ```

#### Hinweise:
- Wenn Sie HTTPS verwenden, müssen Sie das `mitmproxy` CA-Zertifikat auf Ihrem Client-Gerät installieren und vertrauen, um HTTPS-Datenverkehr zu entschlüsseln. Folgen Sie den Anweisungen unter `http://mitm.clash/cert.crt` oder der Dokumentation von `mitmproxy`.
- Diese Methode erfordert das Kaskadieren von Proxies (Client → Clash → mitmproxy → Ziel), was die Latenz leicht erhöhen kann, aber die vollständige Inspektion von Headern ermöglicht.

---

### Methode 3: Einen Network Sniffer verwenden, um den User-Agent zu erfassen
Wenn Sie Proxies nicht kaskadieren möchten, können Sie einen Network Sniffer wie **Wireshark** verwenden, um den HTTP-Datenverkehr, der durch Clash geht, zu erfassen und zu inspizieren.

#### Schritte:
1. **Wireshark installieren**:
   - Laden Sie Wireshark von [wireshark.org](https://www.wireshark.org/) herunter und installieren Sie es.
   - Auf Linux:
     ```bash
     sudo apt install wireshark
     ```
   - Auf macOS:
     ```bash
     brew install wireshark
     ```

2. **Clash starten**:
   - Stellen Sie sicher, dass Clash mit Ihrer gewünschten Konfiguration läuft (z.B. HTTP-Proxy auf Port 7890):
     ```bash
     clash -d ~/.config/clash
     ```

3. **Datenverkehr in Wireshark erfassen**:
   - Öffnen Sie Wireshark und wählen Sie die Netzwerkschnittstelle aus, die Clash verwendet (z.B. `eth0`, `wlan0` oder `lo` für Localhost-Datenverkehr).
   - Wenden Sie einen Filter an, um HTTP-Datenverkehr zu erfassen:
     ```
     http
     ```
   - Alternativ können Sie nach dem Clash HTTP-Proxy-Port filtern (z.B. 7890):
     ```
     tcp.port == 7890
     ```

4. **Eine Test-Anfrage senden**:
   - Verwenden Sie einen Client, der so konfiguriert ist, dass er Clash als Proxy verwendet:
     ```bash
     curl --proxy http://127.0.0.1:7890 http://example.com
     ```

5. **User-Agent inspizieren**:
   - Suchen Sie in Wireshark nach HTTP-Anfragen (z.B. `GET / HTTP/1.1`). Doppelklicken Sie auf ein Paket, um dessen Details anzuzeigen.
   - Erweitern Sie den Abschnitt "Hypertext Transfer Protocol", um den `User-Agent`-Header zu finden (z.B. `User-Agent: curl/8.0.1`).

#### Hinweise:
- Für HTTPS-Datenverkehr kann Wireshark den User-Agent nicht entschlüsseln, es sei denn, Sie haben den privaten Schlüssel des Servers oder verwenden ein Tool wie `mitmproxy`, um den Datenverkehr zu entschlüsseln.
- Diese Methode ist komplexer und erfordert Vertrautheit mit der Analyse von Netzwerkpaketen.

---

### Methode 4: Clash-Konfiguration modifizieren, um benutzerdefinierte Header zu injizieren oder zu protokollieren
Clash unterstützt benutzerdefinierte HTTP-Header in seiner Konfiguration für bestimmte Proxy-Typen (z.B. HTTP oder VMess). Sie können Clash konfigurieren, um einen spezifischen User-Agent zu injizieren oder ein Skript zu verwenden, um Header zu protokollieren. Dies ist jedoch weniger direkt für das Protokollieren des User-Agent aller Anfragen.

#### Schritte:
1. **Benutzerdefinierten User-Agent-Header hinzufügen**:
   - Wenn Sie einen spezifischen User-Agent für Tests erzwingen möchten, modifizieren Sie den `proxies`-Abschnitt in `config.yaml`, um einen benutzerdefinierten Header einzufügen:
     ```yaml
     proxies:
       - name: my-http-proxy
         type: http
         server: proxy.example.com
         port: 8080
         header:
           User-Agent:
             - "MyCustomUserAgent/1.0"
     ```
   - Dies setzt einen benutzerdefinierten User-Agent für Anfragen, die durch diesen Proxy gesendet werden. Allerdings überschreibt er den ursprünglichen User-Agent des Clients, was möglicherweise nicht das ist, was Sie wollen, wenn Sie den User-Agent des Clients protokollieren möchten.

2. **Skript-Regeln verwenden, um Header zu protokollieren**:
   - Clash unterstützt skriptbasierte Regeln mit Engines wie `expr` oder `starlark` (). Sie können ein Skript schreiben, um Header, einschließlich User-Agent, zu protokollieren oder zu verarbeiten.[](https://pkg.go.dev/github.com/yaling888/clash)
   - Beispielkonfiguration:
     ```yaml
     script:
       engine: starlark
       code: |
         def match(req):
           print("User-Agent:", req.headers["User-Agent"])
           return "Proxy"  # Leite zu einer Proxy-Gruppe
     ```
   - Dies erfordert das Schreiben eines benutzerdefinierten Skripts, was fortgeschritten ist und möglicherweise nicht in allen Clash-Versionen vollständig unterstützt wird. Überprüfen Sie die Clash-Dokumentation auf Skript-Unterstützung.

3. **Mit mitmproxy oder Wireshark verifizieren**:
   - Nach dem Injizieren eines benutzerdefinierten User-Agent verwenden Sie Methode 2 oder Methode 3, um zu bestätigen, dass der User-Agent wie erwartet gesendet wird.

#### Einschränkungen:
- Das Injizieren eines benutzerdefinierten User-Agent überschreibt den User-Agent des Clients, daher ist dies nur nützlich zum Testen spezifischer User-Agents.
- Skriptbasierte Protokollierung ist experimentell und möglicherweise nicht in allen Clash-Versionen verfügbar.

---

### Methode 5: Clash’s MITM-Proxy verwenden, um Header zu protokollieren
Clash unterstützt einen **Man-in-the-Middle (MITM)**-Proxy-Modus, der HTTPS-Datenverkehr abfangen und protokollieren kann, einschließlich Headern wie User-Agent.

#### Schritte:
1. **MITM in Clash aktivieren**:
   - Bearbeiten Sie `config.yaml`, um den MITM-Proxy zu aktivieren:
     ```yaml
     mitm-port: 7894
     mitm:
       hosts:
         - "*.example.com"
     ```
   - Dies konfiguriert Clash so, dass es HTTPS-Datenverkehr für spezifizierte Domains abfängt.

2. **Clash’s CA-Zertifikat installieren**:
   - Clash generiert ein CA-Zertifikat für MITM. Rufen Sie `http://mitm.clash/cert.crt` in einem Browser auf, um es herunterzuladen und zu installieren.
   - Vertrauen Sie dem Zertifikat auf Ihrem Client-Gerät, damit Clash HTTPS-Datenverkehr entschlüsseln kann.

3. **Logs inspizieren**:
   - Wenn MITM aktiviert ist, protokolliert Clash möglicherweise detailliertere Anfrageinformationen, einschließlich Header. Überprüfen Sie die Logs im Terminal oder Dashboard.
   - Wenn Header nicht protokolliert werden, verwenden Sie `mitmproxy` (Methode 2), um den entschlüsselten Datenverkehr zu erfassen.

#### Hinweise:
- Der MITM-Modus erfordert, dass das CA-Zertifikat auf allen Client-Geräten vertraut wird, was für alle Anwendungsfälle möglicherweise nicht praktikabel ist.
- Diese Methode ist am besten für HTTPS-Datenverkehr geeignet, erfordert aber zusätzlichen Setup.

---

### Empfehlungen
- **Bevorzugte Methode**: Verwenden Sie **Methode 2 (mitmproxy)** für den einfachsten und zuverlässigsten Weg, den User-Agent von Anfragen zu erfassen und zu protokollieren. Es ist Open-Source, weit unterstützt und für HTTP-Debugging designed.
- **Alternative**: Verwenden Sie **Methode 3 (Wireshark)**, wenn Sie mit der Analyse von Netzwerkpaketen vertraut sind und keine Proxies kaskadieren möchten.
- **Für Fortgeschrittene**: Experimentieren Sie mit **Methode 4 (Benutzerdefinierte Header oder Skripte)**, wenn Sie Header programmatisch innerhalb von Clash manipulieren oder protokollieren müssen.

---

### Zusätzliche Hinweise
- **Clash-Dokumentation**: Konsultieren Sie die offizielle Clash-Dokumentation (,) für Konfigurationsdetails. Das GitHub-Repository (`https://github.com/Dreamacro/clash`) und das Wiki (`https://en.clash.wiki`) bieten detaillierte Anleitungen.[](https://en.clash.wiki/)[](https://en.clash.wiki/configuration/getting-started.html)
- **Client-seitiger User-Agent**: Der User-Agent wird vom Client (z.B. Browser, `curl` oder Anwendung) gesetzt, nicht von Clash. Stellen Sie sicher, dass Ihr Client den erwarteten User-Agent sendet. Zum Beispiel:
  - `curl` verwendet standardmäßig `curl/<version>`.
  - Browser verwenden ihre eigenen User-Agent-Strings (z.B. `Mozilla/5.0 ...`).
- **Testen**: Testen Sie immer mit einer einfachen HTTP-Anfrage (z.B. `curl --proxy http://127.0.0.1:7890 http://example.com`), um den Setup zu verifizieren.
- **Sicherheit**: Wenn Sie MITM oder Debugging-Proxies verwenden, stellen Sie sicher, dass Sie den CA-Zertifikaten und Tools vertrauen, um Sicherheitsrisiken zu vermeiden.

Wenn Sie weitere Klärung oder Hilfe mit spezifischen Konfigurationen benötigen, geben Sie bitte mehr Details zu Ihrem Setup an (z.B. Clash-Version, Betriebssystem oder spezifischer Proxy-Typ), und ich kann die Anweisungen weiter anpassen!
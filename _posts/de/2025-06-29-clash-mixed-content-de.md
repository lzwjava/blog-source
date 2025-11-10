---
audio: false
generated: true
lang: de
layout: post
title: Behebung von Mixed-Content-Fehlern bei Clash VPN
translated: true
type: note
---

Die Fehlermeldungen, die Sie erhalten, deuten auf ein **Mixed Content**-Problem mit der Clash VPN-Anwendung hin. Dies tritt speziell auf, wenn die Seite unter `https://clash.razord.top/` versucht, Ressourcen von einem unsicheren `http://127.0.0.1:9090/`-Endpunkt (z.B. `http://127.0.0.1:9090/version`) zu laden. Moderne Browser blockieren solche Anfragen, da sie gegen Sicherheitsrichtlinien verstoßen, indem sie versuchen, unsichere HTTP-Inhalte auf einer sicheren HTTPS-Seite zu laden. Zusätzlich gibt es CORS (Cross-Origin Resource Sharing) Fehler aufgrund von Zugriffskontrollbeschränkungen. Im Folgenden finden Sie eine schrittweise Anleitung zur Behebung dieses Problems.

---

### Warum das passiert
- **Mixed Content Fehler**: Die Webseite wird über HTTPS bereitgestellt, versucht aber, Ressourcen (wie die Versionsprüfung) von `http://127.0.0.1:9090` abzurufen, was unsicher ist. Browser blockieren diese Anfragen, um potenzielle Sicherheitslücken, wie Man-in-the-Middle-Angriffe, zu verhindern.
- **CORS Fehler**: Der Browser blockiert die Anfrage an `http://127.0.0.1:9090` aufgrund der CORS-Richtlinie, die cross-origin Anfragen einschränkt, sofern sie nicht explizit vom Server erlaubt werden.
- **Clash Kontext**: Clash (oder Clash for Windows) ist eine Proxy-Anwendung, die wahrscheinlich einen lokalen Server (`127.0.0.1:9090`) für ihr Dashboard oder ihre API verwendet. Wenn dieser lokale Server HTTPS nicht unterstützt oder nicht korrekt konfiguriert ist, lösen diese Fehler aus, wenn über eine HTTPS-Webseite darauf zugegriffen wird.

---

### Schritte zur Problembehebung

#### 1. **Clash Core Konfiguration überprüfen**
   - **Prüfen, ob der Clash Core läuft**: Stellen Sie sicher, dass der Clash Core (der Backend-Dienst) auf Ihrem Rechner läuft und auf `127.0.0.1:9090` lauscht. Sie können dies wie folgt überprüfen:
     - Öffnen Sie ein Terminal oder die Eingabeaufforderung.
     - Führen Sie `curl http://127.0.0.1:9090/version` aus, um zu prüfen, ob der Endpunkt mit der Clash-Version antwortet.
     - Wenn keine Antwort kommt, stellen Sie sicher, dass der Clash-Dienst aktiv ist. Starten Sie Clash for Windows oder den Clash Core Prozess neu.
   - **HTTPS für Clash Core aktivieren** (falls möglich):
     - Einige Versionen von Clash (z.B. Clash Premium oder Clash Meta) unterstützen HTTPS für die lokale API. Prüfen Sie die Clash-Dokumentation oder die Konfigurationsdatei (normalerweise `config.yaml`) auf eine Option, um HTTPS für den External Controller (den API-Endpunkt) zu aktivieren.
     - Suchen Sie nach einer Einstellung wie `external-controller` oder `external-ui` in der Konfigurationsdatei. Zum Beispiel:
       ```yaml
       external-controller: 127.0.0.1:9090
       external-ui: <path-to-ui>
       ```
       Wenn HTTPS unterstützt wird, müssen Sie möglicherweise ein Zertifikat für den lokalen Server konfigurieren. Dies ist fortgeschritten und erfordert möglicherweise die Erstellung eines selbstsignierten Zertifikats (siehe Schritt 4 unten).

#### 2. **Auf das Dashboard über HTTP zugreifen (Vorübergehende Problemumgehung)**
   - Wenn auf das Clash-Dashboard über HTTP zugegriffen werden kann (z.B. `http://clash.razord.top/` anstelle von HTTPS), versuchen Sie, es ohne HTTPS zu laden, um Mixed Content-Probleme zu vermeiden:
     - Öffnen Sie Ihren Browser und navigieren Sie zu `http://clash.razord.top/`.
     - Hinweis: Dies wird für den Produktiveinsatz nicht empfohlen, da HTTP unsicher ist. Verwenden Sie dies nur zum Testen oder wenn das Dashboard nur lokal aufgerufen wird.
   - Wenn das Dashboard HTTPS erfordert, fahren Sie mit den nächsten Schritten fort, um die Ursache zu beheben.

#### 3. **URLs auf HTTPS aktualisieren**
   - Der Fehler deutet darauf hin, dass das Clash-Dashboard versucht, Ressourcen von `http://127.0.0.1:9090` abzurufen. Wenn Sie Zugriff auf den Quellcode oder die Konfiguration des Clash-Dashboards haben:
     - Prüfen Sie den Frontend-Code (z.B. `index-5e90ca00.js` oder `vendor-827b5617.js`) auf hartkodierte `http://127.0.0.1:9090`-Referenzen.
     - Aktualisieren Sie diese auf `https://127.0.0.1:9090`, falls der Clash Core HTTPS unterstützt, oder verwenden Sie eine relative URL (z.B. `/version`), damit der Browser dasselbe Protokoll wie die Seite verwendet.
     - Wenn Sie keinen Zugriff auf den Quellcode haben, müssen Sie möglicherweise einen Reverse Proxy konfigurieren (siehe Schritt 4).

#### 4. **Einen Reverse Proxy mit HTTPS einrichten**
   - Um das Mixed Content-Problem zu lösen, können Sie einen Reverse Proxy (z.B. mit Nginx oder Caddy) einrichten, um die Clash Core API (`http://127.0.0.1:9090`) über HTTPS bereitzustellen. Dies ermöglicht dem Dashboard, sicher mit dem Core zu kommunizieren.
   - **Schritte für Nginx**:
     1. Installieren Sie Nginx auf Ihrem System (falls noch nicht geschehen).
     2. Erstellen Sie ein selbstsigniertes SSL-Zertifikat für `127.0.0.1`:
        ```bash
        openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout localhost.key -out localhost.crt -subj "/CN=localhost"
        ```
     3. Konfigurieren Sie Nginx so, dass Anfragen an `http://127.0.0.1:9090` über HTTPS weitergeleitet werden. Erstellen Sie eine Konfigurationsdatei (z.B. `/etc/nginx/sites-available/clash`):
        ```nginx
        server {
            listen 443 ssl;
            server_name localhost;

            ssl_certificate /path/to/localhost.crt;
            ssl_certificate_key /path/to/localhost.key;

            location / {
                proxy_pass http://127.0.0.1:9090;
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;
            }
        }
        ```
     4. Aktivieren Sie die Konfiguration und starten Sie Nginx neu:
        ```bash
        sudo ln -s /etc/nginx/sites-available/clash /etc/nginx/sites-enabled/
        sudo nginx -t
        sudo systemctl restart nginx
        ```
     5. Aktualisieren Sie das Clash-Dashboard so, dass es `https://localhost:443` anstelle von `http://127.0.0.1:9090` für API-Anfragen verwendet.
     6. Akzeptieren Sie in Ihrem Browser das selbstsignierte Zertifikat, wenn Sie dazu aufgefordert werden.

   - **Alternative mit Caddy**: Caddy ist einfacher zu konfigurieren und handhabt HTTPS automatisch:
     1. Installieren Sie Caddy.
     2. Erstellen Sie eine `Caddyfile`:
        ```caddy
        localhost:443 {
            reverse_proxy http://127.0.0.1:9090
        }
        ```
     3. Führen Sie Caddy aus: `caddy run`.
     4. Aktualisieren Sie das Clash-Dashboard so, dass es `https://localhost:443` verwendet.

#### 5. **CORS-Beschränkungen umgehen (Fortgeschritten)**
   - Der CORS-Fehler (`XMLHttpRequest cannot load http://127.0.0.1:9090/version due to access control checks`) deutet darauf hin, dass der Clash Core Server nicht die entsprechenden CORS-Header sendet. Wenn Sie den Clash Core kontrollieren:
     - Modifizieren Sie die Clash Core Konfiguration, um CORS-Header einzubinden, wie z.B.:
       ```yaml
       external-controller: 127.0.0.1:9090
       allow-cors: true
       ```
       (Prüfen Sie die Clash-Dokumentation für die genaue Syntax, da dies von der Clash-Version abhängt.)
     - Alternativ kann das Reverse Proxy-Setup aus Schritt 4 CORS handhaben, indem Header wie folgt hinzugefügt werden:
       ```nginx
       add_header Access-Control-Allow-Origin "https://clash.razord.top";
       add_header Access-Control-Allow-Methods "GET, POST, OPTIONS";
       add_header Access-Control-Allow-Headers "*";
       ```
   - Wenn Sie den Core nicht kontrollieren, können Sie eine Browser-Erweiterung verwenden, um CORS vorübergehend zu umgehen (z.B. "CORS Unblock" für Chrome), was jedoch aus Sicherheitsgründen nicht empfohlen wird.

#### 6. **Clash aktualisieren oder auf eine kompatible Version wechseln**
   - Stellen Sie sicher, dass Sie die neueste Version von Clash for Windows oder Clash Verge verwenden, da ältere Versionen Fehler aufweisen oder keine HTTPS-Unterstützung für den External Controller haben könnten.
   - Prüfen Sie das Clash GitHub-Repository (`github.com/Dreamacro/clash` oder `github.com/Fndroid/clash_for_windows_pkg`) auf Updates oder gemeldete Probleme im Zusammenhang mit Mixed Content oder CORS.
   - Erwägen Sie einen Wechsel zu **Clash Verge** oder **Clash Meta**, die möglicherweise eine bessere Unterstützung für HTTPS und moderne Browser-Sicherheitsrichtlinien bieten.

#### 7. **Unsichere Inhalte im Browser erlauben (Nicht empfohlen)**
   - Als letzten Ausweg können Sie unsichere Inhalte in Ihrem Browser für `https://clash.razord.top/` erlauben:
     - **Chrome**:
       1. Klicken Sie auf das Schloss-Symbol in der Adressleiste.
       2. Gehen Sie zu "Site-Einstellungen" > "Unsicherer Inhalt" > Auf "Erlauben" setzen.
     - **Firefox**:
       1. Klicken Sie auf das Schloss-Symbol und gehen Sie zu "Verbindungseinstellungen".
       2. Deaktivieren Sie vorübergehend "Gefährliche und trügerische Inhalte blockieren".
     - **Warnung**: Dies umgeht die Sicherheitsschutzmaßnahmen und sollte nur für lokale Tests in vertrauenswürdigen Netzwerken verwendet werden.
   - Alternativ können Sie Chrome mit dem Flag `--disable-web-security` starten (nur für die Entwicklung):
     ```bash
     google-chrome --disable-web-security --user-data-dir="/tmp/chrome_dev"
     ```

#### 8. **Auf konfliktverursachende Erweiterungen oder Firewall prüfen**
   - Browser-Erweiterungen (z.B. Ad-Blocker, Privacy-Tools) oder Firewall-Einstellungen könnten den lokalen Server von Clash stören. Deaktivieren Sie Erweiterungen vorübergehend oder prüfen Sie Ihre Firewall, um sicherzustellen, dass `127.0.0.1:9090` erreichbar ist.
   - Stellen Sie unter Windows sicher, dass die Clash-App Firewall-Berechtigungen hat:
     - Gehen Sie zu Einstellungen > Netzwerk & Internet > Windows-Firewall > App durch Windows-Firewall zulassen.
     - Fügen Sie Clash for Windows hinzu oder aktivieren Sie es.

#### 9. **Clash Support oder Community kontaktieren**
   - Wenn die oben genannten Schritte das Problem nicht lösen, melden Sie das Problem auf der Clash for Windows GitHub Issues-Seite (`github.com/Fndroid/clash_for_windows_pkg/issues`) oder in den Clash Community-Foren. Geben Sie Details zu Ihrem Setup an, einschließlich:
     - Clash-Version.
     - Betriebssystem.
     - Konfigurationsdatei (vertrauliche Informationen schwärzen).
     - Browser und Version.
   - Prüfen Sie in der Community auf ähnliche Probleme, da dieser Fehler spezifisch für bestimmte Clash-Versionen oder Konfigurationen sein könnte.

---

### Empfohlener Ansatz
Die sicherste und robusteste Lösung ist, **einen Reverse Proxy mit HTTPS einzurichten** (Schritt 4), um sicherzustellen, dass alle Anfragen über HTTPS bereitgestellt werden, was sowohl die Mixed Content- als auch die CORS-Probleme löst. Wenn Sie den Clash Core oder das Dashboard nicht modifizieren können, ist die Verwendung einer neueren Clash-Version (z.B. Clash Verge) oder der vorübergehende Zugriff auf das Dashboard über HTTP (Schritt 2) möglicherweise eine schnellere Problemumgehung.

---

### Zusätzliche Hinweise
- Wenn Sie ein benutzerdefiniertes Clash-Dashboard oder einen Drittanbieterdienst wie `clash.razord.top` verwenden, verifizieren Sie, dass es mit Ihrer Clash Core-Version kompatibel ist.
- Sichern Sie immer Ihre Clash-Konfiguration (`config.yaml`), bevor Sie Änderungen vornehmen.
- Wenn das Problem bestehen bleibt, können Sie versuchen, auf alternative Proxy-Clients wie v2rayN oder OpenVPN umzusteigen, die möglicherweise eine bessere HTTPS-Unterstützung für lokale APIs bieten.

Lassen Sie mich wissen, wenn Sie Hilfe bei bestimmten Schritten benötigen, z.B. beim Einrichten von Nginx oder beim Debuggen der Clash-Konfiguration!
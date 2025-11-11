---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Safari Localhost Authentifizierungsbehebung
translated: true
type: note
---

Dieses Problem tritt auf, weil Safari auf macOS strengere Sicherheitsrichtlinien als Chrome für localhost-URLs durchsetzt. Insbesondere erfordert Safari einen sicheren HTTPS-Kontext, um persistente Cookies und Authentifizierungssitzungen zu erlauben, was verhindert, dass es zu potenziellen Logout-Schleifen oder erneuten Authentifizierungen bei jedem Besuch für Apps wie LibreChat kommt, die über HTTP laufen. Chrome ist mit HTTP auf localhost toleranter, weshalb die Authentifizierung dort bestehen bleibt, aber nicht in Safari.[1][2][3]

### Wichtige Faktoren
- **Browser-Richtlinien**: Moderne Browser wie Safari fordern HTTPS für localhost, um Mixed-Content-Warnungen und Sitzungsunsicherheiten zu vermeiden.
- **LibreChat-Verhalten**: LibreChat verwendet sichere Cookie- oder localStorage-basierte Token für die Authentifizierung, die bei HTTP in Safari aufgrund der strengeren Handhabung nicht-sicherer Ursprünge brechen.

### Lösungen (Sortiert nach Einfachheit und Wirksamkeit)
1. **HTTPS für Localhost einrichten (Empfohlen)**:
   - Die eigene Dokumentation und der Blog von LibreChat empfehlen dies, um HTTP-bedingte Logouts zu verhindern.[1]
   - Verwenden Sie `mkcert` (ein kostenloses Tool), um lokale SSL-Zertifikate für localhost zu generieren und zu vertrauen:
     - Installieren Sie `mkcert` via `brew install mkcert` oder laden Sie es von GitHub herunter.
     - Führen Sie `mkcert -install` aus, um die Root-CA zu installieren.
     - Erstellen Sie Zertifikate: `mkcert localhost 127.0.0.1`.
     - Konfigurieren Sie LibreChat (z.B. via Docker-Env-Vars oder Konfiguration) zur Verwendung dieser Zertifikate: Fügen Sie `HTTPS=true`, `SSL_CRT_FILE=/pfad/zu/localhost.pem` und `SSL_KEY_FILE=/pfad/zu/localhost-key.pem` in Ihrer `.env`-Datei oder Umgebung hinzu.
     - Starten Sie LibreChat neu und greifen Sie über `https://localhost:3080` zu.
     - Safari wird dies nun als sicher behandeln und nahtlose Logins erlauben.

2. **Alternative: Verwenden Sie 127.0.0.1 anstelle von localhost**:
   - Safari verhält sich manchmal anders mit `localhost` (aufgrund von IPv6 oder DNS-Auflösung). Versuchen Sie, auf `http://127.0.0.1:3080` zuzugreifen – dies hat ähnliche Verbindungsprobleme in einigen Fällen gelöst, obwohl es die Auth-Persistenz möglicherweise nicht vollständig behebt.[4][4][5]

3. **Safari-Website-Daten für localhost löschen**:
   - Gehen Sie zu Safari > Einstellungen > Datenschutz > Website-Daten verwalten > Suchen Sie nach "localhost" > Entfernen Sie alle Einträge.
   - Dies zwingt Safari dazu, die Erzwingung von HTTPS-Upgrades oder zwischengespeicherten unsicheren Kontexten zu beenden.[3][2]
   - Starten Sie Safari neu und testen Sie es; wenn LibreChat es unterstützt, sollte die Authentifizierung bestehen bleiben.

Wenn keine dieser Lösungen funktioniert, überprüfen Sie die LibreChat-Protokolle auf Authentifizierungsfehler, stellen Sie sicher, dass Ihre `.env` keine konfligierenden Flags enthält (z.B. deaktiviert `ALLOW_ANONYMOUS=true` die Authentifizierung vollständig, falls gewünscht), und bestätigen Sie, dass Sie sich nicht im privaten Browsing-Modus von Safari befinden, der persistenten Speicher blockiert.[6][7] Wenn das Problem weiterhin besteht, geben Sie Ihre LibreChat-Version und .env-Konfiguration für eine tiefergehende Fehlerbehebung an.

Zitate:
[1] https://www.librechat.ai/blog/2024-05-16_unsecured_http
[2] https://github.com/danny-avila/LibreChat/discussions/529
[3] https://stackoverflow.com/questions/46394682/safari-keeps-forcing-https-on-localhost
[4] https://superuser.com/questions/30827/safari-is-unable-to-reach-localhost-127-0-0-1
[5] https://apple.stackexchange.com/questions/422556/localhost-has-stopped-working-on-chrome-and-safari-since-upgrading-to-big-sur
[6] https://www.librechat.ai/docs/configuration/authentication
[7] https://discussions.apple.com/thread/255906354
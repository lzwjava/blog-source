---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Deaktivierung von LibreChat-Websuchezitaten
translated: true
type: note
---

## Deaktivieren von Zitaten im LibreChat Web-Suchmodus

Die Web-Suchfunktion von LibreChat (unterstützt von Anbietern wie Serper.dev oder SearxNG, kombiniert mit Scrapern wie Firecrawl) fügt Antworten automatisch Zitate hinzu, um Quellen zu kennzeichnen und die Transparenz zu verbessern. Basierend auf der offiziellen Dokumentation und Community-Diskussionen gibt es keinen integrierten, benutzerseitigen Schalter, um Web-Suchzitate auf individueller Benutzerebene spezifisch zu deaktivieren. Sie können dies jedoch über Konfigurationsänderungen erreichen oder annähern, hauptsächlich für Administratoren oder Self-Hoster. So geht's:

### 1. **Administrator-Konfiguration (Empfohlener Ansatz)**
   Wenn Sie Ihre eigene LibreChat-Instanz betreiben (Self-Hosted), können Sie die Konfigurationsdateien ändern, um die Zitatanzeige einzuschränken oder zu entfernen. Zitate werden über die Oberfläche und die Suchkomponenten verarbeitet.

   - **Bearbeiten von `librechat.yaml` für Interface-Einstellungen**:
     LibreChat verwendet eine YAML-Datei für globale Einstellungen. Suchen Sie nach dem Abschnitt `interface`, der die Sichtbarkeit von Zitaten steuert (inspiriert von Datei-Zitatsteuerungen, die sich auf die Web-Suche auswirken können).
     - Setzen Sie `fileCitations` auf `false`, um Zitatberechtigungen global zu deaktivieren. Dies ist zwar explizit für Dateisuchen, kann aber in einigen Setups das Rendering der Web-Such-UI beeinflussen.
       ```yaml
       interface:
         fileCitations: false  # Deaktiviert die Zitatanzeige für Suchen insgesamt
       ```
     - Speziell für die Web-Suche können Sie unter dem Abschnitt `webSearch` Anbieter deaktivieren oder anpassen, um eine detaillierte Quellenverlinkung zu vermeiden:
       ```yaml
       webSearch:
         enabled: true  # Aktiviert lassen, aber Anbieter anpassen
         serper:  # Oder Ihr Anbieter
           enabled: true
           # Kein direktes 'citations'-Flag, aber das Weglassen von API-Schlüsseln für Scraper wie Firecrawl reduziert detaillierte Extrakte/Zitate
         firecrawl:
           enabled: false  # Deaktiviert das Scraping von Inhalten, was oft Zitate generiert
       ```
     - Starten Sie Ihre LibreChat-Instanz nach den Änderungen neu. Quelle für Interface-Konfiguration: [LibreChat Interface Object Structure](https://www.librechat.ai/docs/configuration/librechat_yaml/object_structure/interface)[1].

   - **Umgebungsvariablen (.env Datei)**:
     Deaktivieren Sie in Ihrer `.env`-Datei Debug- oder Logging-Modi, die Zitate erzwingen könnten, oder setzen Sie die Web-Suche auf einen minimalen Anbieter.
     - Beispiel:
       ```
       DEBUG_PLUGINS=false  # Reduziert die ausführliche Ausgabe, einschließlich Zitate
       SERPER_API_KEY=your_key  # Verwenden Sie einen einfachen Suchanbieter ohne Scraping für weniger Zitate
       FIRECRAWL_API_KEY=  # Leer lassen, um Scraper zu deaktivieren (keine Seitenextrakte/Zitate)
       ```
     - Dies verschiebt die Antworten zu reinen Zusammenfassungssuchergebnissen ohne Inline-Zitate. Vollständiges Setup: [LibreChat .env Configuration](https://www.librechat.ai/docs/configuration/dotenv)[2].

   - **Anpassung des Web-Suchanbieters**:
     Wechseln Sie zu einem Anbieter wie SearxNG, der serverseitig konfiguriert werden kann, um Quelllinks wegzulassen.
     - Setzen Sie `SEARXNG_INSTANCE_URL=your_minimal_searxng_url` in `.env`.
     - Bearbeiten Sie in Ihrer SearxNG-Instanz deren Einstellungen, um Ergebnis-Metadaten zu unterdrücken (z. B. über `settings.yml` in SearxNG: deaktivieren Sie `reveal_version: false` und passen Sie Templates an, um Links zu entfernen).
     - Dokumentation: [Web Search Configuration](https://www.librechat.ai/docs/configuration/librechat_yaml/object_structure/web_search)[3].

### 2. **Benutzer-Workarounds (Ohne Administratorzugriff)**
   Wenn Sie einen gehosteten LibreChat verwenden (z. B. eine öffentliche Instanz), sind die Optionen begrenzt, da Zitate oft aus Gründen der Genauigkeit erzwungen werden:
   - **Prompt Engineering**: Weisen Sie die KI explizit in Ihren Nachrichten an, z. B.: "Durchsuche das Web, aber füge keine Zitate oder Quellen in deiner Antwort hinzu." Dies funktioniert inkonsistent, da das Suchtool sie möglicherweise dennoch anhängt, aber viele Modelle werden teilweise entsprechen.
   - **Web-Suche vollständig deaktivieren**: Wenn Zitate das Hauptproblem sind, schalten Sie die Web-Suche pro Konversation aus:
     - Klicken Sie in der Chat-Oberfläche nicht auf die Schaltfläche "Web Search".
     - Für Agents: Entfernen Sie beim Erstellen/Bearbeiten eines Agents die `web_search`-Fähigkeit in der Konfiguration des Agents (über die Agents-UI). Quelle: [Agents Documentation](https://www.librechat.ai/docs/features/agents)[4].
     - Bitten Sie Administratoren, einen Schalter hinzuzufügen; Community-Diskussionen schlagen dies als Feature-Request vor (z. B. [GitHub Discussion on Web Search Toggle](https://github.com/danny-avila/LibreChat/discussions/7738)[5]).

### 3. **Einschränkungen und Hinweise**
   - Zitate sind ein Kernbestandteil der Web-Suche, um eine ethische KI-Nutzung und Nachverfolgbarkeit zu gewährleisten. Daher könnte das vollständige Deaktivieren benutzerdefinierte Codeänderungen erfordern (z. B. das Bearbeiten von Frontend-Komponenten wie `WebSearchResults.jsx` im GitHub-Repo, um Zitatelemente auszublenden).
   - Es gibt keine direkte "Zitate ausschalten"-Option in aktuellen Versionen (Stand Oktober 2025). Prüfen Sie auf Updates in der [Web Search Feature Docs](https://www.librechat.ai/docs/features/web_search)[6], da sich die Funktionen weiterentwickeln.
   - Wenn Sie self-hosten, testen Sie Änderungen in einer Entwicklungsumgebung – das Deaktivieren von Scrapern könnte die Antwortqualität verringern.
   - Community-Feedback (z. B. Reddit) weist auf gelegentliche Bugs mit Suchfunktionen hin, aber nichts Spezifisches zu Zitaten: [Reddit Thread on LibreChat Issues](https://www.reddit.com/r/LocalLLaMA/comments/1k2hraj/is_it_just_me_or_is_librechat_a_complete_buggy/)[7].

Für offiziellen Support treten Sie dem LibreChat Discord bei oder öffnen Sie ein GitHub-Issue mit Ihren Setup-Details. Wenn dies das Problem nicht löst, geben Sie mehr Kontext zu Ihrer LibreChat-Version oder Hosting-Methode an!

Zitate:
[1] https://www.librechat.ai/docs/configuration/librechat_yaml/object_structure/interface
[2] https://www.librechat.ai/docs/configuration/dotenv
[3] https://www.librechat.ai/docs/configuration/librechat_yaml/object_structure/web_search
[4] https://www.librechat.ai/docs/features/agents
[5] https://github.com/danny-avila/LibreChat/discussions/7738
[6] https://www.librechat.ai/docs/features/web_search
[7] https://www.reddit.com/r/LocalLLaMA/comments/1k2hraj/is_it_just_me_or_is_librechat_a_complete_buggy/
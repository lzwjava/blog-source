---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Übersicht der n8n Workflow-Automatisierungsplattform
translated: true
type: note
---

n8n (ausgesprochen "n-eight-n") ist eine Open-Source-Workflow-Automatisierungsplattform, die für technische Teams und Entwickler konzipiert ist. Sie ermöglicht es, verschiedene Apps, Dienste und APIs zu verbinden, um repetitive Aufgaben, Datenflüsse und komplexe Prozesse zu automatisieren, ohne stark auf benutzerdefinierten Code angewiesen zu sein – obwohl sie Code bei Bedarf unterstützt. Man kann es sich als eine selbst gehostete Alternative zu Tools wie Zapier oder Make vorstellen, aber mit mehr Flexibilität, einschließlich der Möglichkeit, mehrstufige KI-Agenten zu erstellen, jedes Large Language Model (LLM) zu integrieren und alles auf der eigenen Infrastruktur für bessere Datenschutz und Kontrolle auszuführen.

Im Kern verwendet n8n eine visuelle, knotenbasierte Oberfläche, in der Workflows durch Ziehen und Verbinden von "Nodes" (Bausteine, die Trigger, Aktionen oder Transformationen darstellen) erstellt werden. Es ist unter einer Fair-Code-Lizenz lizenziert (Quellcode auf GitHub verfügbar), unterstützt über 400 vorgefertigte Integrationen (z.B. Google Sheets, Slack, OpenAI, GitHub) und kann alles von einfachen Benachrichtigungen bis hin zu fortschrittlichen KI-gesteuerten Automatisierungen wie dem Zusammenfassen von Tickets oder dem Erstellen von Inhalten bewältigen.

### Wichtige Funktionen
- **Visueller Workflow-Builder**: Drag-and-Drop Nodes für No-Code-Einrichtungen, mit Optionen zum Einbetten von JavaScript, Python oder sogar npm/Python-Bibliotheken für benutzerdefinierte Logik.
- **KI-Integration**: Erstellen Sie mehrstufige Agenten mit Tools wie LangChain, verbinden Sie sich mit jedem LLM (lokal oder cloud-basiert) und erstellen Sie Chat-Oberflächen zum Abfragen von Daten oder Ausführen von Aufgaben über Slack, SMS oder Sprache.
- **Self-Hosting & Sicherheit**: Vollständige On-Premise-Bereitstellung via Docker oder npm; unterstützt SSO, verschlüsselte Geheimnisse, RBAC und Audit-Logs. Kein Vendor Lock-in – hosten Sie auch Ihre eigenen KI-Modelle.
- **Hybride Entwicklung**: Kombinieren Sie UI mit Code; spielen Sie Daten für Tests erneut ab, nutzen Sie Inline-Logs für das Debugging und über 1.700 Vorlagen für schnelle Starts.
- **Skalierbarkeit**: Enterprise-Features wie Workflow-Verlauf, Git-Versionskontrolle, isolierte Umgebungen und Einbettung für kundenorientierte Automatisierungen.
- **Leistungsbeispiele**: Unternehmen wie Delivery Hero sparen monatlich über 200 Stunden; StepStone verdichtet wochenlange Arbeit auf Stunden.

Im Vergleich zu Zapier ist n8n entwicklerfreundlicher (Zugriff auf Code, Self-Hosting), kosteneffizienter (kostenloser Kern, keine Gebühren pro Aufgabe) und datenschutzorientierter (keine Datenrouting über Dritte). Es ist ideal für Teams, die mit sensiblen Daten in den Bereichen Finanzen, Gesundheitswesen oder internem Betrieb umgehen.

# So verwenden Sie n8n: Umfassende Anleitung

Diese Anleitung führt Sie durch alles von der Einrichtung bis zur fortgeschrittenen Nutzung. Wir verwenden ein praktisches Beispiel: einen RSS-Feed-Monitor, der täglich neue Artikel per E-Mail verschickt (erweiterbar um KI-Zusammenfassungen). Gehen Sie von grundlegendem Technik-Komfort aus; n8n läuft auf Node.js.

## 1. Installation und Einrichtung

n8n ist leichtgewichtig und schnell zu starten. Voraussetzungen: Node.js (v18+ empfohlen) für lokale Installationen; Docker für Container. Für den Produktionseinsatz verwenden Sie einen VPS wie DigitalOcean oder AWS.

### Schneller lokaler Start (Entwicklung/Test)
1. Öffnen Sie Ihr Terminal.
2. Führen Sie aus: `npx n8n`
   - Dies lädt n8n herunter und startet es temporär.
3. Greifen Sie auf den Editor unter `http://localhost:5678` in Ihrem Browser zu.
   - Standard-Login: Anfangs sind keine Anmeldedaten erforderlich (stellen Sie diese später für die Sicherheit ein).

### Permanente lokale Installation (npm)
1. Installieren Sie global: `npm install n8n -g`
2. Starten Sie: `n8n start`
3. Greifen Sie zu unter `http://localhost:5678`.

### Docker (Empfohlen für die Produktion)
1. Ziehen Sie das Image: `docker run -it --rm --name n8n -p 5678:5678 -v ~/.n8n:/home/node/.n8n n8nio/n8n`
   - Dies bildet ein Volume für Datenpersistenz ab.
2. Für erweiterte Setups (z.B. PostgreSQL-DB): Verwenden Sie `docker-compose.yml` aus der Dokumentation.
3. Greifen Sie zu unter `http://localhost:5678`.

### Cloud-Optionen
- **n8n Cloud**: Verwaltetes Hosting unter n8n.io – registrieren Sie sich, stellen Sie in Minuten bereit, starten Sie kostenlos mit Limits.
- **Drittanbieter-PaaS**: Verwenden Sie Render, Railway oder Sevalla (One-Click-Templates). Beispiel auf Sevalla:
  1. Registrieren Sie sich unter sevalla.com.
  2. Wählen Sie das "n8n"-Template aus, stellen Sie Ressourcen bereit (z.B. 1 CPU, 1 GB RAM).
  3. Erhalten Sie eine URL wie `https://your-n8n.sevalla.app`.

**Tipps**: Für Self-Hosting, sichern Sie mit HTTPS (über Reverse-Proxy wie Nginx), setzen Sie Umgebungsvariablen (z.B. `N8N_BASIC_AUTH_ACTIVE=true`) und sichern Sie den Ordner `~/.n8n`. Skalieren Sie mit dem Queue-Modus für hochvolumige Workflows.

## 2. UI-Übersicht

Sobald geöffnet:
- **Canvas**: Leerer Arbeitsbereich für Workflows. Klicken Sie auf "+", um Nodes hinzuzufügen.
- **Node-Panel**: Durchsuchbare Bibliothek mit 400+ Nodes (z.B. "Schedule Trigger").
- **Ausführungspanel**: Zeigt den Datenfluss in Echtzeit während Tests.
- **Seitenleiste**: Workflow-Einstellungen, Ausführungsverlauf, Vorlagen.
- **Obere Leiste**: Speichern, Aktivieren/Deaktivieren-Umschalter, Teilen/Export-Optionen.

Workflows werden automatisch gespeichert; verwenden Sie Git für Versionskontrolle in Teams.

## 3. Kernkonzepte

- **Workflow**: Eine Sequenz verbundener Nodes, die die Automatisierungslogik definiert. Aktive Workflows laufen bei Triggern; inaktive sind für Tests.
- **Nodes**: Modulare Blöcke:
  - **Trigger**: Starten Workflows (z.B. Schedule für Cron-Jobs, Webhook für HTTP-Ereignisse, RSS Read für Feeds).
  - **Aktionen**: Verrichten Arbeit (z.B. Send Email, HTTP Request für APIs, Function für benutzerdefinierten Code).
  - **Core Nodes**: IF (Bedingungen), Merge (Daten kombinieren), Set (Variablen manipulieren).
- **Verbindungen**: Pfeile zwischen Nodes zeigen den Datenfluss (JSON-Format). Daten von einem Node speisen den nächsten.
- **Ausdrücke**: Dynamische Platzhalter wie `{{ $json.title }}`, um Daten (z.B. Artikeltitel) in Felder zu ziehen. Verwenden Sie `$now` für Zeitstempel oder `$input.all()` für Batches.
- **Credentials**: Sichere Speicherung für API-Schlüssel/OAuth. Einmal pro Dienst einstellen (z.B. Gmail OAuth) und über Nodes hinweg wiederverwenden.
- **Executions**: Läufe eines Workflows; zeigen Sie Logs an, spielen Sie Daten erneut ab oder debuggen Sie Fehler.

## 4. Erstellen Ihres ersten Workflows: Schritt für Schritt

Lassen Sie uns "Daily RSS Digest Email" erstellen.

1. **Neuen Workflow erstellen**:
   - Klicken Sie auf "New" > Nennen Sie ihn "RSS Digest".
   - Canvas öffnet sich.

2. **Trigger-Node hinzufügen**:
   - Klicken Sie auf "+" > Suchen Sie "Schedule Trigger".
   - Konfigurieren: Trigger "Every Day" um 9:00 Uhr (Cron: `0 9 * * *`).
   - Test: Klicken Sie auf "Execute Node" (führt einmal jetzt aus).

3. **Datenabruf-Node hinzufügen**:
   - Klicken Sie auf "+" nach dem Trigger > "RSS Read".
   - URL: `https://blog.cloudflare.com/rss/`.
   - Ausführen: Ruft Elemente ab (z.B. JSON mit Titel, Link, pubDate).

4. **Daten transformieren (Optionale Function-Node)**:
   - "+" > "Function".
   - Code:
     ```
     // Auf die ersten 3 Elemente beschränken
     return items.slice(0, 3);
     ```
   - Dies führt JS auf eingehenden Daten aus.

5. **Aktions-Node hinzufügen**:
   - "+" > "Gmail" (oder "Email Send" für SMTP).
   - Credentials: Klicken Sie auf "Create New" > OAuth für Gmail (folgen Sie dem Google-Auth-Flow).
   - An: Ihre E-Mail.
   - Betreff: `Daily Digest: {{ $input.first().json.title }}`
   - Nachricht: Schleife über Elemente mit Ausdruck:
     ```
     {{#each $input.all()}}
     - {{ $json.title }}: {{ $json.link }} ({{ $json.pubDate }})
     {{/each}}
     ```
   - (Verwendet Handlebars-ähnliche Syntax für Schleifen.)

6. **Verbinden & Testen**:
   - Ziehen Sie Pfeile: Trigger → RSS → Function → Email.
   - "Execute Workflow": Beobachten Sie den Datenfluss; prüfen Sie den Posteingang.
   - Fehler beheben: Rote Nodes heben Probleme hervor (z.B. ungültige Credentials).

7. **Aktivieren**:
   - Schalten Sie den "Active"-Umschalter ein. Es läuft nun täglich.

Speichern und als JSON exportieren, um es zu teilen.

## 5. Erstellen komplexerer Workflows

- **Bedingungen**: Fügen Sie "IF"-Node nach RSS hinzu: `{{ $json.pubDate }} > {{ $now.minus({days:1}) }}`, um neue Elemente zu filtern.
- **Schleifen & Batches**: Verwenden Sie "Split In Batches" für die Verarbeitung großer Datensätze.
- **Fehlerbehandlung**: Fügen Sie "Error Trigger"-Workflow oder "IF" für Wiederholungsversuche hinzu. Verwenden Sie "Set", um Fehler zu protokollieren.
- **API-Integrationen**: "HTTP Request"-Node für benutzerdefinierte Endpunkte (z.B. POST an Slack-Webhook).
- **Datenmanipulation**: "Edit Fields" oder Function-Nodes für JSON-Anpassungen.
- **Testen**: Spielen Sie bestimmte Ausführungen erneut ab; mocken Sie Daten in Nodes.

Beispiel: Twitter-Monitor
1. Trigger: "Twitter Trigger" bei Erwähnungen.
2. KI-Node: "OpenAI" zur Sentiment-Klassifizierung.
3. IF: Positiv → CRM hinzufügen; Negativ → Slack-Benachrichtigung.

## 6. Fortgeschrittene Nutzung & Best Practices

- **KI-Workflows**: Fügen Sie "AI Agent"-Node hinzu > Kette mit Tools (z.B. suchen, zusammenfassen). Integrieren Sie lokale LLMs über "Ollama"-Node.
- **Benutzerdefinierte Nodes**: Bauen Sie via JS (Dokumentation Tutorial); veröffentlichen Sie in der Community.
- **Skalierung**: Verwenden Sie Queue-Modus (`N8N_WORKER=1`), externe DB (PostgreSQL) und Webhooks für Echtzeit.
- **Sicherheit**: Verschlüsseln Sie Geheimnisse, verwenden Sie RBAC für Teams, Audit-Logs.
- **Debugging**: Inline-Logs in Functions (`console.log(items)`); Versionierung mit Git.
- **Häufige Fallstricke**: Achten Sie auf Datentypen (alles JSON); behandeln Sie Ratenlimits in Nodes; starten Sie einfach, bevor Sie KI verwenden.
- **Erweiterungen**: Einbetten in Apps, verwenden Sie Vorlagen (1700+ verfügbar) oder npm für Extras.

Für die Produktion: Überwachen Sie via externer Tools; Self-Hosting spart Kosten (gegenüber Zapiers 20 $+/Monat).

## Referenzen
- [n8n Offizielle Website](https://n8n.io/)
- [n8n Dokumentation - Installation](https://docs.n8n.io/hosting/installation/)
- [freeCodeCamp Beginner's Guide](https://www.freecodecamp.org/news/a-beginners-guide-to-automation-with-n8n/)
- [n8n Workflows Docs](https://docs.n8n.io/workflows/)
- [Medium: Mastering n8n Guide](https://medium.com/data-science-collective/mastering-n8n-from-scratch-a-step-by-step-guide-for-beginners-its-easier-than-you-think-2d7ca5d47277)
- [Wikipedia: n8n](https://en.wikipedia.org/wiki/N8n)
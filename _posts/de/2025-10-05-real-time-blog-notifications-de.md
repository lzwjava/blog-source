---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Echtzeit-Blog-Besuch-Telegram-Benachrichtigungen
translated: true
type: note
---

Ja, du kannst ein System einrichten, um Cloudflare-Logs oder Traffic in nahezu Echtzeit zu analysieren und Telegram-Benachrichtigungen für jeden Blog-Besuch zu senden, aber mit Standard-Analyse-Logs allein ist es nicht einfach. Die Analysen von Cloudflare sind größtenteils aggregiert (z.B. tägliche/wöchentliche Zusammenfassungen), und selbst deren Logpush-Funktion (die Logs exportiert) bündelt Daten alle 1-5 Minuten, was sie für sofortige Benachrichtigungen pro Besuch ungeeignet macht. Instant Logs bietet Echtzeit-Streaming, erfordert jedoch einen Business- oder Enterprise-Plan und würde eine benutzerdefinierte Verarbeitung (z.B. via WebSocket und einem Skript) benötigen, um Telegram-Nachrichten auszulösen – das ist für die meisten Benutzer übertrieben.

Der praktischste und echtzeitfähigste Ansatz ist die Verwendung von **Cloudflare Workers**, um jede eingehende Anfrage an deinen Blog abzufangen. Dies führt serverlosen Code bei jedem Besuch aus, ermöglicht es dir, das Ereignis zu protokollieren und sofort eine Nachricht über die Telegram-API zu senden. Es ist kostenlos für geringen Traffic (bis zu 100.000 Anfragen/Tag), aber Blogs mit hohem Traffic könnten Limits erreichen oder Kosten verursachen – außerdem würdest du mit Benachrichtigungen überschwemmt werden, erwäge also Filterung (z.B. nur für eindeutige IPs oder bestimmte Seiten).

### Schnelle Einrichtungsschritte
1. **Erstelle einen Telegram-Bot**:
   - Schicke @BotFather auf Telegram eine Nachricht, verwende `/newbot`, um einen Bot zu erstellen, und notiere dir das Bot-Token (z.B. `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`).
   - Starte einen Chat mit deinem Bot, dann schicke @userinfobot eine Nachricht, um deine Chat-ID zu erhalten (z.B. `123456789`).
   - Teste das Senden einer Nachricht via curl:
     ```
     curl -X POST "https://api.telegram.org/bot<DEIN_BOT_TOKEN>/sendMessage" \
     -H "Content-Type: application/json" \
     -d '{"chat_id":"<DEINE_CHAT_ID>","text":"Testbesuch!"}'
     ```

2. **Erstelle einen Cloudflare Worker**:
   - Melde dich in deinem Cloudflare-Dashboard an > Workers & Pages > Anwendung erstellen > Worker erstellen.
   - Benenne ihn (z.B. `blog-visit-notifier`) und stelle die Standardvorlage bereit.

3. **Füge den Benachrichtigungscode hinzu**:
   - Bearbeite den Code des Workers, um Anfragen abzufangen und an Telegram zu senden. Hier ein einfaches Beispiel (ersetze die Platzhalter):
     ```javascript
     export default {
       async fetch(request, env) {
         // Optional: Protokolliere oder filtere den Besuch (z.B. nur für deine Blog-Startseite)
         const url = new URL(request.url);
         if (url.pathname !== '/') {  // Passe den Pfad bei Bedarf an
           return fetch(request);  // Überspringe Nicht-Blog-Seiten
         }

         // Sende Telegram-Nachricht (async, um Blockieren zu vermeiden)
         const message = `Neuer Besuch auf ${url.origin}! IP: ${request.headers.get('cf-connecting-ip')}, User-Agent: ${request.headers.get('user-agent')}`;
         await fetch(`https://api.telegram.org/bot${env.TELEGRAM_BOT_TOKEN}/sendMessage`, {
           method: 'POST',
           headers: { 'Content-Type': 'application/json' },
           body: JSON.stringify({
             chat_id: env.TELEGRAM_CHAT_ID,
             text: message,
             parse_mode: 'HTML'  // Für Formatierung, falls benötigt
           })
         }).catch(err => console.error('Senden an Telegram fehlgeschlagen:', err));

         // Leite die ursprüngliche Anfrage an deinen Blog weiter
         return fetch(request);
       }
     };
     ```
     - Dies wird bei jeder passenden Anfrage ausgeführt, protokolliert grundlegende Besucherinformationen und sendet sie via Telegram, ohne das Laden der Seite zu verzögern.

4. **Konfiguriere Umgebungsvariablen**:
   - In den Worker-Einstellungen > Variablen > Hinzufügen:
     - `TELEGRAM_BOT_TOKEN`: Dein Bot-Token.
     - `TELEGRAM_CHAT_ID`: Deine Chat-ID.
   - Speichere und stelle erneut bereit.

5. **Leite den Worker zu deinem Blog weiter**:
   - In Worker-Einstellungen > Trigger > Route hinzufügen.
   - Lege sie auf deine Blog-Domain/ deinen Pfad fest (z.B. `deinblog.com/*`).
   - Dies stellt sicher, dass der Worker bei jedem Besuch ausgeführt wird, bevor dein Origin-Server erreicht wird.

6. **Teste und überwache**:
   - Besuche deinen Blog – du solltest sofort einen Ping auf Telegram erhalten.
   - Überprüfe die Worker-Logs im Dashboard auf Fehler. Wenn du Ratenlimits erreichst (z.B. 30 Nachrichten/Sek. von Telegram), füge Debouncing mit KV Storage hinzu.

### Alternativen, wenn Workers nicht passen
- **Für gebündelte Log-Analyse**: Verwende Logpush, um HTTP-Request-Logs zu einem Dienst wie AWS S3 oder Google Pub/Sub zu exportieren, und leite sie dann an ein Tool wie Zapier oder n8n für Telegram-Benachrichtigungen weiter (z.B. stündliche Besucherzusammenfassung). Allerdings nicht in Echtzeit.
- **Integrationen**: Tools wie Albato oder n8n können Cloudflare-Webhooks mit Telegram für umfassendere Ereignisse verbinden, aber nicht pro Besuch.
- **Einschränkungen**: Kostenlose Worker haben 10ms CPU-Zeit pro Anfrage – hierfür ausreichend, aber skaliere bei Bedarf hoch. Vermeide dies auf stark frequentierten Seiten ohne Drosselung.

Dieses Setup verwandelt deinen Cloudflare-Traffic in umsetzbare, sofortige Benachrichtigungen. Wenn du Code-Anpassungen oder Hilfe bei Fehlern benötigst, teile weitere Details mit!

[Cloudflare Workers Docs](https://developers.cloudflare.com/workers/)  
[Telegram Bot API](https://core.telegram.org/bots/api)  
[Cloudflare Instant Logs](https://developers.cloudflare.com/logs/instant-logs/)
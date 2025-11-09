---
audio: false
date: 2025-09-11
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Fehlerbehebung bei leerer LibreChat-Seitenleiste
translated: true
type: note
---

Einige häufige Gründe, warum die Seitenleisten-Chronik in LibreChat intermittierend leer erscheinen kann, obwohl Chatten/Modelle/Provider funktionieren:

Schnellprüfungen in der Benutzeroberfläche
- Filter: Stellen Sie sicher, dass „Alle Konversationen“ ausgewählt ist, kein Ordner ausgewählt ist, „Nur angeheftete“/„Archivierte“ nicht aktiviert ist und das Suchfeld für die Chronik leer ist.
- Konto/Sitzung: Bestätigen Sie, dass Sie noch angemeldet sind (Avatar/Menü zeigt Ihr Konto). Wenn Ihre Sitzung stillschweigend abgelaufen ist, zeigt die App möglicherweise eine frische, leere Chronik an, bis Sie die Seite aktualisieren oder sich erneut anmelden.
- Hard Refresh: Versuchen Sie einen Hard Reload (Strg/Cmd+Umschalt+R). Browser-Cache oder ein veralteter Service Worker können verhindern, dass die Chronikliste nach einem Update aktualisiert wird.

Sitzungs-/Cookie-Probleme
- Inkognito-Modus/strenge Datenschutzeinstellungen oder das Blockieren von Third-Party-Cookies können neue „anonyme“ Sitzungen verursachen, sodass Ihre Chronik „manchmal“ leer aussieht.
- Wenn Ihr Frontend und Ihre API auf verschiedenen Subdomains liegen, stellen Sie sicher, dass Cookies korrekt gesetzt sind (SameSite, Secure, Domain=.example.com) und Sie HTTPS mit einem korrekt konfigurierten Reverse Proxy verwenden. Andernfalls kann die App intermittierend fehlschlagen, Sitzungs-Cookies zu senden, und eine leere Chronik zurückgeben.

Netzwerk-/Backend-Probleme
- Öffnen Sie DevTools → Netzwerk und suchen Sie nach der Anfrage, die Konversationen lädt (z.B. /api/conversations oder /api/history). Prüfen Sie:
  - Statuscode 401/403: Sitzungs- oder Authentifizierungsproblem.
  - 500: Serverfehler (Server-Logs prüfen).
  - 200 mit []: Server hat keine Konversationen zurückgegeben (könnten Filter, falscher Benutzer/Kontext oder DB-Problem sein).
- Prüfen Sie die Server-Logs auf Fehler bei Abfragen zum Abruf von Konversationen oder in der Auth-Middleware.
- Wenn Sie Docker verwenden, stellen Sie sicher, dass Ihr MongoDB-Volume persistent ist; andernfalls können Container-Neustarts die Chronik löschen.

Datenbank/Migration
- Wenn Sie kürzlich von einem älteren Build auf rc3 upgegradet haben, stellen Sie sicher, dass alle erforderlichen DB-Migrationen abgeschlossen sind und die Conversations-Collection Dokumente für Ihren Benutzer enthält.
- Langsame DB oder fehlende Indizes können zu Timeouts führen; die Benutzeroberfläche wird möglicherweise leer gerendert, wenn die Anfrage fehlschlägt.

Bekannte RC-Instabilität
- Es gab Fixes bezüglich des Ladens der Chronik/Seitenleiste über verschiedene rc-Builds hinweg. Wenn Sie v0.8.0-rc3 verwenden, erwägen Sie ein Upgrade auf das neueste stabile 0.8.0+, um einen behobenen Bug auszuschließen.

Wenn Sie Hilfe bei der Eingrenzung benötigen, teilen Sie bitte mit:
- Wie Sie deployen (Docker/nicht-Docker), Version und ob Authentifizierung aktiviert ist
- Browser und ob es nach Leerlauf oder beim Aktualisieren passiert
- Das Ergebnis im Netzwerk-Tab für die Konversations-/Chronik-Anfrage (URL, Statuscode, kurze Antwort)
- Irgendwelche Ausschnitte aus den Server-Logs um die Zeit, wenn die Seitenleiste leer erscheint

Mit diesen Informationen kann ich Sie auf die genaue Ursache und Lösung hinweisen.
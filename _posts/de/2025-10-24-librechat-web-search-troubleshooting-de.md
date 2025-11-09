---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Fehlerbehebung bei der LibreChat-Websuche
translated: true
type: note
---

Lassen Sie das Problem sorgfältig beheben – wenn die **Websuche in LibreChat** nicht funktioniert, selbst nachdem Sie **Firecrawl**, **SerpApi** und **Jina API**-Schlüssel hinzugefügt haben, liegt das Problem fast immer an einem dieser Punkte: Konfigurationsfehler, fehlende Aktivierungs-Flags im Backend oder Fehlinterpretation der Benutzeroberfläche.

Hier ist eine übersichtliche Aufschlüsselung, der Sie folgen können (keine Tabellen, nur Erklärungen):

---

### 1. **Prüfen Sie, ob „Websuche“ in der Backend-Konfiguration aktiviert ist**

Öffnen Sie Ihre LibreChat-Server-Konfigurationsdatei (normalerweise `.env` oder `api/config.yaml`, abhängig von Ihrem Setup) und bestätigen Sie, dass Sie etwa Folgendes haben:

```
# Für .env
SEARCH_ENABLED=true
```

Oder, wenn Sie YAML verwenden:

```yaml
features:
  search: true
```

Wenn `SEARCH_ENABLED` oder `search` nicht explizit auf `true` gesetzt ist, mag der UI-Button erscheinen, führt aber tatsächlich keine Suchvorgänge durch.

---

### 2. **Bestätigen Sie, dass die API-Schlüssel korrekt benannt sind**

Jeder Anbieter erwartet spezifische Namen für die Umgebungsvariablen. Zum Beispiel:

* Für **SerpApi**:

  ```
  SERPAPI_API_KEY=your_key_here
  ```
* Für **Firecrawl**:

  ```
  FIRECRAWL_API_KEY=your_key_here
  ```
* Für **Jina**:

  ```
  JINA_API_KEY=your_key_here
  ```

Stellen Sie auch sicher, dass diese in derselben Umgebung exportiert oder geladen werden, in der der `backend`-Prozess läuft.

So prüfen Sie es:

```bash
echo $SERPAPI_API_KEY
```

Wenn dies leer zurückgibt, sieht Ihr Backend den Schlüssel nicht.

---

### 3. **Starten Sie LibreChat nach dem Bearbeiten der Schlüssel neu**

LibreChat lädt Umgebungsvariablen nicht neu, während es läuft. Führen Sie aus:

```bash
docker compose down
docker compose up -d
```

(oder `npm run start` erneut, wenn Sie Docker nicht verwenden).

---

### 4. **Überprüfen Sie, welchen Suchanbieter LibreChat tatsächlich verwendet**

LibreChat wählt einen standardmäßigen Websuche-Backend abhängig von der Konfigurationsreihenfolge.

Wenn Sie möchten, dass es z.B. SerpApi verwendet, müssen Sie angeben:

```
SEARCH_PROVIDER=serpapi
```

Alternativ, wenn Sie Jina möchten:

```
SEARCH_PROVIDER=jina
```

Wenn Sie nur Schlüssel gesetzt, aber nicht definiert haben, welchen Anbieter verwendet werden soll, könnte LibreChat standardmäßig auf keinen zurückgreifen.

---

### 5. **Sehen Sie sich die Backend-Protokolle an**

Führen Sie aus:

```bash
docker logs librechat-backend
```

oder

```bash
npm run start:debug
```

Suchen Sie nach Meldungen wie:

```
[Search] SerpApi key missing or invalid
```

oder

```
Search provider not configured
```

Das sind die besten Hinweise.

---

### 6. **Testen Sie die APIs direkt**

Um sicherzustellen, dass Ihre Schlüssel tatsächlich funktionieren:

**SerpApi-Test:**

```bash
curl "https://serpapi.com/search.json?q=chatgpt&api_key=YOUR_KEY"
```

**Firecrawl-Test:**

```bash
curl "https://api.firecrawl.dev/v1/search?q=chatgpt" -H "Authorization: Bearer YOUR_KEY"
```

**Jina-Test:**

```bash
curl "https://r.jina.ai/chatgpt" -H "Authorization: Bearer YOUR_KEY"
```

Wenn diese fehlschlagen, sind die Schlüssel selbst ungültig oder ratenbeschränkt.

---

### 7. **Frontend-Versionen-Konflikt**

Wenn Sie LibreChat kürzlich aktualisiert haben (insbesondere von vor v0.7 auf v0.8+), könnte der `Websuche`-Schalter im Frontend existieren, obwohl Ihre Backend-Version das integrierte Firecrawl/Jina-Suchmodul noch nicht unterstützt.
Führen Sie aus:

```bash
git pull
```

und bauen Sie neu:

```bash
docker compose build --no-cache
docker compose up -d
```

---

### 8. **Letzte Prüfung – Bestätigen Sie in der Web-UI**

Öffnen Sie die Benutzeroberfläche, gehen Sie zu **Einstellungen → Funktionen** und bestätigen Sie:

* Der „Websuche“-Schalter ist EIN.
* Ihr ausgewählter Anbieter ist aufgeführt (SerpApi, Firecrawl oder Jina).

Wenn dort *„Kein Anbieter verfügbar“* steht, liest das Backend Ihre Schlüssel nicht.

---

Wenn Sie möchten, können Sie Ihren relevanten `.env`-Ausschnitt (mit maskierten Schlüsseln) einfügen, und ich zeige Ihnen genau, welche Zeile fehlt oder falsch benannt ist.

Möchten Sie mir diesen Ausschnitt zeigen?
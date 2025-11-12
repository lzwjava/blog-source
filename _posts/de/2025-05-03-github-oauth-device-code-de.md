---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: GitHub OAuth Device-Autorisierungsflow
translated: true
type: note
---

### Übersicht

Dieser JavaScript-Code implementiert den OAuth 2.0 Device Authorization Grant Flow (auch bekannt als Device Code Grant), um sich bei GitHub zu authentifizieren und ein Zugriffstoken zu erhalten. Der Flow wird typischerweise für Headless-Anwendungen (z.B. CLI-Tools oder eingebettete Systeme) verwendet, bei denen der Benutzer nicht direkt mit einem Webbrowser interagieren kann, um die Authentifizierung zu genehmigen.

In diesem speziellen Fall scheint er Anfragen des GitHub Copilot-Plugins (z.B. für Neovim oder Vim) nachzuahmen, indem er Header verwendet, die einen Copilot-Client spoofen, um sich potenziell in das Authentifizierungssystem von GitHub zu integrieren oder darauf zuzugreifen. Das Ziel ist es, ein Zugriffstoken zu generieren, das für GitHub-API-Aufrufe verwendet werden könnte, die Benutzerauthentifizierung erfordern, wie das Lesen von Benutzerinformationen (gemäß `scope: "read:user"`).

Der Code läuft als Node.js-Skript, verwendet `fetch` für HTTP-Anfragen und `process` für Umgebungsvariablen. Es wird vorausgesetzt, dass Node.js `fetch` zur Verfügung stellt (wie in neueren Versionen oder via Polyfill). Bei Erfolg pollt er die GitHub-Server, bis der Benutzer die Anfrage autorisiert oder ein Timeout auftritt.

**Wichtige Hinweise:**
- Dieser Code erfordert das Setzen einer Umgebungsvariable `MY_COPILOT_CLIENT_ID`, wahrscheinlich eine GitHub OAuth App Client ID, die für GitHub Copilot registriert ist.
- Fehler werden minimal behandelt – z.B. wenn ein Fetch fehlschlägt, wird es geloggt und fortgefahren oder beendet.
- Aus Sicherheitssicht ist das Speichern oder Loggen von Zugriffstokens riskant (sie gewähren API-Zugriff). Dieser Code gibt das vollständige Token-Objekt direkt auf der Konsole aus, was in der echten Nutzung ein Datenschutz-/Sicherheitsproblem darstellen könnte. Zugriffstokens sollten sicher gehandhabt werden (z.B. verschlüsselt gespeichert und rotiert).
- Der Flow beinhaltet Benutzerinteraktion: Der Benutzer muss eine URL besuchen und einen Code auf der GitHub-Website eingeben, um zu autorisieren.
- Dies ist kein "offizieller" GitHub-Dokumentationscode; er scheint aus dem Verhalten von GitHub Copilot reverse-engineered zu sein. APIs verantwortungsvoll und gemäß den GitHub-Nutzungsbedingungen verwenden.

### Schritt-für-Schritt Aufschlüsselung

#### 1. Umgebungsprüfung
```javascript
const clientId = process.env.MY_COPILOT_CLIENT_ID;

if (!clientId) {
  console.error("MY_COPILOT_CLIENT_ID ist nicht gesetzt");
  process.exit(1);
}
```
- Holt die `MY_COPILOT_CLIENT_ID` aus den Umgebungsvariablen (z.B. gesetzt via `export MY_COPILOT_CLIENT_ID=your_client_id` in Ihrer Shell).
- Wenn nicht gesetzt, wird ein Fehler geloggt und das Skript beendet (Prozesscode 1 zeigt einen Fehler an).
- Diese Client-ID stammt von einer registrierten GitHub OAuth App (erforderlich für OAuth-Flows).

#### 2. Einrichten gemeinsamer Header
```javascript
const commonHeaders = new Headers();
commonHeaders.append("accept", "application/json");
commonHeaders.append("editor-version", "Neovim/0.6.1");
commonHeaders.append("editor-plugin-version", "copilot.vim/1.16.0");
commonHeaders.append("content-type", "application/json");
commonHeaders.append("user-agent", "GithubCopilot/1.155.0");
commonHeaders.append("accept-encoding", "gzip,deflate,b");
```
- Erstellt ein `Headers`-Objekt mit Schlüssel-Wert-Paaren für HTTP-Anfragen.
- Diese Header lassen die Anfragen so aussehen, als kämen sie vom GitHub Copilot Vim-Plugin (Version 1.16.0 für Neovim 0.6.1). Dies dient wahrscheinlich dazu, den User-Agent zu spoofen und die API-Aufrufe von Copilot nachzuahmen, was möglicherweise erforderlich oder hilfreich ist, damit GitHub die Anfragen akzeptiert.
- `"accept": "application/json"`: Erwartet JSON-Antworten.
- `"content-type": "application/json"`: Sendet JSON in den Anfrage-Bodies.
- `"accept-encoding"`: Erlaubt Gzip/Deflate-Kompression, um Bandbreite zu sparen.

#### 3. `getDeviceCode()` Funktion
```javascript
async function getDeviceCode() {
  const raw = JSON.stringify({
    "client_id": clientId,
    "scope": "read:user",
  });

  const requestOptions = {
    method: "POST",
    headers: commonHeaders,
    body: raw,
  };

  const data = await fetch(
    "https://github.com/login/device/code",
    requestOptions,
  )
    .then((response) => response.json())
    .catch((error) => console.error(error));
  return data;
}
```
- **Zweck**: Initiiert den Device Code Flow, indem ein Device Code von GitHub angefordert wird.
- Konstruiert eine JSON-Nutzlast mit:
  - `client_id`: Die OAuth Client-ID (zur Authentifizierung Ihrer App).
  - `scope`: `"read:user"` – beschränkt das Token auf das Lesen grundlegender Benutzerprofilinformationen (z.B. Benutzername, E-Mail via GitHub API). Dies ist ein minimaler Scope.
- Stellt eine POST-Anfrage an `https://github.com/login/device/code` (GitHub's OAuth Device Code Endpoint).
- Parst die JSON-Antwort (erwartete Felder: `device_code`, `user_code`, `verification_uri`, `expires_in` – nicht im Code gezeigt, aber Standard für diesen Flow).
- Bei einem Fehler (z.B. Netzwerkprobleme) wird dieser geloggt, aber fortgefahren (könnte `undefined` zurückgeben).
- Gibt das geparste JSON-Datenobjekt von GitHub zurück.

#### 4. `getAccessToken(deviceCode: string)` Funktion
```javascript
async function getAccessToken(deviceCode: string) {
  const raw = JSON.stringify({
    "client_id": clientId,
    "device_code": deviceCode,
    "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
  });

  const requestOptions = {
    method: "POST",
    headers: commonHeaders,
    body: raw,
  };

  return await fetch(
    "https://github.com/login/oauth/access_token",
    requestOptions,
  )
    .then((response) => response.json())
    .catch((error) => console.error(error));
}
```
- **Zweck**: Pollt GitHub, um den Device Code gegen ein Zugriffstoken auszutauschen, sobald der Benutzer es autorisiert hat.
- Nimmt den `device_code` aus dem vorherigen Schritt.
- Konstruiert JSON mit:
  - `client_id`: Wie zuvor.
  - `device_code`: Der eindeutige Code, der diesen Device/Auth-Versuch identifiziert.
  - `grant_type`: Spezifiziert, dass es sich um einen Device Code Grant handelt (Standard OAuth2 URN).
- Stellt eine POST-Anfrage an `https://github.com/login/oauth/access_token`.
- Gibt die geparste JSON-Antwort zurück, die sein könnte:
  - Bei Erfolg: `{ access_token: "...", token_type: "bearer", scope: "read:user" }`.
  - Bei Ausstehend/Fehler: `{ error: "...", error_description: "..." }` (z.B. "authorization_pending" oder "slow_down").
- Fehler (z.B. Fetch-Fehler) werden geloggt, aber nicht explizit behandelt, daher muss der Aufrufer den Rückgabewert prüfen.

#### 5. Hauptausführung (Sofort aufgerufene Async-Funktion)
```javascript
(async function () {
  const { device_code, user_code, verification_uri, expires_in } =
    await getDeviceCode();
  console.info(`Benutzercode eingeben:\n${user_code}\n${verification_uri}`);
  console.info(`Läuft ab in ${expires_in} Sekunden`);
  while (true) {
    await new Promise((resolve) => setTimeout(resolve, 5000));
    const accessToken = await getAccessToken(device_code);
    if (accessToken.error) {
      console.info(`${accessToken.error}: ${accessToken.error_description}`);
    }
    if (accessToken.access_token) {
      console.info(`Zugriffstoken:\n${JSON.stringify(accessToken, null, 1)}`);
      break;
    }
  }
})();
```
- **Gesamtfluss**: Orchestriert den vollständigen OAuth 2.0 Device Code Grant.
- Ruft `getDeviceCode()` auf und destructured die Antwort in Variablen (geht von Erfolg und Vorhandensein dieser Eigenschaften aus).
- Loggt Anweisungen für den Benutzer:
  - `user_code`: Ein kurzer alphanumerischer Code (z.B. "ABCD-EFGH").
  - `verification_uri`: Normalerweise `https://github.com/login/device`, wo sich der Benutzer authentifiziert.
  - `expires_in`: Zeit in Sekunden, bis der Code abläuft (z.B. 900 für 15 Minuten).
- Der Benutzer muss die URL besuchen, sich bei GitHub anmelden und den Benutzercode eingeben, um die App zu autorisieren.
- Tritt in eine Endlosschleife ein, um auf das Token zu pollen:
  - Wartet 5 Sekunden zwischen den Versuchen (Polling-Intervall; GitHub empfiehlt slow_down bei zu häufigen Anfragen).
  - Ruft `getAccessToken(device_code)` auf.
  - Wenn die Antwort einen `error` hat: Loggt ihn (z.B. weiter warten bei "authorization_pending").
  - Wenn sie ein `access_token` hat: Loggt das vollständige Token-Objekt (formatiert mit Einrückung) und bricht die Schleife ab.
- **Randfälle/Probleme**:
  - Wenn `getDeviceCode()` fehlschlägt, könnte das Destructuring fehlschlagen (Code prüft dies nicht).
  - Kein Schleifen-Timeout – pollt unbegrenzt weiter, es sei denn, das Zugriffstoken wird empfangen oder das Skript stürzt ab.
  - Das Loggen des Zugriffstokens auf der Konsole legt es offen; in der Produktion sollte man es sicher speichern (z.B. in einer Datei oder Datenbank).

### Wie es End-to-End funktioniert
1.  **Schritt 1: Device Code anfordern** → Skript holt einen temporären Code von GitHub.
2.  **Schritt 2: Benutzerautorisierung** → Benutzer besucht GitHub und gibt den Code ein, um die Berechtigung zu erteilen.
3.  **Schritt 3: Auf Token pollen** → Skript fragt GitHub weiter, bis das Token ausgestellt wird.
4.  **Ergebnis**: Ein Zugriffstoken für den angegebenen Scope (z.B. Benutzerdaten via GitHub API lesen).

Dies ist eine Simulation davon, wie Tools wie die GitHub CLI funktionieren könnten, angepasst für Copilot. Für offizielle GitHub OAuth-Dokumentation siehe https://docs.github.com/en/developers/apps/building-oauth-apps/authorizing-oauth-apps#device-flow. Wenn Sie etwas Ähnliches bauen, stellen Sie die Einhaltung der OAuth-Standards und der GitHub-Richtlinien sicher. Wenn Sie Fragen zur Modifikation oder Ausführung haben, lassen Sie es mich wissen!
---
audio: false
generated: true
lang: de
layout: post
title: Funktionen in der Kong Insomnia GUI verwenden
translated: true
type: note
---

Kong Insomnia bietet eine robuste grafische Benutzeroberfläche (GUI), um die API-Entwicklung zu vereinfachen. Nachfolgend finden Sie eine detaillierte Anleitung zur Verwendung von **Params**, **Body**, **Auth**, **Cookies**, **Certificates**, **Settings** und **Proxy** innerhalb der Insomnia GUI.

---

#### 1. **Params (Abfrageparameter)**
Abfrageparameter werden verwendet, um Daten an die URL anzuhängen, typischerweise für GET-Anfragen.

- **Verwendung**:
  - Öffnen Sie den **Debug-Tab** und wählen Sie eine Anfrage aus oder erstellen Sie eine (z.B. GET).
  - Klicken Sie neben dem URL-Feld auf den Tab **Query**.
  - Fügen Sie Schlüssel-Wert-Paare für Ihre Abfrageparameter hinzu. Wenn Sie z.B. `key` als "id" und `value` als "123" eingeben, wird `?id=123` an Ihre URL angehängt.
  - Um Umgebungsvariablen zu verwenden, tippen Sie `{{variableName}}` in das Wertfeld (z.B. `{{userId}}`).
  - Aktivieren oder deaktivieren Sie bestimmte Parameter durch Umschalten der Checkbox neben jedem Paar.

- **Beispiel**:
  Für eine URL wie `https://api.example.com/users?id=123` fügen Sie hinzu:
  - Key: `id`
  - Value: `123`
  Insomnia formatiert die URL automatisch mit der Abfragezeichenkette.

---

#### 2. **Body**
Der Body wird verwendet, um Daten mit Anfragen wie POST oder PUT zu senden.

- **Verwendung**:
  - Wählen Sie im **Debug-Tab** eine Anfrage aus (z.B. POST oder PUT).
  - Wechseln Sie zum **Body**-Tab unterhalb des URL-Feldes.
  - Wählen Sie einen Body-Typ aus dem Dropdown-Menü:
    - **JSON**: Geben Sie JSON-Daten ein (z.B. `{"name": "John", "age": 30}`).
    - **Form URL-Encoded**: Fügen Sie Schlüssel-Wert-Paare hinzu, ähnlich wie bei Abfrageparametern.
    - **Multipart Form**: Fügen Sie Felder hinzu oder laden Sie Dateien für Formulare mit Dateianhängen hoch.
    - **Raw**: Geben Sie Klartext oder andere Formate ein (z.B. XML).
  - Verwenden Sie Umgebungsvariablen, indem Sie `{{variableName}}` im Body-Inhalt eingeben.

- **Beispiel**:
  Für eine POST-Anfrage, die JSON sendet:
  - Wählen Sie **JSON** aus dem Dropdown-Menü.
  - Geben Sie ein: `{"name": "John", "age": "{{userAge}}"}`.
  Insomnia setzt den `Content-Type`-Header automatisch auf `application/json`.

---

#### 3. **Auth (Authentifizierung)**
Authentifizierungseinstellungen ermöglichen es Ihnen, Anmeldedaten oder Token in Ihre Anfragen aufzunehmen.

- **Verwendung**:
  - Wählen Sie im **Debug-Tab** Ihre Anfrage aus.
  - Gehen Sie zum **Auth**-Tab.
  - Wählen Sie einen Authentifizierungstyp aus dem Dropdown-Menü:
    - **Basic Auth**: Geben Sie einen Benutzernamen und ein Passwort ein.
    - **Bearer Token**: Fügen Sie Ihr Token ein (z.B. ein JWT).
    - **OAuth 2.0**: Konfigurieren Sie Client-ID, Secret und andere Details für OAuth-Flows.
    - **API Key**: Fügen Sie ein Schlüssel-Wert-Paar hinzu (z.B. Key: `Authorization`, Value: `your-api-key`).
  - Insomnia fügt die Authentifizierungsdetails automatisch zu den Request-Headern hinzu.

- **Beispiel**:
  Für einen Bearer Token:
  - Wählen Sie **Bearer Token**.
  - Fügen Sie Ihr Token ein (z.B. `abc123xyz`).
  Der Request-Header enthält: `Authorization: Bearer abc123xyz`.

---

#### 4. **Cookies**
Cookies werden automatisch verwaltet, können aber manuell eingesehen oder bearbeitet werden.

- **Verwendung**:
  - Insomnia speichert von Serverantworten empfangene Cookies pro Workspace.
  - So verwalten Sie Cookies:
    - Gehen Sie zu **Preferences** (Strg + , oder Cmd + , auf macOS).
    - Navigieren Sie zu **Data** > **Cookie Jar**.
    - Sehen Sie Cookies ein, bearbeiten oder löschen Sie sie nach Bedarf.
  - Cookies bleiben über Anfragen im selben Workspace hinweg bestehen und werden automatisch mit nachfolgenden Anfragen mitgesendet.

- **Tipp**:
  Wenn Sie mit bestimmten Cookies testen müssen, fügen Sie diese manuell im **Cookie Jar** für die entsprechende Domain hinzu.

---

#### 5. **Certificates**
Client-Zertifikate werden für HTTPS-Anfragen verwendet, die gegenseitige TLS-Authentifizierung erfordern.

- **Verwendung**:
  - Gehen Sie zu **Preferences** (Strg + , oder Cmd + ,).
  - Wählen Sie den Abschnitt **Certificates**.
  - Klicken Sie auf **Add Certificate**:
    - Stellen Sie die Zertifikatsdatei bereit (z.B. `.pem`, `.crt`).
    - Fügen Sie die Private-Key-Datei und optional eine Passphrase hinzu, falls erforderlich.
    - Ordnen Sie das Zertifikat bestimmten Hosts zu (z.B. `api.example.com`).
  - Insomnia verwendet das Zertifikat für Anfragen an die angegebenen Hosts.

- **Beispiel**:
  Für `api.example.com`, das ein Zertifikat erfordert:
  - Laden Sie `client.crt` und `client.key` hoch.
  - Setzen Sie Host auf `api.example.com`.
  Anfragen an diese Domain enthalten das Zertifikat.

---

#### 6. **Settings**
Einstellungen ermöglichen es Ihnen, das Verhalten von Insomnia anzupassen.

- **Verwendung**:
  - Zugriff über **Preferences** (Strg + , oder Cmd + ,).
  - Wichtige Optionen umfassen:
    - **Theme**: Wechseln Sie zwischen Hell, Dunkel oder Systemstandard.
    - **Proxy**: Konfigurieren Sie Proxy-Einstellungen (siehe unten).
    - **Plugins**: Installieren Sie zusätzliche Funktionalität (z.B. benutzerdefinierte Response-Formatter).
    - **Data**: Verwalten Sie den Local Vault für die sichere Speicherung sensibler Daten wie API-Schlüssel.

- **Tipp**:
  Verwenden Sie den **Local Vault**, um sensible Werte (z.B. Tokens) sicher zu speichern, anstatt sie fest zu kodieren.

---

#### 7. **Proxy**
Proxies leiten Ihre Anfragen über einen bestimmten Server, was für Debugging oder Unternehmensnetzwerke nützlich ist.

- **Verwendung**:
  - Gehen Sie zu **Preferences** > **Proxy**.
  - Aktivieren Sie den Proxy und geben Sie die Details des Proxy-Servers ein (z.B. `http://proxy.example.com:8080`).
  - Für die globale Verwendung speichern Sie ihn hier.
  - Für Proxy pro Anfrage:
    - Klicken Sie auf das Zahnradsymbol neben dem Anfragenamen im **Debug-Tab**.
    - Überschreiben Sie die Proxy-Einstellungen in der anfragespezifischen Konfiguration.

- **Beispiel**:
  Um Anfragen über einen Corporate Proxy zu leiten:
  - Aktivieren Sie den Proxy in **Preferences**.
  - Setzen Sie die Proxy-URL auf `http://proxy.example.com:8080`.
  Alle Anfragen verwenden nun diesen Proxy, sofern nicht überschrieben.

---

### Zusammenfassung
Hier ist eine kurze Zusammenfassung zur Verwendung dieser Funktionen in der Insomnia GUI:
- **Params**: Fügen Sie Abfrageparameter im **Query**-Tab für GET-Anfragen hinzu.
- **Body**: Senden Sie Daten mit POST/PUT-Anfragen über den **Body**-Tab, wählen Sie das Format.
- **Auth**: Richten Sie Authentifizierung im **Auth**-Tab für sichere Anfragen ein.
- **Cookies**: Verwalten Sie Cookies unter **Preferences** > **Cookie Jar**.
- **Certificates**: Fügen Sie Client-Zertifikate unter **Preferences** > **Certificates** für HTTPS hinzu.
- **Settings**: Passen Sie Insomnia in **Preferences** an (Themes, Plugins, etc.).
- **Proxy**: Konfigurieren Sie Proxies in **Preferences** oder pro Anfrage.

Indem Sie diese Funktionen nutzen, können Sie APIs in Kong Insomnia effizient testen und debuggen. Experimentieren Sie mit jedem Abschnitt, um Ihren Workflow anzupassen!
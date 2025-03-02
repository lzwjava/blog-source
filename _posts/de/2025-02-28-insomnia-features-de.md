---
audio: false
generated: false
lang: de
layout: post
title: Funktionen in der Kong Insomnia GUI verwenden
translated: true
---

Kong Insomnia bietet eine robuste grafische Benutzeroberfläche (GUI), um die API-Entwicklung zu vereinfachen. Im Folgenden finden Sie eine detaillierte Anleitung zur Verwendung von **params**, **body**, **auth**, **cookies**, **certificates**, **settings** und **proxy** innerhalb der Insomnia-GUI.

---

#### 1. **Params (Abfrageparameter)**
Abfrageparameter werden verwendet, um Daten an die URL anzuhängen, in der Regel für GET-Anfragen.

- **Verwendung**:
  - Öffnen Sie die **Debug**-Registerkarte und wählen Sie eine Anfrage aus oder erstellen Sie eine neue (z. B. GET).
  - Neben dem URL-Feld klicken Sie auf die Registerkarte **Query**.
  - Fügen Sie Schlüssel-Wert-Paare für Ihre Abfrageparameter hinzu. Zum Beispiel, indem Sie `key` als "id" und `value` als "123" eingeben, wird `?id=123` an Ihre URL angehängt.
  - Um Umgebungsvariablen zu verwenden, geben Sie `{{variableName}}` im Wertfeld ein (z. B. `{{userId}}`).
  - Aktivieren oder deaktivieren Sie spezifische Parameter, indem Sie das Kontrollkästchen neben jedem Paar umschalten.

- **Beispiel**:
  Für eine URL wie `https://api.example.com/users?id=123`, fügen Sie hinzu:
  - Schlüssel: `id`
  - Wert: `123`
  Insomnia formatiert die URL automatisch mit der Abfragezeichenfolge.

---

#### 2. **Body**
Der Body wird verwendet, um Daten mit Anfragen wie POST oder PUT zu senden.

- **Verwendung**:
  - In der **Debug**-Registerkarte wählen Sie eine Anfrage aus (z. B. POST oder PUT).
  - Wechseln Sie zur Registerkarte **Body** unterhalb des URL-Feldes.
  - Wählen Sie einen Body-Typ aus der Dropdown-Liste aus:
    - **JSON**: Geben Sie JSON-Daten ein (z. B. `{"name": "John", "age": 30}`).
    - **Form URL-Encoded**: Fügen Sie Schlüssel-Wert-Paare hinzu, ähnlich wie Abfrageparameter.
    - **Multipart Form**: Fügen Sie Felder hinzu oder laden Sie Dateien für Formulare mit Dateianhängen hoch.
    - **Raw**: Geben Sie einfachen Text oder andere Formate ein (z. B. XML).
  - Verwenden Sie Umgebungsvariablen, indem Sie `{{variableName}}` innerhalb des Body-Inhalts eingeben.

- **Beispiel**:
  Für eine POST-Anfrage, die JSON sendet:
  - Wählen Sie **JSON** aus der Dropdown-Liste aus.
  - Geben Sie ein: `{"name": "John", "age": "{{userAge}}"}`.
  Insomnia setzt den `Content-Type`-Header automatisch auf `application/json`.

---

#### 3. **Auth (Authentifizierung)**
Authentifizierungseinstellungen ermöglichen es Ihnen, Anmeldeinformationen oder Tokens in Ihren Anfragen zu enthalten.

- **Verwendung**:
  - In der **Debug**-Registerkarte wählen Sie Ihre Anfrage aus.
  - Gehen Sie zur Registerkarte **Auth**.
  - Wählen Sie einen Authentifizierungstyp aus der Dropdown-Liste aus:
    - **Basic Auth**: Geben Sie einen Benutzernamen und ein Passwort ein.
    - **Bearer Token**: Fügen Sie Ihren Token ein (z. B. ein JWT).
    - **OAuth 2.0**: Konfigurieren Sie Client-ID, Geheimnis und andere Details für OAuth-Flüsse.
    - **API Key**: Fügen Sie ein Schlüssel-Wert-Paar hinzu (z. B. Schlüssel: `Authorization`, Wert: `your-api-key`).
  - Insomnia fügt die Authentifizierungsdetails automatisch den Anfrage-Headern hinzu.

- **Beispiel**:
  Für einen Bearer Token:
  - Wählen Sie **Bearer Token**.
  - Fügen Sie Ihren Token ein (z. B. `abc123xyz`).
  Der Anfrage-Header enthält: `Authorization: Bearer abc123xyz`.

---

#### 4. **Cookies**
Cookies werden automatisch verwaltet, können jedoch manuell angesehen oder bearbeitet werden.

- **Verwendung**:
  - Insomnia speichert Cookies, die von Serverantworten empfangen werden, pro Arbeitsbereich.
  - Um Cookies zu verwalten:
    - Gehen Sie zu **Preferences** (Strg + , oder Cmd + , auf macOS).
    - Navigieren Sie zu **Data** > **Cookie Jar**.
    - Sehen Sie sich Cookies an, bearbeiten oder löschen Sie diese nach Bedarf.
  - Cookies bleiben über Anfragen im gleichen Arbeitsbereich bestehen und werden automatisch mit nachfolgenden Anfragen gesendet.

- **Tipp**:
  Wenn Sie mit bestimmten Cookies testen müssen, fügen Sie diese manuell im **Cookie Jar** für die relevante Domain hinzu.

---

#### 5. **Certificates**
Client-Zertifikate werden für HTTPS-Anfragen verwendet, die eine gegenseitige TLS-Authentifizierung erfordern.

- **Verwendung**:
  - Gehen Sie zu **Preferences** (Strg + , oder Cmd + ,).
  - Wählen Sie den Abschnitt **Certificates** aus.
  - Klicken Sie auf **Add Certificate**:
    - Geben Sie die Zertifikatsdatei an (z. B. `.pem`, `.crt`).
    - Fügen Sie die private Schlüsseldatei und eine optionale Passphrase hinzu, falls erforderlich.
    - Verbinden Sie das Zertifikat mit bestimmten Hosts (z. B. `api.example.com`).
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
  - Wichtige Optionen sind:
    - **Theme**: Wechseln Sie zwischen hell, dunkel oder Systemstandard.
    - **Proxy**: Konfigurieren Sie Proxy-Einstellungen (siehe unten).
    - **Plugins**: Installieren Sie zusätzliche Funktionen (z. B. benutzerdefinierte Antwortformatierer).
    - **Data**: Verwalten Sie Local Vault für die sichere Speicherung sensibler Daten wie API-Schlüssel.

- **Tipp**:
  Verwenden Sie den **Local Vault**, um sensible Werte (z. B. Tokens) sicher zu speichern, anstatt sie hart zu codieren.

---

#### 7. **Proxy**
Proxys leiten Ihre Anfragen über einen angegebenen Server, was nützlich für das Debuggen oder Unternehmensnetzwerke ist.

- **Verwendung**:
  - Gehen Sie zu **Preferences** > **Proxy**.
  - Aktivieren Sie den Proxy und geben Sie die Proxy-Serverdetails ein (z. B. `http://proxy.example.com:8080`).
  - Für die globale Verwendung speichern Sie es hier.
  - Für einen pro-Anfrage-Proxy:
    - Klicken Sie auf das Zahnradsymbol neben dem Anfragenamen in der **Debug**-Registerkarte.
    - Überschreiben Sie die Proxy-Einstellungen in der anfragespezifischen Konfiguration.

- **Beispiel**:
  Um Anfragen über einen Unternehmensproxy zu leiten:
  - Aktivieren Sie den Proxy in **Preferences**.
  - Setzen Sie Proxy-URL auf `http://proxy.example.com:8080`.
  Alle Anfragen verwenden jetzt diesen Proxy, es sei denn, sie werden überschrieben.

---

### Zusammenfassung
Hier ist eine kurze Zusammenfassung, wie diese Funktionen in der Insomnia-GUI verwendet werden:
- **Params**: Fügen Sie Abfrageparameter in der **Query**-Registerkarte für GET-Anfragen hinzu.
- **Body**: Senden Sie Daten mit POST/PUT-Anfragen über die **Body**-Registerkarte, wobei das Format ausgewählt wird.
- **Auth**: Richten Sie die Authentifizierung in der **Auth**-Registerkarte für sichere Anfragen ein.
- **Cookies**: Verwalten Sie Cookies in **Preferences** > **Cookie Jar**.
- **Certificates**: Fügen Sie Client-Zertifikate in **Preferences** > **Certificates** für HTTPS hinzu.
- **Settings**: Passen Sie Insomnia in **Preferences** an (Themen, Plugins usw.).
- **Proxy**: Konfigurieren Sie Proxys in **Preferences** oder pro Anfrage.

Durch die Nutzung dieser Funktionen können Sie APIs in Kong Insomnia effizient testen und debuggen. Experimentieren Sie mit jedem Abschnitt, um Ihren Workflow anzupassen!
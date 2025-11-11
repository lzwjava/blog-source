---
audio: false
generated: true
lang: de
layout: post
title: Testen des NPM-Registrierungsdienstes mit reinen HTTP-Anfragen
translated: true
type: note
---

Um Ihre NPM-Registry mit rohen HTTP-Anfragen über Tools wie `curl` oder Insomnia zu testen, können Sie deren Funktionalität überprüfen, indem Sie die Konnektivität, Authentifizierung und die Fähigkeit, Paketdaten bereitzustellen, testen – alles ohne Abhängigkeit vom NPM-Client. Da Ihre Registry einen Benutzernamen und ein Passwort erfordert, müssen Sie die Authentifizierung manuell in Ihren Anfragen handhaben. Nachfolgend finden Sie eine vollständige Anleitung zum Testen Ihrer Registry mit rohen HTTP-Anfragen, unter der Annahme, dass es sich um eine NPM-kompatible Registry (z. B. Verdaccio, Nexus oder eine eigene Implementierung) handelt, die tokenbasierte oder Basic-Authentifizierung unterstützt.

---

## Schritte zum Testen der Registry mit rohen HTTP-Anfragen

### 1. Authentifizieren und Token abrufen (falls erforderlich)

Die meisten NPM-Registries verwenden tokenbasierte Authentifizierung, bei der Sie sich zunächst anmelden müssen, um ein Token für weitere Anfragen zu erhalten. Einige Registries unterstützen möglicherweise auch direkt die Basic-Authentifizierung. So authentifizieren Sie sich mit `curl`:

#### Anmeldung mit `curl`
Senden Sie eine PUT-Anfrage an den Authentifizierungs-Endpoint der Registry, um ein Token zu erhalten:

```bash
curl -X PUT \
  -H "Content-Type: application/json" \
  -d '{"name": "<Benutzername>", "password": "<Passwort>"}' \
  <Registry-URL>/-/user/org.couchdb.user:<Benutzername>
```

- **Ersetzen Sie**:
  - `<Benutzername>`: Ihr Registry-Benutzername.
  - `<Passwort>`: Ihr Registry-Passwort.
  - `<Registry-URL>`: Die vollständige URL Ihrer Registry (z. B. `https://meine-registry.example.com`).
- **Erwartete Antwort**: Bei Erfolg erhalten Sie eine JSON-Antwort mit einem Token:
  ```json
  {
    "token": "Ihr-Authentifizierungs-Token"
  }
  ```
- **Token speichern**: Kopieren Sie den Wert `Ihr-Authentifizierungs-Token` für die Verwendung in nachfolgenden Anfragen.

**Hinweis**: Wenn Ihre Registry einen anderen Authentifizierungs-Endpoint oder eine andere Methode verwendet (z. B. Basic Auth oder eine benutzerdefinierte API), konsultieren Sie deren Dokumentation. Wenn sie Basic Auth direkt unterstützt, können Sie diesen Schritt überspringen und in späteren Anfragen stattdessen `-u "<Benutzername>:<Passwort>"` verwenden.

---

### 2. Die Registry anpingen

Testen Sie die grundlegende Konnektivität zur Registry, indem Sie eine GET-Anfrage an ihre Stamm-URL oder einen Ping-Endpoint senden.

#### Ping mit `curl`
```bash
curl -H "Authorization: Bearer Ihr-Authentifizierungs-Token" <Registry-URL>
```

- **Ersetzen Sie**:
  - `Ihr-Authentifizierungs-Token`: Das Token aus Schritt 1.
  - `<Registry-URL>`: Ihre Registry-URL.
- **Erwartete Antwort**: Eine erfolgreiche Antwort (HTTP 200) könnte die Homepage der Registry oder eine einfache Statusmeldung zurückgeben (z. B. `{"db_name":"registry"}` für CouchDB-basierte Registries).
- **Alternative**: Einige Registries bieten einen `/-/ping`-Endpoint an:
  ```bash
  curl -H "Authorization: Bearer Ihr-Authentifizierungs-Token" <Registry-URL>/-/ping
  ```

**Bei Verwendung von Basic Auth**: Falls Ihre Registry keine Tokens verwendet und Basic-Authentifizierung unterstützt:
```bash
curl -u "<Benutzername>:<Passwort>" <Registry-URL>
```

---

### 3. Paket-Metadaten abrufen

Überprüfen Sie, ob die Registry Paket-Metadaten bereitstellen kann, indem Sie Details für ein bestimmtes Paket anfordern.

#### Metadaten abrufen mit `curl`
```bash
curl -H "Authorization: Bearer Ihr-Authentifizierungs-Token" <Registry-URL>/<Paket-Name>
```

- **Ersetzen Sie**:
  - `<Paket-Name>`: Ein Paket, von dem Sie wissen, dass es in Ihrer Registry existiert (z. B. `lodash`, wenn es die öffentliche Registry proxied, oder ein privates Paket wie `meine-org-utils`).
- **Erwartete Antwort**: Ein JSON-Objekt mit den Metadaten des Pakets, einschließlich Versionen, Abhängigkeiten und Tarball-URLs. Zum Beispiel:
  ```json
  {
    "name": "lodash",
    "versions": {
      "4.17.21": {
        "dist": {
          "tarball": "<Registry-URL>/lodash/-/lodash-4.17.21.tgz"
        }
      }
    }
  }
  ```

**Bei Verwendung von Basic Auth**:
```bash
curl -u "<Benutzername>:<Passwort>" <Registry-URL>/<Paket-Name>
```

- **Erfolg**: Eine 200 OK-Antwort mit Metadaten bestätigt, dass die Registry Paketdaten korrekt bereitstellt.

---

### 4. Ein Paket-Tarball herunterladen (Optional)

Um die Registry vollständig zu testen, laden Sie einen Paket-Tarball herunter, um sicherzustellen, dass sie die eigentlichen Paketdateien liefern kann.

#### Tarball herunterladen mit `curl`
1. Suchen Sie in den Metadaten aus Schritt 3 die `tarball`-URL für eine bestimmte Version (z. B. `<Registry-URL>/lodash/-/lodash-4.17.21.tgz`).
2. Laden Sie sie herunter:
```bash
curl -H "Authorization: Bearer Ihr-Authentifizierungs-Token" -O <Tarball-URL>
```

- **Ersetzen Sie**: `<Tarball-URL>` mit der URL aus den Metadaten.
- **`-O`-Flag**: Speichert die Datei unter ihrem ursprünglichen Namen (z. B. `lodash-4.17.21.tgz`).
- **Bei Verwendung von Basic Auth**:
  ```bash
  curl -u "<Benutzername>:<Passwort>" -O <Tarball-URL>
  ```
- **Erfolg**: Die Datei wird erfolgreich heruntergeladen, und Sie können ihren Inhalt extrahieren (z. B. mit `tar -xzf <Dateiname>`), um ihn zu überprüfen.

---

## Testen mit Insomnia

Wenn Sie ein GUI-Tool wie Insomnia bevorzugen, befolgen Sie diese Schritte:

### 1. Authentifizierung einrichten
- Erstellen Sie eine neue Anfrage in Insomnia.
- Gehen Sie zum Tab **Auth**:
  - **Bearer Token**: Wenn Sie in Schritt 1 ein Token erhalten haben, wählen Sie "Bearer Token" und fügen Sie `Ihr-Authentifizierungs-Token` ein.
  - **Basic Auth**: Wenn die Registry Basic Auth verwendet, wählen Sie "Basic Auth" und geben Sie Ihren `<Benutzername>` und `<Passwort>` ein.

### 2. Die Registry anpingen
- **Methode**: GET
- **URL**: `<Registry-URL>` oder `<Registry-URL>/-/ping`
- Klicken Sie auf **Send**.
- **Erwartete Antwort**: Ein 200 OK-Status mit einem einfachen Antwortbody.

### 3. Paket-Metadaten abrufen
- **Methode**: GET
- **URL**: `<Registry-URL>/<Paket-Name>`
- Stellen Sie sicher, dass die Authentifizierung im Auth-Tab eingestellt ist.
- Klicken Sie auf **Send**.
- **Erwartete Antwort**: Ein 200 OK-Status mit Paket-Metadaten im JSON-Format.

### 4. Einen Tarball herunterladen
- **Methode**: GET
- **URL**: Die Tarball-URL aus den Metadaten (z. B. `<Registry-URL>/<Paket-Name>/-/<Paket-Name>-<Version>.tgz`).
- Klicken Sie auf **Send and Download**, um die Datei lokal zu speichern.
- **Erfolg**: Die Datei wird heruntergeladen, was bestätigt, dass die Registry Pakete bereitstellt.

---

## Problembehandlung

- **401 Unauthorized**:
  - Überprüfen Sie Ihr Token oder Ihre Anmeldedaten.
  - Stellen Sie sicher, dass der `Authorization`-Header oder die Basic-Authentifizierung korrekt formatiert ist.
- **404 Not Found**:
  - Vergewissern Sie sich, dass das Paket in der Registry existiert.
  - Wenn Sie öffentliche Pakete testen (z. B. `lodash`), bestätigen Sie, dass die Registry die öffentliche NPM-Registry proxied.
- **Verbindungsfehler**:
  - Überprüfen Sie die `<Registry-URL>` erneut (z. B. schließen Sie `https://` ein, falls erforderlich).
  - Für HTTPS-Registries: Wenn Sie SSL-Fehler mit `curl` erhalten, fügen Sie `-k` hinzu, um Zertifikatsprüfungen zu umgehen (nur für Tests).
- **Benutzerdefiniertes Registry-Verhalten**:
  - Wenn diese Schritte fehlschlagen, konsultieren Sie die Dokumentation Ihrer Registry für spezifische Endpoints oder Authentifizierungsmethoden.

---

## Schlussfolgerung

Indem Sie diese Schritte mit `curl` oder Insomnia befolgen, können Sie die Konnektivität, Authentifizierung und Paket-Bereitstellungsfähigkeiten Ihrer NPM-Registry mit rohen HTTP-Anfragen testen. Beginnen Sie mit der Authentifizierung (falls erforderlich), pingen Sie dann die Registry, rufen Sie Metadaten für ein bekanntes Paket ab und laden Sie optional einen Tarball herunter. Dieser Ansatz stellt sicher, dass Ihre Registry auf HTTP-Ebene voll funktionsfähig ist.
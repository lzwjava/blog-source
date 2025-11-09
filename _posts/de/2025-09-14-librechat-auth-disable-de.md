---
audio: false
date: 2025-09-14
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Deaktivierung von LibreChat-Authentifizierungsumgehungen
translated: true
type: note
---

Kurze Antwort: Man kann die Authentifizierung in LibreChat nicht komplett abschalten, aber man kann das Problem "wird mich ständig zum Einloggen auffordern" beheben und es sich fast wie "ohne Login" anfühlen lassen. Hier ist, was tatsächlich funktioniert (und warum):

### 1) Authentifizierung kann nicht komplett deaktiviert werden

Dies wurde vom Maintainer bestätigt: Die Registrierung kann deaktiviert werden, aber das Authentifizierungssystem selbst kann nicht abgeschaltet werden. ([GitHub][1])

### 2) Warum man ständig ausgeloggt wird

Wenn Sie auf Ihre Instanz über **HTTP** zugreifen (z.B. LAN-IP), werden Cookies in der Produktionsumgebung als `secure` markiert, sodass der Browser sie nicht beibehält; Sie werden zum Login zurückgebracht. Verwenden Sie **HTTPS** (selbst selbstsigniert) oder führen Sie die API in einem Entwicklermodus aus, der sichere Cookies deaktiviert. ([GitHub][1])

### 3) Zwei zuverlässige Lösungen

#### Option A — Richtig/sicher (empfohlen)

* Setzen Sie LibreChat hinter HTTPS (nginx/caddy/traefik; selbstsigniert ist im LAN in Ordnung).
* Erhöhen Sie dann die Session-Fenster in Ihrer `.env`-Datei:

  ```
  SESSION_EXPIRY=1000 * 60 * 60 * 24       # 24h
  REFRESH_TOKEN_EXPIRY=(1000 * 60 * 60 * 24) * 30  # 30d
  ```
* Starten Sie die Container nach der Änderung der .env-Datei neu.
  Dies hält Sie tagelang/wochenlang eingeloggt und behebt das Cookie-Drop-Problem. ([GitHub][2])

#### Option B — "Ich bin in einem privaten LAN und möchte einfach, dass die Abmeldung aufhört"

* Erstellen Sie eine `docker-compose.override.yml` und führen Sie die API im Dev-Modus aus (deaktiviert sichere Cookies):

  ```yaml
  services:
    api:
      command: npm run backend:dev
  ```
* `docker compose up -d` ausführen, um die Änderung zu übernehmen.
  Dies ist weniger sicher (Cookies nicht `secure`), stoppt aber das erzwungene Neu-Einloggen über einfaches HTTP. ([librechat.ai][3])

### 4) Optionale Quality-of-Life-Anpassungen

* **Deaktivieren Sie neue Anmeldungen**, damit es effektiv single-user ist:

  ```
  ALLOW_REGISTRATION=false
  ```

  (Sie können bei Bedarf weiterhin Benutzer über `npm run create-user` hinzufügen.) ([librechat.ai][4])
* Behalten Sie andere Authentifizierungs-Optionen in `.env` (E-Mail/Social-Login-Flags) bei, wenn Sie den einfachsten Login-Pfad wünschen. ([librechat.ai][5])

### 5) Schnelle Checkliste für Ihren Fall (v0.8.0-rc3)

1. Entscheiden Sie: HTTPS-Proxy (beste) **oder** Dev-Modus (schnelle LAN-Lösung).
2. Setzen Sie längere `SESSION_EXPIRY` und `REFRESH_TOKEN_EXPIRY` in `.env`.
3. Starten Sie den Stack neu, damit die .env-Änderungen wirksam werden.
4. (Optional) Schalten Sie die Registrierung aus für ein "Single-User"-Gefühl.

Wenn Sie möchten, fügen Sie Ihre aktuelle `docker-compose.yml` und `.env` (ohne Secrets) ein. Ich markiere genau, was Sie für Ihr Setup hinzufügen/ändern müssen.

[1]: https://github.com/danny-avila/LibreChat/discussions/572 "[Question]: Require login every time refresh · danny-avila LibreChat · Discussion #572 · GitHub"
[2]: https://github.com/danny-avila/LibreChat/discussions/2571?utm_source=chatgpt.com "Is there a way to increase or disable the auto-logoff time?"
[3]: https://www.librechat.ai/blog/2024-05-16_unsecured_http "GitHub"
[4]: https://www.librechat.ai/docs/configuration/authentication "GitHub"
[5]: https://www.librechat.ai/docs/configuration/dotenv "GitHub"
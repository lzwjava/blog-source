---
audio: false
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: GitHub-Personenzugriffstoken-Anleitung
translated: true
type: note
---

Ein **Personal Access Token (PAT)** von GitHub ist wie ein Passwort, das Sie selbst für den sicheren Zugriff auf die APIs und Ressourcen von GitHub generieren. Es wird häufig verwendet, da es flexibler und sicherer ist, als Ihr GitHub-Passwort überall einzutippen.

Hier erfahren Sie, wie Sie es **weise** verwenden und was seine **Hauptfunktionen** sind:

---

## Hauptfunktionen eines PAT

1. **Authentifizierung für Git-Befehle**
   Anstatt Ihren GitHub-Benutzernamen und Ihr Passwort beim Pushen/Pullen einzugeben, verwenden Sie einen PAT. Dies ist besonders wichtig, da GitHub die Passwortauthentifizierung für Git über HTTPS deaktiviert hat.

2. **API-Zugriff**
   Wenn Sie Skripte, Tools oder CI/CD-Pipelines schreiben, die die GitHub-API aufrufen, ermöglicht ein PAT eine sichere Authentifizierung und das Senden von Anfragen (z. B. das Erstellen von Issues, Abrufen von Repositories oder Verwalten von Workflows).

3. **Zugriffskontrolle mit Scopes**
   Sie legen genau fest, was das Token tun darf (z. B. schreibgeschützter Zugriff auf Repos oder Schreibzugriff zum Pushen von Code). Dies hilft, den Schaden zu begrenzen, falls das Token verloren geht.

4. **Automatisierung & Integrationen**
   Tools wie GitHub Actions, Jenkins oder lokale Skripte können PATs verwenden, um Abhängigkeiten abzurufen, Packages zu veröffentlichen oder Repositories zu aktualisieren.

5. **Alternative zu SSH**
   Einige bevorzugen die Verwendung von PATs gegenüber der Einrichtung von SSH-Schlüsseln – es ist einfacher, sie über Skripte oder Umgebungen hinweg zu teilen.

---

## Wie man einen PAT weise verwendet

* **Scopes einschränken**: Gewähren Sie ihm nur die Berechtigungen, die Sie tatsächlich benötigen. Wenn Sie beispielsweise nur private Repos pullen müssen, gewähren Sie keinen Schreibzugriff.
* **Ablaufdatum setzen**: Verwenden Sie für die meisten Aufgaben kurzlebige Tokens (z. B. 30 oder 90 Tage). Erneuern Sie sie, anstatt einen für immer zu behalten.
* **Sicher speichern**: Hardcodieren Sie Ihren PAT nicht in Skripten oder pushen Sie ihn zu GitHub. Verwenden Sie Umweltvariablen, `.gitignore`-Dateien oder Secrets-Manager (z. B. GitHub Actions Secrets, 1Password, AWS Secrets Manager).
* **Regelmäßig rotieren**: Widerrufen Sie alte Tokens, die Sie nicht mehr verwenden. Das hält Ihre Sicherheitshygiene sauber.
* **Feingranulierte Tokens verwenden (neuer)**: GitHub empfiehlt jetzt feingranulierte PATs, bei denen Sie den Zugriff repo-weise kontrollieren können, anstatt eines breiten globalen Zugriffs.
* **SSH für die tägliche Arbeit bevorzugen**: PATs sind am besten für Automatisierung und API-Nutzung geeignet. Für Ihre eigene lokale Entwicklung sind SSH-Schlüssel oft sicherer und langfristig einfacher.

---

👉 Ein gutes mentales Modell:

* **PAT = Passwort, das Sie anpassen und jederzeit widerrufen können.**
* **SSH-Schlüssel = Ausweis für Ihren eigenen Arbeitsplatzrechner.**
* Verwenden Sie **PATs für Skripte, CI oder Integrationen** und **SSH-Schlüssel für Ihre tägliche lokale Entwicklung**.

---

Möchten Sie, dass ich Ihnen auch ein **schrittweises Beispiel** zeige, wie Sie einen PAT für `git push` mit HTTPS einrichten, oder interessieren Sie sich mehr dafür, wie man ihn in der **Automatisierung (z. B. GitHub Actions, Skripte)** verwendet?
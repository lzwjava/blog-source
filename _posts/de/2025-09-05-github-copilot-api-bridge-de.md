---
audio: false
generated: true
image: false
lang: de
layout: post
title: GitHub Copilot API Bridge
translated: true
type: note
---

Du bist auf **ericc-ch/copilot-api** gelandet, ein GitHub-Projekt, das **GitHub Copilot** in einen lokalen API-Server verwandelt, der mit **OpenAI**- und **Anthropic**-APIs (z. B. Claude) kompatibel ist.

Hier ist eine klarere Aufschlüsselung – keine Tabellen, nur klare Worte:

---

### Was ist das?

* Es ist ein **reverse-engineerter Proxy**, der es dir ermöglicht, mit GitHub Copilot über bekannte OpenAI-Endpoints wie `/v1/chat/completions`, `/v1/models` und `/v1/embeddings` zu interagieren. Du kannst auch Anthropic-kompatible Endpoints wie `/v1/messages` verwenden ([GitHub][1]).

* Im Wesentlichen ermöglicht dies Tools, die OpenAI- oder Anthropic-APIs unterstützen – wie Claude Code –, GitHub Copilot als ihr Backend zu nutzen ([GitHub][1]).

---

### Wichtige Funktionen

* **OpenAI- & Anthropic-Kompatibilität**: Funktioniert wie die echte OpenAI- oder Anthropic-API ([GitHub][1]).
* **Claude Code-Integration**: Bereit für die Integration in Claude Code mit einem `--claude-code`-Flag ([GitHub][1]).
* **Nutzungs-Dashboard**: Überwache deine Copilot-API-Nutzung und Kontingente über eine eingebaute Weboberfläche ([GitHub][1]).
* **Rate Limiting & Freigabe-Steuerung**: Beinhaltet Optionen für Ratenbegrenzung (`--rate-limit`), automatisches Warten (`--wait`), manuelle Freigabe (`--manual`) und Debugging (Anzeige von Tokens) – ideal, um die Missbrauchssysteme von GitHub zu umgehen ([GitHub][1]).
* **Unterstützt verschiedene Copilot-Pläne**: Individuelle, Business- oder Enterprise-Accounts funktionieren alle ([GitHub][1]).

---

### Einrichtung & Verwendung

* **Voraussetzungen**: Du benötigst Bun (≥ 1.2.x) und ein GitHub Copilot-Abonnement ([GitHub][1]).
* **Installationsoptionen**:

  * **Docker**:

    ```bash
    docker build -t copilot-api .
    docker run -p 4141:4141 -v $(pwd)/copilot-data:/root/.local/share/copilot-api copilot-api
    ```

    Oder gib deinen GitHub-Token direkt über `GH_TOKEN` an ([GitHub][1]).
  * **npx**:

    ```bash
    npx copilot-api@latest start --port 8080
    ```

    Oder `npx copilot-api@latest auth` nur zur Authentifizierung ([GitHub][1]).
* **Befehlsstruktur**:

  * `start`: Startet den API-Server (erledigt bei Bedarf die Authentifizierung).
  * `auth`: Löst die GitHub-Anmeldung aus, ohne den Server zu starten.
  * `check-usage**: Gibt die aktuelle Copilot-Nutzung in deinem Terminal aus.
  * `debug`: Zeigt Diagnoseinformationen an (Versionen, Auth-Status, etc.), mit optionaler `--json`-Ausgabe ([GitHub][1]).

---

### Feedback aus der Praxis

Reddit-Nutzer haben sich geäußert:

> „Dieses Projekt ermöglicht es dir, Copilot in einen OpenAI-kompatiblen Endpoint zu verwandeln.“ ([Reddit][2])
> „Es ist ein fantastisches Projekt, um dein …“ ([Reddit][3])

---

### Wichtige Hinweise

* **Inoffiziell & Nicht unterstützt**: Dies ist **kein** offizielles GitHub-Produkt und könnte jederzeit brechen ([GitHub][1]).
* **Risiko der Missbrauchserkennung**: Starke oder automatisierte Nutzung könnte den Missbrauchsschutz von GitHub auslösen und deinen Copilot-Zugang suspendieren ([GitHub][1]).
* **Mögliche Probleme mit Ratenbegrenzung**: Einige Nutzer haben Fehler wie `421 Misdirected Request` gemeldet, und der Maintainer hat die Entwicklung pausiert, während er untersucht ([GitHub][4]).

---

### Zusammenfassung (Keine Tabellen nötig)

* **Was es tut**: Stellt GitHub Copilot so bereit, als wäre es eine OpenAI/Anthropic-API.
* **Warum das wichtig ist**: Macht Copilot in Tools nutzbar, die diese APIs erwarten – wie Claude Code.
* **Wie man es benutzt**: Installiere via Docker oder npx; führe Befehle aus, um zu starten, zu authentifizieren oder die Nutzung zu überwachen.
* **Mit Vorsicht genießen**: Es ist praktisch, aber inoffiziell, und die Ratenbegrenzungen oder Sicherheitsvorkehrungen von GitHub könnten bei starker Nutzung Probleme bereiten.

---

Lass mich wissen, wenn du Hilfe bei der Einrichtung benötigst oder neugierig auf die Integration in ein bestimmtes Projekt oder Tool bist!

[1]: https://github.com/ericc-ch/copilot-api?utm_source=chatgpt.com "ericc-ch/copilot-api"
[2]: https://www.reddit.com/r/ChatGPTCoding/comments/1m6cqac/how_to_use_your_github_copilot_subscription_with/?utm_source=chatgpt.com "How to use your GitHub Copilot subscription with Claude ..."
[3]: https://www.reddit.com/r/ClaudeAI/comments/1lc21gk/using_github_copilot_as_a_provider_for_claude_code/?utm_source=chatgpt.com "Using GitHub Copilot as a provider for Claude Code"
[4]: https://github.com/ericc-ch/copilot-api/issues/7?utm_source=chatgpt.com "Issue #7 · ericc-ch/copilot-api - 421 Misdirected Request"
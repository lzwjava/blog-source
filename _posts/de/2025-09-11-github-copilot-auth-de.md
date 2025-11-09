---
audio: false
date: 2025-09-11
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: GitHub Copilot Authentifizierungsablauf
translated: true
type: note
---

Gute Frage – der Authentifizierungsablauf von GitHub Copilot ist im Grunde ein standardmäßiger **OAuth2 Device Code Grant**, jedoch mit einigen GitHub-spezifischen Tokens, die für den Copilot-Dienst selbst darüber gelegt sind. Lass mich das Schritt für Schritt aufschlüsseln:

---

### 1. **Device Flow (`/login/device/code`)**

* Wenn du dich zum ersten Mal anmeldest, ruft der Copilot-Client (z. B. die VS Code-Erweiterung, das JetBrains-Plugin oder die CLI) den GitHub OAuth-Endpunkt auf:

  ```
  POST https://github.com/login/device/code
  ```
* Er sendet die **client_id** (spezifisch für GitHub Copilot) mit.
* GitHub antwortet mit:

  * `device_code` (interner Code, der für das Polling verwendet wird),
  * `user_code` (den Code, den du siehst und in deinem Browser eingibst),
  * `verification_uri` (die URL, die du besuchst, um den Code einzugeben),
  * `interval` (wie oft der Client pollen soll).

---

### 2. **Polling für den Access Token**

* Der Copilot-Client führt dann Polling durch:

  ```
  POST https://github.com/login/oauth/access_token
  ```
* Er fügt den `device_code` und die `client_id` hinzu.
* Sobald du die Anfrage in deinem Browser genehmigt hast, gibt GitHub zurück:

  * `access_token` (ein **GitHub OAuth-Token**, der für die Copilot-Nutzung berechtigt ist),
  * `token_type=bearer`,
  * `expires_in` (Lebensdauer).

Dieser `access_token` ist ein **normales GitHub OAuth2-Token**.

---

### 3. **Austausch gegen den `copilot_internal` Token**

* Der Copilot-Client kann mit dem GitHub OAuth-Token nicht direkt die Copilot-APIs aufrufen.
* Stattdessen tauscht er ihn beim Copilot-Dienst ein:

  ```
  POST https://api.github.com/copilot_internal/v2/token
  Authorization: Bearer <GitHub OAuth access_token>
  ```
* Die Antwort lautet:

  ```json
  {
    "token": "<copilot_internal token>",
    "expires_at": "...",
    "user": { ... }
  }
  ```
* Dieser **`copilot_internal` v2-Token** ist es, was der Copilot-Client verwendet, um mit dem **Copilot Inference Service** (z. B. `https://copilot-proxy.githubusercontent.com`) zu kommunizieren.

---

### 4. **Verwendung des `copilot_internal` Tokens**

* Alle nachfolgenden Completions- oder Chat-Anfragen werden authentifiziert mit:

  ```
  Authorization: Bearer <copilot_internal token>
  ```
* Dieser Token hat eine kurze Lebensdauer (normalerweise ca. 1 Stunde) und ist an deinen GitHub-Account und Copilot-Abonnementstatus gebunden.
* Der Client aktualisiert ihn regelmäßig, indem er den GitHub OAuth Access Token erneut austauscht.

---

✅ **Zusammenfassend:**

* `/login/device/code` → gibt dir einen Code zur Authentifizierung im Browser.
* `/login/oauth/access_token` → gibt dir einen GitHub OAuth-Token.
* `/copilot_internal/v2/token` → tauscht diesen gegen einen kurzlebigen Copilot-Token ein, der die *eigentliche* Berechtigung für Completions ist.

---

Möchtest du, dass ich dir auch die **genauen Request/Response-Beispiele** (mit Headern und Beispiel-JSON) zeichne, damit du siehst, wie die Payloads in der Praxis aussehen?
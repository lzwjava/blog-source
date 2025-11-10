---
audio: false
generated: true
image: false
lang: de
layout: post
title: Beheben des Copilot-Chat-Authentifizierungsfehlers
translated: true
type: note
---

Dieser Fehler bedeutet in der Regel, dass **GitHub Copilot Chat** keinen gültigen Authentifizierungstoken finden konnte und daher nicht mit dem Copilot-Dienst kommunizieren kann.
Es handelt sich nicht um einen Programmierfehler — es ist ein **Authentifizierungs-/Konfigurationsproblem**.

So beheben Sie das Problem Schritt für Schritt, je nachdem, wo Sie Copilot Chat verwenden:

---

### 1. Stellen Sie sicher, dass Sie mit einem Copilot-fähigen Konto angemeldet sind

* In **VS Code** oder einer **JetBrains**-IDE:

  1. Öffnen Sie die Befehlspalette (**Strg+Umschalt+P** / **Cmd+Umschalt+P**).
  2. Suchen Sie nach **"GitHub: Sign in"**.
  3. Folgen Sie dem Anmeldeprozess (er öffnet einen Browser zur Autorisierung).
  4. Stellen Sie sicher, dass das Konto, mit dem Sie sich angemeldet haben, über **ein aktives GitHub Copilot-Abonnement** verfügt.
* In **Neovim CLI** (`copilot.vim` oder `copilot.lua`):

  * Führen Sie `:Copilot sign in` aus und folgen Sie dem Link in Ihrem Browser.

---

### 2. Prüfen Sie, ob GitHub Copilot Chat aktiviert ist

* In VS Code:

  * Gehen Sie zu **Erweiterungen** → suchen Sie nach "GitHub Copilot Chat" → stellen Sie sicher, dass es installiert und aktiviert ist.
  * Einstellungen → suchen Sie nach "Copilot Chat: Enabled" → schalten Sie es ein.

---

### 3. Aktualisieren Sie den Authentifizierungstoken

Manchmal laufen Token ab oder gehen verloren (besonders wenn Sie das Netzwerk gewechselt, die IDE aktualisiert oder die Konten gewechselt haben).

* VS Code:

  1. Befehlspalette → **"GitHub Copilot: Sign out"**.
  2. Dann erneut **"GitHub Copilot: Sign in"**.
* CLI:

  * Löschen Sie die Token-Datei (z.B. `~/.config/github-copilot/hosts.json`) und melden Sie sich erneut an.

---

### 4. Prüfen Sie Netzwerk-/Firewall-Einschränkungen

* Wenn Sie sich in einem Unternehmens-VPN oder hinter einer Firewall befinden, könnte der Zugriff auf die GitHub Copilot-API blockiert sein.
* Erlauben Sie den Zugriff auf `github.com`, `api.githubcopilot.com` und `copilot-proxy.githubusercontent.com`.

---

### 5. Aktualisieren Sie Ihre IDE und Copilot-Erweiterungen

* Veraltete Versionen von VS Code oder Copilot-Erweiterungen verursachen manchmal dieses Problem.
* Aktualisieren Sie beide und starten Sie Ihre IDE neu.

---

💡 Wenn Sie die Authentifizierung behoben haben, aber weiterhin Fehler sehen, benötigt GitHub Copilot Chat auch **Zugriff auf die Copilot Chat-Funktion** — einige Konten haben Copilot für Code, aber **nicht Chat**, es sei denn, dies wird explizit in den Einstellungen aktiviert.

---

Falls Sie möchten, kann ich Ihnen **die genaue VS Code-Befehlssequenz** geben, um die Authentifizierung von Copilot Chat vollständig zurückzusetzen, damit Sie erneut zur Anmeldung aufgefordert werden. Soll ich das für Sie vorbereiten?
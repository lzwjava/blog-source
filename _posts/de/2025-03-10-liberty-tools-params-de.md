---
audio: false
generated: true
lang: de
layout: post
title: Benutzerdefinierte JVM-Parameter im Liberty Tools Plugin übergeben
translated: true
type: note
---

Sie können benutzerdefinierte JVM-Parameter – wie `-Dversion=5.1` – übergeben, indem Sie diese Ihrer Liberty-Dev-Mode-Startkonfiguration in VS Code hinzufügen. Typischerweise erfolgt dies durch Bearbeiten (oder Erstellen) der Datei `.vscode/launch.json` in Ihrem Projekt und Aufnehmen des Parameters unter einer Eigenschaft wie `"vmArgs"` (oder `"args"`, falls Ihre Konfiguration Maven-Goal-Argumente erwartet).

Beispiel: Wenn Sie die Liberty-Tools-Erweiterung mit dem Dev-Mode verwenden, könnte Ihre Konfiguration so aussehen:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "liberty",
      "request": "launch",
      "name": "Liberty Dev Mode",
      "goal": "dev",
      "vmArgs": "-Dversion=5.1"
    }
  ]
}
```

### Schritte:
1.  **Öffnen oder Erstellen Sie die Startkonfiguration:**
    *   Öffnen Sie Ihr Projekt in VS Code.
    *   Navigieren Sie zum Ordner `.vscode` und öffnen (oder erstellen) Sie die Datei `launch.json`.

2.  **Fügen Sie Ihre Dev-Mode-Konfiguration hinzu:**
    *   Fügen Sie einen Konfigurationseintrag wie oben gezeigt hinzu. Der Schlüssel `"vmArgs"` ermöglicht es Ihnen, JVM-Optionen anzugeben, die an den Server übergeben werden, wenn der Dev-Mode startet.

3.  **Speichern und Starten:**
    *   Speichern Sie die Datei.
    *   Verwenden Sie die Ansicht "Ausführen und Debuggen", um die Konfiguration "Liberty Dev Mode" zu starten.

Wenn Sie Maven direkt verwenden, könnten Sie den Dev-Mode auch über die Befehlszeile starten mit:

```bash
mvn liberty:dev -Dversion=5.1
```

Dies übergibt die benutzerdefinierte Eigenschaft an die JVM, wenn der Server startet.

Wenn Sie es auf diese Weise konfigurieren, wird die Liberty-Tools-Erweiterung Ihren benutzerdefinierten Parameter (`-Dversion=5.1`) jedes Mal einbeziehen, wenn Sie den Dev-Mode starten.
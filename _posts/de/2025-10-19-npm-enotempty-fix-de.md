---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Beheben des npm ENOTEMPTY-Installationsfehlers
translated: true
type: note
---

### Den Fehler verstehen

Ihr Befehl `sudo npm i -g @anthropic-ai/claude-code --verbose` schlägt mit einem `ENOTEMPTY`-Fehler während des Installationsprozesses fehl. Dies ist ein häufiges npm-Problem, das auftritt, wenn npm versucht, ein vorhandenes Verzeichnis als Teil eines Updates oder einer Neuinstallation eines Pakets umzubenennen (oder zu verschieben), das Verzeichnis jedoch nicht leer ist. In diesem Fall schlägt die Umbenennung von `/usr/lib/node_modules/@anthropic-ai/claude-code` an einen temporären Sicherungsspeicherort (`/usr/lib/node_modules/@anthropic-ai/.claude-code-ZjqcDZyQ`) speziell fehl.

Dies geschieht typischerweise aufgrund von:
-   Einer vorherigen teilweisen oder unterbrochenen Installation, die Dateien oder Unterverzeichnisse hinterlassen hat.
-   Dateisperren durch einen anderen Prozess (z. B. wenn das Paket teilweise geladen wurde oder ein anderer npm-Befehl ausgeführt wird).
-   Selten: Berechtigungsproblemen bei globalen Installationen mit `sudo`.

Das Paket selbst (`@anthropic-ai/claude-code`) ist legitim – es ist das offizielle CLI-Tool von Anthropic für "Claude Code", einen agentischen Coding-Assistenten, der sich in Ihr Terminal und Ihre Codebase integriert.

### Schnelle Lösungen

Versuchen Sie diese Schritte in der angegebenen Reihenfolge. Führen Sie sie als root oder mit `sudo` aus, wo angegeben, da es sich um eine globale Installation handelt.

1.  **Entfernen Sie das vorhandene Verzeichnis manuell**
    Dies beseitigt die problematische Teilinstallation:
    ```
    sudo rm -rf /usr/lib/node_modules/@anthropic-ai/claude-code
    ```
    -   Wenn das übergeordnete Scoped-Verzeichnis (`@anthropic-ai`) nun leer ist, können Sie es auch entfernen:
        ```
        sudo rm -rf /usr/lib/node_modules/@anthropic-ai
        ```
    Wiederholen Sie dann Ihren ursprünglichen Befehl:
    ```
    sudo npm i -g @anthropic-ai/claude-code --verbose
    ```

2.  **npm-Cache leeren**
    Wenn das Obige nicht funktioniert, könnten beschädigte Cache-Einträge beteiligt sein:
    ```
    sudo npm cache clean --force
    sudo npm cache verify
    ```
    Wiederholen Sie die Installation danach.

3.  **Auf laufende Prozesse prüfen**
    Stellen Sie sicher, dass keine anderen npm/Node-Prozesse das Verzeichnis verwenden:
    ```
    ps aux | grep npm
    ```
    Beenden Sie gegebenenfalls verbleibende Prozesse (z. B. `sudo kill <PID>`) und versuchen Sie es erneut.

4.  **Alternative: Verwenden Sie npx zum Testen**
    Wenn Sie das Tool nur testen möchten, ohne eine vollständige globale Installation durchzuführen, versuchen Sie:
    ```
    npx @anthropic-ai/claude-code --help
    ```
    Dies lädt es temporär herunter und führt es aus, ohne Ihre globalen Module zu verändern.

### Zusätzliche Tipps

-   **Berechtigungen (Best Practice)**: Globale Installationen mit `sudo` können später zu Problemen mit dem Besitz führen. Ziehen Sie in Betracht, einen Node Version Manager wie `nvm` zu verwenden, um `sudo` ganz zu vermeiden, oder setzen Sie ein benutzerdefiniertes globales Präfix:
    ```
    mkdir ~/.npm-global
    npm config set prefix '~/.npm-global'
    export PATH=~/.npm-global/bin:$PATH
    ```
    Installieren Sie dann ohne `sudo`.
-   **Nach der Installation überprüfen**: Sobald installiert, prüfen Sie mit `claude-code --version` (angenommen, das ist der Binärname – bitte in der Dokumentation bestätigen).
-   Wenn die Probleme weiterhin bestehen, teilen Sie die Ausgabe von `npm ls -g @anthropic-ai/claude-code` für weitere Diagnosen mit.

Dies sollte Sie schnell zum Laufen bringen. Wenn Sie auf ein weiteres Problem stoßen, fügen Sie das neue Protokoll ein!

[Claude Code on npm](https://www.npmjs.com/package/@anthropic-ai/claude-code)  
[Anthropic Docs: Set up Claude Code](https://docs.claude.com/en/docs/claude-code/setup)
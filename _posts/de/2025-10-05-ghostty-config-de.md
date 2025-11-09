---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Ghostty Shell Konfigurationsanleitung
translated: true
type: note
---

### Ghostty und .bashrc unter Ubuntu

Ghostty verhält sich ähnlich wie das standardmäßige GNOME-Terminal unter Ubuntu (und anderen Linux-Distributionen), wenn es um das Laden von `.bashrc` geht. Standardmäßig startet Ghostty **non-login interaktive Shells** für bash, was bedeutet, dass es `~/.bashrc` direkt einbindet – genau wie das GNOME-Terminal. Dies ist das Standardverhalten für die meisten Linux-Terminals, bei dem `.bashrc` das Setup der interaktiven Shell behandelt (z.B. Aliase, Prompts, Umgebungsvariablen für Non-Login-Sessions).

#### Wie es .bashrc lädt
- Wenn Sie ein neues Ghostty-Fenster oder einen neuen Tab öffnen, führt es `bash` (oder Ihre Standard-Shell) als Non-Login-Shell aus.
- Bash prüft, ob eine `~/.bashrc` vorhanden ist, und bindet sie ein, wenn die Shell interaktiv ist (was standardmäßig der Fall ist).
- Wenn Sie eine `~/.bash_profile` haben (typischerweise für Login-Shells), wird diese nicht eingebunden, es sei denn, Sie konfigurieren Ghostty explizit so, dass es eine Login-Shell startet (z.B. durch Hinzufügen von `initial-command = bash --login` zu `~/.config/ghostty/config`).
- Mögliche Probleme: Einige Benutzer berichten, dass `.bashrc` beim ersten Start für neue Benutzer oder in bestimmten Setups (z.B. Remote-SSH-Sessions unter Ubuntu) nicht geladen wird. Dies kann oft behoben werden, indem sichergestellt wird, dass keine konfligierende `~/.bash_profile` existiert, oder indem man sie manuell in der Konfiguration einbindet. Das Hinzufügen einer Guard-Klausel in `.bashrc` wie `[[ $- != *i* ]] && return` kann Probleme in nicht-interaktiven Kontexten verhindern.

Kurz gesagt, ja – Ghostty verhält sich genauso wie das Standard-Terminal in Bezug auf die Verwendung von `.bashrc` unter Ubuntu, mit demselben Non-Login-Standard.

### Ghostty auf macOS: .zprofile oder .bash_profile?

Auf macOS folgt Ghostty der Tradition der Plattform (wie Terminal.app) und startet standardmäßig **Login-Shells**, unabhängig von der Shell. Dies beeinflusst, welches Profil geladen wird:

- **Bei Verwendung von zsh (macOS-Standard seit Catalina)**: Es bindet `~/.zprofile` (für das Login-Setup) *und* `~/.zshrc` (für das interaktive Setup) jedes Mal ein, wenn ein neues Terminal geöffnet wird.
- **Bei Verwendung von bash**: Es bindet `~/.bash_profile` (Login-Shell) ein. Bash wird hier `~/.bashrc` nicht direkt einbinden – `~/.bashrc` ist nur für Non-Login interaktive Shells. Um den Inhalt von `.bashrc` einzubinden, fügen Sie dies zu Ihrer `~/.bash_profile` hinzu:
  ```
  if [ -f ~/.bashrc ]; then . ~/.bashrc; fi
  ```

Es lädt also `~/.zprofile` für das Standard-zsh-Setup, oder `~/.bash_profile`, wenn Sie bash verwenden. Sie können die Shell wechseln oder die Einstellungen bei Bedarf über die Ghostty-Konfiguration anpassen.

[Shell Integration - Ghostty](https://ghostty.org/docs/features/shell-integration)  
[macOS Login Shells - Ghostty](https://ghostty.org/docs/help/macos-login-shells)  
[Potential bug, .bashrc not read on startup - GitHub Discussion](https://github.com/ghostty-org/ghostty/discussions/3437)  
[Bash Startup Files - GNU Manual](https://www.gnu.org/software/bash/manual/bash.html#Bash-Startup-Files)
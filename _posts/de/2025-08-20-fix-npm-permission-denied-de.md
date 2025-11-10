---
audio: false
generated: true
image: false
lang: de
layout: post
title: Beheben des npm-Berechtigungsfehlers
translated: true
type: note
---

Der Fehler `EACCES: permission denied`, den Sie erhalten, bedeutet, dass Ihr aktueller Benutzer **keine Schreibberechtigungen** für das Verzeichnis `/usr/local/lib/node_modules` hat. Dies ist ein häufiges Problem bei der Installation globaler npm-Pakete unter Linux oder macOS.

### **So beheben Sie dieses Problem**

#### **Option 1: `sudo` verwenden (Nicht für den regelmäßigen Gebrauch empfohlen)**
Sie können `sudo` verwenden, um den Befehl als Root-Benutzer auszuführen, aber dies ist **für den regelmäßigen Gebrauch nicht empfohlen**, da es später zu Berechtigungsproblemen mit npm-Paketen führen kann.

```bash
sudo npm install -g @anthropic-ai/claude-code
```

#### **Option 2: Das Standardverzeichnis von npm ändern (Empfohlen)**
Die beste Vorgehensweise ist, npm so zu konfigurieren, dass es ein Verzeichnis in Ihrem Home-Ordner verwendet, für das Sie Schreibberechtigungen haben.

1. **Erstellen Sie ein globales npm-Verzeichnis in Ihrem Home-Ordner:**
   ```bash
   mkdir ~/.npm-global
   ```
2. **Konfigurieren Sie npm so, dass es dieses Verzeichnis verwendet:**
   ```bash
   npm config set prefix '~/.npm-global'
   ```
3. **Fügen Sie das neue Verzeichnis zu Ihrem `PATH` hinzu:**
   Öffnen Sie Ihre Shell-Konfigurationsdatei (z.B. `~/.bashrc`, `~/.zshrc` oder `~/.profile`) und fügen Sie diese Zeile hinzu:
   ```bash
   export PATH=~/.npm-global/bin:$PATH
   ```
   Laden Sie dann Ihre Shell neu:
   ```bash
   source ~/.bashrc  # oder ~/.zshrc, ~/.profile
   ```
4. **Wiederholen Sie die Installation:**
   ```bash
   npm install -g @anthropic-ai/claude-code
   ```

#### **Option 3: Berechtigungen für `/usr/local` reparieren (Für Fortgeschrittene)**
Wenn Sie `/usr/local` weiterhin verwenden möchten, können Sie dessen Besitz auf Ihren Benutzer ändern:
```bash
sudo chown -R $(whoami) /usr/local/lib/node_modules
```
Wiederholen Sie dann die Installation.

---

**Empfehlung:** Verwenden Sie **Option 2**, um Berechtigungsprobleme in Zukunft zu vermeiden.
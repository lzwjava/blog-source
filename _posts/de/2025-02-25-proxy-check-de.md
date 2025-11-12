---
audio: false
generated: true
lang: de
layout: post
title: Implementierung einer Proxy-Prüfung in Windows
translated: true
type: note
---

Um eine Proxy-Überprüfung in Windows mit Git-Bash und PowerShell zu implementieren, müssen Sie in jeder Shell Mechanismen einrichten, um zu erkennen, wenn netzwerkbezogene Befehle ausgeführt werden, und die Proxy-Einstellungen anzuzeigen, falls diese konfiguriert sind. Im Folgenden finden Sie die Schritte und den Code für sowohl Git-Bash als auch PowerShell. Das erwähnte "Terminal" bezieht sich wahrscheinlich auf Windows Terminal, das diese Shells hostet, daher konzentrieren wir uns auf die Implementierungen für Git-Bash und PowerShell.

---

### **Für Git-Bash**

Git-Bash ist eine Bash-Emulation unter Windows, und wir können eine `DEBUG`-Trap verwenden, um vor jeder Befehlsausführung eine Funktion auszuführen. Das Ziel ist, zu prüfen, ob der Befehl netzwerkbezogen ist und ob Proxy-Einstellungen gesetzt sind, und diese dann anzuzeigen.

#### **Schritte:**

1. **Definieren Sie die Liste der netzwerkbezogenen Befehle.**
2. **Erstellen Sie eine Funktion zum Anzeigen der Proxy-Einstellungen.**
3. **Erstellen Sie eine Funktion, um den Befehl und die Proxy-Einstellungen zu prüfen.**
4. **Richten Sie die `DEBUG`-Trap ein, um die Prüfung vor jedem Befehl auszuführen.**
5. **Definieren Sie eine manuelle `checkproxy`-Funktion, um Proxy-Einstellungen auf Abruf anzuzeigen.**
6. **Fügen Sie alle Konfigurationen zur `.bashrc`-Datei hinzu.**

#### **Implementierung:**

Fügen Sie den folgenden Code zu Ihrer `~/.bashrc`-Datei hinzu (erstellen Sie sie, falls sie nicht existiert):

```bash
# Liste der netzwerkbezogenen Befehle
network_commands=(
    "gpa"
    "git"
    "ssh"
    "scp"
    "sftp"
    "rsync"
    "curl"
    "wget"
    "apt"
    "yum"
    "dnf"
    "npm"
    "yarn"
    "pip"
    "pip3"
    "gem"
    "cargo"
    "docker"
    "kubectl"
    "ping"
    "traceroute"
    "netstat"
    "ss"
    "ip"
    "ifconfig"
    "dig"
    "nslookup"
    "nmap"
    "telnet"
    "ftp"
    "nc"
    "tcpdump"
    "adb"
    "bundle"
    "brew"
    "cpanm"
    "bundle exec jekyll"
    "make"
    "python"
    "glcoud"
)

# Funktion zum Anzeigen der Proxy-Einstellungen
display_proxy() {
    echo -e "🚀 **Proxy-Einstellungen erkannt:**"
    [ -n "$HTTP_PROXY" ] && echo "   - HTTP_PROXY: $HTTP_PROXY"
    [ -n "$http_proxy" ] && echo "   - http_proxy: $http_proxy"
    [ -n "$HTTPS_PROXY" ] && echo "   - HTTPS_PROXY: $HTTPS_PROXY"
    [ -n "$https_proxy" ] && echo "   - https_proxy: $https_proxy"
    [ -n "$ALL_PROXY" ] && echo "   - ALL_PROXY: $ALL_PROXY"
    [ -n "$all_proxy" ] && echo "   - all_proxy: $all_proxy"
    echo ""
}

# Funktion zum Prüfen, ob der Befehl netzwerkbezogen ist und Proxys gesetzt sind
proxy_check() {
    local cmd
    # Extrahiere das erste Wort des Befehls
    cmd=$(echo "$BASH_COMMAND" | awk '{print $1}')
    
    for network_cmd in "${network_commands[@]}"; do
        if [[ "$cmd" == "$network_cmd" ]]; then
            # Prüfe, ob Proxy-Umgebungsvariablen gesetzt sind
            if [ -n "$HTTP_PROXY" ] || [ -n "$http_proxy" ] || \
               [ -n "$HTTPS_PROXY" ] || [ -n "$https_proxy" ] || \
               [ -n "$ALL_PROXY" ] || [ -n "$all_proxy" ]; then
                display_proxy
            fi
            break
        fi
    done
}

# Setze die DEBUG-Trap, um proxy_check vor jedem Befehl auszuführen
trap 'proxy_check' DEBUG

# Funktion zur manuellen Überprüfung der Proxy-Einstellungen
checkproxy() {
    echo "HTTP_PROXY: $HTTP_PROXY"
    echo "HTTPS_PROXY: $HTTPS_PROXY"
    echo "Git HTTP Proxy:"
    git config --get http.proxy
    echo "Git HTTPS Proxy:"
    git config --get https.proxy
}
```

#### **Funktionsweise:**

- Das Array `network_commands` listet Befehle auf, die netzwerkbezogen sind.
- `display_proxy` zeigt alle relevanten Proxy-Umgebungsvariablen an, falls sie gesetzt sind.
- `proxy_check` verwendet `BASH_COMMAND` (verfügbar in der `DEBUG`-Trap), um den ausgeführten Befehl zu erhalten, extrahiert das erste Wort und prüft, ob es mit einem Netzwerkbefehl übereinstimmt. Wenn Proxy-Variablen gesetzt sind, werden sie angezeigt.
- Die Zeile `trap 'proxy_check' DEBUG` stellt sicher, dass `proxy_check` vor jedem Befehl ausgeführt wird.
- `checkproxy` ermöglicht es Ihnen, Proxy-Einstellungen manuell anzuzeigen, einschließlich Git-spezifischer Proxy-Konfigurationen.
- Nachdem Sie dies zu `.bashrc` hinzugefügt haben, starten Sie Git-Bash neu oder führen Sie `source ~/.bashrc` aus, um die Änderungen zu übernehmen.

#### **Verwendung:**

- Wenn Sie einen Netzwerkbefehl ausführen (z.B. `git clone`, `curl`) und Proxy-Einstellungen konfiguriert sind, werden diese vor der Befehlsausführung angezeigt.
- Führen Sie `checkproxy` aus, um Proxy-Einstellungen manuell anzuzeigen.

---

### **Für PowerShell**

PowerShell hat kein direktes Äquivalent zur Bash-`DEBUG`-Trap, aber wir können den `CommandValidationHandler` des `PSReadLine`-Moduls verwenden, um eine ähnliche Funktionalität zu erreichen. Dieser Handler wird vor jedem Befehl ausgeführt und erlaubt es uns, auf Netzwerkbefehle und Proxy-Einstellungen zu prüfen.

#### **Schritte:**

1. **Definieren Sie die Liste der netzwerkbezogenen Befehle.**
2. **Erstellen Sie eine Funktion zum Anzeigen der Proxy-Einstellungen.**
3. **Richten Sie den `CommandValidationHandler` ein, um Befehle und Proxy-Einstellungen zu prüfen.**
4. **Definieren Sie eine manuelle `checkproxy`-Funktion, um Proxy-Einstellungen auf Abruf anzuzeigen.**
5. **Fügen Sie alle Konfigurationen zu Ihrem PowerShell-Profil hinzu.**

#### **Implementierung:**

Suchen Sie zunächst Ihre PowerShell-Profil-Datei, indem Sie `$PROFILE` in PowerShell ausführen. Wenn sie nicht existiert, erstellen Sie sie:

```powershell
New-Item -Type File -Force $PROFILE
```

Fügen Sie den folgenden Code zu Ihrem PowerShell-Profil hinzu (z.B. `Microsoft.PowerShell_profile.ps1`):

```powershell
# Liste der netzwerkbezogenen Befehle
$networkCommands = @(
    "gpa",
    "git",
    "ssh",
    "scp",
    "sftp",
    "rsync",
    "curl",
    "wget",
    "apt",
    "yum",
    "dnf",
    "npm",
    "yarn",
    "pip",
    "pip3",
    "gem",
    "cargo",
    "docker",
    "kubectl",
    "ping",
    "traceroute",
    "netstat",
    "ss",
    "ip",
    "ifconfig",
    "dig",
    "nslookup",
    "nmap",
    "telnet",
    "ftp",
    "nc",
    "tcpdump",
    "adb",
    "bundle",
    "brew",
    "cpanm",
    "bundle exec jekyll",
    "make",
    "python",
    "glcoud"
)

# Funktion zum Anzeigen der Proxy-Einstellungen
function Display-Proxy {
    Write-Host "🚀 **Proxy-Einstellungen erkannt:**"
    if ($env:HTTP_PROXY) { Write-Host "   - HTTP_PROXY: $env:HTTP_PROXY" }
    if ($env:http_proxy) { Write-Host "   - http_proxy: $env:http_proxy" }
    if ($env:HTTPS_PROXY) { Write-Host "   - HTTPS_PROXY: $env:HTTPS_PROXY" }
    if ($env:https_proxy) { Write-Host "   - https_proxy: $env:https_proxy" }
    if ($env:ALL_PROXY) { Write-Host "   - ALL_PROXY: $env:ALL_PROXY" }
    if ($env:all_proxy) { Write-Host "   - all_proxy: $env:all_proxy" }
    Write-Host ""
}

# Richten Sie den CommandValidationHandler ein, um Befehle vor der Ausführung zu prüfen
Set-PSReadLineOption -CommandValidationHandler {
    param($command)
    # Extrahiere das erste Wort des Befehls
    $cmd = ($command -split ' ')[0]
    
    if ($networkCommands -contains $cmd) {
        # Prüfe, ob Proxy-Umgebungsvariablen gesetzt sind
        if ($env:HTTP_PROXY -or $env:http_proxy -or $env:HTTPS_PROXY -or $env:https_proxy -or $env:ALL_PROXY -or $env:all_proxy) {
            Display-Proxy
        }
    }
    # Gib immer true zurück, um die Befehlsausführung zu erlauben
    return $true
}

# Funktion zur manuellen Überprüfung der Proxy-Einstellungen
function checkproxy {
    Write-Host "HTTP_PROXY: $env:HTTP_PROXY"
    Write-Host "HTTPS_PROXY: $env:HTTPS_PROXY"
    Write-Host "Git HTTP Proxy:"
    git config --get http.proxy
    Write-Host "Git HTTPS Proxy:"
    git config --get https.proxy
}
```

#### **Funktionsweise:**

- `$networkCommands` ist ein Array von netzwerkbezogenen Befehlen.
- `Display-Proxy` zeigt alle relevanten Proxy-Umgebungsvariablen an, falls sie gesetzt sind.
- `Set-PSReadLineOption -CommandValidationHandler` definiert einen Skriptblock, der vor jedem Befehl ausgeführt wird:
  - Er extrahiert das erste Wort des Befehls.
  - Prüft, ob es in `$networkCommands` enthalten ist.
  - Wenn Proxy-Variablen gesetzt sind, ruft er `Display-Proxy` auf.
  - Gibt `$true` zurück, um die Befehlsausführung sicherzustellen.
- `checkproxy` ermöglicht die manuelle Anzeige von Proxy-Einstellungen, einschließlich Git-spezifischer Proxys.
- Nach dem Hinzufügen zu Ihrem Profil starten Sie PowerShell neu oder führen Sie `. $PROFILE` aus, um die Änderungen zu übernehmen.

#### **Voraussetzungen:**

- Das `PSReadLine`-Modul ist erforderlich, das standardmäßig in PowerShell 5.1 und höher enthalten ist.
- Wenn Sie eine ältere Version verwenden, müssen Sie PowerShell möglicherweise aktualisieren oder eine alternative Methode finden (hier nicht behandelt, da die meisten Systeme neuere Versionen verwenden).

#### **Verwendung:**

- Wenn Sie einen Netzwerkbefehl ausführen (z.B. `git pull`, `curl`) und Proxy-Einstellungen konfiguriert sind, werden diese vor der Befehlsausführung angezeigt.
- Führen Sie `checkproxy` aus, um Proxy-Einstellungen manuell anzuzeigen.

---

### **Hinweise zum "Terminal"**

- Wenn sich "Terminal" auf Windows Terminal bezieht, ist dies lediglich ein Host für Shells wie Git-Bash, PowerShell oder Command Prompt (cmd.exe).
- Die oben genannten Implementierungen funktionieren innerhalb von Git-Bash- oder PowerShell-Sitzungen in Windows Terminal.
- Eine Implementierung ähnlicher Funktionalität in Command Prompt (cmd.exe) ist aufgrund der begrenzten Skriptfähigkeiten nicht praktikabel. Es wird empfohlen, stattdessen Git-Bash oder PowerShell zu verwenden.

---

### **Zusätzliche Überlegungen**

- **Befehlsanalyse:**
  - Beide Implementierungen prüfen nur das erste Wort des Befehls gegen die Liste der Netzwerkbefehle. Zum Beispiel löst `git clone` aus, weil `git` in der Liste steht.
  - Mehrwortbefehle wie `bundle exec jekyll` lösen aus, wenn `bundle` in der Liste steht, was für die meisten Fälle ausreichend ist.
  - Bei Bedarf könnten Sie den Code ändern, um alle Wörter des Befehls zu prüfen, aber dies könnte zu falsch positiven Ergebnissen führen und ist im Allgemeinen unnötig.

- **Proxy-Variablen:**
  - Beide Implementierungen prüfen auf `HTTP_PROXY`, `http_proxy`, `HTTPS_PROXY`, `https_proxy`, `ALL_PROXY` und `all_proxy`, um gängige Variationen abzudecken.
  - Unter Windows sind Umgebungsvariablen unabhängig von der Groß-/Kleinschreibung, aber wir prüfen aus Konsistenzgründen mit Unix-ähnlichem Verhalten (insbesondere in Git-Bash) beide Schreibweisen.

- **Git-Proxy-Einstellungen:**
  - Die `checkproxy`-Funktion in beiden Shells zeigt Git-spezifische Proxy-Einstellungen mit `git config --get` an.

---

### **Tests**

- **Setzen Sie Proxy-Variablen:**
  - In Git-Bash: `export HTTP_PROXY=http://proxy.example.com:8080`
  - In PowerShell: `$env:HTTP_PROXY = "http://proxy.example.com:8080"`
- **Führen Sie Netzwerkbefehle aus:**
  - Probieren Sie Befehle wie `git --version`, `curl -V` usw.
  - Proxy-Einstellungen sollten vor der Befehlsausgabe angezeigt werden.
- **Verwenden Sie `checkproxy`:**
  - Führen Sie `checkproxy` in einer der Shells aus, um Proxy-Einstellungen manuell anzuzeigen.

---

Diese Implementierung bietet eine robuste Proxy-Überprüfung in sowohl Git-Bash als auch PowerShell, die für die Verwendung innerhalb von Windows Terminal oder eigenständig geeignet ist.
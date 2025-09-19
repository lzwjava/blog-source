---
audio: false
generated: false
image: true
lang: de
layout: post
title: Proxy-Einstellungen anzeigen, bevor Befehle ausgeführt werden
translated: true
---

<div style="text-align: center;">  
    <img class="responsive" src="/assets/images/preexec/pe1.png" alt="prexec" />  
</div>

Das Leben in China oder die Arbeit in Unternehmen, die VPNs und Proxys verwenden, kann die Softwareentwicklung erschweren. Wenn man vergisst, diese Einstellungen zu konfigurieren, führt dies oft zu Verbindungsproblemen. Um Ihren Arbeitsablauf zu optimieren, habe ich mit Hilfe von ChatGPT ein einfaches Zsh-Skript erstellt, das automatisch Ihre Proxy-Einstellungen anzeigt, wenn Sie bestimmte netzwerkabhängige Befehle ausführen.

## Warum Proxy-Einstellungen anzeigen?

Proxies und VPNs sind unerlässlich, um sicher auf externe Ressourcen zuzugreifen. Das Anzeigen Ihrer Proxy-Einstellungen vor der Ausführung von netzwerkabhängigen Befehlen hilft Ihnen, schnell Konnektivitätsprobleme zu erkennen und zu beheben.

## Das Skript

Dieses Skript nutzt die `preexec`-Funktion von Zsh, um zu überprüfen, ob der bevorstehende Befehl netzwerkabhängig ist. Wenn dies der Fall ist und Proxy-Umgebungsvariablen gesetzt sind, werden die aktuellen Proxy-Einstellungen angezeigt.

```bash
# Funktion zum Überprüfen und Anzeigen der Proxy-Einstellungen vor bestimmten Befehlen
preexec() {
    # Netzwerkabhängige Befehle definieren
    local network_commands=(
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
        # Weitere Befehle nach Bedarf hinzufügen
    )
```

    # Extrahiere das erste Wort (Befehl) aus der Befehlszeile
    local cmd
    cmd=$(echo "$1" | awk '{print $1}')

    # Funktion zur Anzeige von Proxy-Variablen
    display_proxy() {
        echo -e "\n🚀 Erkannte Proxy-Einstellungen:"

        [ -n "$HTTP_PROXY" ] && echo "   - HTTP_PROXY: $HTTP_PROXY"
        [ -n "$http_proxy" ] && echo "   - http_proxy: $http_proxy"
        [ -n "$HTTPS_PROXY" ] && echo "   - HTTPS_PROXY: $HTTPS_PROXY"
        [ -n "$https_proxy" ] && echo "   - https_proxy: $https_proxy"
        [ -n "$ALL_PROXY" ] && echo "   - ALL_PROXY: $ALL_PROXY"
        [ -n "$all_proxy" ] && echo "   - all_proxy: $all_proxy"

```bash
echo ""
```

    # Überprüfen, ob der Befehl netzwerkabhängig ist
    for network_cmd in "${network_commands[@]}"; do
        if [[ "$1" == "$network_cmd"* ]]; then
            if [ -n "$HTTP_PROXY" ] || [ -n "$http_proxy" ] || \
               [ -n "$HTTPS_PROXY" ] || [ -n "$https_proxy" ] || \
               [ -n "$ALL_PROXY" ] || [ -n "$all_proxy" ]; then
                
                display_proxy
            fi
            break
        fi
    done
}
```

## Einrichten des Skripts in Zsh

### 1. Öffnen Sie Ihre `.zshrc`-Datei

Verwenden Sie Ihren bevorzugten Texteditor, um die Konfigurationsdatei `.zshrc` zu öffnen. Zum Beispiel:

```bash
nano ~/.zshrc
```

### 2. Fügen Sie die `preexec`-Funktion hinzu

Fügen Sie das obige Skript am Ende der Datei ein.

### 3. Speichern und Schließen

Drücken Sie `STRG + O`, um zu speichern, und `STRG + X`, um zu beenden.

### 4. Änderungen anwenden

Lade deine `.zshrc` neu, um die neue Konfiguration sofort zu übernehmen:

```bash
source ~/.zshrc
```

## Testen des Setups

### 1. Mit aktiviertem Proxy

Setze eine Proxy-Variable temporär und führe einen netzwerkabhängigen Befehl mit `pip` aus:

```bash
export HTTP_PROXY="http://127.0.0.1:7890"
pip install selenium beautifulsoup4 urllib3
```

Erwartete Ausgabe:

```
(Die Code-Blöcke werden nicht übersetzt, da sie in der Regel in der Originalsprache belassen werden sollten, um die Integrität des Codes zu bewahren.)

🚀 Proxy-Einstellungen erkannt:
   - HTTP_PROXY: http://127.0.0.1:7890
   - http_proxy: 127.0.0.1:7890
   - HTTPS_PROXY: 127.0.0.1:7890
   - https_proxy: 127.0.0.1:7890
   - ALL_PROXY: 127.0.0.1:7890
   - all_proxy: 127.0.0.1:7890

Sammeln von Selenium
  Herunterladen von selenium-4.x.x-py2.py3-none-any.whl (xxx kB)
Sammeln von BeautifulSoup4
  Herunterladen von beautifulsoup4-4.x.x-py3-none-any.whl (xxx kB)
Sammeln von urllib3
  Herunterladen von urllib3-1.x.x-py2.py3-none-any.whl (xxx kB)
...
```

### 2. Ohne aktivierten Proxy

Heben Sie die Proxy-Variable auf und führen Sie denselben `pip`-Befehl aus:

```bash
unset HTTP_PROXY
pip install selenium beautifulsoup4 urllib3
```

*Hinweis: Der obige Code bleibt auf Englisch, da es sich um Befehle handelt, die in der Regel nicht übersetzt werden.*

Erwartete Ausgabe:

```
Collecting selenium
  Downloading selenium-4.x.x-py2.py3-none-any.whl (xxx kB)
Collecting beautifulsoup4
  Downloading beautifulsoup4-4.x.x-py3-none-any.whl (xxx kB)
Collecting urllib3
  Downloading urllib3-1.x.x-py2.py3-none-any.whl (xxx kB)
...
```

*(Es sollte keine Proxy-Benachrichtigung erscheinen.)*

### 3. Nicht-Netzwerk-Befehl

Führe einen lokalen Befehl wie `ls` aus:

```bash
ls
```

Erwartete Ausgabe:

```
[Liste der Dateien und Verzeichnisse]
```

*(Es sollte keine Proxy-Benachrichtigung erscheinen.)*

## Anpassung

- Erweitern Sie `network_commands`: Fügen Sie alle zusätzlichen netzwerkabhängigen Befehle zum `network_commands`-Array hinzu.

- Aliase verarbeiten: Stellen Sie sicher, dass alle Aliase für netzwerkabhängige Befehle in der Liste `network_commands` enthalten sind.

  ```bash
  alias gpa='git push all'
  ```

Fügen Sie `"gpa"` zum `network_commands`-Array hinzu, um Proxy-Benachrichtigungen auszulösen, wenn Sie diesen Alias verwenden.

- Sichtbarkeit mit Farben verbessern:

Für eine bessere Sichtbarkeit, insbesondere in überfüllten Terminals, können Sie den Proxy-Benachrichtigungen Farbe hinzufügen:

  ```bash
  # Füge Farbcodes am Anfang deiner .zshrc hinzu
  GREEN='\033[0;32m'
  NC='\033[0m' # Keine Farbe
  ```

  display_proxy() {
      echo -e "\n${GREEN}🚀 Proxy-Einstellungen erkannt:${NC}"

```bash
      [ -n "$HTTP_PROXY" ] && echo "   - HTTP_PROXY: $HTTP_PROXY"
      [ -n "$http_proxy" ] && echo "   - http_proxy: $http_proxy"
      [ -n "$HTTPS_PROXY" ] && echo "   - HTTPS_PROXY: $HTTPS_PROXY"
      [ -n "$https_proxy" ] && echo "   - https_proxy: $https_proxy"
      [ -n "$ALL_PROXY" ] && echo "   - ALL_PROXY: $ALL_PROXY"
      [ -n "$all_proxy" ] && echo "   - all_proxy: $all_proxy"
```

      echo ""
  }
  ```

## Fazit

Die Verwaltung von Proxy-Einstellungen ist entscheidend für einen reibungslosen Softwareentwicklungsprozess in eingeschränkten Netzwerkumgebungen. Dieses Zsh-Skript stellt sicher, dass Sie stets über Ihre Proxy-Konfigurationen informiert sind, wenn Sie Befehle ausführen, die Netzwerkzugriff erfordern. Dies verbessert Ihren Workflow und die Effizienz bei der Fehlerbehebung.

Viel Spaß beim Programmieren! 🚀
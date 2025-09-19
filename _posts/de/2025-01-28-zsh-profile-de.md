---
audio: false
generated: false
image: false
lang: de
layout: post
title: Zsh-Profil
translated: true
---

Dieses Zsh-Profil zielt darauf ab, das Kommandozeilen-Erlebnis zu verbessern, mit einem Fokus auf Proxy-Konfigurationen, Git-Integration und praktischen Aliassen. Die folgenden Abschnitte beschreiben seine Funktionen:

**1. PATH-Konfiguration:**

   - `export PATH=...`: Diese Zeile setzt die `PATH`-Umgebungsvariable, die der Shell mitteilt, wo nach ausführbaren Dateien gesucht werden soll. Sie enthält verschiedene Verzeichnisse wie die für Java, Ruby, Homebrew, Python, Flutter und das Google Cloud SDK. Dies stellt sicher, dass Befehle aus diesen Tools direkt aus dem Terminal ausgeführt werden können.

**2. Proxy-Verwaltung:**

   - `export GLOBAL_PROXY='127.0.0.1:7890'`: Dies definiert eine Variable `GLOBAL_PROXY`, die die Proxy-Server-Adresse enthält.
   - `function start_proxy { ... }`: Diese Funktion setzt die `HTTP_PROXY`, `HTTPS_PROXY`, `http_proxy`, `https_proxy` und `ALL_PROXY`-Umgebungsvariablen, um den angegebenen Proxy zu verwenden. Sie deaktiviert auch vollständige URI-Anfragen für Proxys.
   - `function start_proxy_without_prefix { ... }`: Ähnlich wie `start_proxy`, aber setzt die Proxy-Variablen ohne das Präfix `http://`.
   - `function stop_proxy { ... }`: Diese Funktion setzt die Proxy-Variablen zurück, wodurch der Proxy effektiv deaktiviert wird. Sie aktiviert auch vollständige URI-Anfragen für Proxys.
   - `export NO_PROXY="localhost,127.0.0.1,.example.com,::1"`: Dies gibt eine Liste von Hosts an, die den Proxy umgehen sollen.

**3. Git-Proxy:**

   - `function start_git_proxy { ... }`: Diese Funktion konfiguriert Git, um den globalen Proxy für HTTP- und HTTPS-Verbindungen zu verwenden.
   - `function stop_git_proxy { ... }`: Diese Funktion setzt die Git-Proxy-Einstellungen zurück.

**4. Homebrew-Integration:**

   - `eval "$(/opt/homebrew/bin/brew shellenv)"`: Diese Zeile integriert Homebrew in die Shell-Umgebung, sodass Homebrew-Befehle verwendet werden können.

**5. Konvenienz-Aliasse:**

   - `alias gpa='python ~/bin/gitmessageai.py --api mistral'`: Dies erstellt einen Alias `gpa`, um ein Python-Skript `gitmessageai.py` mit der Mistral-API auszuführen.
   - `alias gca='python ~/bin/gitmessageai.py --no-push'`: Dies erstellt einen Alias `gca`, um dasselbe Skript ohne Push der Änderungen auszuführen.
   - `alias gm='python ~/bin/gitmessageai.py --only-message'`: Dies erstellt einen Alias `gm`, um dasselbe Skript auszuführen und nur die Commit-Nachricht auszugeben.
   - `alias gpam=/usr/local/bin/git-auto-commit`: Dies erstellt einen Alias `gpam`, um das `git-auto-commit`-Skript auszuführen.
   - `alias rougify=/Users/lzwjava/projects/rouge/bin/rougify`: Dies erstellt einen Alias `rougify`, um das `rougify`-Skript auszuführen.

**6. SSL-Zertifikat:**

   - `export SSL_CERT_FILE=~/bin/cacert.pem`: Dies setzt den Pfad zu einer benutzerdefinierten SSL-Zertifikatsdatei.

**7. Homebrew-Auto-Update:**

   - `export HOMEBREW_NO_AUTO_UPDATE=1`: Dies deaktiviert die automatischen Updates von Homebrew.

**8. Vorausführungs-Proxy-Prüfung:**

   - `preexec() { ... }`: Diese Funktion wird vor jedem Befehl ausgeführt. Sie überprüft, ob der Befehl in einer Liste von netzwerkabhängigen Befehlen steht. Wenn dies der Fall ist und wenn Proxy-Variablen gesetzt sind, werden die Proxy-Einstellungen angezeigt.
   - `local network_commands=( ... )`: Dieses Array listet Befehle auf, die als netzwerkabhängig angesehen werden.
   - `display_proxy() { ... }`: Diese Funktion zeigt die aktuellen Proxy-Einstellungen an.

**9. Google Cloud SDK-Vervollständigung:**

   - `if [ -f '/Users/lzwjava/bin/google-cloud-sdk/completion.zsh.inc' ]; then . '/Users/lzwjava/bin/google-cloud-sdk/completion.zsh.inc'; fi`: Diese Zeile aktiviert die Shell-Befehlsvervollständigung für gcloud.

**10. API-Schlüssel und Anmeldeinformationen:**

    - `export GOOGLE_APPLICATION_CREDENTIALS="/Users/lzwjava/bin/graphite-ally-445108-k3-035f0952219d.json"`: Setzt den Pfad zu den Google Cloud-Dienstkonto-Anmeldeinformationen.
    - `export DEEPSEEK_API_KEY="xxx"`: Setzt den DeepSeek-API-Schlüssel.
    - `export MISTRAL_API_KEY="xxx"`: Setzt den Mistral-API-Schlüssel.
    - `export DYLD_LIBRARY_PATH=$(brew --prefix curl)/lib`: Setzt den dynamischen Bibliothekspfad für curl.
    - `export SPEECH_ENDPOINT="https://ai-lzwjava-5596.cognitiveservices.azure.com/"`: Setzt den Azure-Sprachendpunkt.
    - `export DO_API_KEY="xxx"`: Setzt den Digital Ocean-API-Schlüssel.
    - `export GEMINI_API_KEY="xxx"`: Setzt den Gemini-API-Schlüssel.

**11. Conda-Umgebung:**

    - `conda activate base`: Aktiviert die Basis-Conda-Umgebung.

**Zusammenfassend bietet dieses Zsh-Profil eine umfassende Einrichtung für einen Entwickler, einschließlich:**

- Einfache Proxy-Verwaltung mit Funktionen zum Starten und Stoppen von Proxys.
- Git-Proxy-Konfiguration.
- Integration mit Homebrew.
- Bequeme Aliase für häufige Aufgaben.
- Vorausführungs-Proxy-Prüfungen für netzwerkabhängige Befehle.
- API-Schlüssel und Anmeldeinformationen für verschiedene Dienste.
- Conda-Umgebungsaktivierung.

Dieses Profil ist darauf ausgelegt, den Workflow des Benutzers zu optimieren und die Verwaltung verschiedener Entwicklungstools und -dienste zu erleichtern.

```bash
export PATH=/opt/homebrew/Cellar/openjdk@17/17.0.13/libexec/openjdk.jdk/Contents/Home/bin:/opt/homebrew/opt/ruby/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Users/lzwjava/Library/Python/3.9/bin:/Library/TeX/texbin:/Users/lzwjava/bin:/Users/lzwjava/platform-tools:/Users/lzwjava/Downloads/google-cloud-sdk/bin:/Users/lzwjava/bin/flutter/bin:/opt/homebrew/lib/ruby/gems/3.3.0/bin:/opt/homebrew/Cellar/llama.cpp/4539/bin:/Users/lzwjava/bin/google-cloud-sdk/bin

# /opt/homebrew/opt/openjdk/bin

# /opt/homebrew/Cellar/openjdk@17/17.0.13/libexec/openjdk.jdk/Contents/Home/bin

export GLOBAL_PROXY='127.0.0.1:7890'
# export GLOBAL_PROXY='http://192.168.1.1:7890'

function start_proxy {
    export HTTP_PROXY="http://$GLOBAL_PROXY"
    export HTTPS_PROXY="http://$GLOBAL_PROXY"
    export http_proxy="http://$GLOBAL_PROXY"
    export https_proxy="http://$GLOBAL_PROXY"
    export HTTP_PROXY_REQUEST_FULLURI=false
    export HTTPS_PROXY_REQUEST_FULLURI=false
    export ALL_PROXY=$http_proxy
}

function start_proxy_without_prefix {
    export http_proxy=$GLOBAL_PROXY
		export HTTP_PROXY=$GLOBAL_PROXY
		export https_proxy=$GLOBAL_PROXY
    export HTTPS_PROXY=$GLOBAL_PROXY
    export HTTP_PROXY_REQUEST_FULLURI=false
    export HTTPS_PROXY_REQUEST_FULLURI=false
		export ALL_PROXY=$http_proxy
}

function stop_proxy {
    export http_proxy=
		export HTTP_PROXY=
		export https_proxy=
    export HTTPS_PROXY=
    export HTTP_PROXY_REQUEST_FULLURI=true
    export HTTPS_PROXY_REQUEST_FULLURI=true
		export ALL_PROXY=
}

export NO_PROXY="localhost,127.0.0.1,.example.com,::1"

function start_git_proxy {
  git config --global http.proxy $GLOBAL_PROXY
  git config --global https.proxy $GLOBAL_PROXY
}

function stop_git_proxy {
  git config --global --unset http.proxy
  git config --global --unset https.proxy
}

eval "$(/opt/homebrew/bin/brew shellenv)"

start_proxy
# start_git_proxy

# alias python3=/opt/homebrew/bin/python3
# alias pip3=/opt/homebrew/bin/pip3
# alias pip=pip3

alias gpa='python ~/bin/gitmessageai.py --api mistral'
alias gca='python ~/bin/gitmessageai.py --no-push'
alias gm='python ~/bin/gitmessageai.py --only-message'

alias gpam=/usr/local/bin/git-auto-commit

# bundle exec jekyll serve
export SSL_CERT_FILE=~/bin/cacert.pem

alias rougify=/Users/lzwjava/projects/rouge/bin/rougify

# git config --global core.editor "code --wait"
# git config --global -e

export HOMEBREW_NO_AUTO_UPDATE=1

# Funktion zur Überprüfung und Anzeige von Proxy-Einstellungen vor bestimmten Befehlen
preexec() {
    # Definieren Sie netzwerkabhängige Befehle
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
        "python"
        "glcoud"
        # Fügen Sie nach Bedarf weitere Befehle hinzu
    )

    # Extrahieren Sie das erste Wort (Befehl) aus der Befehlszeile
    local cmd
    cmd=$(echo "$1" | awk '{print $1}')

    # Funktion zur Anzeige von Proxy-Variablen
    display_proxy() {
        echo -e "🚀 **Proxy-Einstellungen erkannt:**"

        [ -n "$HTTP_PROXY" ] && echo "   - HTTP_PROXY: $HTTP_PROXY"
        [ -n "$HTTPS_PROXY" ] && echo "   - HTTPS_PROXY: $HTTPS_PROXY"

        echo ""
    }

    # Überprüfen Sie, ob der Befehl netzwerkabhängig ist
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

# Die nächste Zeile aktiviert die Shell-Befehlsvervollständigung für gcloud.
if [ -f '/Users/lzwjava/bin/google-cloud-sdk/completion.zsh.inc' ]; then . '/Users/lzwjava/bin/google-cloud-sdk/completion.zsh.inc'; fi

export GOOGLE_APPLICATION_CREDENTIALS="/Users/lzwjava/bin/graphite-ally-445108-k3-035f0952219d.json"

export DEEPSEEK_API_KEY="xxx"

export MISTRAL_API_KEY="xxx"

export DYLD_LIBRARY_PATH=$(brew --prefix curl)/lib

export SPEECH_ENDPOINT="https://ai-lzwjava-5596.cognitiveservices.azure.com/"

export DO_API_KEY="xxx"

export GEMINI_API_KEY="xxx"

conda activate base
```
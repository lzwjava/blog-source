---
audio: false
generated: false
image: false
lang: de
layout: post
title: Netplan, Systemd, SSH, Conda-Bereinigung
translated: true
type: post
---

### Inhalt

1. [Netplan ausprobieren](#trying-netplan)
   - Statische IP-Konfiguration führte zu SSH-Verlust
   - Physischer Zugriff zum Zurücksetzen erforderlich
   - Die DNS-Resolver-Datei des Systems wurde geändert

2. [Systemd Dienst](#systemd-service)
   - Dienst für lokale LLM-Inferenz konfigurieren
   - Weboberfläche für LLM-Modelle einrichten
   - Regelbasierten Proxy-Tool-Dienst einrichten
   - systemctl-Befehle zur Dienstverwaltung verwenden

3. [SSH-Konfiguration](#ssh-configuration)
   - Externe Verbindungen über corkscrew proxieren
   - Lokales Netzwerk vom Proxy ausschließen
   - SSH-Schlüssel über Keychain und Agent verwalten
   - Standard-Speicherort für private Schlüssel festlegen

4. [Conda in Linux löschen](#delete-conda-in-linux)
   - Gesamtes Conda-Installationsverzeichnis entfernen
   - Conda-Initialisierungscode aus bashrc löschen
   - PATH-Umgebungsvariable aktualisieren
   - Conda-Binärdateien aus dem Systempfad entfernen


## Netplan ausprobieren

Ich habe die folgende Konfiguration ausprobiert, um einer Ubuntu-Maschine eine statische IP-Adresse zuzuweisen. Ich betreibe OpenWebUI und llama.cpp auf diesem Server.

```
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: no
      addresses:
        - 192.168.1.128/32
      gateway4: 192.168.1.1
```

Nachdem ich `sudo netplan apply` ausgeführt hatte, konnte die Maschine nicht mehr über `ssh lzw@192.168.1.128` erreicht werden.

Tastatur und Maus wurden verwendet, um sich an der Maschine anzumelden, die Dateien zu entfernen und die Einstellungen zurückzusetzen.

`/etc/resolv.conf` wurde geändert.

---

## Systemd Dienst

*2025.02.13*

## LLaMA Serverdienstkonfiguration

Dieser Abschnitt erklärt, wie ein systemd-Dienst für den Betrieb des LLaMA-Servers eingerichtet wird, der lokale LLM-Inferenzfunktionen bereitstellt.

```bash
sudo emacs /etc/systemd/system/llama.service
sudo systemctl daemon-reload
sudo systemctl enable llama.service
journalctl -u llama.service
```

```bash
[Unit]
Description=Llama Script

[Service]
ExecStart=/home/lzw/Projects/llama.cpp/build/bin/llama-server -m /home/lzw/Projects/llama.cpp/models/DeepSeek-R1-Distill-Qwen-14B-Q5_K_M.gguf --port 8000  --ctx-size 2048 --batch-size 512 --n-gpu-layers 49 --threads 8 --parallel 1
WorkingDirectory=/home/lzw/Projects/llama.cpp
StandardOutput=append:/home/lzw/llama.log
StandardError=append:/home/lzw/llama.err
Restart=always
User=lzw

[Install]
WantedBy=default.target
```

## Open WebUI Dienstkonfiguration

Dieser Abschnitt erklärt, wie ein systemd-Dienst für den Betrieb von Open WebUI eingerichtet wird, das eine Weboberfläche für die Interaktion mit LLM-Modellen bietet.

```bash
[Unit]
Description=Open Web UI Service

[Service]
ExecStart=/home/lzw/.local/bin/open-webui serve
WorkingDirectory=/home/lzw
StandardOutput=append:/home/lzw/open-webui.log
StandardError=append:/home/lzw/open-webui.err
Restart=always
User=lzw

[Install]
WantedBy=default.target
```

```bash
sudo systemctl enable openwebui.service
sudo systemctl daemon-reload
sudo systemctl start  openwebui.service
```

## Clash Dienstkonfiguration

Dieser Abschnitt erklärt, wie ein systemd-Dienst für den Betrieb von Clash, einem regelbasierten Proxy-Tool, eingerichtet wird.

```bash
[Unit]
Description=Clash Service

[Service]
ExecStart=/home/lzw/clash-linux-386-v1.17.0/clash-linux-386
WorkingDirectory=/home/lzw/clash-linux-386-v1.17.0
StandardOutput=append:/home/lzw/clash.log
StandardError=append:/home/lzw/clash.err
Restart=always
User=lzw

[Install]
WantedBy=default.target
```

```bash
# Erstellen Sie die Dienstdatei
sudo emacs /etc/systemd/system/clash.service 

# Laden Sie den systemd-Daemon neu
sudo systemctl daemon-reload

# Aktivieren und starten Sie den Dienst
sudo systemctl enable clash.service
sudo systemctl start clash.service
sudo systemctl restart clash.service

# Status prüfen
sudo systemctl status clash.service
```

---

## SSH Konfiguration

*2025.02.09*

Diese `ssh-config`-Datei konfiguriert das Verhalten des SSH-Clients. Lassen Sie uns jeden Teil aufschlüsseln:

-   `Host * !192.*.*.*`: Dieser Abschnitt gilt für alle Hosts *außer* denen, die dem Muster `192.*.*.*` entsprechen (typischerweise lokale Netzwerkadressen).
    -   `ProxyCommand corkscrew localhost 7890 %h %p`: Das ist der entscheidende Teil. Es weist SSH an, das Programm `corkscrew` zu verwenden, um sich mit dem Zielhost zu verbinden.
        -   `corkscrew`: Ein Tool, das es Ihnen ermöglicht, SSH-Verbindungen über HTTP- oder HTTPS-Proxys zu tunneln.
        -   `localhost 7890`: Gibt die Adresse (`localhost`) und den Port (`7890`) des Proxy-Servers an. Dies setzt voraus, dass auf Ihrem lokalen Rechner ein Proxy-Server läuft, der auf Port 7890 lauscht (z. B. Shadowsocks, ein SOCKS-Proxy oder eine andere Tunneling-Lösung).
        -   `%h`: Eine spezielle SSH-Variable, die zum Ziel-Hostname erweitert wird, mit dem Sie sich verbinden möchten.
        -   `%p`: Eine weitere SSH-Variable, die zum Ziel-Port erweitert wird (normalerweise 22 für SSH).
    - Zusammenfassend konfiguriert dieser `Host`-Block SSH so, dass der `corkscrew`-Proxy für alle Verbindungen *außer* denen zum lokalen Netzwerk verwendet wird.

-   `Host *`: Dieser Abschnitt gilt für *alle* Hosts.
    -   `UseKeychain yes`: Unter macOS weist dies SSH an, SSH-Schlüssel aus Ihrem Keychain zu speichern und abzurufen, sodass Sie nicht jedes Mal Ihr Passwort eingeben müssen.
    -   `AddKeysToAgent yes`: Dies fügt Ihre SSH-Schlüssel automatisch dem SSH-Agenten hinzu, sodass Sie sie nach jedem Neustart nicht manuell hinzufügen müssen.
    -   `IdentityFile ~/.ssh/id_rsa`: Gibt den Pfad zu Ihrer privaten SSH-Schlüsseldatei an. `~/.ssh/id_rsa` ist der Standardspeicherort für den RSA-Privatschlüssel.

**Im Wesentlichen richtet diese Konfiguration einen Proxy für alle SSH-Verbindungen ein, außer denen im lokalen Netzwerk, und konfiguriert die Schlüsselverwaltung für mehr Komfort.**


```bash
Host 192.168.1.*
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa 
Host * !192.*.*.* !47.*.*.*
    ProxyCommand corkscrew localhost 7890 %h %p
Host *
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa    
```

---

## Conda in Linux löschen

*2025.02.07*

```bash
rm -rf ~/anaconda3
```

Löschen Sie den folgenden Code in `.bashrc`:

```bash
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/lzw/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/lzw/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/home/lzw/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/lzw/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
```

Pfad aktualisieren von:

```bash
export PATH="/usr/local/cuda-12.2/bin:/home/lzw/.local/share/gem/ruby/3.0.0/bin:/home/lzw/anaconda3/bin:/home/lzw/anaconda3/condabin:/home/lzw/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/snap/bin"
```

Zu:

```bash
export PATH="/usr/local/cuda-12.2/bin:/home/lzw/.local/share/gem/ruby/3.0.0/bin:/home/lzw/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/snap/bin"
```
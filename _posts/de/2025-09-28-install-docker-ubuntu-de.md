---
audio: false
generated: true
image: false
lang: de
layout: post
model: anthropic/claude-sonnet-4
title: Anleitung zur Installation von Docker auf Ubuntu
translated: true
type: note
---

Basierend auf der Ausgabe Ihres Ubuntu-Systems haben Sie mehrere Möglichkeiten, Docker zu installieren. Hier ist der empfohlene Ansatz:

## Option 1: Docker Engine installieren (Empfohlen)

Die gebräuchlichste und empfohlene Methode ist die Installation der Docker Engine aus dem offiziellen Repository von Docker:

```bash
# Paketindex aktualisieren
sudo apt update

# Voraussetzungen installieren
sudo apt install apt-transport-https ca-certificates curl software-properties-common

# Den offiziellen GPG-Schlüssel von Docker hinzufügen
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Docker Repository hinzufügen
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Paketindex erneut aktualisieren
sudo apt update

# Docker Engine installieren
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

## Option 2: Schnellinstallation über APT (Einfacher)

Aus den in Ihrem Terminal angezeigten Optionen können Sie verwenden:

```bash
sudo apt install docker.io
```

## Einrichtung nach der Installation

Nach der Installation sollten Sie:

1. **Docker-Dienst starten und aktivieren:**
```bash
sudo systemctl start docker
sudo systemctl enable docker
```

2. **Ihren Benutzer zur Docker-Gruppe hinzufügen** (um Docker ohne sudo ausführen zu können):
```bash
sudo usermod -aG docker $USER
```

Dann melden Sie sich ab und wieder an, oder führen Sie aus:
```bash
newgrp docker
```

3. **Installation überprüfen:**
```bash
docker --version
docker run hello-world
```

## Welche Option sollten Sie wählen?

- **Option 1** bietet Ihnen die neueste Docker-Version direkt von Docker Inc.
- **Option 2** ist einfacher, kann aber eine etwas ältere Version aus den Ubuntu-Repositorys haben

Für die meisten Benutzer ist Option 2 (`sudo apt install docker.io`) völlig in Ordnung und viel einfacher. Der Versionsunterschied ist für den regulären Gebrauch normalerweise minimal.

Möchten Sie, dass ich einen dieser Schritte genauer erkläre?
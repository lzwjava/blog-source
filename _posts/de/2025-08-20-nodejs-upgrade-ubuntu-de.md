---
audio: false
generated: true
image: false
lang: de
layout: post
title: Node.js Upgrade-Leitfaden für Ubuntu
translated: true
type: note
---

Das Upgrade von Node.js auf Ubuntu kann auf verschiedene Weisen durchgeführt werden. Die zuverlässigsten und empfohlenen Methoden sind die Verwendung von **`nvm` (Node Version Manager)** oder des **NodeSource Repositorys**. Nachfolgend finden Sie Schritt-für-Schritt-Anleitungen für beide Methoden.

---

## **Methode 1: Verwendung von NVM (Empfohlen)**
NVM ermöglicht es Ihnen, mehrere Node.js-Versionen einfach zu installieren und zu verwalten.

### 1. NVM installieren
Öffnen Sie ein Terminal und führen Sie aus:
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
```
Laden Sie dann Ihre Shell neu:
```bash
source ~/.bashrc
```
oder
```bash
source ~/.zshrc
```
(jeweils abhängig von Ihrer Shell)

### 2. Die neueste Node.js-Version installieren
Listen Sie die verfügbaren Versionen auf:
```bash
nvm ls-remote
```
Installieren Sie die neueste LTS-Version (für die meisten Benutzer empfohlen):
```bash
nvm install --lts
```
Oder installieren Sie eine spezifische Version (z.B. 20.x):
```bash
nvm install 20
```

### 3. Standardversion festlegen
```bash
nvm alias default 20
```

### 4. Überprüfen
```bash
node -v
npm -v
```

---

## **Methode 2: Verwendung des NodeSource Repositorys**
Diese Methode installiert Node.js systemweit.

### 1. Alte Node.js-Version entfernen (falls über apt installiert)
```bash
sudo apt remove --purge nodejs npm
sudo apt autoremove
```

### 2. NodeSource Repository hinzufügen
Für **Node.js 20.x** (Stand August 2025: LTS):
```bash
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
```
Für **Node.js 22.x** (falls verfügbar):
```bash
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
```

### 3. Node.js installieren
```bash
sudo apt install -y nodejs
```

### 4. Überprüfen
```bash
node -v
npm -v
```

---

## **Methode 3: Verwenden des Ubuntu Standard-Repositorys (Nicht empfohlen)**
Das Standard-Repository von Ubuntu enthält oft veraltete Node.js-Versionen. Wenn Sie es dennoch verwenden möchten:
```bash
sudo apt update
sudo apt install nodejs npm
```
Dies ist jedoch für die Entwicklung **nicht empfohlen**, da die Version meist veraltet ist.

---

## **Welche Methode sollten Sie verwenden?**
- **Verwenden Sie NVM**, wenn Sie einfach zwischen Node.js-Versionen wechseln möchten oder die neuesten Funktionen benötigen.
- **Verwenden Sie NodeSource**, wenn Sie eine systemweite, stabile Installation wünschen.
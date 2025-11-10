---
audio: false
generated: true
image: false
lang: de
layout: post
title: Behebung des APT-GPG-Signaturfehlers
translated: true
type: note
---

Der Fehler, den du siehst, bedeutet, dass APT sich weigert, Updates vom ShiftKey-Repo durchzuführen, weil es die GPG-Signatur nicht verifizieren kann. Du hast zwei einfache Möglichkeiten, dies zu beheben:

---

## 1. **Das fehlerhafte Repository entfernen oder deaktivieren**

Wenn du `https://apt.packages.shiftkey.dev/ubuntu` nicht wirklich benötigst, deaktiviere es einfach:

```bash
# Finde die Datei, die dieses Repository definiert (sie befindet sich in /etc/apt/sources.list.d/)
ls /etc/apt/sources.list.d/shiftkey*

# Entferne sie (ersetze mit dem tatsächlichen Dateinamen)
sudo rm /etc/apt/sources.list.d/shiftkey.packages.shiftkey.dev.list

# Aktualisiere und installiere dann
sudo apt update
sudo apt install pkg-config libssl-dev
```

---

## 2. **Den Signierschlüssel des Repositorys importieren**

Wenn du die Pakete von ShiftKey weiterhin verwenden möchtest, musst du den öffentlichen Schlüssel abrufen und installieren:

```bash
# Lade den GPG-Schlüssel herunter, wandle ihn um und speichere ihn im APT-Schlüsselbund
curl -fsSL https://apt.packages.shiftkey.dev/ubuntu/pubkey.gpg \
  | gpg --dearmor \
  | sudo tee /usr/share/keyrings/shiftkey-archive-keyring.gpg > /dev/null

# Bearbeite die Repo-Datei, sodass sie auf diesen Schlüsselbund verweist.
# Öffne /etc/apt/sources.list.d/shiftkey*.list in deinem Editor und ändere die deb-Zeile in:
#   deb [signed-by=/usr/share/keyrings/shiftkey-archive-keyring.gpg] https://apt.packages.shiftkey.dev/ubuntu any main

# Aktualisiere und installiere dann
sudo apt update
sudo apt install pkg-config libssl-dev
```

---

Sobald APT sich ohne GPG-Fehler aktualisieren kann, kannst du `pkg-config` und `libssl-dev` installieren und dann neu kompilieren:

```bash
cargo clean
cargo run
```
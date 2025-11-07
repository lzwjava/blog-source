---
audio: false
generated: false
image: false
lang: de
layout: post
title: macOS Befehl Steuerung
translated: true
type: post
---

## WiFi

```
networksetup -listallhardwareports
sudo networksetup -setairportpower en0 on
sudo networksetup -setairportpower en0 off
```

## Bluetooth

```
brew install blueutil
blueutil --power 0
blueutil --power 1
```

## Lautstärke

```
# Lautstärke auf 50% setzen
osascript -e 'set volume output volume 50'

# Lautstärke stumm schalten
osascript -e 'set volume with output muted'

# Lautstärke stumm schalten deaktivieren
osascript -e 'set volume without output muted'
```
---
audio: false
generated: true
lang: es
layout: post
title: Control de Comandos de macOS
translated: true
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

## Volumen

```
# Establecer volumen al 50%
osascript -e 'set volume output volume 50'

# Silenciar el volumen
osascript -e 'set volume with output muted'

# Desilenciar el volumen
osascript -e 'set volume without output muted'
```
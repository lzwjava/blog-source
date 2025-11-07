---
audio: false
generated: false
image: false
lang: fr
layout: post
title: Composants de Commande de macOS
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

## Volume

```
# Régler le volume à 50%
osascript -e 'set volume output volume 50'

# Couper le son
osascript -e 'set volume with output muted'

# Rétablir le son
osascript -e 'set volume without output muted'
```
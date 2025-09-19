---
audio: false
generated: false
image: false
lang: hi
layout: post
title: मैकओएस कमांड कंट्रोल
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

## Volume

```
# Volume 50% पर सेट करें
osascript -e 'set volume output volume 50'

# Volume को म्यूट करें
osascript -e 'set volume with output muted'

# Volume को म्यूट से हटाएं
osascript -e 'set volume without output muted'
```
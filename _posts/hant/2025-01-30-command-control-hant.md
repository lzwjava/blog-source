---
audio: false
generated: false
image: false
lang: hant
layout: post
title: MacOS 系統命令
translated: true
type: post
---

## WiFi

```
networksetup -listallhardwareports
sudo networksetup -setairportpower en0 on
sudo networksetup -setairportpower en0 off
```

## 藍牙

```
brew install blueutil
blueutil --power 0
blueutil --power 1
```

## 音量

```
# 將音量設為 50%
osascript -e 'set volume output volume 50'

# 靜音
osascript -e 'set volume with output muted'

# 取消靜音
osascript -e 'set volume without output muted'
```
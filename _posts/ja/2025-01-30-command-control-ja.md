---
audio: false
generated: true
lang: ja
layout: post
title: macOS コマンド コントロール
translated: true
---

## WiFi

```
networksetup -listallhardwareports
sudo networksetup -setairportpower en0 on
sudo networksetup -setairportpower en0 off
```

## ブルートゥース

```
brew install blueutil
blueutil --power 0
blueutil --power 1
```

## ボリューム

```
# ボリュームを50%に設定
osascript -e 'set volume output volume 50'

# ボリュームをミュート
osascript -e 'set volume with output muted'

# ボリュームをミュート解除
osascript -e 'set volume without output muted'
```
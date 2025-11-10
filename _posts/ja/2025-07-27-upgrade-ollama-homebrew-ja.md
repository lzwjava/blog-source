---
audio: false
generated: true
image: false
lang: ja
layout: post
title: HomebrewでOllamaをアップグレード
translated: true
type: note
---

macOSでHomebrewを使用してOllamaを最新バージョン（2025年7月現在v0.10.0）にアップグレードするには、以下の手順に従ってください。

1. Homebrewのformulaeを更新し、利用可能な最新バージョンを認識できるようにします：
   ```
   brew update
   ```

2. Ollamaをアップグレードします：
   ```
   brew upgrade ollama
   ```

3. バージョンを確認してアップグレードを検証します：
   ```
   ollama --version
   ```

バックグラウンドサービスとしてOllamaを実行している場合は、アップグレード後に再起動してください：
```
brew services restart ollama
```

あるいは、手動で実行している場合は、既存のプロセスを停止し、適切なコマンド（例：インストール出力のcaveatsに記載されているもの）で再起動します：
```
OLLAMA_FLASH_ATTENTION="1" OLLAMA_KV_CACHE_TYPE="q8_0" /opt/homebrew/opt/ollama/bin/ollama serve
```

この標準的なプロセス以外に特別なアップグレード手順は必要ありません。

[Ollama Releases](https://github.com/ollama/ollama/releases)
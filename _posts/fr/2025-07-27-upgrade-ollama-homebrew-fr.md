---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Mettre à jour Ollama avec Homebrew
translated: true
type: note
---

Pour mettre à niveau Ollama vers la dernière version (actuellement v0.10.0 en juillet 2025) en utilisant Homebrew sur macOS, suivez ces étapes :

1. Mettez à jour les formules de Homebrew pour vous assurer qu'il connaît les dernières versions disponibles :
   ```
   brew update
   ```

2. Mettez à niveau Ollama spécifiquement :
   ```
   brew upgrade ollama
   ```

3. Vérifiez la mise à niveau en contrôlant la version :
   ```
   ollama --version
   ```

Si vous exécutez Ollama comme un service en arrière-plan, redémarrez-le après la mise à niveau :
```
brew services restart ollama
```

Alternativement, si vous l'exécutez manuellement, arrêtez tout processus existant et redémarrez-le avec votre commande préférée (par exemple, à partir des caveats dans votre sortie d'installation) :
```
OLLAMA_FLASH_ATTENTION="1" OLLAMA_KV_CACHE_TYPE="q8_0" /opt/homebrew/opt/ollama/bin/ollama serve
```

Aucune instruction de mise à niveau spéciale n'est nécessaire au-delà de ce processus standard.

[Ollama Releases](https://github.com/ollama/ollama/releases)
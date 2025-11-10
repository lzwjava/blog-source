---
audio: false
generated: true
lang: fr
layout: post
title: Obtenir le chemin complet d'un fichier sous Ubuntu
translated: true
type: note
---

Sous Ubuntu, vous pouvez obtenir le chemin complet d'un fichier en utilisant les commandes `realpath` ou `readlink -f`. Pour votre exemple avec `geckodriver`, vous pouvez exécuter :

```bash
realpath ./geckodriver
```

ou

```bash
readlink -f ./geckodriver
```

Les deux commandes afficheront le chemin complet, par exemple :

```
/home/lzw/bin/geckodriver
```

La commande `realpath` est simple et couramment utilisée pour cet usage. Si `realpath` n'est pas installé, vous pouvez l'installer avec :

```bash
sudo apt install realpath
```

Alternativement, `readlink -f` est généralement disponible par défaut dans le cadre de coreutils.
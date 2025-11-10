---
audio: false
generated: true
lang: ja
layout: post
title: Ubuntuでのファイルの絶対パスの取得
translated: true
type: note
---

Ubuntuでは、`realpath` または `readlink -f` コマンドを使用してファイルの絶対パスを取得できます。`geckodriver` の例の場合、次のように実行します：

```bash
realpath ./geckodriver
```

または

```bash
readlink -f ./geckodriver
```

どちらも絶対パスを出力します。例：

```
/home/lzw/bin/geckodriver
```

`realpath` コマンドは直感的で、この目的で一般的に使用されます。`realpath` がインストールされていない場合は、次のコマンドでインストールできます：

```bash
sudo apt install realpath
```

あるいは、`readlink -f` は通常 coreutils の一部としてデフォルトで利用可能です。
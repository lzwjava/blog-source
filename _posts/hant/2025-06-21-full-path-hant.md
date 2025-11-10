---
audio: false
generated: true
lang: hant
layout: post
title: 在 Ubuntu 中取得檔案的完整路徑
translated: true
type: note
---

在 Ubuntu 系統中，你可以使用 `realpath` 或 `readlink -f` 指令來取得檔案的完整路徑。以 `geckodriver` 為例，你可以執行：

```bash
realpath ./geckodriver
```

或

```bash
readlink -f ./geckodriver
```

兩者都會輸出完整路徑，例如：

```
/home/lzw/bin/geckodriver
```

`realpath` 指令用法直觀且常用於此用途。如果系統未安裝 `realpath`，你可以透過以下指令安裝：

```bash
sudo apt install realpath
```

另外，`readlink -f` 通常預設已隨 coreutils 套件安裝在系統中。
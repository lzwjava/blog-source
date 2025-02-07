---
audio: true
lang: ja
layout: post
title: OpenWrt リセット
translated: true
---

## Webインターフェースからのリセット

イーサネットケーブルでルータに接続することをお勧めします。リセット後、Wi-FiのSSIDはデフォルト設定に戻ります。これは、予期しないものになる可能性があります。

## コマンドライン（SSH）からのリセット

コマンドラインインターフェース（SSH）を使用して、OpenWrtをデフォルト設定にリセットできます。方法は次のとおりです。

1. SSH経由でOpenWrtルータに接続します。
2. 次のコマンドを実行します。

    ```bash
    root@OpenWrt:~# firstboot
    This will erase all settings and remove any installed packages. Are you sure? [N/y]
    y
    /dev/ubi0_1 is mounted as /overlay, only erasing files
    root@OpenWrt:~# reboot
    ```
3. ルータはデフォルト設定で再起動します。

**コマンドの説明:**

* `firstboot`: このコマンドはリセットプロセスを開始し、すべての設定とインストールされているパッケージを消去します。
* `reboot`: このコマンドは、リセットを適用してルータを再起動します。

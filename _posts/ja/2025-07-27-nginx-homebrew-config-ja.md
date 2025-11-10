---
audio: false
generated: true
image: false
lang: ja
layout: post
title: macOS HomebrewでのNginx設定
translated: true
type: note
---

HomebrewでmacOSにインストールされたNginx（バイナリパス `/opt/homebrew/bin/nginx` で示される）の場合、メイン設定ファイルは通常以下の場所にあります：

```
/opt/homebrew/etc/nginx/nginx.conf
```

このディレクトリには、`servers/` サブディレクトリ内のサーバーブロック（例：`/opt/homebrew/etc/nginx/servers/`）など、他の関連ファイルも含まれています。

お使いのNginxインスタンスが使用している正確な設定ファイルのパスを確認するには、ターミナルで以下のコマンドを実行してください：

```
nginx -t
```

これにより設定がテストされ、使用している `nginx.conf` ファイルへのパスが出力されます。あるいは、`nginx -V` を使用して、設定パスのプレフィックスを含むコンパイル時の詳細を確認することもできます。

もし、Homebrewが `/usr/local` にインストールされる古いIntelベースのMacを使用している場合、パスは `/usr/local/etc/nginx/nginx.conf` になりますが、提供されたバイナリパスは `/opt/homebrew` の場所を確認しています。

**参考文献**  
[Locate the nginx.conf file my nginx is actually using - Stack Overflow](https://stackoverflow.com/questions/19910042/locate-the-nginx-conf-file-my-nginx-is-actually-using)  
[Installing nginx in macOS using homebrew | by Ram - Medium](https://medium.com/@rprprasath05/installing-nginx-in-macos-ventura-using-homebrew-12b87a900a03)  
[Simple Configuration of NGINX on Mac - DEV Community](https://dev.to/arjavdave/simple-configuration-of-nginx-on-mac-3cg3)
---
audio: false
generated: false
image: false
lang: ja
layout: post
title: Brew Upgradeのログ
translated: true
type: note
---

```bash
==> インストール完了処理中
ln -s ../../Cellar/azure-cli/2.68.0/etc/bash_completion.d/az az
ln -s ../Cellar/azure-cli/2.68.0/bin/az az
ln -s ../../../Cellar/azure-cli/2.68.0/share/fish/vendor_completions.d/az.fish az.fish
ln -s ../../../Cellar/azure-cli/2.68.0/share/zsh/site-functions/_az _az
==> 注意事項
zsh補完機能は以下にインストールされました:
  /opt/homebrew/share/zsh/site-functions
==> 概要
🍺  /opt/homebrew/Cellar/azure-cli/2.68.0: 24,507ファイル, 580.4MB
==> `brew cleanup azure-cli`を実行中...
削除中: /opt/homebrew/Cellar/azure-cli/2.67.0_1... (27,401ファイル, 647.1MB)
削除中: /Users/lzwjava/Library/Caches/Homebrew/azure-cli_bottle_manifest--2.67.0_1... (22.5KB)
削除中: /Users/lzwjava/Library/Caches/Homebrew/azure-cli--2.67.0_1... (54MB)
==> 注意事項
==> openjdk
システムのJavaラッパーがこのJDKを見つけるようにするには、以下のようにシンボリックリンクを作成してください:
  sudo ln -sfn /opt/homebrew/opt/openjdk/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk

openjdkはkeg-onlyです。これは/opt/homebrewにシンボリックリンクされていないことを意味し、
macOSが同様のソフトウェアを提供しているため、このソフトウェアを並行してインストールすると
様々な問題を引き起こす可能性があるからです。

PATHでopenjdkを優先する必要がある場合は、以下を実行してください:
  echo 'export PATH="/opt/homebrew/opt/openjdk/bin:$PATH"' >> ~/.zshrc

コンパイラがopenjdkを見つけるようにするには、以下を設定する必要があるかもしれません:
  export CPPFLAGS="-I/opt/homebrew/opt/openjdk/include"
==> ruby
デフォルトでは、gemによってインストールされるバイナリは以下に配置されます:
  /opt/homebrew/lib/ruby/gems/3.4.0/bin

これをPATHに追加することをお勧めします。

rubyはkeg-onlyです。これは/opt/homebrewにシンボリックリンクされていないことを意味し、
macOSが既にこのソフトウェアを提供しているため、別のバージョンを並行してインストールすると
様々な問題を引き起こす可能性があるからです。

PATHでrubyを優先する必要がある場合は、以下を実行してください:
  echo 'export PATH="/opt/homebrew/opt/ruby/bin:$PATH"' >> ~/.zshrc

コンパイラがrubyを見つけるようにするには、以下を設定する必要があるかもしれません:
  export LDFLAGS="-L/opt/homebrew/opt/ruby/lib"
  export CPPFLAGS="-I/opt/homebrew/opt/ruby/include"
==> yt-dlp
zsh補完機能は以下にインストールされました:
  /opt/homebrew/share/zsh/site-functions
==> redis
アップグレード後にredisを再起動するには:
  brew services restart redis
または、バックグラウンドサービスが不要な場合は、以下を実行してください:
  /opt/homebrew/opt/redis/bin/redis-server /opt/homebrew/etc/redis.conf
==> perl
デフォルトでは、brew以外のcpanモジュールはCellarにインストールされます。
モジュールをアップデート後も保持したい場合は、`local::lib`の使用をお勧めします。

以下のように設定できます:
  PERL_MM_OPT="INSTALL_BASE=$HOME/perl5" cpan local::lib
そして以下をシェルプロファイル（~/.profileや~/.zshrcなど）に追加してください:
  eval "$(perl -I$HOME/perl5/lib/perl5 -Mlocal::lib=$HOME/perl5)"
==> awscli
"examples"ディレクトリは以下にインストールされました:
  /opt/homebrew/share/awscli/examples

zsh補完機能と関数は以下にインストールされました:
  /opt/homebrew/share/zsh/site-functions
==> php
ApacheでPHPを有効にするには、httpd.confに以下を追加してApacheを再起動してください:
    LoadModule php_module /opt/homebrew/opt/php/lib/httpd/modules/libphp.so

    <FilesMatch \.php$>
        SetHandler application/x-httpd-php
    </FilesMatch>

最後に、DirectoryIndexにindex.phpが含まれていることを確認してください:
    DirectoryIndex index.php index.html

php.iniとphp-fpm.iniファイルは以下で見つかります:
    /opt/homebrew/etc/php/8.4/

phpを今すぐ起動し、ログイン時に再起動するには:
  brew services start php
または、バックグラウンドサービスが不要な場合は、以下を実行してください:
  /opt/homebrew/opt/php/sbin/php-fpm --nodaemonize
==> nginx
ドキュメントルートは: /opt/homebrew/var/www

デフォルトポートは/opt/homebrew/etc/nginx/nginx.confで8080に設定されているため、
nginxはsudoなしで実行できます。

nginxは/opt/homebrew/etc/nginx/servers/内のすべてのファイルを読み込みます。

アップグレード後にnginxを再起動するには:
  brew services restart nginx
または、バックグラウンドサービスが不要な場合は、以下を実行してください:
  /opt/homebrew/opt/nginx/bin/nginx -g daemon\ off\;
==> git-lfs
インストールを完了するにはgit設定を更新してください:

  # グローバルgit設定を更新
  $ git lfs install

  # システムgit設定を更新
  $ git lfs install --system

zsh補完機能は以下にインストールされました:
  /opt/homebrew/share/zsh/site-functions
==> wireshark
このフォーミュラはデフォルトでコマンドラインユーティリティのみをインストールします。

Wireshark.appはHomebrew Caskでインストールしてください:
  brew install --cask wireshark

利用可能なキャプチャインターフェースのリストが空の場合
（macOSのデフォルト動作）、ChmodBPFをインストールしてください:
  brew install --cask wireshark-chmodbpf
==> doctl
zsh補完機能は以下にインストールされました:
  /opt/homebrew/share/zsh/site-functions
==> azure-cli
zsh補完機能は以下にインストールされました:
  /opt/homebrew/share/zsh/site-functions
```
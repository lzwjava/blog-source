---
audio: false
generated: false
image: false
lang: de
layout: post
title: Das Protokoll des Brau-Upgrades
translated: true
type: note
---

```bash
==> Abschließen
ln -s ../../Cellar/azure-cli/2.68.0/etc/bash_completion.d/az az
ln -s ../Cellar/azure-cli/2.68.0/bin/az az
ln -s ../../../Cellar/azure-cli/2.68.0/share/fish/vendor_completions.d/az.fish az.fish
ln -s ../../../Cellar/azure-cli/2.68.0/share/zsh/site-functions/_az _az
==> Caveats
Zsh-Completion wurden installiert nach:
  /opt/homebrew/share/zsh/site-functions
==> Zusammenfassung
🍺  /opt/homebrew/Cellar/azure-cli/2.68.0: 24.507 Dateien, 580,4 MB
==> Ausführung von `brew cleanup azure-cli`...
Entfernen: /opt/homebrew/Cellar/azure-cli/2.67.0_1... (27.401 Dateien, 647,1 MB)
Entfernen: /Users/lzwjava/Library/Caches/Homebrew/azure-cli_bottle_manifest--2.67.0_1... (22,5 KB)
Entfernen: /Users/lzwjava/Library/Caches/Homebrew/azure-cli--2.67.0_1... (54 MB)
==> Caveats
==> openjdk
Damit die System-Java-Wrapper dieses JDK finden, verlinken Sie es mit
  sudo ln -sfn /opt/homebrew/opt/openjdk/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk

openjdk ist keg-only, was bedeutet, dass es nicht nach /opt/homebrew symlinkt wurde,
weil macOS ähnliche Software bereitstellt und die parallele Installation dieser Software
alle möglichen Probleme verursachen kann.

Wenn Sie openjdk als Erstes in Ihrem PATH benötigen, führen Sie aus:
  echo 'export PATH="/opt/homebrew/opt/openjdk/bin:$PATH"' >> ~/.zshrc

Damit Compiler openjdk finden, müssen Sie möglicherweise setzen:
  export CPPFLAGS="-I/opt/homebrew/opt/openjdk/include"
==> ruby
Standardmäßig werden von gem installierte Binärdateien platziert in:
  /opt/homebrew/lib/ruby/gems/3.4.0/bin

Sie sollten dies möglicherweise zu Ihrem PATH hinzufügen.

ruby ist keg-only, was bedeutet, dass es nicht nach /opt/homebrew symlinkt wurde,
weil macOS diese Software bereits bereitstellt und die Installation einer weiteren Version
parallel alle möglichen Probleme verursachen kann.

Wenn Sie ruby als Erstes in Ihrem PATH benötigen, führen Sie aus:
  echo 'export PATH="/opt/homebrew/opt/ruby/bin:$PATH"' >> ~/.zshrc

Damit Compiler ruby finden, müssen Sie möglicherweise setzen:
  export LDFLAGS="-L/opt/homebrew/opt/ruby/lib"
  export CPPFLAGS="-I/opt/homebrew/opt/ruby/include"
==> yt-dlp
Zsh-Completion wurden installiert nach:
  /opt/homebrew/share/zsh/site-functions
==> redis
Um redis nach einem Upgrade neu zu starten:
  brew services restart redis
Oder, wenn Sie keinen Hintergrunddienst benötigen, können Sie einfach ausführen:
  /opt/homebrew/opt/redis/bin/redis-server /opt/homebrew/etc/redis.conf
==> perl
Standardmäßig werden nicht über brew installierte cpan-Module in die Cellar installiert. Wenn Sie möchten,
dass Ihre Module über Updates hinweg bestehen bleiben, empfehlen wir die Verwendung von `local::lib`.

Sie können dies wie folgt einrichten:
  PERL_MM_OPT="INSTALL_BASE=$HOME/perl5" cpan local::lib
Und fügen Sie Folgendes zu Ihrem Shell-Profil hinzu, z.B. ~/.profile oder ~/.zshrc
  eval "$(perl -I$HOME/perl5/lib/perl5 -Mlocal::lib=$HOME/perl5)"
==> awscli
Das "examples"-Verzeichnis wurde installiert nach:
  /opt/homebrew/share/awscli/examples

Zsh-Completion und -Funktionen wurden installiert nach:
  /opt/homebrew/share/zsh/site-functions
==> php
Um PHP in Apache zu aktivieren, fügen Sie Folgendes zu httpd.conf hinzu und starten Apache neu:
    LoadModule php_module /opt/homebrew/opt/php/lib/httpd/modules/libphp.so

    <FilesMatch \.php$>
        SetHandler application/x-httpd-php
    </FilesMatch>

Stellen Sie abschließend sicher, dass DirectoryIndex index.php enthält
    DirectoryIndex index.php index.html

Die php.ini- und php-fpm.ini-Dateien befinden sich in:
    /opt/homebrew/etc/php/8.4/

Um php jetzt zu starten und beim Login neu zu starten:
  brew services start php
Oder, wenn Sie keinen Hintergrunddienst benötigen, können Sie einfach ausführen:
  /opt/homebrew/opt/php/sbin/php-fpm --nodaemonize
==> nginx
Docroot ist: /opt/homebrew/var/www

Der Standardport wurde in /opt/homebrew/etc/nginx/nginx.conf auf 8080 gesetzt, damit
nginx ohne sudo ausgeführt werden kann.

nginx lädt alle Dateien in /opt/homebrew/etc/nginx/servers/.

Um nginx nach einem Upgrade neu zu starten:
  brew services restart nginx
Oder, wenn Sie keinen Hintergrunddienst benötigen, können Sie einfach ausführen:
  /opt/homebrew/opt/nginx/bin/nginx -g daemon\ off\;
==> git-lfs
Aktualisieren Sie Ihre git-Konfiguration, um die Installation abzuschließen:

  # Globale git-Konfiguration aktualisieren
  $ git lfs install

  # Systemweite git-Konfiguration aktualisieren
  $ git lfs install --system

Zsh-Completion wurden installiert nach:
  /opt/homebrew/share/zsh/site-functions
==> wireshark
Diese Formel installiert standardmäßig nur die Kommandozeilenprogramme.

Installieren Sie Wireshark.app mit Homebrew Cask:
  brew install --cask wireshark

Wenn Ihre Liste der verfügbaren Erfassungsschnittstellen leer ist
(Standardverhalten von macOS), installieren Sie ChmodBPF:
  brew install --cask wireshark-chmodbpf
==> doctl
Zsh-Completion wurden installiert nach:
  /opt/homebrew/share/zsh/site-functions
==> azure-cli
Zsh-Completion wurden installiert nach:
  /opt/homebrew/share/zsh/site-functions
```
---
audio: true
lang: es
layout: post
title: El Registro de la Actualización de Brew
translated: true
---

==> Finalizando
ln -s ../../Cellar/azure-cli/2.68.0/etc/bash_completion.d/az az
ln -s ../Cellar/azure-cli/2.68.0/bin/az az
ln -s ../../../Cellar/azure-cli/2.68.0/share/fish/vendor_completions.d/az.fish az.fish
ln -s ../../../Cellar/azure-cli/2.68.0/share/zsh/site-functions/_az _az
==> Advertencias
Las compleciones de zsh se han instalado en:
  /opt/homebrew/share/zsh/site-functions
==> Resumen
🍺  /opt/homebrew/Cellar/azure-cli/2.68.0: 24.507 archivos, 580.4MB
==> Ejecutando `brew cleanup azure-cli`...
Eliminando: /opt/homebrew/Cellar/azure-cli/2.67.0_1... (27.401 archivos, 647.1MB)
Eliminando: /Users/lzwjava/Library/Caches/Homebrew/azure_cli_bottle_manifest--2.67.0_1... (22.5KB)
Eliminando: /Users/lzwjava/Library/Caches/Homebrew/azure-cli--2.67.0_1... (54MB)
==> Advertencias
==> openjdk
Para que los wrappers Java del sistema encuentren este JDK, cree un enlace simbólico con
  sudo ln -sfn /opt/homebrew/opt/openjdk/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk

openjdk es solo keg, lo que significa que no se ha creado un enlace simbólico en /opt/homebrew,
porque macOS proporciona software similar e instalar este software en
paralelo puede causar todo tipo de problemas.

Si necesita tener openjdk primero en su PATH, ejecute:
  echo 'export PATH="/opt/homebrew/opt/openjdk/bin:$PATH"' >> ~/.zshrc

Para que los compiladores encuentren openjdk, es posible que deba establecer:
  export CPPFLAGS="-I/opt/homebrew/opt/openjdk/include"
==> ruby
De forma predeterminada, los binarios instalados por gem se colocarán en:
  /opt/homebrew/lib/ruby/gems/3.4.0/bin

Es posible que desee agregar esto a su PATH.

ruby es solo keg, lo que significa que no se ha creado un enlace simbólico en /opt/homebrew,
porque macOS ya proporciona este software e instalar otra versión en
paralelo puede causar todo tipo de problemas.

Si necesita tener ruby primero en su PATH, ejecute:
  echo 'export PATH="/opt/homebrew/opt/ruby/bin:$PATH"' >> ~/.zshrc

Para que los compiladores encuentren ruby, es posible que deba establecer:
  export LDFLAGS="-L/opt/homebrew/opt/ruby/lib"
  export CPPFLAGS="-I/opt/homebrew/opt/ruby/include"
==> yt-dlp
Las compleciones de zsh se han instalado en:
  /opt/homebrew/share/zsh/site-functions
==> redis
Para reiniciar redis después de una actualización:
  brew services restart redis
O, si no quiere/necesita un servicio en segundo plano, simplemente ejecute:
  /opt/homebrew/opt/redis/bin/redis-server /opt/homebrew/etc/redis.conf
==> perl
De forma predeterminada, los módulos cpan no elaborados se instalan en Cellar. Si desea
que sus módulos persistan a través de las actualizaciones, recomendamos usar `local::lib`.

Puede configurarlo de la siguiente manera:
  PERL_MM_OPT="INSTALL_BASE=$HOME/perl5" cpan local::lib
Y agregue lo siguiente a su perfil de shell, por ejemplo, ~/.profile o ~/.zshrc
  eval "$(perl -I$HOME/perl5/lib/perl5 -Mlocal::lib=$HOME/perl5)"
==> awscli
El directorio "examples" se ha instalado en:
  /opt/homebrew/share/awscli/examples

Las funciones y las compleciones de zsh se han instalado en:
  /opt/homebrew/share/zsh/site-functions
==> php
Para habilitar PHP en Apache, agregue lo siguiente a httpd.conf y reinicie Apache:
    LoadModule php_module /opt/homebrew/opt/php/lib/httpd/modules/libphp.so

    <FilesMatch \.php$>
        SetHandler application/x-httpd-php
    </FilesMatch>

Finalmente, verifique que DirectoryIndex incluya index.php
    DirectoryIndex index.php index.html

El archivo php.ini y php-fpm.ini se pueden encontrar en:
    /opt/homebrew/etc/php/8.4/

Para iniciar php ahora y reiniciar al iniciar sesión:
  brew services start php
O, si no quiere/necesita un servicio en segundo plano, simplemente ejecute:
  /opt/homebrew/opt/php/sbin/php-fpm --nodaemonize
==> nginx
El docroot es: /opt/homebrew/var/www

El puerto predeterminado se ha establecido en /opt/homebrew/etc/nginx/nginx.conf en 8080 para que
nginx pueda ejecutarse sin sudo.

nginx cargará todos los archivos en /opt/homebrew/etc/nginx/servers/.

Para reiniciar nginx después de una actualización:
  brew services restart nginx
O, si no quiere/necesita un servicio en segundo plano, simplemente ejecute:
  /opt/homebrew/opt/nginx/bin/nginx -g daemon\ off\;
==> git-lfs
Actualice su configuración de git para finalizar la instalación:

  # Actualizar la configuración global de git
  $ git lfs install

  # Actualizar la configuración del sistema git
  $ git lfs install --system

Las compleciones de zsh se han instalado en:
  /opt/homebrew/share/zsh/site-functions
==> wireshark
Esta fórmula solo instala las utilidades de línea de comandos de forma predeterminada.

Instale Wireshark.app con Homebrew Cask:
  brew install --cask wireshark

Si su lista de interfaces de captura disponibles está vacía
(comportamiento predeterminado de macOS), instale ChmodBPF:
  brew install --cask wireshark-chmodbpf
==> doctl
Las compleciones de zsh se han instalado en:
  /opt/homebrew/share/zsh/site-functions
==> azure-cli
Las compleciones de zsh se han instalado en:
  /opt/homebrew/share/zsh/site-functions


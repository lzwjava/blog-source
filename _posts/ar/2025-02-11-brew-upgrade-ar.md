---
audio: false
generated: false
image: false
lang: ar
layout: post
title: سجل ترقية بريو
translated: true
type: note
---

```bash
==> الانتهاء
ln -s ../../Cellar/azure-cli/2.68.0/etc/bash_completion.d/az az
ln -s ../Cellar/azure-cli/2.68.0/bin/az az
ln -s ../../../Cellar/azure-cli/2.68.0/share/fish/vendor_completions.d/az.fish az.fish
ln -s ../../../Cellar/azure-cli/2.68.0/share/zsh/site-functions/_az _az
==> ملاحظات
تم تثبيت إكمالات zsh في:
  /opt/homebrew/share/zsh/site-functions
==> الملخص
🍺  /opt/homebrew/Cellar/azure-cli/2.68.0: 24,507 ملف، 580.4 ميجابايت
==> تشغيل `brew cleanup azure-cli`...
جاري الإزالة: /opt/homebrew/Cellar/azure-cli/2.67.0_1... (27,401 ملف، 647.1 ميجابايت)
جاري الإزالة: /Users/lzwjava/Library/Caches/Homebrew/azure-cli_bottle_manifest--2.67.0_1... (22.5 كيلوبايت)
جاري الإزالة: /Users/lzwjava/Library/Caches/Homebrew/azure-cli--2.67.0_1... (54 ميجابايت)
==> ملاحظات
==> openjdk
لكي تجد أغلفة Java النظامية هذا JDK، أنشئ رابطًا رمزيًا باستخدام
  sudo ln -sfn /opt/homebrew/opt/openjdk/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk

openjdk هو keg-only، مما يعني أنه لم يتم إنشاء رابط رمزي له في /opt/homebrew،
لأن macOS يوفر برنامجًا مشابهًا وتثبيت هذا البرنامج بالتزامن يمكن أن يسبب جميع أنواع المشاكل.

إذا كنت بحاجة إلى أن يكون openjdk أولًا في مسار PATH الخاص بك، فشغّل:
  echo 'export PATH="/opt/homebrew/opt/openjdk/bin:$PATH"' >> ~/.zshrc

لكي تجد المترجمات openjdk قد تحتاج إلى تعيين:
  export CPPFLAGS="-I/opt/homebrew/opt/openjdk/include"
==> ruby
بشكل افتراضي، سيتم وضع الملفات الثنائية المثبتة بواسطة gem في:
  /opt/homebrew/lib/ruby/gems/3.4.0/bin

قد ترغب في إضافة هذا إلى مسار PATH الخاص بك.

ruby هو keg-only، مما يعني أنه لم يتم إنشاء رابط رمزي له في /opt/homebrew،
لأن macOS يوفر هذا البرنامج بالفعل وتثبيت نسخة أخرى بالتزامن يمكن أن يسبب جميع أنواع المشاكل.

إذا كنت بحاجة إلى أن يكون ruby أولًا في مسار PATH الخاص بك، فشغّل:
  echo 'export PATH="/opt/homebrew/opt/ruby/bin:$PATH"' >> ~/.zshrc

لكي تجد المترجمات ruby قد تحتاج إلى تعيين:
  export LDFLAGS="-L/opt/homebrew/opt/ruby/lib"
  export CPPFLAGS="-I/opt/homebrew/opt/ruby/include"
==> yt-dlp
تم تثبيت إكمالات zsh في:
  /opt/homebrew/share/zsh/site-functions
==> redis
لإعادة تشغيل redis بعد التحديث:
  brew services restart redis
أو، إذا كنت لا تريد/تحتاج خدمة خلفية، يمكنك فقط تشغيل:
  /opt/homebrew/opt/redis/bin/redis-server /opt/homebrew/etc/redis.conf
==> perl
بشكل افتراضي، يتم تثبيت وحدات cpan غير المخمرة في Cellar. إذا كنت تريد
أن تبقى وحداتك عبر التحديثات، نوصي باستخدام `local::lib`.

يمكنك إعداد ذلك كالتالي:
  PERL_MM_OPT="INSTALL_BASE=$HOME/perl5" cpan local::lib
وأضف ما يلي إلى ملف تعريف shell الخاص بك، مثلاً ~/.profile أو ~/.zshrc
  eval "$(perl -I$HOME/perl5/lib/perl5 -Mlocal::lib=$HOME/perl5)"
==> awscli
تم تثبيت دليل "examples" في:
  /opt/homebrew/share/awscli/examples

تم تثبيت إكمالات ووظائف zsh في:
  /opt/homebrew/share/zsh/site-functions
==> php
لتمكين PHP في Apache، أضف ما يلي إلى httpd.conf وأعد تشغيل Apache:
    LoadModule php_module /opt/homebrew/opt/php/lib/httpd/modules/libphp.so

    <FilesMatch \.php$>
        SetHandler application/x-httpd-php
    </FilesMatch>

أخيرًا، تحقق من أن DirectoryIndex يتضمن index.php
    DirectoryIndex index.php index.html

يمكن العثور على ملفي php.ini و php-fpm.ini في:
    /opt/homebrew/etc/php/8.4/

لبدء تشغيل php الآن وإعادة التشغيل عند تسجيل الدخول:
  brew services start php
أو، إذا كنت لا تريد/تحتاج خدمة خلفية، يمكنك فقط تشغيل:
  /opt/homebrew/opt/php/sbin/php-fpm --nodaemonize
==> nginx
الدليل الجذري للمستندات هو: /opt/homebrew/var/www

تم تعيين المنفذ الافتراضي في /opt/homebrew/etc/nginx/nginx.conf إلى 8080 حتى
يتمكن nginx من التشغيل بدون sudo.

سيقوم nginx بتحميل جميع الملفات في /opt/homebrew/etc/nginx/servers/.

لإعادة تشغيل nginx بعد التحديث:
  brew services restart nginx
أو، إذا كنت لا تريد/تحتاج خدمة خلفية، يمكنك فقط تشغيل:
  /opt/homebrew/opt/nginx/bin/nginx -g daemon\ off\;
==> git-lfs
قم بتحديث إعدادات git الخاصة بك لإنهاء التثبيت:

  # تحديث إعدادات git العامة
  $ git lfs install

  # تحديث إعدادات git النظامية
  $ git lfs install --system

تم تثبيت إكمالات zsh في:
  /opt/homebrew/share/zsh/site-functions
==> wireshark
هذه الصيغة تثبت فقط أدوات سطر الأوامر بشكل افتراضي.

قم بتثبيت Wireshark.app باستخدام Homebrew Cask:
  brew install --cask wireshark

إذا كانت قائمة واجهات الالتقاط المتاحة فارغة
(السلوك الافتراضي لنظام macOS)، قم بتثبيت ChmodBPF:
  brew install --cask wireshark-chmodbpf
==> doctl
تم تثبيت إكمالات zsh في:
  /opt/homebrew/share/zsh/site-functions
==> azure-cli
تم تثبيت إكمالات zsh في:
  /opt/homebrew/share/zsh/site-functions
```
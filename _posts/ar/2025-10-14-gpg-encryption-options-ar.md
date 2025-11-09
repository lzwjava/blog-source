---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: خيارات تشفير GPG موضحة
translated: true
type: note
---

### شرح خيارات GPG

أمر `gpg` (GNU Privacy Guard) هو أداة للتشفير وفك التشفير وإدارة المفاتيح. الخيارات التي ذكرتها تُستخدم عادةً معًا لتشفير الملفات لمستلم محدد. إليك ما يعنيه كل واحد منها:

- **`--homedir <directory>`**: يحدد دليل البداية لـ GnuPG (الإعداد الافتراضي هو `~/.gnupg`). هذا هو المكان الذي يخزن فيه GPG حلقات المفاتيح وملفات التكوين والبيانات الأخرى. يتجاوز هذا الخيار متغير البيئة `GNUPGHOME` وهو مفيد لعزل عمليات GPG في موقع مخصص (على سبيل المثال، لملفات تعريف متعددة أو لأسباب أمنية). يجب توفيره في سطر الأوامر.

- **`-e` (أو `--encrypt`)**: يشفر بيانات الإدخال باستخدام تشفير المفتاح العام. هذا هو الوضع الأساسي للتشفير غير المتماثل، حيث يتم تشفير البيانات باستخدام المفتاح العام للمستلم. يمكن دمجه مع خيارات أخرى مثل التوقيع.

- **`-r <user-id>` (أو `--recipient <user-id>`)**: يحدد المستلم (المستلمين) للتشفير. يمكن أن يكون `<user-id>` معرّف مفتاح، أو بريدًا إلكترونيًا، أو اسمًا مرتبطًا بالمفتاح العام. سوف يستخدم GPG المفتاح العام المقابل لتشفير البيانات. يمكن سرد عدة مستلمين للتشفير الجماعي.

#### مثال للاستخدام
قد يبدو أمر شائع يجمع بين هذه الخيارات كما يلي:
```
gpg --homedir /path/to/custom/dir -e -r recipient@example.com inputfile.txt
```
هذا يشفر الملف `inputfile.txt` من أجل `recipient@example.com` باستخدام المفاتيح من `/path/to/custom/dir`، وينتج الملف `inputfile.txt.gpg`.

للحصول على التفاصيل الكاملة، قم بتشغيل `gpg --help` أو راجع صفحة الدليل (man page).

[ArchWiki: GnuPG](https://wiki.archlinux.org/title/GnuPG)  
[GPG Cheat Sheet](https://irtfweb.ifa.hawaii.edu/~lockhart/gpg/)  
[GPG Command in Linux](https://www.tutorialspoint.com/unix_commands/gpg.htm)
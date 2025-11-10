---
audio: false
generated: true
image: false
lang: ar
layout: post
title: خدمات الشبكة في نظامي التشغيل macOS وLinux
translated: true
type: note
---

### خدمات الشبكة والمصطلحات ذات الصلة في macOS وLinux

يبدو أن هذه المصطلحات تشير بشكل أساسي إلى أسماء خدمات الشبكة، التي يتم تعريفها غالبًا في ملف `/etc/services` على أنظمة macOS وLinux. يقوم هذا الملف بربط أسماء الخدمات بأرقام المنافذ والبروتوكولات لخدمات الشبكة القياسية. بعضها خدمات مسجلة رسميًا في IANA، بينما البعض الآخر أسماء مستعارة أو أسماء بروتوكولات شائعة الاستخدام في تكوينات النظام. فيما يلي شرح لكل منها، بناءً على الاستخدام القياسي في macOS (الذي يستخدم قاعدة تشبه BSD) وتوزيعات Linux.

- **service**: هذا مصطلح عام للبرامج الخفيفة (daemons) أو العمليات في النظام في كل من macOS (عبر launchd) وLinux (عبر systemd أو أنظمة init). إنه ليس خدمة شبكة محددة في `/etc/services`، ولكن قد يشير إلى أمر "service" في Linux لإدارة نصوص تشغيل SysV init القديمة، أو بشكل واسع إلى أي خدمة خلفية.

- **ircu**: يشير إلى خدمة IRCU (Internet Relay Chat Undernet)، وهي نوع مختلف من برنامج خادم IRC. يستخدم المنفذ 6667/tcp (وأحيانًا udp). في Linux، قد يرتبط ببرامج IRD الخفيفة مثل حزم ircu أو undernet-ircu. لا يتم تثبيته مسبقًا بشكل شائع على macOS أو Linux الحديث، ولكنه متاح عبر المنافذ أو الحزم لخوادم الدردشة.

- **complex-link**: على الأرجح خطأ إملائي أو متغير لـ "commplex-link"، وهي خدمة شبكة مسجلة على المنفذ 5001/tcp. تُستخدم لربط تعدد الإرسال في الاتصالات (مثلًا، في بعض أدوات الشبكات أو البروتوكولات). في macOS، يرتبط هذا المنفذ بتكوين AirPort/Time Capsule أو أدوات إدارة الموجه (مثل أجهزة Netgear أو Apple). في Linux، قد يظهر في قواعد جدار الحماية أو ناتج netstat لأغراض مماثلة.

- **dhcpc**: اسم مستعار لخدمة عميل DHCP، باستخدام المنفذ 68/udp (المعروف أيضًا باسم bootpc). هذا هو جانب العميل في DHCP للحصول على عناوين IP ديناميكيًا. في Linux، يتم التعامل معه بواسطة عمليات مثل dhclient أو dhcpcd؛ في macOS، بواسطة configd أو bootpd (وضع العميل).

- **zeroconf**: يشير إلى Zero Configuration Networking (Zeroconf)، وهو بروتوكول لاكتشاف الخدمات تلقائيًا دون تكوين يدوي. في macOS، يتم تنفيذه كـ Bonjour (باستخدام mDNS على المنفذ 5353/udp). في Linux، يكون عادةً Avahi (أيضًا على المنفذ 5353/udp). يُستخدم لاكتشاف الطابعات والمشاركات وخدمات الشبكة المحلية الأخرى.

- **ntp**: خدمة Network Time Protocol لمزامنة ساعات النظام عبر الشبكة. تستخدم المنفذ 123/udp (وأحيانًا tcp). في Linux، يتم التعامل معها بواسطة ntpd أو chronyd؛ في macOS، بواسطة ntpd أو برنامج المزامنة الزمنية المدمج.

- **http**: بروتوكول HyperText Transfer Protocol، أساس اتصالات الويب. يستخدم المنفذ 80/tcp (أحيانًا udp). في كل من macOS وLinux، يرتبط بخوادم الويب مثل Apache (httpd) أو Nginx.

- **ssh**: بروتوكول Secure Shell للوصول الآمن عن بُعد ونقل الملفات. يستخدم المنفذ 22/tcp (و udp/sctp). في Linux وmacOS، البرنامج الخفي هو sshd، يتم تمكينه عبر تفضيلات النظام أو ملف sshd_config.

- **hgvirtgrp**: يبدو أن هذا إشارة إلى مجموعة مستخدمين تتعلق بالافتراضية، ربما متغير أو خطأ إملائي لمجموعة "libvirt" في Linux (مثل مجموعة libvirt أو libvirt-qemu). في Linux، إضافة المستخدمين إلى مجموعة libvirt تمنحهم صلاحية إدارة الأجهزة الظاهرية عبر libvirt (لـ KVM/QEMU). في macOS، يستخدم الافتراضية إطار عمل Hypervisor، ولكن لا توجد مجموعة قياسية "hgvirtgrp" — قد تشير إلى مجموعات مخصصة لأدوات الافتراضية/المحاكاة الافتراضية مثل QEMU أو Virt-Manager. إذا كانت مجموعة محددة، فتحقق من ملف `/etc/group` على نظامك.

عادة ما تُرى هذه في أدوات مثل `netstat`، أو `lsof`، أو تكوينات جدار الحماية (مثل pf على macOS، iptables/ufw على Linux). للحصول على تعريفات دقيقة، استشر ملف `/etc/services` في نظامك أو سجل منافذ IANA.

**المراجع**  
[Service Name and Transport Protocol Port Number Registry](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml)  
[what is an open port with a commplex-link? - Apple Community](https://discussions.apple.com/thread/7747034)  
[Running virt-manager and libvirt on macOS](https://www.arthurkoziel.com/running-virt-manager-and-libvirt-on-macos/)
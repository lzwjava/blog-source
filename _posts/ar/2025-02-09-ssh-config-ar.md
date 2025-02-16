---
audio: true
lang: ar
layout: post
title: تكوين SSH
translated: true
---

هذا ملف `ssh-config` يحدد سلوك عميل SSH. دعونا نفصل كل جزء:

-   `Host * !192.*.*.*`: هذا القسم ينطبق على جميع المضيفين *باستثناء* أولئك الذين يتطابقون مع نمط `192.*.*.*` (عادةً، عناوين الشبكة المحلية).
    -   `ProxyCommand corkscrew localhost 7890 %h %p`: هذا هو الجزء الرئيسي. يوصي SSH باستخدام برنامج `corkscrew` للاتصال بالمضيف الهدف.
        -   `corkscrew`: أداة تسمح لك بتونل SSH عبر HTTP أو HTTPS.
        -   `localhost 7890`: يحدد عنوان خادم الوكيل (`localhost`) وميناء (`7890`). هذا يفترض أن لديك خادم وكيل يعمل على جهازك المحلي، يستمع على الميناء 7890 (مثل Shadowsocks، وكيل SOCKS، أو حل تونل آخر).
        -   `%h`: متغير SSH خاص يوسع إلى اسم المضيف الهدف الذي تحاول الاتصال به.
        -   `%p`: متغير SSH آخر يوسع إلى الميناء الهدف (عادةً 22 لـ SSH).
    - في ملخص، هذا كتلة `Host` تهيئ SSH لاستخدام الوكيل `corkscrew` لجميع الاتصالات *باستثناء* تلك إلى الشبكة المحلية.

-   `Host *`: هذا القسم ينطبق على *جميع* المضيفين.
    -   `UseKeychain yes`: على macOS، هذا يوصي SSH بحفظ استرجاع مفاتيح SSH من Keychain، فلا تحتاج إلى إدخال كلمة المرور كل مرة.
    -   `AddKeysToAgent yes`: هذا يضيف مفاتيح SSH تلقائيًا إلى وكيل SSH، فلا تحتاج إلى إضافتها يدويًا بعد كل إعادة تشغيل.
    -   `IdentityFile ~/.ssh/id_rsa`: يحدد مسار ملف مفتاح SSH الخاص بك. `~/.ssh/id_rsa` هو الموقع الافتراضي لمفتاح RSA الخاص.

**في جوهره، هذه التكوين يهيئ وكيلًا لجميع الاتصالات SSH باستثناء تلك على الشبكة المحلية، ويهيئ إدارة المفاتيح للسهولة.**

```bash
Host 192.168.1.*
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
Host * !192.*.*.* !47.*.*.*
    ProxyCommand corkscrew localhost 7890 %h %p
Host *
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
```
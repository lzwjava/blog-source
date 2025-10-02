---
audio: false
generated: false
image: false
lang: ar
layout: post
title: Netplan، Systemd، SSH، تنظيف Conda
translated: true
---

### جدول المحتويات

1. [تجربة Netplan](#trying-netplan)
   - تسبب تكوين IP الثابت في فقدان SSH
   - يتطلب الوصول المادي لإعادة الضبط
   - تم تعديل ملف محلل DNS للنظام

2. [خدمة Systemd](#systemd-service)
   - تكوين خدمة استدلال LLM المحلية
   - إعداد واجهة ويب لنماذج LLM
   - إنشاء خدمة أداة الوكيل القائمة على القواعد
   - استخدام أوامر systemctl لإدارة الخدمة

3. [تكوين SSH](#ssh-configuration)
   - وكيل الاتصالات الخارجية عبر corkscrew
   - استبعاد الشبكة المحلية من الوكيل
   - إدارة مفاتيح SSH عبر keychain و agent
   - تحديد موقع المفتاح الخاص الافتراضي

4. [حذف Conda في Linux](#delete-conda-in-linux)
   - إزالة دليل تثبيت conda بالكامل
   - حذف رمز تهيئة conda من bashrc
   - تحديث متغير بيئة PATH
   - إزالة الثنائيات conda من مسار النظام


## تجربة Netplan

جربت التكوين أدناه لتعيين عنوان IP ثابت لجهاز Ubuntu. أقوم بتشغيل OpenWebUI و llama.cpp على ذلك الخادم.

```
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: no
      addresses:
        - 192.168.1.128/32
      gateway4: 192.168.1.1
```

بعد تشغيل `sudo netplan apply`، لم يعد من الممكن الوصول إلى الجهاز عبر `ssh lzw@192.168.1.128`.

تم استخدام لوحة المفاتيح والماوس لتسجيل الدخول إلى الجهاز، وحذف الملفات، واستعادة الإعدادات.

تم تغيير `/etc/resolv.conf`.

---

## خدمة Systemd

*2025.02.13*

## تكوين خدمة خادم LLaMA

يشرح هذا القسم كيفية إعداد خدمة systemd لتشغيل خادم LLaMA، الذي يوفر إمكانات استدلال LLM المحلية.

```bash
sudo emacs /etc/systemd/system/llama.service
sudo systemctl daemon-reload
sudo systemctl enable llama.service
journalctl -u llama.service
```

```bash
[Unit]
Description=Llama Script

[Service]
ExecStart=/home/lzw/Projects/llama.cpp/build/bin/llama-server -m /home/lzw/Projects/llama.cpp/models/DeepSeek-R1-Distill-Qwen-14B-Q5_K_M.gguf --port 8000  --ctx-size 2048 --batch-size 512 --n-gpu-layers 49 --threads 8 --parallel 1
WorkingDirectory=/home/lzw/Projects/llama.cpp
StandardOutput=append:/home/lzw/llama.log
StandardError=append:/home/lzw/llama.err
Restart=always
User=lzw

[Install]
WantedBy=default.target
```

## تكوين خدمة Open WebUI

يشرح هذا القسم كيفية إعداد خدمة systemd لتشغيل Open WebUI، الذي يوفر واجهة ويب للتفاعل مع نماذج LLM.

```bash
[Unit]
Description=Open Web UI Service

[Service]
ExecStart=/home/lzw/.local/bin/open-webui serve
WorkingDirectory=/home/lzw
StandardOutput=append:/home/lzw/open-webui.log
StandardError=append:/home/lzw/open-webui.err
Restart=always
User=lzw

[Install]
WantedBy=default.target
```

```bash
sudo systemctl enable openwebui.service
sudo systemctl daemon-reload
sudo systemctl start  openwebui.service
```

## تكوين خدمة Clash

يشرح هذا القسم كيفية إعداد خدمة systemd لتشغيل Clash، وهي أداة وكيل قائمة على القواعد.

```bash
[Unit]
Description=Clash Service

[Service]
ExecStart=/home/lzw/clash-linux-386-v1.17.0/clash-linux-386
WorkingDirectory=/home/lzw/clash-linux-386-v1.17.0
StandardOutput=append:/home/lzw/clash.log
StandardError=append:/home/lzw/clash.err
Restart=always
User=lzw

[Install]
WantedBy=default.target
```

```bash
# إنشاء ملف الخدمة
sudo emacs /etc/systemd/system/clash.service 

# إعادة تحميل systemd daemon
sudo systemctl daemon-reload

# تمكين وبدء الخدمة
sudo systemctl enable clash.service
sudo systemctl start clash.service
sudo systemctl restart clash.service

# التحقق من الحالة
sudo systemctl status clash.service
```

---

## تكوين SSH

*2025.02.09*

يقوم ملف `ssh-config` هذا بتكوين سلوك عميل SSH. دعنا نقسم كل جزء:

-   `Host * !192.*.*.*`: ينطبق هذا القسم على جميع المضيفين *باستثناء* أولئك الذين يطابقون النمط `192.*.*.*` (عادةً، عناوين الشبكة المحلية).
    -   `ProxyCommand corkscrew localhost 7890 %h %p`: هذا هو الجزء الأساسي. يخبر SSH باستخدام برنامج `corkscrew` للاتصال بالمضيف الهدف.
        -   `corkscrew`: أداة تسمح لك بتوجيه اتصالات SSH عبر وكلاء HTTP أو HTTPS.
        -   `localhost 7890`: يحدد عنوان خادم الوكيل (`localhost`) ومنفذه (`7890`). يفترض هذا أن لديك خادم وكيل يعمل على جهازك المحلي، ويستمع على المنفذ 7890 (مثل Shadowsocks، وكيل SOCKS، أو حل نفق آخر).
        -   `%h`: متغير SSH خاص يتوسع إلى اسم المضيف الهدف الذي تحاول الاتصال به.
        -   `%p`: متغير SSH آخر يتوسع إلى المنفذ الهدف (عادةً 22 لـ SSH).
    - باختصار، تقوم كتلة `Host` هذه بتكوين SSH لاستخدام وكيل `corkscrew` لجميع الاتصالات *باستثناء* تلك المتصلة بالشبكة المحلية.

-   `Host *`: ينطبق هذا القسم على *جميع* المضيفين.
    -   `UseKeychain yes`: على macOS، يخبر هذا SSH بتخزين واسترداد مفاتيح SSH من Keychain الخاص بك، لذلك لا تضطر إلى إدخال كلمة المرور الخاصة بك في كل مرة.
    -   `AddKeysToAgent yes`: يضيف هذا مفاتيح SSH الخاصة بك تلقائيًا إلى وكيل SSH، لذلك لا تضطر إلى إضافتها يدويًا بعد كل إعادة تشغيل.
    -   `IdentityFile ~/.ssh/id_rsa`: يحدد المسار إلى ملف مفتاح SSH الخاص بك. `~/.ssh/id_rsa` هو الموقع الافتراضي للمفتاح الخاص RSA.

**في الأساس، يقوم هذا التكوين بإعداد وكيل لجميع اتصالات SSH باستثناء تلك الموجودة على الشبكة المحلية، ويقوم بتكوين إدارة المفاتيح للراحة.**


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

---

## حذف Conda في Linux

*2025.02.07*

```bash
rm -rf ~/anaconda3
```

احذف الرمز أدناه في `.bashrc`:

```bash
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/lzw/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/lzw/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/home/lzw/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/lzw/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
```

تحديث المسار من:

```bash
export PATH="/usr/local/cuda-12.2/bin:/home/lzw/.local/share/gem/ruby/3.0.0/bin:/home/lzw/anaconda3/bin:/home/lzw/anaconda3/condabin:/home/lzw/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/snap/bin"
```

إلى:

```bash
export PATH="/usr/local/cuda-12.2/bin:/home/lzw/.local/share/gem/ruby/3.0.0/bin:/home/lzw/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/snap/bin"
```
---
audio: true
generated: false
lang: ar
layout: post
title: تكوين ملف باشرش في لينكس
translated: true
---

هذا الملف `bashrc` يُهيئ بيئة نظام التشغيل باش في لينكس.  وهو يُخصّص المُطوّع، ويُنشئ اختصارات، ويدير إعدادات الوكيل، ويتكامل مع أدوات مثل جيت. فيما يلي تفصيل للإعدادات الرئيسية:

**1. الإعدادات الأساسية:**

   - `HISTCONTROL=ignoreboth`: يتجاهل الأوامر المُكرّرة والأوامر التي تبدأ بمسافة في السجل.
   - `shopt -s histappend`: يُضيف إدخالات السجل الجديدة إلى ملف السجل.
   - `HISTSIZE=1000`: يُعيّن عدد إدخالات السجل التي يجب الاحتفاظ بها في الذاكرة.
   - `HISTFILESIZE=2000`: يُعيّن الحجم الأقصى لملف السجل.
   - `shopt -s checkwinsize`: يُحدّث حجم نافذة المحطة الطرفية.

**2. مُطوّع ملون:**

   - يُهيئ مُطوّع أوامر ملون إذا كانت المحطة الطرفية تدعمه.

**3. عنوان النافذة:**

   - يُعيّن عنوان نافذة المحطة الطرفية لعرض المستخدم الحالي، والجهاز المُضيف، ودليل العمل.

**4. ألوان الدليل:**

   - يُمكّن الإخراج الملون لأمر `ls` إذا كان `dircolors` متوفراً.

**5. الاختصارات:**

   - `alias ll='ls -alF'`: يعرض جميع الملفات بمعلومات مُفصّلة.
   - `alias la='ls -A'`: يعرض جميع الملفات، بما في ذلك الملفات المخفية.
   - `alias l='ls -CF'`: يعرض الملفات في أعمدة.
   - `alias alert='notify-send ...'`: يُرسل إشعاراً لسطح المكتب بعد انتهاء الأمر.

**6. ملف اختصارات باش:**

   - يتضمن ملفاً منفصلاً للاختصارات المُخصّصة (`~/.bash_aliases`).

**7. إكمال باش:**

   - يُمكّن إكمال باش إذا كان متوفراً.

**8. تهيئة المسار:**

   - `export PATH=...`: يُضيف العديد من الدلائل إلى متغير بيئة `PATH`، بما في ذلك تلك الخاصة بـ CUDA، و Ruby gems، والملفات الثنائية المحلية، والملفات الثنائية للنظام.

**9. إدارة الوكيل:**

   - `export GLOBAL_PROXY='127.0.0.1:7890'`: يُعرّف متغيراً لعنوان خادم الوكيل.
   - `function start_proxy { ... }`: يُعيّن متغيرات بيئة `HTTP_PROXY`, `HTTPS_PROXY`, `http_proxy`, `https_proxy`, و `ALL_PROXY` لاستخدام الوكيل المُحدّد.
   - `function start_proxy_without_prefix { ... }`: مشابه لـ `start_proxy`، لكنه يُعيّن متغيرات الوكيل بدون بادئة `http://`.
   - `function stop_proxy { ... }`: يُلغي تعيين متغيرات الوكيل، مما يُعطل الوكيل بشكل فعال.
   - `export NO_PROXY="localhost,127.0.0.1,.example.com,::1"`: يُحدّد المُضيفات التي يجب أن تتجاوز الوكيل.

**10. وكيل جيت:**

    - `function start_git_proxy { ... }`: يُهيئ جيت لاستخدام الوكيل العام لاتصالات HTTP و HTTPS.
    - `function stop_git_proxy { ... }`: يُلغي تعيين إعدادات وكيل جيت.

**11. وكيل افتراضي:**

    - `start_proxy`: يبدأ الوكيل افتراضيًا.
    - `start_git_proxy`: يبدأ وكيل جيت افتراضيًا.

**12. اختصارات بايثون:**

   - `alias python=python3`: يُعيّن `python` لاستخدام `python3`.
   - `alias pip=pip3`: يُعيّن `pip` لاستخدام `pip3`.

**13. اختصارات جيت مسج AI:**

   - `function gpa { ... }`: يُنشئ اختصار `gpa` لتشغيل البرنامج النصي لبايثون `gitmessageai.py` باستخدام واجهة برمجة تطبيقات Mistral والسماح بالسحب والدفع.
   - `function gca { ... }`: يُنشئ اختصار `gca` لتشغيل نفس البرنامج النصي بدون دفع التغييرات.
   - `function gm { ... }`: يُنشئ اختصار `gm` لتشغيل البرنامج النصي نفسه وطباعة رسالة الالتزام فقط.

**14. دفع جيت مع السحب وإعادة القاعدة:**

   - `function gpp { ... }`: يحاول دفع التغييرات، وإذا فشل، يحاول السحب مع إعادة القاعدة ثم الدفع مرة أخرى.

**15. فحص الوكيل قبل التنفيذ:**

   - `preexec() { ... }`: يتم تنفيذ هذه الدالة قبل كل أمر.  تتحقق مما إذا كان الأمر موجودًا في قائمة الأوامر المعتمدة على الشبكة. إذا كان الأمر كذلك، وإذا تم تعيين أي متغيرات وكيل، فإنه يعرض إعدادات الوكيل.
   - `local network_commands=( ... )`: هذه المصفوفة تسرد الأوامر التي تعتبر معتمدة على الشبكة.
   - `display_proxy() { ... }`: تعرض هذه الدالة إعدادات الوكيل الحالية.

**16. دالة فحص الوكيل:**

   - `function checkproxy { ... }`: تعرض إعدادات وكيل HTTP و HTTPS الحالية، بالإضافة إلى إعدادات وكيل جيت.


```bash
case $- in
    *i*) ;;
      *) return;;
esac

HISTCONTROL=ignoreboth
shopt -s histappend
HISTSIZE=1000
HISTFILESIZE=2000
shopt -s checkwinsize

[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

case "$TERM" in
    xterm-color|*-256color) color_prompt=yes;;
esac

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
	color_prompt=yes
    else
	color_prompt=
    fi
fi

if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
unset color_prompt force_color_prompt

case "$TERM" in
xterm*|rxvt*)
    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
    ;;
*)
    ;;
esac

if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi



export PATH="/usr/local/cuda-12.2/bin:/home/lzw/.local/share/gem/ruby/3.0.0/bin:/home/lzw/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/snap/bin"

export GLOBAL_PROXY='127.0.0.1:7890'

function start_proxy {
    export HTTP_PROXY="http://$GLOBAL_PROXY"
    export HTTPS_PROXY="http://$GLOBAL_PROXY"
    export http_proxy="http://$GLOBAL_PROXY"
    export https_proxy="http://$GLOBAL_PROXY"
    export HTTP_PROXY_REQUEST_FULLURI=false
    export HTTPS_PROXY_REQUEST_FULLURI=false
    export ALL_PROXY=$http_proxy
}

function start_proxy_without_prefix {
    export http_proxy=$GLOBAL_PROXY
		export HTTP_PROXY=$GLOBAL_PROXY
		export https_proxy=$GLOBAL_PROXY
    export HTTPS_PROXY=$GLOBAL_PROXY
    export HTTP_PROXY_REQUEST_FULLURI=false
    export HTTPS_PROXY_REQUEST_FULLURI=false
		export ALL_PROXY=$http_proxy
}

function stop_proxy {
    export http_proxy=
		export HTTP_PROXY=
		export https_proxy=
    export HTTPS_PROXY=
    export HTTP_PROXY_REQUEST_FULLURI=true
    export HTTPS_PROXY_REQUEST_FULLURI=true
		export ALL_PROXY=		
}

export NO_PROXY="localhost,127.0.0.1,.example.com,::1"


function start_git_proxy {
  git config --global http.proxy $GLOBAL_PROXY
  git config --global https.proxy $GLOBAL_PROXY
}

function stop_git_proxy {
  git config --global --unset http.proxy
  git config --global --unset https.proxy
}

start_proxy
start_git_proxy

alias python=python3
alias pip=pip3

function gpa {
  python ~/bin/gitmessageai.py --api mistral --allow-pull-push
}

function gca {
  python ~/bin/gitmessageai.py --no-push
}

function gm {
  python ~/bin/gitmessageai.py --only-message
}

function gpp {
  git push || {
    echo "Push failed, attempting pull and merge"
    git pull --rebase || {
      echo "Pull failed, please resolve conflicts manually"
      return 1
    }
    git push || {
      echo "Push failed after pull, please resolve conflicts manually"
      return 1
    }
  }
}

preexec() {
    local network_commands=(
        "gpa"
        "git"
        "ssh"
        "scp"
        "sftp"
        "rsync"
        "curl"
        "wget"
        "apt"
        "yum"
        "dnf"
        "npm"
        "yarn"
        "pip"
        "pip3"
        "gem"
        "cargo"
        "docker"
        "kubectl"
        "ping"
        "traceroute"
        "netstat"
        "ss"
        "ip"
        "ifconfig"
        "dig"
        "nslookup"
        "nmap"
        "telnet"
        "ftp"
        "nc"
        "tcpdump"
        "adb"
        "bundle"
        "brew"
        "cpanm"
        "bundle exec jekyll"
        "make"
        "python"
        "glcoud"
    )

    local cmd
    cmd=$(echo "$1" | awk '{print $1}')

    display_proxy() {
        echo -e "🚀 **Proxy Settings Detected:**"

        [ -n "$HTTP_PROXY" ] && echo "   - HTTP_PROXY: $HTTP_PROXY"
        [ -n "$HTTPS_PROXY" ] && echo "   - HTTPS_PROXY: $HTTPS_PROXY"

        echo ""
    }

    for network_cmd in "${network_commands[@]}"; do
        if [[ "$1" == "$network_cmd"* ]]; then
            if [ -n "$HTTP_PROXY" ] || [ -n "$http_proxy" ] || \
               [ -n "$HTTPS_PROXY" ] || [ -n "$https_proxy" ] || \
               [ -n "$ALL_PROXY" ] || [ -n "$all_proxy" ]; then
                
                display_proxy
            fi
            break
        fi
    done
}

function checkproxy {
  echo "HTTP_PROXY: $HTTP_PROXY"
  echo "HTTPS_PROXY: $HTTPS_PROXY"
  echo "Git HTTP Proxy:"
  git config --get http.proxy
  echo "Git HTTPS Proxy:"
  git config --get https.proxy
}

```

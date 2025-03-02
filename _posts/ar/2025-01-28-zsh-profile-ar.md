---
audio: false
generated: true
lang: ar
layout: post
title: ملف تعريف Zsh
translated: true
---

```markdown
يهدف ملف تعريف zsh هذا إلى تحسين تجربة سطر الأوامر، مع التركيز على تكوينات الوكيل، وإدماج Git، والأسماء المستعارة المفيدة. تفصيل الأقسام التالية ميزاته:

**1. تكوين PATH:**

   - `export PATH=...`: تعيين هذا السطر المتغير البيئي `PATH`، الذي يخبر الصدفة أين يجب البحث عن ملفات التنفيذ. يتضمن مجلدات مختلفة مثل تلك الخاصة بـ Java، وRuby، وHomebrew، وPython، وFlutter، وGoogle Cloud SDK. يضمن ذلك أنه يمكن تشغيل الأوامر من هذه الأدوات مباشرة من الطرفية.

**2. إدارة الوكيل:**

   - `export GLOBAL_PROXY='127.0.0.1:7890'`: يعرّف هذا متغيرًا `GLOBAL_PROXY` يحتوي على عنوان خادم الوكيل.
   - `function start_proxy { ... }`: يعيّن هذا الدالة المتغيرات البيئية `HTTP_PROXY`، و`HTTPS_PROXY`، و`http_proxy`، و`https_proxy`، و`ALL_PROXY` لاستخدام الوكيل المحدد. كما يعطيل طلبات URI الكاملة للأوكيل.
   - `function start_proxy_without_prefix { ... }`: مماثل لـ `start_proxy`، ولكنه يعيّن المتغيرات الوكيل بدون البادئة `http://`.
   - `function stop_proxy { ... }`: يعيّن هذا الدالة المتغيرات الوكيل، مما يعطل الوكيل بفعالية. كما يمكّن طلبات URI الكاملة للأوكيل.
   - `export NO_PROXY="localhost,127.0.0.1,.example.com,::1"`: يحدد هذا قائمة من المضيفين التي يجب أن تتجاوز الوكيل.

**3. وكيل Git:**

   - `function start_git_proxy { ... }`: يكوّن هذا الدالة git لاستخدام الوكيل العام للاتصالات HTTP وHTTPS.
   - `function stop_git_proxy { ... }`: يعيّن هذا الدالة إعدادات الوكيل git.

**4. إدماج Homebrew:**

   - `eval "$(/opt/homebrew/bin/brew shellenv)"`: يدمج هذا السطر Homebrew في بيئة الصدفة، مما يتيح لك استخدام أوامر Homebrew.

**5. الأسماء المستعارة المريحة:**

   - `alias gpa='python ~/bin/gitmessageai.py --api mistral'`: ينشئ هذا اسمًا مستعارًا `gpa` لتشغيل نص Python `gitmessageai.py` مع API mistral.
   - `alias gca='python ~/bin/gitmessageai.py --no-push'`: ينشئ هذا اسمًا مستعارًا `gca` لتشغيل نفس النص بدون دفع التغييرات.
   - `alias gm='python ~/bin/gitmessageai.py --only-message'`: ينشئ هذا اسمًا مستعارًا `gm` لتشغيل نفس النص وطباعة رسالة الالتزام فقط.
   - `alias gpam=/usr/local/bin/git-auto-commit`: ينشئ هذا اسمًا مستعارًا `gpam` لتشغيل النص `git-auto-commit`.
   - `alias rougify=/Users/lzwjava/projects/rouge/bin/rougify`: ينشئ هذا اسمًا مستعارًا `rougify` لتشغيل النص `rougify`.

**6. شهادة SSL:**

   - `export SSL_CERT_FILE=~/bin/cacert.pem`: يعيّن هذا مسار ملف شهادة SSL مخصص.

**7. تحديث Homebrew التلقائي:**

   - `export HOMEBREW_NO_AUTO_UPDATE=1`: يعطّل هذا تحديثات Homebrew التلقائية.

**8. فحص الوكيل قبل التنفيذ:**

   - `preexec() { ... }`: يتم تنفيذ هذه الدالة قبل كل أمر. يتحقق مما إذا كان الأمر في قائمة الأوامر المعتمدة على الشبكة. إذا كان كذلك، وإذا كان أي من المتغيرات الوكيل معيّن، فإنه يعرض إعدادات الوكيل.
   - `local network_commands=( ... )`: تسرد هذه المصفوفة الأوامر التي يُعتبر أنها معتمدة على الشبكة.
   - `display_proxy() { ... }`: تعرض هذه الدالة إعدادات الوكيل الحالية.

**9. إكمال Google Cloud SDK:**

   - `if [ -f '/Users/lzwjava/bin/google-cloud-sdk/completion.zsh.inc' ]; then . '/Users/lzwjava/bin/google-cloud-sdk/completion.zsh.inc'; fi`: يمكّن هذا السطر إكمال أمر الصدفة لـ gcloud.

**10. مفاتيح API والأوراق الاعتمادية:**

    - `export GOOGLE_APPLICATION_CREDENTIALS="/Users/lzwjava/bin/graphite-ally-445108-k3-035f0952219d.json"`: يعيّن المسار إلى أوراق الاعتماد الخدمية لـ Google Cloud.
    - `export DEEPSEEK_API_KEY="xxx"`: يعيّن مفتاح API DeepSeek.
    - `export MISTRAL_API_KEY="xxx"`: يعيّن مفتاح API Mistral.
    - `export DYLD_LIBRARY_PATH=$(brew --prefix curl)/lib`: يعيّن مسار مكتبة الروابط الديناميكية لـ curl.
    - `export SPEECH_ENDPOINT="https://ai-lzwjava-5596.cognitiveservices.azure.com/"`: يعيّن نقطة نهاية الخطاب لـ Azure.
    - `export DO_API_KEY="xxx"`: يعيّن مفتاح API Digital Ocean.
    - `export GEMINI_API_KEY="xxx"`: يعيّن مفتاح API Gemini.

**11. بيئة Conda:**

    - `conda activate base`: يفعّل البيئة الأساسية لـ conda.

**ملخصًا، يوفر ملف تعريف zsh هذا إعدادًا شاملاً لمطور، يتضمن:**

- إدارة الوكيل السهلة مع وظائف لبدء وإيقاف الأوكيل.
- تكوين وكيل Git.
- إدماج مع Homebrew.
- الأسماء المستعارة المريحة للمهام الشائعة.
- فحص الوكيل قبل التنفيذ للأوامر المعتمدة على الشبكة.
- مفاتيح API والأوراق الاعتمادية لمختلف الخدمات.
- تفعيل بيئة Conda.

يُعد هذا الملف لتيسير سير عمل المستخدم وجعل إدارة الأدوات والخدمات المختلفة أسهل.

```bash
export PATH=/opt/homebrew/Cellar/openjdk@17/17.0.13/libexec/openjdk.jdk/Contents/Home/bin:/opt/homebrew/opt/ruby/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Users/lzwjava/Library/Python/3.9/bin:/Library/TeX/texbin:/Users/lzwjava/bin:/Users/lzwjava/platform-tools:/Users/lzwjava/Downloads/google-cloud-sdk/bin:/Users/lzwjava/bin/flutter/bin:/opt/homebrew/lib/ruby/gems/3.3.0/bin:/opt/homebrew/Cellar/llama.cpp/4539/bin:/Users/lzwjava/bin/google-cloud-sdk/bin

# /opt/homebrew/opt/openjdk/bin

# /opt/homebrew/Cellar/openjdk@17/17.0.13/libexec/openjdk.jdk/Contents/Home/bin

export GLOBAL_PROXY='127.0.0.1:7890'
# export GLOBAL_PROXY='http://192.168.1.1:7890'

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

eval "$(/opt/homebrew/bin/brew shellenv)"

start_proxy
# start_git_proxy

# alias python3=/opt/homebrew/bin/python3
# alias pip3=/opt/homebrew/bin/pip3
# alias pip=pip3

alias gpa='python ~/bin/gitmessageai.py --api mistral'
alias gca='python ~/bin/gitmessageai.py --no-push'
alias gm='python ~/bin/gitmessageai.py --only-message'

alias gpam=/usr/local/bin/git-auto-commit

# bundle exec jekyll serve
export SSL_CERT_FILE=~/bin/cacert.pem

alias rougify=/Users/lzwjava/projects/rouge/bin/rougify

# git config --global core.editor "code --wait"
# git config --global -e

export HOMEBREW_NO_AUTO_UPDATE=1

# Function to check and display proxy settings before certain commands
# Function to check and display proxy settings before certain commands
preexec() {
    # Define network-dependent commands
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
        # Add more commands as needed
    )

    # Extract the first word (command) from the command line
    local cmd
    cmd=$(echo "$1" | awk '{print $1}')

    # Function to display proxy variables
    display_proxy() {
        echo -e "🚀 **Proxy Settings Detected:**"

        [ -n "$HTTP_PROXY" ] && echo "   - HTTP_PROXY: $HTTP_PROXY"
        [ -n "$HTTPS_PROXY" ] && echo "   - HTTPS_PROXY: $HTTPS_PROXY"

        echo ""
    }

    # Check if the command is network-dependent
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

# The next line enables shell command completion for gcloud.
if [ -f '/Users/lzwjava/bin/google-cloud-sdk/completion.zsh.inc' ]; then . '/Users/lzwjava/bin/google-cloud-sdk/completion.zsh.inc'; fi

export GOOGLE_APPLICATION_CREDENTIALS="/Users/lzwjava/bin/graphite-ally-445108-k3-035f0952219d.json"

export DEEPSEEK_API_KEY="xxx"

export MISTRAL_API_KEY="xxx"

export DYLD_LIBRARY_PATH=$(brew --prefix curl)/lib

export SPEECH_ENDPOINT="https://ai-lzwjava-5596.cognitiveservices.azure.com/"

export DO_API_KEY="xxx"

export GEMINI_API_KEY="xxx"

conda activate base
```
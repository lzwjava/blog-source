---
audio: false
generated: false
image: false
lang: fr
layout: post
title: Profil Zsh
translated: true
type: post
---

Ce profil zsh vise à améliorer l'expérience en ligne de commande, avec un accent sur les configurations de proxy, l'intégration de Git et des alias pratiques. Les sections suivantes détaillent ses fonctionnalités :

**1. Configuration du PATH :**

   - `export PATH=...`: Cette ligne définit la variable d'environnement `PATH`, qui indique au shell où chercher les fichiers exécutables. Elle inclut divers répertoires comme ceux pour Java, Ruby, Homebrew, Python, Flutter et le SDK Google Cloud. Cela garantit que les commandes de ces outils peuvent être exécutées directement depuis le terminal.

**2. Gestion des Proxys :**

   - `export GLOBAL_PROXY='127.0.0.1:7890'`: Cette ligne définit une variable `GLOBAL_PROXY` contenant l'adresse du serveur proxy.
   - `function start_proxy { ... }`: Cette fonction définit les variables d'environnement `HTTP_PROXY`, `HTTPS_PROXY`, `http_proxy`, `https_proxy` et `ALL_PROXY` pour utiliser le proxy spécifié. Elle désactive également les requêtes d'URI complètes pour les proxys.
   - `function start_proxy_without_prefix { ... }`: Similaire à `start_proxy`, mais définit les variables de proxy sans le préfixe `http://`.
   - `function stop_proxy { ... }`: Cette fonction annule la définition des variables de proxy, désactivant ainsi le proxy. Elle réactive également les requêtes d'URI complètes pour les proxys.
   - `export NO_PROXY="localhost,127.0.0.1,.example.com,::1"`: Cette ligne spécifie une liste d'hôtes qui doivent contourner le proxy.

**3. Proxy Git :**

   - `function start_git_proxy { ... }`: Cette fonction configure git pour utiliser le proxy global pour les connexions HTTP et HTTPS.
   - `function stop_git_proxy { ... }`: Cette fonction annule la configuration du proxy git.

**4. Intégration de Homebrew :**

   - `eval "$(/opt/homebrew/bin/brew shellenv)"`: Cette ligne intègre Homebrew dans l'environnement du shell, permettant l'utilisation des commandes Homebrew.

**5. Alias de Convenance :**

   - `alias gpa='python ~/bin/gitmessageai.py --api mistral'`: Cette ligne crée un alias `gpa` pour exécuter un script Python `gitmessageai.py` avec l'API mistral.
   - `alias gca='python ~/bin/gitmessageai.py --no-push'`: Cette ligne crée un alias `gca` pour exécuter le même script sans pousser les modifications.
   - `alias gm='python ~/bin/gitmessageai.py --only-message'`: Cette ligne crée un alias `gm` pour exécuter le même script et n'afficher que le message de commit.
   - `alias gpam=/usr/local/bin/git-auto-commit`: Cette ligne crée un alias `gpam` pour exécuter le script `git-auto-commit`.
   - `alias rougify=/Users/lzwjava/projects/rouge/bin/rougify`: Cette ligne crée un alias `rougify` pour exécuter le script `rougify`.

**6. Certificat SSL :**

   - `export SSL_CERT_FILE=~/bin/cacert.pem`: Cette ligne définit le chemin vers un fichier de certificat SSL personnalisé.

**7. Mise à Jour Automatique de Homebrew :**

   - `export HOMEBREW_NO_AUTO_UPDATE=1`: Cette ligne désactive les mises à jour automatiques de Homebrew.

**8. Vérification du Proxy avant Exécution :**

   - `preexec() { ... }`: Cette fonction est exécutée avant chaque commande. Elle vérifie si la commande fait partie d'une liste de commandes dépendant du réseau. Si c'est le cas, et si des variables de proxy sont définies, elle affiche les paramètres de proxy.
   - `local network_commands=( ... )`: Ce tableau liste les commandes considérées comme dépendant du réseau.
   - `display_proxy() { ... }`: Cette fonction affiche les paramètres de proxy actuels.

**9. Complétion des Commandes Google Cloud SDK :**

   - `if [ -f '/Users/lzwjava/bin/google-cloud-sdk/completion.zsh.inc' ]; then . '/Users/lzwjava/bin/google-cloud-sdk/completion.zsh.inc'; fi`: Cette ligne active la complétion des commandes shell pour gcloud.

**10. Clés API et Informations d'Identification :**

    - `export GOOGLE_APPLICATION_CREDENTIALS="/Users/lzwjava/bin/graphite-ally-445108-k3-035f0952219d.json"`: Définit le chemin vers les informations d'identification du compte de service Google Cloud.
    - `export DEEPSEEK_API_KEY="xxx"`: Définit la clé API de DeepSeek.
    - `export MISTRAL_API_KEY="xxx"`: Définit la clé API de Mistral.
    - `export DYLD_LIBRARY_PATH=$(brew --prefix curl)/lib`: Définit le chemin de la bibliothèque dynamique pour curl.
    - `export SPEECH_ENDPOINT="https://ai-lzwjava-5596.cognitiveservices.azure.com/"`: Définit le point de terminaison de la parole Azure.
    - `export DO_API_KEY="xxx"`: Définit la clé API de Digital Ocean.
    - `export GEMINI_API_KEY="xxx"`: Définit la clé API de Gemini.

**11. Environnement Conda :**

    - `conda activate base`: Active l'environnement conda de base.

**En résumé, ce profil zsh offre une configuration complète pour un développeur, incluant :**

- Une gestion facile des proxys avec des fonctions pour démarrer et arrêter les proxys.
- La configuration du proxy git.
- L'intégration avec Homebrew.
- Des alias pratiques pour les tâches courantes.
- Des vérifications de proxy avant l'exécution pour les commandes dépendant du réseau.
- Des clés API et des informations d'identification pour divers services.
- L'activation de l'environnement conda.

Ce profil est conçu pour rationaliser le flux de travail de l'utilisateur et faciliter la gestion des divers outils et services de développement.

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

# Fonction pour vérifier et afficher les paramètres de proxy avant certaines commandes
# Fonction pour vérifier et afficher les paramètres de proxy avant certaines commandes
preexec() {
    # Définir les commandes dépendant du réseau
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
        # Ajouter d'autres commandes si nécessaire
    )

    # Extraire le premier mot (commande) de la ligne de commande
    local cmd
    cmd=$(echo "$1" | awk '{print $1}')

    # Fonction pour afficher les variables de proxy
    display_proxy() {
        echo -e "🚀 **Paramètres de Proxy Détectés:**"

        [ -n "$HTTP_PROXY" ] && echo "   - HTTP_PROXY: $HTTP_PROXY"
        [ -n "$HTTPS_PROXY" ] && echo "   - HTTPS_PROXY: $HTTPS_PROXY"

        echo ""
    }

    # Vérifier si la commande dépend du réseau
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

# La ligne suivante active la complétion des commandes shell pour gcloud.
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
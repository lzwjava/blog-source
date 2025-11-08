---
audio: false
generated: false
image: true
lang: fr
layout: post
title: Afficher les Paramètres du Proxy Avant d'Exécuter des Commandes
translated: true
type: post
---

<div style="text-align: center;">  
    <img class="responsive" src="/assets/images/preexec/pe1.png" alt="prexec" />  
</div>

Vivre en Chine ou travailler dans des entreprises qui utilisent des VPN et des proxies peut compliquer le développement de logiciels. Oublier de configurer ces paramètres entraîne souvent des problèmes de connectivité. Pour simplifier votre flux de travail, j'ai créé un simple script Zsh avec l'aide de ChatGPT qui affiche automatiquement vos paramètres de proxy lorsque vous exécutez des commandes spécifiques dépendantes du réseau.

## Pourquoi afficher les paramètres du proxy ?

Les proxys et les VPN sont essentiels pour accéder de manière sécurisée à des ressources externes. Afficher vos paramètres de proxy avant d'exécuter des commandes dépendantes du réseau vous aide à identifier et à résoudre rapidement les problèmes de connectivité.

## Le Script

Ce script utilise la fonction `preexec` de Zsh pour vérifier si la commande à venir dépend du réseau. Si c'est le cas et que les variables d'environnement du proxy sont définies, il affiche les paramètres actuels du proxy.

```bash
# Fonction pour vérifier et afficher les paramètres de proxy avant certaines commandes
preexec() {
    # Définir les commandes dépendantes du réseau
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
        # Ajouter plus de commandes au besoin
    )
```

    # Extraire le premier mot (commande) de la ligne de commande
    local cmd
    cmd=$(echo "$1" | awk '{print $1}')

    # Fonction pour afficher les variables de proxy
    display_proxy() {
        echo -e "\n🚀 Paramètres de proxy détectés :"

```bash
[ -n "$HTTP_PROXY" ] && echo "   - HTTP_PROXY: $HTTP_PROXY"
[ -n "$http_proxy" ] && echo "   - http_proxy: $http_proxy"
[ -n "$HTTPS_PROXY" ] && echo "   - HTTPS_PROXY: $HTTPS_PROXY"
[ -n "$https_proxy" ] && echo "   - https_proxy: $https_proxy"
[ -n "$ALL_PROXY" ] && echo "   - ALL_PROXY: $ALL_PROXY"
[ -n "$all_proxy" ] && echo "   - all_proxy: $all_proxy"
```

```bash
echo ""
```

```bash
    # Vérifie si la commande dépend du réseau
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
```

## Configuration du Script dans Zsh

### 1. Ouvrez votre fichier `.zshrc`

Utilisez votre éditeur de texte préféré pour ouvrir le fichier de configuration `.zshrc`. Par exemple :

```bash
nano ~/.zshrc
```

### 2. Ajouter la fonction `preexec`

Collez le script ci-dessus à la fin du fichier.

### 3. Enregistrer et fermer

Appuyez sur `CTRL + O` pour enregistrer et `CTRL + X` pour quitter.

### 4. Appliquer les modifications

Rechargez votre fichier `.zshrc` pour appliquer immédiatement la nouvelle configuration :

```bash
source ~/.zshrc
```

## Tester la configuration

### 1. Avec Proxy Activé

Définissez une variable de proxy temporairement et exécutez une commande dépendante du réseau en utilisant `pip` :

```bash
export HTTP_PROXY="http://127.0.0.1:7890"
pip install selenium beautifulsoup4 urllib3
```

Sortie attendue :

```

🚀 Paramètres de proxy détectés :
   - HTTP_PROXY : http://127.0.0.1:7890
   - http_proxy : 127.0.0.1:7890
   - HTTPS_PROXY : 127.0.0.1:7890
   - https_proxy : 127.0.0.1:7890
   - ALL_PROXY : 127.0.0.1:7890
   - all_proxy : 127.0.0.1:7890

Collecting selenium
  Téléchargement de selenium-4.x.x-py2.py3-none-any.whl (xxx kB)
Collecting beautifulsoup4
  Téléchargement de beautifulsoup4-4.x.x-py3-none-any.whl (xxx kB)
Collecting urllib3
  Téléchargement de urllib3-1.x.x-py2.py3-none-any.whl (xxx kB)
...
```

### 2. Sans Proxy Activé

Définissez la variable de proxy et exécutez la même commande `pip` :

```bash
unset HTTP_PROXY
pip install selenium beautifulsoup4 urllib3
```

Sortie attendue :

```
Collecting selenium
  Téléchargement de selenium-4.x.x-py2.py3-none-any.whl (xxx kB)
Collecting beautifulsoup4
  Téléchargement de beautifulsoup4-4.x.x-py3-none-any.whl (xxx kB)
Collecting urllib3
  Téléchargement de urllib3-1.x.x-py2.py3-none-any.whl (xxx kB)
...
```

*(Aucune notification de proxy ne devrait apparaître.)*

### 3. Commande Non-Network

Exécutez une commande locale comme `ls` :

```bash
ls
```

Sortie attendue :

```
[Liste des fichiers et répertoires]
```

*(Aucune notification de proxy ne devrait apparaître.)*

## Personnalisation

- Étendre `network_commands` : Ajoutez toutes les commandes supplémentaires dépendantes du réseau au tableau `network_commands`.

- Gérer les alias : Assurez-vous que tous les alias pour les commandes dépendantes du réseau sont inclus dans la liste `network_commands`.

  ```bash
  alias gpa='git push all'
  ```

 Ajoutez `"gpa"` au tableau `network_commands` pour déclencher des notifications de proxy lors de l'utilisation de cet alias.

- Améliorez la visibilité avec les couleurs :

 Pour une meilleure visibilité, notamment dans les terminaux encombrés, vous pouvez ajouter de la couleur aux notifications du proxy :

  ```bash
  # Ajoutez les codes de couleur en haut de votre fichier .zshrc
  GREEN='\033[0;32m'
  NC='\033[0m' # Pas de couleur
  ```

  display_proxy() {
      echo -e "\n${GREEN}🚀 Paramètres de proxy détectés :${NC}"

```bash
[ -n "$HTTP_PROXY" ] && echo "   - HTTP_PROXY: $HTTP_PROXY"
[ -n "$http_proxy" ] && echo "   - http_proxy: $http_proxy"
[ -n "$HTTPS_PROXY" ] && echo "   - HTTPS_PROXY: $HTTPS_PROXY"
[ -n "$https_proxy" ] && echo "   - https_proxy: $https_proxy"
[ -n "$ALL_PROXY" ] && echo "   - ALL_PROXY: $ALL_PROXY"
[ -n "$all_proxy" ] && echo "   - all_proxy: $all_proxy"
```

```bash
      echo ""
  }
```

## Conclusion

La gestion des paramètres de proxy est essentielle pour un développement logiciel fluide dans des environnements réseau restreints. Ce script Zsh garantit que vous êtes toujours informé de vos configurations de proxy lors de l'exécution de commandes nécessitant un accès réseau, améliorant ainsi votre flux de travail et l'efficacité de la résolution des problèmes.

Bon Codage ! 🚀
---
audio: false
generated: true
lang: fr
layout: post
title: Paramétrage du proxy APT dans Ubuntu
translated: true
type: note
---

Pour vérifier si `apt` utilise un proxy dans Ubuntu, suivez ces étapes :

1. **Vérifier le fichier de configuration APT** :
   - Ouvrez le fichier de configuration APT situé dans `/etc/apt/apt.conf` ou `/etc/apt/apt.conf.d/` (les fichiers dans ce répertoire, comme `70debconf` ou `proxy.conf`, peuvent contenir les paramètres de proxy).
   - Utilisez une commande comme :
     ```bash
     sudo cat /etc/apt/apt.conf
     ```
     ou
     ```bash
     sudo grep -r Proxy /etc/apt/apt.conf.d/
     ```
   - Cherchez des lignes comme :
     ```
     Acquire::http::Proxy "http://proxy-server:port";
     Acquire::https::Proxy "https://proxy-server:port";
     Acquire::ftp::Proxy "ftp://proxy-server:port";
     ```
     Si ces lignes existent, `apt` est configuré pour utiliser un proxy.

2. **Vérifier les variables d'environnement** :
   - `apt` peut utiliser les paramètres de proxy définis dans les variables d'environnement comme `http_proxy`, `https_proxy` ou `ftp_proxy`.
   - Exécutez :
     ```bash
     env | grep -i proxy
     ```
   - Si vous voyez une sortie comme `http_proxy=http://proxy-server:port`, `apt` peut utiliser ces paramètres.

3. **Vérifier les paramètres de proxy système** :
   - Si vous utilisez un environnement de bureau (par exemple, GNOME), vérifiez les paramètres de proxy système :
     - Allez dans *Paramètres > Réseau > Proxy* ou similaire, selon votre environnement de bureau.
     - Ces paramètres peuvent s'appliquer à `apt` si aucun proxy spécifique à APT n'est configuré.

4. **Tester APT avec une commande** :
   - Exécutez une commande `apt` et observez le comportement :
     ```bash
     sudo apt update
     ```
   - Si `apt` se connecte via un proxy, vous pourriez voir des délais, des messages d'erreur spécifiques ou des logs liés au proxy. Pour un débogage plus poussé, utilisez :
     ```bash
     sudo apt -o Debug::pkgProblemResolver=yes update
     ```
     Cela fournit une sortie verbeuse, qui peut indiquer l'utilisation d'un proxy.

5. **Vérifier la présence d'un proxy dans `/etc/environment`** :
   - Certains systèmes définissent les proxys dans `/etc/environment`. Vérifiez avec :
     ```bash
     cat /etc/environment
     ```
   - Cherchez des lignes comme :
     ```
     http_proxy="http://proxy-server:port"
     ```

Si aucune de ces vérifications ne montre de paramètres de proxy, `apt` n'utilise probablement pas de proxy. Pour une confirmation en temps réel, vous pouvez surveiller le trafic réseau avec des outils comme `tcpdump` ou `wireshark` pour voir si les connexions `apt` passent par un serveur proxy.

Si vous avez besoin d'aide pour analyser une sortie spécifique ou configurer un proxy, faites-le moi savoir !
---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Configuration des hôtes de contournement de proxy Ubuntu
translated: true
type: note
---

### Configuration de plusieurs hôtes dans les paramètres de proxy manuel d'Ubuntu

Dans la configuration manuelle du proxy d'Ubuntu (accessible via **Paramètres > Réseau > Proxy de réseau > Manuel**), le champ "Ignorer les hôtes" vous permet de spécifier une liste d'hôtes, de domaines ou de plages d'adresses IP, séparés par des points-virgules, pour contourner le proxy. Ceci est couramment utilisé pour le trafic local comme localhost ou les réseaux internes. Vous ne pouvez pas définir ces adresses comme adresse du *serveur proxy* (qui attend un seul hôte:port), mais elles conviennent parfaitement dans "Ignorer les hôtes".

#### Étapes de configuration via l'interface graphique :
1. Ouvrez les **Paramètres** (recherchez-les dans l'aperçu des Activités).
2. Allez dans **Réseau** > **Proxy de réseau**.
3. Définissez la méthode sur **Manuel**.
4. Dans le champ **Ignorer les hôtes**, entrez votre liste séparée par des points-virgules (sans espaces autour) :
   ```
   localhost;127.0.0.1;192.168.1.1;192.168.2.1;::1
   ```
   - `localhost` : Se résout en adresses de loopback.
   - `127.0.0.1` : Loopback IPv4.
   - `192.168.1.1` et `192.168.2.1` : IP locales spécifiques (ajoutez-en autant que nécessaire).
   - `::1` : Loopback IPv6.

5. Cliquez sur **Appliquer** pour sauvegarder. Ceci s'applique à l'ensemble du système (affecte les applications comme les navigateurs, apt, etc.).

#### Utilisation de wildcards comme `192.168.1.*` :
- Les wildcards directs (par exemple, `192.168.1.*`) ne sont **pas pris en charge** dans le champ "Ignorer les hôtes" — il est conçu pour des hôtes exacts, des suffixes de domaine (par exemple, `*.local`) ou la notation CIDR pour les plages d'IP.
- Utilisez plutôt la **notation CIDR** pour les plages :
  - Pour `192.168.1.*` (toutes les IP du sous-réseau 192.168.1.0/24), utilisez `192.168.1.0/24`.
  - Exemple de liste mise à jour :
    ```
    localhost;127.0.0.1;::1;192.168.1.0/24;192.168.2.1
    ```
  - Pour des réseaux locaux plus larges, ajoutez `10.0.0.0/8;172.16.0.0/12;192.168.0.0/16` (plages privées courantes).

#### Alternative en ligne de commande (pour les scripts ou la précision) :
Si vous préférez le terminal (ou avez besoin d'automatiser), utilisez `gsettings` (Ubuntu moderne) ou modifiez `/etc/environment` pour l'ensemble du système :
- Affichez la liste d'ignorance actuelle :
  ```
  gsettings get org.gnome.system.proxy ignore-hosts
  ```
- Définissez la liste (remplacez par vos valeurs) :
  ```
  gsettings set org.gnome.system.proxy ignore-hosts "['localhost', '127.0.0.1', '::1', '192.168.1.0/24', '192.168.2.1']"
  ```
- Pour la variable d'environnement permanente (affecte certaines applications) : Ajoutez dans `/etc/environment` :
  ```
  no_proxy="localhost,127.0.0.1,::1,192.168.1.0/24,192.168.2.1"
  ```
  Puis redémarrez ou exécutez `source /etc/environment`.

Testez en pingant un hôte listé ou en vérifiant le comportement du proxy dans un navigateur. Si des problèmes surviennent (par exemple, avec des applications spécifiques), la méthode de la variable d'environnement couvre souvent plus de cas.

[Setting up proxy to ignore all local addresses](https://askubuntu.com/questions/11274/setting-up-proxy-to-ignore-all-local-addresses)  
[How to Configure Proxy Settings on Ubuntu](https://phoenixnap.com/kb/ubuntu-proxy-settings)  
[Set a network range in the no_proxy environment variable](https://unix.stackexchange.com/questions/23452/set-a-network-range-in-the-no-proxy-environment-variable)
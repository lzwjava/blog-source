---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Mode Boucle Locale de GPG Pinentry Expliquée
translated: true
type: note
---

### Qu'est-ce que `--pinentry-mode loopback` dans GPG ?

Dans GNU Privacy Guard (GPG), l'option `--pinentry-mode loopback` contrôle la manière dont l'outil gère les invites de phrase de passe lors des opérations de chiffrement, de déchiffrement ou de signature. Pinentry est le mécanisme de GPG pour saisir de manière sécurisée les phrases de passe (comme les mots de passe pour les clés privées), généralement via une boîte de dialogue graphique, une invite de console ou d'autres interfaces.

#### Signification et objectif principal
- **Mode Loopback** : Ceci définit le pinentry sur un comportement de "bouclage" (loopback), où GPG ne lance pas de programme pinentry externe (par exemple, une fenêtre popup graphique). Au lieu de cela, il simule le pinentry en renvoyant les requêtes directement au processus appelant (comme un script ou une application). Cela permet de fournir la phrase de passe de manière programmatique, par exemple via l'entrée standard (STDIN), des variables d'environnement ou des fichiers, sans invites interactives de l'utilisateur.

- **Pourquoi l'utiliser ?**
  - Idéal pour **l'automatisation** : Dans les scripts bash, les pipelines CI/CD (par exemple, GitHub Actions) ou les environnements sans interface graphique (comme les sessions SSH) où une boîte de dialogue graphique ne peut pas apparaître.
  - Évite les blocages ou les échecs dans les configurations non interactives.
  - Depuis GnuPG 2.1.12, le mode loopback est souvent autorisé par défaut avec `--allow-loopback-pinentry`, mais le définir explicitement avec `--pinentry-mode loopback` garantit son utilisation.

- **Exemple d'utilisation courant** :
  Pour déchiffrer un fichier dans un script tout en fournissant la phrase de passe via STDIN :
  ```
  echo "votre-phrase-de-passe" | gpg --pinentry-mode loopback --passphrase-fd 0 --decrypt fichier-chiffre.gpg > fichier-dechiffre.txt
  ```
  - `--passphrase-fd 0` : Lit la phrase de passe depuis le descripteur de fichier 0 (STDIN).
  - Cela demande la phrase une seule fois (ou utilise le cache si configuré) et fonctionne de manière non interactive.

#### Pièges potentiels
- **Note de sécurité** : Le mode loopback peut exposer les phrases de passe dans les listes de processus ou les journaux si elles ne sont pas gérées avec précaution — à utiliser uniquement dans des environnements de confiance.
- **Configuration** : Pour l'activer globalement, ajoutez `allow-loopback-pinentry` dans `~/.gnupg/gpg-agent.conf` et rechargez avec `gpgconf --reload gpg-agent`.
  - S'il demande répétitivement la phrase de passe, vérifiez les délais d'expiration du cache dans `gpg-agent.conf` (par exemple, `default-cache-ttl 3600` pour 1 heure).

Ce mode est particulièrement utile pour les développeurs intégrant GPG dans des outils comme la signature Git ou les flux de travail Emacs.

#### Références
- [How do I use gpg --pinentry-mode loopback in a bash script?](https://stackoverflow.com/questions/77231645/how-do-i-use-gpg-pinentry-mode-loopback-in-a-bash-script)
- [Agent OPTION (GnuPG Manual)](https://www.gnupg.org/documentation/manuals/gnupg/Agent-OPTION.html)
- [GnuPG - ArchWiki](https://wiki.archlinux.org/title/GnuPG)
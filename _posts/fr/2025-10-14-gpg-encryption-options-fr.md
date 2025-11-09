---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Options de chiffrement GPG expliquées
translated: true
type: note
---

### Explication des options GPG

La commande `gpg` (GNU Privacy Guard) est un outil pour le chiffrement, le déchiffrement et la gestion de clés. Les options que vous avez mentionnées sont couramment utilisées ensemble pour chiffrer des fichiers à un destinataire spécifique. Voici ce que chacune signifie :

- **`--homedir <répertoire>`** : Spécifie le répertoire home de GnuPG (par défaut `~/.gnupg`). C'est là que GPG stocke les porte-clés, les fichiers de configuration et autres données. Cette option remplace la variable d'environnement `GNUPGHOME` et est utile pour isoler les opérations GPG dans un emplacement personnalisé (par exemple, pour plusieurs profils ou pour des raisons de sécurité). Elle doit être fournie sur la ligne de commande.

- **`-e` (ou `--encrypt`)** : Chiffre les données d'entrée en utilisant la cryptographie à clé publique. C'est le mode principal pour le chiffrement asymétrique, où les données sont chiffrées avec la clé publique du destinataire. Elle peut être combinée avec d'autres options comme la signature.

- **`-r <identifiant-utilisateur>` (ou `--recipient <identifiant-utilisateur>`)** : Spécifie le(s) destinataire(s) pour le chiffrement. Le `<identifiant-utilisateur>` peut être un ID de clé, un email ou un nom associé à la clé publique. GPG utilisera la clé publique correspondante pour chiffrer les données. Plusieurs destinataires peuvent être listés pour un chiffrement de groupe.

#### Exemple d'utilisation
Une commande courante combinant ces options pourrait ressembler à :
```
gpg --homedir /chemin/vers/repertoire/personnalise -e -r destinataire@exemple.com fichier_entree.txt
```
Ceci chiffre `fichier_entree.txt` pour `destinataire@exemple.com` en utilisant les clés du répertoire `/chemin/vers/repertoire/personnalise`, produisant `fichier_entree.txt.gpg`.

Pour plus de détails, exécutez `gpg --help` ou consultez la page de manuel.

[ArchWiki: GnuPG](https://wiki.archlinux.org/title/GnuPG)  
[GPG Cheat Sheet](https://irtfweb.ifa.hawaii.edu/~lockhart/gpg/)  
[GPG Command in Linux](https://www.tutorialspoint.com/unix_commands/gpg.htm)
---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Explication du destinataire du chiffrement GPG
translated: true
type: note
---

### Comprendre la commande GPG et l'invite "Destinataire"

La commande que vous exécutez sert à chiffrer un fichier (`inputfile.txt`) avec GnuPG (GPG) :

```
gpg --homedir /chemin/vers/repertoire/personnalise -e -r destinataire@exemple.com --encrypt inputfile.txt
```

- `--homedir /chemin/vers/repertoire/personnalise` : Utilise un répertoire personnalisé pour le porte-clés et la configuration de GPG (au lieu du répertoire par défaut `~/.gnupg`).
- `-e` (ou `--encrypt`) : Demande à GPG de chiffrer le fichier.
- `-r destinataire@exemple.com` : Spécifie le **destinataire** (la personne ou l'entité pour laquelle vous chiffrez). Cela doit être son email, son nom ou l'identifiant de sa clé publique.
- `--encrypt inputfile.txt` : Le fichier à chiffrer (le résultat sera `inputfile.txt.gpg`).

#### Que signifie "Destinataire" ici ?
Dans le chiffrement GPG :
- Le **destinataire** est la personne qui *recevra et déchiffrera* le fichier. Vous chiffrez le fichier en utilisant *sa clé publique*, ainsi seul(e) lui (avec sa clé privée) peut le déchiffrer.
- Ce n'est pas l'"expéditeur" (vous) car le chiffrement protège les données *pour le destinataire*. Votre rôle en tant qu'expéditeur concerne davantage la signature (si vous ajoutez `-s` pour signer), mais ici il s'agit d'un simple chiffrement.

Vous avez raison de dire que c'est pour "envoyer" des données sécurisées, mais la terminologie se concentre sur le destinataire car c'est sa clé qui sécurise l'opération. Voyez cela comme verrouiller une boîte avec le cadenas de quelqu'un d'autre—il/elle est le/la seul(e) à pouvoir l'ouvrir.

#### Pourquoi l'erreur : "You did not specify a user ID. (you may use '-r')" et l'invite ?
Cette invite interactive apparaît parce que :
1. GPG n'a pas trouvé de clé publique correspondant à `destinataire@exemple.com` dans votre porte-clés (dans le homedir personnalisé).
2. L'option `-r` est fournie, mais elle ne correspond pas à une clé valide, donc GPG revient à vous demander de saisir l'identifiant utilisateur manuellement.

L'invite est :
```
Current recipients:
Enter the user ID.  End with an empty line:
```

- **User ID** signifie l'identifiant complet du destinataire, comme `John Doe <destinataire@exemple.com>` ou son empreinte/identifiant de clé (par exemple, `ABCDEF123456`).
- Saisissez-le ligne par ligne si nécessaire (par exemple, nom, email, commentaire), puis appuyez deux fois sur Entrée (ligne vide) pour terminer.

#### Comment résoudre ce problème
1. **Importer d'abord la clé publique du destinataire** (problème le plus courant) :
   - Demandez au destinataire de vous envoyer sa clé publique (exportée via `gpg --export -a son@email.com`).
   - Importez-la : `gpg --homedir /chemin/vers/repertoire/personnalise --import sa-cle-publique.asc`.
   - Puis relancez votre commande.

2. **Si la clé est déjà importée mais ne correspond pas** :
   - Listez les clés : `gpg --homedir /chemin/vers/repertoire/personnalise --list-keys`.
   - Utilisez l'identifiant utilisateur exact de cette liste avec `-r` (par exemple, `-r "John Doe <destinataire@exemple.com>"`).

3. **À l'invite** (comme solution rapide) :
   - Tapez l'identifiant utilisateur complet, par exemple :
     ```
     John Doe
     destinataire@exemple.com
     
     ```
     (La ligne vide termine la saisie.)

#### Pourquoi "Destinataire" et non "Expéditeur" ?
- Le chiffrement est *asymétrique* : Clé publique (n'importe qui peut chiffrer) → Clé privée (seul le propriétaire peut déchiffrer).
- L'expéditeur (vous) chiffre avec la clé **publique** du destinataire.
- Si vous voulez prouver que vous êtes l'expéditeur, ajoutez la signature : `gpg ... -e -r destinataire@exemple.com -s --encrypt inputfile.txt` (utilise *votre* clé privée pour signer).
- "Destinataire" est le terme standard de GPG—il ne s'agit pas de qui envoie, mais de qui reçoit/déchiffre. L'appeler "expéditeur" prêterait à confusion, car les expéditeurs n'ont pas besoin d'une clé pour le chiffrement (seulement pour la signature).

Si cela ne résout pas le problème, partagez le résultat de `--list-keys` (masquez les informations sensibles), et je pourrai vous aider à déboguer !

#### Références
- [GPG Encryption Basics](https://www.gnupg.org/documentation/manuals/gnupg/Encrypting-and-Decrypting.html)
- [GPG Man Page](https://www.gnupg.org/documentation/manuals/gnupg/gpg.html)
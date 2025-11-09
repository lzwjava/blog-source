---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Armure ASCII GPG expliquée
translated: true
type: note
---

Dans GPG (GNU Privacy Guard), « armor » fait référence au format ASCII armor, un format qui encode les données binaires OpenPGP (comme les fichiers chiffrés, les signatures ou les clés) en une représentation textuelle lisible par un humain. Ceci est utile pour transmettre des données via des canaux en texte seul, comme le courrier électronique, sans corruption — de la même manière que fonctionnent uuencode ou base64, mais avec des en-têtes ajoutés (par exemple, « -----BEGIN PGP MESSAGE----- ») et des sommes de contrôle pour l'intégrité.

Vous pouvez l'activer avec l'option `--armor` (ou `-a`) lors de commandes comme le chiffrement (`gpg -a -e fichier.txt`) ou l'exportation de clé (`gpg --armor --export keyid`), ce qui affiche le résultat dans ce format texte « armoré » au lieu du binaire brut.

## Références
- [What is the armored option for in GnuPG?](https://unix.stackexchange.com/questions/623375/what-is-the-armored-option-for-in-gnupg)
- [Exchanging keys - GnuPG](https://www.gnupg.org/gph/en/manual/x56.html)
- [13. ASCII armor - Notes on OpenPGP](https://openpgp.dev/book/armor.html)
- [GPG Input and Output (Using the GNU Privacy Guard)](https://www.gnupg.org/documentation/manuals/gnupg/GPG-Input-and-Output.html)
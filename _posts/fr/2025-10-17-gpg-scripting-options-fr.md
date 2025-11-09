---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Options GPG pour les scripts
translated: true
type: note
---

### Explication des options de commande GPG

Les options `--batch`, `--yes`, `-o` et `--pinentry-mode` sont des indicateurs couramment utilisés avec la commande `gpg` (GNU Privacy Guard) pour des opérations non interactives ou automatisées, telles que le chiffrement, le déchiffrement ou la signature. Voici une explication de chacune :

- **`--batch`** : Active le mode batch, ce qui empêche `gpg` de poser des questions interactives ou d'autoriser des commandes interactives. Ceci est utile pour les scripts ou l'automatisation où la saisie de l'utilisateur n'est pas possible. Il peut être désactivé avec `--no-batch`.

- **`--yes`** : Suppose automatiquement "oui" comme réponse à la plupart des invites de confirmation (par exemple, pour écraser des fichiers). Cela évite d'interrompre l'exécution à cause de questions oui/non.

- **`-o` (ou `--output`)** : Spécifie le fichier de sortie pour l'opération. Il doit être suivi d'un nom de fichier, par exemple `-o output.txt`. Sans cette option, la sortie peut aller vers stdout ou un emplacement par défaut.

- **`--pinentry-mode`** : Contrôle la façon dont la saisie du PIN (invite de phrase de passe) est gérée par l'agent GPG. Il prend une valeur de mode comme `ask` (par défaut : affiche une invite graphique ou console), `loopback` (permet de transmettre les phrases de passe via stdin pour les scripts, sans fenêtre contextuelle), `cancel` (annule les opérations nécessitant un PIN) ou `error` (renvoie une erreur au lieu d'afficher une invite). Cette option est souvent utilisée avec `loopback` dans les scripts batch pour une saisie de phrase de passe sécurisée et non interactive.

Ces options sont fréquemment combinées dans les scripts, par exemple `gpg --batch --yes -o decrypted.txt --pinentry-mode loopback --decrypt encrypted.gpg`, pour une exécution entièrement automatisée.

#### Références
- [Page de manuel GPG](https://linux.die.net/man/1/gpg)
- [Options de l'agent GnuPG](https://www.gnupg.org/documentation/manuals/gnupg/Agent-Options.html)
- [Manuel GnuPG](https://www.gnupg.org/documentation/manuals/gnupg/index.html)
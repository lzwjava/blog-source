---
audio: false
generated: true
lang: fr
layout: post
title: Installation du client Outline sur Ubuntu
translated: true
type: note
---

Oui, vous pouvez installer le client Outline sur Ubuntu, car il s'agit d'une distribution Linux basée sur Debian, et le client Outline est fourni sous forme de paquet Debian, qui est compatible avec Ubuntu. Il existe deux méthodes pour l'installer : la méthode recommandée utilisant le dépôt et une méthode alternative en téléchargeant directement le paquet Debian. Ci-dessous, je vais expliquer comment procéder en utilisant la méthode recommandée du dépôt, qui est préférable car elle s'intègre au gestionnaire de paquets d'Ubuntu, facilitant ainsi la gestion des mises à jour.

### Étapes pour installer le client Outline sur Ubuntu (Méthode recommandée)

Suivez ces étapes pour installer le client Outline sur votre système Ubuntu :

1. **Ouvrir un terminal**  
   Lancez l'application terminal sur votre système Ubuntu. Vous pouvez le faire en recherchant "Terminal" dans le menu des applications ou en appuyant sur `Ctrl + Alt + T`.

2. **Installer la clé du dépôt Outline**  
   Exécutez la commande suivante pour télécharger et ajouter la clé de signature du dépôt aux clés de confiance de votre système. Cela garantit que les paquets provenant du dépôt sont vérifiés pour leur authenticité :
   ```bash
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   ```

3. **Ajouter le dépôt du client Outline**  
   Ajoutez le dépôt du client Outline à la liste des sources de votre système en exécutant cette commande. Cela indique à Ubuntu où trouver le paquet du client Outline :
   ```bash
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```
   - Remarque : La partie `[arch=amd64]` spécifie qu'il s'agit d'un système 64 bits. La plupart des installations Ubuntu modernes sont en 64 bits, mais vous pouvez confirmer l'architecture de votre système en exécutant `uname -m`. Si le résultat est `x86_64`, vous utilisez un système 64 bits et cette commande fonctionnera telle quelle.

4. **Mettre à jour la liste des paquets**  
   Actualisez la liste des paquets de votre système pour inclure le nouveau dépôt Outline ajouté :
   ```bash
   sudo apt update
   ```

5. **Installer le client Outline**  
   Installez la dernière version du client Outline avec cette commande :
   ```bash
   sudo apt install outline-client
   ```

### Post-installation

- **Lancer le client Outline** : Après l'installation, vous pouvez trouver le client Outline dans le menu de vos applications ou le lancer depuis le terminal en tapant `outline-client`.
- **Maintenir à jour** : Pour vérifier et installer les mises à jour, utilisez les commandes de mise à jour standard d'Ubuntu :
  ```bash
  sudo apt update
  sudo apt upgrade
  ```
  Ces commandes mettront à jour tous les paquets installés, y compris le client Outline, puisqu'il est géré via le dépôt. Notez que les mises à jour automatiques intégrées à l'application sont désactivées pour le client Outline sur Linux à partir de la version 1.15, donc s'appuyer sur le gestionnaire de paquets est la meilleure façon de rester à jour.
- **Désinstallation** : Si vous devez supprimer le client Outline, exécutez :
  ```bash
  sudo apt purge outline-client
  ```

### Pourquoi utiliser la méthode recommandée ?

La méthode du dépôt est recommandée car :
- Elle s'intègre au gestionnaire de paquets `apt` d'Ubuntu, vous permettant de mettre à jour le client Outline en même temps que les autres paquets du système.
- Vous n'avez pas besoin de télécharger et d'installer manuellement les nouvelles versions, contrairement à la méthode alternative où vous devriez répéter le processus de téléchargement et d'installation pour chaque mise à jour.

### Hypothèses et exigences

- **Version d'Ubuntu** : Les instructions ne spécifient pas de version minimale d'Ubuntu, mais comme Ubuntu est basée sur Debian et que le paquet cible les systèmes 64 bits, toute version récente d'Ubuntu 64 bits devrait fonctionner. Pour plus de sécurité, assurez-vous que votre système est à jour en exécutant `sudo apt update && sudo apt upgrade` avant de commencer.
- **Architecture** : Ces instructions supposent un système 64 bits (amd64). Si vous utilisez une architecture différente (par exemple, 32 bits ou ARM), cette méthode ne fonctionnera pas telle quelle, et vous devriez vérifier l'existence de paquets alternatifs ou contacter le support Outline.

### Méthode alternative (Optionnelle)

Si vous préférez ne pas ajouter de dépôt, vous pouvez télécharger et installer le paquet Debian directement :
1. Téléchargez le paquet :
   ```bash
   wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
   ```
2. Installez-le :
   ```bash
   sudo apt install ./outline-client.deb
   ```
Cependant, vous devrez répéter manuellement ce processus pour les mises à jour, ce qui est moins pratique.

### Conclusion

En utilisant la méthode recommandée du dépôt, vous pouvez facilement installer et maintenir le client Outline sur Ubuntu. Suivez simplement les étapes ci-dessus, et vous l'aurez opérationnel avec la possibilité de le maintenir à jour sans effort via le gestionnaire de paquets de votre système.
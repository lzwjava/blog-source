---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Configuration du clavier Logitech via Bluetooth en ligne de commande
translated: true
type: note
---

### Prérequis
- Assurez-vous que votre émetteur Bluetooth 5.3 (dongle) est branché sur le port USB 3.0 et reconnu par Ubuntu. Exécutez `lsusb` dans le terminal pour vérifier s'il apparaît (recherchez quelque chose comme "Bluetooth" ou l'ID du vendeur). Sinon, essayez un autre port USB ou redémarrez.
- Installez les outils Bluetooth s'ils ne sont pas déjà présents :
  ```
  sudo apt update
  sudo apt install bluez bluetooth bluez-tools
  ```
- Débloquez Bluetooth si nécessaire :
  ```
  rfkill unblock bluetooth
  ```
- Redémarrez le service Bluetooth :
  ```
  sudo systemctl restart bluetooth
  ```

### Étapes d'appairage avec bluetoothctl (Recommandé pour la CLI)
L'outil `bluetoothctl` est la méthode standard pour gérer Bluetooth sous Linux/Ubuntu. Les claviers Logitech (comme les MX Keys, K380 ou similaires) nécessitent souvent de saisir un code PIN d'appairage sur le clavier physique lui-même.

1. **Ouvrez la console Bluetooth** :
   ```
   bluetoothctl
   ```
   Ceci entre dans un shell interactif (l'invite change en `[bluetooth]#`).

2. **Activez l'adaptateur** :
   ```
   power on
   ```
   (Si le message "No default controller available" apparaît, exécutez `list` pour voir votre adaptateur et `select <MAC_adaptateur>` s'il y en a plusieurs.)

3. **Configurez l'agent d'appairage** :
   ```
   agent on
   default-agent
   ```
   Ceci active la gestion du code PIN et fait de votre session l'agent par défaut pour l'appairage.

4. **Lancez la recherche des appareils** :
   ```
   scan on
   ```
   Gardez cette commande active. Votre clavier Logitech devrait apparaître après ~10-20 secondes (par exemple, sous le nom "Logitech K380" ou similaire, avec une adresse MAC comme `XX:XX:XX:XX:XX:XX`).

5. **Mettez votre clavier Logitech en mode appairage** :
   - Allumez-le (s'il a un interrupteur d'alimentation).
   - Appuyez et maintenez le bouton d'appairage Bluetooth (généralement sur le côté ou le dessus — vériez votre modèle ; pour les modèles multi-appareils comme les MX Keys, maintenez le bouton de canal 1/2/3 enfoncé pendant 3-5 secondes jusqu'à ce que la LED clignote rapidement).
   - S'il s'agit d'un modèle mono-appareil, maintenez le bouton d'appairage principal enfoncé.

6. **Appairez l'appareil** :
   Une fois qu'il apparaît dans la recherche (appuyez sur Entrée pour actualiser), exécutez :
   ```
   pair <ADRESSE_MAC>
   ```
   - Exemple : `pair 12:34:56:78:9A:BC`
   - Ubuntu demandera un code PIN (souvent 0000 ou 1234 pour Logitech — essayez d'abord les valeurs par défaut).
   - **Étape clé pour Logitech** : Tapez le code PIN directement sur le *clavier physique* et appuyez sur Entrée. (Si aucune notification graphique n'apparaît, ceci est crucial — certains utilisateurs signalent qu'il faut activer les notifications système via `gnome-control-center` > Notifications, mais la CLI contourne souvent ce problème.)

7. **Marquez comme approuvé et connectez** :
   ```
   trust <ADRESSE_MAC>
   connect <ADRESSE_MAC>
   ```
   - Ceci permet la connexion automatique lors des utilisations futures.

8. **Quittez la console** :
   ```
   exit
   ```

### Dépannage
- **L'appareil n'apparaît pas dans la recherche** : Assurez-vous que le clavier est en mode appairage (LED clignotante). Exécutez `scan off` puis `scan on` à nouveau. Attendez jusqu'à 30 secondes.
- **L'appairage échoue (ex: "AuthenticationCanceled")** : Supprimez d'abord l'appareil (`remove <MAC>`), puis réessayez. Pour les modèles Logitech récalcitrants, essayez de maintenir le bouton d'appairage plus longtemps ou de basculer les canaux.
- **Aucune demande de code PIN** : Certains claviers s'appairent sans code — passez à l'étape de connexion. Si bloqué, vérifiez les logs : `sudo journalctl -u bluetooth -f` pendant l'appairage.
- **Problèmes d'adaptateur** : Si vous utilisez un dongle USB Bluetooth 5.3, confirmez la prise en charge par le noyau (Ubuntu 22.04+ gère bien BT 5.3). Mettez à jour le noyau si vous êtes sur une ancienne version d'Ubuntu : `sudo apt install linux-generic-hwe-22.04`.
- **Alternative graphique** : Ouvrez Paramètres > Bluetooth, activez-le et appairez depuis là — mais la CLI est plus fiable pour les particularités des appareils Logitech.
- Test : Après l'appairage, tapez dans un terminal. Si cela fonctionne, ajoutez une connexion automatique au démarrage via `bluetoothctl` ou crontab.

Si votre modèle Logitech spécifique (par exemple, MX Keys Mini) présente des problèmes particuliers, fournissez le modèle exact pour des étapes adaptées.

### Références
- [Pairing LOGITECH K380 in Ubuntu 20.04](https://unix.stackexchange.com/questions/590221/pairing-logitech-k380-in-ubuntu-20-04)
- [Logitech MX Keys won't pair with Bluetooth](https://askubuntu.com/questions/1270419/20-04-logitech-mx-keys-wont-pair-with-bluetooth)
- [Pair Logitech MX Keys with Xubuntu via Bluetooth](https://zroupas.github.io/linux/2021/08/25/pair_mxkeys_xubuntu_bt.html)
- [Ubuntu 20.04 cannot pair Bluetooth Keyboard](https://askubuntu.com/questions/1398096/ubuntu-20-04-cannot-pair-bluetooth-keyboard)
---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Résoudre les problèmes d'appairage Bluetooth Logitech
translated: true
type: note
---

### Résolution de l'erreur AuthenticationCanceled

Cette erreur se produit couramment avec les claviers Bluetooth Logitech (votre adresse MAC `F4:73:35:78:28:4E` correspond au préfixe OUI de Logitech) lors de l'appairage sous Ubuntu en raison de délais d'authentification, d'invites de code PIN manquantes ou d'une mauvaise gestion de l'agent dans BlueZ. La brève connexion/déconnexion dans vos logs suggère que le clavier répond mais que le processus expire avant d'être terminé. D'autres appareils (comme `54:2B:FC:F1:1C:D8`) qui apparaissent peuvent causer des interférences—supprimez-les d'abord.

#### Étapes de préparation rapide
1.  **Supprimez tous les appareils appairés** pour éviter les conflits :
    Dans `bluetoothctl`, exécutez `devices` pour les lister, puis `remove <MAC>` pour chacun (par exemple, `remove 54:2B:FC:F1:1C:D8`). Quittez avec `exit`.

2.  **Redémarrez le service Bluetooth** :
    ```
    sudo systemctl restart bluetooth
    sudo systemctl status bluetooth  # Vérifiez qu'il est actif
    ```

3.  **Mettez le clavier en mode appairage** : Appuyez et maintenez le bouton d'appairage (par exemple, le canal Easy-Switch ou le bouton Bluetooth) jusqu'à ce que la LED clignote rapidement. Faites cela à nouveau avant chaque tentative.

#### Étapes d'appairage avancées dans bluetoothctl
Rouvrez `bluetoothctl` et suivez ces étapes **exactement**—la configuration de l'agent est cruciale, et l'étape "trust" (faire confiance) dès le début permet souvent de contourner certains délais d'expiration. Pour les modèles Logitech (par exemple, K380, K480, MX Keys), saisissez n'importe quel code PIN **à l'aveugle** sur le clavier physique (aucun écho à l'écran) immédiatement après la commande `pair`.

1.  **Entrez dans bluetoothctl** :
    ```
    bluetoothctl
    ```

2.  **Allumez et définissez l'agent** :
    ```
    power on
    agent on
    default-agent
    ```

3.  **Scannez et confirmez l'appareil** :
    ```
    scan on
    ```
    Attendez que `F4:73:35:78:28:4E` apparaisse (actualisez avec Entrée si nécessaire). Puis :
    ```
    scan off  # Arrêtez le scan pour vous concentrer
    ```

4.  **Faites confiance à l'appareil** (aide pour l'acceptation automatique lors des reconnexions) :
    ```
    trust F4:73:35:78:28:4E
    ```

5.  **Appairez** :
    ```
    pair F4:73:35:78:28:4E
    ```
    - Si un code PIN/passkey apparaît (par exemple, `[agent] PIN code: 390412` ou `[agent] Passkey: 299595`), **tapez-le immédiatement sur le clavier physique** et appuyez sur Entrée. Faites-le à l'aveugle—même si aucune invite ne semble active.
    - Si aucun code PIN n'apparaît (courant avec certains Logitech), essayez de taper `0000` ou `1234` sur le clavier et appuyez sur Entrée quand même.
    - Surveillez `[CHG] Paired: yes`. S'il se connecte brièvement puis se déconnecte, réexécutez `connect F4:73:35:78:28:4E` juste après.

6.  **Connectez et faites confiance** :
    ```
    connect F4:73:35:78:28:4E
    trust F4:73:35:78:28:4E  # Si ce n'était pas fait plus tôt
    ```

7.  **Quittez et testez** :
    ```
    exit
    ```
    Ouvrez un éditeur de texte ou un terminal—tapez pour vérifier la saisie. Si cela fonctionne, il devrait se reconnecter automatiquement au réveil.

#### Si cela échoue toujours
- **Solution de secours GUI** : Utilisez Paramètres Ubuntu > Bluetooth (activez-le, sélectionnez l'appareil). Cela affiche souvent une invite de code PIN visible. Si l'agent en ligne de commande échoue, le pinentry de l'interface graphique le gère souvent mieux.
- **Nouvel essai du code PIN à l'aveugle** : Même sans code affiché, certains utilisateurs réussissent en tapant `0000` + Entrée juste après `pair`—le clavier s'authentifie silencieusement.
- **Logs pour des indices** : Exécutez `sudo journalctl -u bluetooth -f` dans un autre terminal pendant l'appairage. Cherchez les messages "PIN code" ou "timeout".
- **Mise à jour de BlueZ** : Assurez-vous d'avoir la dernière version (Ubuntu 24.04+ a BlueZ 5.72+ avec un meilleur support Logitech) :
  ```
  sudo apt update && sudo apt upgrade bluez
  ```
- **Particularité du dongle USB** : Votre émetteur BT 5.3 sur USB 3.0 convient, mais testez sur un port USB 2.0—des interférences rares ont été signalées.
- **Spécifique au modèle** : S'il s'agit d'un K480/MX Keys, maintenez le bouton d'appairage enfoncé pendant 5 secondes ou plus. Pour les modèles multi-appareils, passez d'abord sur un canal inutilisé.

Cela devrait résoudre le problème—la plupart des cas Logitech proviennent de l'étape du code PIN à l'aveugle. Si vous partagez votre modèle exact ou les logs complets, je peux affiner davantage.

[Bluetooth Pairing - AuthenticationCanceled (AskUbuntu)](https://askubuntu.com/questions/1373574/bluetooth-pairing-authenticationcanceled)
[[SOLVED] Bluetooth keyboard: Unable to pair (Arch Linux Forums)](https://bbs.archlinux.org/viewtopic.php?id=174239)
[Barely able to pair Logitech K480 on bluez 5.72 (GitHub)](https://github.com/bluez/bluez/issues/654)
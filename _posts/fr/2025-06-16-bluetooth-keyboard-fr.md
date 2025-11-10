---
audio: false
generated: true
lang: fr
layout: post
title: Résoudre les problèmes de connexion du clavier Bluetooth
translated: true
type: note
---

D'après la sortie de `bluetoothctl` affichant `[DEL] Device` lors d'une tentative de connexion, voici une solution précise :

### Solution Immédiate pour le Problème de Suppression de Connexion
1. **Supprimer les enregistrements existants de l'appareil** (essentiel pour les configurations obsolètes) :
   ```bash
   bluetoothctl
   remove F4:73:35:78:28:4E  # Supprimer le clavier
   remove 24:27:30:24:C8:31   # Supprimer un appareil potentiellement interférent
   exit
   ```

2. **Réinitialiser la pile Bluetooth** :
   ```bash
   sudo systemctl stop bluetooth
   sudo rm -rf /var/lib/bluetooth/*
   sudo systemctl start bluetooth
   ```

3. **Réparer en utilisant la séquence correcte** :
   ```bash
   bluetoothctl
   power on
   discoverable on
   pairable on
   agent on  # Activer l'agent de code d'accès
   scan on
   ```
   - **Mettre le K380 en mode appairage** (LED clignotant rapidement)
   - Lorsque le clavier apparaît :
     ```bash
     pair F4:73:35:78:28:4E
     ```
   - **Taper immédiatement le code à 6 chiffres** affiché à l'écran (par exemple, `123456`) **sur le clavier** et appuyer sur Entrée

4. **Se connecter uniquement après un appairage réussi** :
   ```bash
   connect F4:73:35:78:28:4E
   trust F4:73:35:78:28:4E
   scan off
   quit
   ```

### Pourquoi Cela Se Produit
- Le `[DEL] Device` se produit parce que :
  - La pile Bluetooth détecte un échec de connexion et purge l'enregistrement de l'appareil
  - **L'étape d'appairage est manquante** avant la tentative de connexion
  - Possibilité d'interférences RF d'autres appareils (comme l'appareil `midea`)

### Vérifications Critiques Supplémentaires
1. **Vérifier la connexion de l'antenne** :
   - Assurez-vous que les antennes Bluetooth sont bien vissées sur le panneau arrière I/O de votre carte mère MSI

2. **Vérifier les pilotes du noyau** :
   ```bash
   dmesg | grep -i bluetooth
   ```
   Recherchez des erreurs comme `hci0: command timeout` ou `Firmware failed to start`

3. **Mettre à jour le firmware** (si des erreurs de timeout apparaissent) :
   ```bash
   sudo apt install linux-firmware
   ```

4. **Tester avec un environnement minimal** :
   ```bash
   sudo rfkill unblock all
   sudo systemctl stop NetworkManager  # Arrêt temporaire
   sudo systemctl restart bluetooth
   ```

### Si l'Échec Persiste
1. **Méthode d'appairage alternative** (contourner l'agent) :
   ```bash
   echo -e 'remove F4:73:35:78:28:4E\npair F4:73:35:78:28:4E\nconnect F4:73:35:78:28:4E\ntrust F4:73:35:78:28:4E' | bluetoothctl
   ```

2. **Vérifier la batterie du clavier** (essentiel pour Bluetooth) :
   - Remplacer la batterie si la tension est faible (le K380 utilise 2x CR2032)

3. **Test avec un adaptateur Bluetooth USB** :
   - Si le Bluetooth interne est problématique, essayez un adaptateur USB CSR4.0 à 10$

**Indicateurs de succès attendus** :
- Message `Pairing successful`
- `Connection successful` dans bluetoothctl
- `dmesg` affichant `HIDP: Bluetooth HID device driver`

Après l'appairage, votre K380 devrait survivre aux redémarrages. Si les déconnexions se répètent, vérifiez `journalctl -u bluetooth -f` pour des erreurs en temps réel.
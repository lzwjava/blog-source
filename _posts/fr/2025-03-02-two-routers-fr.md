---
audio: false
lang: fr
layout: post
title: Utilisation de deux routeurs
translated: true
---

Pour configurer vos deux routeurs TP-Link AX3000 (TL-XDR 3050) avec votre modem dans la configuration **Modem → Cable → Router1 → Wireless → Router2**, suivez ce guide étape par étape. Votre modem dispose déjà de la fonctionnalité WiFi et d'une adresse IP de `192.168.1.1`. Nous configurerons Router1 comme routeur principal connecté au modem via un câble et Router2 pour étendre le réseau sans fil.

Voici comment procéder :

---

### **Étape 1 : Comprendre la Configuration**
- **Modem** : Fournit l'accès à Internet et dispose de son propre WiFi (IP : `192.168.1.1`).
- **Router1** : Se connectera au modem avec un câble et agira comme routeur principal pour votre réseau.
- **Router2** : Se connectera sans fil à Router1 pour étendre la couverture du réseau.

Vous avez mentionné plusieurs modes (Wired AP Bridge, Wireless AP Bridge, DHCP, Broadband Connect). Nous utiliserons **DHCP** pour Router1 pour obtenir une connexion Internet à partir du modem et **Wireless AP Bridge** (ou un mode similaire comme WDS/Repeater) pour Router2 pour se connecter sans fil à Router1.

---

### **Étape 2 : Configurer Router1**
1. **Connecter Router1 au Modem** :
   - Prenez un câble Ethernet et branchez une extrémité sur un **port LAN** de votre modem.
   - Branchez l'autre extrémité sur le **port WAN (Internet)** de Router1.

2. **Accéder à l'interface Web de Router1** :
   - Connectez un ordinateur ou un smartphone au réseau WiFi par défaut de Router1 (vérifiez l'étiquette sur le routeur pour le SSID et le mot de passe par défaut) ou utilisez un câble Ethernet.
   - Ouvrez un navigateur web et tapez `http://tplinkwifi.net` ou `192.168.0.1` (l'adresse IP par défaut pour les routeurs TP-Link).
   - Connectez-vous avec les identifiants par défaut (généralement `admin` pour le nom d'utilisateur et le mot de passe) sauf si vous les avez modifiés.

3. **Configurer Router1** :
   - **Connexion Internet** :
     - Allez dans **Quick Setup** ou la section **Internet**.
     - Sélectionnez le mode **DHCP**. Cela permet à Router1 d'obtenir automatiquement une adresse IP à partir du modem (probablement dans la plage `192.168.1.x`).
   - **Paramètres WiFi** :
     - Définissez un **SSID** unique (nom du réseau) et un mot de passe fort pour le WiFi de Router1.
     - Enregistrez ces détails, car Router2 en aura besoin pour se connecter sans fil.
   - **Paramètres LAN** :
     - Assurez-vous que l'IP LAN de Router1 est différente de celle du modem. Par défaut, elle est probablement `192.168.0.1`, ce qui est correct puisque le modem est `192.168.1.1`.
     - Confirmez que **DHCP** est activé sur Router1. Cela permet à Router1 d'attribuer des adresses IP (par exemple, `192.168.0.x`) aux appareils connectés, y compris Router2.
   - Enregistrez les paramètres et redémarrez Router1 si nécessaire.

---

### **Étape 3 : Configurer Router2 en Pont Sans Fil**
1. **Accéder à l'interface Web de Router2** :
   - Connectez un ordinateur ou un smartphone au réseau WiFi par défaut de Router2 ou via Ethernet.
   - Ouvrez un navigateur web et tapez `http://tplinkwifi.net` ou `192.168.0.1`.
   - Connectez-vous avec les identifiants par défaut (ou vos identifiants personnalisés).

2. **Configurer Router2 en Mode Pont Sans Fil** :
   - Recherchez un mode comme **Wireless AP Bridge**, **WDS** ou **Repeater** dans les paramètres (probablement sous **Operation Mode** ou **Wireless** settings).
   - Sélectionnez **Wireless AP Bridge** (ou WDS/Repeater si c'est ce qui est disponible).
   - **Se connecter au WiFi de Router1** :
     - Scannez les réseaux disponibles et sélectionnez le SSID de Router1.
     - Entrez le mot de passe WiFi de Router1.
     - Assurez-vous que Router2 utilise le même canal sans fil que Router1 pour la compatibilité (par exemple, si Router1 est sur le Canal 6, définissez Router2 sur le Canal 6).
   - **Paramètres IP LAN** :
     - Changez l'IP LAN de Router2 pour éviter les conflits avec Router1. Par exemple, définissez-la sur `192.168.0.2` (puisque Router1 est probablement `192.168.0.1`).
     - **Désactivez DHCP** sur Router2. Router1 gérera l'attribution des adresses IP pour tous les appareils.
   - Enregistrez les paramètres et redémarrez Router2. Il devrait maintenant se connecter sans fil à Router1.

---

### **Étape 4 : Tester la Configuration**
1. **Vérifier la Connexion de Router2** :
   - Après le redémarrage, vérifiez l'interface de Router2 pour confirmer qu'il est connecté au WiFi de Router1.
2. **Connecter un Appareil à Router2** :
   - Utilisez un smartphone, un ordinateur portable ou un autre appareil pour vous connecter au WiFi de Router2 (il peut utiliser le même SSID que Router1, selon le mode).
   - Vérifiez que l'appareil obtient une adresse IP de Router1 (par exemple, `192.168.0.x`).
   - Testez l'accès à Internet en naviguant sur un site web.

---

### **Résumé de la Configuration Finale**
- **Modem** : IP `192.168.1.1`, fournit Internet et WiFi.
- **Router1** :
  - WAN : Connecté au modem via câble, défini sur **DHCP** (obtient IP du modem, par exemple `192.168.1.x`).
  - LAN : IP `192.168.0.1`, **DHCP activé** pour attribuer des adresses IP aux appareils.
  - WiFi : SSID et mot de passe personnalisés.
- **Router2** :
  - Mode : **Wireless AP Bridge** (ou WDS/Repeater), connecté sans fil au WiFi de Router1.
  - IP LAN : `192.168.0.2`, **DHCP désactivé**.

---

### **Conseils de Dépannage**
- **Router2 ne se connecte pas sans fil** :
  - Vérifiez à nouveau le SSID, le mot de passe et les paramètres de canal de Router1 dans la configuration de Router2.
  - Si **Wireless AP Bridge** n'est pas disponible, essayez le mode **WDS** ou **Repeater**. Consultez le manuel TP-Link AX3000 pour les modes pris en charge.
- **Pas d'Internet sur Router2** :
  - Assurez-vous que le DHCP de Router1 fonctionne et que le DHCP de Router2 est désactivé.
  - Vérifiez que Router2 se connecte correctement à Router1.
- **Problèmes de Double NAT** :
  - Puisque votre modem dispose de WiFi et que Router1 agit comme routeur, vous pourriez avoir un double NAT (modem et Router1 attribuant tous deux des adresses IP). Cela est généralement correct pour une utilisation de base mais pourrait affecter certaines applications (par exemple, le jeu). Si nécessaire, définissez le modem en mode **pont** (consultez le manuel de votre modem), bien que cela puisse désactiver son WiFi.

Avec cette configuration, Router2 étendra votre réseau sans fil à partir de Router1, et les appareils connectés à l'un ou l'autre des routeurs accéderont à Internet via le modem. Faites-moi savoir si vous avez besoin d'une assistance supplémentaire !
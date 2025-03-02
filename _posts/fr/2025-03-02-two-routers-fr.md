---
audio: false
lang: fr
layout: post
title: Utilisation de deux routeurs
translated: true
---

Pour configurer vos deux routeurs TP-Link AX3000 (TL-XDR 3050) avec votre modem dans la configuration **Modem → Cable → Router1 → Wireless → Router2**, suivez ce guide étape par étape. Votre modem dispose déjà de la fonctionnalité WiFi et d'une adresse IP de `192.168.1.1`. Nous allons configurer Router1 comme routeur principal connecté au modem via un câble et Router2 pour étendre le réseau sans fil.

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
   - Prenez un câble Ethernet et branchez une extrémité sur un port **LAN** de votre modem.
   - Branchez l'autre extrémité sur le port **WAN (Internet)** de Router1.

2. **Accéder à l'Interface Web de Router1** :
   - Connectez un ordinateur ou un smartphone au réseau WiFi par défaut de Router1 (vérifiez l'étiquette sur le routeur pour le SSID et le mot de passe par défaut) ou utilisez un câble Ethernet.
   - Ouvrez un navigateur web et tapez `http://tplinkwifi.net` ou `192.168.0.1` (l'IP par défaut pour les routeurs TP-Link).
   - Connectez-vous avec les identifiants par défaut (généralement `admin` pour le nom d'utilisateur et le mot de passe) sauf si vous les avez modifiés.

3. **Configurer Router1** :
   - **Connexion Internet** :
     - Allez dans **Quick Setup** ou la section **Internet**.
     - Sélectionnez le mode **DHCP**. Cela permet à Router1 d'obtenir automatiquement une adresse IP à partir du modem (probablement dans la plage `192.168.1.x`).
   - **Paramètres WiFi** :
     - Définissez un **SSID** unique (nom du réseau) et un mot de passe fort pour le WiFi de Router1.
     - Enregistrez ces détails, car Router2 en aura besoin pour se connecter sans fil.
   - **Paramètres LAN** :
     - Assurez-vous que l'IP LAN de Router1 est différente de l'IP du modem. Par défaut, elle est probablement `192.168.0.1`, ce qui est correct puisque le modem est `192.168.1.1`.
     - Confirmez que **DHCP** est activé sur Router1. Cela permet à Router1 d'attribuer des adresses IP (par exemple, `192.168.0.x`) aux appareils connectés, y compris Router2.
   - Enregistrez les paramètres et redémarrez Router1 si demandé.

---

### **Étape 3 : Configurer Router2 en Pont Sans Fil**
1. **Accéder à l'Interface Web de Router2** :
   - Connectez un ordinateur ou un smartphone au réseau WiFi par défaut de Router2 ou via Ethernet.
   - Ouvrez un navigateur web et tapez `http://tplinkwifi.net` ou `192.168.0.1`.
   - Connectez-vous avec les identifiants par défaut (ou vos identifiants personnalisés).

2. **Configurer Router2 en Mode Pont Sans Fil** :
   - Recherchez un mode comme **Wireless AP Bridge**, **WDS**, ou **Repeater** dans les paramètres (probablement sous **Operation Mode** ou **Wireless** settings).
   - Sélectionnez **Wireless AP Bridge** (ou WDS/Repeater si c'est ce qui est disponible).
   - **Se connecter au WiFi de Router1** :
     - Scannez les réseaux disponibles et sélectionnez le SSID de Router1.
     - Entrez le mot de passe WiFi de Router1.
     - Assurez-vous que Router2 utilise le même canal sans fil que Router1 pour la compatibilité (par exemple, si Router1 est sur le Canal 6, définissez Router2 sur le Canal 6).
   - **Paramètre IP LAN** :
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
  - LAN : IP `192.168.0.1`, **DHCP activé** pour attribuer des IPs aux appareils.
  - WiFi : SSID et mot de passe personnalisés.
- **Router2** :
  - Mode : **Wireless AP Bridge** (ou WDS/Repeater), connecté sans fil au WiFi de Router1.
  - IP LAN : `192.168.0.2`, **DHCP désactivé**.

---

### **Conseils de Dépannage**
- **Router2 ne se connecte pas sans fil** :
  - Vérifiez à nouveau les paramètres SSID, mot de passe et canal de Router1 dans la configuration de Router2.
  - Si **Wireless AP Bridge** n'est pas disponible, essayez le mode **WDS** ou **Repeater**. Référez-vous au manuel TP-Link AX3000 pour les modes pris en charge.
- **Pas d'Internet sur Router2** :
  - Assurez-vous que le DHCP de Router1 fonctionne et que le DHCP de Router2 est désactivé.
  - Vérifiez que Router2 se connecte correctement à Router1.
- **Problèmes de Double NAT** :
  - Puisque votre modem a un WiFi et que Router1 agit comme routeur, vous pourriez avoir un double NAT (modem et Router1 attribuant tous deux des IPs). Cela est généralement correct pour une utilisation de base mais pourrait affecter certaines applications (par exemple, le jeu). Si nécessaire, mettez le modem en mode **pont** (consultez le manuel de votre modem), bien que cela puisse désactiver son WiFi.

Avec cette configuration, Router2 étendra votre réseau sans fil à partir de Router1, et les appareils connectés à l'un ou l'autre routeur accéderont à Internet via le modem. Faites-le moi savoir si vous avez besoin d'une assistance supplémentaire !

---

Si vous décidez d'utiliser une adresse IP fixe (statique) pour le premier routeur (Router1) au lieu de compter sur DHCP, vous devrez configurer manuellement ses paramètres WAN pour communiquer avec votre modem. Voici ce que vous devez configurer pour l'adresse IP, le DNS, le masque de sous-réseau et la passerelle :

---

### **Hypothèses**
- Votre modem a une adresse IP de `192.168.1.1` et utilise le sous-réseau `192.168.1.0/24` (masque de sous-réseau `255.255.255.0`).
- Le modem a une plage DHCP (par exemple, `192.168.1.2` à `192.168.1.100`) qui attribue des adresses IP aux appareils connectés.

Si votre modem utilise une adresse IP ou un sous-réseau différent, ajustez les valeurs en conséquence.

---

### **Paramètres WAN pour Router1**
Ces paramètres configurent comment Router1 se connecte au modem :

1. **Adresse IP**
   - Choisissez une adresse IP statique dans le sous-réseau du modem (`192.168.1.0/24`) mais **en dehors de la plage DHCP du modem** pour éviter les conflits.
   - Exemple : Si la plage DHCP du modem est `192.168.1.2` à `192.168.1.100`, vous pouvez utiliser **`192.168.1.101`**.
   - Cela garantit que Router1 a une adresse fixe unique sur le réseau du modem.

2. **Masque de Sous-Réseau**
   - Définissez-le pour correspondre au masque de sous-réseau du modem, qui est généralement **`255.255.255.0`**.
   - Cela définit la plage du réseau comme `192.168.1.0` à `192.168.1.255`.

3. **Passerelle Par Défaut**
   - Définissez-la sur l'adresse IP du modem, qui est **`192.168.1.1`**.
   - La passerelle est l'appareil (votre modem) que Router1 utilise pour accéder à Internet.

4. **Serveurs DNS**
   - Vous avez deux options :
     - Utiliser l'IP du modem : **`192.168.1.1`**. Cela permet au modem de gérer les requêtes DNS.
     - Utiliser des serveurs DNS publics : **`8.8.8.8`** (Google) et **`8.8.4.4`** (Google secondaire). Ceux-ci sont fiables et souvent plus rapides.
   - Recommandation : Commencez avec `192.168.1.1`. Si vous rencontrez des problèmes DNS, passez à `8.8.8.8` et `8.8.4.4`.

---

### **Exemple de Configuration**
Voici à quoi pourraient ressembler les paramètres WAN de Router1 :

- **Adresse IP** : `192.168.1.101`
- **Masque de Sous-Réseau** : `255.255.255.0`
- **Passerelle Par Défaut** : `192.168.1.1`
- **Serveur DNS** : `192.168.1.1` (ou `8.8.8.8` et `8.8.4.4`)

---

### **Notes Supplémentaires**
- **Vérifiez les Paramètres du Modem** : Connectez-vous à votre modem (généralement à `192.168.1.1`) pour confirmer son IP, son masque de sous-réseau et sa plage DHCP. Ajustez l'IP statique de Router1 si nécessaire.
- **Paramètres LAN pour Router1** : Pour éviter les conflits, configurez le réseau LAN de Router1 sur un sous-réseau différent, comme `192.168.0.1` avec un masque de sous-réseau de `255.255.255.0`. Activez DHCP sur Router1 pour attribuer des IPs (par exemple, `192.168.0.2` à `192.168.0.254`) aux appareils connectés à lui.
- **Test** : Après avoir appliqué ces paramètres, assurez-vous que Router1 peut accéder à Internet. Si ce n'est pas le cas, vérifiez l'IP (pas de conflits), la passerelle et les valeurs DNS.

Cette configuration donne à Router1 une IP fixe sur le réseau du modem, assurant une connectivité constante. Faites-le moi savoir si vous avez besoin d'aide pour des routeurs supplémentaires ou des détails spécifiques sur le modem !
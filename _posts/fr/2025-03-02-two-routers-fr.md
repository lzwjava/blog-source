---
audio: true
generated: false
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
   - Prenez un câble Ethernet et branchez une extrémité sur un port **LAN** de votre modem.
   - Branchez l'autre extrémité sur le port **WAN (Internet)** de Router1.

2. **Accéder à l'Interface Web de Router1** :
   - Connectez un ordinateur ou un smartphone au réseau WiFi par défaut de Router1 (vérifiez l'étiquette sur le routeur pour le SSID et le mot de passe par défaut) ou utilisez un câble Ethernet.
   - Ouvrez un navigateur web et tapez `http://tplinkwifi.net` ou `192.168.0.1` (l'IP par défaut pour les routeurs TP-Link).
   - Connectez-vous avec les identifiants par défaut (généralement `admin` pour les deux identifiants) sauf si vous les avez changés.

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
1. **Accéder à l'Interface Web de Router2** :
   - Connectez un ordinateur ou un smartphone au réseau WiFi par défaut de Router2 ou via Ethernet.
   - Ouvrez un navigateur web et tapez `http://tplinkwifi.net` ou `192.168.0.1`.
   - Connectez-vous avec les identifiants par défaut (ou les vôtres).

2. **Configurer Router2 en Mode Pont Sans Fil** :
   - Recherchez un mode comme **Wireless AP Bridge**, **WDS**, ou **Repeater** dans les paramètres (probablement sous **Operation Mode** ou **Wireless**).
   - Sélectionnez **Wireless AP Bridge** (ou WDS/Repeater si c'est ce qui est disponible).
   - **Se Connecter au WiFi de Router1** :
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
  - WAN : Connecté au modem via câble, défini sur **DHCP** (obtient une IP du modem, par exemple `192.168.1.x`).
  - LAN : IP `192.168.0.1`, **DHCP activé** pour attribuer des IPs aux appareils.
  - WiFi : SSID et mot de passe personnalisés.
- **Router2** :
  - Mode : **Wireless AP Bridge** (ou WDS/Repeater), connecté sans fil au WiFi de Router1.
  - IP LAN : `192.168.0.2`, **DHCP désactivé**.

---

### **Conseils de Dépannage**
- **Router2 Ne Se Connecte Pas Sans Fil** :
  - Vérifiez à nouveau le SSID, le mot de passe et les paramètres de canal de Router1 dans la configuration de Router2.
  - Si **Wireless AP Bridge** n'est pas disponible, essayez le mode **WDS** ou **Repeater**. Consultez le manuel TP-Link AX3000 pour les modes pris en charge.
- **Pas d'Internet sur Router2** :
  - Assurez-vous que le DHCP de Router1 fonctionne et que le DHCP de Router2 est désactivé.
  - Vérifiez que Router2 se connecte correctement à Router1.
- **Problèmes de Double NAT** :
  - Puisque votre modem a un WiFi et que Router1 agit comme routeur, vous pourriez avoir un double NAT (modem et Router1 attribuant tous deux des IPs). Cela est généralement correct pour une utilisation de base mais pourrait affecter certaines applications (par exemple, le jeu). Si nécessaire, définissez le modem en mode **pont** (consultez le manuel de votre modem), bien que cela puisse désactiver son WiFi.

Avec cette configuration, Router2 étendra votre réseau sans fil à partir de Router1, et les appareils connectés à l'un ou l'autre routeur accéderont à Internet via le modem. Faites-moi savoir si vous avez besoin d'une assistance supplémentaire !

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
   - Choisissez une IP statique dans le sous-réseau du modem (`192.168.1.0/24`) mais **en dehors de la plage DHCP du modem** pour éviter les conflits.
   - Exemple : Si la plage DHCP du modem est `192.168.1.2` à `192.168.1.100`, vous pouvez utiliser **`192.168.1.101`**.
   - Cela garantit que Router1 a une adresse fixe unique sur le réseau du modem.

2. **Masque de Sous-Réseau**
   - Définissez-le pour correspondre au masque de sous-réseau du modem, qui est généralement **`255.255.255.0`**.
   - Cela définit la plage du réseau comme `192.168.1.0` à `192.168.1.255`.

3. **Passerelle Par Défaut**
   - Définissez-la sur l'adresse IP du modem, qui est **`192.168.1.1`**.
   - La passerelle est le dispositif (votre modem) que Router1 utilise pour accéder à Internet.

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
- **Vérifier les Paramètres du Modem** : Connectez-vous à votre modem (généralement à `192.168.1.1`) pour confirmer son IP, son masque de sous-réseau et sa plage DHCP. Ajustez l'IP statique de Router1 si nécessaire.
- **Paramètres LAN pour Router1** : Pour éviter les conflits, configurez le réseau LAN de Router1 sur un sous-réseau différent, comme `192.168.0.1` avec un masque de sous-réseau de `255.255.255.0`. Activez DHCP sur Router1 pour attribuer des IPs (par exemple, `192.168.0.2` à `192.168.0.254`) aux appareils connectés à celui-ci.
- **Test** : Après avoir appliqué ces paramètres, assurez-vous que Router1 peut accéder à Internet. Si ce n'est pas le cas, vérifiez l'IP (pas de conflits), la passerelle et les valeurs DNS.

Cette configuration donne à Router1 une IP fixe sur le réseau du modem, assurant une connectivité constante. Faites-moi savoir si vous avez besoin d'aide pour des routeurs supplémentaires ou des détails spécifiques sur le modem !

---

Il semble que vous ayez configuré Router1 avec une IP WAN statique et configuré son LAN avec DHCP, mais votre ordinateur portable ne peut toujours pas se connecter au réseau. Procédons au dépannage étape par étape pour comprendre pourquoi et comment le résoudre.

---

### Étape 1 : Vérifier la Connexion WAN de Router1
Vos paramètres WAN sont :

- **Adresse IP** : `192.168.1.101`
- **Masque de Sous-Réseau** : `255.255.255.0`
- **Passerelle Par Défaut** : `192.168.1.1`
- **Serveur DNS** : `192.168.1.1` (ou `8.8.8.8` et `8.8.4.4`)

Ces paramètres suggèrent que Router1 est connecté à un modem ou un autre routeur avec une IP de `192.168.1.1`. Voici ce qu'il faut vérifier :

- **Accès Internet sur Router1** :
  - Connectez-vous à l'interface web de Router1 (probablement à `192.168.0.1` à partir de vos paramètres LAN ci-dessous).
  - Allez dans la section **Status** ou **WAN** pour voir si Router1 affiche une connexion Internet active. Si ce n'est pas le cas, le problème pourrait être entre Router1 et le modem.

- **Conflit d'IP** :
  - Assurez-vous qu'aucun autre appareil sur le réseau du modem n'utilise `192.168.1.101`. Si la plage DHCP du modem inclut cette IP, cela pourrait causer un conflit. Connectez-vous au modem (à `192.168.1.1`) et vérifiez ses paramètres DHCP ou la liste des appareils connectés. Si `192.168.1.101` est dans la plage DHCP du modem, changez l'IP WAN de Router1 pour quelque chose en dehors de cette plage (par exemple, `192.168.1.200`) ou excluez-la du pool DHCP du modem.

- **Connectivité du Modem** :
  - Confirmez que le câble Ethernet est branché sur le port **LAN** du modem et le port **WAN** de Router1. Si ce n'est pas configuré correctement, Router1 ne se connectera pas à Internet.

---

### Étape 2 : Vérifier les Paramètres LAN et DHCP de Router1
Vos paramètres LAN et DHCP sont :

- **IP LAN** : `192.168.0.1`
- **Masque de Sous-Réseau** : `255.255.255.0`
- **DHCP Activé** : Oui
- **Plage d'Adresses IP** : `192.168.0.2` à `192.168.0.254`
- **Passerelle** : `192.168.0.1`
- **Serveur DNS** : `192.168.0.1`

Cela semble correct, mais vérifions qu'ils fonctionnent :

- **Fonctionnalité DHCP** :
  - Avec DHCP activé, votre ordinateur portable devrait automatiquement obtenir une adresse IP entre `192.168.0.2` et `192.168.0.254`, avec une passerelle de `192.168.0.1`. Si ce n'est pas le cas, DHCP ne fonctionne peut-être pas correctement.

- **Configuration DNS** :
  - Définir le serveur DNS sur `192.168.0.1` signifie que Router1 gère les requêtes DNS pour votre ordinateur portable. Assurez-vous que Router1 est configuré pour transférer ces requêtes à un serveur DNS en amont (comme `192.168.1.1` ou `8.8.8.8`). Cela est généralement automatique, mais double-checkez dans les paramètres de Router1. Alternativement, vous pourriez définir le DNS DHCP directement sur `8.8.8.8` et `8.8.4.4` pour contourner Router1 pour le DNS.

---

### Étape 3 : Tester la Connexion de Votre Ordinateur Portable
Puisque votre ordinateur portable ne se connecte pas, diagnostiquons-le :

- **Type de Connexion** :
  - Utilisez-vous le WiFi ou l'Ethernet ? Si WiFi, assurez-vous de vous connecter au SSID de Router1 (et non au modem). Si Ethernet, confirmez que le câble est branché sur l'un des ports LAN de Router1.

- **Vérifier l'Adresse IP de l'Ordinateur Portable** :
  - Sur votre ordinateur portable, ouvrez un **Invite de Commandes** (Windows) ou un **Terminal** (macOS/Linux) :
    - Windows : Tapez `ipconfig` et appuyez sur Entrée.
    - macOS/Linux : Tapez `ifconfig` ou `ip addr` et appuyez sur Entrée.
  - Recherchez l'adresse IP de votre adaptateur réseau. Elle devrait être quelque chose comme `192.168.0.x` (où `x` est entre 2 et 254), avec un masque de sous-réseau de `255.255.255.0` et une passerelle `192.168.0.1`.
  - **Si Pas d'Adresse IP** :
    - Votre ordinateur portable pourrait ne pas obtenir d'IP de DHCP. Assurez-vous que ses paramètres réseau sont définis sur "Obtenir une adresse IP automatiquement." Essayez de renouveler l'IP :
      - Windows : Exécutez `ipconfig /release` puis `ipconfig /renew`.
    - Si cela échoue toujours, le DHCP de Router1 ou la connexion à celui-ci pourrait être le problème.

- **Ping Router1** :
  - Depuis votre ordinateur portable, exécutez `ping 192.168.0.1`. Si vous obtenez des réponses, votre ordinateur portable est connecté à Router1 mais pourrait ne pas avoir accès à Internet. S'il expire, l'ordinateur portable n'atteint pas Router1.

---

### Étape 4 : Problèmes Courants et Solutions
Voici quelques coupables probables :

- **Problèmes de Câble** :
  - Si vous utilisez Ethernet, essayez un autre câble ou un autre port LAN sur Router1. Un câble ou un port défectueux pourrait empêcher la connectivité.

- **Problèmes WiFi** :
  - Si vous êtes sur WiFi, vérifiez à nouveau le mot de passe et assurez-vous que le WiFi de Router1 est activé. Les interférences de signal ou un SSID mal configuré pourraient également être le problème.

- **Lien Router1-Modem** :
  - Si Router1 n'obtient pas de connexion Internet, le modem pourrait nécessiter des paramètres spécifiques (par exemple, le clonage d'adresse MAC). Consultez le manuel du modem ou ses paramètres pour cela.

- **Double NAT** :
  - Votre configuration a le modem (à `192.168.1.1`) et Router1 (à `192.168.0.1`) agissant tous deux comme routeurs. Cela ne devrait pas bloquer la connectivité de base, mais définir le modem en mode **pont** (si possible) pourrait simplifier les choses.

- **Pare-feu** :
  - Le pare-feu de Router1 pourrait bloquer votre ordinateur portable. Désactivez temporairement toutes les règles de pare-feu personnalisées pour tester.

---

### Étape 5 : Réinitialiser si Nécessaire
Si rien ne fonctionne, réinitialisez Router1 et reconfigurez :

- **Réinitialisation d'Usine** :
  - Appuyez et maintenez le bouton de réinitialisation de Router1 pendant 10 secondes, puis reconfigurez les paramètres WAN et DHCP comme vous l'avez listé.

- **Essayer WAN Dynamique** :
  - Au lieu d'une IP WAN statique, définissez Router1 sur **DHCP** pour voir s'il peut tirer une IP du modem automatiquement. Si cela fonctionne, l'IP statique (`192.168.1.101`) pourrait être le problème.

---

### Conseils Finaux
- **Plage DHCP du Modem** : Confirmez que `192.168.1.101` est en dehors de la plage DHCP du modem pour éviter les conflits.
- **Firmware** : Vérifiez l'interface web de Router1 pour une mise à jour du firmware.
- **Pilotes de l'Ordinateur Portable** : Assurez-vous que les pilotes de l'adaptateur réseau de votre ordinateur portable sont à jour.

Suivez ces étapes, et vous devriez identifier pourquoi votre ordinateur portable ne se connecte pas. Si vous êtes toujours bloqué, faites-moi savoir ce que vous trouvez à chaque étape – je vous aiderai à affiner davantage !
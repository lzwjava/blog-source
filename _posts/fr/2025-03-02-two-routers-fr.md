---
audio: false
generated: true
lang: fr
layout: post
title: Utiliser deux routeurs
translated: true
type: note
---

Pour configurer vos deux routeurs TP-Link AX3000 (TL-XDR 3050) avec votre modem dans la configuration **Modem → Câble → Routeur1 → Sans fil → Routeur2**, suivez ce guide étape par étape. Votre modem dispose déjà d'une fonctionnalité WiFi et d'une adresse IP `192.168.1.1`. Nous configurerons le Routeur1 comme routeur principal connecté au modem via un câble et le Routeur2 pour étendre le réseau sans fil.

Voici comment procéder :

---

### **Étape 1 : Comprendre la configuration**
- **Modem** : Fournit l'accès à Internet et possède son propre WiFi (IP : `192.168.1.1`).
- **Routeur1** : Se connectera au modem avec un câble et agira comme le routeur principal de votre réseau.
- **Routeur2** : Se connectera sans fil au Routeur1 pour étendre la couverture du réseau.

Vous avez mentionné plusieurs modes (Wired AP Bridge, Wireless AP Bridge, DHCP, Broadband Connect). Nous utiliserons **DHCP** pour que le Routeur1 obtienne une connexion Internet depuis le modem et **Wireless AP Bridge** (ou un mode similaire comme WDS/Repeater) pour que le Routeur2 se connecte sans fil au Routeur1.

---

### **Étape 2 : Configurer le Routeur1**
1. **Connecter le Routeur1 au Modem** :
   - Prenez un câble Ethernet et branchez une extrémité dans un **port LAN** de votre modem.
   - Branchez l'autre extrémité dans le **port WAN (Internet)** du Routeur1.

2. **Accéder à l'Interface Web du Routeur1** :
   - Connectez un ordinateur ou un smartphone au réseau WiFi par défaut du Routeur1 (vérifiez l'étiquette sur le routeur pour le SSID et le mot de passe par défaut) ou utilisez un câble Ethernet.
   - Ouvrez un navigateur web et tapez `http://tplinkwifi.net` ou `192.168.0.1` (l'IP par défaut des routeurs TP-Link).
   - Connectez-vous avec les identifiants par défaut (généralement `admin` pour le nom d'utilisateur et le mot de passe) sauf si vous les avez modifiés.

3. **Configurer le Routeur1** :
   - **Connexion Internet** :
     - Allez dans **Quick Setup** ou la section des paramètres **Internet**.
     - Sélectionnez le mode **DHCP**. Cela permet au Routeur1 d'obtenir automatiquement une adresse IP du modem (probablement dans la plage `192.168.1.x`).
   - **Paramètres WiFi** :
     - Définissez un **SSID** (nom du réseau) unique et un **mot de passe** robuste pour le WiFi du Routeur1.
     - Enregistrez ces détails, car le Routeur2 en aura besoin pour se connecter sans fil.
   - **Paramètres LAN** :
     - Assurez-vous que l'IP LAN du Routeur1 est différente de l'IP du modem. Par défaut, c'est probablement `192.168.0.1`, ce qui convient puisque le modem est sur `192.168.1.1`.
     - Confirmez que le **DHCP** est activé sur le Routeur1. Cela permet au Routeur1 d'attribuer des adresses IP (par exemple, `192.168.0.x`) aux appareils qui lui sont connectés, y compris le Routeur2.
   - Enregistrez les paramètres et redémarrez le Routeur1 si vous y êtes invité.

---

### **Étape 3 : Configurer le Routeur2 en mode Pont Sans Fil**
1. **Accéder à l'Interface Web du Routeur2** :
   - Connectez un ordinateur ou un smartphone au réseau WiFi par défaut du Routeur2 ou via Ethernet.
   - Ouvrez un navigateur web et tapez `http://tplinkwifi.net` ou `192.168.0.1`.
   - Connectez-vous avec les identifiants par défaut (ou les vôtres).

2. **Configurer le Routeur2 en mode Pont Sans Fil** :
   - Recherchez un mode comme **Wireless AP Bridge**, **WDS** ou **Repeater** dans les paramètres (probablement sous **Operation Mode** ou **Wireless** settings).
   - Sélectionnez **Wireless AP Bridge** (ou WDS/Repeater si c'est ce qui est disponible).
   - **Se connecter au WiFi du Routeur1** :
     - Scannez les réseaux disponibles et sélectionnez le SSID du Routeur1.
     - Entrez le mot de passe WiFi du Routeur1.
     - Assurez-vous que le Routeur2 utilise le même canal sans fil que le Routeur1 pour la compatibilité (par exemple, si le Routeur1 est sur le Canal 6, réglez le Routeur2 sur le Canal 6).
   - **Paramètre d'IP LAN** :
     - Changez l'IP LAN du Routeur2 pour éviter les conflits avec le Routeur1. Par exemple, réglez-la sur `192.168.0.2` (puisque le Routeur1 est probablement sur `192.168.0.1`).
     - **Désactivez le DHCP** sur le Routeur2. Le Routeur1 gérera l'attribution des IP pour tous les appareils.
   - Enregistrez les paramètres et redémarrez le Routeur2. Il devrait maintenant se connecter sans fil au Routeur1.

---

### **Étape 4 : Tester la configuration**
1. **Vérifier la connexion du Routeur2** :
   - Après le redémarrage, vérifiez l'interface du Routeur2 pour confirmer qu'il est connecté au WiFi du Routeur1.
2. **Connecter un appareil au Routeur2** :
   - Utilisez un smartphone, un ordinateur portable ou un autre appareil pour vous connecter au WiFi du Routeur2 (il peut utiliser le même SSID que le Routeur1, selon le mode).
   - Vérifiez que l'appareil obtient une adresse IP du Routeur1 (par exemple, `192.168.0.x`).
   - Testez l'accès à Internet en naviguant sur un site web.

---

### **Résumé de la configuration finale**
- **Modem** : IP `192.168.1.1`, fournit Internet et le WiFi.
- **Routeur1** :
  - WAN : Connecté au modem via câble, réglé sur **DHCP** (obtient une IP du modem, par exemple `192.168.1.x`).
  - LAN : IP `192.168.0.1`, **DHCP activé** pour attribuer des IP aux appareils.
  - WiFi : SSID et mot de passe personnalisés.
- **Routeur2** :
  - Mode : **Wireless AP Bridge** (ou WDS/Repeater), connecté sans fil au WiFi du Routeur1.
  - IP LAN : `192.168.0.2`, **DHCP désactivé**.

---

### **Conseils de dépannage**
- **Le Routeur2 ne se connecte pas sans fil** :
  - Vérifiez le SSID, le mot de passe et les paramètres de canal du Routeur1 dans la configuration du Routeur2.
  - Si **Wireless AP Bridge** n'est pas disponible, essayez le mode **WDS** ou **Repeater**. Référez-vous au manuel du TP-Link AX3000 pour les modes pris en charge.
- **Pas d'Internet sur le Routeur2** :
  - Assurez-vous que le DHCP du Routeur1 fonctionne et que le DHCP du Routeur2 est désactivé.
  - Vérifiez que le Routeur2 se connecte correctement en pont au Routeur1.
- **Problèmes de Double NAT** :
  - Puisque votre modem a le WiFi et que le Routeur1 agit comme un routeur, vous pourriez avoir un double NAT (le modem et le Routeur1 attribuent tous deux des IP). Ceci est généralement acceptable pour un usage basique mais pourrait affecter certaines applications (par exemple, les jeux). Si nécessaire, réglez le modem en **mode bridge** (consultez le manuel de votre modem), bien que cela puisse désactiver son WiFi.

Avec cette configuration, le Routeur2 étendra votre réseau sans fil depuis le Routeur1, et les appareils connectés à l'un ou l'autre routeur devraient accéder à Internet via le modem. Faites-moi savoir si vous avez besoin d'une aide supplémentaire !

---

Si vous décidez d'utiliser une adresse IP fixe (statique) pour le premier routeur (Routeur1) au lieu de compter sur le DHCP, vous devrez configurer manuellement ses paramètres WAN pour communiquer avec votre modem. Voici ce que vous devez configurer pour l'adresse IP, le DNS, le masque de sous-réseau et la passerelle :

---

### **Hypothèses**
- Votre modem a une adresse IP de `192.168.1.1` et utilise le sous-réseau `192.168.1.0/24` (masque de sous-réseau `255.255.255.0`).
- Le modem a une plage DHCP (par exemple, `192.168.1.2` à `192.168.1.100`) qui attribue des adresses IP aux appareils connectés.

Si votre modem utilise une IP ou un sous-réseau différent, ajustez les valeurs en conséquence.

---

### **Paramètres WAN pour le Routeur1**
Ces paramètres configurent la façon dont le Routeur1 se connecte au modem :

1. **Adresse IP**
   - Choisissez une IP statique dans le sous-réseau du modem (`192.168.1.0/24`) mais **en dehors de la plage DHCP du modem** pour éviter les conflits.
   - Exemple : Si la plage DHCP du modem est `192.168.1.2` à `192.168.1.100`, vous pouvez utiliser **`192.168.1.101`**.
   - Cela garantit que le Routeur1 a une adresse fixe et unique sur le réseau du modem.

2. **Masque de sous-réseau**
   - Réglez-le pour qu'il corresponde au masque de sous-réseau du modem, qui est typiquement **`255.255.255.0`**.
   - Cela définit la plage du réseau de `192.168.1.0` à `192.168.1.255`.

3. **Passerelle par défaut**
   - Réglez-la sur l'adresse IP du modem, qui est **`192.168.1.1`**.
   - La passerelle est l'appareil (votre modem) que le Routeur1 utilise pour accéder à Internet.

4. **Serveurs DNS**
   - Vous avez deux options :
     - Utiliser l'IP du modem : **`192.168.1.1`**. Cela laisse le modem gérer les requêtes DNS.
     - Utiliser des serveurs DNS publics : **`8.8.8.8`** (Google) et **`8.8.4.4`** (secondaire Google). Ils sont fiables et souvent plus rapides.
   - Recommandation : Commencez avec `192.168.1.1`. Si vous rencontrez des problèmes DNS, passez à `8.8.8.8` et `8.8.4.4`.

---

### **Exemple de configuration**
Voici à quoi pourraient ressembler les paramètres WAN de votre Routeur1 :

- **Adresse IP** : `192.168.1.101`
- **Masque de sous-réseau** : `255.255.255.0`
- **Passerelle par défaut** : `192.168.1.1`
- **Serveur DNS** : `192.168.1.1` (ou `8.8.8.8` et `8.8.4.4`)

---

### **Notes supplémentaires**
- **Vérifier les paramètres du modem** : Connectez-vous à votre modem (généralement à `192.168.1.1`) pour confirmer son IP, son masque de sous-réseau et sa plage DHCP. Ajustez l'IP statique du Routeur1 si nécessaire.
- **Paramètres LAN pour le Routeur1** : Pour éviter les conflits, configurez le réseau LAN du Routeur1 sur un sous-réseau différent, comme `192.168.0.1` avec un masque de sous-réseau de `255.255.255.0`. Activez le DHCP sur le Routeur1 pour attribuer des IP (par exemple, `192.168.0.2` à `192.168.0.254`) aux appareils qui lui sont connectés.
- **Test** : Après avoir appliqué ces paramètres, assurez-vous que le Routeur1 peut accéder à Internet. Sinon, vérifiez l'IP (pas de conflits), la passerelle et les valeurs DNS.

Cette configuration donne au Routeur1 une IP fixe sur le réseau du modem, garantissant une connectivité constante. Faites-moi savoir si vous avez besoin d'aide pour des routeurs supplémentaires ou des détails spécifiques au modem !

---

Il semble que vous ayez configuré le Routeur1 avec une IP WAN statique et configuré son LAN avec le DHCP, mais votre ordinateur portable ne peut toujours pas se connecter au réseau. Déboguons cela étape par étape pour déterminer pourquoi et comment le résoudre.

---

### Étape 1 : Vérifier la connexion WAN du Routeur1
Vos paramètres WAN sont :

- **Adresse IP** : `192.168.1.101`
- **Masque de sous-réseau** : `255.255.255.0`
- **Passerelle par défaut** : `192.168.1.1`
- **Serveur DNS** : `192.168.1.1` (ou `8.8.8.8` et `8.8.4.4`)

Ces paramètres suggèrent que le Routeur1 est connecté à un modem ou à un autre routeur avec une IP de `192.168.1.1`. Voici ce qu'il faut vérifier :

- **Accès Internet sur le Routeur1** :
  - Connectez-vous à l'interface web du Routeur1 (probablement à `192.168.0.1` depuis vos paramètres LAN ci-dessous).
  - Allez dans la section **Status** ou **WAN** pour voir si le Routeur1 affiche une connexion Internet active. Sinon, le problème pourrait se situer entre le Routeur1 et le modem.

- **Conflit d'IP** :
  - Assurez-vous qu'aucun autre appareil sur le réseau du modem n'utilise `192.168.1.101`. Si la plage DHCP du modem inclut cette IP, cela pourrait causer un conflit. Connectez-vous au modem (à `192.168.1.1`) et vérifiez ses paramètres DHCP ou la liste des appareils connectés. Si `192.168.1.101` est dans la plage DHCP du modem, changez l'IP WAN du Routeur1 pour une IP en dehors de cette plage (par exemple, `192.168.1.200`) ou excluez-la du pool DHCP du modem.

- **Connectivité du modem** :
  - Confirmez que le câble Ethernet est branché dans le **port LAN** du modem et le **port WAN** du Routeur1. Si ce n'est pas correctement configuré, le Routeur1 ne se connectera pas à Internet.

---

### Étape 2 : Vérifier les paramètres LAN et DHCP du Routeur1
Vos paramètres LAN et DHCP sont :

- **IP LAN** : `192.168.0.1`
- **Masque de sous-réseau** : `255.255.255.0`
- **DHCP Activé** : Oui
- **Plage d'adresses IP** : `192.168.0.2` à `192.168.0.254`
- **Passerelle** : `192.168.0.1`
- **Serveur DNS** : `192.168.0.1`

Ils semblent solides, mais assurons-nous qu'ils fonctionnent :

- **Fonctionnalité DHCP** :
  - Avec le DHCP activé, votre ordinateur portable devrait obtenir automatiquement une adresse IP entre `192.168.0.2` et `192.168.0.254`, avec une passerelle `192.168.0.1`. Si ce n'est pas le cas, le DHCP ne fonctionne peut-être pas correctement.

- **Configuration DNS** :
  - Régler le serveur DNS sur `192.168.0.1` signifie que le Routeur1 gère les requêtes DNS pour votre ordinateur portable. Assurez-vous que le Routeur1 est configuré pour transférer ces requêtes vers un serveur DNS en amont (comme `192.168.1.1` ou `8.8.8.8`). Ceci est généralement automatique, mais vérifiez dans les paramètres du Routeur1. Alternativement, vous pourriez définir le DNS DHCP directement sur `8.8.8.8` et `8.8.4.4` pour contourner le Routeur1 pour le DNS.

---

### Étape 3 : Tester la connexion de votre ordinateur portable
Puisque votre ordinateur portable ne se connecte pas, diagnostiquons-le :

- **Type de connexion** :
  - Utilisez-vous le WiFi ou l'Ethernet ? Si WiFi, assurez-vous que vous vous connectez au SSID du Routeur1 (et non à celui du modem). Si Ethernet, confirmez que le câble est branché dans un des ports LAN du Routeur1.

- **Vérifier l'adresse IP de l'ordinateur portable** :
  - Sur votre ordinateur portable, ouvrez une **Invite de commandes** (Windows) ou un **Terminal** (macOS/Linux) :
    - Windows : Tapez `ipconfig` et appuyez sur Entrée.
    - macOS/Linux : Tapez `ifconfig` ou `ip addr` et appuyez sur Entrée.
  - Recherchez l'adresse IP de votre adaptateur réseau. Elle devrait être quelque chose comme `192.168.0.x` (où `x` est entre 2 et 254), avec un masque de sous-réseau de `255.255.255.0` et une passerelle `192.168.0.1`.
  - **Si aucune adresse IP** :
    - Votre ordinateur portable n'obtient peut-être pas d'IP du DHCP. Assurez-vous que ses paramètres réseau sont réglés sur "Obtenir une adresse IP automatiquement". Essayez de renouveler l'IP :
      - Windows : Exécutez `ipconfig /release` puis `ipconfig /renew`.
    - Si cela échoue encore, le DHCP sur le Routeur1 ou la connexion à celui-ci pourrait être le problème.

- **Ping vers le Routeur1** :
  - Depuis votre ordinateur portable, exécutez `ping 192.168.0.1`. Si vous obtenez des réponses, votre ordinateur portable est connecté au Routeur1 mais n'a peut-être pas accès à Internet. Si cela dépasse le temps imparti, l'ordinateur portable n'atteint pas le Routeur1.

---

### Étape 4 : Problèmes courants et correctifs
Voici quelques causes probables :

- **Problèmes de câble** :
  - Si vous utilisez l'Ethernet, essayez un câble différent ou un autre port LAN sur le Routeur1. Un câble ou un port défectueux pourrait empêcher la connectivité.

- **Problèmes WiFi** :
  - Si vous êtes en WiFi, vérifiez le mot de passe et assurez-vous que le WiFi du Routeur1 est activé. Des interférences de signal ou un SSID mal configuré pourraient également être en cause.

- **Lien Routeur1-Modem** :
  - Si le Routeur1 n'obtient pas de connexion Internet, le modem pourrait nécessiter des paramètres spécifiques (par exemple, le clonage d'adresse MAC). Vérifiez le manuel ou les paramètres du modem pour cela.

- **Double NAT** :
  - Votre configuration a le modem (sur `192.168.1.1`) et le Routeur1 (sur `192.168.0.1`) agissant tous deux comme des routeurs. Cela ne devrait pas bloquer la connectivité basique, mais régler le modem en **mode bridge** (si possible) pourrait simplifier les choses.

- **Pare-feu** :
  - Le pare-feu du Routeur1 pourrait bloquer votre ordinateur portable. Désactivez temporairement toutes les règles de pare-feu personnalisées pour tester.

---

### Étape 5 : Réinitialiser si nécessaire
Si rien ne fonctionne, réinitialisez le Routeur1 et reconfigurez :

- **Réinitialisation d'usine** :
  - Appuyez et maintenez le bouton de réinitialisation du Routeur1 pendant 10 secondes, puis configurez à nouveau les paramètres WAN et DHCP comme vous les avez listés.

- **Essayer le WAN Dynamique** :
  - Au lieu d'une IP WAN statique, réglez le WAN du Routeur1 sur **DHCP** pour voir s'il peut obtenir automatiquement une IP du modem. Si cela fonctionne, l'IP statique (`192.168.1.101`) pourrait être le problème.

---

### Conseils finaux
- **Plage DHCP du modem** : Confirmez que `192.168.1.101` est en dehors de la plage DHCP du modem pour éviter les conflits.
- **Firmware** : Vérifiez dans l'interface web du Routeur1 s'il existe une mise à jour du firmware.
- **Pilotes de l'ordinateur portable** : Assurez-vous que les pilotes de l'adaptateur réseau de votre ordinateur portable sont à jour.

Suivez ces étapes, et vous devriez identifier pourquoi votre ordinateur portable ne se connecte pas. Si vous êtes toujours bloqué, faites-moi savoir ce que vous trouvez à chaque étape — je vous aiderai à affiner le diagnostic !